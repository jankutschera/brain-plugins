---
type: method
sources: [blog, x, youtube-appearances, github]
quotes: 27
first_seen: 2011-04
last_seen: 2025-11
---
# Measure it yourself

He measures things himself instead of trusting reported numbers: he becomes the human baseline on a dataset, keeps his own question sets for models, and runs self-experiments on his own life.
  > "Whenever possible evaluate your own (human) accuracy and compare to it." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04

## Evidence

- In 2011 he hand-labeled CIFAR-10 to find the human accuracy.
  > "Over the weekend I wanted to see what kind of classification accuracy a human would achieve on this dataset." — [blog/karpathy.github.io/2011__04__27__manually-classifying-cifar10.md](https://karpathy.github.io/2011/04/27/manually-classifying-cifar10/) · 2011-04
  > "My classification accuracy ended up at about 94% on 400 images." — [blog/karpathy.github.io/2011__04__27__manually-classifying-cifar10.md](https://karpathy.github.io/2011/04/27/manually-classifying-cifar10/) · 2011-04
- In 2014 he did the same for ImageNet, building his own labeling interface.
  > "In the end I realized that to get anywhere competitively close to GoogLeNet, it was most efficient if I sat down and went through the painfully long training process and the subsequent careful annotation process myself." — [blog/karpathy.github.io/2014__09__02__what-i-learned-from-competing-against-a-convnet-on-imagenet.md](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/) · 2014-09
  > "and so I created this Javascript interface And I was showing myself the images" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=209s) · 2017-08
- Doing the task by hand teaches him where models fail.
  > "After seeing so many images, issues, and ConvNet predictions you start to develop a really good model of the failure modes." — [blog/karpathy.github.io/2014__09__02__what-i-learned-from-competing-against-a-convnet-on-imagenet.md](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/) · 2014-09
  > "I thought it was a just an extremely instructed exercise by itself" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=238s) · 2017-08
- For LLMs he keeps a set of "gotcha" questions that are easy for people and hard for models.
  > "Gotchas are queries that specifically on the easy side for humans but on the hard side for LLMs" — [x/2025-02.md](https://x.com/karpathy/status/1891720635363254772) · 2025-02
- He tells people to judge models by using them, and to rotate between them.
  > "Go talk to the model. Talk to the other models (Ride the LLM Cycle - use a different LLM every day)." — [x/2025-11.md](https://x.com/karpathy/status/1990854771058913347) · 2025-11
- He built an LLM council where models review each other's answers blind.
  > "all models get to see each other's (anonymized) responses and they review and rank them" — [x/2025-11.md](https://x.com/karpathy/status/1992381094667411768) · 2025-11
  > "Under the hood, the LLM identities are anonymized so that the LLM can't play favorites when judging their outputs." — [github/llm-council/README.md](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/README.md) · 2025-11
- He logs his own life to answer questions about it.
  > "I recorded 3 months of my computer activity with new pet project ulogme." — [x/2014-08.md](https://x.com/karpathy/status/496056909808414720) · 2014-08
  > "To validate the energy deficit math I spent 100 days around late 2019 very carefully tracking my daily energy input and output." — [blog/karpathy.github.io/2020__06__11__biohacking-lite.md](https://karpathy.github.io/2020/06/11/biohacking-lite/) · 2020-06
- He compares tools by wearing all of them at once and logging daily.
  > "Results of an experiment where I wore 4 sleep trackers every night for 2 months." — [x/2025-03.md](https://x.com/karpathy/status/1906386327190257963) · 2025-03
  > "I'd log these every day right when I wake up so that I can compare and contrast the numbers and relate them to how I felt that morning." — [blog/karpathy.bearblog.dev/finding-the-best-sleep-tracker.md](https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/) · 2025-03

## How it shows up

- His own baseline gives him a suspicion threshold for other people's results.
  > "So if we get below 1.5% I would be extremely suspicious on imageet. Uh that seems wrong." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=518s) · 2016-09
- When no tool measures what he wants, he writes one.
  > "Nothing like this (by far, actually) exists, so I set out to implement my own solution." — [blog/karpathy.github.io/2014__08__03__quantifying-productivity.md](https://karpathy.github.io/2014/08/03/quantifying-productivity/) · 2014-08
- He toggles habits on and off to see which ones predict the outcome.
  > "I'm still trying out stuff and toggling the bits to find the ones that seem to be predictive." — [x/2025-01.md](https://x.com/karpathy/status/1884374429322600964) · 2025-01
- He goes for the 80/20, not perfect compliance.
  > "I think sticking to it 90% of the time produces 90% of the benefit" — [blog/karpathy.github.io/2020__06__11__biohacking-lite.md](https://karpathy.github.io/2020/06/11/biohacking-lite/) · 2020-06
- His logs tie sleep to the quality of his work.
  > "my sleep scores correlate strongly with the quality of work I am able to do that day" — [blog/karpathy.bearblog.dev/finding-the-best-sleep-tracker.md](https://karpathy.bearblog.dev/finding-the-best-sleep-tracker/) · 2025-03
- He learns a craft like training a classifier: he seeks out bad examples, not only good ones.
  > "What you really want is to also have exposure to a large number of bad papers and one way to get this is by reviewing papers." — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
  > "build a binary classifier in your mind" — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
- He reads a model's character from what it does off the beaten path.
  > "It's in these unintended moments where you are clearly off the hiking trails and somewhere in the generalization jungle that you can best get a sense of model smell." — [x/2025-11.md](https://x.com/karpathy/status/1990855382756164013) · 2025-11

## Tensions and evolution

- His 2011 forecast from his own CIFAR-10 labeling was far off, and he added a note saying so.
  > "My impression from this exercise is that it will be hard to go above 80%" — [blog/karpathy.github.io/2011__04__27__manually-classifying-cifar10.md](https://karpathy.github.io/2011/04/27/manually-classifying-cifar10/) · 2011-04
  > "Obviously this prediction was way off, with state of the art now in 95%" — [blog/karpathy.github.io/2011__04__27__manually-classifying-cifar10.md](https://karpathy.github.io/2011/04/27/manually-classifying-cifar10/) · 2011-04
- Personal measurement has limits. In March 2025 he turned against his own vibe checks of models.
  > "In absence of great comprehensive evals I tried to turn to vibe checks instead, but I now fear they are misleading and there is too much opportunity for confirmation bias, too low sample size, etc., it's just not great." — [x/2025-03.md](https://x.com/karpathy/status/1896266683301659068) · 2025-03
- His council experiment showed models judging each other differently than he did.
  > "But I'm not 100% convinced this aligns with my own qualitative assessment." — [x/2025-11.md](https://x.com/karpathy/status/1992381094667411768) · 2025-11

## Related

- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Look at the data and numbers](look-at-the-data-and-numbers.md)
- [Training recipe](training-recipe.md)
- [Using LLMs day to day](using-llms-day-to-day.md)
- [Deep work and side projects](deep-work-and-side-projects.md)
- [LLMs are ghosts](../principles/llms-are-ghosts.md)
