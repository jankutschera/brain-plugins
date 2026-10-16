---
type: rules
question: "How does he build, and how does he teach?"
date: 2026-10-15
rules: 7
---
# Seven rules: how he builds and how he teaches

## Coverage

Drawn from the principle and method pages on 2026-10-15, after the claim check. A rule is **active** only if he states it in at least two different raw source folders (x, youtube, blog, github, youtube-appearances); every active rule below has quotes from 3 to 5 of them. Rules are instructions someone could follow, ranked by number of sources, how many years they span, and how useful they are as instructions. **Bench** rules have only one source so far; `/brain` refresh promotes them when a second source appears.

## How he builds

### 1. Rebuild it from scratch until you understand it
Don't trust a library, paper or framework you couldn't write yourself; re-implement the core.
  > "when you build something from scratch, you're forced to come to terms with what you don't understand and you don't know that you don't understand it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1795s) · 2025-10
  > "I always like to re-implement all the things." — [x/2021-04.md](https://x.com/karpathy/status/1386086887014555650) · 2021-04
  > "I set out to re-implement t-SNE from scratch since doing so is the best way of learning something that I know of" — [blog/karpathy.github.io/2014__07__02__visualizing-top-tweeps-with-t-sne-in-Javascript.md](https://karpathy.github.io/2014/07/02/visualizing-top-tweeps-with-t-sne-in-Javascript/) · 2014-07
  > "that's why I don't think it's the case that because pytorch or other Frameworks offer autograd it is okay for us to ignore how it works" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=171s) · 2022-10

### 2. Look at the data, and know which number to expect
Before and during training, look at exactly what goes into the model, and predict the numbers before you see them.
  > "The unambiguously correct place to examine your training data is immediately before it feeds into the network." — [x/2020-11.md](https://x.com/karpathy/status/1328547710966743040) · 2020-11
  > "I can’t count the number of times this has saved me and revealed problems in data preprocessing and augmentation." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "I like to spend copious amount of time (measured in units of hours) scanning through thousands of examples, understanding their distribution and looking for patterns." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "in training of neural Nets it is almost always the case that you will have a rough idea for what loss to expect at initialization" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=282s) · 2022-10

### 3. Build up from something you trust, and check every step against it
Start from the simplest working baseline or a reference implementation, overfit one batch, and add one thing at a time while the numbers still match.
  > "most common neural net mistakes: 1) you didn't try to overfit a single batch first." — [x/2018-07.md](https://x.com/karpathy/status/1013244313327681536) · 2018-07
  > "I like to write a very specific function to what I’m doing right now, get that to work, and then generalize it later making sure that I get the same result." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "if I Aline up the steps you will see that the losses and Norms that are printed between these two are identical" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=14351s) · 2024-06
  > "they're a bit faster usually over time but they match uh the specification exactly and give the exact same numbers" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=655s) · 2024-10
  > "You'll see that this first forwards the reference code on the CPU, then it runs kernel 1 on the GPU, compares the results to check for correctness" — [github/llm.c/dev/cuda/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/dev/cuda/README.md) · 2024-04

### 4. Make complexity earn its place
Simplicity is a constraint, not a preference: reject or delete what doesn't pay for itself.
  > "All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
  > "Classical software engineering would have you believe that dependencies are good (we're building pyramids from bricks), but imo this has to be re-evaluated" — [x/2026-03.md](https://x.com/karpathy/status/2036487306585268612) · 2026-03
  > "It's a crutch, it's a distraction, it causes entropy, and it diffuses the team, it dilutes the team and you're not focusing on what's actually necessary" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5656s) · 2022-10
  > "it's just like it's it's too much complexity for not enough gain at this point" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=972s) · 2024-10

