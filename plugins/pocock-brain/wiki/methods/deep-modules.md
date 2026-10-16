---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2026-02
last_seen: 2026-10
---
# Deep modules

He restructures codebases into a few deep modules with small interfaces: the human designs the interface, the agent owns the implementation behind it, and tests at the boundary keep it honest.
  > "Design the interface, delegate the implementation." — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=986s) · AI Engineer

## Evidence

- His definition, after Ousterhout.
  > "Design **deep modules**: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)
- He calls them grey boxes: you can look inside but don't need to.
  > "I call them "grey-box modules" because you can look inside if you want to, but you're not really supposed to." — [blog/ways-ai-coding-has-rewired-my-brain.md](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain) · 2026-03
- After months of AI-only code he called them "KING".
  > "Deep, grey-box modules with simple interfaces are the KING - let AI control what's in the box to decrease your cognitive load" — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02
- AI tends to produce shallow-module codebases.
  > "which AI is really good at creating codebases like this" — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=812s) · AI Engineer
- The split keeps his sense of the codebase and his sanity.
  > "I found that has been a really nice way to retain my sense of the code base while preserving my sanity." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4861s) · AI Engineer
- He watches interfaces more than implementations.
  > "Notice how I'm thinking about the interface more than I'm actually thinking about the implementation here." — [youtube/2026-03-18_hX7yG1KVYhI_building-a-real-feature-with-claude.md](https://www.youtube.com/watch?v=hX7yG1KVYhI&t=1626s) · 2026-03

## How it shows up

1. Apply the deletion test: if deleting the module makes complexity vanish, it was a pass-through.
  > "Imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)
2. Only add a seam when two adapters actually vary across it.
  > "**One adapter means a hypothetical seam. Two adapters means a real one.** Don't introduce a seam unless something actually varies across it." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)
3. Measure depth as leverage at the interface, not Ousterhout's line ratio (skill doc, supporting evidence).
  > "Depth is a property of the interface, not the implementation." — [blog/skills-codebase-design.md](https://www.aihero.dev/skills-codebase-design) · 2026-07
4. Make the file system match the mental map of the code.
  > "you need to make sure that the file system and the design of your code base matches this internal map that you have of it." — [youtube/2026-02-26_uC44zFz7JSM_your-codebase-is-not-ready-for.md](https://www.youtube.com/watch?v=uC44zFz7JSM&t=157s) · 2026-02
5. Use parallel sub-agents to "design it twice" with radically different interfaces.
  > "Spawn 3+ sub-agents in parallel. Each must produce a **radically different** interface for the deepened module." — [github/skills/skills/engineering/codebase-design/DESIGN-IT-TWICE.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/DESIGN-IT-TWICE.md)
6. Refactor only where code is active, and run a daily architecture-improvement loop.
  > "A deepening in code that nobody touches is a refactor that never pays back." — [blog/skills-improve-codebase-architecture.md](https://www.aihero.dev/skills-improve-codebase-architecture) · 2026-05
  > "I have loops that essentially every morning it will run my improve codebase architecture skill and give me a proposal" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4100s) · The Pragmatic Engineer
- For TypeScript backends he recommends Effect for this style.
  > "If you're building backend in TypeScript, I really cannot recommend `Effect` enough." — [blog/ways-ai-coding-has-rewired-my-brain.md](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain) · 2026-03

## Tensions and evolution

- He builds on Ousterhout but rejects his line-ratio metric.
  > "**Depth as ratio of implementation-lines to interface-lines** (Ousterhout): rewards padding the implementation. We use depth-as-leverage instead." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)
- Taste still applies at the boundaries, which is what separates this from vibe coding.
  > "this of course is still a million miles away from vibe coding because you need to apply taste at the boundaries of these modules." — [youtube/2026-02-26_uC44zFz7JSM_your-codebase-is-not-ready-for.md](https://www.youtube.com/watch?v=uC44zFz7JSM&t=349s) · 2026-02
- In October 2026 he argued for more abstractions as agent guardrails, after "sometimes no abstraction" in 2024.
  > "You can use them (combined with harsh lint rules) to reduce the design space available to the agent and constrain them only to good decisions." — [x/2026-10.md](https://x.com/mattpocockuk/status/2106425743479546343) · 2026-10

## Related

- [The codebase is the agent's environment](../principles/the-codebase-is-the-agents-environment.md)
- [Humans own the strategy](../principles/humans-own-the-strategy.md)
- [TDD at agreed seams](tdd-at-agreed-seams.md)
- [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md)
