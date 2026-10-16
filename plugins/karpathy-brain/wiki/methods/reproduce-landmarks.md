---
type: method
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 26
first_seen: 2018-04
last_seen: 2026-09
---
# Reproduce landmarks

He reproduces a known result as his benchmark, explains any gap, then pushes the cost down.
  > "I just love reproducing landmark results for much cheaper, it's so fun!" — [x/2026-01.md](https://x.com/karpathy/status/2009406042267136238) · 2026-01

## Evidence

- He reproduced LeCun's 1989 network and traced the remaining gap to the data.
  > "This code tries to reproduce the 1989 Yann LeCun et al. paper" — [github/lecun1989-repro/README.md](https://github.com/karpathy/lecun1989-repro/blob/8553f52c8d0a51a4bbbabf98e005cef28a22a36b/README.md) · 2022-03
  > "I expect that the majority of this discrepancy comes from the training dataset itself." — [github/lecun1989-repro/README.md](https://github.com/karpathy/lecun1989-repro/blob/8553f52c8d0a51a4bbbabf98e005cef28a22a36b/README.md) · 2022-03
- He uses the reproduction to measure what each kind of progress bought.
  > "I was able to very quickly halve the learning just by time traveling by 33 years." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1561s) · 2025-10
  > "But to get further gains, I had to add a lot more data, I had to 10x the training set, and then I had to add more computational optimizations." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1578s) · 2025-10
  > "simply scaling up the dataset in 1989 would have been an effective way to drive up the performance of the system, at no cost to inference latency" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- He writes down what the paper leaves out, and how he filled the gap, before training.
  > "What is the learning rate? I will run a sweep to determine the best one manually." — [github/lecun1989-repro/README.md](https://github.com/karpathy/lecun1989-repro/blob/8553f52c8d0a51a4bbbabf98e005cef28a22a36b/README.md) · 2022-03
  > "Was any learning rate decay used? Not mentioned, I am assuming no." — [github/lecun1989-repro/README.md](https://github.com/karpathy/lecun1989-repro/blob/8553f52c8d0a51a4bbbabf98e005cef28a22a36b/README.md) · 2022-03
- He says so when he can't match a paper, or when he had to change its method to match.
  > "I was not able to reproduce single-forward-pass gains that the paper alludes to when training with multiple masks, might be doing something wrong." — [github/pytorch-made/README.md](https://github.com/karpathy/pytorch-made/blob/81886ccc8270cdf3a2b32cbbca5c7feab422f907/README.md) · 2018-04
  > "However I had to resort to a data-driven intialization scheme with k-means" — [github/deep-vector-quantization/README.md](https://github.com/karpathy/deep-vector-quantization/blob/c3c026a1ccea369bc892ad6dde5e6d6cd5a508a4/README.md) · 2021-02
- GPT-2 is his fixed target in videos, repos and leaderboards.
  > "today we are going to be continuing our Zero to Hero series and in particular today we are going to reproduce the gpt2 model the 124 million version of it" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=0s) · 2024-06
  > "GPT-2 is just my favorite LLM because it's the first time the LLM stack comes together in a recognizably modern form." — [x/2026-01.md](https://x.com/karpathy/status/2017703360393318587) · 2026-01
  > "Your CORE metric must be greater than GPT-2 0.256525." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09
- Once matched, the goal becomes making it cheap.
  > "you can train your own GPT-2 capability LLM (which cost ~$43,000 to train in 2019) for only $48 (~2 hours of 8XH100 GPU node)" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
  > "This is a 600X cost reduction over 7 years" — [x/2026-01.md](https://x.com/karpathy/status/2017703360393318587) · 2026-01

## How it shows up

- He frames the 1989 work as history and as time travel.
  > "we reproduce what I think may be the earliest real-world application of a neural net trained end-to-end with backprop (LeCun et al. 1989), try improve it with time travel, and reflect." — [x/2022-03.md](https://x.com/karpathy/status/1503394811188973569) · 2022-03
- He runs ablations on the reproduction to find which modern change mattered.
  > "I verified that just naively increasing passes in original setting did not substantially improve results" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- He reports the paper's number when he hits it.
  > "which converges at binary cross entropy loss of `94.5`, as shown in the paper." — [github/pytorch-made/README.md](https://github.com/karpathy/pytorch-made/blob/81886ccc8270cdf3a2b32cbbca5c7feab422f907/README.md) · 2018-04
- He reproduced GPT-2 in C for fun and noted how cheap it could get.
  > "I actually tried to reproduce uh gpt2 for fun as part of this project called lm. C" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=1998s) · 2025-02
  > "it took about one day and about $600 uh but this wasn't even trying too hard I think you could really bring this down to about $100 today" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=2022s) · 2025-02
- He has tried to reproduce capabilities by hand, too, such as writing transformer weights for addition.
  > "I was trying to write out the transformer weights by hand to do addition. Uh but this is kind of like 50% done." — [youtube-appearances/unknown_3OxEpGU1unA_recent-breakthroughs-in-ai-andrej-karpathy.md](https://www.youtube.com/watch?v=3OxEpGU1unA&t=2495s) · 2021-02
- The lesson he draws from these reproductions is that no single factor wins.
  > "All of those, it's almost like no one of them is winning too much. All of them are surprisingly equal." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1600s) · 2025-10

## Tensions and evolution

- The cost of reaching GPT-2 kept falling, and he logged each step. The targets differ: nanoGPT and build-nanogpt reproduce the 124M model, nanochat targets the larger model's CORE score.
  > "currently the file `train.py` reproduces GPT-2 (124M) on OpenWebText, running on a single 8XA100 40GB node in about 4 days of training." — [github/nanoGPT/README.md](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/README.md) · 2022-12
  > "today, reproducing it is a matter of ~1hr and ~$10." — [github/build-nanogpt/README.md](https://github.com/karpathy/build-nanogpt/blob/6104ab1b53920f6e2159749676073ff7d815c1fa/README.md) · 2024-06
  > "Currently this takes ~1.5 hours (down from 3h), but by improving the pretraining stage we can improve this further." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- GPT-2 went from a model judged too risky to release to a teaching benchmark.
  > "GPT-2 (7 years ago): too dangerous to release. GPT-2 (today): new MNIST! :)" — [x/2026-02.md](https://x.com/karpathy/status/2018804068874064198) · 2026-02

## Related

- [Scale and compute](../principles/scale-and-compute.md)
- [Build to understand](../principles/build-to-understand.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Reference then port](reference-then-port.md)
- [Fast feedback loops](fast-feedback-loops.md)
- [Training recipe](training-recipe.md)
