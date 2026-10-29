# MEDIA KOLFAT | Platforms and official downloads

**Updated: October 29, 2026.** This guide describes public distribution channels and their known testing boundaries. It is not a compatibility guarantee.

> 🟠 **OFFICIAL DOWNLOADS ONLY:** Download MEDIA KOLFAT only from developer-listed official channels: the [Microsoft Store](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare) or the [MEDIA KOLFAT GitHub Releases](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases). Do not use third-party mirrors, repackaged installers, or GitHub-generated **Source code** archives as application installers.

## Availability by platform

| Platform | Status | Package | Source | Important limitation |
|---|---|---|---|---|
| **Windows x64** | **2.0.0 Stable** | Microsoft Store or EXE installer | [Windows v2.0.0 release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0) / [Microsoft Store](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare) | Advanced MOVE is opt-in; keep backups |
| **Linux x64** | **2.4.0 Public Beta** | **AppImage** | [Separate Linux Beta release](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta) | Experimental; **COPY only; MOVE disabled** |
| **macOS Apple Silicon (M-series, arm64)** | **Planned, not released** | None yet | None | **No public build, download or release date** |
| **macOS Intel (x64)** | **Not targeted** | None | None | Not part of the planned macOS port |

Windows, Linux and planned macOS have **separate release tracks**, titles, tags, package files and release notes. A release on one operating system does not indicate availability on another. The main MEDIA KOLFAT application is **free forever**; nothing in this guide announces a paid subscription or a released PRO product.

## Windows x64 Stable

- **Microsoft Store:** [Official listing](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare). Store-managed updates apply to the Store installation.
- **GitHub EXE:** [MEDIA_KOLFAT_2.0.0_Setup.exe](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_Setup.exe) with [published SHA-256 checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_SHA256.txt). Standalone EXE installations are updated by obtaining a newer **official Windows release**, not through Microsoft Store.

The GitHub EXE is currently **unsigned** and may display an unknown-publisher warning. **Do not disable Windows security protections** to install software. If the file's origin or checksum cannot be established, do not run it.

Optional Windows checksum calculation in PowerShell:

```powershell
Get-FileHash .\MEDIA_KOLFAT_2.0.0_Setup.exe -Algorithm SHA256
```

Compare the calculated hash to the checksum published alongside the **same release asset**. A checksum checks file integrity, but **does not independently authenticate the publisher**.

## Linux x64 Public Beta

The GitHub Linux release offers the **AppImage and its SHA-256 checksum only**. Other package types, if distributed in the future, belong in their appropriate stores or distribution repositories rather than GitHub release downloads.

1. Download [MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage) and the [corresponding checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.4.0-linux-beta/MEDIA_KOLFAT_Linux_Beta_2.4.0_SHA256.txt).
2. Compute and compare the checksum with the published value:

   ```bash
   sha256sum MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage
   ```

3. On a compatible x64 Linux desktop, make the file executable and launch it:

   ```bash
   chmod +x MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage
   ./MEDIA_KOLFAT_Linux_Beta_2.4.0_x86_64.AppImage
   ```

**Safety and testing:** Guided COPY retains source originals. **MOVE is disabled even in Advanced Mode.** The 2.4.0 release has reported automated validation (**49 focused tests passed**) and a WSLg startup check, but interactive native Ubuntu testing for **this exact 2.4.0 AppImage remains unverified** in the published documentation. A prior beta completed native Ubuntu 26.04.1 GUI/COPY testing with 101 sample photos. Do not confuse the earlier result with a test of the 2.4.0 binary. Always keep independent backups of irreplaceable media.

## Planned macOS port

The future port targets **Apple Silicon M-series Macs only (arm64)**, not Intel Macs. There is **no published macOS installer, beta, notarization claim, or fixed launch date**. Any website or mirror offering a “MEDIA KOLFAT for Mac” download before an official release announcement should be treated as unverified.

## Support and safety

- [Support and troubleshooting](../SUPPORT.md)
- [Report a public bug](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues/new/choose): include operating system, exact app version, installed package, reproduction steps and sanitized logs.
- [Privately report a suspected vulnerability](../SECURITY.md). Do not publish exploit details or private media.
- [Development timeline](DEVELOPMENT_TIMELINE.md) · [Roadmap](../ROADMAP.md) · [GitHub Releases](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases)
