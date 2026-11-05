#!/usr/bin/env python3
"""Create labels, milestones, issues and a Project board from this repo's files using the gh CLI.

Prereqs: `gh auth login` (add scope: `gh auth refresh -s project`), run from the repo root.
Usage:   python backlog/setup_github.py OWNER/REPO [--dry-run] [--skip-project]
Edit USERS below first. Safe to re-run: labels/milestones are upserted; issues are skipped if a
same-titled issue exists.
"""

import csv
import json
import pathlib
import subprocess
import sys

import yaml

USERS = {  # TODO: real GitHub usernames
    "P1": "atul-gh",
    "P2": "kanak-gh",
    "P3": "nuthan-gh",
    "P4": "samarth-gh",
}
repo = sys.argv[1] if len(sys.argv) > 1 and "/" in sys.argv[1] else None
DRY = "--dry-run" in sys.argv
NOPROJ = "--skip-project" in sys.argv
if not repo:
    sys.exit(__doc__)
root = pathlib.Path(__file__).resolve().parent.parent


def gh(*args, check=True, capture=True):
    cmd = ["gh", *args]
    if DRY:
        print("DRY:", " ".join(cmd))
        return ""
    r = subprocess.run(cmd, check=False, capture_output=capture, text=True)
    if check and r.returncode:
        print("ERR:", " ".join(cmd), r.stderr.strip())
    return r.stdout.strip()


# labels
for l in yaml.safe_load((root / ".github/labels.yml").read_text()):
    gh(
        "label",
        "create",
        l["name"],
        "-R",
        repo,
        "-c",
        l["color"],
        "-d",
        l["description"],
        "--force",
    )

# milestones (REST API)
existing = json.loads(gh("api", f"repos/{repo}/milestones?state=all&per_page=100") or "[]")
have = {m["title"] for m in existing}
for m in json.loads((root / "backlog/milestones.json").read_text()):
    if m["title"] not in have:
        gh(
            "api",
            f"repos/{repo}/milestones",
            "-f",
            f"title={m['title']}",
            "-f",
            f"description={m['description']}",
        )

# project board
proj_num = None
if not NOPROJ:
    owner = repo.split("/")[0]
    out = gh(
        "project",
        "create",
        "--owner",
        owner,
        "--title",
        "Watermark Hardening Backlog",
        "--format",
        "json",
    )
    if out:
        proj_num = json.loads(out)["number"]
        print(
            f"Project #{proj_num} created. In the UI, add Status columns: Backlog / Ready / In progress / In review / Done."
        )

# issues
have_titles = {
    i["title"]
    for i in json.loads(
        gh("issue", "list", "-R", repo, "--state", "all", "--limit", "500", "--json", "title")
        or "[]"
    )
}
for row in csv.DictReader((root / "backlog/backlog.csv").open()):
    title = f"[{row['id']}] {row['title']}"
    if title in have_titles:
        continue
    args = [
        "issue",
        "create",
        "-R",
        repo,
        "--title",
        title,
        "--body",
        row["body"],
        "--milestone",
        row["milestone"],
    ]
    for lab in row["labels"].split(";"):
        args += ["--label", lab]
    if USERS.get(row["assignee_key"]):
        args += ["--assignee", USERS[row["assignee_key"]]]
    url = gh(*args)
    if proj_num and url:
        gh(
            "project",
            "item-add",
            str(proj_num),
            "--owner",
            repo.split("/")[0],
            "--url",
            url,
            check=False,
        )
    if row["status"] == "done" and url:
        gh("issue", "close", url, "-R", repo, "--reason", "completed")
print("Done.")
