---
type: source
raw: raw/youtube/
files: 298
words: 502861
date_range: 2020-11-10 – 2026-10-05
---
# YouTube: @mattpocockuk

## Coverage

- Matt's own channel, https://www.youtube.com/@mattpocockuk, using the /videos, /shorts and /streams tabs. The channel has no podcasts tab. Collected 2026-10-06.
- 301 uploads found (144 videos, 136 shorts, 21 streams). 298 transcripts saved (144 videos, 134 shorts, 20 streams). 3 failed because captions are disabled: 2 shorts and the stream with Poteto.
- All 298 are **auto-generated captions**. Expect mishearings, for example "claw code" for Claude Code, "Versel" for Vercel, "spectrum development" for spec-driven development, "typ script", "enemies" for "anys". Pre-2024 captions mostly have no punctuation. Per-segment timestamps are in each `<name>.segments.json`.
- Method: `yt-dlp` for enumeration and metadata, then `youtube_transcript_api` (23 files) or the Apify actor `johnvc/YoutubeTranscripts` (275 files) for captions. Raw caption text is joined into roughly 60-second paragraphs with no summarizing.
- Size is 502,861 words (wc -w, including YAML headers).
- By year:

| Year | Videos | Shorts | Streams | Words (approx.) |
|---|---|---|---|---|
| 2020–21 | 7 | 0 | 0 | 27k |
| 2022 | 45 | 4 | 1 | 59k |
| 2023 | 36 | 28 | 11 | 180k |
| 2024 | 12 | 23 | 3 | 38k |
| 2025 | 15 | 60 | 1 | 66k |
| 2026 | 29 | 19 | 4 | 132k |

- Arc: XState and state machines (2020–22), then TypeScript tips and Total TypeScript (2022–24), then AI apps in TypeScript and AI Hero (2025), then AI coding with Claude Code, his skills repo, Ralph loops and Sandcastle (late 2025–2026).
- Streams with guests (Dex Horthy, Uncle Bob, Anders Hejlsberg, Aleksandra Sikora) mix speakers. Only turns that are clearly Matt's are quoted from them.
- Extraction depth: about 90 transcripts were read in full, including every 2026 video and most 2025–26 shorts. About 35 long videos and streams were read partially through targeted searches, mainly 2021–24 XState and TypeScript streams.

## What this source shows about him

