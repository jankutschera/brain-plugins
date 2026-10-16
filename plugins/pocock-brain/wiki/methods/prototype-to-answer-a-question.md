---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 20
first_seen: 2021-04
last_seen: 2026-08
---
# Prototype to answer a question

When talking cannot settle a question, especially one of taste, he has the agent build throwaway code aimed at exactly that question instead of writing a longer spec.
  > "A prototype is throwaway code that answers a question." — [youtube/2026-07-23_n0VhIVtviC0_don-t-waste-time-on-specs.md](https://www.youtube.com/watch?v=n0VhIVtviC0&t=59s) · 2026-07

## Evidence

- Some questions can only be answered with code.
  > "Some questions really can only be answered by prototyping." — [youtube/2026-07-23_n0VhIVtviC0_don-t-waste-time-on-specs.md](https://www.youtube.com/watch?v=n0VhIVtviC0&t=142s) · 2026-07
- AI has no taste for UI, so he prototypes aggressively before committing.
  > "AI has no taste for UI, prototype extremely aggressively before committing to a PRD" — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02
- Prototyping is how he imposes taste.
  > "Prototyping is really important if you need to impose your taste on the outcome." — [youtube/2026-03-03_Ah9p7v7nJWg_the-7-phases-of-ai-driven.md](https://www.youtube.com/watch?v=Ah9p7v7nJWg&t=169s) · 2026-03
- Replacing plans with prototypes improves output.
  > "The more I replace plans with prototypes, the better the outputs" — [x/2026-05.md](https://x.com/mattpocockuk/status/2052437310302462173) · 2026-05
- Prototypes are cheaper than ever, which answers the "waterfall" critique.
  > "It was always expensive to produce prototypes. Now it's the cheapest that it's ever been." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4576s) · The Pragmatic Engineer
  > "the prototypes are the way that you prevent it from becoming waterfall" — [youtube/2026-07-30_F3lL98Pj90o_wayfinder-nothing-is-too-big-to.md](https://www.youtube.com/watch?v=F3lL98Pj90o&t=503s) · 2026-07
- He sees prototyping as underused.
  > "prototyping I think especially is really underused and really a very important technique for getting good results out of your specs." — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=1445s) · Unhandled Exception Podcast

## How it shows up

1. Name the one question first; a prototype answering the wrong question is waste.
  > "A prototype that answers the wrong question is wasted, however good it looks." — [blog/skills-prototype.md](https://www.aihero.dev/skills-prototype) · 2026-05
2. UI questions: several radically different variants on one route, switchable by a URL param.
  > "Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar." — [github/skills/skills/engineering/prototype/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/prototype/SKILL.md)
  > "Variants must disagree about structure, not colour" — [blog/skills-prototype.md](https://www.aihero.dev/skills-prototype) · 2026-05
3. Logic questions: a pure logic prototype that pushes state through edge cases.
  > "In other words, a pure logic prototype." — [youtube/2026-07-23_n0VhIVtviC0_don-t-waste-time-on-specs.md](https://www.youtube.com/watch?v=n0VhIVtviC0&t=584s) · 2026-07
4. Skip the polish, surface the state after every action.
  > "**Skip the polish.** No tests, no error handling beyond what makes the prototype _runnable_, no abstractions. The point is to learn something fast." — [github/skills/skills/engineering/prototype/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/prototype/SKILL.md)
5. Keep only the validated decision on main.
  > "The main branch keeps only the validated decision." — [github/skills/skills/engineering/prototype/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/prototype/SKILL.md)
- It is his answer to making AFK agents good at frontend.
  > "People often ask me like, \"What's the best way to make AFK agents really good at front end?\" And the answer is prototyping." — [youtube/2026-05-12_DNqsMXH6Eog_new-skills-handoff-prototype-review-and.md](https://www.youtube.com/watch?v=DNqsMXH6Eog&t=367s) · 2026-05

## Tensions and evolution

- Prototype code used to be binned; since 2026 it is kept on a branch.
  > "Not any more. It used to be: build it, keep the answer, bin the code." — [blog/skills-prototype.md](https://www.aihero.dev/skills-prototype) · 2026-05
- Logic prototypes moved from terminal apps (2026-05) to single HTML files (2026-08).
  > "The logic branch now produces a single self-contained file, plain HTML, CSS and JS, no build and no server, instead of a terminal app." — [blog/skills__skills-changelog-v12-wait-what-writing-for-agents-claude-code-plugin-and-more.md](https://www.aihero.dev/skills/skills-changelog-v12-wait-what-writing-for-agents-claude-code-plugin-and-more) · 2026-08
- In 2021 he wanted prototypes that are not disposable; in 2026 he wants them, and specs, thrown away.
  > "The next frontier in product design tools is in making prototypes/designs/sketches that are NOT disposable" — [x/2021-04.md](https://x.com/mattpocockuk/status/1385153436954546177) · 2021-04
  > "The specs my skills create are intended to be deleted immediately - not kept around, or treated as source code." — [x/2026-08.md](https://x.com/mattpocockuk/status/2083563195671667176) · 2026-08
- He credits Shape Up's low-fidelity-first idea, so prototypes come after text, not instead of it.
  > "when you're first starting out, it's often really good to operate at a really low fidelity. In other words, just text." — [youtube-appearances/unknown_LMpMmOWTtVk_matt-pocock-built-the-skills-repo.md](https://www.youtube.com/watch?v=LMpMmOWTtVk&t=183s) · The Next New Thing

## Related

- [Alignment before code](../principles/alignment-before-code.md)
- [Grilling](grilling.md)
- [The main flow](the-main-flow.md)
- [Humans own the strategy](../principles/humans-own-the-strategy.md)
