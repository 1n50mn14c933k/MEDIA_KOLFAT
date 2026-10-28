#!/usr/bin/env python3
"""Multi-platform GitHub release-asset downloads. Public counters, no telemetry."""
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
PLATFORMS = ("windows", "linux", "macos")
LABELS = {"windows": "WINDOWS", "linux": "LINUX", "macos": "macOS"}
COLORS = {"windows": "#e8edf1", "linux": "#ff914d", "macos": "#9ca4ad"}
EXCLUDE = re.compile(r"(?:sha[-_]?256|checksum|checksums|signature|\.sig$|\.asc$|\.sha\d+$|sbom)", re.I)
MAC_HINT = re.compile(r"(?:macos|mac[-_ ]?os|darwin|osx|apple[-_ ]?silicon)", re.I)
LINUX_HINT = re.compile(r"(?:linux|ubuntu|debian|fedora|appimage)", re.I)
WINDOWS_HINT = re.compile(r"(?:windows|win[-_ ]?(?:x64|arm64)|setup)", re.I)


def classify(name, tag=""):
    """Only count binary distribution packages; never checksums or source archives."""
    name = str(name)
    lower = name.lower()
    if EXCLUDE.search(name):
        return None
    # Portable native binaries and OS-specific package formats.
    if lower.endswith((".appimage", ".deb", ".rpm", ".flatpak", ".snap")):
        return "linux"
    if lower.endswith((".exe", ".msi", ".msix", ".msixbundle", ".appx", ".appxbundle")):
        return "windows"
    if lower.endswith((".dmg", ".pkg")):
        return "macos"
    # Generic archives are counted only when the asset or its release explicitly
    # identifies a platform. This avoids treating source-code archives as installers.
    if lower.endswith((".tar.gz", ".tgz", ".zip", ".7z")):
        identifying = name + " " + str(tag)
        found = [p for p, rx in (("macos", MAC_HINT), ("linux", LINUX_HINT),
                                  ("windows", WINDOWS_HINT)) if rx.search(identifying)]
        return found[0] if len(found) == 1 else None
    return None


def collect(releases):
    totals = {p: 0 for p in PLATFORMS}
    assets = []
    for release in releases:
        if release.get("draft"):
            continue
        for asset in release.get("assets", []):
            name = asset.get("name", "")
            platform = classify(name, release.get("tag_name", ""))
            if platform is None:
                continue
            count = asset.get("download_count")
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("Invalid GitHub asset download count: " + str(name))
            identifier = asset.get("id")
            if isinstance(identifier, bool) or not isinstance(identifier, int):
                raise ValueError("Missing numeric GitHub asset ID: " + str(name))
            totals[platform] += count
            assets.append({"id": identifier, "name": str(name), "os": platform,
                           "version": release.get("tag_name", ""), "count": count})
    assets.sort(key=lambda a: (-a["count"], a["os"], a["name"]))
    active = {p: any(a["os"] == p for a in assets) for p in PLATFORMS}
    return {"totals": totals, "assets": assets, "active": active}


def github_releases():
    if os.environ.get("GITHUB_REPOSITORY", REPO).lower() != REPO.lower():
        raise RuntimeError("Unexpected GitHub repository")
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")
    headers = {"User-Agent": "MEDIA-KOLFAT-download-dashboard",
               "Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    all_releases = []
    for page in range(1, 21):
        url = f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}"
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            releases = json.load(response)
        if not isinstance(releases, list):
            raise ValueError("Unexpected GitHub Releases API response")
        all_releases.extend(releases)
        if len(releases) < 100:
            return all_releases
    raise RuntimeError("Release pagination limit reached; refusing partial totals")


def read_history(raw):
    if not raw:
        return []
    version = raw.get("schema_version")
    if version == 1:
        # Historical Windows-only observations are preserved exactly.
        # Other platforms were NOT measured; null is not zero.
        return [{"date": s["date"], "counts": {
            "windows": s["github_exe_downloads"], "linux": None, "macos": None}}
                for s in raw["snapshots"]]
    if version == 2:
        rows = []
        for s in raw["snapshots"]:
            date.fromisoformat(s["date"])
            counts = {p: s["counts"].get(p) for p in PLATFORMS}
            if any(v is not None and
                   (isinstance(v, bool) or not isinstance(v, int) or v < 0)
                   for v in counts.values()):
                raise ValueError("Invalid historical download count")
            rows.append({"date": s["date"], "counts": counts})
        return rows
    raise ValueError("Unknown dashboard history schema; refusing to discard history")


