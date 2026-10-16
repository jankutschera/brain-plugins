---
type: source
raw: raw/github/
files: 1672
words: 4965048
date_range: 2011-04 – 2026-09
---
# GitHub (karpathy repos and gists)

## Coverage

- **What exists (MANIFEST.md):** github.com/karpathy via `gh repo list` and the gists API. 63 repos and 13 gists listed; 54 repos and all 13 gists cloned shallow (`.git` removed, SHAs in `clones.json`); 9 forks skipped (cpython, examples, lifejs, nn, optim, scriptsbots, simple-amt, sqlitedict, transformers). 1,672 files (370 binary), about 5.0M words of text, of which about 871K are "prose" by file type. No fetch failures.
- **Dates:** repo `createdAt` runs 2011-04 to 2026-03 and last push runs to 2026-09; gists 2015-04 to 2026-04. README and code text is dated by the repo's creation month. Text that is an explicitly later update (for example "Update Nov 2025", deprecation notes) or that describes later events (nanochat README, LOG and LEADERBOARD, the microgpt paragraph in micrograd, the later lecture list in nn-zero-to-hero) uses the last-push month. So a date marks a window, not the exact writing day.
- **Most of the prose count is datasets, not Karpathy's writing:** tinyshakespeare `input.txt` in char-rnn, build-nanogpt and ng-video-lecture (about 200K words each), `taylorswift.txt` in minbpe, the 3.1M-word BLS dump in `jobs`, scholaroctopus data.
- **Read in full:** READMEs and docs of the teaching and LLM repos (nanoGPT, minGPT, micrograd, makemore, char-rnn, llm.c including `doc/layernorm/layernorm.md` and `dev/cuda/README.md`, nanochat including all of `dev/LOG.md` at about 9K words and `dev/LEADERBOARD.md`, autoresearch including `program.md`, minbpe including `exercise.md` and `lecture.md`, llama2.c, nn-zero-to-hero, LLM101n, build-nanogpt, ng-video-lecture, rustbpe); READMEs of the 2025-2026 vibe-coded apps (rendergit, reader3, llm-council, hn-time-capsule, jobs, calorie); READMEs of older projects (lecun1989-repro, cryptos, convnetjs, recurrentjs, reinforcejs, arxiv-sanity, ulogme, neuraltalk, paper-notes and others).
- **Sampled:** code docstrings and comments, by grep for first-person and opinion words, across the teaching repos; file headers of the main training files; gists microgpt.py and llm-wiki.md (full) and the headers of the rest; markdown cells of the nn-zero-to-hero notebooks.
- **Skipped:** datasets, vendored code, the `karpathy.github.io` repo (duplicates the blog), `llm-council/CLAUDE.md` and the gist HELLO.md (written by Claude per the gist description), heavy multi-contributor llm.c CUDA internals, a CSS-only gist, Lua code.
- **Caveat on nanochat `dev/LOG.md`:** written in the first person and published in the karpathy account, but some entries read as if drafted with an LLM assistant. Treat its wording as approved by Karpathy rather than strictly hand-typed.
- **Shape of the account:** browser JavaScript libraries (2012-2015), PhD research code and paper tools (2014-2016), minimal teaching implementations (micrograd, minGPT, makemore, nanoGPT, minbpe, llama2.c, llm.c, nanochat, microgpt, 2020-2026), and small vibe-coded tools and agent experiments (2025-2026). The most-starred repos are autoresearch, nanoGPT, nanochat, LLM101n and llm.c.

## What this source shows about them

- Simplicity is a hard constraint, traded against performance in explicit numbers.
  > "A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
  > "This repo still cares about efficiency, but not at the cost of simplicity, readability or portability." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- Accessibility is defined as low cognitive load, so the code avoids frameworks and configuration machinery.
  > "Accessibility is about overall cost but also about cognitive complexity" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
  > "there are no giant configuration objects, model factories, or if-then-else monsters in the code base." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- The repos keep cutting models down to the lines that carry the idea.
  > "This file is the complete algorithm. Everything else is just efficiency." — [github/_gists/8627fe009c40f57531cb18360106ce95/microgpt.py](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) · 2026-02
