## 2026-10-28 — Large maid-support image button on Linux Beta release

The newly published Linux Beta 2.3 release was not included in the six historical Windows release-note sync files. Added the same clickable 720px-wide orange maid-support image badge to `release-notes/v2.0.0-linux-beta.2.3.md` and updated its existing publish workflow to synchronize an already-existing pre-release's body safely. Preserve prerelease status, tag, version notes and assets. Rollback: revert these source/workflow edits.

---

## 2026-10-28 — Restore real orange Ko-fi badges (not text links)

**Correction:** The 2026-10-28 support-text update inadvertently replaced clickable image badges with plain bold text links. Restored a standard-sized 430px orange Shields.io badge in README and a large 720px orange Shields.io badge in all six release notes. Both retain the exact message **🧹🪣❤️ Keep Our Maid Alive, Strong & Cleaning!** and destination https://ko-fi.com/kolfat_app. The existing release-note synchronization workflow updates the six published GitHub releases without changing version information, assets, or publication dates.

**Verification:** Confirm the six live descriptions contain linked `<img>` elements with `width="720"` and the new label, and the README badge uses `width="430"`. Check release-sync success and GitHub rendering.

**Rollback:** Revert this badge-only commit; do not alter installer assets, release metadata, or other documentation.

---

## 2026-10-28 — Unified maid-support message in README and all GitHub Releases

Updated the README and all six tracked release-note files to show **🧹🪣❤️ Keep Our Maid Alive, Strong & Cleaning!** linking to https://ko-fi.com/kolfat_app. Existing `.github/workflows/sync-release-notes.yml` publishes these descriptions automatically, including historical v1.8.0 via its release ID. Existing release assets, version notes, publication dates and tags are unchanged. Verify the workflow and live release bodies. Rollback by reverting these text changes and allowing the sync workflow to restore the release descriptions.

---

## 2026-10-27 — Support KOLFAT button added to every GitHub release

**Purpose:** Place the same large, orange **☕ Support KOLFAT** Ko-fi badge immediately after the “Thank you for using MEDIA KOLFAT! 🖤” and “ORDER FROM CHAOS.” closing lines in all six GitHub release descriptions.

**Files:** `release-notes/v1.0.0.md`, `v1.2.0.md`, `v1.4.0.md`, `v1.6.0.md`, `v1.8.0.md`, `v2.0.0.md`, and this maintenance history.

**Destination:** https://ko-fi.com/kolfat_app, matching the existing README sponsor badge and `.github/FUNDING.yml`. Support is entirely optional; the application stays free.

**Verification:** Ensure the release-note sync workflow succeeds; compare all six live release descriptions with the markdown sources and confirm the button appears after the closing branding. Preserve release assets, dates, features, and historical version information.

**Rollback:** Remove the button block from the six markdown files and let the existing release-note sync workflow update the live descriptions. No binaries or application files are affected.

---

## 2026-10-27 — GitHub-only download dashboard

**Purpose:** Remove the Microsoft Store acquisition counter and related configuration entirely at the user's request. Retain GitHub EXE download counts, historical snapshots, the dark SVG design and the daily refresh workflow.

**Changes:** Simplified the README dashboard, generator, SVG, historical JSON and documentation; removed `assets/store-acquisitions.json`; removed the Store config trigger from the workflow. The history stores only GitHub installer download counts.

**Security:** No app telemetry, new credentials, changes to Microsoft Store packaging, release binaries or user-managed data.

**Verification:** Verify the new GitHub workflow succeeds and the rendered README SVG contains no Store acquisition counter.

**Rollback:** Revert this commit to restore the previous presentation. No application or release files were modified.

---

## 2026-10-27 — Automated distribution dashboard

**Purpose:** Add a dark static download dashboard at the bottom of the public README based on official GitHub release-asset counters.

**Files:** README.md, docs/DOWNLOAD_DASHBOARD.md, docs/CHANGES.md, assets/download-dashboard.svg, assets/download-dashboard-history.json, assets/store-acquisitions.json, .github/scripts/update_download_dashboard.py, and .github/workflows/update-download-dashboard.yml.

**Data:** GitHub EXE asset downloads collected once daily from the official API; optional validated Microsoft Partner Center acquisitions remain "Not connected" without verified data. These are not confirmed installations, and pre-tracking historical counts are not fabricated.

**Privacy and safety:** No application telemetry, user identifiers, proprietary source, permanent credentials, installer changes or paid services. GitHub Actions uses its ephemeral repository token. Initial snapshot was observed on October 27, 2026.

**Verification:** Review the README's rendered SVG, the GitHub Actions workflow result, and the actual release-asset counts. The workflow is required to confirm the dashboard updates automatically.

**Rollback:** Disable the scheduled workflow and revert the dashboard documentation and asset changes; release artifacts remain untouched.

---

## 2026-10-27 — MEDIA KOLFAT 2.0.0 public documentation update

**Purpose:** Update the GitHub project README, CHANGELOG, roadmap, release checklist, security and support pages, current Wiki guides, and community starter documents to MEDIA KOLFAT 2.0.0.

**Release:** October 27, 2026; Windows MSIX 2.0.0.0 through Microsoft Store and Windows x64 standalone EXE via official GitHub Releases (checksum asset included). The EXE is currently unsigned and does not receive Store-managed updates.

**Scope and safety:** Preserve historical release notes, privacy claims, proprietary-source boundaries and the existing GitHub release assets. No application source, installer binary or secrets are committed to the repository.

**Verification:** Compare current-version text and links across changed files; inspect GitHub Actions Wiki/Discussion publication outcomes separately from source-file commits.

**Rollback:** Revert the documentation commit. This does not alter the published v2.0.0 release assets.

---

# Public repository maintenance history

## 2026-10-25 — Visible optional KOLFAT support shortcut

**Purpose:** Show the optional one-time Ko-fi support link on the MEDIA_KOLFAT repository's main README and GitHub Sponsor interface, without charging for the free application.

**Files:** `README.md` (orange support badge), `.github/FUNDING.yml` (GitHub Ko-fi funding link), `docs/CHANGES.md` (this record).

**Verification:** Funding YAML must contain `ko_fi: kolfat_app`, and the README badge must point to `https://ko-fi.com/kolfat_app`. No payment scripts or private account data are added. Verify rendered GitHub badge and Sponsor menu separately; admin repo Sponsorships setting may be required.

**Rollback:** Revert this commit or remove the badge line and `.github/FUNDING.yml`. Keep this historical record for recovery. This is a public-repository documentation/config change, not a MEDIA KOLFAT executable or store release.

**Policy:** Every future GitHub modification must include relevant documentation updates and recovery notes in the same commit or PR.
