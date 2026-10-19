#!/usr/bin/env python3
"""Idempotent publisher for MEDIA KOLFAT community starter discussions.

Requires GH_TOKEN with GitHub Discussions read/write scope, GH_REPO owner/name.
Run only from the repository's manually triggered workflow.
"""
import json
import os
from pathlib import Path
import subprocess
import sys

def graphql(query, **variables):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        cmd.extend(["-F" if isinstance(value, (int, bool)) else "-f", f"{key}={value}"])
    p = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if p.returncode:
        raise RuntimeError("GitHub GraphQL request failed: " + p.stderr.strip()[:600])
    result = json.loads(p.stdout)
    if result.get("errors"):
        raise RuntimeError(str(result["errors"])[:600])
    return result["data"]

repo = os.environ["GH_REPO"]
owner, name = repo.split("/", 1)
info = graphql("""query($owner:String!,$name:String!){
 repository(owner:$owner,name:$name){
  id
  discussionCategories(first:50){nodes{id,name,slug}}
  discussions(first:100){nodes{title}}
 }
}""", owner=owner, name=name)["repository"]
if not info:
    raise SystemExit("Repository not found")
cats = info["discussionCategories"]["nodes"]
if not cats:
    raise SystemExit("No Discussion categories are configured; create them in repository Settings first")
existing = {x["title"] for x in info["discussions"]["nodes"]}
mapping = {
    "01-welcome.md": ["Announcements", "General"],
    "02-feature-requests.md": ["Ideas", "General"],
    "03-version-feedback.md": ["General", "Announcements"],
    "04-language-poll.md": ["Ideas", "General"],
    "05-before-after.md": ["General"],
    "06-current-tools.md": ["General"],
    "07-pro-concepts.md": ["Ideas", "General"],
    "08-platform-interest.md": ["Ideas", "General"],
    "09-questions-and-help.md": ["Q&A", "Questions", "General"],
}
mutation = """mutation($repositoryId:ID!,$categoryId:ID!,$title:String!,$body:String!){
 createDiscussion(input:{repositoryId:$repositoryId,categoryId:$categoryId,title:$title,body:$body}){
  discussion{url}
 }
}"""
for filename, preferences in mapping.items():
    src = Path("discussion-starters") / filename
    body = src.read_text(encoding="utf-8")
    title = body.splitlines()[0].removeprefix("# ").strip()
    if title in existing:
        print("Already present:", title)
        continue
    cat = next((c for pref in preferences for c in cats if c["name"].casefold() == pref.casefold()), None)
    if not cat:
        raise RuntimeError("No suitable discussion category for " + filename)
    # gh CLI's GraphQL variable string args are supplied through -f.
    result = graphql(mutation, repositoryId=info["id"], categoryId=cat["id"], title=title, body=body)
    print("Created:", result["createDiscussion"]["discussion"]["url"])
