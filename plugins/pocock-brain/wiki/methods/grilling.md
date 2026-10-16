---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 25
first_seen: 2026-01
last_seen: 2026-07
---
# Grilling

Before any code, he has the agent interview him relentlessly down every branch of the design tree until they share one understanding; facts are the agent's job, decisions are his.
  > "Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it." — [github/skills/skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/grilling/SKILL.md)

## Evidence

- He calls the original grill-me prompt his most influential writing.
  > "the most influential four sentences I've ever written." — [youtube/2026-05-14_6BB6exR8Zd8_i-stopped-using-grill-me-for.md](https://www.youtube.com/watch?v=6BB6exR8Zd8&t=4s) · 2026-05
- He starts virtually every piece of AI work this way.
  > "And this is virtually how I start every piece of work with AI." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=964s) · AI Engineer
- It exists because agents fill gaps silently.
  > "The technique exists because agents fill gaps silently." — [blog/ai-coding-dictionary__grilling.md](https://www.aihero.dev/ai-coding-dictionary/grilling) · n.d.
- It counters the agent's "asset rush" toward a plan.
  > "it has a little bit of what I'm going to call an asset rush. It's rushing towards creating an asset. It's like a premature completion." — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=508s) · Unhandled Exception Podcast
- The design tree comes from Brooks; he credits the idea to a Claude Code team member's thread.
  > "The concept of a "design tree" comes from _The Design of Design_ by Frederick P. Brooks." — [blog/5-agent-skills-i-use-every-day.md](https://www.aihero.dev/5-agent-skills-i-use-every-day) · 2026-03
  > "it wasn't an original idea to me. I think I saw it from a Tariq thread who works in claw code" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=455s) · Unhandled Exception Podcast
- He uses it for non-code decisions too.
  > "I've used it for figuring out what course to build next" — [blog/my-grill-me-skill-has-gone-viral.md](https://www.aihero.dev/my-grill-me-skill-has-gone-viral) · 2026-03

## How it shows up

1. Pick the variant: grill-with-docs when a codebase exists (adds a glossary and ADRs), grill-me when it does not.
  > "the rule is when you have a code base, use Grill with Docs. When you don't have a code base, use Grill me." — [youtube/2026-05-14_6BB6exR8Zd8_i-stopped-using-grill-me-for.md](https://www.youtube.com/watch?v=6BB6exR8Zd8&t=860s) · 2026-05
2. Size the work first: small things get aligned afterwards; grilling is for work that fits one session.
  > "Is it a small enough thing that I can align afterwards? Then don't use grill me. Does it fit into a single session? Then use grill me." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4477s) · The Pragmatic Engineer
3. The agent asks the whole frontier each round, numbered, with a recommended answer for each.
  > "Ask the whole frontier in one round: number each question and give your recommended answer." — [github/skills/skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/grilling/SKILL.md)
4. The agent looks facts up itself and waits for the human's decisions.
  > "Finding _facts_ is your job, never the user's." — [github/skills/skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/grilling/SKILL.md)
5. Push back; a session with no pushback was not needed.
  > "A session with no pushback from you is a session you didn't need." — [blog/skills-grill-me.md](https://www.aihero.dev/skills-grill-me) · 2026-04
6. Use the biggest model for grilling, run two sessions in parallel, and dictate the answers.
  > "Another thing people get wrong is that they use too dumb a model for grilling." — [youtube/2026-05-25_UzMNBN6xLLA_9-things-people-get-wrong-with.md](https://www.youtube.com/watch?v=UzMNBN6xLLA&t=520s) · 2026-05
  > "I will tend to run multiple grilling sessions at once, be switching tabs" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=3110s) · Unhandled Exception Podcast
7. Done means the frontier is empty; questions that talk cannot settle go to a prototype.
  > "The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed." — [github/skills/skills/productivity/grilling/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/productivity/grilling/SKILL.md)
  > "there are questions that are grillable, in other words, answerable in a grilling session, and questions that are ungrillable" — [youtube/2026-05-25_UzMNBN6xLLA_9-things-people-get-wrong-with.md](https://www.youtube.com/watch?v=UzMNBN6xLLA&t=156s) · 2026-05

## Tensions and evolution

- Grilling replaced plan mode. In January 2026 every change went through plan mode; by April he had stopped, and the post carries a reversal note.
  > "Every piece of code I write now goes through this loop where I first plan it in plan mode with an AI." — [youtube/2026-01-15_WNx-s-RxVxk_i-was-an-ai-skeptic-then.md](https://www.youtube.com/watch?v=WNx-s-RxVxk&t=22s) · 2026-01
  > "I have also stopped using plan mode It creates a plan FAR too eagerly and usually asks you zero questions en route" — [x/2026-04.md](https://x.com/mattpocockuk/status/2039806494435074555) · 2026-04
  > "Now I just have a conversation with the agent, like I would with a colleague." — [blog/plan-mode-introduction.md](https://www.aihero.dev/plan-mode-introduction) · 2026-01
- Cadence flipped within a month: v1.1 (2026-07) insisted on one question at a time; v1.2 moved to rounds.
  > "asking multiple questions at once is bewildering." — [youtube/2026-07-08_A8mokin_YOs_new-skills-v1-1-brings-wayfinder.md](https://www.youtube.com/watch?v=A8mokin_YOs&t=168s) · 2026-07
  > "No more "one question at a time" - now it asks questions in rounds" — [x/2026-07.md](https://x.com/mattpocockuk/status/2078077849785815465) · 2026-07
  > "doesn't have the failure mode where you just say "I agree" turn after turn." — [x/2026-07.md](https://x.com/mattpocockuk/status/2077385093027340382) · 2026-07
- He kept the old cadence as a supported opt-out (skill doc, 2026-07; supporting evidence).
  > "The opt-out is a supported setting, not a workaround." — [blog/skills-grilling.md](https://www.aihero.dev/skills-grilling) · 2026-07
- In May 2026 he said he "stopped using grill-me for coding" in favour of grill-with-docs.
  > "what is the thinnest layer of documentation I could use to just give the AI a bit more of a leg up." — [youtube/2026-05-14_6BB6exR8Zd8_i-stopped-using-grill-me-for.md](https://www.youtube.com/watch?v=6BB6exR8Zd8&t=210s) · 2026-05

## Related

- [Alignment before code](../principles/alignment-before-code.md)
- [Humans own the strategy](../principles/humans-own-the-strategy.md)
- [The main flow](the-main-flow.md)
- [Prototype to answer a question](prototype-to-answer-a-question.md)
- [Communication and shared language](../principles/communication-and-shared-language.md)
