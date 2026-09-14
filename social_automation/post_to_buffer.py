#!/usr/bin/env python3
"""Schedule one deterministic MEDIA KOLFAT marketing post through Buffer.

Designed for GitHub Actions. Scheduled runs wake shortly before the desired
Europe/Vienna slot and create a Buffer customScheduled post for exactly 09:00
or 18:00 local time. Manual runs default to dry-run unless explicitly told
otherwise by the workflow.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

API_URL = "https://api.buffer.com"
VIENNA = ZoneInfo("Europe/Vienna")
POSTS_FILE = Path(__file__).with_name("posts.json")
TARGET_HOURS = (9, 18)


def graphql(api_key: str, query: str, variables: dict | None = None) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=payload,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "KOLFAT-Social-Automation/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Buffer HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Buffer connection failed: {exc}") from exc

    if data.get("errors"):
        raise RuntimeError(f"Buffer GraphQL error: {data['errors']}")
    return data


def discover_x_channel(api_key: str) -> tuple[str, str]:
    account_query = """
    query AccountOrganizations {
      account {
        organizations { id name }
      }
    }
    """
    account = graphql(api_key, account_query)
    organizations = account.get("data", {}).get("account", {}).get("organizations", [])
    if not organizations:
        raise RuntimeError("No Buffer organization found for this API key.")

    channel_query = """
    query Channels($organizationId: OrganizationId!) {
      channels(input: { organizationId: $organizationId }) {
        id
        name
        service
      }
    }
    """

    matches: list[dict] = []
    for organization in organizations:
        result = graphql(api_key, channel_query, {"organizationId": organization["id"]})
        channels = result.get("data", {}).get("channels", [])
        matches.extend(channel for channel in channels if str(channel.get("service", "")).lower() in {"twitter", "x"})

    if not matches:
        raise RuntimeError("No connected X/Twitter channel found in Buffer.")
    if len(matches) > 1:
        names = ", ".join(str(item.get("name", item["id"])) for item in matches)
        raise RuntimeError(f"Multiple X channels found ({names}). Set BUFFER_X_CHANNEL_ID as a GitHub variable.")

    channel = matches[0]
    return str(channel["id"]), str(channel.get("name") or "X")


def next_target(now_local: datetime) -> datetime | None:
    """Return an upcoming target within 35 minutes, otherwise no-op.

    GitHub cron wakes twice around each DST-dependent UTC time. Only the run
    immediately before the actual Vienna-local slot proceeds.
    """
    for hour in TARGET_HOURS:
        target = now_local.replace(hour=hour, minute=0, second=0, microsecond=0)
        delta = target - now_local
        if timedelta(minutes=0) <= delta <= timedelta(minutes=35):
            return target
    return None


def choose_post(posts: list[str], target_local: datetime) -> tuple[int, str]:
    if not posts:
        raise RuntimeError("posts.json is empty.")
    slot = 0 if target_local.hour == 9 else 1
    base = datetime(2026, 9, 15, tzinfo=VIENNA).date().toordinal()
    sequence = (target_local.date().toordinal() - base) * 2 + slot
    index = sequence % len(posts)
    return index, posts[index]


def validate_post(text: str) -> None:
    # X shortens URLs internally, but the library intentionally contains no URLs.
    if len(text) > 280:
        raise RuntimeError(f"Selected post is {len(text)} characters; X limit is 280.")
    if "MEDIA KOLFAT" not in text and "KOLFAT" not in text:
        raise RuntimeError("Selected post does not contain KOLFAT branding.")


def schedule_post(api_key: str, channel_id: str, text: str, due_at_utc: datetime) -> dict:
    mutation = """
    mutation CreateScheduledPost($text: String!, $channelId: ChannelId!, $dueAt: DateTime!) {
      createPost(input: {
        text: $text
        channelId: $channelId
        schedulingType: automatic
        mode: customScheduled
        dueAt: $dueAt
      }) {
        ... on PostActionSuccess {
          post { id text dueAt status }
        }
        ... on MutationError {
          message
        }
      }
    }
    """
    variables = {
        "text": text,
        "channelId": channel_id,
        "dueAt": due_at_utc.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    }
    result = graphql(api_key, mutation, variables)
    outcome = result.get("data", {}).get("createPost", {})
    if outcome.get("message"):
        raise RuntimeError(f"Buffer rejected the post: {outcome['message']}")
    post = outcome.get("post")
    if not post:
        raise RuntimeError(f"Unexpected Buffer response: {result}")
    return post


def main() -> int:
    dry_run = os.getenv("DRY_RUN", "false").strip().lower() == "true"
    forced_slot = os.getenv("FORCE_SLOT", "").strip()
    now_local = datetime.now(timezone.utc).astimezone(VIENNA)

    with POSTS_FILE.open("r", encoding="utf-8") as handle:
        posts = json.load(handle)
    if not isinstance(posts, list) or not all(isinstance(item, str) for item in posts):
        raise RuntimeError("posts.json must be a JSON array of strings.")

    if forced_slot:
        hour = int(forced_slot)
        if hour not in TARGET_HOURS:
            raise RuntimeError("FORCE_SLOT must be 9 or 18.")
        target_local = now_local.replace(hour=hour, minute=0, second=0, microsecond=0)
        if target_local <= now_local:
            target_local += timedelta(days=1)
    else:
        target_local = next_target(now_local)
        if target_local is None:
            print(f"No 09:00/18:00 Vienna slot is due soon. Current local time: {now_local.isoformat()}")
            return 0

    index, text = choose_post(posts, target_local)
    validate_post(text)
    due_at_utc = target_local.astimezone(timezone.utc)

    print(f"Selected post #{index + 1}/{len(posts)}")
    print(f"Vienna target: {target_local.isoformat()}")
    print(f"UTC target:    {due_at_utc.isoformat()}")
    print("---")
    print(text)
    print("---")

    if dry_run:
        print("DRY_RUN=true: nothing was sent to Buffer.")
        return 0

    api_key = os.getenv("BUFFER_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("BUFFER_API_KEY GitHub secret is missing.")

    channel_id = os.getenv("BUFFER_X_CHANNEL_ID", "").strip()
    channel_name = "configured X channel"
    if not channel_id:
        channel_id, channel_name = discover_x_channel(api_key)

    post = schedule_post(api_key, channel_id, text, due_at_utc)
    print(f"Scheduled successfully for {channel_name}: Buffer post {post['id']} at {post['dueAt']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
