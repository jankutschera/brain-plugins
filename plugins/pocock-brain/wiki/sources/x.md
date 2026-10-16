---
type: source
raw: raw/x/
files: 124
words: 1920614
date_range: 2016-03-10 – 2026-10-06
---
# X / Twitter (@mattpocockuk)

## Coverage

- 124 monthly files (`raw/x/YYYY-MM.md`), 35,859 unique posts, about 1.92M words. Each block holds id, created_at, url, type, in_reply_to, metrics (likes, retweets, replies, quotes, views, bookmarks) and the verbatim text. Quote posts also carry the quoted tweet's text, which is not his.
- Types: 5,537 original, 743 quote, 29,574 reply (82%), 5 retweet. Retweets are not his words and are never quoted here.
- Collected 2026-10-06 via TwitterAPI.io advanced search (`from:mattpocockuk include:nativeretweets`), one UTC day per window from 2011-08-01 to 2026-10-06, deduped by id. A coverage check against the timeline endpoint (500 tweets, 2026-09-01..10-06) found nothing missing.
- Gaps (from MANIFEST): the profile reports 37,027 statuses, so 1,168 are missing. Likely causes: older native retweets are not returned by search, and nothing before 2016-03-10 was found although the account dates from 2011. Withheld or deleted posts are also missing.
- Volume by year (original+quote / reply): 2016 147/13 · 2017 138/64 · 2018 47/21 · 2019 10/22 · 2020 294/870 · 2021 536/1814 · 2022 1217/5125 · 2023 1151/5917 · 2024 1122/5298 · 2025 879/5227 · 2026 (to Oct) 739/5203.
- Eras visible in the feed: voice/accent coach (2016–17), React developer (2018–19), XState team lead, then Stately (2020–22), Vercel/Turborepo devrel and Total TypeScript (2022–24), AI Hero and the AI SDK (2025), mattpocock/skills and AI coding cohorts (2026).
- How it was read for this wiki: a script parsed all files. Read in full were the top 600 original/quote posts by likes, every 2016–2019 original, samples from every later year, opinion-marker and audience-question greps, about 20 self-authored threads, and the top 220 replies. About 1,700 distinct posts in all. Raw candidates for synthesis are in `build/candidates/x.md`.

## What this source shows about him

