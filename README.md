<p align="center"><img src="assets/media-kolfat-logo.png" alt="MEDIA KOLFAT mascot" width="185"></p>

<h1 align="center">MEDIA KOLFAT</h1>

<p align="center"><strong>Every memory, right where it belongs.</strong><br>Free, local-first photo and video organization for Windows and Linux.</p>

<p align="center">
  <a href="https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0"><img src="https://img.shields.io/badge/Windows-2.0.0_Stable-333333?style=flat-square&labelColor=181818" alt="Windows Stable 2.0.0"></a>
  <a href="https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta"><img src="https://img.shields.io/badge/Linux-2.4.0_Beta-FF812E?style=flat-square&labelColor=181818" alt="Linux Beta 2.4.0"></a>
  <img src="https://img.shields.io/badge/Price-FREE-333333?style=flat-square&labelColor=181818" alt="Free">
  <img src="https://img.shields.io/badge/Privacy-Local--First-333333?style=flat-square&labelColor=181818" alt="Local-first">
</p>

<p align="center">
  <a href="#-install--download">Download</a> ·
  <a href="https://kolfat.app/en/Media_Kolfat/">Website</a> ·
  <a href="#overview">Overview</a> ·
  <a href="#-development-timeline">Timeline</a> ·
  <a href="https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues">Bug Reports</a>
</p>

<p align="center">
  <a href="https://youtu.be/j__sznypSKs" title="Watch the MEDIA KOLFAT official intro on YouTube">
    <img src="https://img.youtube.com/vi/j__sznypSKs/maxresdefault.jpg" alt="MEDIA KOLFAT official intro trailer — click to watch on YouTube" width="950">
  </a>
</p>
<p align="center"><a href="https://youtu.be/j__sznypSKs"><strong>▶️ Watch the MEDIA KOLFAT Intro Trailer on YouTube</strong></a></p>

## Overview

MEDIA KOLFAT makes it easier to discover, browse and organize your personal photos and videos. It focuses on predictable, local-first workflows, EXIF/date-based organization, duplicate detection and a dark desktop interface, without subscriptions, advertising or mandatory cloud uploads.

- **Windows 2.0.0 Stable:** Guided COPY and explicit Advanced MOVE.
- **Linux 2.4.0 Public Beta:** Secure COPY and duplicate detection; **MOVE is disabled**, even in Advanced Mode.
- **macOS:** Apple Silicon (M-series, arm64) port planned; **Intel Macs are not targeted**. No public release yet.

## ⬇️ Install & Download

<p><img src="https://img.shields.io/badge/IMPORTANT-OFFICIAL%20DOWNLOADS%20ONLY-FF812E?style=for-the-badge&labelColor=181818" alt="IMPORTANT: Official downloads only"></p>

> 🟠 **Security notice:** Only download MEDIA KOLFAT from the official sources explicitly listed by the developer below: the **Microsoft Store** and the developer's **GitHub Releases**. Avoid third-party mirrors, repackaged installers, and unverified download websites. Verify published **SHA-256 checksums** when available. GitHub's automatic source archives are **not** application installers.

| Platform | Release | Format | Official downloads |
|---|---|---|---|
| 💻 **Windows x64** | **Stable 2.0.0** | `.exe` / Store | [Windows installer](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_Setup.exe) · [Microsoft Store](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare) |
| 🐧 **Linux x64** | **Public Beta 2.4.0** | `.AppImage` | [Download AppImage](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage) · [SHA-256 checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_SHA256.txt) |
| 🍎 **macOS Apple Silicon (M-series)** | Planned; not released | — | Not available; Intel Macs not targeted |

[**Full platform, download and checksum guide**](docs/PLATFORMS_AND_DOWNLOADS.md) covers Windows Stable, Linux Beta and planned Apple Silicon macOS.

**Linux quick start:** Download both files from the [separate Linux Beta release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta), verify the checksum, then launch the AppImage on a compatible x64 Linux desktop:

