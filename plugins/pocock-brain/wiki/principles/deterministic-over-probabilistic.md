---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 22
first_seen: 2024-07
last_seen: 2026-10
---
# Deterministic over probabilistic

If something can be built or enforced deterministically, it should be; the model is for what code cannot do, and a check beats a sentence in a Markdown file.
  > "A check can fail. A sentence in a Markdown file cannot." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10

## Evidence

- In 2025 he set determinism as the default for AI systems.
  > "**Deterministic systems should be your default choice for any task**, until you hit a barrier which can only be solved by an LLM." — [blog/what-are-llms-used-for.md](https://www.aihero.dev/what-are-llms-used-for) · 2025-03
- He prefers workflows to agents, and says so on video and in writing.
  > "workflows are better than agents." — [youtube/2025-06-05_b2ntTXVlGQk_agents-are-dead-long-live-workflows.md](https://www.youtube.com/shorts/b2ntTXVlGQk?t=36s) · 2025-06
  > "I don't know whether it's me being old and boring, but I am more excited by workflows than agents." — [blog/what-is-an-agent.md](https://www.aihero.dev/what-is-an-agent) · 2025-09
- His line between agent and workflow is who decides when to stop.
  > "To me, the key difference is who decides when to stop the program." — [youtube/2025-10-08_AtYtuVTZCQU_most-devs-don-t-understand-what.md](https://www.youtube.com/watch?v=AtYtuVTZCQU&t=249s) · 2025-10
- An instruction reduces risk; a hook prevents it.
  > "Adding "don't use `git push`" to your `CLAUDE.md` _reduces_ the chance of a force push. It doesn't _prevent_ it." — [blog/how-to-use-claude-code-hooks-to-enforce-the-right-cli.md](https://www.aihero.dev/how-to-use-claude-code-hooks-to-enforce-the-right-cli) · 2026-02
- The retro skill defaults to building checks over writing rules.
  > "Default to building the check over writing the rule." — [github/skills/skills/engineering/retro/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/retro/SKILL.md)
- For AFK orchestration, a script beats an agent.
  > "The agent loop is worse than a deterministic loop." — [blog/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md.md](https://www.aihero.dev/skills-changelog-v13-implement-spec-pr-retro-and-glossary-md) · 2026-10

## How it shows up

- He moves rules out of the prompt into hooks and lint rules.
  > "You get to take instructions out of your instruction budget and enforce them deterministically." — [youtube/2026-02-25_3CSi8QAoN-s_how-to-actually-force-claude-code.md](https://www.youtube.com/watch?v=3CSi8QAoN-s&t=337s) · 2026-02
  > "I really hate positional parameters in functions, and turning them into ESLint rules so that I can lint Claude into the right thing" — [youtube/2026-02-25_3CSi8QAoN-s_how-to-actually-force-claude-code.md](https://www.youtube.com/watch?v=3CSi8QAoN-s&t=359s) · 2026-02
- Ralph, his famous loop, is a bash loop.
  > "Ralph is a bash loop." — [youtube/2026-01-05__IK18goX4X8_ship-working-code-while-you-sleep.md](https://www.youtube.com/watch?v=_IK18goX4X8&t=275s) · 2026-01
- A repeated mistake becomes a check, not a line in AGENTS.md.
  > "Found an error? Do a /retro, and make it impossible next time" — [x/2026-09.md](https://x.com/mattpocockuk/status/2099859946053533933) · 2026-09
- He prefers removing a class of error by design to testing for it.
  > "More "let me make that class of error impossible with a better design"" — [x/2026-08.md](https://x.com/mattpocockuk/status/2086830429416333758) · 2026-08
- User-invoked skills remove the unpredictability of model-triggered ones.
  > "what you get is just you're removing a class of problem from even being a problem." — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=419s) · AI Engineer

## Tensions and evolution

- In 2025 workflows beat agents; by 2026 AFK agents were his most productive mode, but wrapped in deterministic loops.
  > "I have found this is the most productive way of working with agents." — [youtube/2026-05-13_lNOQaakmyDU_anthropic-s-dedicated-monthly-credit-is.md](https://www.youtube.com/watch?v=lNOQaakmyDU&t=165s) · 2026-05
  > "that's just a loop, right? You just have to just loop over that, and that can be deterministic. It doesn't have to be an agent." — [youtube-appearances/unknown_LMpMmOWTtVk_matt-pocock-built-the-skills-repo.md](https://www.youtube.com/watch?v=LMpMmOWTtVk&t=1192s) · The Next New Thing
- In January 2026 the agent picked the next task; by October a script walks the tickets.
  > "With Ralph, the agent picks what to work on next from your PRD. You define the end state. Ralph gets there." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
  > "once you've set up your deterministic loop, it's going to run the same way every time." — [youtube/2026-10-05_BsJGo1wFTvQ_new-skills-v1-3-brings-pr.md](https://www.youtube.com/watch?v=BsJGo1wFTvQ&t=117s) · 2026-10
- He distrusted self-improvement loops in June 2026, then put `/retro` into the main flow in October, framed as building checks.
  > "I have a deep distrust of almost any 'self-improvement' loop in coding agents" — [x/2026-06.md](https://x.com/mattpocockuk/status/2066612676520779867) · 2026-06
  > "I've added /retro into the "Main Flow" of my skills - I consider it that important." — [x/2026-10.md](https://x.com/mattpocockuk/status/2107037429324513535) · 2026-10
- Pre-commit hooks went from hated (2024) to desirable friction (2026).
  > "We're talking about pre-commit hooks? Nice. I hate them." — [x/2024-07.md](https://x.com/mattpocockuk/status/1810922990785135063) · 2024-07
  > "Friction via pre-commit hooks/CI/strong types is now super desirable" — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02

## Related

- [Feedback is the speed limit](feedback-is-the-speed-limit.md)
- [Less is more](less-is-more.md)
- [AFK loops](../methods/afk-loops.md)
- [Review and retro](../methods/review-and-retro.md)
- [Evals as tests](../methods/evals-as-tests.md)
