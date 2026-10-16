---
type: source
raw: raw/blog/
files: 265
words: 194456
date_range: 2024-11 – 2026-10
---
# AI Hero (aihero.dev)

## Coverage

- 265 files, 194,456 words (`wc -w`, including YAML headers), collected 2026-10-06 from https://www.aihero.dev/ (Matt Pocock's AI Hero site). No login and no paywall bypass.
- Discovery: sitemap.xml, sitemap.md, the public search API, RSS, listing pages and the resource trees in workshop landing pages (527 lesson URLs). Posts, lists, skill pages, cohort/event pages and workshop landing pages were saved from the site's official markdown twins (`<url>.md`) with MDX components left in. Pages without a twin (the AI Coding Dictionary, skills changelog pages, homepage, newsletter) were scraped with firecrawl. Only workshop lessons the server renders publicly were saved, with their video transcripts appended under `### Video Transcript`.
- Rough split by content type: 72 posts and articles (about 56k words, 2024-11 to 2026-03, plus a few later posts); 40 skill documentation and changelog pages (about 57k words, 2026-03 to 2026-10); 72 AI Coding Dictionary files (index plus entries, about 22k words, undated); 70 workshop pages (about 36k words, undated landing pages and lessons, 29 with video transcripts); 5 cohort and event sales pages (about 13k words); 6 landing and list pages.
- `published` is the JSON-LD `datePublished` of the HTML page and may equal the last update. Several older posts were edited later (for example `how-to-improve-your-llm-powered-app.md` mentions Claude 4.6; `plan-mode-introduction.md` carries a later "Update" note).
- 181 files carry `author: "Matt Pocock"`. The rest (workshop pages, cohort and event pages, the homepage) are in his first-person voice but have no author field. Sales and course pages are treated as low-weight evidence.
- Gaps: `/newsletter` is a signup form only, with no archive. The skill pages from 2026-07 onward read like documentation written to a style guide (short sentences, "One user reported…" FAQs compiled from user questions), so their wording may be partly agent-assisted; the corpus does not say.
- The site moves from AI engineering (building LLM apps with the Vercel AI SDK, MCP and evals, 2024-11 to 2025) to AI-assisted coding with Claude Code and his open-source skills repo (2026).

## What this source shows about him

