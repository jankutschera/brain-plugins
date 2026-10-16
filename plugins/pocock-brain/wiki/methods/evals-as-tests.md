---
type: method
sources: [blog, github, youtube, youtube-appearances]
quotes: 17
first_seen: 2024-11
last_seen: 2025-06
---
# Evals as tests

For LLM-powered apps (his 2024-2025 AI engineering phase) he treats evals as the unit tests of AI, scored rather than pass/fail, fed by real user data, and climbed toward through the simplest technique first.
  > "Evals are the AI engineer's unit tests." — [blog/what-are-evals.md](https://www.aihero.dev/what-are-evals) · 2024-11

## Evidence

- Evalite maps evals onto the test-runner model.
  > "**Evals are to AI-powered apps what tests are to regular apps**." — [github/evalite/apps/evalite-docs/src/content/docs/what-is-evalite.mdx](https://github.com/mattpocock/evalite/blob/HEAD/apps/evalite-docs/src/content/docs/what-is-evalite.mdx)
- Vibe-checking changes is dangerous.
  > "You make a change, try a few favourite prompts and see if it "feels" better. But this is a dangerous way to work." — [blog/what-are-evals.md](https://www.aihero.dev/what-are-evals) · 2024-11
- Users supply the best eval data.
  > "The best data for your evals comes from your users." — [blog/what-are-evals.md](https://www.aihero.dev/what-are-evals) · 2024-11
- AI apps need an experimentation mindset.
  > "you go from a building mindset to an experimentation mindset." — [youtube/2025-06-20_EjjPMHwPRlw_the-ai-engineer-mindset-is-wild.md](https://www.youtube.com/shorts/EjjPMHwPRlw?t=36s) · 2025-06
- Evaluate a model inside your own app.
  > "The only way a model can truly be evaluated is by testing it in the context of your application." — [blog/how-to-choose-an-llm.md](https://www.aihero.dev/how-to-choose-an-llm) · 2025-03

## How it shows up

1. Expect the first version to be bad; measure to climb out of the "Vibes-Only Trough".
  > "Here's an uncomfortable truth: the first version of your app won't be great - you simply don't have enough data yet." — [blog/the-ai-engineer-mindset.md](https://www.aihero.dev/the-ai-engineer-mindset) · 2025-03
  > "If you can't measure it, you can't improve it." — [blog/the-ai-engineer-mindset.md](https://www.aihero.dev/the-ai-engineer-mindset) · 2025-03
2. Score from 0 to 100 instead of pass/fail.
  > "Normal tests give you a pass or fail metric. **Evals give you a score from 0-100** based on how well your app is performing." — [github/evalite/apps/evalite-docs/src/content/docs/what-is-evalite.mdx](https://github.com/mattpocock/evalite/blob/HEAD/apps/evalite-docs/src/content/docs/what-is-evalite.mdx)
3. Build on Vitest so existing tooling carries over, and keep it local.
  > "Based on Vitest, so you can use all the same tools (mocks, lifecycle hooks) you're used to" — [github/evalite/apps/evalite-docs/src/content/docs/what-is-evalite.mdx](https://github.com/mattpocock/evalite/blob/HEAD/apps/evalite-docs/src/content/docs/what-is-evalite.mdx)
4. Treat LLM-as-judge as a smoke test.
  > "So, it's more like a smoke test than a real test (personal opinion)." — [blog/three-types-of-evals.md](https://www.aihero.dev/three-types-of-evals) · 2024-11
5. Climb the "Staircase Of Complexity Hell" one step at a time.
  > "The key is to start at the top of the staircase, and work your way down only when you've exhausted all the simpler options." — [blog/how-to-improve-your-llm-powered-app.md](https://www.aihero.dev/how-to-improve-your-llm-powered-app) · 2025-03
6. Start with the smartest model to prove feasibility, then optimise down.
  > "you start with the smartest model to see that it can be done, right? And then you optimize your system so you can include a stupider model in there" — [youtube-appearances/unknown_DCfn1UlSZzs_ai-in-practice-from-cloud-privacy.md](https://www.youtube.com/watch?v=DCfn1UlSZzs&t=340s) · Callstack
- UX, not model quality, differentiates AI apps.
  > "the differentiator between really good AI powered apps and really bad ones is not how good the AI is, it's how good the UX is." — [youtube/2025-06-05_b2ntTXVlGQk_agents-are-dead-long-live-workflows.md](https://www.youtube.com/shorts/b2ntTXVlGQk?t=12s) · 2025-06

## Tensions and evolution

- He moved from building LLM apps to AI-assisted coding, after a long search for his positioning.
  > "AI Engineers create AI-powered apps, while AI-assisted Developers use AI to enhance their development workflow." — [blog/what-is-an-ai-engineer.md](https://www.aihero.dev/what-is-an-ai-engineer) · 2025-03
  > "for the last 18 months I've been trying to figure out my positioning, trying to work out where I fit." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=1008s) · Latent Space
- The constant across both eras: workflows over agents.
  > "The less 'agentic' your application is, the more predictable it becomes." — [blog/workshops__day-8-agents-vs-workflows.md](https://www.aihero.dev/workshops/day-8-agents-vs-workflows) · n.d.

## Related

- [Build your own tools](build-your-own-tools.md)
- [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md)
- [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md)
