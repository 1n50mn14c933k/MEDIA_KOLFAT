# Public repository maintenance history

## 2026-10-25 — Visible optional KOLFAT support shortcut

**Purpose:** Show the optional one-time Ko-fi support link on the MEDIA_KOLFAT repository's main README and GitHub Sponsor interface, without charging for the free application.

**Files:** `README.md` (orange support badge), `.github/FUNDING.yml` (GitHub Ko-fi funding link), `docs/CHANGES.md` (this record).

**Verification:** Funding YAML must contain `ko_fi: kolfat_app`, and the README badge must point to `https://ko-fi.com/kolfat_app`. No payment scripts or private account data are added. Verify rendered GitHub badge and Sponsor menu separately; admin repo Sponsorships setting may be required.

**Rollback:** Revert this commit or remove the badge line and `.github/FUNDING.yml`. Keep this historical record for recovery. This is a public-repository documentation/config change, not a MEDIA KOLFAT executable or store release.

**Policy:** Every future GitHub modification must include relevant documentation updates and recovery notes in the same commit or PR.
