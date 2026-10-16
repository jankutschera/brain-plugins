---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 19
first_seen: 2022-11
last_seen: 2026-06
---
# Feedback is the speed limit

How fast and how reliably you get feedback limits how fast you can safely go, for agents, for learners and for content; so work in small steps and build the loop first.
  > "The rate at which you can get feedback is your speed limit. Never outrun your headlights." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01

## Evidence

- The quality of feedback loops is the ceiling on agent output.
  > "the quality of your feedback loops influences how good your AI can code, essentially. That is the ceiling." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4218s) · AI Engineer
- Without feedback the agent flies blind.
  > "Without feedback on how the code it produces actually runs, the agent will be flying blind." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- Agents should check their own work, or you become QA.
  > "If you don't do this, you're hamstringing the agent and forcing yourself into the role of QA." — [x/2025-03.md](https://x.com/mattpocockuk/status/1902755644966670425) · 2025-03
- In debugging, building the loop is the skill.
  > "Build the right feedback loop, and the bug is 90% fixed." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- TypeScript is cheap, fast feedback, which has been his pitch since 2022.
  > "time to error is really really critical When You're Building Things fast" — [youtube/2022-11-03_dg1eJZk7waw_why-you-should-migrate-to-typescript.md](https://www.youtube.com/watch?v=dg1eJZk7waw&t=99s) · 2022-11
  > "Does TypeScript make you slower? No, it introduces a feedback loop, which is much shorter." — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=744s) · Tejas Kumar
- The same rule drives his teaching and his content.
  > "One thing I find really important whenever you're teaching anything is to develop a feedback loop" — [youtube/2026-06-08_s5T5oQJcJ6U_learn-anything-with-the-teach-skill.md](https://www.youtube.com/watch?v=s5T5oQJcJ6U&t=234s) · 2026-06
  > "feedback's the whole game really" — [youtube-appearances/unknown_hQDSr7uwu6E_the-future-of-developer-content-matt.md](https://www.youtube.com/watch?v=hQDSr7uwu6E&t=1095s) · Sanity

## How it shows up

- He wants types, tests, CI and a browser for every agent.
  > "And most of all, you want types, types, types, types, types." — [youtube/2026-01-05__IK18goX4X8_ship-working-code-while-you-sleep.md](https://www.youtube.com/watch?v=_IK18goX4X8&t=909s) · 2026-01
  > "That's because it's flying blind. It can't test the code in the environment where it's running - the browser." — [x/2026-01.md](https://x.com/mattpocockuk/status/2010728707997278296) · 2026-01
- He slices work into thin vertical tracer bullets so feedback arrives early.
  > "The AI is building too much in the dark, without feedback loops to validate assumptions early." — [blog/tracer-bullets.md](https://www.aihero.dev/tracer-bullets) · 2026-01
- His Ralph loops must keep CI green on every commit.
  > "Whenever your Ralph loop commits, CI has to stay green." — [youtube/2026-01-05__IK18goX4X8_ship-working-code-while-you-sleep.md](https://www.youtube.com/watch?v=_IK18goX4X8&t=634s) · 2026-01
- He trusts agent output because he trusts his CI.
  > "Because I'm confident in my CI, I can look at the code the agent has produced" — [youtube/2025-07-03_xnUYnd-Pgeg_most-companies-are-not-ready-for.md](https://www.youtube.com/shorts/xnUYnd-Pgeg?t=54s) · 2025-07
- He ships content quickly and lets the response decide.
  > "I don't really try not to worry too much about shipping something that's bad because I just rely on the feedback that I'm getting" — [youtube-appearances/unknown_hQDSr7uwu6E_the-future-of-developer-content-matt.md](https://www.youtube.com/watch?v=hQDSr7uwu6E&t=472s) · Sanity

## Tensions and evolution

- TDD went from "absolutely essential" in his workshop to a "mixed relationship" on The Pragmatic Engineer, where he asks for proof instead.
  > "TDD I found is absolutely essential for getting the most out of agents." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4008s) · AI Engineer
  > "So yeah, I I have a mixed relationship with TDD." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4838s) · The Pragmatic Engineer
  > "provide proof that your change does the thing it's purported to do. Give me TDD evidence" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4802s) · The Pragmatic Engineer
- Green checks are necessary but not sufficient.
  > "Does a green CI mean that the code is ready for merge? No, it does not." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=293s) · AI Engineer

## Related

- [Deterministic over probabilistic](deterministic-over-probabilistic.md)
- [TDD at agreed seams](../methods/tdd-at-agreed-seams.md)
- [Diagnosing bugs](../methods/diagnosing-bugs.md)
- [Content strategy](../methods/content-strategy.md)
- [Learning at the edge](learning-at-the-edge.md)
