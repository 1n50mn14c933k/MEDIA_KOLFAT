#!/usr/bin/env python3
"""Archive factual MEDIA KOLFAT GitHub repository visitor counts.

Daily = completed UTC day. Weekly = preceding completed Monday-Sunday UTC week.
Weekly unique visitors are GitHub's own week aggregate, NEVER summed daily uniques.
Requires a read-only fine-grained token with MEDIA_KOLFAT Administration: Read.
"""
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

REPO = "1n50mn14c933k/MEDIA_KOLFAT"
OUTPUT = Path("assets/repository-visitors.json")
URL = "https://api.github.com/repos/" + REPO + "/traffic/views"


def periods(now):
    today = now.astimezone(timezone.utc).date()
    yesterday = today - timedelta(days=1)
    this_monday = today - timedelta(days=today.weekday())
    last_monday = this_monday - timedelta(days=7)
    last_sunday = this_monday - timedelta(days=1)
    return yesterday, last_monday, last_sunday


def select_period(payload, field, date):
    """Use GitHub's native unique count; a missing bucket remains unknown."""
    if not isinstance(payload, dict) or not isinstance(payload.get(field), list):
        raise ValueError("Invalid GitHub traffic response")
    match = next((row for row in payload[field]
                  if isinstance(row, dict) and str(row.get("timestamp", ""))[:10] == date.isoformat()), None)
    if match is None:
        return {"unique_visitors": None, "views": None}
    count = match.get("count")
    unique = match.get("uniques")
    if (type(count) is not int or type(unique) is not int
            or count < 0 or unique < 0 or unique > count):
        raise ValueError("Invalid visitor totals from GitHub")
    return {"unique_visitors": unique, "views": count}


def get_views(token, per):
    req = Request(URL + "?per=" + per, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "User-Agent": "media-kolfat-repository-visitor-collector",
    })
    try:
        with urlopen(req, timeout=25) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"GitHub traffic API denied request (HTTP {exc.code})") from None
    except URLError:
        raise RuntimeError("Could not reach the GitHub traffic API") from None


def build_snapshot(now, daily_response, weekly_response):
    yesterday, previous_monday, previous_sunday = periods(now)
    return {
        "schema_version": 1,
        "repository": REPO,
        "generated_at_utc": now.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "daily": {"date": yesterday.isoformat(),
                  **select_period(daily_response, "views", yesterday)},
        "weekly": {"week_start": previous_monday.isoformat(),
                   "week_end": previous_sunday.isoformat(),
                   **select_period(weekly_response, "views", previous_monday)},
    }


def main():
    token = os.getenv("KOLFAT_TRAFFIC_READ_TOKEN", "").strip()
    if not token:
        raise SystemExit("KOLFAT_TRAFFIC_READ_TOKEN is missing; no visitor totals published.")
    now = datetime.now(timezone.utc)
    daily = get_views(token, "day")
    weekly = get_views(token, "week")
    result = build_snapshot(now, daily, weekly)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Published repository visitor snapshot for", result["daily"]["date"],
          "and", result["weekly"]["week_start"], "through", result["weekly"]["week_end"],
          "(UTC); unavailable periods remain null.")


if __name__ == "__main__":
    main()
