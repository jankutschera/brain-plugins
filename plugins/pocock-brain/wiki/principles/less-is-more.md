---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 25
first_seen: 2024-09
last_seen: 2026-10
---
# Less is more

Most steering text is a no-op or rots, so he deletes: near-empty instruction files, short skills, few docs, and the simplest loop that works, with every addition made to earn its place.
  > "Long skills are such a red flag to me" — [x/2026-05.md](https://x.com/mattpocockuk/status/2055298876093952489) · 2026-05

## Evidence

- Most lines in agent-written skills change nothing.
  > "They're no-ops. They do nothing to change the agent's behavior." — [x/2026-06.md](https://x.com/mattpocockuk/status/2069784839474032896) · 2026-06
  > "you can probably go through that and delete about half of it and not much about the output will change." — [youtube-appearances/unknown_LMpMmOWTtVk_matt-pocock-built-the-skills-repo.md](https://www.youtube.com/watch?v=LMpMmOWTtVk&t=1378s) · The Next New Thing
- Most AGENTS.md files hurt (reply).
  > "90% of people can delete their AGENTS.md and their output will improve." — [x/2026-07.md](https://x.com/mattpocockuk/status/2073473197991715246) · 2026-07
- Instruction files spend a limited instruction budget.
  > "LLMs really only have a realistic instruction budget of around 300 to 400 instructions." — [youtube/2026-02-24_9tmsq-Gvx6g_never-run-claude-init.md](https://www.youtube.com/watch?v=9tmsq-Gvx6g&t=466s) · 2026-02
- Docs that duplicate code rot and poison context.
  > "if there are two sources of truth and they conflict, then AI won't know which one is the real one." — [youtube/2026-07-16_Fj8DKMbdIzU_delete-most-of-your-docs.md](https://www.youtube.com/shorts/Fj8DKMbdIzU?t=62s) · 2026-07
- In LLM apps, each new technique must earn its place.
  > "Each new AI development needs to earn its place in your system." — [blog/how-to-improve-your-llm-powered-app.md](https://www.aihero.dev/how-to-improve-your-llm-powered-app) · 2025-03
- Simple loops beat elaborate agent architectures.
  > "Ralph works because it's ruthlessly simple. Keep it that way." — [blog/why-the-anthropic-ralph-plugin-sucks.md](https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks) · 2026-01
  > "Models like Fable and Sol don't need huge frameworks - they just need a bit of structure." — [x/2026-08.md](https://x.com/mattpocockuk/status/2089408902228042036) · 2026-08

## How it shows up

- His CLAUDE.md was one six-word line, and he tells people never to run `/init`.
  > "all I've got is a single line which is six words saying you are on WSL on Windows." — [youtube/2026-02-24_9tmsq-Gvx6g_never-run-claude-init.md](https://www.youtube.com/watch?v=9tmsq-Gvx6g&t=545s) · 2026-02
  > "Never run it. If you find one that was auto-generated, delete it." — [blog/never-run-claude-init.md](https://www.aihero.dev/never-run-claude-init) · 2026-02
- His advice for a new setup: delete everything, observe, then add back.
  > "First thing I would do is I would delete every single skill, every single plugin, every single MCP server." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=3649s) · David Ondrej
- He keeps only the docs code cannot express: ADRs and a glossary.
  > "The only exception are things that the code cannot explain itself, like alternatives considered or domain language. I.e. ADR's and glossaries" — [x/2026-07.md](https://x.com/mattpocockuk/status/2076596586612765105) · 2026-07
- Specs and handoffs are deleted once used.
  > "Once the spec is present in the code, then you can just delete the spec." — [youtube/2026-07-30_F3lL98Pj90o_wayfinder-nothing-is-too-big-to.md](https://www.youtube.com/watch?v=F3lL98Pj90o&t=823s) · 2026-07
- He turns agent memory off.
  > "actually I find it just works better if you kill the memory completely." — [youtube/2026-07-17_A0scuiiGBC4_kill-your-memory-md.md](https://www.youtube.com/shorts/A0scuiiGBC4?t=83s) · 2026-07
- His recipe for short skills (reply).
  > "Just remove the no-ops, kill duplication, and take out anything irrelevant to the task." — [x/2026-06.md](https://x.com/mattpocockuk/status/2069785124950945825) · 2026-06

## Tensions and evolution

- His own CLAUDE.md shrank: in October 2025 a rule was permanent; by February 2026 it had moved into a skill.
  > "I've added to rules and I'm never taking it out." — [youtube/2025-10-27_kZ-zzHVUrO4_how-i-use-claude-code-for.md](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=187s) · 2025-10
  > "Instead, I prefer now I think this is actually better placed inside a skill." — [youtube/2026-02-24_9tmsq-Gvx6g_never-run-claude-init.md](https://www.youtube.com/watch?v=9tmsq-Gvx6g&t=574s) · 2026-02
- Docs went from "more" to "delete" within months.
  > "First I thought MOAR DOCS = BETTER but 'doc rot' is real." — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02
  > "1. Delete the docs you create to explain your code" — [x/2026-07.md](https://x.com/mattpocockuk/status/2076596585069174925) · 2026-07
- The repos do not always follow the rule: his retro skill says to use agent files sparingly, while evalite's CLAUDE.md restates build commands, and he keeps "hundreds of lines" of review standards (outside the always-loaded file).
  > "They should be used incredibly sparingly, usually only for **navigation pointers** to other files." — [github/skills/skills/engineering/retro/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/retro/SKILL.md)
  > "This builds `evalite` package first, then `evalite-ui`, copying UI assets to `packages/evalite/dist/ui`." — [github/evalite/CLAUDE.md](https://github.com/mattpocock/evalite/blob/HEAD/CLAUDE.md)
  > "I have hundreds of lines in my CODING_STANDARDS.md files" — [x/2026-08.md](https://x.com/mattpocockuk/status/2088256432265167185) · 2026-08
- His view of abstraction moved from "most readable" (2019) to "sometimes none" (2024) to "MORE, as guardrails for agents" (2026).
  > "Sometimes no abstraction is the right abstraction" — [x/2024-09.md](https://x.com/mattpocockuk/status/1837778942427640031) · 2024-09
  > "My hot take from chatting to @poteto is that we should use MORE abstractions in the AI age" — [x/2026-10.md](https://x.com/mattpocockuk/status/2106425743479546343) · 2026-10

## Related

- [Context is a scarce budget](context-is-a-scarce-budget.md)
- [Deterministic over probabilistic](deterministic-over-probabilistic.md)
- [Writing for agents](../methods/writing-for-agents.md)
- [Context hygiene](../methods/context-hygiene.md)
