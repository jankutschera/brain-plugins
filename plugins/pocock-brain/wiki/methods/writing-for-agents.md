---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 25
first_seen: 2025-06
last_seen: 2026-10
---
# Writing for agents

He packages his process as short, user-invoked skills and writes every agent-facing text by subtraction: leading words, context pointers, positive phrasing, clear completion criteria, and deletion of anything that changes nothing.
  > "And these skills help me encode my process so the AI has a really strict path it can walk down every single time." — [youtube/2026-03-16_EJyuu6zlQCg_5-claude-code-skills-i-use.md](https://www.youtube.com/watch?v=EJyuu6zlQCg&t=42s) · 2026-03

## Evidence

- Process has never been more important, and skills bundle it.
  > "I've been an engineer for nearly a decade. Right now, process has never been more important. And skills are the best way to bundle up processes for agents." — [x/2026-03.md](https://x.com/mattpocockuk/status/2033647563627212953) · 2026-03
- Short is fine.
  > "Skills don't have to be long to be impactful. You just need to choose the right words at the right time." — [blog/5-agent-skills-i-use-every-day.md](https://www.aihero.dev/5-agent-skills-i-use-every-day) · 2026-03
- His great skills share leading words.
  > "I've realised that all of the great skills I've written share one thing in common. They make heavy use of Leitwörter - leading words." — [x/2026-06.md](https://x.com/mattpocockuk/status/2066922013000671731) · 2026-06
- Skills are his process put into words: introspection.
  > "You're essentially trying to put your process into words. And that's what I've been doing with the skills." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=5606s) · The Pragmatic Engineer
- Writing well for humans works for AI too.
  > "if you write well for humans, turns out that the AI actually responds really well to that." — [youtube-appearances/unknown_hQDSr7uwu6E_the-future-of-developer-content-matt.md](https://www.youtube.com/watch?v=hQDSr7uwu6E&t=1278s) · Sanity
- Negative instructions waste budget.
  > "These kind of negative instructions to the LLM are really bad, I think" — [youtube/2026-02-25_3CSi8QAoN-s_how-to-actually-force-claude-code.md](https://www.youtube.com/watch?v=3CSi8QAoN-s&t=102s) · 2026-02

## How it shows up

1. Decide the trigger: mostly user-invoked, which saves tokens and keeps him in control.
  > "my skills are mostly user invoked." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=249s) · 2026-07
  > "every single skill that you write it leaks a description this description here into the context window." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1273s) · David Ondrej
2. Split steps from reference; hide branching reference behind context pointers.
  > "I think of there as being two main units that you need to put into most skills. These two units are the steps and the reference." — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=451s) · AI Engineer
  > "Hide branching reference material behind context pointers." — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=686s) · AI Engineer
3. Steer with leading words already in the model's priors.
  > "Refactoring is such an old book, such a well-cited book, that these uh kind of smells are deep in the agent's priors." — [youtube/2026-07-08_A8mokin_YOs_new-skills-v1-1-brings-wayfinder.md](https://www.youtube.com/watch?v=A8mokin_YOs&t=424s) · 2026-07
4. Hide future steps to force legwork on the current one.
  > "this is a really cool technique for increasing legwork on the step that you're on by hiding the future goal, hiding the future steps." — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=976s) · AI Engineer
5. End each step on a completion criterion.
  > "Every step ends on a **completion criterion**, the condition that tells the agent the work is done." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)
6. Prompt the positive.
  > "Prompt the **positive**: state the target behaviour (\"write one-line comments\") so the banned one is never spoken." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)
7. Prune: hunt no-ops, delete whole sentences, use deletion tests.
  > "When a sentence fails, delete the whole sentence rather than trim words from it." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)
  > "People ask me a lot how I get my skills so small, and it's just using these techniques, using deletion tests" — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1131s) · AI Engineer
8. Keep instruction files to navigation pointers; cache only what the agent cannot find by looking.
  > "`AGENTS.md` and `CLAUDE.md` are for navigation pointers and little else." — [blog/skills-retro.md](https://www.aihero.dev/skills-retro) · 2026-10
  > "Cache what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)
- In one-off prompts he gives the reason why.
  > "The last few days I have forced myself to end every prompt I write with: "The reason why is" — [x/2025-06.md](https://x.com/mattpocockuk/status/1935056514416284112) · 2025-06
- He reads skills himself instead of trusting agent-written ones.
  > "This is why reading the skills is actually blooming important" — [youtube-appearances/unknown_LMpMmOWTtVk_matt-pocock-built-the-skills-repo.md](https://www.youtube.com/watch?v=LMpMmOWTtVk&t=1464s) · The Next New Thing

## Tensions and evolution

- In October 2025 "sacrifice grammar" was his favourite global rule; by 2026 he had moved it into a skill, then dropped it.
  > ""Be extremely concise. Sacrifice grammar for the sake of concision."" — [x/2025-10.md](https://x.com/mattpocockuk/status/1974528553569137095) · 2025-10
  > "But I've since dropped this idea in preference to a grilling session" — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=2930s) · AI Engineer
- His earlier prompts shouted prohibitions, which his later guide warns against.
  > "ONLY WORK ON A SINGLE TASK." — [github/ralph-workshop-repo-001/plans/prompt.md](https://github.com/mattpocock/ralph-workshop-repo-001/blob/HEAD/plans/prompt.md)
- He is careful not to overfit docs to one model (skill doc, supporting evidence).
  > "Mostly no, and over-fitting to one model causes its own problems." — [blog/skills-writing-for-agents.md](https://www.aihero.dev/skills-writing-for-agents) · 2026-07

## Related

- [Less is more](../principles/less-is-more.md)
- [Communication and shared language](../principles/communication-and-shared-language.md)
- [Own the process](../principles/own-the-process.md)
- [Context is a scarce budget](../principles/context-is-a-scarce-budget.md)
