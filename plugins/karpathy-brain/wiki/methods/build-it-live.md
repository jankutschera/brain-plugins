---
type: method
sources: [x, youtube, github, youtube-appearances, blog]
quotes: 24
first_seen: 2014-07
last_seen: 2026-03
---
# Build it live

He teaches by building from an empty file, spelled out in code and not on slides, with a clean commit history to follow.
  > "Let's build GPT: from scratch, in code, spelled out." — [x/2023-01.md](https://x.com/karpathy/status/1615398117683388417) · 2023-01

## Evidence

- His lectures open on a blank notebook or an empty file and end with a working system.
  > "we are going to start with a blank jupiter notebook and by the end of this lecture we will define and train in neural net and you'll get to see everything that goes on under the hood" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=8s) · 2022-08
  > "I would like to basically uh write this repository from scratch so we're going to begin with an empty file and we're we're going to define a Transformer piece by piece" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=411s) · 2023-01
- He spells every step out, slowly, together with the viewer.
  > "just like with micrograd, I'm going to build it out step-by-step and I'm going to spell everything out. So, we're going to build it out slowly and together." — [youtube/2022-10-09_PaCmpygFfXo_the-spelled-out-intro-to-language.md](https://www.youtube.com/watch?v=PaCmpygFfXo&t=12s) · 2022-09
- The commit history is part of the lesson.
  > "The git commits were specifically kept step by step and clean so that one can easily walk through the git commit history to see it built slowly." — [github/build-nanogpt/README.md](https://github.com/karpathy/build-nanogpt/blob/6104ab1b53920f6e2159749676073ff7d815c1fa/README.md) · 2024-06
  > "The associated GitHub repo contains the full commit history so you can step through all of the code changes in the video, step by step." — [x/2024-06.md](https://x.com/karpathy/status/1799949853289804266) · 2024-06
- Releasing the code alone was not enough; walking through it was the point of the video.
  > "at the time i only uploaded the source code and you'd have to go in by yourself and really figure out how it works so in this lecture i will take you through it step by step" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=30s) · 2022-08
- The format came out of years of looking for the best explanation.
  > "This is the culmination of about 8 years of obsessing about the best way to explain neural nets and backprop." — [x/2022-08.md](https://x.com/karpathy/status/1559672719414681601) · 2022-08
- He teaches in code even in a slide lecture, and asks people to step through it.
  > "So I wrote like some simple Python-- I wrote this in Python basically to create one round of communication of using attention as the message passing scheme." — [youtube-appearances/unknown_XfpMkf4rD6E_stanford-cs25-v2-i-introduction-to.md](https://www.youtube.com/watch?v=XfpMkf4rD6E&t=1412s) · 2023-01
  > "So I invite you to step through it later and convince yourself that this is actually doing the right thing." — [youtube-appearances/unknown_XfpMkf4rD6E_stanford-cs25-v2-i-introduction-to.md](https://www.youtube.com/watch?v=XfpMkf4rD6E&t=2414s) · 2023-01
  > "It's not mathematical symbols, et cetera. The source of truth is the code. It's not slides, it's just like let's build it." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9700s) · 2022-10
- He thinks in code more easily than in prose, and assumes many readers do too.
  > "if you’re like me, reading code can be much easier than reading text descriptions" — [blog/karpathy.github.io/2014__07__02__visualizing-top-tweeps-with-t-sne-in-Javascript.md](https://karpathy.github.io/2014/07/02/visualizing-top-tweeps-with-t-sne-in-Javascript/) · 2014-07

## How it shows up

1. Do it by hand first, then codify the pattern once it is clear.
  > "doing the back propagation manually is obviously ridiculous so we are now going to put an end to this suffering" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=4141s) · 2022-08
  > "let's go up to the value object and we're going to start codifying what we've seen in the examples below" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=4158s) · 2022-08
2. Rebuild the library you will use, then "unlock" it.
  > "the API that I've developed here is identical to the API that pytorch uses" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6747s) · 2022-10
  > "I think going forward I will probably have considered us having unlocked um torch.nn" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=3128s) · 2022-11
3. Each lecture rebuilds one real component of a real system.
  > "In this lecture we build from scratch the Tokenizer used in the GPT series from OpenAI." — [x/2024-02.md](https://x.com/karpathy/status/1759996549109776702) · 2024-02
  > "we start with empty file and end up with a GPT-2 (124M) model" — [x/2024-06.md](https://x.com/karpathy/status/1799949853289804266) · 2024-06
4. The code he writes while preparing becomes a public repo that people can hack.
  > "in the process of developing this lecture I've done that and I published the code under this repository MBP" — [youtube/2024-10-09_zduSFxRajkE_let-s-build-the-gpt-tokenizer.md](https://www.youtube.com/watch?v=zduSFxRajkE&t=5131s) · 2024-02
  > "Publishing here as a Github repo so people can easily hack it, walk through the `git log` history of it, etc." — [github/ng-video-lecture/README.md](https://github.com/karpathy/ng-video-lecture/blob/52201428ed7b46804849dea0b3ccf0de9df1a5c3/README.md) · 2023-01
5. He tells learners to build too, and then write it up.
  > "Of course you’ll learn much more by doing than by reading" — [blog/karpathy.github.io/2015__10__25__selfie.md](https://karpathy.github.io/2015/10/25/selfie/) · 2015-10
  > "in which case I warmly recommend that you not only do but also write about it, and post it places for all of us to read" — [blog/karpathy.github.io/2015__10__25__selfie.md](https://karpathy.github.io/2015/10/25/selfie/) · 2015-10

## Tensions and evolution

- micrograd shipped in 2020 as bare code; the 2022 lecture was his fix for that.
  > "micrograd is this library that i released on github about two years ago" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=26s) · 2022-08
- In 2026 he says he now explains things to agents rather than to people directly.
  > "I'm not explaining to people anymore. I'm explaining it to agents." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3789s) · 2026-03

## Related

- [Build to understand](../principles/build-to-understand.md)
- [Smallest complete version](smallest-complete-version.md)
- [Ramps to knowledge](ramps-to-knowledge.md)
- [Learner does the work](learner-does-the-work.md)
- [Show the mess](show-the-mess.md)
- [Reference then port](reference-then-port.md)
- [Education with AI](education-with-ai.md)