- Many projects are from-scratch rebuilds made to learn, even where a better tool exists.
  > "Just me developing a pure Python from-scratch zero-dependency implementation of Bitcoin for educational purposes" — [github/cryptos/README.md](https://github.com/karpathy/cryptos/blob/e59d4ca9a77da7459e0e792e9a3a82882c41a11d/README.md) · 2021-04
- The code is meant to be forked and changed, not used as a platform.
  > "I expect most applications will wish to create a fork of this repo and hack it to their specific needs and deployment platforms." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- Every port is checked against a simpler reference that Karpathy fully understands.
  > "I wrote the Python reference code personally and from scratch and I am expert there and understand it fully. I then wrote the Rust code against this implementation with tests for equality." — [github/rustbpe/README.md](https://github.com/karpathy/rustbpe/blob/ddf848f6961a0655dc8693742fc338e5682c0d3b/README.md) · 2026-01
- Opaque framework behavior gets replaced with explicit code.
  > "it is buried 30 layers deep in the code, behind an inscrutable dynamical dispatcher, in some possibly auto-generated CUDA code" — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
  > "By making precision explicit, we gain fine-grained control (e.g. can experiment with fp32 norms) and eliminate an unnecessary layer of abstraction." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- Changes are judged end to end on the metric that matters, not on per-step or microbenchmark gains.
  > "This pass did not find any cheap parameter-golf transfer that clearly improves nanochat on the metric that matters: wall clock time to capability." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- Results from small proxies are checked again at target scale.
  > "The elaborate fine-tuning that won at d12 actively hurts at d20." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
  > "Validate at target scale before shipping." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- Failed experiments are logged as carefully as wins.
  > "This is the fifth failed attempt to beat pure FineWeb-EDU on CORE score." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- Code that does not earn its place is deleted, not left behind a flag.
  > "Deleted all grad-clip code paths. The code naturally produces well-behaved gradients." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- The commit history is part of the lesson.
  > "The git commits were specifically kept step by step and clean so that one can easily walk through the git commit history to see it built slowly." — [github/build-nanogpt/README.md](https://github.com/karpathy/build-nanogpt/blob/6104ab1b53920f6e2159749676073ff7d815c1fa/README.md) · 2024-06
- The lecture repos ask learners to do the work and use the video as the answer key.
  > "I recommend you work through the exercise yourself but work with it in tandem and whenever you are stuck unpause the video and see me give away the answer. This video is not super intended to be simply watched." — [github/nn-zero-to-hero/README.md](https://github.com/karpathy/nn-zero-to-hero/blob/73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde/README.md) · 2024-08
- Gaps and mistakes are named in the READMEs.
  > "sadly I did not go too much into model initialization in the video lecture, but it is quite important for good performance." — [github/ng-video-lecture/README.md](https://github.com/karpathy/ng-video-lecture/blob/52201428ed7b46804849dea0b3ccf0de9df1a5c3/README.md) · 2023-01
- Old projects get deprecated when better code appears, including code by other people.
  > "In other words, torch-rnn should be the default char-rnn implemention to use now instead of the one in this code base." — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2023-10
  > "nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity." — [github/nanoGPT/README.md](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/README.md) · 2025-11
- The teaching code moved from education only (2020) to education that also matches industry benchmarks.
  > "minGPT tries to be small, clean, interpretable and educational" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
  > "from a sole focus on education to something that is still simple and hackable but has teeth (reproduces medium-sized industry benchmarks, accepts some tradeoffs to gain runtime efficiency, etc)." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2024-08
- By 2025 code is treated as cheap and disposable: share the idea, let an LLM do the rest.
  > "Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like." — [github/reader3/README.md](https://github.com/karpathy/reader3/blob/64960f99d8d3c2eaaec56c6765b4c1aeae14c80b/README.md) · 2025-11
  > "The document's only job is to communicate the pattern. Your LLM can figure out the rest." — [github/_gists/442a6bf555914893e9891c11519de94f/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 2026-04
- In 2026 the human moves up a level: the researcher edits the instructions, the agent edits the code.
  > "you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- Contributors are still expected to understand and disclose code an LLM wrote.
  > "When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09

## Notable pieces

- **micrograd (2020-04).** A scalar autograd engine and neural net library, small enough to read in one sitting.
  > "Both are tiny, with about 100 and 50 lines of code respectively." — [github/micrograd/README.md](https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md) · 2020-04
- **minGPT (2020-08).** The first minimal GPT.
  > "GPT is not a complicated model and this implementation is appropriately about 300 lines of code" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
- **nanoGPT `configurator.py` (2022-12).** A short file that shows the dislike of configuration systems.
  > "Poor Man's Configurator. Probably a terrible idea." — [github/nanoGPT/configurator.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/configurator.py) · 2022-12
  > "I know people are not going to love this, I just really dislike configuration complexity and having to prepend config. to every single variable." — [github/nanoGPT/configurator.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/configurator.py) · 2022-12
- **llama2.c README (2023-07).** The clearest statement of what a Karpathy repo refuses to be.
  > "It shouldn't be full-featured. It shouldn't take 100 different options or settings. It shouldn't be the most efficient." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- **llm.c README (2024-04).** GPT-2 training in raw C and CUDA, against a PyTorch reference.
  > "LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
- **llm.c `doc/layernorm/layernorm.md` (2024-04).** A worked tutorial on one layer, down to memory offsets.
  > "What are Tensors? They are 1) a 1D block of memory called Storage that holds the raw data, and 2) a View over that storage that holds its shape." — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
- **minbpe `lecture.md` (2024-02).** Opens the tokenizer lesson with LLM failures traced back to tokenization.
  > "Tokenization is at the heart of a lot of weirdness in LLMs and I would advise that you do not brush it off." — [github/minbpe/lecture.md](https://github.com/karpathy/minbpe/blob/1acefe89412b20245db5a22d2a02001e547dc602/lecture.md) · 2024-02
- **lecun1989-repro (2022-03).** A reproduction of the oldest real-world backprop network.
  > "To my knowledge this is the earliest real-world application of a neural net trained with backpropagation (now 33 years ago)." — [github/lecun1989-repro/README.md](https://github.com/karpathy/lecun1989-repro/blob/8553f52c8d0a51a4bbbabf98e005cef28a22a36b/README.md) · 2022-03
- **nanochat README (2026-09).** The full ChatGPT-style stack in one repo, with the cost of GPT-2 capability tracked.
  > "you can train your own GPT-2 capability LLM (which cost ~$43,000 to train in 2019) for only $48 (~2 hours of 8XH100 GPU node)" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- **nanochat `dev/LOG.md` (2026-09).** About 9K words of experiments, most of them negative, each with its effect on the metric.
  > "A running summary documenting some experiments and findings." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
- **autoresearch (2026-03).** The most-starred repo: an agent tunes nanochat's training code overnight against a fixed metric.
  > "You wake up in the morning to a log of experiments and (hopefully) a better model." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
  > "do NOT pause to ask the human if you should continue." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- **llm-wiki gist (2026-04).** The pattern this wiki is built on.
  > "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." — [github/_gists/442a6bf555914893e9891c11519de94f/llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 2026-04
- **microgpt gist (2026-02).** A complete GPT in plain Python, with comments that read like a story.
  > "Let there be Autograd to recursively apply the chain rule through a computation graph" — [github/_gists/8627fe009c40f57531cb18360106ce95/microgpt.py](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) · 2026-02
- **The vibe-coded tools of 2025-2026** (rendergit, llm-council, hn-time-capsule, reader3, jobs) are shared as-is and labeled as LLM-written.
  > "99% of this repo was vibe coded in a few hours with Opus 4.5." — [github/hn-time-capsule/README.md](https://github.com/karpathy/hn-time-capsule/blob/ca02ebb4de5e953bf1629689abd1f82b454b6905/README.md) · 2025-12
  > "I'm not going to support it in any way, it's provided here as is for other people's inspiration and I don't intend to improve it." — [github/llm-council/README.md](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/README.md) · 2025-11
- **ConvNetJS (2014-01).** The early browser-demo era of teaching.
  > "ConvNetJS is a Javascript implementation of Neural networks, together with nice browser-based demos." — [github/convnetjs/README.md](https://github.com/karpathy/convnetjs/blob/4c3358a315b4d71f31a0d532eb5d1700e9e592ee/README.md) · 2014-01
- **ulogme (2014-05).** One of many small tools built to measure Karpathy's own life.
  > "How productive were you today? How much code have you written? Where did your time go?" — [github/ulogme/README.md](https://github.com/karpathy/ulogme/blob/416163e9c2399cc0f2f271630ccc6e15fe63a9fd/README.md) · 2014-05

## Related

- Sources: [X](x.md) · [YouTube channel](youtube.md) · [Blogs](blog.md) · [YouTube appearances](youtube-appearances.md)
- Principles: [Build to understand](../principles/build-to-understand.md) · [The core is tiny](../principles/core-is-tiny.md) · [Neural nets fail silently](../principles/neural-nets-fail-silently.md) · [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md) · [Scale and compute](../principles/scale-and-compute.md) · [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md) · [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md) · [Openness and ownership](../principles/openness-and-ownership.md)
- Methods: [Training recipe](../methods/training-recipe.md) · [Reference then port](../methods/reference-then-port.md) · [Reproduce landmarks](../methods/reproduce-landmarks.md) · [Fast feedback loops](../methods/fast-feedback-loops.md) · [Experiment log and delete](../methods/experiment-log-and-delete.md) · [AI-assisted coding](../methods/ai-assisted-coding.md) · [Autoresearch](../methods/autoresearch.md) · [Knowledge work](../methods/knowledge-work.md) · [Deep work and side projects](../methods/deep-work-and-side-projects.md) · [Build it live](../methods/build-it-live.md) · [Smallest complete version](../methods/smallest-complete-version.md) · [Ramps to knowledge](../methods/ramps-to-knowledge.md) · [Demystify the math](../methods/demystify-the-math.md) · [Learner does the work](../methods/learner-does-the-work.md) · [Show the mess](../methods/show-the-mess.md) · [Playful and accessible](../methods/playful-and-accessible.md)
