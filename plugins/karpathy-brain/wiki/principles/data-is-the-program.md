---
type: principle
sources: [blog, x, youtube, youtube-appearances]
quotes: 30
first_seen: 2016-09
last_seen: 2025-10
---
# The data is the program

In Software 2.0 the dataset is the program, so the data and the loop that improves it matter more than the architecture.
  > "So here the source code are the data sets. The compilation is the training of the neural network and your binary is the final neural net, the weights." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=2576s) · 2021-09

## Evidence

- In 2017 he described most Software 2.0 development as dataset work. A failure gets fixed with more examples, not more code.
  > "takes the form of curating, growing, massaging and cleaning labeled datasets" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "when the network fails in some hard or rare cases, we do not fix those predictions by writing code, but by including more labeled examples of those cases" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
- At Tesla his time went to data, which surprised him.
  > "what I found kind of shocking was that a huge amount of my time ended up just empirically being spent on the data set and just massaging all the data sets." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=38s) · 2018-08
  > "at Tesla I probably spent 1/3 of my time on data, 1/3 on evals, and 1/3 on everything else." — [x/2024-05.md](https://x.com/karpathy/status/1795873666481402010) · 2024-05
- Searching over data mixes paid off more than searching over architectures.
  > "We see more significant improvements from training data distribution search (data splits + oversampling factor ratios) than neural architecture search. The latter is so overrated :)" — [x/2019-09.md](https://x.com/karpathy/status/1175138379198914560) · 2019-09
- So he calls the people who curate data the programmers.
  > "the labelers are kind of the programmers because by curating data sets they're really um informing the final functioning of the system." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=300s) · 2018-08
  > "they're telling the system how to interpret the scene, and they are quite literally programming the autopilot." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=3411s) · 2021-09
- More real data is his first choice of regularizer, ahead of clever tricks on a small set.
  > "First, the by far best and preferred way to regularize a model in any practical setting is to add more real training data." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "It is a very common mistake to spend a lot engineering cycles trying to squeeze juice out of a small dataset when you could instead be collecting more data." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- A good dataset covers the hard cases evenly. Size alone does not make it good.
  > "real-world data distribution is ~N(0,1) good dataset is ~U(-2,2)" — [x/2022-05.md](https://x.com/karpathy/status/1528453604515778560) · 2022-05
  > "You have to be careful though because more data is not always better. If you if you add boring data into your data set you may actually be diluting your data set, right?" — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=3727s) · 2021-09
  > "It's an active process of adding hard examples and subtracting the easy examples often." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=3752s) · 2021-09
- The edge goes to whoever runs the data loop fastest, not to whoever owns the most data.
  > "competitive advantage in AI goes not so much to those with data but those with a data engine: iterated data aquisition, re-training, evaluation, deployment, telemetry. And whoever can spin it fastest." — [x/2022-12.md](https://x.com/karpathy/status/1599852921541128194) · 2022-12
- He applies the same lesson to LLMs: raw web text is poor, and the assistant is programmed by its conversation data.
  > "The average webpage on the internet is so random and terrible it's not even clear how prior LLMs learn anything at all." — [x/2024-06.md](https://x.com/karpathy/status/1797313173449764933) · 2024-06
  > "When you're looking at a pre-training dataset in the frontier lab and you look at a random internet document, it's total garbage." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=3692s) · 2025-10
  > "we are going to be implicitly programming the assistant by creating data sets of conversations" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=3734s) · 2025-02

## How it shows up

- His training recipe starts with the data, before any model code.
  > "The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- He reads the trained net as a compiled copy of its data.
  > "since the neural net is effectively a compressed/compiled version of your dataset" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- At Tesla he let the network take over logic that people had written by hand.
  > "the software 2.0 stack quite literally ate through the software stack of the autopilot." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=326s) · 2025-06
  > "we don't actually want to do all of that fusion in the C++ code because we're actually not good enough to write that algorithm. We want the neural nets to write the algorithm" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=4349s) · 2022-10
- When he re-ran LeCun's 1989 network, he found that more data would have helped at no cost.
  > "simply scaling up the dataset in 1989 would have been an effective way to drive up the performance of the system, at no cost to inference latency" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- He tells newcomers that data work is dull and essential.
  > "they have to iterate on their data set and it's like eating their vegetables. But it's so incredibly important." — [youtube-appearances/unknown_3OxEpGU1unA_recent-breakthroughs-in-ai-andrej-karpathy.md](https://www.youtube.com/watch?v=3OxEpGU1unA&t=1747s) · 2021-02
- He counts open datasets as the open source of this era.
  > "The equivalent of open source in Software 2.0 land are open datasets." — [x/2021-02.md](https://x.com/karpathy/status/1365511769255342084) · 2021-02

## Tensions and evolution

- He saw the bottleneck move over the years. In 2016 algorithms had improved least, and by 2024 he said the architecture no longer held things back.
  > "in those 20 years there's been much less improvement in uh in algorithms than all these other three pieces." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=2155s) · 2016-09
  > "We are not constrained by human ingenuity in algorithms, as used to be the case in computer vision" — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=2282s) · 2021-09
  > "I don't think that the neural network architecture is like holding us back fundamentally anymore" — [youtube-appearances/unknown_hM_h0UA7upI_no-priors-ep-80-with-andrej.md](https://www.youtube.com/watch?v=hM_h0UA7upI&t=982s) · 2024-09
- He does not move everything into the net. Hand-written code stays where a rule is simpler, as a guard rail.
  > "just putting functionality from software 1.0 to 2.0 uh is not always a good idea. It's good idea sometimes." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=1713s) · 2020-04
  > "You almost think of it as like sedimentary layers where you have the new functionality, but the software 1.0 is is used for example to keep sort of a guarding rails around the software 2.0 part." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=1763s) · 2020-04
- Even in 2025 he had not found data he would call clean.
  > "I think I've never come across a data stream that felt *perfect* in quality." — [x/2025-06.md](https://x.com/karpathy/status/1936171874398208202) · 2025-06

## Related

- [Data engine](../methods/data-engine.md)
- [Software 2.0 and 3.0](software-2-and-3.md)
- [Look at the data and the numbers](../methods/look-at-the-data-and-numbers.md)
- [Training recipe](../methods/training-recipe.md)
- [Scale and compute](scale-and-compute.md)
- [Evaluation is the bottleneck](evaluation-is-the-bottleneck.md)
- [Verifiability drives progress](verifiability-drives-progress.md)
