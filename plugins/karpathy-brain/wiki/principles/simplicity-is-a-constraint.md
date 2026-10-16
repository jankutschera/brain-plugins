---
type: principle
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 37
first_seen: 2014-07
last_seen: 2026-09
---
# Simplicity is a constraint

Simplicity, readability and few dependencies are hard constraints, and any added complexity has to earn its place.
  > "All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03

## Evidence

- He states it as a rule for contributions, and he enforces it.
  > "as a constraint, I want to keep the mainline `llm.c` in the root folder simple and readable." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
  > "I may reject the PR because the complexity is not worth it." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
  > "I've actually rejected a lot of PRS because of that because the code starts to get crazy and I think that decreases the amount of people that can be on board in the project" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=1051s) · 2024-10
- Speed is welcome, but not at the cost of readability.
  > "This repo still cares about efficiency, but not at the cost of simplicity, readability or portability." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- For him, accessible means low cognitive load, not only low cost. So he avoids frameworks and config systems.
  > "Accessibility is about overall cost but also about cognitive complexity" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
  > "there are no giant configuration objects, model factories, or if-then-else monsters in the code base." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- Dependencies count as a cost, and abstractions exist because humans have limits.
  > "LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
  > "software abstractions like Python/PyTorch and everything else really exist only because humans are finite in knowledge, IQ and attention" — [x/2024-10.md](https://x.com/karpathy/status/1841536804073439268) · 2024-10
  > "Classical software engineering would have you believe that dependencies are good (we're building pyramids from bricks), but imo this has to be re-evaluated" — [x/2026-03.md](https://x.com/karpathy/status/2036487306585268612) · 2026-03
- He distrusts abstractions he can't see into, and replaces them with explicit code.
  > "it silently decides which ops run in which precision via internal allowlists." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-03
  > "By making precision explicit, we gain fine-grained control (e.g. can experiment with fp32 norms) and eliminate an unnecessary layer of abstraction." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-03
  > "I just don't really love using that code because honestly it's like five lines of code and I fully understand what's happening inside these lines so I don't love to use abstractions where they're kind of in screwable" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=8577s) · 2024-06
- He writes a reference people fork, not a platform that covers every case.
  > "I expect most applications will wish to create a fork of this repo and hack it to their specific needs and deployment platforms." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
  > "Build a eukaryotic monorepo backbone if you have to, but maximize bacterial DNA." — [x/2025-07.md](https://x.com/karpathy/status/1941616674094170287) · 2025-07
- The rule reaches beyond code. At Tesla he applied it to sensors and to HD maps.
  > "if once you consider the full cost of a sensor, it actually is potentially a liability and you need to be really sure that it's giving you extremely useful information." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5375s) · 2022-10
  > "It's a crutch, it's a distraction, it causes entropy, and it diffuses the team, it dilutes the team and you're not focusing on what's actually necessary" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5656s) · 2022-10

## How it shows up

- His code comments complain about configuration machinery, even his own.
  > "Poor Man's Configurator. Probably a terrible idea." — [github/nanoGPT/configurator.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/configurator.py) · 2022-12
  > "I know people are not going to love this, I just really dislike configuration complexity and having to prepend config. to every single variable." — [github/nanoGPT/configurator.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/configurator.py) · 2022-12
- In nanochat, one setting decides the rest.
  > "This single integer automatically determines all other hyperparameters" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- Complexity is allowed in a scratch folder, not in the main files.
  > "I will be a lot more sensitive to complexity in the root folder of the project, which contains the main / default files of the project." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
- Leaderboard records are judged on aesthetics as well as speed.
  > "In addition to raw gains, there are some qualitative and aesthetic considerations that go into whether your improvement is merged." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09
- In llm.c he refused even a tensor abstraction.
  > "I just want to keep things simple I don't want to create a tensor abstraction I don't want to create any abstraction really it's just float arrays and operations on float arrays" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=418s) · 2024-10
- He wants the tokenizer, an extra stage with its own failure modes, deleted, at least at the input.
  > "tokenization is my least favorite part of working with large language models but unfortunately it is necessary to understand in some detail because it it is fairly hairy gnarly and there's a lot of hidden foot guns" — [youtube/2024-10-09_zduSFxRajkE_let-s-build-the-gpt-tokenizer.md](https://www.youtube.com/watch?v=zduSFxRajkE&t=8s) · 2024-02
  > "The tokenizer must go." — [x/2025-10.md](https://x.com/karpathy/status/1980397031542989305) · 2025-10
  > "delete the tokenizer (at the input)!!" — [x/2025-10.md](https://x.com/karpathy/status/1980397031542989305) · 2025-10
- He praises simple, self-contained tools and attacks bloated ones, in software and outside it.
  > "The calculator is a fully self-contained arithmetic plugin for your brain." — [blog/karpathy.bearblog.dev/i-love-calculator.md](https://karpathy.bearblog.dev/i-love-calculator/) · 2024-09
  > "Wordpress is a bloated, clunky, slow, vulnerable, closed mess." — [blog/karpathy.github.io/2014__07__01__switching-to-jekyll.md](https://karpathy.github.io/2014/07/01/switching-to-jekyll/) · 2014-07

## Tensions and evolution

- Dependencies went from a joke (2014) to a real aversion (2026), now with agents copying out only the needed part.
  > "I don't need some library holding my hand and providing abstractions. Real men command GPUs with their own raw kernel code :D" — [x/2014-08.md](https://x.com/karpathy/status/499070051526668289) · 2014-08
  > "maybe you point your agent at it and rip out the exact part you need." — [x/2026-02.md](https://x.com/karpathy/status/2021633574089416993) · 2026-02
- PyTorch went from loved (2017) to stripped out in llm.c (2024) to "a crappy IR" (2026).
  > "I've been using PyTorch a few months now and I've never felt better." — [x/2017-05.md](https://x.com/karpathy/status/868178954032513024) · 2017-05
  > "In llm.c, all this startup latency is ~gone." — [x/2024-04.md](https://x.com/karpathy/status/1778841713605525889) · 2024-04
  > "everything else is just a matter of compilation and PyTorch etc is kind of a crappy IR" — [x/2026-08.md](https://x.com/karpathy/status/2090479399842054610) · 2026-08
- Simple code had to get "teeth". minGPT (2020) was only for teaching; by 2023 he wanted simple code that also matches industry benchmarks.
  > "minGPT tries to be small, clean, interpretable and educational" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
  > "from a sole focus on education to something that is still simple and hackable but has teeth (reproduces medium-sized industry benchmarks, accepts some tradeoffs to gain runtime efficiency, etc)." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2023-01
- With agents writing his side projects in 2026, he mostly stopped fighting their bloat.
  > "I'm not very happy with the code quality and I think agents bloat abstractions, have poor code aesthetics, are very prone to copy pasting code blocks and it's a mess, but at this point I stopped fighting it too hard and just moved on." — [x/2026-03.md](https://x.com/karpathy/status/2035173492447224237) · 2026-03
  > "it's very bloated and there's a lot of copy-paste and there's awkward abstractions that are brittle and like it works but it's just really gross." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1365s) · 2026-04

## Related

- [The core is tiny](core-is-tiny.md)
- [Openness and ownership](openness-and-ownership.md)
- [Understanding cannot be outsourced](understanding-cannot-be-outsourced.md)
- [Experiment log and delete](../methods/experiment-log-and-delete.md)
- [Smallest complete version](../methods/smallest-complete-version.md)
- [AI-assisted coding](../methods/ai-assisted-coding.md)
