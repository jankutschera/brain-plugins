---
type: method
sources: [blog, github, youtube, youtube-appearances]
quotes: 16
first_seen: 2025-10
last_seen: 2026-08
---
# Context hygiene

He manages sessions deliberately: one task per session, a visible token meter, clear by default, and a conscious choice between continuing, clearing, handing off or compacting at each phase boundary.
  > "Doing one task per session gives each task the sharpest part of the session." — [github/dictionary-of-ai-coding/README.md](https://github.com/mattpocock/dictionary-of-ai-coding/blob/HEAD/README.md)

## Evidence

- Clear is the default.
  > "clear is should be your default" — [youtube/2025-10-22_-uW5-TaVXu4_most-devs-don-t-understand-how.md](https://www.youtube.com/watch?v=-uW5-TaVXu4&t=411s) · 2025-10
- Token awareness is essential to using AI well.
  > "I believe that being conscious about the context window that you're using, the tokens that you're using is essential to using AI well." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=458s) · 2026-07
- A token status line is essential information.
  > "this is essential information on every coding session cuz you need to know exactly how many tokens you're using" — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=596s) · AI Engineer
- Compaction leaves sediment from earlier conversations.
  > "you're going to end up with this kind of sediment of different layers here from previous conversations." — [youtube/2026-05-21_dtAJ2dOd3ko_handoff-is-my-new-favourite-skill.md](https://www.youtube.com/watch?v=dtAJ2dOd3ko&t=253s) · 2026-05
- A session full of grilling decisions is valuable and should not be thrown away.
  > "Every grilling session, every decision that you make in that session is so valuable." — [youtube/2026-05-25_UzMNBN6xLLA_9-things-people-get-wrong-with.md](https://www.youtube.com/watch?v=UzMNBN6xLLA&t=485s) · 2026-05

## How it shows up

1. Put the plan in an asset outside the window (an issue or spec) before clearing.
  > "And now that I have this asset outside of my context window, I can feel happy clearing it." — [youtube/2025-10-27_kZ-zzHVUrO4_how-i-use-claude-code-for.md](https://www.youtube.com/watch?v=kZ-zzHVUrO4&t=493s) · 2025-10
2. Give sessions a budget.
  > "I've sort of have a budget of 100K for this session." — [youtube/2026-05-07_MzWIIlx0Gpc_burn-through-the-backlog-from-hell.md](https://www.youtube.com/watch?v=MzWIIlx0Gpc&t=334s) · 2026-05
3. Hand off to a fresh session with intent, not just content.
  > "It needs to not only handoff the content of the context window, it also needs to handoff the vibe of the context window and the intent of the context window." — [youtube/2026-05-12_DNqsMXH6Eog_new-skills-handoff-prototype-review-and.md](https://www.youtube.com/watch?v=DNqsMXH6Eog&t=75s) · 2026-05
4. Judge a handoff by what a zero-context session could do with it (dictionary entry).
  > "Judge a handoff by what a session with zero context could do with it." — [blog/ai-coding-dictionary__handoff.md](https://www.aihero.dev/ai-coding-dictionary/handoff) · n.d.
5. Fix token blowouts upstream by right-sizing tickets (skill doc, supporting evidence).
  > "The fix is upstream. Right-size the tickets" — [blog/skills-implement.md](https://www.aihero.dev/skills-implement) · 2026-07
6. Keep the agent stateless: no memory file.
  > "I much prefer my agent to be completely stateless" — [youtube/2026-07-17_A0scuiiGBC4_kill-your-memory-md.md](https://www.youtube.com/shorts/A0scuiiGBC4?t=40s) · 2026-07
7. Disable tools that burn context, like the ask-question UI.
  > "I actually have that tool disabled because I hate that thing so much." — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=2393s) · Unhandled Exception Podcast

## Tensions and evolution

- Handoff went from a "great upgrade" (2026-05) to "narrow" (2026-08); the docs now say it gives portability, not compression.
  > "Both have been great upgrades to how I work with agents, especially during planning." — [blog/skills__skills-changelog-handoff-prototype-review-and-writing.md](https://www.aihero.dev/skills/skills-changelog-handoff-prototype-review-and-writing) · 2026-05
  > "What it gives you is **portability**, not compression, so the skill is narrower than it sounds." — [blog/skills-handoff.md](https://www.aihero.dev/skills-handoff) · 2026-05
- He prefers continuing a session over a summary when he can, because the conversation stays a primary source.
  > "it is the only move that keeps the conversation as a primary source rather than a summary of one." — [blog/skills__skills-changelog-v12-wait-what-writing-for-agents-claude-code-plugin-and-more.md](https://www.aihero.dev/skills/skills-changelog-v12-wait-what-writing-for-agents-claude-code-plugin-and-more) · 2026-08

## Related

- [Context is a scarce budget](../principles/context-is-a-scarce-budget.md)
- [Less is more](../principles/less-is-more.md)
- [The main flow](the-main-flow.md)
- [Never trust an LLM](../principles/never-trust-an-llm.md)
