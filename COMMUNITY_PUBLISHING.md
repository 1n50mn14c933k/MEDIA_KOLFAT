# Publish the MEDIA KOLFAT Wiki and Discussions

The complete MEDIA KOLFAT 1.8.0 content lives in this repository:

- `wiki/` — 15 Wiki Markdown files (including Home, sidebar and two Persian guides)
- `discussion-starters/` — 9 community starter posts
- `.github/workflows/publish-wiki.yml` — Wiki publishing automation
- `.github/workflows/publish-discussions.yml` — one-time, duplicate-aware Discussion publishing

**Important:** Committed Markdown files are **not automatically GitHub Wiki pages or Discussions**. The two publishing workflows require repository-authenticated access. Do not paste tokens into Issues, Discussions, Wiki pages, source files or chat.

## 1. Activate the Wiki once

1. Confirm **Settings → General → Features → Wikis** is enabled.
2. Open the repository's **Wiki** tab.
3. If it says "Create the first page", initialize it once with a simple **Home** page.
4. Generate a token that can push to the repository's `.wiki.git` Git endpoint. A GitHub personal access token (classic) with the necessary repo access is often the practical choice; check your organization's token policies and use the minimum permitted permissions.
5. In **Settings → Secrets and variables → Actions → New repository secret**, save the token as **`WIKI_PUBLISH_TOKEN`**.
6. Open **Actions → Publish MEDIA KOLFAT Wiki → Run workflow**.
7. Verify the Wiki Home, sidebar and individual pages at [the Wiki](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/wiki).

The Wiki workflow copies the tracked Markdown files to the Wiki repository. It doesn't delete unrelated existing pages. If no token is configured, the workflow explains why it skipped publication.

## 2. Prepare Discussions

1. Confirm **Settings → General → Features → Discussions** is enabled.
2. Open [Discussions](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/discussions) and verify that categories such as **General**, **Ideas**, **Announcements** and **Q&A** exist. The script uses the first relevant available category and requires at least one suitable category.
3. Create a GitHub token with repository **Discussions: read and write** access. For a fine-grained personal access token, scope it to the `MEDIA_KOLFAT` repository and grant **Discussions read/write**.
4. Save it as the Actions repository secret **`DISCUSSIONS_PUBLISH_TOKEN`**.
5. Open **Actions → Publish MEDIA KOLFAT Discussion starters → Run workflow**.
6. Check the workflow log and [Discussions](https://github.com/1n50mn14c933k/MEDIA_KOLFAT/discussions).

The script checks existing discussion titles before creating posts, so rerunning normally avoids duplicates. It does not create announcements or change repository configuration beyond creating requested discussions.

## 3. After publication

- Link the live Wiki and Discussions from the website/README.
- Consider pinning the Welcome discussion and 1.8.0 feedback thread.
- Monitor feedback when convenient; don't promise immediate support response times.
- Keep reproducible bugs in Issues and suspected vulnerabilities in private reporting.
- Review new Wiki content for accuracy whenever MEDIA KOLFAT releases a new version.

**Safety:** This work does not publish proprietary source, installer artifacts, signing material, or private development information. The published guides describe already-announced user-facing functionality.
