# brain-plugins

Claude Code plugins that let an agent work the way a specific person builds and teaches. Each plugin is built from a wiki of that person's public work, and every claim in the wiki carries a verbatim quote linked to its public source.

| Plugin | Person | Wiki | You get |
|---|---|---|---|
| `karpathy-brain` | Andrej Karpathy | 47 pages, 1,430 quotes | `karpathy` subagent, `/karpathy-brain:teach` |
| `pocock-brain` | Matt Pocock | 41 pages, 837 quotes | `pocock` subagent, `/pocock-brain:teach` |

These are unofficial. Neither person made, reviewed or endorsed them.

An explainer page with the full rules and how the wikis were built is in [`index.html`](index.html).

## Install

```
/plugin marketplace add jankutschera/brain-plugins
/plugin install karpathy-brain@brain-plugins
/plugin install pocock-brain@brain-plugins
```

The hooks need `python3` on your PATH.

## Use

```
/karpathy-brain:teach Write a numerically stable softmax in numpy and show why it is stable
/pocock-brain:teach Add a typed retry helper to src/http.ts
```

The `teach` skill hands your task to the persona subagent, grades the answer against the person's 7 rules (PASS / PARTIAL / FAIL with evidence), checks the footer and citations with tools, and runs at most one revision round. You can also call the subagent directly, for example "use the karpathy-brain:karpathy agent to …".

## What's inside a plugin

```
plugins/karpathy-brain/
├── .claude-plugin/plugin.json
├── agents/karpathy.md         the persona: 7 rules, wiki grounding, output contract
├── skills/teach/SKILL.md      delegate → grade → one revision → show
├── hooks/hooks.json           the three guards below
├── scripts/                   hook scripts (Python, stdlib only)
└── wiki/                      hot.md, rules.md, index.md, log.md, principles/, methods/, sources/
```

The hooks keep the persona honest:

| Hook | Event | What it does |
|---|---|---|
| `wiki_budget.py` | PreToolUse | Inside the persona subagent only: blocks every tool until `wiki/hot.md` is read, then allows at most 5 wiki pages per run |
| `footer_check.py` | SubagentStop | The answer must end with **Ran / Came out / Changed**, and every mention of the person must cite a wiki page that exists |
| `run_check.py` | Stop | If a turn used the persona and wrote code but ran nothing afterwards, it blocks once: "Karpathy rule, run it before you say it works." |

## How the wikis were built

1. **Collect** everything the person published publicly (X, YouTube, blog, GitHub, talks on other channels), raw and unsummarized, then freeze it with checksums.
2. **Extract** candidate quotes per source; a script checks each one verbatim against the raw files.
3. **Write** principle, method and source pages. No claim without a quote directly under it.
4. **Claim check** with separate fresh agents: does the quote support the claim, did this person say it, is the date right? For Karpathy this caught 64 overstated claims, a Feynman line credited to him, and 25 quotes from an LLM-cleaned transcript; all were fixed.
5. **Rules**: the 7 strongest rules that appear in at least 2 different source types.
6. **Persona**: the agent, the teach skill and the hooks above.

`wiki/log.md` in each plugin records the build steps and check results.

## License

MIT for the code, prompts and wiki prose. Quoted passages remain the work of the people quoted. See [LICENSE](LICENSE).
