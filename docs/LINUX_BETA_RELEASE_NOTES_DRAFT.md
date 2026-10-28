# MEDIA KOLFAT 2.0 for Linux | Public Beta — Release Notes Draft

> **PREPARATION ONLY — NOT A PUBLISHED RELEASE.** Publish only after the final Linux Beta build, settings-reset fix, checksums and asset upload are verified. Choose a Linux-specific tag matching the actual final Beta package version. Mark the GitHub release as **Pre-release**; do not modify Windows stable `v2.0.0`.

**Platform:** Linux x64 / AMD64  
**Channel:** Experimental public Beta  
**Price:** Free  
**Source:** Proprietary; binaries only

MEDIA KOLFAT is coming to Linux! 🐧

This early Beta brings the desktop photo and video organization experience to Linux, with a focus on local processing and **COPY that retains original files**.

## Included in the Beta

- Guided photo and video COPY organization, including manually selected sources
- Date-based folder organization and embedded EXIF date support
- Duplicate Finder using SHA-256 comparison
- Library browsing, media discovery and the dark MEDIA KOLFAT desktop interface
- Operation reports, file-collision handling, and cancellation safeguards

## Important limitations

- **MOVE is disabled on Linux, including Advanced Mode.** Do not interpret Windows MOVE descriptions as Linux feature availability.
- Some Linux settings and interface functions remain under investigation, including reset-related behavior.
- The Beta is not considered production-stable or verified across all distributions.
- Always maintain an independent backup of irreplaceable files.

## Tested systems and scope

Native Ubuntu 26.04.1 LTS x64: application startup and an interactive Guided COPY using 101 sample photos succeeded. Focused automated filesystem tests cover source retention, EXIF handling, symlink and traversal rejection, collisions, cancellation and cross-filesystem copying. This is not a guarantee of full distribution or desktop compatibility.

## Downloads

When the GitHub pre-release is actually published, download the verified artifacts **from its Assets section**:

- Portable Linux x64 `.tar.gz`
- Debian/Ubuntu x64 `.deb` (dependencies may vary by distribution)
- SHA-256 checksum manifest

**Do not insert guessed direct-download asset URLs.** Verify the actual tag, file names and checksums after upload.

## Community feedback

Found a Linux-specific bug? Please open a [GitHub Issue](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues) with your distribution, desktop environment, Beta version, reproduction steps and sanitized error logs. Do not post private file paths, secrets or personal photos.

Thanks for helping make MEDIA KOLFAT useful on Linux. 🧹❤️

[Official website](https://kolfat.app) · [Support KOLFAT](https://ko-fi.com/kolfat_app)
