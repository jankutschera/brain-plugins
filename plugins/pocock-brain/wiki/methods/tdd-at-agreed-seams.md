---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 21
first_seen: 2026-02
last_seen: 2026-07
---
# TDD at agreed seams

Agents build test-first, one red test and one implementation at a time, at interfaces the human agreed in advance, so tests stay honest and survive rewrites.
  > "The most effective technique I've found to improve Claude Code's output is 20 years old: Write a failing test first." — [x/2026-02.md](https://x.com/mattpocockuk/status/2025935480609468862) · 2026-02

## Evidence

- He calls good TDD his most consistent lever on agent output.
  > "Doing really, really good TDD has been the most consistent way that I've improved agents outputs." — [youtube/2026-03-16_EJyuu6zlQCg_5-claude-code-skills-i-use.md](https://www.youtube.com/watch?v=EJyuu6zlQCg&t=586s) · 2026-03
- Failing first stops agents cheating.
  > "This constraint prevents cheating. If a test fails first, the LLM can't fake it, it has to write real implementation." — [blog/skill-test-driven-development-claude-code.md](https://www.aihero.dev/skill-test-driven-development-claude-code) · 2026-02
- Agents otherwise write horizontal layers and one-shot the implementation.
  > "they love to create huge horizontal layers and then they'll try to oneshot an implementation" — [youtube/2026-02-23_hYZdIwFIy-c_red-green-refactor-is-op-with.md](https://www.youtube.com/watch?v=hYZdIwFIy-c&t=215s) · 2026-02
- Seeing red then green lets him skip reading every test.
  > "I don't necessarily read all of the implementations because I've seen it go red and then go green." — [youtube/2026-02-23_hYZdIwFIy-c_red-green-refactor-is-op-with.md](https://www.youtube.com/watch?v=hYZdIwFIy-c&t=158s) · 2026-02
- Better tests make a better agent.
  > "And the better your tests are, the better the output from the agent is going to be." — [youtube/2026-04-29_3MP8D-mdheA_how-to-de-slop-a-codebase.md](https://www.youtube.com/watch?v=3MP8D-mdheA&t=620s) · 2026-04

## How it shows up

1. Agree the seams with the human before any test exists.
  > "**Test only at pre-agreed seams.** Before writing any test, write down the seams under test and confirm them with the user." — [github/skills/skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/tdd/SKILL.md)
2. Work in vertical slices: one test, one implementation, repeat.
  > "Work in **vertical slices** instead: one test → one implementation → repeat, each test a **tracer bullet** that responds to what the last cycle taught you." — [github/skills/skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/tdd/SKILL.md)
3. Test behaviour through public interfaces; expected values come from an independent source.
  > "Tests verify behavior through public interfaces, not implementation details. Code can change entirely; tests shouldn't." — [github/skills/skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/tdd/SKILL.md)
  > "Expected values must come from an independent source of truth: a known-good literal, a worked example, the spec." — [github/skills/skills/engineering/tdd/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/tdd/SKILL.md)
4. Mock only at system boundaries; never your own modules.
  > "Never mock your own modules." — [blog/skills-tdd.md](https://www.aihero.dev/skills-tdd) · 2026-04
5. No tests for what types already guarantee, and none that restate the implementation.
  > ""Don't write tests for what the type system already guarantees."" — [x/2026-02.md](https://x.com/mattpocockuk/status/2023712176729715184) · 2026-02
6. Fewer seams are better; design out bad tests with deeper modules.
  > "The fewer test seams you have in your app, the better" — [x/2026-05.md](https://x.com/mattpocockuk/status/2059955079067713960) · 2026-05
  > "So you can actually design your way out of these bad checks." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=507s) · AI Engineer

## Tensions and evolution

- Refactor was a phase in February 2026; by July it moved out of TDD and into review, because agents skipped it.
  > "after all tests pass, look for refactor candidates." — [youtube/2026-02-23_hYZdIwFIy-c_red-green-refactor-is-op-with.md](https://www.youtube.com/watch?v=hYZdIwFIy-c&t=254s) · 2026-02
  > "So it's no longer a red green refactor loop, it's more just red green." — [youtube/2026-07-08_A8mokin_YOs_new-skills-v1-1-brings-wayfinder.md](https://www.youtube.com/watch?v=A8mokin_YOs&t=782s) · 2026-07
  > "There is no refactor phase. The skill dropped it in June 2026 because agents almost never performed it" — [blog/skills-tdd.md](https://www.aihero.dev/skills-tdd) · 2026-04
- He cares about results over orthodoxy.
  > "Whether the result still counts as TDD by the book matters less than whether the loop produces better code." — [blog/skills-tdd.md](https://www.aihero.dev/skills-tdd) · 2026-04
- "Absolutely essential" in his workshop became a "mixed relationship": TDD optimises for small human working memory, so he now also accepts proof.
  > "TDD optimizes for having a very small working memory, right?" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4722s) · The Pragmatic Engineer
- His early TDD skill shouted prohibitions; his later writing guide says negation backfires.
  > "**DO NOT write all tests first, then all implementation.**" — [github/ai-engineer-workshop-2026-project/.claude/skills/tdd/SKILL.md](https://github.com/mattpocock/ai-engineer-workshop-2026-project/blob/HEAD/.claude/skills/tdd/SKILL.md)
  > "steering by prohibition drags the forbidden behaviour into context and makes it _more_ available, not less." — [github/skills/skills/productivity/writing-for-agents/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/writing-for-agents/SKILL.md)

## Related

- [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md)
- [Deep modules](deep-modules.md)
- [Diagnosing bugs](diagnosing-bugs.md)
- [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md)