def update_history(history, observation, today):
    rows = [r for r in history if r["date"] != today.isoformat()]
    rows.append({"date": today.isoformat(), "counts": {
        p: observation["totals"][p] if observation["active"][p] else None
        for p in PLATFORMS}})
    rows.sort(key=lambda r: r["date"])
    if len({r["date"] for r in rows}) != len(rows):
        raise ValueError("Duplicate historical dates")
    return rows


def daily_rate(history, platform):
    if len(history) < 2:
        return None
    last = history[-1]
    current = last["counts"].get(platform)
    if current is None:
        return None
    # Find the latest previous measured snapshot, without inventing counts
    # for periods before a platform was tracked.
    previous = next((r for r in reversed(history[:-1])
                     if r["counts"].get(platform) is not None), None)
    if previous is None:
        return None
    elapsed = (date.fromisoformat(last["date"]) -
               date.fromisoformat(previous["date"])).days
    if elapsed <= 0 or current < previous["counts"][platform]:
        return None  # Counter reset or invalid comparison
    return (current - previous["counts"][platform]) / elapsed


def step(peak):
    if peak <= 0:
        return 1
    raw = peak / 4
    scale = 10 ** math.floor(math.log10(raw))
    return next(v * scale for v in (1, 2, 5, 10) if v * scale >= raw)


