# KOLFAT X Marketing Automation

This automation publishes two curated MEDIA KOLFAT marketing posts per day through Buffer:

- **09:00 Europe/Vienna**
- **18:00 Europe/Vienna**

GitHub Actions provides the runner. No always-on Windows or Linux machine is required.

## Required one-time setup

Create a Buffer API key and store it in this repository as a GitHub Actions secret:

1. Open this repository on GitHub.
2. Go to **Settings → Secrets and variables → Actions**.
3. Under **Secrets**, create a repository secret named exactly:
   - `BUFFER_API_KEY`
4. Paste the Buffer API key as the secret value.

Never commit the Buffer API key to the repository.

## X channel selection

By default, the script discovers the connected Buffer X/Twitter channel automatically.

If the Buffer account later contains more than one X channel, create a GitHub Actions **Variable** named:

- `BUFFER_X_CHANNEL_ID`

and set it to the Buffer channel ID that should receive MEDIA KOLFAT posts.

## Safe manual test

Open **Actions → KOLFAT X Marketing → Run workflow**.

Keep **dry_run = true**. Choose 09:00 or 18:00. The workflow validates the post library, selects the post, prints the target schedule and exits without contacting Buffer.

Only set **dry_run = false** when intentionally testing a real Buffer schedule.

## Scheduling and daylight saving time

GitHub cron expressions run in UTC. The workflow wakes before both possible CET/CEST UTC times. The Python script converts the current time to `Europe/Vienna` and only proceeds when a real 09:00 or 18:00 local slot is due soon.

The post is then sent to Buffer using `customScheduled` with an exact UTC `dueAt`, so Buffer is responsible for publishing at the intended local time.

## Content rotation

`posts.json` contains the curated X post library. Selection is deterministic from the Vienna date and morning/evening slot, so no mutable state file or automated Git commit is required.

Before scheduling, the workflow rejects any post longer than 280 characters.

## Files

- `posts.json` — curated MEDIA KOLFAT X posts
- `post_to_buffer.py` — Buffer API discovery and scheduling logic
- `.github/workflows/kolfat-x-marketing.yml` — GitHub Actions schedule