```bash
chmod +x MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage
./MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage
```

**Linux Beta warning:** COPY retains originals; **MOVE is unavailable**. The 2.4.0 AppImage passed automated tests and WSLg startup, but has not yet been tested interactively on native Ubuntu 26.04. A previous Beta successfully organized **101 sample photos** on native Ubuntu 26.04.1. Always keep independent backups of irreplaceable media.

**Distribution:** GitHub distributes **only the Linux AppImage and its checksum**. Other Linux package formats, if available later, will be distributed through appropriate stores or distro repositories. The standalone Windows EXE is unsigned and does not receive Microsoft Store updates.

## 🗓️ Development Timeline

| Date | Platform | Milestone |
|---|---|---|
| **Sep 10, 2026** | Windows | **1.0.0** public launch |
| **Sep–Oct 2026** | Windows | **1.2–1.8:** localization, Duplicate Finder, Guided/Advanced modes and MOVE safety |
| **Oct 27, 2026** | Windows | **2.0.0 Stable**, Microsoft Store + EXE |
| **Oct 2026** | Linux | Avalonia/.NET 10 port, secure COPY, EXIF and filesystem safety validation |
| **Oct 28, 2026** | Linux | Earlier Beta: native Ubuntu Guided COPY of **101 sample photos** |
| **Oct 28, 2026** | Linux | **2.4.0 Public Beta** AppImage + checksum published; reported **49 focused tests passed / 0 failed** |

See the [full Development Timeline](docs/DEVELOPMENT_TIMELINE.md) and [Public Roadmap](ROADMAP.md).

## 🐧 Linux Beta — Known Limitations

- **MOVE is disabled.** Safe source-deletion guarantees are still being developed.
- Some Linux settings, system-information labels and desktop integrations may need refinement.
- Native 2.4.0 AppImage testing and broader distribution compatibility remain unverified.
- Report problems through [GitHub Issues](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues), sharing only sanitized logs, not personal media or private file paths.

<p align="center"><a href="https://ko-fi.com/kolfat_app"><img src="https://img.shields.io/badge/%F0%9F%A7%B9%F0%9F%AA%A3%E2%9D%A4%EF%B8%8F-Keep_Our_Maid_Alive%2C_Strong_%26_Cleaning%21-FF812E?style=for-the-badge&amp;labelColor=181818" alt="🧹🪣❤️ Keep Our Maid Alive, Strong &amp; Cleaning!" width="430"></a></p>

---

## Core capabilities

### What's available in version 2.0.0 (Windows Stable)

- 🧭 **Guided and Advanced experiences** for different user needs
- 📁 **Media Folder Browser** and automatic computer scanning for photo and video discovery
- 🔎 **Duplicate Finder** for identifying duplicate media
- 🖼️ **Browse Library** with improved layout, previews and thumbnail fallback handling
- 📊 **Library Overview** with media, health, duplicate and organization information
- 🩺 **Photos Health Check** and metadata/date handling, including media without usable EXIF dates
- 📅 **Organize by Date** for predictable file organization
- 📋 **COPY and MOVE modes** with automatic operation reports; use COPY when originals should remain in place and select MOVE intentionally when transferring originals
- 🕘 **Activity History** for completed scans and organization operations
- 🔄 **Manual photo rotation**, including multi-select, batch rotation, Rotate Left, Rotate Right, 180°, and batch Undo in Browse Library
- 🔐 **Privacy & Local Processing** information inside the app
- 🌍 **English, Persian (Farsi), German and Spanish** language support, including Persian right-to-left (RTL) presentation
- 🌑 Dedicated dark interface and stability, safety and performance improvements
- ⏯️ **Pause, Resume and Cancel** controls with improved handling of interrupted operations
- 📊 **Detailed organization progress**, including the current file, processing stage, completed items and percentage
- 👁️ **Improved organized-file visibility**, including hidden and system attribute handling on network drives
- 🛡️ **Additional MOVE safeguards** to help protect original files
- ✨ Improved activity indicator, **Select All Visible** selection and error handling
- 🗂️ **File Type Selection** with extension counts and optional Other Files
- 📁 **Seven conditional destination categories**, created only when needed
- 🌐 **Improved SMB/NAS-to-NAS MOVE** behavior
- 🔗 **Safer symbolic-link handling**

