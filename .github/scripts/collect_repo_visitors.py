#!/usr/bin/env python3
"""Publish exact GitHub-native rolling 14-day repository traffic counters.

Use the API's top-level 'count' (views) and 'uniques' (unique visitors).
Never sum daily unique visitors: one visitor can appear on multiple days.
The visible 14-day period is inclusive of the snapshot's current UTC date.
"""
import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

REPO = "1n50mn14c933k/MEDIA_KOLFAT"
OUTPUT = Path("assets/repository-visitors.json")
# Query native daily granularity to avoid relying on weekly-bucket behavior.
# Totals are taken from API top-level keys, never aggregated daily buckets.
API_URL = "https://api.github.com/repos/" + REPO + "/traffic/views?per=day"


def rolling_14_day_window(now):
    """GitHub's rolling 14-day reporting interval ending today in UTC."""
    if now.tzinfo is None:
        raise ValueError("Snapshot time must include a timezone")
    end = now.astimezone(timezone.utc).date()
    return end - timedelta(days=13), end


def traffic_metrics(payload):
    """Validate GitHub-native 14-day totals; never add daily unique counts."""
    if not isinstance(payload, dict) or not isinstance(payload.get("views"), list):
        raise ValueError("Invalid GitHub repository traffic response")
    views, uniques = payload.get("count"), payload.get("uniques")
    if (type(views) is not int or type(uniques) is not int
            or views < 0 or uniques < 0 or uniques > views):
        raise ValueError("Invalid GitHub rolling 14-day totals")
    return {"unique_visitors": uniques, "views": views}


def fetch_rolling_traffic(token):
    request = Request(API_URL, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
        "User-Agent": "media-kolfat-14-day-repository-traffic",
    })
    try:
        with urlopen(request, timeout=25) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"GitHub Traffic API returned HTTP {exc.code}") from None
    except URLError:
        raise RuntimeError("Could not reach GitHub Traffic API") from None


def build_snapshot(now, payload):
    start, end = rolling_14_day_window(now)
    return {
        "schema_version": 3,
        "repository": REPO,
        "generated_at_utc": now.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "rolling_14_days": {
            "start_date": start.isoformat(),
            "end_date": end.isoformat(),
            **traffic_metrics(payload),
        },
    }


def format_period(start_iso, end_iso):
    """Human-readable date range in UTC, including cross-year periods."""
    from datetime import date
    start, end = date.fromisoformat(start_iso), date.fromisoformat(end_iso)
    if (end - start).days != 13:
        raise ValueError("Expected exactly 14 inclusive UTC dates")
    if start.year == end.year:
        return f"{start.day} {start:%b} – {end.day} {end:%b} {end.year} · UTC"
    return f"{start.day} {start:%b} {start.year} – {end.day} {end:%b} {end.year} · UTC"


def render_badge(label, metric, start_iso, end_iso, target):
    """Render a 370×48 monochrome badge with honest UTC dates."""
    if metric is not None and (type(metric) is not int or metric < 0):
        raise ValueError("Invalid traffic badge metric")
    value = "—" if metric is None else f"{metric:,}"
    period = escape(format_period(start_iso, end_iso))
    accessible = escape(f"{label}: {value} (last 14 days, {start_iso} to {end_iso} UTC)")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="370" height="48" viewBox="0 0 370 48" role="img" aria-label="{accessible}">
  <title>{accessible}</title>
  <rect width="370" height="48" rx="6" fill="#171717"/>
  <rect x="306" width="64" height="48" rx="6" fill="#3b3b3b"/>
  <text x="14" y="19" fill="#e7e7e7" font-family="Arial,Helvetica,sans-serif" font-size="12" font-weight="700">{escape(label)}</text>
  <text x="14" y="36" fill="#bdbdbd" font-family="Arial,Helvetica,sans-serif" font-size="11">{period}</text>
  <text x="338" y="29" text-anchor="middle" fill="#ffffff" font-family="Arial,Helvetica,sans-serif" font-size="16" font-weight="700">{escape(value)}</text>
</svg>
"""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(svg, encoding="utf-8")



BADGE_ASSETS = ("repository-visitors-weekly.svg", "repository-pageviews-weekly.svg")


def readme_with_fresh_badge_urls(text, generated_at_utc):
    """Force GitHub's image proxy to fetch each newly generated badge.

    Filenames stay stable for external links, but README image source URLs get
    a unique query string for every successful verified collection.
    """
    stamp = re.fullmatch(r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z", generated_at_utc)
    if not stamp:
        raise ValueError("Invalid verified UTC collection timestamp")
    version = "".join(stamp.groups()) + "Z"
    updated = text
    for asset in BADGE_ASSETS:
        pattern = r'(src="assets/' + re.escape(asset) + r')(?:\\?v=[0-9TZ]+)?(")'
        matches = re.findall(pattern, updated)
        if len(matches) != 1:
            raise ValueError("Expected exactly one README image reference to " + asset)
        updated = re.sub(pattern, lambda m: m.group(1) + "?v=" + version + m.group(2), updated, count=1)
    return updated


def refresh_readme_badge_urls(generated_at_utc, path=Path("README.md")):
    current = path.read_text(encoding="utf-8")
    changed = readme_with_fresh_badge_urls(current, generated_at_utc)
    if changed != current:
        path.write_text(changed, encoding="utf-8")


def main():
    token = os.getenv("KOLFAT_TRAFFIC_READ_TOKEN", "").strip()
    if not token:
        raise SystemExit("KOLFAT_TRAFFIC_READ_TOKEN missing: refusing to publish guessed data")
    result = build_snapshot(datetime.now(timezone.utc), fetch_rolling_traffic(token))
    data = result["rolling_14_days"]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Keep existing filename paths for GitHub README image-link compatibility.
    render_badge("Unique GitHub repository visitors", data["unique_visitors"],
                 data["start_date"], data["end_date"], Path("assets/repository-visitors-weekly.svg"))
    render_badge("GitHub repository page views", data["views"],
                 data["start_date"], data["end_date"], Path("assets/repository-pageviews-weekly.svg"))
    refresh_readme_badge_urls(result["generated_at_utc"])
    print("Verified rolling 14 days:", data["start_date"], "through", data["end_date"],
          "; unique visitors:", data["unique_visitors"], "; page views:", data["views"])


if __name__ == "__main__":
    main()