### 5. Keep the AI on a short leash, and keep the understanding
Ask for one small concrete change at a time, verify it yourself, and stay responsible for code you didn't type.
  > "Describe the next single, concrete incremental change we're trying to implement. Don't ask for code, ask for a few high-level approaches, pros/cons." — [x/2025-04.md](https://x.com/karpathy/status/1915581920022585597) · 2025-04
  > "in my own work, I'm always scared to get way too big diffs. I always go in small incremental chunks." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=1435s) · 2025-06
  > "work with them as tools and be ultimately respons responsible for the you know product of your work" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11368s) · 2025-02
  > "When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09

The leash got longer in December 2025, when agents started writing most of his code: he now hands them success criteria instead of instructions.
  > "I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
  > "Don't tell it what to do, give it success criteria and watch it go." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01

## How he teaches

### 6. Build it live, from an empty file, as the smallest complete version
Teach by writing the code in front of the learner, at the smallest scale where the whole idea is still present.
  > "Let's build GPT: from scratch, in code, spelled out." — [x/2023-01.md](https://x.com/karpathy/status/1615398117683388417) · 2023-01
  > "I would like to basically uh write this repository from scratch so we're going to begin with an empty file and we're we're going to define a Transformer piece by piece" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=411s) · 2023-01
  > "The git commits were specifically kept step by step and clean so that one can easily walk through the git commit history to see it built slowly." — [github/build-nanogpt/README.md](https://github.com/karpathy/build-nanogpt/blob/6104ab1b53920f6e2159749676073ff7d815c1fa/README.md) · 2024-06
  > "It's not mathematical symbols, et cetera. The source of truth is the code. It's not slides, it's just like let's build it." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9700s) · 2022-10
  > "Scalar valued autograd has the main concept, everything else is just vectorization, there’s no other deeper algorithmic concept there." — [x/2024-07.md](https://x.com/karpathy/status/1809273572705095977) · 2024-07
  > "if you understand microgpt, you understand the algorithmic essence." — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02

### 7. Build the ramp, then make the learner climb it
Order the material so each step needs only the previous one, and give learners exercises that make them do the step themselves.
  > "TLDR: Step 1 build the thing. Step 2 build the ramp." — [x/2024-02.md](https://x.com/karpathy/status/1760388761349927356) · 2024-02
  > "In my mind, education is the very difficult technical process of building ramps to knowledge." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7401s) · 2025-10
  > "We implement a bigram character-level language model, which we will further complexify in followup videos into a modern Transformer language model, like GPT." — [github/nn-zero-to-hero/README.md](https://github.com/karpathy/nn-zero-to-hero/blob/73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde/README.md) · 2024-08
  > "this is the exercise and maybe pause the video here and see if you can figure it out yourself as to what we should put here" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=5655s) · 2022-08
  > "The students had to implement the forward and the backward pass of each layer in raw numpy." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12

## Bench

- Hire by watching someone build a big project.
  > "I would say that hiring have to has to look like give me a really big project and see someone implement that big project." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1126s) · 2026-04
- Manage people like compute: know which work is serial and which parallel.
  > "A good manager will understand the computational geometry of the project at hand and know when to delegate parts of it on the CPU or on the GPU." — [x/2024-04.md](https://x.com/karpathy/status/1780684098773876941) · 2024-04
- Keep labeling rules consistent and known to every labeler.
  > "Whatever you do decide uh you have to be consistent and you have to make sure that everyone knows" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=439s) · 2018-08
- Assume AI at home; grade in class.
  > "the majority of grading has to shift to in-class work (instead of at-home assignments), in settings where teachers can physically monitor students." — [x/2025-11.md](https://x.com/karpathy/status/1993010584175141038) · 2025-11

## Related

- [hot.md](hot.md) · [index.md](index.md) · [principles/build-to-understand.md](principles/build-to-understand.md) · [methods/training-recipe.md](methods/training-recipe.md) · [methods/ai-assisted-coding.md](methods/ai-assisted-coding.md) · [methods/ramps-to-knowledge.md](methods/ramps-to-knowledge.md)
