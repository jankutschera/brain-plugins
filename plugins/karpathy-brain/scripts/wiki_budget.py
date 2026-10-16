#!/usr/bin/env python3
"""PreToolUse hook for a persona subagent.

Usage (plugin hooks.json): python3 wiki_budget.py <person-wiki-dir> <agent-name> [limit]
- Acts only inside the subagent whose type is <agent-name> (with or without the plugin prefix).
- Blocks every tool call until <wiki>/hot.md has been read.
- Allows at most <limit> (default 5) distinct wiki pages per agent run, hot.md included.
- Blocks Grep/Bash over the wiki so pages can't be read around the budget.
Exit 2 blocks the call; stderr is shown to the agent.
"""
import json
import os
import re
import sys
from pathlib import Path

WIKI = Path(sys.argv[1]).expanduser().resolve()
AGENT = sys.argv[2]
LIMIT = int(sys.argv[3]) if len(sys.argv) > 3 else 5
HOT = WIKI / "hot.md"
STATE = Path(os.environ.get("CLAUDE_PLUGIN_DATA") or Path.home() / ".cache" / "persona-hooks")


def block(msg):
    print(msg, file=sys.stderr)
    sys.exit(2)


data = json.load(sys.stdin)
agent = data.get("agent_id")
if not agent or (data.get("agent_type") or "").split(":")[-1] != AGENT:
    sys.exit(0)

tool = data.get("tool_name", "")
inp = data.get("tool_input") or {}
cwd = Path(data.get("cwd") or os.getcwd())

STATE.mkdir(parents=True, exist_ok=True)
state_file = STATE / (re.sub(r"[^A-Za-z0-9_-]", "_", agent) + ".json")
read = json.loads(state_file.read_text()) if state_file.exists() else []


def resolve(p):
    p = Path(p).expanduser()
    return (p if p.is_absolute() else cwd / p).resolve()


def in_wiki(p):
    return p == WIKI or WIKI in p.parents


def record(p):
    read.append(str(p))
    state_file.write_text(json.dumps(read))
    sys.exit(0)


target = resolve(inp["file_path"]) if tool == "Read" and inp.get("file_path") else None

if str(HOT) not in read:
    if target == HOT:
        record(HOT)
    block(f"Read {HOT} first. Every other tool call is blocked until you do.")

if target is not None and in_wiki(target):
    if str(target) in read:
        sys.exit(0)
    if len(read) >= LIMIT:
        used = ", ".join(Path(r).relative_to(WIKI).as_posix() for r in read)
        block(f"Wiki budget used: {LIMIT} pages already read ({used}). Answer with what you have.")
    record(target)

if tool == "Grep":
    p = resolve(inp.get("path") or cwd)
    if in_wiki(p) or p in (WIKI.parent, WIKI.parent.parent):
        block(f"Don't grep the wiki. Open specific pages with Read; each counts toward the {LIMIT}-page budget.")

if tool == "Bash":
    cmd = inp.get("command", "")
    names_wiki = str(WIKI) in cmd
    if names_wiki or (in_wiki(cwd) and re.search(r"\.md\b", cmd)):
        block(f"Read wiki pages with the Read tool, not Bash; each counts toward the {LIMIT}-page budget.")

sys.exit(0)
