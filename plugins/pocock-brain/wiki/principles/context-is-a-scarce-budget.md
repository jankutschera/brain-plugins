---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 21
first_seen: 2025-09
last_seen: 2026-08
---
# Context is a scarce budget

Model quality drops as the context window fills, so every token competes for attention and work should be sized to the "smart zone", not the advertised window.
  > "The context window is the main constraint that most AI coding agents face these days." — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=22s) · 2025-10

## Evidence

- Less in the window means better output.
  > "the more you put in the context window, the worse the AI is going to be." — [blog/creating-the-perfect-claude-code-status-line.md](https://www.aihero.dev/creating-the-perfect-claude-code-status-line) · 2025-10
- A bigger window does not change the arithmetic.
  > "It's still 100K of smart, and 900K of dumb." — [x/2026-03.md](https://x.com/mattpocockuk/status/2034572011175907474) · 2026-03
  > "They shipped a lot more dumb zone to you essentially." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=2278s) · AI Engineer
- Irrelevant context is noise, not neutral.
  > "Content that doesn't serve the task isn't neutral — it's noise over everything that does." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)
- More tools make the model worse.
  > "the more tools that you give the LLM, the worse it performs." — [youtube/2025-09-25__1KrC_5Xv4s_stop-giving-your-llm-more-tools.md](https://www.youtube.com/shorts/_1KrC_5Xv4s?t=3s) · 2025-09
- He calls not thinking about context the most common skill issue.
  > "if there is a skill issue that I see most often with devs, it is not thinking enough about the context window." — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=17s) · 2025-10
- He recommends his own paranoia.
  > "This is a constant source of paranoia for me." — [blog/creating-the-perfect-claude-code-status-line.md](https://www.aihero.dev/creating-the-perfect-claude-code-status-line) · 2025-10

## How it shows up

- He sizes tickets to one smart zone and runs one task per session.
  > "Each one of these tickets is supposed to just be the size of a single context window or a single smart zone." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=751s) · 2026-07
- He clears rather than compacts.
  > "And devs love compacting for some reason, but I hate it." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=636s) · AI Engineer
- He is extremely cautious about MCP servers and trims Claude Code's own system prompt.
  > "I tend to be extremely, extremely cautious about adding MCP servers to my setup" — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=451s) · 2025-10
  > "from 25K down to around 8K" — [youtube/2026-07-16_oLx4yCbeklQ_claude-code-s-system-tools-are.md](https://www.youtube.com/shorts/oLx4yCbeklQ?t=78s) · 2026-07
- He built a logging proxy to see what fills the context.
  > "A zero-dependency logging proxy that sits between Claude Code and the Anthropic" — [github/_gists/5b3d76ea21f5f698aefded47a9cea3b1/README.md](https://gist.github.com/mattpocock/5b3d76ea21f5f698aefded47a9cea3b1)
- He rejected Anthropic's Ralph plugin because it kept context instead of clearing it.
  > "It defeats the entire purpose of Ralph - to aggressively clear the context window on each task to keep the LLM in the smart zone." — [x/2026-01.md](https://x.com/mattpocockuk/status/2014627397241282564) · 2026-01

## Tensions and evolution

- Where the dumb zone starts keeps moving: about 60% (2025-10), 40% (2026-01), 120k (2026-05), 140-150k (2026-07), with 100k in one workshop.
  > "Ooh, I think about 60 is probably where I want to stop" — [blog/creating-the-perfect-claude-code-status-line.md](https://www.aihero.dev/creating-the-perfect-claude-code-status-line) · 2025-10
  > "I consider the dumb zone to start at around 40% usage. Do smaller tasks. Use fewer tokens. Stay in the smart zone." — [x/2026-01.md](https://x.com/mattpocockuk/status/2010388114167202210) · 2026-01
  > "around by the 120k token mark, I start to feel like I'm in the dumb zone." — [youtube/2026-05-21_dtAJ2dOd3ko_handoff-is-my-new-favourite-skill.md](https://www.youtube.com/watch?v=dtAJ2dOd3ko&t=165s) · 2026-05
  > "I used to think it was around 100K tokens about 6 months ago." — [youtube/2026-07-20_sOd7svdu_1I_what-is-the-dumb-zone.md](https://www.youtube.com/shorts/sOd7svdu_1I?t=82s) · 2026-07
  > "I would say around 100K is kind of my new marker for this." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=244s) · AI Engineer
- He calls the smart zone a heuristic rather than a hard cliff.
  > "It's just a very very simple huristic to say that you should probably spend most of your time in the smart zone if you can" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=1644s) · Unhandled Exception Podcast
- He credits the term to Dex Horthy.
  > "It's not my term. That's Dex Hardy's term. I stole it and it's very very good." — [youtube/2026-08-19_zcLPGC-tvgk_live-uncle-bob-on-software-fundamentals.md](https://www.youtube.com/watch?v=zcLPGC-tvgk&t=921s) · 2026-08

## Related

- [Context hygiene](../methods/context-hygiene.md)
- [Less is more](less-is-more.md)
- [The main flow](../methods/the-main-flow.md)
- [AFK loops](../methods/afk-loops.md)
