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
**downloads/day** rate, computed from the two most recent suitable dated snapshots.
When an OS has **no published packages**, it says **Not released**, never a fictional
zero download history. If a package is newly introduced, the daily rate says
**awaiting 2 observations** rather than inventing a previous count.

The combined total is the sum of all currently published download counts. A compact
package list shows the highest-count assets individually; all eligible packages
are included in the totals regardless of how many fit in the graphic.

## Historic observations and daily refreshes

The existing Windows EXE history recorded on October 27–28, 2026 is migrated
without changing its original counts. Linux and macOS were **not measured** by the
old collector, so older snapshots for those systems remain `null` (unknown),
not zero. New observations use history schema v2 with independent counters for
Windows, Linux and macOS. GitHub's cumulative `download_count` values are taken
from the actual release assets each day. Deleted/replaced assets can reset counters;
negative daily rates are intentionally suppressed.

The [GitHub Actions workflow](../.github/workflows/update-download-dashboard.yml)
runs daily at 07:23 UTC, can run manually and is triggered by changes to the
script/workflow. It writes only `assets/download-dashboard.svg` and
`assets/download-dashboard-history.json`. The dashboard shows the latest
**90 observed snapshots**, not invented historical daily values.

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
