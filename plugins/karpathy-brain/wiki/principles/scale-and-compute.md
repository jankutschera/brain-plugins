---
type: principle
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 29
first_seen: 2015-05
last_seen: 2026-03
---
# Scale and compute

Long-run progress comes mostly from compute, data and infrastructure, scaling is predictable, and the order is: make it work, then make it cheap.
  > "to a first-order approximation the main driver of recent progress is not the algorithms but (similar to Computer Vision) compute/data/infrastructure" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05

## Evidence

- He reads deep learning history as old ideas plus scale.
  > "In Computer Vision, the 2012 AlexNet was mostly a scaled up (deeper and wider) version of 1990’s ConvNets." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
  > "in those 20 years there's been much less improvement in uh in algorithms than all these other three pieces." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=2155s) · 2016-09
- Compute is the upper bound, then and now.
  > "if I was transported to 1989, I would have ultimately become upper-bounded in my ability to further improve the system without a bigger computer" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
  > "I would never bet against compute as the upper bound for achievable intelligence in the long run." — [x/2025-01.md](https://x.com/karpathy/status/1883941452738355376) · 2025-01
- Scaling is smooth and predictable, which makes it a safe bet.
  > "the performance of these large language models in terms of the accuracy of the next word prediction task is a remarkably smooth well behaved and predictable function of only two variables" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=1547s) · 2023-11
  > "fundamentally the scaling kind of offers one guaranteed path to success" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=1659s) · 2023-11
- So you design for a family of models on one compute dial, not for one model.
  > "The correct way to think about LLMs is that you are not optimizing for a single specific model but for a family models controlled by a single dial (the compute you wish to spend) to achieve monotonically better results." — [x/2026-01.md](https://x.com/karpathy/status/2009037707918626874) · 2026-01
- First reach top performance, then cut the cost.
  > "Number 1, achieve your top performance, and Number 2, optimize your performance in that order." — [youtube-appearances/unknown_bZQun8Y4L2A_state-of-gpt-brk216hfs.md](https://www.youtube.com/watch?v=bZQun8Y4L2A&t=2238s) · 2023-05
  > "I would say go after performance first and then you make it cheaper later" — [youtube-appearances/unknown_c3b-JASoPi0_making-ai-accessible-with-andrej-karpathy.md](https://www.youtube.com/watch?v=c3b-JASoPi0&t=1776s) · 2024-03
- He judges every change by wall-clock time to capability, not per-step or microbenchmark wins.
  > "This pass did not find any cheap parameter-golf transfer that clearly improves nanochat on the metric that matters: wall clock time to capability." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-03
  > "Slightly better per-step quality, but slightly slower. Net worse on wall clock." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-03
- Hyperparameters depend on scale, so a small-model win must be checked at the target size.
  > "Hyperparameters are scale-dependent." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "The elaborate fine-tuning that won at d12 actively hurts at d20." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "small scale experiments alone sometimes make me nervous because the findings don't always always generalize (or gains disappear) to larger scales or longer training horizons" — [x/2024-06.md](https://x.com/karpathy/status/1798920127779660129) · 2024-06

## How it shows up

- He summarizes a model by the compute that went into it.
  > "The single number that should summarize your expectations about any LLM is the number of total flops that went into its training." — [x/2024-04.md](https://x.com/karpathy/status/1781047292486914189) · 2024-04
- He runs ideas through a "bitter lesson" check.
  > "Good habit to keep checking ideas on whether they pass the bitter lesson gut check" — [x/2022-04.md](https://x.com/karpathy/status/1509962678319595523) · 2022-04
- He re-runs scaling laws in his own setup instead of trusting published ratios.
  > "I re-ran the scaling laws and, because the models are now very parameter bloated, the optimal ratio has halved from 8 to 4! Way down lower than Chinchilla's 20 at this point." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
- He expects the nets of the far future to look like today's, only bigger.
  > "2055 neural nets are basically the same as 2022 neural nets on the macro level, except bigger." — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- His default is the biggest model the hardware allows.
  > "I use the biggest thing that fits in my GPU." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=4276s) · 2016-09
  > "The winning strategy to obtaining very good models (if you have the compute time) is to always err on making the network larger" — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
- He tracks how fast the cost of a fixed capability falls.
  > "This is a 600X cost reduction over 7 years" — [x/2026-01.md](https://x.com/karpathy/status/2017703360393318587) · 2026-01
  > "today you can reproduce this model in roughly an hour or probably less even and it will cost you about 10 bucks" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=158s) · 2024-06

## Tensions and evolution

- Around 2011 he felt algorithms were the limit. After GPT-3 he saw compute as the limit.
  > "In ~2011, progress in AI felt constrained primarily by algorithms." — [x/2024-05.md](https://x.com/karpathy/status/1795980744436932871) · 2024-05
  > "Today, if you gave me a 10X bigger computer I would know exactly what to do with it, and then I'd ask for more." — [x/2024-05.md](https://x.com/karpathy/status/1795980744436932871) · 2024-05
- Where he places the bottleneck moved: data in 2018, not the architecture by 2024.
  > "what I found kind of shocking was that a huge amount of my time ended up just empirically being spent on the data set and just massaging all the data sets." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=38s) · 2018-08
  > "I don't think that the neural network architecture is like holding us back fundamentally anymore" — [youtube-appearances/unknown_hM_h0UA7upI_no-priors-ep-80-with-andrej.md](https://www.youtube.com/watch?v=hM_h0UA7upI&t=982s) · 2024-09
- By 2025 he softened the bitter lesson into an ideal to aim at, and said no single factor dominates.
  > "I still think the bitter lesson is correct, but I see it more as something platonic to pursue, not necessarily to reach" — [x/2025-10.md](https://x.com/karpathy/status/1973435013875314729) · 2025-10
  > "I do expect that nothing dominates. Everything plus 20%. This is roughly what I've seen." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=3948s) · 2025-10

## Related

- [Data is the program](data-is-the-program.md)
- [Verifiability drives progress](verifiability-drives-progress.md)
- [The core is tiny](core-is-tiny.md)
- [Reproduce landmarks](../methods/reproduce-landmarks.md)
- [Fast feedback loops](../methods/fast-feedback-loops.md)
- [Training recipe](../methods/training-recipe.md)