def draw(history, observation):
    latest = history[-1]
    samples = history[-90:]
    totals, assets, active = (observation[k] for k in ("totals", "assets", "active"))
    overall = sum(totals.values())
    box = ['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="890" '
           'viewBox="0 0 1100 890" role="img" aria-labelledby="dashTitle dashDesc">',
           '<title id="dashTitle">MEDIA KOLFAT | GitHub Package Downloads</title>',
           '<desc id="dashDesc">Real GitHub Release asset download totals and observed rates '
           'for Windows, Linux, and future macOS packages.</desc>',
           '<rect x="1" y="1" width="1098" height="888" rx="20" fill="#0c0c0c" '
           'stroke="#444" stroke-width="2"/>',
           '<text x="38" y="49" fill="#f7f7f7" font-family="Arial,sans-serif" '
           'font-size="25" font-weight="700">MEDIA KOLFAT | GitHub Downloads Dashboard</text>',
           '<text x="1060" y="74" fill="#b3b3b3" text-anchor="end" '
           'font-family="Arial,sans-serif" font-size="13">Official GitHub release assets | Daily updates</text>',
           '<path d="M38 91H1062" stroke="#444"/>',
           '<text x="45" y="123" fill="#c9c9c9" font-family="Arial,sans-serif" '
           'font-size="16">ALL PLATFORMS - TOTAL PACKAGE DOWNLOADS</text>',
           f'<text x="45" y="172" fill="#fff" font-family="Arial,sans-serif" '
           f'font-size="48" font-weight="700">{overall:,}</text>',
           '<text x="285" y="165" fill="#aaa" font-family="Arial,sans-serif" '
           'font-size="14">Each download counts a release asset, not an installation</text>']
    for index, platform in enumerate(PLATFORMS):
        x = 38 + index * 347
        status = active[platform]
        value = f'{totals[platform]:,}' if status else "Not released"
        rate = daily_rate(history, platform) if status else None
        if not status:
            rate_text = "Waiting for first package"
        elif rate is None:
            rate_text = "Daily rate: awaiting 2 observations"
        else:
            rate_text = f"Daily rate: +{rate:,.1f} downloads/day"
        n = sum(a["os"] == platform for a in assets)
        box.extend([
            f'<rect x="{x}" y="195" width="329" height="149" rx="14" fill="#171717" stroke="#555"/>',
            f'<rect x="{x+14}" y="212" width="5" height="22" rx="2" fill="{COLORS[platform]}"/>',
            f'<text x="{x+28}" y="231" fill="#ddd" font-family="Arial,sans-serif" '
            f'font-size="17" font-weight="700">{LABELS[platform]}</text>',
            f'<text x="{x+16}" y="285" fill="#fff" font-family="Arial,sans-serif" '
            f'font-size="{30 if not status else 40}" font-weight="700">{value}</text>',
            f'<text x="{x+16}" y="313" fill="#aeb0b2" font-family="Arial,sans-serif" '
            f'font-size="12">{html.escape(rate_text)}</text>',
            f'<text x="{x+16}" y="332" fill="#aeb0b2" font-family="Arial,sans-serif" '
            f'font-size="11">{"No published package" if not status else str(n) + " downloadable package(s)"}</text>'
        ])
    box.extend([
        '<text x="42" y="386" fill="#eee" font-family="Arial,sans-serif" '
        'font-size="19" font-weight="700">Cumulative downloads by platform</text>',
        '<text x="1052" y="385" fill="#aaa" text-anchor="end" '
        'font-family="Arial,sans-serif" font-size="12">Observed daily snapshots (max 90)</text>'])
    x0,x1,y0,y1=95,1040,415,607
    vals = [v for row in samples for v in row["counts"].values() if v is not None]
    tick = step(max(vals) if vals else 0)
    maximum = tick*4
    def xcoord(i):
        return 560 if len(samples)==1 else x0+(x1-x0)*i/(len(samples)-1)
    def ycoord(v):
        return y1-(y1-y0)*v/maximum
    for i in range(5):
        val=i*tick
        yp=ycoord(val)
        box.append(f'<path d="M{x0} {yp:.1f}H{x1}" stroke="#383838" stroke-dasharray="4 6"/>')
        box.append(f'<text x="83" y="{yp+5:.1f}" text-anchor="end" '
                   f'fill="#aaa" font-family="Arial,sans-serif" font-size="13">{val:,.0f}</text>')
    for platform in PLATFORMS:
        segments=[]
        current=[]
        for i,s in enumerate(samples):
            value=s["counts"].get(platform)
            if value is None:
                if current: segments.append(current)
                current=[]
            else:
                current.append((xcoord(i),ycoord(value)))
        if current:segments.append(current)
        for segment in segments:
            if len(segment)>1:
                pts=" ".join(f"{x:.1f},{y:.1f}" for x,y in segment)
                box.append(f'<polyline points="{pts}" fill="none" '
                           f'stroke="{COLORS[platform]}" stroke-width="3" stroke-linejoin="round"/>')
            for x,y in segment:
                box.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" '
                           f'fill="{COLORS[platform]}"/>')
    indices=sorted({0,len(samples)//2,len(samples)-1})
    for i in indices:
        stamp=date.fromisoformat(samples[i]["date"]).strftime("%d %b")
        box.append(f'<text x="{xcoord(i):.1f}" y="627" text-anchor="middle" '
                   f'fill="#aaa" font-family="Arial,sans-serif" font-size="12">{stamp}</text>')
    for i,p in enumerate(PLATFORMS):
        xx=305+i*180
        box.append(f'<rect x="{xx}" y="647" width="16" height="4" fill="{COLORS[p]}"/>')
        box.append(f'<text x="{xx+25}" y="654" fill="#ddd" '
                   f'font-family="Arial,sans-serif" font-size="13">{LABELS[p]}</text>')
    box.append('<path d="M38 674H1062" stroke="#444"/>')
    box.append('<text x="42" y="703" fill="#eee" font-family="Arial,sans-serif" '
               'font-size="19" font-weight="700">Published package downloads</text>')
    if not assets:
        box.append('<text x="50" y="750" fill="#ccc" font-family="Arial,sans-serif" '
                   'font-size="16">No downloadable application packages found yet</text>')
    else:
        for i,a in enumerate(assets[:4]):
            yy=735+i*29
            name=a["name"]
            if len(name)>71:name=name[:68]+"..."
            display=f'{LABELS[a["os"]]}  |  {name}'
            box.append(f'<text x="50" y="{yy}" fill="#ddd" font-family="Arial,sans-serif" '
                       f'font-size="14">{html.escape(display)}</text>')
            box.append(f'<text x="1038" y="{yy}" fill="#fff" text-anchor="end" '
                       f'font-family="Arial,sans-serif" font-size="15" font-weight="700">{a["count"]:,}</text>')
        if len(assets)>4:
            box.append(f'<text x="50" y="853" fill="#aaa" font-family="Arial,sans-serif" '
                       f'font-size="12">+ {len(assets)-4} additional package(s) included in the totals</text>')
    box.append(f'<text x="42" y="864" fill="#999" font-family="Arial,sans-serif" '
               f'font-size="12">Last snapshot: {html.escape(latest["date"])} UTC  |  '
               'Excludes checksums, source archives and draft releases  |  No in-app tracking</text>')
    box.append('</svg>')
    return "\n".join(box)+"\n"


def main():
    today=datetime.now(timezone.utc).date()
    observation=collect(github_releases())
    old=json.loads(HISTORY.read_text(encoding="utf-8")) if HISTORY.exists() else {}
    history=update_history(read_history(old),observation,today)
    svg=draw(history,observation)
    HISTORY.parent.mkdir(parents=True,exist_ok=True)
    HISTORY.write_text(json.dumps({"schema_version":2,"snapshots":history},indent=2)+"\n",
                       encoding="utf-8")
    SVG.write_text(svg,encoding="utf-8")
    print("GitHub package downloads:",observation["totals"],
          "assets:",len(observation["assets"]),"snapshots:",len(history))


if __name__ == "__main__":
    main()
