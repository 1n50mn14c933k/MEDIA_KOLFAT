#!/usr/bin/env python3
"""Publish factual MEDIA KOLFAT GitHub traffic badges for the previous complete UTC week.

Both metrics come from the SAME GitHub Traffic API weekly bucket. Do not sum
daily uniques or infer visitors from page views. No website/download changes.
"""
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

REPO = "1n50mn14c933k/MEDIA_KOLFAT"
OUTPUT = Path("assets/repository-visitors.json")
API_URL = "https://api.github.com/repos/" + REPO + "/traffic/views?per=week"


def previous_complete_week(now):
    today = now.astimezone(timezone.utc).date()
    this_monday = today - timedelta(days=today.weekday())
    return this_monday - timedelta(days=7), this_monday - timedelta(days=1)


def weekly_metrics(payload, week_start):
    """Use native GitHub weekly count/uniques. Missing data stays unavailable."""
    if not isinstance(payload, dict) or not isinstance(payload.get("views"), list):
        raise ValueError("Invalid GitHub weekly traffic response")
    match = next((row for row in payload["views"]
                  if isinstance(row, dict)
                  and str(row.get("timestamp", ""))[:10] == week_start.isoformat()), None)
    if match is None:
        return {"unique_visitors": None, "views": None}
    views, visitors = match.get("count"), match.get("uniques")
    if (type(views) is not int or type(visitors) is not int
            or views < 0 or visitors < 0 or visitors > views):
        raise ValueError("Invalid GitHub weekly traffic counters")
    return {"unique_visitors": visitors, "views": views}


def fetch_weekly_traffic(token):
    request = Request(API_URL, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "User-Agent": "media-kolfat-weekly-repository-traffic",
    })
    try:
        with urlopen(request, timeout=25) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"GitHub Traffic API returned HTTP {exc.code}") from None
    except URLError:
        raise RuntimeError("Could not reach GitHub Traffic API") from None


def build_snapshot(now, weekly_payload):
    monday, sunday = previous_complete_week(now)
    return {
        "schema_version": 2,
        "repository": REPO,
        "generated_at_utc": now.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "weekly": {
            "week_start": monday.isoformat(),
            "week_end": sunday.isoformat(),
            **weekly_metrics(weekly_payload, monday),
        },
    }


def render_badge(label, metric, week_start, week_end, target):
    """Create monochrome 370x32 badge; unavailable data must never appear as zero."""
    if metric is not None and (type(metric) is not int or metric < 0):
        raise ValueError("Invalid badge metric")
    value = "—" if metric is None else f"{metric:,}"
    accessible = escape(f"{label}: {value} (previous completed UTC week {week_start} to {week_end})")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="370" height="32" viewBox="0 0 370 32" role="img" aria-label="{accessible}">
  <title>{accessible}</title>
  <rect width="370" height="32" rx="6" fill="#171717"/>
  <rect x="306" width="64" height="32" rx="6" fill="#3b3b3b"/>
  <text x="14" y="21" fill="#e7e7e7" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700">{escape(label)}</text>
  <text x="338" y="21" text-anchor="middle" fill="#ffffff" font-family="Arial,Helvetica,sans-serif" font-size="16" font-weight="700">{escape(value)}</text>
</svg>
"""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(svg, encoding="utf-8")


def main():
    token = os.getenv("KOLFAT_TRAFFIC_READ_TOKEN", "").strip()
    if not token:
        raise SystemExit("KOLFAT_TRAFFIC_READ_TOKEN missing: refusing to publish guessed data")
    result = build_snapshot(datetime.now(timezone.utc), fetch_weekly_traffic(token))
    weekly = result["weekly"]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_badge("Unique GitHub repository visitors", weekly["unique_visitors"],
                 weekly["week_start"], weekly["week_end"], Path("assets/repository-visitors-weekly.svg"))
    render_badge("GitHub repository page views", weekly["views"],
                 weekly["week_start"], weekly["week_end"], Path("assets/repository-pageviews-weekly.svg"))
    print("Verified previous UTC week:", weekly["week_start"], "through", weekly["week_end"],
          "; unique visitors:", weekly["unique_visitors"], "; page views:", weekly["views"])


if __name__ == "__main__":
    main()
