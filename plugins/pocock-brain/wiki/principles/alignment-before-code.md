---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2023-03
last_seen: 2026-08
---
# Alignment before code

Misalignment is the main failure mode, so the expensive moment is before any code: reach a shared "design concept" with the agent, and treat plans and specs as by-products of that conversation.
  > "The most common failure mode in software development is misalignment." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)

## Evidence

- He has defined programming as clarifying intent since at least 2023.
  > "that's what programming is it's about turning a poorly defined spec into a well-defined one" — [youtube/2023-03-07_WuHSnvsO6Mg_total-typescript-tour-and-ama.md](https://www.youtube.com/watch?v=WuHSnvsO6Mg&t=935s) · 2023-03
- He borrows Brooks's "design concept": once it is shared, implementation is trivial.
  > "Frederick Brooks calls this the design concept, the design concept that you have with the AI. Once that's clear in your head, then it's trivial for the AI to implement it" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=617s) · Unhandled Exception Podcast
- The agent cannot read your mind, however good the model.
  > "the agent, however good it is, however smart the model is, you know, even mythos, it can't read your mind." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=2244s) · The Pragmatic Engineer
- Wrong output usually means the human had not finished thinking.
  > "The usual cause is that you hadn't fully figured out what you wanted." — [blog/ai-coding-dictionary__design-concept.md](https://www.aihero.dev/ai-coding-dictionary/design-concept) · n.d.
- Planning is about wavelength, not documents.
  > "The whole point of planning is to get on the same wavelength with the LLM, not to generate an asset you don't read" — [x/2026-04.md](https://x.com/mattpocockuk/status/2039806494435074555) · 2026-04
- Better conversations give better output.
  > "if you can increase the quality of the conversation you're having with the agent, you're going to increase the quality of the outputs." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=2154s) · The Pragmatic Engineer
- Alignment is the part that must stay human-in-the-loop.
  > "But planning, this alignment phase, has to be human in the loop. Has to be." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=1621s) · AI Engineer

## How it shows up

- He starts nearly every piece of AI work with a grilling session.
  > "And this is virtually how I start every piece of work with AI." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=964s) · AI Engineer
- He stopped reading the plans the agent writes; he judges alignment from the conversation.
  > "The plan is then just a compacted version of the conversation. I don't need to read it." — [x/2026-02.md](https://x.com/mattpocockuk/status/2020828724740923456) · 2026-02
- He calls specs a projection of decisions, and deletes them after use.
  > "The specs aren't that important. They're just a projection of the decisions made during grilling." — [x/2026-08.md](https://x.com/mattpocockuk/status/2083563195671667176) · 2026-08
- He tells people to explain the why to the agent.
  > "It's always really important when you enter these sessions that you explain the why to the LLM" — [youtube/2026-03-18_hX7yG1KVYhI_building-a-real-feature-with-claude.md](https://www.youtube.com/watch?v=hX7yG1KVYhI&t=346s) · 2026-03
- When talk cannot settle a question, he raises the fidelity with a prototype instead of writing a longer spec.
  > "So, I beg of you, have your discussions at a higher fidelity." — [youtube/2026-07-23_n0VhIVtviC0_don-t-waste-time-on-specs.md](https://www.youtube.com/watch?v=n0VhIVtviC0&t=603s) · 2026-07

## Tensions and evolution

- In April 2025 he described AI-assisted development as spec-heavy; by 2026 he rejected "specs are the new code".
  > "Use AI to plan detailed specs. Pass those specs to another AI to generate the code. Keep an eye on the code and refactor when necessary." — [x/2025-04.md](https://x.com/mattpocockuk/status/1913313872666321018) · 2025-04
  > "I disagreed with it - IMO you need to keep a close watch on the code to avoid slop." — [x/2026-06.md](https://x.com/mattpocockuk/status/2069379106974670888) · 2026-06
- He tried specs-to-code seriously and says it failed.
  > "And I tried this. I really tried it. And it sucks. It doesn't work. Because you need to keep a handle on the code." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=808s) · AI Engineer
- His concision rule for plans died when he stopped reading plans.
  > "when I stopped reading the plans, I stopped needing them to be concise." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=2944s) · AI Engineer
- He dislikes the spec-driven-development label even though his flow produces specs.
  > "I think I have a massive issue with the specdriven development label" — [youtube/2026-08-19_zcLPGC-tvgk_live-uncle-bob-on-software-fundamentals.md](https://www.youtube.com/watch?v=zcLPGC-tvgk&t=2500s) · 2026-08

## Related

- [Grilling](../methods/grilling.md)
- [The main flow](../methods/the-main-flow.md)
- [Prototype to answer a question](../methods/prototype-to-answer-a-question.md)
- [Humans own the strategy](humans-own-the-strategy.md)
- [Communication and shared language](communication-and-shared-language.md)
