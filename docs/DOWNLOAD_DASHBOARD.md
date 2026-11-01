# MEDIA KOLFAT GitHub package downloads dashboard

The [README dashboard](../assets/download-dashboard.svg) counts downloads of
**published application packages** attached to GitHub Releases across all operating
systems, including **experimental pre-releases**.

## Platforms and package types

- 🪟 **Windows:** EXE, MSI, MSIX, MSIXBundle, AppX, AppXBundle.
- 🐧 **Linux:** AppImage, DEB, RPM, Flatpak and Snap packages.
- 🍎 **macOS:** DMG and PKG, plus explicitly platform-named portable archives.

OS-qualified portable archives such as Linux `.tar.gz` and macOS `.zip`
are counted when their asset filename or release tag uniquely identifies the platform.
Checksum/verification files, automatic GitHub source archives, release drafts,
documentation, and unrelated assets are **excluded**. Downloads of two different
packages count as two release asset downloads, not unique people or devices.

Each OS card shows the current total, number of attached packages and the observed
**downloads/hour** rate, computed from the two most recent actual timestamped observations (minimum 30 minutes apart).
When an OS has **no published packages**, it says **Not released**, never a fictional
zero download history. If a package is newly introduced, the daily rate says
**awaiting 2 checks** rather than inventing a previous count.

The combined total is the sum of all currently published download counts. A compact
package list shows the highest-count assets individually; all eligible packages
are included in the totals regardless of how many fit in the graphic.

## Historic observations and daily refreshes

Hourly readings are stored in the existing schema-v2 JSON file under the optional `hourly_snapshots` key. Existing dated snapshots remain unchanged. GitHub scheduled actions can be delayed or occasionally skipped; the displayed rate divides the actual download-count difference by elapsed hours, and waits for two real measurements.\n\nThe existing Windows EXE history recorded on October 27–28, 2026 is migrated
without changing its original counts. Linux and macOS were **not measured** by the
old collector, so older snapshots for those systems remain `null` (unknown),
not zero. New observations use history schema v2 with independent counters for
Windows, Linux and macOS. GitHub's cumulative `download_count` values are taken
from the actual release assets each day. Deleted/replaced assets can reset counters;
negative daily rates are intentionally suppressed.

The [GitHub Actions workflow](../.github/workflows/update-download-dashboard.yml)
has two scheduled opportunities per hour at minutes 17 and 47 UTC, can run manually and is triggered by changes to the
script/workflow. It writes only `assets/download-dashboard.svg` and
`assets/download-dashboard-history.json`. The dashboard shows the latest
**90 daily snapshots** for the chart, plus up to **7 days of hourly snapshots** for rate calculations; historical unknown hours are never fabricated.

## Privacy and limits

GitHub's count measures asset-download events, **not installations, unique users,
Microsoft Store downloads or Apple/Mac App Store downloads**. It does not collect
OS/device telemetry, upload media, or track individual users. No permanent secret
or external analytics service is required. The GitHub Actions short-lived token
queries the official GitHub REST Releases API.

## Validation and rollback

The workflow runs local unit tests for package classification, pre-release support,
checksum exclusions, historic migration, daily rates, and not-yet-released macOS.
Check the dashboard, current assets and workflow success before relying on counters.
Rollback by reverting the dashboard script, workflow, README and documentation.
The schema-v2 history should be preserved or intentionally migrated back, never
silently overwritten. No application binaries, releases or product data are modified.

## Independent hourly health monitoring

The [monitor workflow](../.github/workflows/monitor-download-dashboard.yml) independently checks dashboard health every hour at minute 39 UTC and after every updater run. It verifies the last completed updater result, history/schema, SVG consistency, and exact last refresh timestamp. A failed, cancelled or missing updater, malformed data, or a snapshot older than 110 minutes, a missing recent updater run, an inconsistent exact refresh timestamp, or stale counters against the live GitHub Releases API (after a 30-minute grace period) triggers one issue assigned to the repository owner. The existing issue is updated, rather than duplicated. Recovery automatically closes it with a comment.

The updater writes the exact UTC time to the chart and last_checked_at_utc in UTC ISO 8601 format alongside historical schema-v2 observations. Older date-only snapshots remain intact and use a conservative end-of-day fallback. No fabricated counters are created. GitHub notifications for assigned issues must be enabled to receive external alerts. The monitor cannot guarantee detection during a GitHub Actions/API outage; delayed scheduled runs can delay notification. A ChatGPT alert requires a free automation slot.


## Visible health badge and limits

The README uses GitHub's official [monitor workflow badge](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/actions/workflows/monitor-download-dashboard.yml/badge.svg?branch=main). Red means the latest completed monitor run failed; green means that run passed, not that every future schedule is guaranteed to run. If GitHub misses the monitor itself, a status badge cannot autonomously switch to red. The SVG displays the precise last-check UTC timestamp to expose that limitation. The two offset updater schedules are redundant opportunities, not a claim of guaranteed exact-minute execution.

The monitor independently checks live release counts, allowing 30 minutes after a successful refresh for any new downloads. No commercial service or additional paid infrastructure is required.
