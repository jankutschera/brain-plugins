---
type: source
raw: raw/github/
files: 41758
words: 33564686
date_range: 2018-01 – 2026-10
---
# GitHub (mattpocock repos and gists)

## Coverage

- **What it is:** every public non-fork repo of github.com/mattpocock (168 of 223 listed; 55 forks skipped) as shallow `--depth 1` clones, plus all 84 public gists in `_gists/`, plus `repos.json` and `gists.json` metadata. Collected 2026-10-06 per `raw/github/MANIFEST.md`; nothing was installed, built or executed.
- **Size:** 41,758 files (2,702 binary), 33.6M whitespace tokens. Most of that is code, lockfiles and generated output. One file alone (`total-typescript-monorepo/apps/written-content/scratch/.../big-file.txt`, 6.7M tokens) and `accentlab` (5.4M) dominate the count. Real prose is a few hundred thousand words.
- **Dates:** repo `pushedAt` runs 2018-01-10 (foxginger, crackapack, accentlab) to 2026-10-06 (course-video-manager). `repos.json` has no `createdAt`, so dates are last-push dates, not creation dates. Gists run 2019-05-21 to 2026-07-07.
- **Shallow clones:** no commit history beyond the tip, so evolution has to be read from CHANGELOGs, ADRs, archived repos and `_old/` folders rather than from git log.
- **Duplication:** the 20 `total-typescript-book-*` repos share one identical `book-content/` (the full Total TypeScript book, ~100K words); the 17 `pro-essentials-workshop-*` and 11 `react-typescript-tutorial-*` repos are per-section copies of the same exercise sets. Cite one copy (`total-typescript-book-010`).
- **Authorship caveats:** `CLAUDE.md`, `CONTEXT.md`, ADRs and skills in recent repos are co-written with agents but live in his repos under his rules; `rubix-cube/NOTES.md` is agent-written and quotes him. `_old/taylor-drafts/` and `_old/articles/interview-with-donny.md` in the monorepo are likely not his words and were skipped. Client and portfolio sites were skimmed for categorisation only.
- **Read in full or near full:** skills (README, CLAUDE.md, GLOSSARY, writing-for-agents, grilling, codebase-design, tdd, diagnosing-bugs, to-tickets, prototype, retro, teach, code-review, writing-* in-progress skills, setup-ts-deep-modules, ADR 0002, out-of-scope, CHANGELOG excerpts); sandcastle (README head, CLAUDE.md, CONTEXT.md head, CODING_STANDARDS, ADR 0009, out-of-scope, simple-loop prompt); evalite (what-is-evalite, readme, CLAUDE.md); ts-reset (readme, CLAUDE.md, out-of-scope, research skill, entrypoint comments); dictionary-of-ai-coding (CLAUDE.md, README intro and key entries); course-video-manager (README, CLAUDE.md, CODING_STANDARDS, CONTEXT.md entries); mise-en-place (CONTEXT.md, CLAUDE.md, prep-plan); rubix-cube (MISSION, NOTES); total-typescript-monorepo (CLAUDE.md, video workflow, any/enums/npm-package articles); Total TypeScript book (chapters 9, 11, 14, 16 passages, README, workshop.md); react-typescript-tutorial exercises; ai-hero-cli, ralph-workshop and ai-engineer-workshop prompts and skills; older READMEs (boilersuit, sextant, xstate-codegen, graph-docs-cli, make-route-map, zod-fetch, use-fsm-reducer, redux-xstate-poc, xstate-next-boilerplate, debates-stream); gists (agent-proxy, strict, open-objects, exercises note, xstate-codegen RFC, 2019 architecture notes).
- **Gaps:** most of the ~350 written-content drafts in the monorepo, the 31 CVM ADRs, sandcastle's 20 ADRs and research files, slopwatch research, and most AI Hero exercise readmes were sampled, not read.

### Repos by category (all 168)

