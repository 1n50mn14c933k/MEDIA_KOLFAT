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

<p align="center"><img src="https://raw.githubusercontent.com/1n50mn14c933k/1n50mn14c933k.github.io/main/assets/media-kolfat-2-guide/screenshots/05-01-library-overview.png" alt="MEDIA KOLFAT photo and video library interface, Windows guide screenshot" width="950"></p>
<p align="center"><sub>Windows 2.0 interface preview. Experimental Linux Beta appearance may differ.</sub></p>

## Overview

MEDIA KOLFAT makes it easier to discover, browse and organize your personal photos and videos. It focuses on predictable, local-first workflows, EXIF/date-based organization, duplicate detection and a dark desktop interface, without subscriptions, advertising or mandatory cloud uploads.

- **Windows 2.0.0 Stable:** Guided COPY and explicit Advanced MOVE.
- **Linux 2.4.0 Public Beta:** Secure COPY and duplicate detection; **MOVE is disabled**, even in Advanced Mode.
- **macOS:** Potential future platform, not yet released.

## ⬇️ Install & Download

| Platform | Release | Format | Official downloads |
|---|---|---|---|
| 💻 **Windows x64** | **Stable 2.0.0** | `.exe` / Store | [Windows installer](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_Setup.exe) · [Microsoft Store](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare) |
| 🐧 **Linux x64** | **Public Beta 2.4.0** | `.AppImage` | [Download AppImage](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage) · [SHA-256 checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_SHA256.txt) |
| 🍎 **macOS** | Not released | — | Not available |

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

## What is MEDIA KOLFAT?

Large photo and video collections can become difficult to manage when files come from different cameras, phones, folders and years.

MEDIA KOLFAT is designed to make those libraries easier to understand and organize by combining media discovery, metadata handling, previews and structured organization workflows in a desktop application with a stable Windows edition and a separate experimental Linux Beta.

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

MEDIA KOLFAT is designed for users who primarily want to **organize, inspect and clean up their photo and video collections** without paying for a professional editing suite they may never need.

The products below are all capable applications, but they serve somewhat different audiences. This comparison is intended to make those differences clear rather than suggest that one product is the right choice for every user.

| Feature | **MEDIA KOLFAT FREE** | Adobe Lightroom / Classic | ACDSee Photo Studio Home | Mylio Photos+ | ON1 Photo RAW |
|---|---|---|---|---|---|
| **Core pricing model** | ✅ **FREE** | 💰 Subscription | 💰 Paid license / subscription | ◐ Free app available; Photos+ is paid | 💰 Paid license / subscription |
| **Free core edition** | ✅ **Yes — remains free** | ❌ | ❌ | ✅ Free Mylio Photos app available | ❌ |
| **Windows desktop** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **macOS support** | ❌ | ✅ | ❌ Home edition is Windows-focused | ✅ | ✅ |
| **iOS / Android ecosystem** | ❌ | ✅ | ◐ Mobile Sync ecosystem | ✅ | ✅ |
| **Local-first media management** | ✅ **Core design** | ◐ Lightroom Classic supports local files; Lightroom also offers cloud-centric workflows | ✅ | ✅ **Core design** | ✅ |
| **Cloud required for core workflow** | ✅ **No** | ◐ Depends on Lightroom workflow/product | ✅ No | ✅ No | ✅ No |
| **Photo + video library** | ✅ | ✅ | ✅ | ✅ | ◐ Primarily photography-focused |
| **Metadata / EXIF handling** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Date-based physical folder organization** | ✅ **Core focus** | ✅ Lightroom Classic supports local folder organization | ✅ | ◐ Preserves and works with existing folder structures | ✅ Folder-based browsing |
| **Duplicate Finder** | ✅ | ◐ Duplicate Detection available in Lightroom on the web | ✅ | ✅ | — |
| **Photos Health Check** | ✅ **Dedicated workflow** | — | — | — | — |
| **Manual photo rotation** | ✅ Left, right, 180° and batch Undo | ◐ Rotation/editing tools | ◐ Rotation/editing tools | ◐ Rotation/editing tools | ◐ Rotation/editing tools |
| **Large-library browsing** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **RAW development** | ❌ | ✅ **Advanced** | ◐ RAW viewing/decoding in Home | ◐ Essential RAW editing | ✅ **Advanced** |
| **Advanced photo editing** | ❌ | ✅ | ✅ | ◐ Essential editing tools | ✅ |
| **Layers / compositing** | ❌ | ❌ Lightroom itself | ❌ Home edition | ❌ | ✅ |
| **AI-assisted organization / search** | ❌ | ✅ | ✅ | ✅ | ✅ AI keywording |
| **Face recognition** | ❌ | ✅ | ✅ | ✅ | — |
| **Cross-device sync** | ❌ | ✅ | ◐ Mobile Sync ecosystem | ✅ **Strong focus** | ✅ With Cloud Sync options |
| **Simple guided organization workflow** | ✅ **Core design** | ◐ Professional / feature-rich workflow | ◐ Feature-rich DAM workflow | ◐ Library and device-sync workflow | ◐ Professional photography workflow |