MEDIA KOLFAT uses local-first processing. Windows is the stable edition, and Linux is an experimental Beta. Routine organization does not require media-library uploads.

**Important when organizing files:** COPY and MOVE have different consequences for source files. Review the selected mode and destination carefully, and keep an independent backup of irreplaceable media.

See the [official version 2.0.0 release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/latest) for published release highlights.

## Why choose MEDIA KOLFAT?

**FREE FOREVER. YOUR MEDIA. YOUR CONTROL.**

Organize, protect and manage your photos and videos without subscriptions, complicated editing suites or mandatory cloud uploads.

### Platform & feature comparison

| Feature | **MEDIA KOLFAT** | Lightroom | ACDSee Home | Mylio | ON1 RAW |
|---|---|---|---|---|---|
| **🖥️ OS SUPPORT** | | | | | |
| 💻 Windows | ✅ | ✅ | ✅ | ✅ | ✅ |
| 🐧 Linux | 🧪 Beta | ❌ | ❌ | ❌ | ❌ |
| 🍎 macOS | 🚧 Planned | ✅ | ❌ | ✅ | ✅ |
| 📱 iOS / Android | ❌ | ✅ | ◐ | ✅ | ✅ |
| **💎 PRICING & PRIVACY** | | | | | |
| Free forever | ✅ | ❌ | ❌ | ◐ | ❌ |
| Local-first media | ✅ | ◐ | ✅ | ✅ | ✅ |
| **📁 DISCOVERY & ORGANIZATION** | | | | | |
| Guided Mode & scanning | ✅ | ◐ | ◐ | ◐ | ◐ |
| Local, USB & NAS sources | ✅ | ◐ | ✅ | ◐ | ✅ |
| EXIF/date & unknown dates | ✅ | ◐ | ◐ | ◐ | ◐ |
| File-type selection & smart folders | ✅ | ◐ | ◐ | ◐ | ◐ |
| Duplicate Finder | ✅ | ◐ | ✅ | ✅ | — |
| **🖼️ LIBRARY & TOOLS** | | | | | |
| Photo/video previews | ✅ | ✅ | ✅ | ✅ | ◐ |
| Library Overview & Photo Health | ✅ | ◐ | ◐ | ◐ | ◐ |
| Batch rotation & selection | ✅ | ◐ | ✅ | ◐ | ◐ |
| **⚡ PERFORMANCE & SAFETY** | | | | | |
| System Benchmark / Performance Check | ✅* | — | — | — | — |
| Safe COPY / MOVE | ✅* | ◐ | ◐ | ◐ | ◐ |
| NAS-to-NAS MOVE | ✅* | — | ◐ | — | ◐ |
| Pause, Resume & Cancel | ✅ | ◐ | ◐ | ◐ | ◐ |
| Detailed progress & reports | ✅ | ◐ | ◐ | ◐ | ◐ |
| File & symbolic-link safeguards | ✅ | — | — | — | — |
| **🌍 EXPERIENCE** | | | | | |
| Four languages including RTL | ✅ | ◐ | ◐ | ◐ | ◐ |
| Dedicated dark UI | ✅ | ◐ | ◐ | ◐ | ◐ |
| Professional RAW editing | ❌ | ✅ | ◐ | ◐ | ✅ |

**Legend:** ✅ Available · 🧪 Public Beta · 🚧 Planned · ◐ Partial, optional or different workflow · ❌ Not supported · — No directly verified equivalent.

### Built for real-world media collections

