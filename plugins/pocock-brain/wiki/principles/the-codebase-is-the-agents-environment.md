---
type: principle
sources: [blog, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2025-04
last_seen: 2026-09
---
# The codebase is the agent's environment

The codebase and harness an agent works in shape its output more than the prompt or the model, so the fix for bad output is usually in the repo.
  > "Your code base, way more than the prompts that you use, way more than your agents.md file, is the biggest influence on AI's output." — [youtube/2026-02-26_uC44zFz7JSM_your-codebase-is-not-ready-for.md](https://www.youtube.com/watch?v=uC44zFz7JSM&t=7s) · 2026-02

## Evidence

- Bad codebases, not big ones, are what make agents fail.
  > "Some folks say AI is bad in big codebases. I don't think that's right - I think it's bad in bad codebases." — [x/2026-02.md](https://x.com/mattpocockuk/status/2019042507871429104) · 2026-02
- Garbage in, garbage out.
  > "bad code bases make bad agents. If you have a garbage code base, you're going to get garbage out of the agent that's working in that code base." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=2212s) · AI Engineer
- Agents copy what they see.
  > "it will be happy to play in the mud if what you have is mud." — [youtube/2026-02-23_hYZdIwFIy-c_red-green-refactor-is-op-with.md](https://www.youtube.com/watch?v=hYZdIwFIy-c&t=297s) · 2026-02
- He names the idea AX, agent experience, and says the fix is usually in the repo.
  > "The instinct is to blame the model or rewrite the prompt; the fix is more often in the repo." — [blog/ai-coding-dictionary__ax.md](https://www.aihero.dev/ai-coding-dictionary/ax) · n.d.
  > "I think of there as being a difference between DX developer experience and AX, right? Agent experience." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=3491s) · David Ondrej
- Harness and model matter about equally, and you control the harness.
  > "the harness has an equal amount of work and you have much more control of the harness than you do the model." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=18s) · David Ondrej
- He tells people to stop chasing model releases (his most-liked reply).
  > "Stop caring so much about model releases. Focus on the harness, and improving the environment your agent operates in." — [x/2026-09.md](https://x.com/mattpocockuk/status/2102757952180686945) · 2026-09
- An easy-to-change codebase even lets you use a cheaper model.
  > "Have a code base that's easier to make changes in? Because then you can employ a stupider model." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1950s) · David Ondrej

## How it shows up

- He treats agents as memoryless new starters and designs the repo for them ("Memento-driven development").
  > "AI is not a super-powered developer. It's a new starter with no memory." — [blog/how-to-make-codebases-ai-agents-love.md](https://www.aihero.dev/how-to-make-codebases-ai-agents-love) · 2026-02
  > "is momentodriven development right we are trying to optimize our code bases for new starters" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=3617s) · The Pragmatic Engineer
- He casts humans as the agents' platform team, gardening the environment.
  > "We are essentially just Ralph's platform team, right?" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=5508s) · The Pragmatic Engineer
- He runs a daily loop that proposes architecture improvements.
  > "I have loops that essentially every morning it will run my improve codebase architecture skill and give me a proposal" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4100s) · The Pragmatic Engineer
- On a major model launch he had "no take", because his harness was model-agnostic.
  > "If you've designed your harness/environment well, and not over-optimised around a specific model, today should feel like any other day" — [x/2026-07.md](https://x.com/mattpocockuk/status/2080748648120439249) · 2026-07
- He waits about a month before trying a new model.
  > "I prefer to essentially not try a new model when it comes out and wait about a month just to see how things shake out." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=797s) · David Ondrej

## Tensions and evolution

- In 2025 he already separated himself from vibe coding on this point.
  > "We actually do care about the code because the code is the input to our LLM." — [youtube/2025-04-08_FRogt98OF80_build-an-mcp-server-in-5.md](https://www.youtube.com/watch?v=FRogt98OF80&t=414s) · 2025-04
- He admits the harness-first bet might be the wrong side of the bitter lesson.
  > "maybe I'm falling into the bitter lesson that instead of like like optimizing my setup, optimizing my harness, I should just wait for the models to get better" — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1776s) · David Ondrej
- In 2025 he found AI better on big mature codebases than toy projects, which he later explained by quality rather than size.
  > "Hot take, but I've found that AI is _better_ on large, mature codebases than toy projects." — [x/2025-05.md](https://x.com/mattpocockuk/status/1922624052016882073) · 2025-05

## Related

- [Fundamentals matter more with AI](fundamentals-matter-more-with-ai.md)
- [Code is cheap; maintenance is not](code-is-cheap-maintenance-is-not.md)
- [Deterministic over probabilistic](deterministic-over-probabilistic.md)
- [Deep modules](../methods/deep-modules.md)
- [Review and retro](../methods/review-and-retro.md)