- He believes AI coding raises the value of classic engineering instead of replacing it.
  > "But the principles apply harder to AI than they ever did to humans." — [blog/tracer-bullets.md](https://www.aihero.dev/tracer-bullets) · 2026-01
- He thinks the cost of software has moved from writing code to reading and maintaining it.
  > "Writing code got cheap. Reading it did not." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10
- He keeps thinking and decisions for the human and gives agents the legwork.
  > "The moment you start delegating your thinking to an LLM, you're screwed." — [blog/personal-software-is-insane-in-the-age-of-ai-u2hx2.md](https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2) · 2025-11
- He treats agents as capable but memoryless colleagues who need strict process.
  > "AI is not a super-powered developer. It's a new starter with no memory." — [blog/how-to-make-codebases-ai-agents-love.md](https://www.aihero.dev/how-to-make-codebases-ai-agents-love) · 2026-02
- He sees the codebase, not the prompt, as the main lever on agent output, and pushes deep modules with small interfaces.
  > "Your codebase, way more than your prompt or your `AGENTS.md` file, is the biggest influence on AI's output." — [blog/how-to-make-codebases-ai-agents-love.md](https://www.aihero.dev/how-to-make-codebases-ai-agents-love) · 2026-02
- He treats context as a scarce budget and organises his workflow around a "smart zone".
  > "the more you put in the context window, the worse the AI is going to be." — [blog/creating-the-perfect-claude-code-status-line.md](https://www.aihero.dev/creating-the-perfect-claude-code-status-line) · 2025-10
- He prefers deterministic mechanisms (checks, hooks, scripts, workflows) over trusting a model or a line of prose.
  > "A check can fail. A sentence in a Markdown file cannot." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10
- He was already preferring workflows to agents in 2025, before his AI-coding phase.
  > "I don't know whether it's me being old and boring, but I am more excited by workflows than agents." — [blog/what-is-an-agent.md](https://www.aihero.dev/what-is-an-agent) · 2025-09
- He insists on reaching shared understanding with the agent before any code, through "grilling".
  > "The technique exists because agents fill gaps silently." — [blog/ai-coding-dictionary__grilling.md](https://www.aihero.dev/ai-coding-dictionary/grilling) · n.d.
- He works in thin vertical slices and fast feedback loops, drawing on The Pragmatic Programmer.
  > "The rate at which you can get feedback is your speed limit. Never outrun your headlights." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
- He cares intensely about precise names and shared vocabulary, which is why he wrote his own AI Coding Dictionary.
  > "consistent language is the whole point, and a term nobody uses consistently is worse than no term." — [blog/skills-codebase-design.md](https://www.aihero.dev/skills-codebase-design) · 2026-07
- He wants evidence, not claims, before trusting agent output, including his own skills.
  > "`teach` is not reliable enough to trust unchecked, and no skill built on an LLM is." — [blog/skills-teach.md](https://www.aihero.dev/skills-teach) · 2026-07
- He changes his mind in public and marks the change, as with plan mode.
  > "I wrote this in January 2026, and my thinking has changed. I no longer use plan mode." — [blog/plan-mode-introduction.md](https://www.aihero.dev/plan-mode-introduction) · 2026-01
- He builds the tools he wants when they do not exist, and runs them on his own projects.
  > "It feels crazy to me that there's no TypeScript-native, local-first tool for testing LLM-powered apps." — [blog/evalite-an-early-preview.md](https://www.aihero.dev/evalite-an-early-preview) · 2024-12
- He teaches by demystifying: strip the mystery, show the plain mechanism, then build.
  > "There's nothing particularly fancy going on - it's just tool definitions inside the system prompt." — [blog/what-are-tools.md](https://www.aihero.dev/what-are-tools) · 2025-09
- He positions his audience as "real engineers" against vibe coders.
  > "Fancy tools can't eliminate engineering. In fact, the better the tools get, the wider the gulf gets between vibe coders and real engineers." — [blog/cohorts__ai-coding-for-real-engineers-m0k0w.md](https://www.aihero.dev/cohorts/ai-coding-for-real-engineers-m0k0w) · 2026-06

## Notable pieces

- `never-run-claude-init.md` is his sharpest statement on instruction files: delete generated ones, keep CLAUDE.md nearly empty, trust the explore step.
  > "Never run it. If you find one that was auto-generated, delete it." — [blog/never-run-claude-init.md](https://www.aihero.dev/never-run-claude-init) · 2026-02
- In the same post he shows his entire CLAUDE.md, one line long.
  > "you are on WSL on Windows" — [blog/never-run-claude-init.md](https://www.aihero.dev/never-run-claude-init) · 2026-02
- `plan-mode-introduction.md` is the clearest public reversal: a January guide that says plan mode is essential, with a later note that he dropped it for grilling.
  > "Now I just have a conversation with the agent, like I would with a colleague." — [blog/plan-mode-introduction.md](https://www.aihero.dev/plan-mode-introduction) · 2026-01
- `how-to-make-codebases-ai-agents-love.md` sets out the grey-box module idea: the human designs interfaces and the agent fills them.
  > "You own the interface. AI owns the implementation. Tests keep it honest." — [blog/how-to-make-codebases-ai-agents-love.md](https://www.aihero.dev/how-to-make-codebases-ai-agents-love) · 2026-02
- `tips-for-ai-coding-with-ralph-wiggum.md` (3,900 words) is his long-form guide to autonomous loops, and shows the scepticism behind them.
  > "Great programmers don't trust their own code. They don't trust external libraries. They especially don't trust their colleagues." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
- `ways-ai-coding-has-rewired-my-brain.md` is the most personal account of how AI changed his practice.
  > "I have been writing all the software that I work on completely 100% AI-contributed for a few months now." — [blog/ways-ai-coding-has-rewired-my-brain.md](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain) · 2026-03
- `5-agent-skills-i-use-every-day.md` introduces his skills as process for memoryless agents.
  > "Right now, process has never been more important." — [blog/5-agent-skills-i-use-every-day.md](https://www.aihero.dev/5-agent-skills-i-use-every-day) · 2026-03
- `skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md` (2026-10) is the latest snapshot of his thinking: review as bottleneck, retro, and deterministic loops over agent orchestration.
  > "The agent loop is worse than a deterministic loop." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10
- `skills-writing-for-agents.md` captures how he writes for agents: delete, prune, use leading words.
  > "Its default fix is to delete, not to explain." — [blog/skills-writing-for-agents.md](https://www.aihero.dev/skills-writing-for-agents) · 2026-07
- `skills-wait-what.md` shows his belief that a single well-chosen word can be a whole mechanism.
  > "An agent that hears \"be brief\" writes clipped fragments. An agent that hears \"wait, you lost me\" backs up and explains." — [blog/skills-wait-what.md](https://www.aihero.dev/skills-wait-what) · 2026-08
- `personal-software-is-insane-in-the-age-of-ai-u2hx2.md` states his rule that AI does the grunt work and he keeps the thinking.
  > "Everything the AI touches in my workflow is pure grunt work." — [blog/personal-software-is-insane-in-the-age-of-ai-u2hx2.md](https://www.aihero.dev/personal-software-is-insane-in-the-age-of-ai-u2hx2) · 2025-11
- `what-are-llms-used-for.md` is the 2025 root of his determinism-first stance.
  > "**Deterministic systems should be your default choice for any task**, until you hit a barrier which can only be solved by an LLM." — [blog/what-are-llms-used-for.md](https://www.aihero.dev/what-are-llms-used-for) · 2025-03
- The AI Coding Dictionary entry on AX names the idea behind most of his 2026 advice.
  > "The instinct is to blame the model or rewrite the prompt; the fix is more often in the repo." — [blog/ai-coding-dictionary__ax.md](https://www.aihero.dev/ai-coding-dictionary/ax) · n.d.
- The skill FAQs record weaknesses openly, for example in `skills-wayfinder.md`.
  > "This is the sharpest open complaint about wayfinder, and nobody has fixed it yet." — [blog/skills-wayfinder.md](https://www.aihero.dev/skills-wayfinder) · 2026-07

## Related

- Principles: [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md) · [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md) · [Context is a scarce budget](../principles/context-is-a-scarce-budget.md) · [Humans own the strategy](../principles/humans-own-the-strategy.md) · [Less is more](../principles/less-is-more.md) · [Never trust an LLM](../principles/never-trust-an-llm.md) · [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md) · [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md) · [Own the process](../principles/own-the-process.md) · [Revise in public](../principles/revise-in-public.md) · [The codebase is the agent's environment](../principles/the-codebase-is-the-agents-environment.md) · [Alignment before code](../principles/alignment-before-code.md) · [Communication and shared language](../principles/communication-and-shared-language.md) · [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md)
- Methods: [Evals as tests](../methods/evals-as-tests.md) · [The main flow](../methods/the-main-flow.md) · [AFK loops](../methods/afk-loops.md) · [Grilling](../methods/grilling.md) · [Context hygiene](../methods/context-hygiene.md) · [Build your own tools](../methods/build-your-own-tools.md) · [Deep modules](../methods/deep-modules.md) · [Prototype to answer a question](../methods/prototype-to-answer-a-question.md) · [TDD at agreed seams](../methods/tdd-at-agreed-seams.md) · [Problem/solution teaching](../methods/problem-solution-teaching.md) · [Writing for agents](../methods/writing-for-agents.md) · [Content production](../methods/content-production.md) · [Running the business](../methods/running-the-business.md) · [Diagnosing bugs](../methods/diagnosing-bugs.md)
