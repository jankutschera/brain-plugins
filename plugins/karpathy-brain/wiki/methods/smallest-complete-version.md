---
type: method
sources: [x, blog, youtube-appearances, youtube, github]
quotes: 34
first_seen: 2015-03
last_seen: 2026-04
---
# Smallest complete version

He teaches at the smallest scale where the concept is still fully present, and ships one minimal, complete, runnable artifact.
  > "Scalar valued autograd has the main concept, everything else is just vectorization, there’s no other deeper algorithmic concept there." — [x/2024-07.md](https://x.com/karpathy/status/1809273572705095977) · 2024-07

## Evidence

- He teaches backprop on scalars because tensors add nothing conceptual.
  > "I think matrix calculus scares everyone and it’s just unnecessary to go there at all." — [x/2024-07.md](https://x.com/karpathy/status/1809273572705095977) · 2024-07
  > "i don't think that it's pedagogically useful to be dealing with tensors from scratch" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=393s) · 2022-08
  > "that's why i fundamentally wrote micrograd because you can understand how things work uh at the fundamental level and then you can speed it up later" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=398s) · 2022-08
- From physics he takes the habit of finding the first-order term and showing it alone.
  > "What is the first-order component? How can I simplify it? How can I have a simplest thing that shows that thing, shows it in action, and then I can tack on the other terms?" — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8268s) · 2025-10
  > "So I love finding these small-order terms and serving them on a platter and discovering them." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8338s) · 2025-10
- His teaching artifacts are single small files that hold the whole algorithm.
  > "This file contains the full algorithmic content of what is needed" — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
  > "if you understand microgpt, you understand the algorithmic essence." — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
  > "the whole thing is 130 lines of Python only using numpy as a dependency" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- Small, but complete: the repo covers the whole pipeline and is short enough to read.
  > "It's trying to be the simplest complete repository that covers the whole pipeline end-to-end of building a ChatGPT clone." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1689s) · 2025-10
  > "And it's very readable. It's 300 lines, so everyone can take a look at it." — [youtube-appearances/unknown_XfpMkf4rD6E_stanford-cs25-v2-i-introduction-to.md](https://www.youtube.com/watch?v=XfpMkf4rD6E&t=1882s) · 2023-01
- Educational code and efficient code are different artifacts, so he splits them.
  > "I realized I have to split up minGPT because I can't properly simultaneously satisfy both 1) educational and 2) efficient in one repo." — [x/2022-12.md](https://x.com/karpathy/status/1607791539258003457) · 2022-12
  > "We also split off the fp32 code base into its own file, which will be pure CUDA kernels only (no cublas or cudnn or etc), and which I think would make a really nice endpoint of a CUDA course." — [x/2024-05.md](https://x.com/karpathy/status/1786461447654125625) · 2024-05
- He simplifies on purpose and tells the viewer when he does.
  > "obviously you would never be doing any of this in production it's really just put down for pedagogical reasons" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=343s) · 2022-08
  > "I did this for educational reasons, but you'd never use this in practice." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=2014s) · 2022-09
- Tiny models and toy problems make the whole system visible.
  > "I think it's interesting to train/study tiny GPTs because it becomes tractable to visualize and get an intuitive sense of the entire dynamical system." — [x/2023-04.md](https://x.com/karpathy/status/1645115622517542913) · 2023-04
  > "We can understand this process in even more detail by condensing the problem to the smallest toy example that displays the problem." — [blog/karpathy.github.io/2015__03__30__breaking-convnets.md](https://karpathy.github.io/2015/03/30/breaking-convnets/) · 2015-03
- The code is written to be read: short, commented, with a usage example.
  > "All of the files above are very short and thoroughly commented, and also contain a usage example on the bottom of the file." — [github/minbpe/README.md](https://github.com/karpathy/minbpe/blob/1acefe89412b20245db5a22d2a02001e547dc602/README.md) · 2024-02
  > "You should not have feel scared to read the code and understand how it works." — [github/minbpe/README.md](https://github.com/karpathy/minbpe/blob/1acefe89412b20245db5a22d2a02001e547dc602/README.md) · 2024-02

## How it shows up

- Minimal does not mean minified; the line count stops where readability would suffer.
  > "The optimization should be: minimize LOC subject to constraint that the code is clean." — [x/2024-04.md](https://x.com/karpathy/status/1783527854741114981) · 2024-04
  > "200 lines of breathable, commented code. It would be easy to go lower if you sacrifice that, I've only chipped away at the conceptual parts." — [x/2026-02.md](https://x.com/karpathy/status/2021998329899757908) · 2026-02
- File headers say what the file is and what was cut.
  > "Full definition of a GPT Language Model, all of it in this single file." — [github/nanoGPT/model.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/model.py) · 2022-12
  > "I removed dropout layers because the models we train here are small," — [github/makemore/makemore.py](https://github.com/karpathy/makemore/blob/988aa59e4d8fefa526d06f3b453ad116258398d4/makemore.py) · 2022-06
  > "This version is the clean, minimal, reference." — [github/llm.c/train_gpt2.c](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/train_gpt2.c) · 2024-04
- He keeps a small model when it still teaches the real thing.
  > "it's going to be a character level language model I still think that is uh very educational with respect to how these systems work" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=218s) · 2023-01
- He skips details that don't help the mental model.
  > "I'm not actually going to dwell too much on the precise kind of like mathematical details of all these Transformations honestly I don't think it's that important" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=1524s) · 2025-02
- He says current models cannot do this distillation for him.
  > "I was trying to simplify uh LLM training to be as simple as possible. The models hate this. They can't do it." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1380s) · 2026-04
  > "if you go to ChatGPT and you say, teach me AI, there's no way. It's going to give you some slop. AI is never going to write nanochat right now." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7499s) · 2025-10

## Tensions and evolution

- minGPT (2020) aimed only to teach. In January 2023 he moved on to nanoGPT, a rewrite that "prioritizes teeth over education" and matches industry benchmarks, though in 2024 he still called nanoGPT educational.
  > "minGPT tries to be small, clean, interpretable and educational" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
  > "from a sole focus on education to something that is still simple and hackable but has teeth (reproduces medium-sized industry benchmarks, accepts some tradeoffs to gain runtime efficiency, etc)." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2024-08
  > "btw nanoGPT is meant for education" — [x/2024-06.md](https://x.com/karpathy/status/1802821261409804611) · 2024-06
  > "that prioritizes teeth over education." — [github/nanoGPT/README.md](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/README.md) · 2022-12
- By 2026 the minimal file had become an end in itself, which he calls art.
  > "This is a brief guide to my new art project" — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
  > "Everything else is just efficiency. I cannot simplify this any further." — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02

## Related

- [The core is tiny](../principles/core-is-tiny.md)
- [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md)
- [Build it live](build-it-live.md)
- [Ramps to knowledge](ramps-to-knowledge.md)
- [Demystify the math](demystify-the-math.md)
- [Playful and accessible](playful-and-accessible.md)
