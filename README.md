# brain-plugins

Claude Code plugins that let an agent work the way a specific person builds and teaches. Each plugin is built from a wiki of that person's public work, and every claim in the wiki carries a verbatim quote linked to its public source.

| Plugin | Person | Wiki | You get |
|---|---|---|---|
| `karpathy-brain` | Andrej Karpathy | 47 pages, 1,430 quotes | `karpathy` subagent, `/karpathy-brain:do`, `/karpathy-brain:review` |
| `pocock-brain` | Matt Pocock | 41 pages, 837 quotes | `pocock` subagent, `/pocock-brain:do`, `/pocock-brain:review` |

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
/pocock-brain:do Add a typed retry helper to src/http.ts
/karpathy-brain:do Find out why the loss in train.py stops going down after epoch 3
/pocock-brain:review 42            # a GitHub PR number or URL
/karpathy-brain:review src/model.py
/pocock-brain:review diff          # your uncommitted changes
```

- **`do`** hands your task to the persona subagent. It then grades the answer against the person's 7 rules (PASS / PARTIAL / FAIL with evidence), checks the footer and citations with tools, and runs at most one revision round.
- **`review`** grades existing work against the same 7 rules: files, a folder, your git diff, a GitHub PR or a plan. It changes nothing and returns a grade table and the top 3 fixes, each with the person's own words from `wiki/rules.md` as the reason.
- **The subagent** can also be called directly, for example "use the karpathy-brain:karpathy agent to …".

## When to use which

| Situation | Use |
|---|---|
| You want a feature built without the agent running off: scope first, a test first, then small steps | `/pocock-brain:do` |
| Something is broken or you want to understand it: predict, run, compare, rebuild the smallest version | `/karpathy-brain:do` |
| You want a second opinion on code, a PR or a plan, whoever wrote it | `/…:review` |
| You want to learn something with an exercise before the answer | either `do`, phrased as "teach me …" |
| You want to know what the person actually said about a topic, with a source | read `wiki/hot.md`, then `wiki/index.md` |

They don't help with work outside software, such as copy, ads or email: the rules are about building and explaining code.

## What's inside a plugin

```
plugins/karpathy-brain/
├── .claude-plugin/plugin.json
├── agents/karpathy.md         the persona: 7 rules, wiki grounding, output contract
├── skills/do/SKILL.md         delegate → grade → one revision → show
├── skills/review/SKILL.md     read the work → grade → top 3 fixes (read-only)
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
6. **Persona**: the agent, the do and review skills, and the hooks above.

`wiki/log.md` in each plugin records the build steps and check results.

## License

MIT for the code, prompts and wiki prose. Quoted passages remain the work of the people quoted. See [LICENSE](LICENSE).
