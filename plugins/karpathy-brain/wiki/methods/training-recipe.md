---
type: method
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 37
first_seen: 2012-07
last_seen: 2026-04
---
# Training recipe

He trains nets with a fixed recipe: become one with the data, build the skeleton, overfit, regularize, tune, squeeze, and copy a proven setup before getting creative.
  > "it builds from simple to complex and at every step of the way we make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04

## Evidence

- Stage one is reading the data, for hours, before any model code.
  > "I like to spend copious amount of time (measured in units of hours) scanning through thousands of examples, understanding their distribution and looking for patterns." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- The training skeleton gets sanity checks before any real run.
  > "Always use a fixed random seed to guarantee that when you run the code twice you will get the same outcome." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "Verify that your loss starts at the correct loss value." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "Train an input-independent baseline, (e.g. easiest is to just set all your inputs to zero)." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- Overfitting one small batch is the gate. He lists skipping it first among the most common neural net mistakes, and still does it on camera.
  > "Overfit a single batch of only a few examples (e.g. as little as two)." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "most common neural net mistakes: 1) you didn't try to overfit a single batch first." — [x/2018-07.md](https://x.com/karpathy/status/1013244313327681536) · 2018-07
  > "we want to see that we can overfit this single batch we can we can crush this little batch and we can perfectly predict the indices on just this little batch" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=3655s) · 2024-06
- Then grow capacity until it overfits, and regularize back.
  > "first get a model large enough that it can overfit (i.e. focus on training loss) and then regularize it appropriately (give up some training loss to improve the validation loss)" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- "Don't be a hero": copy the closest known-good setup first. He said it in a 2016 lecture, a 2019 essay, and practiced it in 2024.
  > "So my answer here and I've already hinted at this is don't be a hero. Don't go crazy." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=3826s) · 2016-09
  > "I always advise people to simply find the most related paper and copy paste their simplest architecture that achieves good performance." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "for the most part I'm in this video I'm just trying to copy paste the settings that open AI used" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=9264s) · 2024-06
- Try the simple thing before the powerful one.
  > "One should always try a BB gun before reaching for the Bazooka." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
  > "You almost always want to try the linear SVM first and see how that works." — [github/svmjs/README.md](https://github.com/karpathy/svmjs/blob/b75b71289dd81fc909a5b3fb8b1caf20fbe45121/README.md) · 2012-07
  > "we're going to start off with the simplest possible neural network which in the case of language modeling in my opinion is the Byram language model" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1339s) · 2023-01
- Before adding capacity, check that the task needs it. He learned this from three months on video models.
  > "I tried for 3 months pretty hard to squeeze out any juice from that video and the single frame baseline was extremely strong" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=2347s) · 2018-08
  > "I like to do all the intermediates first" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=2486s) · 2018-08
- Tuning means a few knobs, mostly the learning rate, with safe defaults.
  > "3e-4 is a safe choice in most medium-sized applications, but can be too low for small networks, so try to increase it!" — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
  > "I mostly only ever tune these parameters and leave most of the others unchanged." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
  > "FixedLR (+optional warmup) with 1 manual decay of 10X on plateau is a safe strong baseline." — [x/2021-08.md](https://x.com/karpathy/status/1431380525759885313) · 2021-08

## How it shows up

- He develops on a tiny subset and a tiny dataset first.
  > "I'm doing first five just for efficiency while we are developing all the code." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=619s) · 2022-09
  > "for me the best debugging simplest data set that I like to use is the tiny Shakespeare data set" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=2762s) · 2024-06
- In the GPT-2 build, he starts at the target: loading the released weights proves the code is arranged right.
  > "that's going to give us confidence that we can load the open ey model and therefore there's a setting of Weights that exactly is the 124 model" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=784s) · 2024-06
- He initializes from a principle, not from numbers found by trial.
  > "we did not have to introduce any um magic numbers that we got from just looking at histograms and guessing checking we have something that is semi- principled" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=2422s) · 2022-10
- He keeps the learning rate constant until the end, and counts iterations, not epochs.
  > "In my own work I always disable learning rate decays entirely (I use a constant LR) and tune this all the way at the very end." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "are a bug-inducing concept in neural net training and should be avoided in favor of number of iterations." — [x/2022-03.md](https://x.com/karpathy/status/1508437725514510336) · 2022-03
- Batch size: max out the device, then accumulate gradients.
  > "You get there by first maxing out the batch_size to whatever your system allows" — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- His main overfitting signal is the gap between train and val loss.
  > "The most important quantity to keep track of is the difference between your training loss" — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
- The last stage is squeezing: ensembles and long training.
  > "Model ensembles are a pretty much guaranteed way to gain 2% of accuracy on anything." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "One time I accidentally left a model training during the winter break and when I got back in January it was SOTA" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- During long runs he watches vital signs.
  > "You're there carefully monitoring the vital signs of your run: loss spikes, numerical issues, throughput, gradient norms, policy entropy, etc." — [x/2024-03.md](https://x.com/karpathy/status/1765424847705047247) · 2024-03

## Tensions and evolution

- Training your own net went from core craft (2019) to mostly outdated by fine-tuning (2022) to "pull the lever" fine-tuning frameworks (2026).
  > "You’re now ready to read a lot of papers, try a large number of experiments, and get your SOTA results." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "the whole setting of training a neural network from scratch on some target task (like digit recognition) is quickly becoming outdated due to finetuning" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
  > "If you have huge amount of diverse data sets of RL environments, etc., uh you can use your favorite fine-tuning framework and um and uh pull the lever and get something that actually uh works pretty well." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=878s) · 2026-04
- In 2019 the recipe warned against unsupervised pretraining outside NLP. By 2025 he called pretraining "our crappy evolution".
  > "Do not get over-excited about unsupervised pretraining." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "TLDR: Pretraining is our crappy evolution." — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
- He admits when his own lecture process falls short of the recipe.
  > "Obviously, this is janky and not exactly how you would train it in production, but this is roughly what you're going through." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=3166s) · 2022-09

## Related

- [Neural nets fail silently](../principles/neural-nets-fail-silently.md)
- [Data is the program](../principles/data-is-the-program.md)
- [Scale and compute](../principles/scale-and-compute.md)
- [Look at the data and numbers](look-at-the-data-and-numbers.md)
- [Fast feedback loops](fast-feedback-loops.md)
- [Reproduce landmarks](reproduce-landmarks.md)
