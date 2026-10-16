---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2021-05
last_seen: 2026-10
---
# Code is cheap; maintenance is not

Agents made writing code cheap, so the cost moved to reading, reviewing and living with it, and bad code is now more expensive than ever.
  > "Writing code got cheap. Reading it did not." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10

## Evidence

- He states the inversion bluntly on stage.
  > "I think code is not cheap. In fact, bad code is the most expensive it's ever been." — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=237s) · AI Engineer
- He compresses it into a two-line post.
  > "Writing code is cheap Maintaining code is not cheap" — [x/2026-05.md](https://x.com/mattpocockuk/status/2050167042771194226) · 2026-05
- He says AI accelerates software entropy rather than escaping it.
  > "AI helps you move faster, but it just accelerates software entropy." — [x/2026-05.md](https://x.com/mattpocockuk/status/2050102353248874884) · 2026-05
  > "Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
- He defines tech debt as anything that makes change harder, and treats it as a permanent fight.
  > "tech debt is anything that makes the code base harder to make modifications to over time." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4895s) · The Pragmatic Engineer
- He describes a vicious circle between codebase quality and agent output.
  > "And the worse the codebase, the worse the AI performs. It's a vicious circle." — [blog/index.md](https://www.aihero.dev/) · n.d.
- Review, not writing, is now the bottleneck.
  > "Agents raise the volume of code produced, so review becomes the bottleneck." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)

## How it shows up

- He treats every line, and every test, as a liability.
  > "Every line of code you add carries a maintenance burden." — [blog/my-claude-code-cohort-a-teaser.md](https://www.aihero.dev/my-claude-code-cohort-a-teaser) · 2026-03
  > "Bad tests aren't just a review problem, they're a debt problem." — [blog/skill-test-driven-development-claude-code.md](https://www.aihero.dev/skill-test-driven-development-claude-code) · 2026-02
- He calls "code is cheap" a mind virus when it excuses negligent use.
  > "But the "code is cheap" mind virus is making it worse IMO." — [x/2026-05.md](https://x.com/mattpocockuk/status/2050860119928262883) · 2026-05
- He keeps reading code, because ignoring it produced a mess.
  > "every time I tried to ignore the code, I would just end up with a this terrible mess." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=203s) · Latent Space
- He builds review tooling (the `/pr` skill) to make reading cheaper, since that is now the expensive step.
  > "my goal with this PR skill, kind of inspired by Show Me, is to make human review as easy as possible." — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=330s) · 2026-10

## Tensions and evolution

- The idea is old for him: in 2021 he renamed state management "entropy management".
  > "We should call it entropy management" — [x/2021-06.md](https://x.com/mattpocockuk/status/1402696390778798082) · 2021-06
  > "But most dev work is not building, it's maintaining." — [x/2021-05.md](https://x.com/mattpocockuk/status/1390250003021578240) · 2021-05
- In 2025 he used cheap code as a reason to throw work away; by mid-2026 he half-rejected the phrase.
  > "Code is so cheap to produce now that you can just step back in time anytime you want to." — [youtube/2025-05-31_Hw9ytLUln5A_vibe-coders-won-t-be-able.md](https://www.youtube.com/shorts/Hw9ytLUln5A?t=41s) · 2025-05
  > "saying that code is cheap, and it's partially true and partially I hate that phrase." — [youtube/2026-07-23_n0VhIVtviC0_don-t-waste-time-on-specs.md](https://www.youtube.com/watch?v=n0VhIVtviC0&t=64s) · 2026-07
- He dates the point where agent entropy became manageable to a specific model.
  > "Before Opus 4.5, models produced software entropy at an alarming rate. Opus 4.5 was the first time I felt like the entropy was manageable." — [x/2026-02.md](https://x.com/mattpocockuk/status/2022005584828997932) · 2026-02

## Related

- [Fundamentals matter more with AI](fundamentals-matter-more-with-ai.md)
- [The codebase is the agent's environment](the-codebase-is-the-agents-environment.md)
- [Review and retro](../methods/review-and-retro.md)
- [Deep modules](../methods/deep-modules.md)
