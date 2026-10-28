# MEDIA KOLFAT | Development Timeline

**Updated:** October 28, 2026. Public milestones and verified testing scope; future priorities are not release promises.

## Windows — Stable

| Date | Version | Milestone |
|---|---|---|
| 2026-09-10 | [1.0.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.0.0) | Initial Windows release, media browsing and date-based organization |
| 2026-09-11 | [1.2.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.2.0) | Persian language and RTL refinements |
| 2026-09-17 | [1.4.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.4.0) | Duplicate Finder and computer scanning |
| 2026-10-01 | [1.6.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.6.0) | Guided/Advanced modes, MOVE, reports and activity history |
| 2026-10-19 | [1.8.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.8.0) | COPY/MOVE safeguards, pause/resume/cancel and progress |
| **2026-10-27** | **[2.0.0 Stable](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0)** | Microsoft Store 2.0.0.0 and standalone Windows EXE |

## Linux — Experimental Beta

| Time | Milestone | Verification |
|---|---|---|
| October 2026 | .NET 10/Avalonia Linux port | Native Linux GUI launched under WSLg |
| October 2026 | Secure filesystem boundary | Contained-handle COPY, safe source retention, symlink and traversal checks |
| October 2026 | Beta 2.1–2.2 | EXIF correctness, Linux case-sensitive indexing, manual and indexed COPY, collision/cancellation tests |
| October 2026 | Beta 2.3 | Native Ubuntu 26.04.1 GUI startup and Guided COPY of **101 sample photos**, with report |
| **2026-10-28** | **[2.4.0 Public Beta](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta)** | AppImage and SHA-256 checksum available, **49 focused tests passed / 0 failed** in reported validation; WSLg startup passed |

**Testing boundary:** Successful native Ubuntu COPY applies to an **earlier Beta**, not the 2.4.0 AppImage. The 2.4.0 AppImage has not been independently tested interactively on native Ubuntu 26.04 and remains experimental.

## Current priorities

- **Linux MOVE:** Disabled. Source deletion requires safety guarantees that have not yet been established.
- **Linux compatibility:** Native AppImage 2.4.0 testing; settings reset, desktop integration and broader distribution testing.
- **Windows:** Maintain stable 2.0.0 and respond to user feedback without compromising existing releases.
- **macOS:** Possible future release; no public release or fixed schedule.

## Distribution and support

- [Windows Stable 2.0.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0): EXE and Microsoft Store.
- [Linux Beta 2.4.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta): AppImage and SHA-256 checksum **only** on GitHub; other package formats belong in appropriate stores or distro repositories.
- [Report bugs](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues): include OS, desktop environment, version, steps and sanitized errors. Keep independent backups of important media.

[README](../README.md) · [Roadmap](../ROADMAP.md) · [Product website](https://kolfat.app/en/Media_Kolfat/)
