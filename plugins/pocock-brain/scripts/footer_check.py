#!/usr/bin/env python3
"""SubagentStop hook for a persona subagent.

Usage (plugin hooks.json, SubagentStop): python3 footer_check.py <person-wiki-dir> <agent-name> <person-name-regex> [--no-footer]
Acts only when the stopping subagent's type is <agent-name> (with or without the plugin prefix).
Blocks the agent from finishing until its final answer:
- ends with the **Ran:** / **Came out:** / **Changed:** block (unless --no-footer),
- cites a wiki page as wiki/<page>.md whenever it mentions the person (name match ignores case),
- cites only wiki pages that exist inside the wiki.
Allows one correction round (stop_hook_active) so it can't loop.
Unreadable hook input is skipped with a note (exit 0), since there is no answer to check.
"""
import json
import re
import sys
from pathlib import Path

WIKI = Path(sys.argv[1]).expanduser().resolve()
AGENT = sys.argv[2]
NAME_RE = sys.argv[3]
FOOTER = "--no-footer" not in sys.argv

try:
    data = json.load(sys.stdin)
except ValueError:
    print("footer_check: hook input is not JSON, skipped", file=sys.stderr)
    sys.exit(0)
if (data.get("agent_type") or "").split(":")[-1] != AGENT or data.get("stop_hook_active"):
    sys.exit(0)

msg = data.get("last_assistant_message") or ""
problems = []

if FOOTER:
    tail = msg[-3000:]
    for label in ("**Ran:**", "**Came out:**", "**Changed:**"):
        if label not in tail:
            problems.append(f"the closing block is missing {label}")

cited = set(re.findall(r"wiki/([\w./-]+?\.md)", msg))
if re.search(NAME_RE, msg, re.IGNORECASE) and not cited:
    problems.append("it says something about the person without citing a wiki page as wiki/<page>.md")
for page in sorted(cited):
    path = (WIKI / page).resolve()
    if not path.is_relative_to(WIKI):
        problems.append(f"it cites wiki/{page}, which points outside the wiki")
    elif not path.is_file():
        problems.append(f"it cites wiki/{page}, which doesn't exist")

if problems:
    hint = " End with three lines: **Ran:** <commands/tools or nothing> **Came out:** <what they showed> **Changed:** <files with paths or nothing>." if FOOTER else ""
    print("Before you finish, fix your answer: " + "; ".join(problems) + "." + hint, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
