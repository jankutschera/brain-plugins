---
type: principle
sources: [blog, x, github, youtube-appearances]
quotes: 24
first_seen: 2022-10
last_seen: 2026-04
---
# Build for agents

The main reader of docs, tools and products is now an LLM, so build for the agent.
  > "99.9% of attention is about to be LLM attention, not human attention." — [x/2025-03.md](https://x.com/karpathy/status/1899876370492383450) · 2025-03

## Evidence

- Docs should be one text file meant for an LLM's context window, because users paste them there anyway.
  > "In 2025 the docs should be a single your_project.md text file that is intended to go into the context window of an LLM." — [x/2025-03.md](https://x.com/karpathy/status/1899876370492383450) · 2025-03
  > "Everything you tell the user will be basically right away copy pasted to an LLM, so you might as well talk directly to the LLM." — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
- Instructions that ask a person to click are the wrong interface.
  > "Don't talk to a developer. Don't ask a developer to visit, look, or click. Instruct and empower their LLM." — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
  > "anytime your docs say click this is bad." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=2161s) · 2025-06
  > "LLMs don’t like to click, they like to curl." — [x/2025-04.md](https://x.com/karpathy/status/1914494203696177444) · 2025-04
- A product an LLM cannot script is a product it cannot help with.
  > "If an LLM can't read the underlying representations and manipulate them and all of the related settings via scripting, then it also can't co-pilot your product" — [x/2025-06.md](https://x.com/karpathy/status/1930354382106964079) · 2025-06
  > "All of this work and state is not even accessible or manipulatable by an LLM - how are we supposed to be automating society by 2027 like this?" — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
- He calls human-only docs his favorite pet peeve, on stage at Sequoia Ascent 2026.
  > "They still have docs that are fundamentally written for humans. This is my favorite pet peeve." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1548s) · 2026-04
- Builders should meet the models halfway rather than wait for them to handle human interfaces.
  > "I still think it's very worth u basically meeting LLM halfway" — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=2260s) · 2025-06
- Research and ideas should also be packaged for LLM readers, who then serve them to people.
  > "What does a research paper look like for an LLM instead of a human? It’s definitely not a pdf." — [x/2025-07.md](https://x.com/karpathy/status/1943411187296686448) · 2025-07
  > "it can then target, personalize and serve the idea to its user." — [x/2025-11.md](https://x.com/karpathy/status/1990577951671509438) · 2025-11

## How it shows up

- He publishes his own writing in a form LLMs can read and invites readers to ask a model about it.
  > "These can be useful for both people who may want to just read the summary in text format, but also for LLMs so that my content is legible and available to them." — [blog/karpathy.bearblog.dev/sequoia-ascent-2026.md](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · 2026-04
  > "should you wish to fork the conversation and ask any questions with all of the context" — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
  > "ask your favorite LLM for more information on any of the items" — [blog/karpathy.bearblog.dev/chemical-hygiene.md](https://karpathy.bearblog.dev/chemical-hygiene/) · 2025-12
- His recent gists and repos hand over an idea for the reader's agent to build, not a finished library.
  > "Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you." — [github/_gists/442a6bf555914893e9891c11519de94f/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 2026-04
  > "Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like." — [github/reader3/README.md](https://github.com/karpathy/reader3/blob/64960f99d8d3c2eaaec56c6765b4c1aeae14c80b/README.md) · 2025-11
- He runs his home through an agent that takes plain-language instructions.
  > "Like Dobby controls everything in natural language. It's amazing." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=695s) · 2026-03
- He wants the other direction too: models should answer people in the formats people like.
  > "In the same way, LLMs should speak to us in our favored format - in images, infographics, slides, whiteboards, animations/videos, web apps, etc." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "People actually dislike reading text - it is slow and effortful." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12

## Tensions and evolution

- The push got louder over a year: a docs suggestion in March 2025, then frustration while shipping MenuGen in April, then a slogan in February 2026.
  > "It's 2026. Build. For. Agents." — [x/2026-02.md](https://x.com/karpathy/status/2026360908398862478) · 2026-02
- It changed how he teaches. In the Lex Fridman interview he spent about ten hours per hour of lecture for human viewers. In the Skill Issue episode he said he now explains to agents, while still thinking he explains a little better than they do.
  > "it probably takes me somewhere around 10 hours to create one hour of content." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9649s) · 2022-10
  > "I'm not explaining to people anymore. I'm explaining it to agents." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3789s) · 2026-03
  > "I still think I can probably explain things a little bit better than the agents, but I still feel like the models are improving so rapidly that um I feel like it's a losing battle to some to some extent." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3856s) · 2026-03

## Related

- [Software 2.0 and 3.0](software-2-and-3.md)
- [Demos are not products](demos-are-not-products.md)
- [AI-assisted coding](../methods/ai-assisted-coding.md)
- [Knowledge work](../methods/knowledge-work.md)
- [Education with AI](../methods/education-with-ai.md)
- [Openness and ownership](openness-and-ownership.md)
