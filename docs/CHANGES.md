## 2026-10-28 — Repair v1.8.0 tag chronology and release-list clarity

**Problem:** Release ID `417370501`, named MEDIA KOLFAT 1.8.0, retains original publication date **October 19, 2026** but its Git tag `v1.8.0` was mistakenly moved to the **October 28, 2026** Linux Beta documentation commit `026f78502c41824bb673bc9a4da46444ab974ef7`. GitHub sorts the Releases sidebar using tag-commit chronology, so 1.8.0 appeared ahead of Windows 2.0.0.

**Verified original target:** The original 2026-10-19 release-sync implementation recorded `91b9a3bf4a530b23bbb4ee44e39fdf6a5563b5c6` as the true v1.8.0 release target, and the commit date is 2026-10-19 14:29:21 UTC.

**Repair:** A one-time, guarded GitHub Actions workflow `.github/workflows/repair-release-v180-order.yml` restores exactly `refs/tags/v1.8.0` to the original commit, accepting the current wrong SHA only. Separately renames the older, empty-assets Linux Beta 2.3 release (ID 427090517) to **🐧 MEDIA KOLFAT 2.0.0 for Linux | Beta 2.3 (Superseded)** to clearly distinguish it from Linux 2.4 and stable Windows 2.0.0. Both historical pre-releases stay published.

**Explicit non-changes:** No release is deleted or redrafted; no version notes, upload assets, publication timestamps, `v2.0.0` Windows tag or `v2.4.0-linux-beta` tag are changed. Existing Windows installer and SHA-256 remain attached.

**Verification:** Require GitHub workflow success; fetch the exact tag refs, all releases with their tag/created/published dates, the historical Beta title and Windows installer assets. GitHub's release sidebar has no custom semantic-version sorting; the corrected tag makes 1.8.0 sort by its historical release commit date.

**Rollback:** To undo the tag-only repair if needed, deliberately reset `refs/tags/v1.8.0` to the pre-repair SHA `026f78502c41824bb673bc9a4da46444ab974ef7` and restore the old Linux Beta 2.3 title; **do not** delete tags/releases or alter release assets. Once repair succeeds, this one-time maintenance workflow can be removed in a separate documented PR.

---

## 2026-10-28 — Publish separate MEDIA KOLFAT Linux 2.4.0 experimental pre-release page

**Purpose:** Publish **🐧 MEDIA KOLFAT 2.4.0 for Linux | Public Beta** under `v2.4.0-linux-beta` as a separate GitHub **Pre-release**, without rebuilding or modifying Windows 2.0.0 and the earlier Linux 2.3 release.

**Files:** `release-notes/v2.4.0-linux-beta.md`, `.github/workflows/publish-linux-beta-announcement.yml`, `README.md`, and this document.

**Scope:** Linux x64 AppImage only; MOVE remains disabled. WSLg tests passed, but **this 2.4.0 AppImage has not been launched on native Ubuntu 26.04**. The previous Linux version completed a real native Ubuntu Guided COPY test with 101 photos; no cross-version equivalence is asserted. Document experimental risk and potential Linux UI caveats.

**Assets:** The two exported/verified files (AppImage and matching SHA-256 checksum) are **not present in this public repository or release and are not uploaded by this documentation workflow**. The release page must clearly say attachment is pending. No dummy binaries, fabricated names or checksums.

**Verification:** Check GitHub Actions success, exact tag/title, `prerelease=true`, intact Windows release, and truthful empty Assets state. After a user separately attaches the two verified files, verify uploaded names, checksums and assets; do not claim binary publication beforehand.

**Rollback:** Restore the older Linux announcement workflow and README, delete the new 2.4.0 GitHub release/tag only if explicitly requested, and retain the historical 2.3 release. Do not delete Windows binaries or alter source-code archives.

---

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
