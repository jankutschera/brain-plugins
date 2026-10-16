#!/usr/bin/env python3
"""Stop hook: "<Name> rule, run it before you say it works."

Usage (plugin hooks.json): python3 run_check.py <Short name> <plugin:agent> <plugin:skill>
Blocks the stop when the current turn
  1. used the persona agent or its do skill, and
  2. wrote or edited a code file (main thread or any subagent), and
  3. ran nothing after the last code write.
Every other turn passes untouched. Lets the stop through on a
continuation it caused itself (stop_hook_active), so it can't loop.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

MESSAGE = "{short} rule, run it before you say it works."


def personas():
    """[(agent, do_skill, short name)] for this plugin's persona."""
    return [(sys.argv[2], sys.argv[3], sys.argv[1])]

CODE_EXT = (
    ".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".rb",
    ".java", ".kt", ".swift", ".c", ".cc", ".cpp", ".h", ".hpp", ".cs", ".php",
    ".sh", ".bash", ".zsh", ".fish", ".lua", ".sql", ".scala", ".ex", ".exs",
    ".vue", ".svelte", ".dart", ".r", ".pl",
)
# Commands that only look at or move files; running one of these isn't "running it".
INSPECT = {
    "ls", "cat", "head", "tail", "less", "more", "echo", "printf", "pwd", "wc",
    "grep", "rg", "find", "which", "file", "stat", "cd", "mkdir", "touch", "cp",
    "mv", "rm", "chmod", "diff", "tree", "sort", "uniq", "cut", "jq", "true",
    "export", "basename", "dirname", "realpath", "date", "sleep", "open",
}
GIT_READ = {"status", "diff", "log", "show", "branch", "add", "restore", "stash"}
FILE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}


def load(path):
    out = []
    try:
        with open(path) as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    except OSError:
        pass
    return out


def when(entry):
    try:
        return datetime.fromisoformat(entry["timestamp"])
    except (KeyError, ValueError, TypeError):
        return None


def content(entry):
    c = (entry.get("message") or {}).get("content")
    if isinstance(c, str):
        return [{"type": "text", "text": c}]
    return c if isinstance(c, list) else []


def is_human_prompt(entry):
    if entry.get("type") != "user" or entry.get("isMeta"):
        return False
    blocks = content(entry)
    if not blocks or any(b.get("type") == "tool_result" for b in blocks):
        return False
    origin = (entry.get("origin") or {}).get("kind")
    return origin in (None, "human")


def tool_uses(entries):
    for e in entries:
        if e.get("type") != "assistant":
            continue
        t = when(e)
        for b in content(e):
            if b.get("type") == "tool_use" and t is not None:
                yield t, b.get("name", ""), b.get("input") or {}


def strip_heredocs(cmd):
    """Drop heredoc bodies so file contents aren't mistaken for commands."""
    kept, terminators = [], []
    for line in cmd.splitlines():
        if terminators:
            if line.strip() == terminators[0]:
                terminators.pop(0)
            continue
        kept.append(line)
        terminators += re.findall(r"<<-?\s*['\"]?([A-Za-z_][A-Za-z0-9_]*)['\"]?", line)
    return "\n".join(kept)


def is_code(path):
    return path.strip("'\"").lower().endswith(CODE_EXT)


def analyze_shell(cmd):
    """Return (writes_code, runs_something) for one shell command."""
    text = strip_heredocs(cmd)
    targets = re.findall(r"(?:>>?|\btee\s+(?:-a\s+)?)\s*([^\s;&|<>]+)", text)
    targets += re.findall(r"\bsed\s+-i\S*\s+(?:'[^']*'|\"[^\"]*\"|\S+)\s+([^\s;&|]+)", text)
    writes = any(is_code(t) for t in targets)

    runs = False
    for segment in re.split(r"&&|\|\||[;|\n]", text):
        words = segment.split()
        while words and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", words[0]):
            words.pop(0)
        if not words:
            continue
        head = Path(words[0]).name
        if head in INSPECT:
            continue
        if head == "git" and len(words) > 1 and words[1] in GIT_READ:
            continue
        if head == "sed" and any(w.startswith("-i") for w in words[1:]):
            continue
        runs = True
    return writes, runs


def main():
    data = json.load(sys.stdin)
    if data.get("stop_hook_active"):
        sys.exit(0)
    transcript = data.get("transcript_path")
    if not transcript:
        sys.exit(0)

    entries = load(transcript)
    starts = [i for i, e in enumerate(entries) if is_human_prompt(e)]
    if not starts:
        sys.exit(0)
    turn = entries[starts[-1]:]
    turn_start = when(entries[starts[-1]])

    prompt_text = " ".join(b.get("text", "") for b in content(turn[0]))
    used = None
    for agent, skill, short in personas():
        if skill and f"<command-name>/{skill}</command-name>" in prompt_text:
            used = short
        for _, name, inp in tool_uses(turn):
            if name == "Skill" and skill and str(inp.get("skill", "")) == skill:
                used = short
            if name in ("Agent", "Task") and inp.get("subagent_type") in (agent, agent.split(":")[-1]):
                used = short
    if not used:
        sys.exit(0)

    calls = list(tool_uses(turn))
    sub_dir = Path(transcript).with_suffix("") / "subagents"
    for sub in sorted(sub_dir.glob("*.jsonl")) if sub_dir.is_dir() else []:
        calls += [c for c in tool_uses(load(sub)) if turn_start is None or c[0] >= turn_start]

    last_write, last_run = None, None
    for t, name, inp in calls:
        wrote = ran = False
        if name in FILE_TOOLS:
            wrote = is_code(str(inp.get("file_path") or inp.get("notebook_path") or ""))
        elif name in SHELL_TOOLS:
            wrote, ran = analyze_shell(str(inp.get("command", "")))
        if wrote and (last_write is None or t > last_write):
            last_write = t
        if ran and (last_run is None or t > last_run):
            last_run = t

    # A shell command that writes and then runs counts as running after its write.
    if last_write is not None and (last_run is None or last_run < last_write):
        print(MESSAGE.format(short=used), file=sys.stderr)
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