- **Libraries and published tools** (25): ts-reset, evalite, sandcastle, zod-fetch, xstate-codegen, xstate-catalogue, sextant, graph-docs-cli, boilersuit, boilersuit-raw, make-route-map, use-fsm-reducer, redux-xstate-poc, xstate-sync-to-context, xstate-inspect-cli, ts-error-translator, json-server-wrapper, figma-xstate-plugin, xstate-test-playwright, total-typescript-helpers, total-typescript-cli, tt-upgrader, tsconfig-creator, matt-cli, vscode-xstate
- **AI tooling and AI education** (15): skills, dictionary-of-ai-coding, ai-hero-cli, ai-hero-cli-archived, ai-sdk-cache, ai-sdk-tips, mcp-server-from-prompts, markdown-streaming-demo, ai-interviewer, slopwatch, harness-claude-code-usage-repro, ai-engineer-workshop-2026-project, ralph-workshop-repo-001, ralph-workshop-repo-002, poland-ai-talk
- **Courses, workshops, talks and teaching demos** (74): total-typescript-book-005, total-typescript-book-010, total-typescript-book-015, total-typescript-book-016.5, total-typescript-book-018, total-typescript-book-020, total-typescript-book-028, total-typescript-book-030, total-typescript-book-032, total-typescript-book-040, total-typescript-book-045, total-typescript-book-050, total-typescript-book-060, total-typescript-book-065, total-typescript-book-080, total-typescript-book-082, total-typescript-book-083, total-typescript-book-085, total-typescript-book-090, total-typescript-book-095, pro-essentials-workshop-005, pro-essentials-workshop-010, pro-essentials-workshop-015, pro-essentials-workshop-016.5, pro-essentials-workshop-018, pro-essentials-workshop-020, pro-essentials-workshop-028, pro-essentials-workshop-030, pro-essentials-workshop-032, pro-essentials-workshop-040, pro-essentials-workshop-045, pro-essentials-workshop-050, pro-essentials-workshop-060, pro-essentials-workshop-065, pro-essentials-workshop-080, pro-essentials-workshop-083, pro-essentials-workshop-085, pro-essentials-cut-down, pro-essentials-cut-down-to-chapters, react-typescript-tutorial-01, react-typescript-tutorial-02, react-typescript-tutorial-03, react-typescript-tutorial-04, react-typescript-tutorial-05, react-typescript-tutorial-06, react-typescript-tutorial-07, react-typescript-tutorial-08, react-typescript-tutorial-09, react-typescript-tutorial-fake, react-typescript-tutorial-helpers, react-day-berlin-react-types, react-finland-talk, vscode-day-talk, workshops, xstate-sandpack-tutorials, xstate-tutorial, neverthrow-tutorial, debates-stream, tt-package-demo, pkg-demo, typescript-node, esbuild-node, project-references-demo, as-prop-perf-demo, total-typescript-monorepo-template, my-monorepo, turbo-ignore-demo, turborepo-stately-demo, cypress-xstate-demo, xstate-real-world-app, xstate-stream-demo-app, xstate-next-boilerplate, xstate-inspect-storybook-example, package-tools
- **Internal tooling and personal workspaces** (13): total-typescript-monorepo, course-video-manager, mise-en-place, video-ideas, obs-stinger, new-mattpocock, mattpocock, rubix-cube, chess-opening-learner, matt-product-boilerplate, actions-pr-merge-check, kelvin-chat, practice-cli
- **Experiments, repros and early boilerplates** (29): xstate-inspect-repro, xstate-form-test, xstate-command-palette, multi-step-form, create-t3-turbo-test, gql-tada-testing, full-stack-ui, cdk-recipes, netlify-test, gatsby-test, gatsby-pomodoro, gatsby-starter-storybook-mdx, gatsby-starter-netlify-cms, storybook-components, ui_experiments, solve-the-format, graphql-rest-contracts, lambda-local-watch, aws-serverless-mongo-api, default_setup, redux_default_app, node-react-mysql-spa, react-boilerplate-custom, react-typescript-boilerplate, day-tracker-typescript, bubble-sort, one-coding-test, jazz-chord-finder, cypress-job-search
- **Client, portfolio and pre-2019 work (low weight)** (12): accentlab, crackapack, voicehacker, voicehacker-accents, foxginger, freelancer, frauleinlouise-static, louiseburfitt-new, andrebatista.dev, canarycare, race-manager, wordpress-react-simplified

## What this source shows about him

