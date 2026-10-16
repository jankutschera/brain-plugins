---
type: principle
sources: [youtube-appearances, blog, github, x, youtube]
quotes: 29
first_seen: 2014-07
last_seen: 2026-02
---
# Build to understand

You understand something only once you have built it yourself, from scratch.
  > "when you build something from scratch, you're forced to come to terms with what you don't understand and you don't know that you don't understand it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1795s) · 2025-10

## Evidence

- He repeats Feynman's line that if you can't build it you don't understand it, credits it to Feynman and says he has always believed it.
  > "It's the only way to build. If I can't build it, I don't understand it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1809s) · 2025-10
  > "If I can't build it, I don't understand it. That’s a Feynman quote, I believe. I 100% have always believed this very strongly" — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1809s) · 2025-10
- Reimplementing a thing has been his default way to learn it since at least 2014.
  > "I set out to re-implement t-SNE from scratch since doing so is the best way of learning something that I know of" — [blog/karpathy.github.io/2014__07__02__visualizing-top-tweeps-with-t-sne-in-Javascript.md](https://karpathy.github.io/2014/07/02/visualizing-top-tweeps-with-t-sne-in-Javascript/) · 2014-07
  > "I always like to re-implement all the things." — [x/2021-04.md](https://x.com/karpathy/status/1386086887014555650) · 2021-04
- He learned backpropagation by writing his own JavaScript library.
  > "so I wrote my own library it's called convnet js it was written in Javascript and implements convolutional neural networks that was my way of learning about back propagation" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=836s) · 2017-08
  > "It's just implementing it myself from scratch was the most important" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=829s) · 2017-08
- He rebuilds things even when good tools exist, to learn them.
  > "Just me developing a pure Python from-scratch zero-dependency implementation of Bitcoin for educational purposes" — [github/cryptos/README.md](https://github.com/karpathy/cryptos/blob/e59d4ca9a77da7459e0e792e9a3a82882c41a11d/README.md) · 2021-04
  > "what better way to do this than implement it from scratch?" — [blog/karpathy.github.io/2021__06__21__blockchain.md](https://karpathy.github.io/2021/06/21/blockchain/) · 2021-06
- Frameworks that hide the internals are a trap, because autograd leaks.
  > "it is a leaky abstraction in the sense that you can shoot yourself in the foot if you do not understanding its internals" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=79s) · 2022-10
  > "that's why I don't think it's the case that because pytorch or other Frameworks offer autograd it is okay for us to ignore how it works" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=171s) · 2022-10
- The code is the source of truth; papers and slides are summaries of it.
  > "The code is the source of truth. The papers and everything else, it's a high-level summary." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9366s) · 2022-10
  > "So don't write blog posts, don't do slides, don't do any of that. Build the code, arrange it, get it to work. It's the only way to go." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1825s) · 2025-10
- He picks the slower, more instructive version on purpose.
  > "This will be a lot less efficient than just forwarding a `LayerNorm` module, but it is algorithmically instructive." — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
  > "we want to actually write our own gpt2 class so that we have full understanding of what's happening there we don't want to be working with something like uh the modeling gpt2 Pi because it's just too complicated" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=759s) · 2024-06

## How it shows up

- He tells students to implement backprop themselves before using a framework.
  > "this is why I always urge people also to implement backdrop themselves to get an intuition for how it works, what it's computing and so on." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=2810s) · 2016-09
  > "that you Not work with tensorflow or something else you can work with it once you have written it something Something yourself on the lowest detail" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=847s) · 2017-08
- His courses are from-scratch builds by design.
  > "We are going to build everything end-to-end from basics to a functioning web app similar to ChatGPT, from scratch in Python, C and CUDA, and with minimal computer science prerequisites." — [github/LLM101n/README.md](https://github.com/karpathy/LLM101n/blob/c6de374acd4b57b6fea3b1a1b6e945d58f19cd30/README.md) · 2024-05
  > "This helps build competence and intuition around how neural nets are optimized and sets you up to more confidently innovate on and debug modern neural networks." — [github/nn-zero-to-hero/README.md](https://github.com/karpathy/nn-zero-to-hero/blob/73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde/README.md) · 2024-08
- He strips projects down to the lowest level he can reach.
  > "I am deleting all of this complexity and boiling the LLM training down to its bare essentials, speaking directly to the computer in a very low-level language (C), and with no other library dependencies." — [x/2024-04.md](https://x.com/karpathy/status/1778153659106533806) · 2024-04
- He reproduces old papers to learn what changed.
  > "So I set out to reproduce the paper 1) for fun, but 2) to use the exercise as a case study on the nature of progress in deep learning." — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- Production libraries are for use, not for learning.
  > "unfortunately these libraries are quite complex they're meant to be used not really inspected" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=8529s) · 2022-08

## Tensions and evolution

- Writing backward passes by hand was normal around 2012; by 2022 he kept it only as an exercise, and regrets what was lost.
  > "about 10 years ago in deep learning this was fairly standard and in fact pervasive" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=225s) · 2022-10
  > "today writing your backward pass by hand and manually is not recommended and no one does it except for the purposes of exercise" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=220s) · 2022-10
  > "now everyone just calls lost that backward uh we've lost something" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=239s) · 2022-10
- At Tesla (2017-2022) management pulled him away from the code, which he describes as a loss of touch.
  > "In the beginning, when I joined Tesla, I was writing code and then I was writing less and less code, and I was reading code and then I was reading less and less code." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9331s) · 2022-10
- In 2025 he started treating some code as disposable and let an LLM write parts he did not learn himself, while still hand-distilling GPT into microgpt in 2026.
  > "Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like." — [github/reader3/README.md](https://github.com/karpathy/reader3/blob/64960f99d8d3c2eaaec56c6765b4c1aeae14c80b/README.md) · 2025-11
  > "In nanochat, I vibe coded my own custom highly efficient BPE tokenizer in Rust instead of having to adopt existing libraries or learn Rust at that level." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "a decade-long obsession to simplify LLMs to their bare essentials, and I think it is beautiful" — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02

## Related

- [The core is tiny](core-is-tiny.md)
- [Simplicity is a constraint](simplicity-is-a-constraint.md)
- [Understanding cannot be outsourced](understanding-cannot-be-outsourced.md)
- [Reference then port](../methods/reference-then-port.md)
- [Reproduce landmarks](../methods/reproduce-landmarks.md)
- [Build it live](../methods/build-it-live.md)
- [Learner does the work](../methods/learner-does-the-work.md)
- [Smallest complete version](../methods/smallest-complete-version.md)