- X is where he thinks out loud. Opinions, reversals and half-built ideas appear here first, often as questions to his audience.
  > "I figure it's super beneficial both for me (to figure out what I think) and for you" — [x/2026-02.md](https://x.com/mattpocockuk/status/2025568007460729274) · 2026-02
- He changes his mind in public and says so plainly.
  > "Thanks to a chat with @robpalmer2, I've changed my mind about the Types as Comments proposal." — [x/2022-11.md](https://x.com/mattpocockuk/status/1593241036267999233) · 2022-11
- He is a teacher first. Even product posts are framed as lessons, and he calls teaching the most rewarding thing he has done.
  > "Of all the things I've tried to get good at, teaching has been the most rewarding" — [x/2026-06.md](https://x.com/mattpocockuk/status/2064417495918727526) · 2026-06
- His TypeScript case rests on tooling, not on types for their own sake.
  > "TypeScript WASN'T invented to add types to JavaScript." — [x/2023-01.md](https://x.com/mattpocockuk/status/1616008761155489793) · 2023-01
- In the AI era his central claim is that old engineering fundamentals decide how well agents work.
  > "If your code sucks, your agent will too." — [x/2026-08.md](https://x.com/mattpocockuk/status/2089336734530109837) · 2026-08
- He keeps the human as strategist and refuses to hand off thinking.
  > "The most important thing when you're working with coding agents: DO NOT DELEGATE YOUR THINKING" — [x/2025-10.md](https://x.com/mattpocockuk/status/1977810532154650870) · 2025-10
- He is a minimalist about agent steering: short skills, few instructions, pruned docs.
  > "Long skills are such a red flag to me" — [x/2026-05.md](https://x.com/mattpocockuk/status/2055298876093952489) · 2026-05
- He treats context as a scarce budget and coined "smart zone"/"dumb zone" language for it.
  > "It's still 100K of smart, and 900K of dumb." — [x/2026-03.md](https://x.com/mattpocockuk/status/2034572011175907474) · 2026-03
- He builds his audience with free material and treats questions and polls as both content and market research.
  > "I get 5-6 questions every day about TypeScript." — [x/2023-01.md](https://x.com/mattpocockuk/status/1618539859504959493) · 2023-01
- He openly criticises vendors and hype when it hurts learners, including Anthropic.
  > "I have never before experienced, from any developer tool, such a frustrating lack of clarity over the basic terms of usage." — [x/2026-04.md](https://x.com/mattpocockuk/status/2040536403289764275) · 2026-04
- He is skeptical of model output by default.
  > "Every time an LLM says anything to me, I automatically assume it's BS unless it's read a source confirming it" — [x/2026-03.md](https://x.com/mattpocockuk/status/2037110265796264189) · 2026-03
- His tone is informal, profane and self-deprecating, which he acknowledges (reply).
  > "In real life I have the vocabulary of a stevedore" — [x/2026-04.md](https://x.com/mattpocockuk/status/2040850532877680785) · 2026-04
- He keeps politics mostly off the feed on purpose (reply).
  > "But genuinely, I know that a lot of folks follow me for a refuge from non-political content." — [x/2024-09.md](https://x.com/mattpocockuk/status/1835345553988706387) · 2024-09

## Notable pieces

- **2016-03: voice coach tips.** Before tech, the feed was public-speaking advice. Its emphasis on bodily tension comes back in his 2026 talk advice.
  > "If you're worried about how you're coming across, warmth beats confidence every time. Establish trust, then show your skills" — [x/2016-03.md](https://x.com/mattpocockuk/status/713399873723305985) · 2016-03
- **2021-06: "entropy management".** The XState-era framing that prefigures his AI-era focus on maintainability.
  > "We should call it entropy management" — [x/2021-06.md](https://x.com/mattpocockuk/status/1402696390778798082) · 2021-06
- **2022-04: The Ultimate TypeScript Thread.** An evergreen thread of tips that launched the "wizard" brand.
  > "Here's everything I've learned from leading TS dev teams and working on XState's core team." — [x/2022-04.md](https://x.com/mattpocockuk/status/1509964736275927042) · 2022-04
- **2022-11: leaving Vercel for Total TypeScript.**
  > "But it's time to go all-in on education. I'm so excited." — [x/2022-11.md](https://x.com/mattpocockuk/status/1592467692912406528) · 2022-11
- **2023-02: the generics thread.** His template thread: a promise, small steps, a recap, a share ask, then "did I succeed?".
  > "What you think of as 'generics' are actually several different patterns:" — [x/2023-02.md](https://x.com/mattpocockuk/status/1625838932771409923) · 2023-02
- **2023-03: Total TypeScript launch story.**
  > "I realised that so many of the problems I'd had with TypeScript as an app developer had been solved by these library developers." — [x/2023-03.md](https://x.com/mattpocockuk/status/1630976265283829765) · 2023-03
- **2024-07: biggest ship day.** A free book, a cheaper course, and a giveaway to past buyers.
  > "And it's 100% free. Forever." — [x/2024-07.md](https://x.com/mattpocockuk/status/1810229565203112215) · 2024-07
- **2024-12: "I don't want to be a pundit."** His stance on entering AI education.
  > "I just want to teach you useful skills to get you paid." — [x/2024-12.md](https://x.com/mattpocockuk/status/1866798098204316106) · 2024-12
- **2025-06: content-for-developers thread.** His explicit content playbook.
  > "Developers are problem solvers. Lean into it." — [x/2025-06.md](https://x.com/mattpocockuk/status/1934939832058523663) · 2025-06
- **2026-01: Ralph.** The KISS loop that made his AI-coding following explode.
  > "There's an AI coding approach that lets you run seriously long-running AI agents (hours, days) that ship code while you sleep." — [x/2026-01.md](https://x.com/mattpocockuk/status/2007924876548637089) · 2026-01
- **2026-02: "9 ways it's changed my brain".** His most compact statement of AI-era engineering beliefs.
  > "AI has no taste for software architecture, be extremely explicit about the modules you want and think about their interfaces" — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02
- **2026-05: tactical vs strategic programming, and the junior problem.** His most developed essay on X.
  > "But what makes me nervous is that we've pulled down the only bridge that brought juniors into the industry." — [x/2026-05.md](https://x.com/mattpocockuk/status/2057110441864696164) · 2026-05
- **2026-06: no-ops in skills.**
  > "Learn to spot them, test them, and remove them. Your skills will thank you." — [x/2026-06.md](https://x.com/mattpocockuk/status/2069784839474032896) · 2026-06
- **2026-09: pen and paper beat the agent for course planning.**
  > "I felt out-of-control." — [x/2026-09.md](https://x.com/mattpocockuk/status/2101303255397494867) · 2026-09
- **2026-09: top reply of the corpus (3,960 likes).**
  > "You'll find yourself far ahead of the curve." — [x/2026-09.md](https://x.com/mattpocockuk/status/2102757952180686945) · 2026-09

## Related

- Principles: [Less is more](../principles/less-is-more.md) · [Humans own the strategy](../principles/humans-own-the-strategy.md) · [Revise in public](../principles/revise-in-public.md) · [Teacher, not pundit](../principles/teacher-not-pundit.md) · [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md) · [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md) · [Own the process](../principles/own-the-process.md) · [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md) · [Alignment before code](../principles/alignment-before-code.md) · [Communication and shared language](../principles/communication-and-shared-language.md) · [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md) · [Never trust an LLM](../principles/never-trust-an-llm.md) · [The codebase is the agent's environment](../principles/the-codebase-is-the-agents-environment.md) · [Context is a scarce budget](../principles/context-is-a-scarce-budget.md) · [Learning at the edge](../principles/learning-at-the-edge.md) · [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md)
- Methods: [Content strategy](../methods/content-strategy.md) · [Running the business](../methods/running-the-business.md) · [Build your own tools](../methods/build-your-own-tools.md) · [Review and retro](../methods/review-and-retro.md) · [Content production](../methods/content-production.md) · [Prototype to answer a question](../methods/prototype-to-answer-a-question.md) · [Writing for agents](../methods/writing-for-agents.md) · [AFK loops](../methods/afk-loops.md) · [Grilling](../methods/grilling.md) · [TDD at agreed seams](../methods/tdd-at-agreed-seams.md) · [Deep modules](../methods/deep-modules.md) · [Problem/solution teaching](../methods/problem-solution-teaching.md) · [The main flow](../methods/the-main-flow.md)
