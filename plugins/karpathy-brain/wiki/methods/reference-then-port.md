---
type: method
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 29
first_seen: 2019-04
last_seen: 2026-03
---
# Reference, then port

He writes a simple reference version first, then ports or speeds it up, and checks that the two give the same numbers.
  > "I wrote the Python reference code personally and from scratch and I am expert there and understand it fully. I then wrote the Rust code against this implementation with tests for equality." — [github/rustbpe/README.md](https://github.com/karpathy/rustbpe/blob/ddf848f6961a0655dc8693742fc338e5682c0d3b/README.md) · 2026-01

## Evidence

- llm.c ships with a test that compares the C code against PyTorch, step by step.
  > "runs a forward pass, compares the logits and loss with the PyTorch reference implementation, then it does 10 iterations of training with Adam and makes sure the losses match PyTorch." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
  > "we've re-established full and exact equality to PyTorch training, giving a lot more confidence in correctness." — [x/2024-06.md](https://x.com/karpathy/status/1798391910870200409) · 2024-06
- In talks he describes the PyTorch code as the yardstick, not the product.
  > "our pytorch code which Now isn't the primary thing we're working with it's only a reference that we check correctness with respect to" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=320s) · 2024-10
  > "they're a bit faster usually over time but they match uh the specification exactly and give the exact same numbers" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=655s) · 2024-10
- He shows the match on screen in his lectures.
  > "the nanog gbt here acts as reference code in pytorch to the C implementation so we're trying to exactly match up the two" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=14207s) · 2024-06
  > "if I Aline up the steps you will see that the losses and Norms that are printed between these two are identical" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=14351s) · 2024-06
- Gradients get the same treatment: check against a numerical estimate or a trusted library.
  > "all Neural Network libraries always compute the analytic gradient, but the correctness of the implementation is verified by comparing it to the numerical gradient" — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
  > "which the tests use as a reference for verifying the correctness of the calculated gradients." — [github/micrograd/README.md](https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md) · 2020-04
  > "there's a test which you'll see basically creates two chunks of code one in micrograd and one in pi torch and we'll make sure that the forward and the backward pass agree identically" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=8318s) · 2022-08
- Inside his own code, the specific, loopy version comes first and the general one must reproduce it.
  > "I like to write a very specific function to what I’m doing right now, get that to work, and then generalize it later making sure that I get the same result." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "I almost always write out the fully loopy version first and only then transform it to vectorized code one loop at a time." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- For math, the reference is a small example worked by hand.
  > "what I find works well for me is you find a specific small example that you then fully write out and then in the process of analyzing how that individual small example works you will understand the broader pattern" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=2598s) · 2022-10
  > "this is where you kind of take out your pen and paper do some back propop" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=367s) · 2024-10
- His advice for learning nanochat: rebuild it next to the reference without copy-paste, because the build order carries what the final repo hides.
  > "You're not allowed to copy-paste, you're allowed to reference, you're not allowed to copy-paste." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1751s) · 2025-10
  > "When you write this code, you don't go from top to bottom, you go from chunks and you grow the chunks, and that information is absent." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1763s) · 2025-10

## How it shows up

- Kernels in llm.c go from simple to fast, and the fastest correct one is copied into the main file.
  > "The comments at the top then document the different versions of this kernel available, usually these are in increasing complexity and decreasing running times." — [github/llm.c/dev/cuda/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/dev/cuda/README.md) · 2024-04
  > "You'll see that this first forwards the reference code on the CPU, then it runs kernel 1 on the GPU, compares the results to check for correctness" — [github/llm.c/dev/cuda/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/dev/cuda/README.md) · 2024-04
- The layernorm walkthrough derives the backward pass by hand and checks it.
  > "So now we can do our own backward pass and see that they match (the errors are tiny)" — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
- He applies it to inference paths and tokenizers too.
  > "which forward the model in both C and Python for 200 steps and check the output against a known good expected output." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
  > "I verified with a unit test that the Engine inference is correct compared to the naive inference of `GPT.generate()`." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-03
  > "We can verify that the `RegexTokenizer` has feature parity with the GPT-4 tokenizer" — [github/minbpe/README.md](https://github.com/karpathy/minbpe/blob/1acefe89412b20245db5a22d2a02001e547dc602/README.md) · 2024-02
- He uses small random values in tests so errors can't hide behind zeros.
  > "by making it small numbers I'm trying to unmask those potential errors in these calculations" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=515s) · 2022-10
- He likes what is left at the end.
  > "you verify the correctness by checking agains PyTorch, you’re left with something very simple, small and imo quite beautiful." — [x/2024-04.md](https://x.com/karpathy/status/1778153659106533806) · 2024-04
- llm.c itself began when a framework blocked a lesson he was preparing.
  > "the entire llm.c project started with me thinking about reproducing GPT-2 for an educational video, getting stuck with some PyTorch things, then rage quitting to just write the whole thing from scratch in C/CUDA." — [x/2024-07.md](https://x.com/karpathy/status/1811467135279104217) · 2024-07
  > "the computation itself the algorithm itself is totally clear in my mind I and for some reason torch compal doesn't let me like use it run it Etc so I felt a little bit powerless" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=228s) · 2024-10

## Tensions and evolution

- Hand-written backward passes were normal about ten years before his 2022 lectures. Now he uses them only as an exercise and a check.
  > "about 10 years ago in deep learning this was fairly standard and in fact pervasive" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=225s) · 2022-10
  > "today writing your backward pass by hand and manually is not recommended and no one does it except for the purposes of exercise" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=220s) · 2022-10
- By 2025 the port could be vibe coded. The reference he wrote and understood is what made that safe.
  > "In nanochat, I vibe coded my own custom highly efficient BPE tokenizer in Rust instead of having to adopt existing libraries or learn Rust at that level." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12

## Related

- [Build to understand](../principles/build-to-understand.md)
- [The core is tiny](../principles/core-is-tiny.md)
- [Neural nets fail silently](../principles/neural-nets-fail-silently.md)
- [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md)
- [Reproduce landmarks](reproduce-landmarks.md)
- [AI-assisted coding](ai-assisted-coding.md)
- [Build it live](build-it-live.md)
