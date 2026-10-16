---
type: method
sources: [github, youtube, youtube-appearances, x]
quotes: 23
first_seen: 2026-03
last_seen: 2026-10
---
# Review and retro

Implementation makes it work and review makes it good: coding standards live in a separate reviewer, humans review in proportion to risk, and every repeated mistake is turned into a check through a retro.
  > "implement, you make it work, and then code review, you actually make it good." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=821s) · AI Engineer

## Evidence

- Human review reviews the system, not just the code.
  > "when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1215s) · AI Engineer
- You never want to write the same comment twice.
  > "you never want to write the same comment twice." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1221s) · AI Engineer
- Automated review is one of his biggest quality levers.
  > "Automated code review is one of the most impactful ways that you can improve the code quality coming out of your agent." — [youtube/2026-05-28_mh5XZ-L5SFQ_can-cursor-s-hardcore-review-skill.md](https://www.youtube.com/watch?v=mh5XZ-L5SFQ&t=0s) · 2026-05
- Reading code is a scale, not a yes/no.
  > "The "should you read code" debate is dumb because the real decision isn't binary, it's a scale:" — [x/2026-07.md](https://x.com/mattpocockuk/status/2073711736838918436) · 2026-07
- Both automated and human review are needed.
  > "Two things can be true at the same time: You aren't doing enough automated review You should still do human review" — [x/2026-08.md](https://x.com/mattpocockuk/status/2093433213347581965) · 2026-08
- Agents are bad at improving code they just wrote, so review runs in a fresh context.
  > "agents are often really bad at editing code or improving code they've just written." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=953s) · 2026-07
  > "the reviewer will be dumber than the thing that actually implemented it." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=3965s) · AI Engineer

## How it shows up

1. Keep coding standards out of the implementer; push them to the reviewer.
  > "my first piece of advice is don't put coding standards in your implementer agent." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=696s) · AI Engineer
  > "Then pass it to a reviewer agent that runs on every PR. Save tokens during implementation, spend them during review." — [x/2026-04.md](https://x.com/mattpocockuk/status/2043320548776681627) · 2026-04
2. Build your own reviewer, and let it commit fixes.
  > "The reviewer should commit. It should make fixes." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=946s) · AI Engineer
3. Split review into Standards and Spec axes as parallel sub-agents.
  > "Both axes run as **parallel sub-agents** so they don't pollute each other's context, then this skill aggregates their findings." — [github/skills/skills/engineering/code-review/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/code-review/SKILL.md)
4. Scale human review to the door: one-way doors always, two-way doors rarely; shift checkpoints left for big work.
  > "You really don't need to review every single two-way door. Every single one-way door you do." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1329s) · AI Engineer
  > "You shift checkpoints left for big work, for stuff you need to align on first, and you can shift it to the right for small work." — [youtube/2026-07-20_Yn8h5Ip-L9c_do-you-even-need-human-review.md](https://www.youtube.com/shorts/Yn8h5Ip-L9c?t=92s) · 2026-07
5. The PR carries evidence, not claims.
  > "This evidence is an essential part of learning to trust your agent" — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=353s) · 2026-10
6. Human QA imposes taste.
  > "You need a human touch when you're building this stuff because without that, you just end up with slop." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4406s) · AI Engineer
7. Retro: note mistakes into CODING_STANDARDS, then prefer a lint rule, hook or CI check.
  > "Every meaningful thing your agent gets wrong should be noted into CODING_STANDARDS." — [x/2026-09.md](https://x.com/mattpocockuk/status/2103748049906397613) · 2026-09
  > "It'll propose custom lint rules, pre-commit hooks, or CI workflows." — [x/2026-09.md](https://x.com/mattpocockuk/status/2099859946053533933) · 2026-09

## Tensions and evolution

- In March 2026 his QA included reading code; two weeks later he barely looked at it.
  > "And QA here also involves a human actually going and reading the code that's been produced during the execution loop." — [youtube/2026-03-03_Ah9p7v7nJWg_the-7-phases-of-ai-driven.md](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=346s) · 2026-03
  > "You can also notice how little I looked at the code really." — [youtube/2026-03-18_hX7yG1KVYhI_building-a-real-feature-with-claude.md](https://www.youtube.com/watch?v=hX7yG1KVYhI&t=2579s) · 2026-03
- He admits he has no answer to the growing review load.
  > "I don't honestly know what the answer to this yet. I think we just need to be ready to be doing more code review, essentially." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=3602s) · AI Engineer
- He distrusted self-improvement loops in June 2026 and made `/retro` part of the main flow in October.
  > "I have been extremely reluctant to add this since I think models are REALLY bad at improving their own behavior" — [x/2026-08.md](https://x.com/mattpocockuk/status/2088741042744901842) · 2026-08
  > "Even running it on a 'successful' agent session can turn up inefficiencies and workarounds the agent is battling against." — [x/2026-10.md](https://x.com/mattpocockuk/status/2107037429324513535) · 2026-10

## Related

- [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md)
- [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md)
- [Never trust an LLM](../principles/never-trust-an-llm.md)
- [The main flow](the-main-flow.md)
- [AFK loops](afk-loops.md)
