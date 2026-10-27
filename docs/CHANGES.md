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
