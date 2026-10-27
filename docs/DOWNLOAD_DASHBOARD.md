# MEDIA KOLFAT download dashboard

The bottom of the public repository README displays a generated SVG dashboard:
[assets/download-dashboard.svg](../assets/download-dashboard.svg).

## Data and accuracy

**GitHub EXE downloads** is the cumulative sum of GitHub's public release-asset
`download_count` for published files matching `MEDIA_KOLFAT_<version>_Setup.exe`.
It excludes checksum files and GitHub source archives. Download counts are
**not completed installations**; multiple downloads may come from the same person.

**Microsoft Store acquisitions** cannot be obtained from GitHub. The dashboard
shows **Not connected**, not zero, until you supply a verified aggregate from
Microsoft Partner Center. Never invent a Store count.

The chart starts collecting daily observations on October 27, 2026. We cannot
reconstruct historical months from GitHub's current cumulative totals, so the
dashboard never generates fictional July–September figures.

## Automatic refresh

[GitHub Actions: Update MEDIA KOLFAT downloads dashboard](../.github/workflows/update-download-dashboard.yml)
runs once a day at **07:23 UTC**, manually through `workflow_dispatch`, and
when the dashboard workflow, script, or Store data configuration changes.

It uses GitHub's short-lived, built-in `GITHUB_TOKEN`. No permanent
credentials, paid analytics, private source code, external telemetry services
or modifications to the MEDIA KOLFAT application are required.

The script `.github/scripts/update_download_dashboard.py` fetches release
download counts from the official GitHub API, updates the current day's sample
in `assets/download-dashboard-history.json`, and renders
`assets/download-dashboard.svg`. The workflow commits only those two files
when they change. The SVG is static and has no JavaScript.

## Optional verified Microsoft Store acquisitions

`assets/store-acquisitions.json` begins with a null value. If you obtain a
**verified cumulative acquisitions total** in Microsoft Partner Center, you may
manually enter an aggregate number, source date and source label. For example,
this is ONLY a fictional schema illustration, **not a production count**:

```json
{
  "acquisitions": 123,
  "as_of": "2026-10-27",
  "source": "Microsoft Partner Center manual report"
}
```

Never commit credentials, personal user records, exports with sensitive
information or private analytics. The Store series begins only after real
numbers become available. The manually entered count is not a live Store API
integration, and the two channel metrics measure different actions.

## Safe rollback

Disable the GitHub Actions workflow to stop new samples. Revert the README
dashboard section and the files introduced by this feature to remove it.
No EXE/MSIX installer, release assets, source code, photos or settings
are modified by this dashboard.