**Legend:** ✅ Included · ◐ Available, partial, optional, or implemented differently · ❌ Not included · — No directly equivalent primary feature identified in the referenced product documentation

### The difference in one sentence

> **MEDIA KOLFAT is not trying to replace Lightroom or a professional RAW editor.**
>
> It is built for users who want to **organize, inspect and clean up their photo and video collection without paying for an editing suite they may never use.**
>
> **MEDIA KOLFAT FREE stays FREE.**
>
> Need professional RAW editing, AI-assisted search, cloud synchronization or mobile apps? Another product may be a better fit.
>
> Need a straightforward, local-first Windows tool focused on taking care of your media? That is what **MEDIA KOLFAT** is built for.

### Comparison notes

Competitor capabilities and commercial models can change over time. The table is based on publicly documented product information available at the time of writing and is intended as a practical feature overview, not a claim that the products are identical in scope.

Official references:

- Adobe Lightroom: https://www.adobe.com/products/photoshop-lightroom.html
- Adobe Duplicate Detection: https://helpx.adobe.com/lightroom/web/share-your-work/review-and-download/duplicate-detection.html
- ACDSee Photo Studio Home: https://www.acdsee.com/en/products/photo-studio-home/features/
- Mylio Photos: https://mylio.com/
- Mylio Photo DeDupe: https://support.mylio.com/find-duplicate-photos-photo-dedupe
- ON1 Photo RAW: https://www.on1.com/products/photo-raw/features/

## MEDIA KOLFAT editions

### MEDIA KOLFAT

The core edition is available free of charge and provides the essential media organization experience.

### MEDIA KOLFAT PRO

MEDIA KOLFAT PRO is planned as an optional paid edition/add-on for additional advanced functionality over time.

Future PRO functionality will be announced only when it is ready to be publicly committed to. The public roadmap is not a contractual promise of specific future features or release dates.

## System requirements

Windows Stable supports x64 desktop systems and is distributed via Microsoft Store and GitHub Releases. Linux Beta is a separate x64 AppImage release with limited compatibility testing.

Check the Microsoft Store listing for Store requirements and the GitHub release for standalone Windows x64 distribution.

Storage requirements depend on the size of the user's library and generated application data such as thumbnails and cache files.

## Privacy

MEDIA KOLFAT is designed around local media organization. The current core workflow processes the user's photo and video library locally on the user's device rather than requiring the library to be uploaded to KOLFAT servers.

For complete and authoritative privacy information, see:

- Privacy Policy: https://kolfat.app/privacy/

If future cloud, online or AI-backed functionality changes how data is processed, the relevant product information and privacy documentation will be updated before that functionality is released.

## Installation and downloads

Download only from official channels, not third-party mirrors. Windows stable and Linux Beta are separate release tracks.

- **GitHub Windows EXE:** [Installer](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_Setup.exe) and [SHA-256 checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_SHA256.txt)
- **Microsoft Store:** [Official listing](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare)
- **Linux x64 Beta:** [2.4.0 experimental pre-release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta) (AppImage and checksum awaiting upload)

The Store edition receives Store-managed updates; the GitHub EXE edition does not. GitHub-generated source archives are not Windows installers.

## What this repository is for

This is the public home of MEDIA KOLFAT on GitHub. Use it to:

- ⭐ Star the project
- 👁️ Watch for project and release updates
- 🐛 Report reproducible bugs
- 💡 Suggest features and improvements
- 📋 Read the public roadmap
- 📦 Read release notes and version history
- 🔐 Follow the private security-reporting process

## What this repository does not contain

For security and intellectual-property protection, this repository does **not** contain:

- MEDIA KOLFAT application source code
- Internal build or signing pipelines
- Code-signing certificates or keys
- Credentials or secrets
- Private development plans

The proprietary application source is maintained separately in a private repository.

## Reporting bugs

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

![MEDIA KOLFAT GitHub EXE downloads dashboard](assets/download-dashboard.svg)

**GitHub EXE downloads** are counted automatically from official GitHub Release installer assets. These figures represent downloads, **not confirmed installations**. No in-app telemetry or personal information is collected for this dashboard.

[Download MEDIA KOLFAT 2.0.0](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0) · [How dashboard statistics work](docs/DOWNLOAD_DASHBOARD.md)

---

© 2026 KOLFAT · MEDIA KOLFAT
