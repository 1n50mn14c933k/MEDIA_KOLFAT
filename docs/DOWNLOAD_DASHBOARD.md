# MEDIA KOLFAT GitHub download dashboard

The chart at the **bottom of the public README** displays actual GitHub EXE
installer downloads using the static image
[assets/download-dashboard.svg](../assets/download-dashboard.svg).

## What the counter measures

GitHub EXE downloads are the total of GitHub's public release-asset
`download_count` values across published assets whose names match
`MEDIA_KOLFAT_<version>_Setup.exe`. Checksum files and GitHub-generated
source archives are excluded.

**Downloads are not confirmed installations.** Repeated or automated downloads
cannot be distinguished. The application does not collect usage data, device
identifiers or installation telemetry for this dashboard.

## Daily automatic updates

The [Update MEDIA KOLFAT downloads dashboard](../.github/workflows/update-download-dashboard.yml)
GitHub Actions workflow runs daily at **07:23 UTC**, can be started manually
and is triggered by changes to its script or workflow.

The job uses GitHub's official REST API and GitHub Actions' temporary
`GITHUB_TOKEN`. It commits only the updated static chart and
`assets/download-dashboard-history.json` when those files change.

The earliest recorded snapshot is **October 27, 2026**. Each subsequent
snapshot reflects the cumulative count observed on that date. Historic daily
or monthly counts before recording started cannot be reconstructed reliably
and are not invented. The chart displays up to 90 actual observations.

## Maintenance and rollback

No permanent credentials, external analytics services, paid tools or new
application permissions are needed. To stop updates, disable the workflow
in GitHub Actions. To remove the dashboard, revert the README chart section
and this dashboard's assets and automation.

The dashboard never changes installer files, Store packaging, proprietary
source code or user-managed photos, videos, settings and reports.
