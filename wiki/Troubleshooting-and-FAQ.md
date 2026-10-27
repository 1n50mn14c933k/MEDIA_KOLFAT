# Troubleshooting and Frequently Asked Questions

These checks are for MEDIA KOLFAT **2.0.0** on Windows.

## I cannot find the newest version in Microsoft Store

Open the product's [official Store listing](https://apps.microsoft.com/detail/9p0x091t7mv4?ocid=webpdpshare) and check for an update. Store rollout and caching can vary by device or region. Verify the installed app version before assuming an update is available to your device. Never install packages from unofficial mirrors.

## My network drive or external disk is missing

Confirm that the drive is connected, visible in Windows and accessible to your account. For network shares, check network connectivity and permissions. If the drive disconnects during organization, stop, reconnect and inspect the source, destination and report.

## Organized files are hidden or missing from File Explorer

MEDIA KOLFAT includes fixes for hidden/system file attributes, including on network drives. Verify Windows Explorer view settings and check the destination and relevant file attributes. **Do not re-run MOVE or delete source files until you know where the media is.**

## Progress is slow or uneven

Large video files, metadata processing and network storage can take longer than small photos. Use the current-file and stage indicators. Ensure the source and destination remain accessible and that the destination has sufficient space.

## Can I stop a running operation?

MEDIA KOLFAT supports Pause, Resume and Cancel. A canceled operation is not necessarily undone; read the operation report and inspect completed files before retrying.

## What is the difference between COPY and MOVE?

COPY is the safer recommended route because the originals remain at the source. MOVE intentionally transfers the originals and requires more care. Read [[File Safety, Privacy and Backups|File-Safety-Privacy-and-Backups]].

## Why does a photo have the wrong date?

EXIF or other date metadata can be missing, inconsistent or altered by exports and editing software. Check the file's metadata and the selected organization pattern. Validate with a small test run first.

## Thumbnails, previews or rotation look wrong

Check the original file in another trusted image viewer. If a problem is reproducible, record your Windows version, MEDIA KOLFAT version, the relevant action and a sanitized screenshot.

## Why isn't Select All Visible selecting the entire library?

It applies to **visible** library entries, not necessarily the entire collection. The application also includes a fix for this behavior. Verify the visible selection before any batch rotation.

## Does MEDIA KOLFAT upload my private photos?

Normal local organization workflows do not require uploading the library to KOLFAT servers. Refer to the [Privacy Policy](https://kolfat.app/privacy/) for complete information.

## Reporting a problem

Use [GitHub Issues](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/issues) for reproducible defects. Include: app version, Windows version, steps, expected outcome, actual outcome and **sanitized** logs/screenshots. Use [Discussions](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/discussions) for usage questions. Security vulnerabilities must be reported privately.

## I installed the GitHub EXE but it does not update in Microsoft Store

The standalone EXE and Microsoft Store edition use different update channels. Download later standalone installer versions only from the official [GitHub Releases](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/releases). Never disable Windows security protections to install or update the EXE.