| **20,000+ photos** | **30 documented Windows features** |
|:---:|:---:|
| NAS-to-NAS MOVE workload tested | Feature descriptions on the [official product page](https://kolfat.app/en/Media_Kolfat/) |

**MEDIA KOLFAT focuses on media organization rather than professional photo editing.** Guided workflows, duplicate detection, date-based organization and safety controls help you manage your collection without unnecessary complexity.

*Platform note:* The comparison highlights **Windows 2.0.0 Stable** features. Linux 2.4.0 is an experimental beta with a smaller feature set and **MOVE disabled**. macOS is planned, not released. The documented 20,000+ photo workload is a Windows NAS transfer test, **not** a system benchmark score.

*Feature note:* System Benchmark / Performance Check is included in this comparison as requested, but is **not currently documented on the official product page**. Competitor features are high-level comparisons and may use different workflows; a dash does not prove the feature is absent.

## What this repository is for

This is the public home of MEDIA KOLFAT on GitHub. Use it to:

- ⭐ Star the project
- 👁️ Watch for project and release updates
- 🐛 Report reproducible bugs
- 💡 Suggest features and improvements
- 📋 Read the public roadmap
- 📦 Read release notes and version history
- 🔐 Follow the private security-reporting process

## Reporting bugs

Use the [issue form](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues/new/choose) for Windows or Linux, and specify your operating system and exact version.

Before opening an issue, please check existing issues to avoid duplicates.

For bug reports, include:

- MEDIA KOLFAT version
- Operating system and version (Windows or Linux; include desktop environment for Linux)
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant sanitized logs or screenshots

Remove personal information, private file paths, credentials and sensitive media before posting publicly.

Do **not** publish suspected security vulnerabilities in public Issues. See [SECURITY.md](SECURITY.md).

## Releases and version history

MEDIA KOLFAT is publicly available through Microsoft Store and official GitHub Releases.

Current **stable Windows release**: **2.0.0** (Store package **2.0.0.0**). Linux has a separate pre-release. Release notes and version history are tracked through [GitHub Releases](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases) and [CHANGELOG.md](CHANGELOG.md).

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Support

- Support website: https://kolfat.app/support/
- GitHub support guidance: [SUPPORT.md](SUPPORT.md)

## Legal

The authoritative KOLFAT legal pages are:

- Privacy Policy: https://kolfat.app/privacy/
- Terms of Use: https://kolfat.app/terms/
- Disclaimer: https://kolfat.app/disclaimer/
- Third-Party Licenses: https://kolfat.app/licenses/
- Support: https://kolfat.app/support/

## License and source availability

MEDIA KOLFAT is proprietary software.

This public repository is provided for product information, community interaction, support coordination and release transparency. No open-source license is granted for the MEDIA KOLFAT application source code.

See [LICENSE.md](LICENSE.md) for the repository's proprietary rights notice and [CONTRIBUTING.md](CONTRIBUTING.md) for the forms of public contribution accepted here.

## 📊 MEDIA KOLFAT | GitHub Downloads Dashboard

![MEDIA KOLFAT Windows, Linux and macOS GitHub package downloads dashboard](assets/download-dashboard.svg)

**Automatic GitHub package-download tracking for 🪟 Windows, 🐧 Linux and 🍎 macOS.** The dashboard shows lifetime asset downloads, an observed downloads/day rate by platform and a package breakdown. Experimental Linux AppImage downloads are included; future macOS packages will appear automatically when published. **Not released** and **awaiting 2 observations** are shown when data is unavailable instead of fabricated statistics.

Counts reflect **GitHub Release downloads, not confirmed installations**. Microsoft Store, App Store and other external distribution channels are not included. No in-app telemetry or personal information is collected.

[Windows stable release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0) · [Linux Public Beta](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta) · [How the dashboard works](docs/DOWNLOAD_DASHBOARD.md)

---

© 2026 KOLFAT · MEDIA KOLFAT