- He sees himself as a teacher first.
  > "I am a teacher. I am not a pundit." — [youtube/2026-05-13_lNOQaakmyDU_anthropic-s-dedicated-monthly-credit-is.md](https://www.youtube.com/watch?v=lNOQaakmyDU&t=578s) · 2026-05
- He came to coding from teaching and music, and keeps returning to pedagogy.
  > "I've been teaching stuff for 10 years. I was a voice coach for 6 years and I've been doing this job teaching devs for 4 years." — [youtube/2026-06-08_s5T5oQJcJ6U_learn-anything-with-the-teach-skill.md](https://www.youtube.com/watch?v=s5T5oQJcJ6U&t=0s) · 2026-06
- His channel grew out of short Twitter tips, and he still values short, dense teaching.
  > "I know that what works is 2-minute videos." — [youtube/2022-12-20_l2iVQkY6mXQ_i-quit-vercel-to-make-content.md](https://www.youtube.com/watch?v=l2iVQkY6mXQ&t=247s) · 2022-12
- His central belief in the AI era is that old engineering fundamentals carry over.
  > "I really believe that AI coding is not that different from human coding." — [youtube/2026-02-21_yv8VZpov8bk_i-m-using-claude-worktree-for.md](https://www.youtube.com/watch?v=yv8VZpov8bk&t=443s) · 2026-02
- He moved from AI skeptic to AI-coding educator over 2023–2026.
  > "Before I tried plan mode, I was a total AI skeptic." — [youtube/2026-01-15_WNx-s-RxVxk_i-was-an-ai-skeptic-then.md](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=3s) · 2026-01
- In 2026 he talks constantly about the context window and its limits.
  > "The context window is the main constraint that most AI coding agents face these days." — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=22s) · 2025-10
- He keeps the human in charge of strategy and treats agents as tactical help.
  > "I think of my skills as empowering the user, not empowering the agent." — [youtube/2026-07-17_32LyZyFQhCQ_framework-hell-tutorial-hell-now-skill.md](https://www.youtube.com/shorts/32LyZyFQhCQ?t=25s) · 2026-07
- His TypeScript taste is pragmatic: stay close to JavaScript, avoid TypeScript-only runtime features.
  > "anything that does like typescript stuff at runtime is odd to me" — [youtube/2025-01-24_zeNh4fuJhcA_typescript-shipped-a-flag-to-disable.md](https://www.youtube.com/watch?v=zeNh4fuJhcA&t=104s) · 2025-01
- He revises his own advice in public.
  > "So, I'm going to do something I find deeply uncomfortable, which is look at my old work." — [youtube/2025-04-18_e0AIkYrXAYE_types-vs-interfaces-what-i-got.md](https://www.youtube.com/watch?v=e0AIkYrXAYE&t=19s) · 2025-04
- He defines programming as clarifying intent, from his 2023 streams to his 2026 videos.
  > "that's what programming is it's about turning a poorly defined spec into a well-defined one" — [youtube/2023-03-07_WuHSnvsO6Mg_total-typescript-tour-and-ama.md](https://www.youtube.com/watch?v=WuHSnvsO6Mg&t=935s) · 2023-03
- He positions his audience as serious engineers, not vibe coders.
  > "This is not for vibe coders. We are people that are serious about AI engineering and serious about building applications that are built to last." — [youtube/2026-03-03_Ah9p7v7nJWg_the-7-phases-of-ai-driven.md](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=42s) · 2026-03

## Notable pieces

- **I quit Vercel to make content (2022-12).** His origin story: Twitter tips, Vercel, then Total TypeScript.
  > "I suggest choosing something that you know really well, getting absolutely deep into it until you find the nuggets of information that are widely useful." — [youtube/2022-12-20_l2iVQkY6mXQ_i-quit-vercel-to-make-content.md](https://www.youtube.com/watch?v=l2iVQkY6mXQ&t=281s) · 2022-12
- **Enums considered harmful (2022-12).** A canonical TypeScript hot take that sets his "structural, not nominal" taste.
  > "I don't even teach enums in total typescript That's how little I think of them" — [youtube/2022-12-15_jjMbPt_H3RQ_enums-considered-harmful.md](https://www.youtube.com/watch?v=jjMbPt_H3RQ&t=468s) · 2022-12
- **Total TypeScript tour and AMA (2023-03).** An early skeptical take on ChatGPT and a lasting definition of programming.
  > "it's not about writing code it's about being able to take someone's idea whether it's yours or not and put it into a format where a computer can understand it" — [youtube/2023-03-07_WuHSnvsO6Mg_total-typescript-tour-and-ama.md](https://www.youtube.com/watch?v=WuHSnvsO6Mg&t=947s) · 2023-03
- **Types vs interfaces: what I got wrong in 2022 (2025-04).** He reviews his old video on camera and reverses his advice.
  > "So I think my recommendation has unbelievably changed again." — [youtube/2025-04-18_e0AIkYrXAYE_types-vs-interfaces-what-i-got.md](https://www.youtube.com/watch?v=e0AIkYrXAYE&t=511s) · 2025-04
- **Effect: the unreadable library that captured my heart (2025-06).** He embraces a hard library and rejects FP branding.
  > "Personally, I feel like I'm writing some of the best code in my career using effect." — [youtube/2025-06-30_S2GChOwivwQ_effect-the-unreadable-library-that-captured.md](https://www.youtube.com/watch?v=S2GChOwivwQ&t=772s) · 2025-06
- **Most devs don't understand how context windows work (2025-10).** The basis for his later smart-zone/dumb-zone teaching.
  > "if there is a skill issue that I see most often with devs, it is not thinking enough about the context window." — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=17s) · 2025-10
- **Ship working code while you sleep: Ralph Wiggum (2026-01).** His shift from multi-phase plans to looping agents over a backlog.
  > "Instead of this kind of like really anal retentive planner here, Ralph puts you in the seat of the requirements gatherer." — [youtube/2026-01-05__IK18goX4X8_ship-working-code-while-you-sleep.md](https://www.youtube.com/watch?v=_IK18goX4X8&t=868s) · 2026-01
- **I was an AI skeptic. Then I tried plan mode (2026-01).** His conversion story.
  > "And the more feel I can get for AI, I know the more secure my career is going forward." — [youtube/2026-01-15_WNx-s-RxVxk_i-was-an-ai-skeptic-then.md](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=707s) · 2026-01
- **Never run claude /init (2026-02).** The instruction-budget argument against global context files.
  > "Too much is global. Too much is going to go out of date and just rot away." — [youtube/2026-02-24_9tmsq-Gvx6g_never-run-claude-init.md](https://www.youtube.com/watch?v=9tmsq-Gvx6g&t=433s) · 2026-02
- **Your codebase is NOT ready for AI (2026-02).** Deep modules and gray boxes as AI-era architecture.
  > "So, what works here for humans is also great for AI." — [youtube/2026-02-26_uC44zFz7JSM_your-codebase-is-not-ready-for.md](https://www.youtube.com/watch?v=uC44zFz7JSM&t=395s) · 2026-02
- **Building a REAL feature with Claude Code (2026-03).** A 9,700-word end-to-end session: grill, PRD, issues, AFK Ralph, human QA.
  > "it's slow because you're trying to extract ideas out of your human brain." — [youtube/2026-03-18_hX7yG1KVYhI_building-a-real-feature-with-claude.md](https://www.youtube.com/watch?v=hX7yG1KVYhI&t=2007s) · 2026-03
- **Never Trust An LLM (2026-03).** Hallucination explained for a general audience.
  > "LLMs hallucinate because guessing is more highly rewarded than refusal" — [youtube/2026-03-27_9VNG0h4pLh0_never-trust-an-llm.md](https://www.youtube.com/watch?v=9VNG0h4pLh0&t=592s) · 2026-03
- **I stopped using /grill-me for coding (2026-05).** He brings DDD's ubiquitous language into agent planning.
  > "what is the thinnest layer of documentation I could use to just give the AI a bit more of a leg up." — [youtube/2026-05-14_6BB6exR8Zd8_i-stopped-using-grill-me-for.md](https://www.youtube.com/watch?v=6BB6exR8Zd8&t=210s) · 2026-05
- **Learn anything with the /teach skill (2026-06).** His teaching philosophy turned into an agent skill.
  > "teach someone in the area where they are perfectly challenged but not intimidated." — [youtube/2026-06-08_s5T5oQJcJ6U_learn-anything-with-the-teach-skill.md](https://www.youtube.com/watch?v=s5T5oQJcJ6U&t=442s) · 2026-06
- **/wayfinder: Nothing is too big to plan anymore (2026-07).** Planning under uncertainty as a map of decision tickets.
  > "There is no more fun feeling than starting a new Wayfinder session, and knowing that you're going to see something awesome," — [youtube/2026-07-30_F3lL98Pj90o_wayfinder-nothing-is-too-big-to.md](https://www.youtube.com/watch?v=F3lL98Pj90o&t=873s) · 2026-07
- **New Skills v1.3: /pr, /implement-spec, /retro (2026-10).** The latest piece, on verification, reviewable PRs and reviewing agent sessions.
  > "This evidence is an essential part of learning to trust your agent" — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=353s) · 2026-10

## Related

- Principles: [Context is a scarce budget](../principles/context-is-a-scarce-budget.md) · [Never trust an LLM](../principles/never-trust-an-llm.md) · [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md) · [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md) · [Less is more](../principles/less-is-more.md) · [Revise in public](../principles/revise-in-public.md) · [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md) · [Alignment before code](../principles/alignment-before-code.md) · [Communication and shared language](../principles/communication-and-shared-language.md) · [Learning at the edge](../principles/learning-at-the-edge.md) · [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md) · [The codebase is the agent's environment](../principles/the-codebase-is-the-agents-environment.md) · [Humans own the strategy](../principles/humans-own-the-strategy.md) · [Own the process](../principles/own-the-process.md) · [Teacher, not pundit](../principles/teacher-not-pundit.md) · [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md)
- Methods: [Context hygiene](../methods/context-hygiene.md) · [Grilling](../methods/grilling.md) · [The main flow](../methods/the-main-flow.md) · [Prototype to answer a question](../methods/prototype-to-answer-a-question.md) · [Review and retro](../methods/review-and-retro.md) · [TDD at agreed seams](../methods/tdd-at-agreed-seams.md) · [AFK loops](../methods/afk-loops.md) · [Writing for agents](../methods/writing-for-agents.md) · [Build your own tools](../methods/build-your-own-tools.md) · [Deep modules](../methods/deep-modules.md) · [Content strategy](../methods/content-strategy.md) · [Evals as tests](../methods/evals-as-tests.md) · [Problem/solution teaching](../methods/problem-solution-teaching.md)
