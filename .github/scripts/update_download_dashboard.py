#!/usr/bin/env python3
"""README chart from official GitHub release-asset counters. No telemetry."""
import html
import json
import math
import os
import re
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
HISTORY = ROOT / "assets/download-dashboard-history.json"
SVG = ROOT / "assets/download-dashboard.svg"
REPO = "1n50mn14c933k/MEDIA_KOLFAT"
PATTERN = re.compile(r"MEDIA_KOLFAT_[0-9.]+_Setup\.exe", re.I)


def github_downloads():
    if os.environ.get("GITHUB_REPOSITORY", REPO).lower() != REPO.lower():
        raise RuntimeError("Unexpected repository")
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    headers = {"User-Agent": "MEDIA-KOLFAT-dashboard",
               "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    total = 0
    for page in range(1, 11):
        url = f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}"
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            releases = json.load(response)
        if not isinstance(releases, list):
            raise RuntimeError("GitHub API did not return releases")
        for release in releases:
            if release.get("draft") or release.get("prerelease"):
                continue
            for asset in release.get("assets", []):
                if PATTERN.fullmatch(asset.get("name", "")):
                    count = asset.get("download_count")
                    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                        raise ValueError("Invalid asset download count")
                    total += count
        if len(releases) < 100:
            return total
    raise RuntimeError("Too many releases; refusing incomplete totals")


def tick_step(peak):
    raw = max(1, peak) / 4
    mag = 10 ** math.floor(math.log10(raw))
    return next(m * mag for m in (1, 2, 5, 10) if m * mag >= raw)


def draw(history):
    latest = history[-1]
    samples = history[-90:]
    values = [r["github_exe_downloads"] for r in samples]
    tick = tick_step(max(values))
    maximum = tick * 4
    x0, x1, y0, y1 = 95, 1000, 288, 527

    def x(i):
        return 548 if len(samples) == 1 else x0 + (x1-x0)*i/(len(samples)-1)

    def y(v):
        return y1 - (y1-y0)*v/maximum

    def fmt(s):
        return html.escape(str(s))

    tag = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="690" viewBox="0 0 1100 690" role="img">',
        '<title>MEDIA KOLFAT distribution dashboard</title>',
        '<rect x="1" y="1" width="1098" height="688" rx="20" fill="#0b0d0e" stroke="#363b3e" stroke-width="2"/>',
        '<text x="42" y="48" fill="#f2f3f4" font-family="Arial,sans-serif" font-size="23" font-weight="700">MEDIA KOLFAT | GitHub Downloads</text>',
        '<text x="1050" y="47" fill="#a8b0b5" font-family="Arial,sans-serif" font-size="14" text-anchor="end">Actual data · Daily refresh</text>',
        '<path d="M42 67H1058 M42 224H1058" stroke="#303537"/>',
        '<text x="55" y="109" fill="#c0c6ca" font-family="Arial,sans-serif" font-size="18">GitHub EXE downloads</text>',
        '<text x="590" y="109" fill="#c0c6ca" font-family="Arial,sans-serif" font-size="18">Official release assets</text>',
        '<text x="590" y="155" fill="#e9f9eb" font-family="Arial,sans-serif" font-size="19">Automatic daily snapshot</text>',
        f'<text x="55" y="171" fill="#e9f9eb" font-family="Arial,sans-serif" font-size="53" font-weight="700">{latest["github_exe_downloads"]:,}</text>',
        '<circle cx="61" cy="198" r="6" fill="#7ed48a"/>',
        '<text x="76" y="203" fill="#a3b5a8" font-family="Arial,sans-serif" font-size="14">Published GitHub installer assets</text>',
        '<text x="55" y="263" fill="#e0e4e6" font-family="Arial,sans-serif" font-size="17" font-weight="600">Download history</text>',
        '<text x="1040" y="263" text-anchor="end" fill="#9ea5aa" font-family="Arial,sans-serif" font-size="13">Observed daily snapshots</text>'
    ]
    for i in range(5):
        v = i*tick
        pos = y(v)
        tag.append(f'<path d="M{x0} {pos:.1f}H{x1}" stroke="#373c3e" stroke-dasharray="4 5"/>')
        tag.append(f'<text x="80" y="{pos+5:.1f}" text-anchor="end" fill="#a5adb1" font-family="Arial,sans-serif" font-size="14">{fmt(f"{v:,.0f}")}</text>')
    pts = " ".join(f"{x(i):.1f},{y(r['github_exe_downloads']):.1f}" for i,r in enumerate(samples))
    if len(samples) > 1:
        tag.append(f'<polyline points="{pts}" fill="none" stroke="#7ed48a" stroke-width="3" stroke-linejoin="round"/>')
    for i,r in enumerate(samples):
        tag.append(f'<circle cx="{x(i):.1f}" cy="{y(r["github_exe_downloads"]):.1f}" r="5" fill="#7ed48a" stroke="#dceee0" stroke-width="1.4"/>')
    positions = sorted(set((0, len(samples)//3, (2*len(samples))//3, len(samples)-1)))
    for i in positions:
        dt = date.fromisoformat(samples[i]["date"])
        tag.append(f'<text x="{x(i):.1f}" y="556" text-anchor="middle" fill="#b0b7bb" font-family="Arial,sans-serif" font-size="13">{fmt(dt.strftime("%d %b"))}</text>')
    if len(samples)==1:
        tag.append('<text x="550" y="320" text-anchor="middle" fill="#b3b9bd" font-family="Arial,sans-serif" font-size="15">Trend appears as new daily snapshots are collected</text>')
    tag += [
        '<circle cx="465" cy="593" r="6" fill="#7ed48a"/>',
        '<text x="481" y="598" fill="#d7dcdf" font-family="Arial,sans-serif" font-size="15">GitHub EXE downloads</text>',
        f'<text x="42" y="635" fill="#adb3b7" font-family="Arial,sans-serif" font-size="14">Last observation: {fmt(date.fromisoformat(latest["date"]).strftime("%d %b %Y"))} UTC · Official GitHub release asset counters</text>',
        '<text x="42" y="664" fill="#adb3b7" font-family="Arial,sans-serif" font-size="14">Download counts are not confirmed installations. No application tracking or user analytics.</text>',
        '</svg>'
    ]
    return "\n".join(tag) + "\n"


def main():
    today = datetime.now(timezone.utc).date()
    github = github_downloads()
    history = []
    if HISTORY.exists():
        old = json.loads(HISTORY.read_text(encoding="utf-8"))
        if old.get("schema_version") != 1:
            raise ValueError("Unknown history schema")
        history = [{"date": row["date"], "github_exe_downloads": row["github_exe_downloads"]}
                   for row in old["snapshots"]]
    history = [x for x in history if x["date"] != today.isoformat()]
    history.append({"date": today.isoformat(), "github_exe_downloads": github})
    history.sort(key=lambda x: x["date"])
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    HISTORY.write_text(json.dumps({"schema_version": 1, "snapshots": history}, indent=2) + "\n", encoding="utf-8")
    SVG.write_text(draw(history), encoding="utf-8")
    print(f"GitHub installer downloads: {github}; snapshots: {len(history)}")


if __name__ == "__main__":
    main()
