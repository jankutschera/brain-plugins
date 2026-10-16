"""Pipe tests for the persona hooks in every plugin.

Run from the repo root: python3 -m unittest discover tests
Each hook is fed the JSON a real Claude Code hook receives on stdin.
"""
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = {"karpathy-brain": ("karpathy", "Karpathy", r"\b(Karpathy|Andrej)\b"),
           "pocock-brain": ("pocock", "Pocock", r"\b(Pocock|Matt)\b")}
FOOTER = "\n**Ran:** python3 x.py\n**Came out:** ok\n**Changed:** nothing"


def run(script, args, payload, env=None):
    stdin = payload if isinstance(payload, str) else json.dumps(payload)
    r = subprocess.run(["python3", str(script), *args], input=stdin,
                       capture_output=True, text=True, env=env)
    return r.returncode


def transcript(skill, events):
    t = Path(tempfile.mkdtemp()) / "t.jsonl"
    lines = [dict(type="user", timestamp="2026-10-16T10:00:00",
                  message=dict(content=f"<command-name>/{skill}</command-name> task"))]
    for i, (name, inp) in enumerate(events):
        lines.append(dict(type="assistant", timestamp=f"2026-10-16T10:00:{i + 1:02d}",
                          message=dict(content=[dict(type="tool_use", name=name, input=inp)])))
    t.write_text("\n".join(json.dumps(line) for line in lines))
    return str(t)


def each_plugin():
    for plugin, (agent, short, name_re) in PLUGINS.items():
        p = ROOT / "plugins" / plugin
        yield p, p / "wiki", p / "scripts", agent, short, name_re, f"{plugin}:{agent}", plugin


class HookTests(unittest.TestCase):
    def test_wiki_budget(self):
        for p, wiki, sc, agent, _, _, full, _ in each_plugin():
            env = dict(os.environ, CLAUDE_PLUGIN_DATA=tempfile.mkdtemp())
            hook, args = sc / "wiki_budget.py", [str(wiki), agent]
            me = dict(agent_id="a1", agent_type=full, cwd="/tmp")
            ls = dict(tool_name="Bash", tool_input={"command": "ls"})
            self.assertEqual(run(hook, args, dict(ls, cwd="/tmp"), env), 0, "main thread is never limited")
            self.assertEqual(run(hook, args, dict(ls, agent_id="x", agent_type="other:agent"), env), 0)
            self.assertEqual(run(hook, args, dict(me, **ls), env), 2, "blocked before hot.md")
            hot = dict(tool_name="Read", tool_input={"file_path": str(wiki / "hot.md")})
            self.assertEqual(run(hook, args, dict(me, **hot), env), 0)
            pages = sorted(wiki.rglob("*.md"))
            pages = [pg for pg in pages if pg.name != "hot.md"][:5]
            for i, pg in enumerate(pages):
                read = dict(tool_name="Read", tool_input={"file_path": str(pg)})
                self.assertEqual(run(hook, args, dict(me, **read), env), 0 if i < 4 else 2, f"page {i + 2}")
            grep = dict(tool_name="Grep", tool_input={"path": str(wiki)})
            self.assertEqual(run(hook, args, dict(me, **grep), env), 2, "grep over the wiki")

    def test_footer_check(self):
        for p, wiki, sc, agent, short, name_re, full, _ in each_plugin():
            hook, args = sc / "footer_check.py", [str(wiki), agent, name_re]

            def check(msg, **extra):
                return run(hook, args, dict(dict(agent_type=full, last_assistant_message=msg), **extra))

            self.assertEqual(run(hook, args, dict(agent_type="other:agent", last_assistant_message="x")), 0)
            self.assertEqual(check("done"), 2, "missing footer")
            self.assertEqual(check(f"{short} says so." + FOOTER), 2, "uncited name")
            self.assertEqual(check(f"{short.lower()} says so." + FOOTER), 2, "lowercase name is still a name")
            self.assertEqual(check(f"{short} says so (wiki/nope.md)." + FOOTER), 2, "missing page")
            self.assertEqual(check(f"{short} says so (wiki/../agents/{agent}.md)." + FOOTER), 2, "page outside the wiki")
            self.assertEqual(check(f"{short} says so (wiki/rules.md)." + FOOTER), 0)
            self.assertEqual(check("done", stop_hook_active=True), 0, "one correction round only")
            self.assertEqual(run(hook, args, "not json"), 0, "unreadable input is skipped")

    def test_run_check(self):
        for p, wiki, sc, agent, short, _, full, plugin in each_plugin():
            hook, args = sc / "run_check.py", [short, full, f"{plugin}:do"]
            w = ("Write", {"file_path": "/tmp/a.py"})
            r = ("Bash", {"command": "python3 /tmp/a.py"})
            self.assertEqual(run(hook, args, dict(transcript_path=transcript(f"{plugin}:do", [w]))), 2)
            self.assertEqual(run(hook, args, dict(transcript_path=transcript(f"{plugin}:do", [w, r]))), 0)
            self.assertEqual(run(hook, args, dict(transcript_path=transcript("other-brain:do", [w]))), 0)
            agent_call = ("Agent", {"subagent_type": full})
            self.assertEqual(run(hook, args, dict(transcript_path=transcript("other", [agent_call, w]))), 2)
            self.assertEqual(run(hook, args, dict(stop_hook_active=True,
                                                  transcript_path=transcript(f"{plugin}:do", [w]))), 0)


if __name__ == "__main__":
    unittest.main()
