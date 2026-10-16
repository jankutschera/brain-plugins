---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2025-10
last_seen: 2026-10
---
# Own the process

Developers should own their process and stack: small, local, hackable tools beat frameworks that take control, and the durable thing is the technique, not the vendor.
  > "Turns out that giving away control of context to a framework makes things a lot harder to debug My advice: own the process" — [x/2026-04.md](https://x.com/mattpocockuk/status/2044029094942159126) · 2026-04

## Evidence

- His skills repo is pitched against process-owning frameworks.
  > "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- He believes in inversion of control while no tool has won.
  > "I believe in inversion of control and you should be in control of the stack." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=1464s) · AI Engineer
- He prefers user-invoked "procedures" so he stays in control.
  > "I tend to prefer my skills as procedures. I like to be the one in control." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1153s) · David Ondrej
  > "Superpowers gives the agent superpowers My skills give you superpowers" — [x/2026-07.md](https://x.com/mattpocockuk/status/2077789613691699629) · 2026-07
- The technique is the durable part, not the tool.
  > "the workflow is the durable part, not the tool." — [blog/workshops__ai-coding-crash-course.md](https://www.aihero.dev/workshops/ai-coding-crash-course) · n.d.
- Local and lock-in free, from evals to sandboxes.
  > "Evalite is different. It's **local-only**. It runs on your machine, and you stay in complete control of your data." — [github/evalite/apps/evalite-docs/src/content/docs/what-is-evalite.mdx](https://github.com/mattpocock/evalite/blob/HEAD/apps/evalite-docs/src/content/docs/what-is-evalite.mdx)
- He wants users to adapt his skills, not depend on them.
  > "IMO you should be specializing my skills to your work" — [x/2026-10.md](https://x.com/mattpocockuk/status/2107376343537385946) · 2026-10

## How it shows up

- His skills are small, model-agnostic and meant to be forked.
  > "These skills are designed to be small, easy to adapt, and composable. They work with any model." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
  > "Hack around with them. Make them your own. Enjoy." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- Skills stay opinionated with no per-user config (skill doc, supporting evidence).
  > "The answer is that skills stay opinionated and take no per-user config." — [blog/skills-setup-matt-pocock-skills.md](https://www.aihero.dev/skills-setup-matt-pocock-skills) · 2026-07
- He built Sandcastle because the alternatives sold a service.
  > "all the tools that I found were trying to sell me some third party service. So, I realized I needed to build something here." — [youtube/2026-04-30_E5-QK3CDVQM_i-open-sourced-my-own-afk.md](https://www.youtube.com/watch?v=E5-QK3CDVQM&t=75s) · 2026-04
- He keeps his course and workflow harness-agnostic: "Claude Code For Real Engineers" became "AI Coding For Real Engineers".
  > "How it started: Claude Code For Real Engineers How it's going: AI Coding For Real Engineers" — [x/2026-05.md](https://x.com/mattpocockuk/status/2055177489538756984) · 2026-05
- He warns about "skill hell".
  > "And now we have skill hell." — [youtube/2026-07-17_32LyZyFQhCQ_framework-hell-tutorial-hell-now-skill.md](https://www.youtube.com/shorts/32LyZyFQhCQ?t=7s) · 2026-07

## Tensions and evolution

- Model-agnostic in principle, Claude-first in shipping: the skills plugin targeted Claude Code first.
  > "We ship a native **Claude Code plugin** and, for now, **defer** a native **Codex plugin**." — [github/skills/.agents/adr/0002-ship-as-a-claude-code-plugin.md](https://github.com/mattpocock/skills/blob/HEAD/.agents/adr/0002-ship-as-a-claude-code-plugin.md)
- Loyalty to Claude Code (2025-10) gave way to Codex for AFK work when pricing changed (2026-05).
  > "Claude Code is so freaking good now" — [x/2025-10.md](https://x.com/mattpocockuk/status/1979865873403007003) · 2025-10
  > "But it's time to try Codex." — [x/2026-05.md](https://x.com/mattpocockuk/status/2054637261388447956) · 2026-05
  > "You notice I'm using Claude, but I don't like Claude very much." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=1697s) · AI Engineer

## Related

- [Humans own the strategy](humans-own-the-strategy.md)
- [Build your own tools](../methods/build-your-own-tools.md)
- [Writing for agents](../methods/writing-for-agents.md)
- [Less is more](less-is-more.md)
