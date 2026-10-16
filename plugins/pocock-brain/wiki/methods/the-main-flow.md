---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 25
first_seen: 2025-10
last_seen: 2026-10
---
# The main flow

His AI coding process is a chain from idea to merged code: grill, write a spec (the destination), split it into tickets (the journey), implement each ticket in a fresh context, review, and run a retro that improves the environment.
  > "grill-with-docs → to-spec → to-tickets → implement → code-review → retro" — [blog/skills-retro.md](https://www.aihero.dev/skills-retro) · 2026-10

## Evidence

- He calls it the flow all his work runs through.
  > "This is the main flow that all of my work runs through." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=993s) · 2026-07
- Two documents carry work across context windows.
  > "We need something to document the destination. And we need something to document the journey." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=1775s) · AI Engineer
- The spec exists because sessions end, and only records what was said.
  > "The spec exists because context windows end." — [blog/skills-to-spec.md](https://www.aihero.dev/skills-to-spec) · 2026-04
  > "If the spec states something you never said, that is a defect." — [blog/skills-to-spec.md](https://www.aihero.dev/skills-to-spec) · 2026-04
- Humans plan by day; agents implement at night.
  > "Day shift is planning/review/QA, night shift is AFK implementation." — [x/2026-04.md](https://x.com/mattpocockuk/status/2048159313357598989) · 2026-04
- He built the flow as a skill because people kept asking for it.
  > "I almost didn't create a skill for this because it's so simple, but people kept asking "what's the flow?"" — [blog/skills__skills-changelog-v1-1-wayfinder-to-spec-to-tickets-grilling-improvements.md](https://www.aihero.dev/skills/skills-changelog-v1-1-wayfinder-to-spec-to-tickets-grilling-improvements) · 2026-07

## How it shows up

1. Grill until aligned (see [Grilling](grilling.md)).
  > "You just grill. You turn that grilling into a spec. And then you just run some kind of implement loop over those tickets" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=2622s) · The Pragmatic Engineer
2. `to-spec` synthesises the conversation without re-interviewing.
  > "Turn the current conversation into a spec and publish it to the issue tracker. No interview, just synthesizes what you've already discussed." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
3. `to-tickets` cuts the spec into vertical tracer-bullet slices, each sized for one fresh context window, with blocking relationships.
  > "Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests): vertical, NOT a horizontal slice of one layer" — [github/skills/skills/engineering/to-tickets/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/to-tickets/SKILL.md)
  > "They're a task graph with blocking relationships between them." — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=219s) · 2026-10
4. He does not read the AI-written plan or tickets he already aligned on.
  > "Am I going to review these issues? Absolutely not." — [youtube/2026-03-18_hX7yG1KVYhI_building-a-real-feature-with-claude.md](https://www.youtube.com/watch?v=hX7yG1KVYhI&t=1856s) · 2026-03
5. Implement each ticket in a fresh session, often AFK, and never reopen the plan (skill doc, supporting evidence).
  > "It never reopens the plan." — [blog/skills-implement.md](https://www.aihero.dev/skills-implement) · 2026-07
6. Review in a fresh context, then a human QA pass that imposes taste.
  > "QA is how I then um impose my uh opinions back onto the code base, how I impose my taste." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4367s) · AI Engineer
7. Retro: turn mistakes into checks (see [Review and retro](review-and-retro.md)).
  > "So the loop is: find a mistake, run `/retro`, and make the mistake impossible next time. Your `AGENTS.md` gets shorter over time, not longer." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10
8. Delete the spec once it lives in the code.
  > "The way I think about specs is they are temporary artifacts that are supposed to be discarded" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=1076s) · Unhandled Exception Podcast
- For work too big for one session, Wayfinder maps the "fog of war" as decision tickets first, and he uses it beyond code.
  > "You have to clear the fog of war." — [youtube/2026-07-30_F3lL98Pj90o_wayfinder-nothing-is-too-big-to.md](https://www.youtube.com/watch?v=F3lL98Pj90o&t=33s) · 2026-07
  > "I'm using Wayfinder for literally everything, even non-coding stuff." — [youtube/2026-07-08_A8mokin_YOs_new-skills-v1-1-brings-wayfinder.md](https://www.youtube.com/watch?v=A8mokin_YOs&t=831s) · 2026-07

## Tensions and evolution

- The October 2025 version was multi-phase plans in plan mode, stored as GitHub issues.
  > "Make the plan multihase is really, really nice" — [youtube/2025-10-27_kZ-zzHVUrO4_how-i-use-claude-code-for.md](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=259s) · 2025-10
- By March 2026 it was "seven phases" with a Kanban board instead of sequential plans.
  > "I have identified seven phases of development with AI." — [youtube/2026-03-03_Ah9p7v7nJWg_the-7-phases-of-ai-driven.md](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=0s) · 2026-03
  > "that's why I prefer a Kanban board set up like this to a sequential plan." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=3072s) · AI Engineer
- By June the cohort warned against over-planning on a static board.
  > "How to avoid planning everything in a static Kanban board" — [blog/workshops__hitl-patterns~x8o98.md](https://www.aihero.dev/workshops/hitl-patterns~x8o98) · n.d.
- PRD became "spec", and interviewing moved out of the spec step.
  > "**`to-prd` is renamed to `to-spec`** — "spec" is now the single through-line term" — [github/skills/CHANGELOG.md](https://github.com/mattpocock/skills/blob/HEAD/CHANGELOG.md)
- He moved from "mostly not parallelizing" (2026-03) to parallel implementers (2026-10), with caveats.
  > "I'm also mostly not parallelizing - the stuff I'm building doesn't need multiple agents running in parallel." — [blog/ways-ai-coding-has-rewired-my-brain.md](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain) · 2026-03
  > "Worktrees don't remove collisions; they postpone them to merge time." — [blog/skills-implement-spec.md](https://www.aihero.dev/skills-implement-spec) · 2026-10

## Related

- [Alignment before code](../principles/alignment-before-code.md)
- [Grilling](grilling.md)
- [AFK loops](afk-loops.md)
- [Review and retro](review-and-retro.md)
- [Context hygiene](context-hygiene.md)
- [Context is a scarce budget](../principles/context-is-a-scarce-budget.md)
