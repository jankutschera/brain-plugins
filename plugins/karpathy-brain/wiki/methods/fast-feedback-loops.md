---
type: method
sources: [github, x, youtube, youtube-appearances]
quotes: 32
first_seen: 2021-01
last_seen: 2026-09
---
# Fast feedback loops

He iterates on a small proxy with one clear metric, fast tooling and napkin math, and checks the result at the target scale.
  > "I like to change something in the code, re-run a d12 (or a d16 etc) and see if it helped, in an iteration loop." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09

## Evidence

- His proxy is a small model that trains in minutes.
  > "For quick experimentation (~5 min pretraining runs) my favorite scale is to train a 12-layer model (GPT-1 sized)" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- In autoresearch a fixed time budget makes runs comparable and sets the pace.
  > "First, this makes experiments directly comparable regardless of what the agent changes (model size, batch size, architecture, etc)." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
  > "This means you can expect approx 12 experiments/hour and approx 100 experiments while you sleep." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- He picks one metric that stays fair across changes and has little noise.
  > "lower is better, and vocab-size-independent so architectural changes are fairly compared." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
  > "If the dataset is not changed, the `val_bpb` number is a great, smooth metric to track relative performance w.r.t. and has less noise than CORE." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-03
- Because runs are noisy, he repeats them and reports a spread.
  > "I ran this command 7 individual times. Because our training is mildly non-deterministic, we get a spread of CORE scores" — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-03
  > "we are getting a tiny Improvement now but it's not clear if this is statistical significant" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2735s) · 2022-11
- He wants code that compiles and runs at once.
  > "I love the feeling of hitting Enter to launch your program, and it just goes. Direct to useful computation on your problem. No waiting." — [x/2024-04.md](https://x.com/karpathy/status/1778841713605525889) · 2024-04
  > "we have a single file of C there's no dependencies whatsoever it compiles instantly it runs instantly" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=554s) · 2024-10
- He does napkin math first: FLOPs for a model, the real bottleneck for a system.
  > "the napkin math via a different estimation method of FLOPs = 6ND (N is params D is tokens), gives:" — [x/2024-04.md](https://x.com/karpathy/status/1781047292486914189) · 2024-04
  > "So the stat to look at is not FLOPS but the memory bandwidth." — [x/2023-08.md](https://x.com/karpathy/status/1691571869051445433) · 2023-08
  > "great example I think of being aware of um memory hierarchy the fact that flops don't matter uh the entire memory access pattern matters" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=7482s) · 2024-06
- A proxy result only counts if it carries over to other sizes.
  > "So your change must be principled enough that it can easily generalize to other model depths, so that we can sweep out a miniseries." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09
  > "Validate at target scale before shipping." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
- He guards the test split so fast iteration doesn't fool him.
  > "every single time you evaluate your test loss and you learn something from it, you are basically starting to also train on the test split" — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=3357s) · 2022-09

## How it shows up

- He prototypes in a notebook, then moves code into a script and launches jobs.
  > "I usually have jupyter notebook and vs code I develop in Jupiter notebook I paste into vs code and then I kick off experiments" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=3244s) · 2022-11
  > "Usually, you don't do it in line. You launch a bunch of jobs and you wait for them to finish." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=3549s) · 2022-09
- He thinks of research speed as experiment throughput.
  > "success in it is to a large extent proportional to raw experimental throughput - the ability to babysit a large number of experiments at once, staring at plots and tweaking/re-launching what works." — [x/2021-01.md](https://x.com/karpathy/status/1350503355299205120) · 2021-01
  > "you're looking at what is working and what is not working and you're working on this like population level and you're doing all these hyper parameter searches" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=3297s) · 2022-11
- He prefers many cheap approximate steps to few exact ones.
  > "it's much better to have an approximate gradient and just make more steps than it is to evaluate the exact gradient and take fewer steps" — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=2661s) · 2022-09
- His debugging is close to the code: drop into the interpreter, or build with debug symbols.
  > "simply drops you into interpreter, perfect for 95% of debugging" — [x/2023-01.md](https://x.com/karpathy/status/1610822271157022720) · 2023-01
  > "modify it by replacing `-O3` with `-g` so you can step through the code in your favorite IDE (e.g. vscode)." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
- Speed tricks he reaches for: nice numbers and compiling by default.
  > "basically scan your code and look for ugly numbers is roughly theistic" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=7681s) · 2024-06
  > "there's no real good reason for you to not use torch compile in your pie torch I kind of feel like you should be using almost by default" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=6555s) · 2024-06
- At Tesla he moved the slow, expensive work offline, out of the inner loop.
  > "you want to do as much a training time and labeling time as possible" — [youtube-appearances/unknown_g6bOwQdCJrc_cvpr-21-wad-keynote-andrej-karpathy.md](https://www.youtube.com/watch?v=g6bOwQdCJrc&t=1787s) · 2021-06
  > "The nice thing about the annotation is that it is fully offline. You have infinite time" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=4572s) · 2022-10

## Tensions and evolution

- Fast proxies can mislead. Gains seen in targeted tests often vanish in a full run.
  > "The improvement was there for targeted tests (~20%) but washed out completely to noise in an actual training run" — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "small scale experiments alone sometimes make me nervous because the findings don't always always generalize (or gains disappear) to larger scales or longer training horizons" — [x/2024-06.md](https://x.com/karpathy/status/1798920127779660129) · 2024-06
- In a 2022 lecture he guessed by hand and said that is not how real work is done; by 2026 an agent ran the loop overnight.
  > "honestly we're kind of in the dark we have no experimental harness we're just guessing and checking and this whole thing is terrible" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2826s) · 2022-11
  > "this is not representative of typical deep learning workflows" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=3284s) · 2022-11
  > "You wake up in the morning to a log of experiments and (hopefully) a better model." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03

## Related

- [Scale and compute](../principles/scale-and-compute.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Experiment log and delete](experiment-log-and-delete.md)
- [Autoresearch](autoresearch.md)
- [Training recipe](training-recipe.md)
- [Data engine](data-engine.md)
