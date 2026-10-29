# MEDIA KOLFAT Changelog

All notable public production changes to MEDIA KOLFAT are documented here.

This changelog covers public product releases. Internal development builds, private engineering changes and security-sensitive implementation details are not listed.

Public GitHub releases use `MAJOR.MINOR.PATCH` versioning. Microsoft Store packages use the Windows four-part version format, for example `2.0.0.0`.

## [Unreleased]

Future production changes will be documented here before publication. **MEDIA KOLFAT remains free forever.** Linux experimental releases use a separate version/tag track from Windows Stable; the planned macOS port targets Apple Silicon M-series only and is not released.

---

## [2.4.0-linux-beta] — 2026-10-28 (Linux Public Beta)

**Linux x64 AppImage release**, separate from Windows Stable. Official GitHub release contains the AppImage and checksum only. **MOVE disabled**; COPY retains original files. Reported 49 focused tests passed and WSLg startup succeeded; interactive native Ubuntu testing of this specific AppImage remains unverified. The earlier beta completed native Ubuntu Guided COPY with 101 samples.

[Linux Beta release and checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.4.0-linux-beta) · [Platform guide](docs/PLATFORMS_AND_DOWNLOADS.md)

---

## [2.0.0] — 2026-10-27

**Microsoft Store package version:** `2.0.0.0`
**Languages:** English, Persian (RTL), German and Spanish

### Added and improved

- File Type Selection with extension counts and an optional Other Files category
- Seven conditional destination folders created only when needed
- Extended COPY/MOVE organization for optional Other Files
- Improved SMB/NAS-to-NAS MOVE handling, including large-library testing
- Improved symbolic-link and file-operation safety
- Added German and Spanish localization alongside English and Persian
- Refined interface, localization and branding
- Independent Windows x64 EXE installer alongside Microsoft Store MSIX

### Distribution

- [Windows x64 EXE installer](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_Setup.exe) and [SHA-256 checksum](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/download/v2.0.0/MEDIA_KOLFAT_2.0.0_SHA256.txt)
- [Microsoft Store](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare)
- [Version 2.0.0 release notes](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v2.0.0)

---

## [1.8.0] — 2026-10-19

**Microsoft Store package version:** `1.8.0.0`

### Improved

- Guided Mode focuses on safe COPY operations; Advanced Mode offers both COPY and MOVE
- Pause, Resume and Cancel controls, including better handling of interrupted operations
- Progress reporting for current file, processing stage, completed items and overall percentage
- Handling of hidden and system file attributes for organized media, including network drives
- MOVE operation safeguards to help protect original files from accidental deletion
- Animated activity feedback during background processing
- Error handling, automatic reporting and general stability

### Fixed

- **Select All Visible** behavior in Browse Library
- File visibility issues caused by hidden and system attributes

### Distribution

Production installers are provided through the Microsoft Store.

- [Official Microsoft Store download](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare)
- [GitHub release notes](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/untagged-ce0d52a8f6375672fbad)

---

## [1.6.0] — 2026-10-01

**Microsoft Store package version:** `1.6.0.0`

### Added

- Guided and Advanced experiences for different user needs
- MOVE mode to transfer originals as part of media organization
- Automatic COPY and MOVE operation reports
- Library Overview with media, health, duplicate and organization information
- Activity History for completed scans and organization operations
- In-app Privacy & Local Processing information
- Rotate Left, Rotate Right, 180° and batch Undo controls in Browse Library

### Improved

- Manual photo rotation with multi-select and batch rotation
- Browse Library layout and usability
- English and Persian (Farsi), including RTL interface support
- Application stability, safety, user interface and performance

### Distribution

MEDIA KOLFAT 1.6.0 is distributed through the Microsoft Store.

- [Official Microsoft Store download](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare)
- [GitHub release notes](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases/tag/v1.6.0)

---

## [1.4.0] — 2026-09-17

**Microsoft Store package version:** `1.4.0.0`

### Added

- Added Media Folder Browser workflow
- Added automatic computer scanning for media discovery
- Added Duplicate Finder workflow
- Added improved media organization guidance
- Added improved navigation assistance for guided users

### Improved

- Improved folder selection experience
- Improved support for external, network and cloud storage locations
- Improved duplicate detection workflow and reporting
- Improved user guidance and workflow clarity
- Improved performance and stability for large media collections
- Improved user interface consistency

### Fixed

- Fixed various user interface issues
- Fixed workflow state and reset behavior issues
- Fixed localization and RTL interface refinements
- Fixed general stability and usability issues

### Distribution

MEDIA KOLFAT production builds are distributed through the Microsoft Store.

Microsoft Store:
https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare

---

## [1.2.0] — 2026-09-11

**Microsoft Store package version:** `1.2.0.0`

### Improved

- Improved Persian (Farsi) language support
- Improved right-to-left (RTL) interface support
- Improved user interface and overall user experience
- Improved application stability
- Improved application performance

### Fixed

- General bug fixes
- General usability and interface refinements

### Distribution

MEDIA KOLFAT production builds are distributed through the Microsoft Store.

Microsoft Store:
https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare

---

## [1.0.0] — 2026-09-10

Initial public production release of MEDIA KOLFAT for Windows.

### Added

- Media source management
- Photo and video library browsing
- Metadata and date handling
- Date-based organization workflows
- Handling for media without usable EXIF/date metadata
- Thumbnail and preview generation with fallback handling
- Dedicated dark user interface
- Large-library performance and stability work
- Microsoft Store distribution
- Public support, privacy, security and legal documentation

### Distribution

The first public production release was published through the Microsoft Store.

Microsoft Store:
https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare

---

Official product page: https://kolfat.app/en/Media_Kolfat/

Support: https://kolfat.app/support/