- He builds his AI-era work on classic engineering fundamentals rather than new process, and says so in his most-starred repo.
  > "Software engineering fundamentals matter more than ever." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- He treats misalignment as the main failure mode and fixes it by having the agent interrogate him before any code is written.
  > "The most common failure mode in software development is misalignment." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- He designs code, and has agents design code, as deep modules tested through their interfaces.
  > "Design **deep modules**: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)
- He thinks feedback loops are what make both agents and debuggers effective.
  > "Build the right feedback loop, and the bug is 90% fixed." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- He uses a shared domain glossary in nearly every recent repo, so humans and agents use the same short words.
  > "Names the raw materials, containers, channels, activities, and disciplines of the work so that Matt and AI agents can speak the same language." — [github/mise-en-place/CONTEXT.md](https://github.com/mattpocock/mise-en-place/blob/HEAD/CONTEXT.md)
- As a TypeScript teacher, he frames the language as JavaScript with types and type errors as communication.
  > "The right way to think about TypeScript today is as "JavaScript with types"." — [github/total-typescript-book-010/book-content/chapters/09-typescript-only-features.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/book-content/chapters/09-typescript-only-features.md)
- He teaches through problem/solution exercises where tests are the success signal.
  > "You'll know if you've succeeded because the tests will pass." — [github/total-typescript-book-010/README.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/README.md)
- He writes about learning as a design problem: retention over fluency, difficulty used deliberately.
  > "Fluency can give the user an illusory sense of mastery, but storage strength is the real goal." — [github/skills/skills/productivity/teach/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/teach/SKILL.md)
- He runs his content business as a modelled system with named disciplines and failure modes.
  > "The morning ritual. **Work Clean**: Prep before Ship, every day, in a fixed order." — [github/mise-en-place/prep-plan.md](https://github.com/mattpocock/mise-en-place/blob/HEAD/prep-plan.md)
- His topics move from Redux code generators (2018) to XState (2020-23) to TypeScript (2023-24) to AI agents (2025-26), but a few threads stay: generate from one source of truth, type safety, and learning paths.
  > "**Don't write ten files, write one.** Define your state and actions in a JSON file and watch as your code writes itself." — [github/boilersuit/README.md](https://github.com/mattpocock/boilersuit/blob/HEAD/README.md)
- His register changed from hype in early READMEs to a deliberately flat, de-hyped style.
  > "Write in a plain, de-hyped register. No selling the concept" — [github/dictionary-of-ai-coding/CLAUDE.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/CLAUDE.md)

## Notable pieces

- **skills/README.md** (277K stars by `repos.json`) is his manifesto for agent-assisted engineering: four failure modes, each paired with a classic book quote and a skill.
  > "I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- **skills/.../writing-for-agents/SKILL.md** is his theory of prompting: context pointers, the two loads, completion criteria, leading words, pruning.
  > "A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)
- **skills/.../grilling/SKILL.md** is the interview primitive behind most of his planning skills.
  > "Finding _facts_ is your job, never the user's." — [github/skills/skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/grilling/SKILL.md)
- **skills/.../diagnosing-bugs/SKILL.md** is a gated six-phase debugging discipline.
  > "If you have a **tight** pass/fail signal for the bug (one that goes red on _this_ bug), you will find the cause" — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- **skills/.../teach/SKILL.md** shows his learning theory: mission, zone of proximal development, knowledge vs skills vs wisdom.
  > "To learn at a deep level, the user needs three things:" — [github/skills/skills/productivity/teach/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/teach/SKILL.md)
- **dictionary-of-ai-coding/README.md** is his plain-English glossary of AI coding, with a political edge about manufactured confusion.
  > "**The vocabulary of AI coding, translated into plain English**." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)
- **mise-en-place/CONTEXT.md** models his own content business: Notes, Hooks, Bricks, Pitches, Revenue vs Audience Deliverables, Work Clean.
  > "Lightweight and meant to be killed cheaply — if you can't package a Pitch, you don't have one." — [github/mise-en-place/CONTEXT.md](https://github.com/mattpocock/mise-en-place/blob/HEAD/CONTEXT.md)
- **course-video-manager/CONTEXT.md** shows how he plans a course video: learning goals, beats, clip mockups, animatic, script.
  > "It is the first step of the authoring flow: Learning Goals → Lessons, Videos and Beats → Script → recording → article." — [github/course-video-manager/CONTEXT.md](https://github.com/mattpocock/course-video-manager/blob/HEAD/CONTEXT.md)
- **course-video-manager/CODING_STANDARDS.md** has his strongest statement on `any`, with an incident from his own code.
  > "An `any` switches the type checker off for every value that flows through it, and those values keep flowing long after the line that produced them." — [github/course-video-manager/CODING_STANDARDS.md](https://github.com/mattpocock/course-video-manager/blob/HEAD/CODING_STANDARDS.md)
- **sandcastle** (README, CODING_STANDARDS, ADRs, `.out-of-scope/`) is his AFK agent orchestration library and his most complete example of library governance.
  > "Every built-in provider is a standing maintenance commitment" — [github/sandcastle/.out-of-scope/built-in-agent-providers.md](https://github.com/mattpocock/sandcastle/blob/HEAD/.out-of-scope/built-in-agent-providers.md)
- **ts-reset/.out-of-scope/promise-catch-in-recommended.md** documents 20 failed approaches before declaring a fix impossible.
  > "We exhaustively investigated 30+ approaches to solve this. None succeeded." — [github/ts-reset/.out-of-scope/promise-catch-in-recommended.md](https://github.com/mattpocock/ts-reset/blob/HEAD/.out-of-scope/promise-catch-in-recommended.md)
- **evalite** maps LLM evaluation onto the test-runner mental model, local-only.
  > "**Evals are to AI-powered apps what tests are to regular apps**." — [github/evalite/apps/evalite-docs/src/content/docs/what-is-evalite.mdx](https://github.com/mattpocock/evalite/blob/HEAD/apps/evalite-docs/src/content/docs/what-is-evalite.mdx)
- **Total TypeScript book, chapter 9** gives his position on enums and namespaces, and its limits.
  > "But I prefer writing code in the spirit of the language I'm using." — [github/total-typescript-book-010/book-content/chapters/09-typescript-only-features.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/book-content/chapters/09-typescript-only-features.md)
- **graph-docs-cli/README.md** (2022) shows his early idea of docs as a dependency graph of concepts.
  > "What you end up with is a graph of **optimal paths to learn any piece of information**." — [github/graph-docs-cli/README.md](https://github.com/mattpocock/graph-docs-cli/blob/HEAD/README.md)
- **_gists/5b3d76ea21f5f698aefded47a9cea3b1** (agent-proxy, 2026) is a tool for seeing what fills Claude Code's context.
  > "A zero-dependency logging proxy that sits between Claude Code and the Anthropic" — [github/_gists/5b3d76ea21f5f698aefded47a9cea3b1/README.md](https://gist.github.com/mattpocock/5b3d76ea21f5f698aefded47a9cea3b1)

## Related

- Principles: [Communication and shared language](../principles/communication-and-shared-language.md) · [Own the process](../principles/own-the-process.md) · [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md) · [Learning at the edge](../principles/learning-at-the-edge.md) · [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md) · [Context is a scarce budget](../principles/context-is-a-scarce-budget.md) · [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md) · [Less is more](../principles/less-is-more.md) · [Never trust an LLM](../principles/never-trust-an-llm.md) · [Alignment before code](../principles/alignment-before-code.md) · [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md) · [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md) · [Revise in public](../principles/revise-in-public.md)
- Methods: [Diagnosing bugs](../methods/diagnosing-bugs.md) · [Content production](../methods/content-production.md) · [TDD at agreed seams](../methods/tdd-at-agreed-seams.md) · [Deep modules](../methods/deep-modules.md) · [Writing for agents](../methods/writing-for-agents.md) · [Grilling](../methods/grilling.md) · [Problem/solution teaching](../methods/problem-solution-teaching.md) · [Build your own tools](../methods/build-your-own-tools.md) · [Evals as tests](../methods/evals-as-tests.md) · [Prototype to answer a question](../methods/prototype-to-answer-a-question.md) · [The main flow](../methods/the-main-flow.md) · [AFK loops](../methods/afk-loops.md) · [Context hygiene](../methods/context-hygiene.md) · [Review and retro](../methods/review-and-retro.md)
