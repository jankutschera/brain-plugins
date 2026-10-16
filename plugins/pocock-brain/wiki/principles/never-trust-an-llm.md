---
type: principle
sources: [blog, github, youtube, x]
quotes: 17
first_seen: 2023-03
last_seen: 2026-10
---
# Never trust an LLM

Model output is a hypothesis until a primary source or shown evidence confirms it; he is pro-LLM but paranoid about hallucination, summaries and the agent's own account of its work.
  > "Every time an LLM says anything to me, I automatically assume it's BS unless it's read a source confirming it" — [x/2026-03.md](https://x.com/mattpocockuk/status/2037110265796264189) · 2026-03

## Evidence

- He says it plainly on video.
  > "I am now paranoid about everything an LLM says to me and I will never ever trust an LLM." — [youtube/2026-03-27_9VNG0h4pLh0_never-trust-an-llm.md](https://www.youtube.com/watch?v=9VNG0h4pLh0&t=8s) · 2026-03
- Models are more reliable when given the information than when recalling it.
  > "My experience with LLMs is that they're much, much more reliable when you send them the information first." — [youtube/2026-03-27_9VNG0h4pLh0_never-trust-an-llm.md](https://www.youtube.com/watch?v=9VNG0h4pLh0&t=312s) · 2026-03
- His teach skill tells the agent to distrust its own knowledge.
  > "Never trust your parametric knowledge." — [github/skills/skills/productivity/teach/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/teach/SKILL.md)
- Sub-agent output is a hypothesis, not evidence.
  > "Sub-agent output is a hypothesis, not evidence." — [blog/skills-code-review.md](https://www.aihero.dev/skills-code-review) · 2026-07
- Narration about the work is not the work; review means reading the diff.
  > "Reading the diff or the changed files counts; reading the agent's _description_ of what it did does not — narration is not the artifact." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)
- Stronger models fail the same way (reply).
  > "It's prone to exactly the same failure modes as lesser models Use with caution" — [x/2026-07.md](https://x.com/mattpocockuk/status/2073866163063275984) · 2026-07
- Yet he stays pro-LLM.
  > "Now, don't get me wrong. I'm really pro LLM." — [youtube/2026-03-27_9VNG0h4pLh0_never-trust-an-llm.md](https://www.youtube.com/watch?v=9VNG0h4pLh0&t=39s) · 2026-03

## How it shows up

- He forces retrieval in prompts.
  > "Use your search tool." — [youtube/2026-03-27_9VNG0h4pLh0_never-trust-an-llm.md](https://www.youtube.com/watch?v=9VNG0h4pLh0&t=664s) · 2026-03
- His `/pr` skill asks for evidence, because "tests are green" is only a claim.
  > "This evidence is an essential part of learning to trust your agent" — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=353s) · 2026-10
  > ""Tests are green" on its own is a claim, not a before and after." — [blog/skills-pr.md](https://www.aihero.dev/skills-pr) · 2026-10
- He tells the agent to push back on him, to counter sycophancy.
  > "LLMs are sort of naturally sycophantic and so telling it to stand up to me is a nice way" — [youtube/2026-03-23_llwTBpPqo9A_claude-code-tried-to-improve-init.md](https://www.youtube.com/watch?v=llwTBpPqo9A&t=305s) · 2026-03
- His teach skill sends learners to primary sources rather than keeping them on the agent.
  > "The goal isn't to keep you shackled to the agent, it's to get you confident enough to read the sources for yourself" — [x/2026-06.md](https://x.com/mattpocockuk/status/2064697254779228450) · 2026-06
- He applies the rule to his own skills.
  > "`teach` is not reliable enough to trust unchecked, and no skill built on an LLM is." — [blog/skills-teach.md](https://www.aihero.dev/skills-teach) · 2026-07

## Tensions and evolution

- In 2023 he played ChatGPT down; by 2026 he was all-in on AI coding, but kept the distrust.
  > "chat gbt and things like it I think are less useful in general than we think" — [youtube/2023-03-07_WuHSnvsO6Mg_total-typescript-tour-and-ama.md](https://www.youtube.com/watch?v=WuHSnvsO6Mg&t=883s) · 2023-03
  > "I was an AI coding skeptic until I tried plan mode. Without it? Slop. With it? Me-quality code." — [x/2026-01.md](https://x.com/mattpocockuk/status/2011841207891038468) · 2026-01
- His interest in verification is growing (2026-10).
  > "verification is something I'm beginning to be really obsessed with" — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=380s) · 2026-10

## Related

- [Feedback is the speed limit](feedback-is-the-speed-limit.md)
- [Review and retro](../methods/review-and-retro.md)
- [Learning at the edge](learning-at-the-edge.md)
- [Humans own the strategy](humans-own-the-strategy.md)
