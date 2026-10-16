---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 19
first_seen: 2026-01
last_seen: 2026-10
---
# AFK loops

He runs coding agents unattended over a queue of tickets, each iteration in a fresh context, sandboxed, with an implementer and a reviewer, but only after watching the loop work with a human in it.
  > "Run a coding agent with a clean slate, again and again until a stop condition is met." — [x/2026-01.md](https://x.com/mattpocockuk/status/2007924876548637089) · 2026-01

## Evidence

- The Ralph approach made his AI-coding following take off.
  > "There's an AI coding approach that lets you run seriously long-running AI agents (hours, days) that ship code while you sleep." — [x/2026-01.md](https://x.com/mattpocockuk/status/2007924876548637089) · 2026-01
- AFK was when AI coding clicked for him.
  > "the moment that I discovered AFK was the moment I really got into AI coding and the moment I was really able to massively increase my output" — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=2639s) · David Ondrej
- Fresh context per iteration is why it works.
  > "Each iteration of Ralph uses a fresh context window" — [blog/why-the-anthropic-ralph-plugin-sucks.md](https://www.aihero.dev/why-the-anthropic-ralph-plugin-sucks) · 2026-01
- It is queue management, not looping.
  > "The way I mostly think about these things as cues, okay, cues, not loops." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=2719s) · David Ondrej
- Sandboxing is required.
  > "in order to get agents to run properly AFK, you need them to be sandboxed." — [youtube/2026-04-30_E5-QK3CDVQM_i-open-sourced-my-own-afk.md](https://www.youtube.com/watch?v=E5-QK3CDVQM&t=45s) · 2026-04
- Architecture stays HITL; rote work goes AFK (reply).
  > "In other words, if architecture is required, use HITL. If it's rote, do AFK Ralph." — [x/2026-01.md](https://x.com/mattpocockuk/status/2006695757982659049) · 2026-01

## How it shows up

1. Work HITL first until you trust the loop; he took three days.
  > "It took me a solid three days of working with HITL Ralph before I felt comfortable letting it run AFK." — [blog/events__turn-ai-agents-into-autonomous-software-engineers-with-ralph.md](https://www.aihero.dev/events/turn-ai-agents-into-autonomous-software-engineers-with-ralph) · 2026-02
2. One issue per iteration, picked by priority, tracer bullets early.
  > "Work on **one issue per iteration**. Do not attempt multiple issues in a single iteration." — [github/sandcastle/src/templates/simple-loop/prompt.md](https://github.com/mattpocock/sandcastle/blob/HEAD/src/templates/simple-loop/prompt.md)
3. Keep CI green on every commit and cap iterations.
  > "Whenever your Ralph loop commits, CI has to stay green." — [youtube/2026-01-05__IK18goX4X8_ship-working-code-while-you-sleep.md](https://www.youtube.com/watch?v=_IK18goX4X8&t=634s) · 2026-01
  > "Infinite loops are dangerous with stochastic systems." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
4. Pair an implementer with a reviewer.
  > "This pattern has been incredibly powerful because the implementer can make mistakes, but the reviewer generally picks it up." — [youtube/2026-04-30_E5-QK3CDVQM_i-open-sourced-my-own-afk.md](https://www.youtube.com/watch?v=E5-QK3CDVQM&t=477s) · 2026-04
5. End in something reviewable, never merged code.
  > "After: the run ends in something reviewable — a PR, not changes already merged." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)
6. Run it in Sandcastle or a GitHub Actions loop overnight.
  > "I've had specs that have like 30 tickets, and I have a setup in GitHub actions where it just basically churns through." — [youtube-appearances/unknown_LMpMmOWTtVk_matt-pocock-built-the-skills-repo.md](https://www.youtube.com/watch?v=LMpMmOWTtVk&t=1135s) · The Next New Thing

## Tensions and evolution

- January 2026: the agent picks the task and Ralph does everything; October: a deterministic script walks tickets.
  > "Honestly, there's nothing I want to do without Ralph anymore" — [blog/events__turn-ai-agents-into-autonomous-software-engineers-with-ralph.md](https://www.aihero.dev/events/turn-ai-agents-into-autonomous-software-engineers-with-ralph) · 2026-02
  > "This is what I recommend for most people. It runs the same way every time, it is reliable, and it is cheap." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10
- In January most of his own use was HITL despite the AFK pitch.
  > "I've run AFK Ralph a few times, but most of my usage is HITL." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
- Pricing moved his AFK work off Claude Code in May 2026.
  > "I need to move off Claude Code for my AFK use cases if I want to get the best bang for my buck." — [youtube/2026-05-13_lNOQaakmyDU_anthropic-s-dedicated-monthly-credit-is.md](https://www.youtube.com/watch?v=lNOQaakmyDU&t=589s) · 2026-05
- A fully automated factory without brakes becomes a "slop cannon".
  > "If you just have permanent acceleration pushing stuff through your factory, you're going to end up with a slop cannon, right?" — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=141s) · AI Engineer

## Related

- [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md)
- [The main flow](the-main-flow.md)
- [Context is a scarce budget](../principles/context-is-a-scarce-budget.md)
- [Review and retro](review-and-retro.md)
- [Build your own tools](build-your-own-tools.md)
