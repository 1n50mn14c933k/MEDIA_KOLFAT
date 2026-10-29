#!/usr/bin/env python3
"""Independent check: failed updater, corrupt dashboard, or refresh older than 48h."""
import argparse
import json
import os
from datetime import datetime, date, time, timedelta, timezone
from pathlib import Path
from urllib.request import Request, urlopen

REPO="1n50mn14c933k/MEDIA_KOLFAT"
ROOT=Path(__file__).resolve().parents[2]

def evaluate(history, svg, runs, now):
    errors=[]
    observed=None
    latest_date=None
    latest_run=None
    try:
        if history["schema_version"]!=2: raise ValueError("Unexpected history schema")
        snaps=history["snapshots"]
        if not snaps: raise ValueError("No observations")
        dates=[x["date"] for x in snaps]
        if dates!=sorted(set(dates)): raise ValueError("Unsorted/duplicate observations")
        latest_date=date.fromisoformat(dates[-1])
        for osname in ("windows","linux","macos"):
            val=snaps[-1]["counts"][osname]
            if val is not None and (type(val) is not int or val<0):
                raise ValueError("Invalid "+osname+" counter")
        stamp=history.get("last_checked_at_utc")
        observed=datetime.fromisoformat(stamp.replace("Z","+00:00")) if stamp else datetime.combine(latest_date,time.max,timezone.utc)
        if observed.tzinfo is None: raise ValueError("Refresh timestamp without timezone")
        observed=observed.astimezone(timezone.utc)
        if stamp and observed.date()!=latest_date: errors.append("Refresh timestamp and snapshot date disagree")
        if now-observed>timedelta(hours=48):
            errors.append("Latest dashboard refresh is %.1f hours old (limit 48h)"%((now-observed).total_seconds()/3600))
        if observed-now>timedelta(minutes=10): errors.append("Refresh timestamp is in the future")
    except (KeyError,ValueError,TypeError,AttributeError,IndexError) as exc:
        errors.append("Missing or malformed download history: "+str(exc))
    if not svg: errors.append("Dashboard SVG missing")
    elif latest_date and ("Last snapshot: "+latest_date.isoformat()+" UTC") not in svg:
        errors.append("SVG date differs from latest dashboard JSON")
    if not isinstance(runs,list):
        errors.append("GitHub updater workflow status unavailable")
    else:
        completed=[r for r in runs if isinstance(r,dict) and r.get("head_branch")=="main" and r.get("status")=="completed"]
        completed.sort(key=lambda x:x.get("created_at") or "",reverse=True)
        if not completed: errors.append("No completed dashboard updater workflow")
        else:
            latest_run=completed[0]
            if latest_run.get("conclusion")!="success":
                errors.append("Last completed dashboard updater failed: "+str(latest_run.get("conclusion")))
    return {"healthy":not errors,"reasons":errors,
            "checked_at":now.isoformat(timespec="seconds"),
            "last_refresh":observed.isoformat(timespec="seconds") if observed else None,
            "snapshot_date":latest_date.isoformat() if latest_date else None,
            "updater_url":latest_run.get("html_url") if latest_run else None}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--json-out",required=True)
    parser.add_argument("--issue-out",required=True)
    args=parser.parse_args()
    failures=[]
    history=svg=runs=None
    try: history=json.loads((ROOT/"assets/download-dashboard-history.json").read_text(encoding="utf8"))
    except Exception as e: failures.append("History file unreadable: "+str(e))
    try: svg=(ROOT/"assets/download-dashboard.svg").read_text(encoding="utf8")
    except Exception as e: failures.append("Chart unreadable: "+str(e))
    try:
        token=os.environ["GH_TOKEN"]
        if os.environ.get("GITHUB_REPOSITORY",REPO)!=REPO:
            raise ValueError("Unexpected repository")
        url="https://api.github.com/repos/"+REPO+"/actions/workflows/update-download-dashboard.yml/runs?branch=main&per_page=25"
        headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json",
                 "X-GitHub-Api-Version":"2022-11-28","User-Agent":"KOLFAT-Dashboard-Monitor"}
        with urlopen(Request(url,headers=headers),timeout=30) as reply:
            runs=json.load(reply)["workflow_runs"]
    except Exception as e: failures.append("Cannot query updater workflow: "+str(e))
    report=evaluate(history,svg,runs,datetime.now(timezone.utc))
    report["reasons"]=failures+report["reasons"]
    report["healthy"]=not report["reasons"]
    Path(args.json_out).write_text(json.dumps(report,indent=2)+"\n",encoding="utf8")
    lines=["# MEDIA KOLFAT Downloads Dashboard health alert","",
           "**Status:** "+("Healthy" if report["healthy"] else "UNHEALTHY"),
           "**UTC checked:** "+report["checked_at"],
           "**Last observation:** "+str(report["snapshot_date"]),
           "**Last precise refresh:** "+str(report["last_refresh"]),"",
           "## Detected problems"]
    lines.extend("- "+reason for reason in report["reasons"])
    lines.extend(["","## Recovery",
      "- Examine the [dashboard updater](https://github.com/"+REPO+"/actions/workflows/update-download-dashboard.yml).",
      "- Examine the [independent monitor](https://github.com/"+REPO+"/actions/workflows/monitor-download-dashboard.yml).",
      "- Repair and rerun the updater; this issue automatically closes when health returns.",
      "- These are GitHub package-download events, NOT unique users, installations, or Store downloads."])
    if report["updater_url"]: lines.append("- Last completed updater: "+report["updater_url"])
    Path(args.issue_out).write_text("\n".join(lines)+"\n",encoding="utf8")
    print("HEALTHY" if report["healthy"] else "UNHEALTHY",report["reasons"])
if __name__=="__main__":main()
