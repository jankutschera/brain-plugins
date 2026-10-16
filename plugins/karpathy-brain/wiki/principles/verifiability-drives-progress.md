---
type: principle
sources: [blog, x, youtube, youtube-appearances]
quotes: 42
first_seen: 2016-05
last_seen: 2026-10
---
# Verifiability drives progress

What can be verified gets automated. Reinforcement learning against a verifiable reward can go past imitation, though RL as practiced today is crude.
  > "traditional computers can easily automate what you can specify in code. And uh, kind of this latest round of LLMs can easily automate what you can uh, verify in a certain in a certain sense." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=607s) · 2026-04

## Evidence

- Specification predicted what classic software automated; verification predicts what learned systems automate.
  > "Software 1.0 easily automates what you can specify." — [blog/karpathy.bearblog.dev/verifiability.md](https://karpathy.bearblog.dev/verifiability/) · 2025-11
  > "Software 2.0 easily automates what you can verify." — [blog/karpathy.bearblog.dev/verifiability.md](https://karpathy.bearblog.dev/verifiability/) · 2025-11
  > "In this new programming paradigm then, the new most predictive feature to look at is verifiability." — [x/2025-11.md](https://x.com/karpathy/status/1990116666194456651) · 2025-11
- A verifiable task is an optimizable task.
  > "If a task/job is verifiable, then it is optimizable directly or via reinforcement learning, and a neural net can be trained to work extremely well." — [blog/karpathy.bearblog.dev/verifiability.md](https://karpathy.bearblog.dev/verifiability/) · 2025-11
- Imitation caps a model at human level. Trial and error is where the surprises come from.
  > "There is 1) imitation learning (watch and repeat, i.e. pretraining, supervised finetuning), and 2) trial-and-error learning (reinforcement learning)." — [x/2025-01.md](https://x.com/karpathy/status/1883941452738355376) · 2025-01
  > "you can't fundamentally go beyond a human player if you're just imitating human players" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9817s) · 2025-02
  > "alphago in the process of reinforcement learning discovered kind of like a strategy of playing that was unknown to humans and but is in retrospect uh brilliant" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9952s) · 2025-02
- RL is guess-and-check, and through it the model finds its own ways of thinking that a labeler could not write down.
  > "it's basically a guess and check we're going to guess many different types of solutions we're going to check them and we're going to do more of what worked in the future" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=8729s) · 2025-02
  > "it's learning what I like to call cognitive strategies of how you manipulate a problem and how you approach it from different perspectives" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9144s) · 2025-02
  > "The model could never learn this with 1 (by imitation), because the cognition of the model and the cognition of the human labeler is different." — [x/2025-01.md](https://x.com/karpathy/status/1883941452738355376) · 2025-01
- RLHF does not count as real RL for him, because a learned reward model can be gamed. A verifiable reward can be run much longer.
  > "RL is powerful. RLHF is not." — [x/2024-08.md](https://x.com/karpathy/status/1821277264996352246) · 2024-08
  > "The RM we train for LLMs is just a vibe check in the exact same way." — [x/2024-08.md](https://x.com/karpathy/status/1821277264996352246) · 2024-08
  > "reinforcement learning is extremely good at discovering a way to game the model to game the simulation" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=10891s) · 2025-02
  > "in these verifiable domains you can run RL indefinitely" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11132s) · 2025-02
- Verifiability also explains why models are jagged: they are strong where labs could reward them. In 2026 he adds economic value, since labs pick their training environments by revenue potential.
  > "So, I think the reason I wrote about verifiability is I'm trying to understand why these things are so jagged." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=644s) · 2026-04
  > "if you're in the circuits that were part of the RL, you fly and if you're in the circuits that are out of the data distribution, you're going to struggle" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=794s) · 2026-04
  > "You're either in the data distribution (on the rails of the RL circuits) and flying or you're off-roading in the jungle with a machete, in relative terms." — [x/2026-04.md](https://x.com/karpathy/status/2049903821095354523) · 2026-04
  > "Capability peaks in domains that are digital, verifiable and economically valuable." — [x/ingest/2026-10-11_2109361546505966046.md](https://x.com/karpathy/status/2109361546505966046) · 2026-10
  > "This is because LLM capability emerges from reinforcement learning on verifiable rewards on a curated environment mixture driven by revenue potential." — [x/ingest/2026-10-11_2109361546505966046.md](https://x.com/karpathy/status/2109361546505966046) · 2026-10
- Outcome-based RL is still crude: one reward spread over a whole attempt.
  > "Reinforcement learning is terrible. It just so happens that everything that we had before it is much worse because previously we were just imitating people" — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2502s) · 2025-10
  > "The way I like to put it is you're sucking supervision through a straw." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2599s) · 2025-10
- The bottleneck is a reward signal and practice problems for every domain.
  > "the main challenge here is that there's a lack of a reward Criterion in the general case" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2401s) · 2023-11
  > "we have to create practice problems for all of domains of knowledge" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=10086s) · 2025-02

## How it shows up

- He describes building datasets for LLMs as writing textbooks with exercises in them.
  > "When we're creating datasets for LLMs, it's no different from writing textbooks for them, with these 3 types of data. They have to read, and they have to practice." — [x/2025-01.md](https://x.com/karpathy/status/1885026028428681698) · 2025-01
  > "we now have to effectively write textbooks for llms and AIS across all the disciplines of human knowledge" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11248s) · 2025-02
- He tells users to map where a model was trained, since there is no manual.
  > "you have to actually explore this thing that they give you that has no manual" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=784s) · 2026-04
  > "you have to kind of figure out which which circuits you're in in your application" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=802s) · 2026-04
- He lost trust in benchmarks, because benchmarks are verifiable and so get trained against.
  > "Related to all this is my general apathy and loss of trust in benchmarks in 2025." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "Training on the test set is a new art form." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
- He looks for methods that get more signal out of each attempt.
  > "There's significantly more bits of supervision we extract per rollout via a review/reflect stage" — [x/2025-07.md](https://x.com/karpathy/status/1944435412489171119) · 2025-07

## Tensions and evolution

- His view of RL has swung several times. In 2016 it was "guess-and-check", in 2017 a field where his ConvNet instincts failed, and in 2023 something to set aside until LLMs existed.
  > "The approach is a fancy form of guess-and-check" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
  > "Everything I know about design of ConvNets (resnets, bigger=better, batchnorms etc) is useless in RL. Superbasic 4-layer ConvNets work best." — [x/2017-01.md](https://x.com/karpathy/status/822563606344695810) · 2017-01
  > "the correct thing was to forget all that, first train LLMs that learn (1) world knowledge, (2) reasoning and (3) tool-use (esp writing code) all from internet text" — [x/2023-05.md](https://x.com/karpathy/status/1662160997451431936) · 2023-05
- In 2025 RL on verifiable rewards became the new training stage. Within months he called himself bearish on RL as such and expected more ideas to be needed.
  > "In 2025, Reinforcement Learning from Verifiable Rewards (RLVR) emerged as the de facto new major stage to add to this mix." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "I'm fairly certain RL will continue to yield more intermediate gains, but I also don't expect it to be the full story." — [x/2025-07.md](https://x.com/karpathy/status/1944435412489171119) · 2025-07
  > "I am bullish on environments and agentic interactions but I am bearish on reinforcement learning specifically." — [x/2025-08.md](https://x.com/karpathy/status/1960803117689397543) · 2025-08
- In November 2023 he called RLHF an optional third stage and said LLMs had only "system one". By February 2025 RLHF was "not RL in the magical sense", because it can't be run indefinitely, and models were learning to think.
  > "this is kind of this optional stage three that can gain you additional performance in these language models" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=1332s) · 2023-11
  > "it turns out that large language models currently only have a system one" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2188s) · 2023-11
  > "RF is RL obviously but it's not RL in the magical sense this is not RL that you can run indefinitely" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11106s) · 2025-02
  > "what's incredible here is basically the model is discovering ways to think" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9140s) · 2025-02
- He leaves open whether skills learned in verifiable domains carry over to the rest.
  > "it's a a question an open question as to whether the thinking strategies that are developed inside verifiable domains transfer and are generalizable to other domains that are unverifiable" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=12530s) · 2025-02

## Related

- [Software 2.0 and 3.0](software-2-and-3.md)
- [LLMs are ghosts](llms-are-ghosts.md)
- [Evaluation is the bottleneck](evaluation-is-the-bottleneck.md)
- [Demos are not products](demos-are-not-products.md)
- [Scale and compute](scale-and-compute.md)
- [Autoresearch](../methods/autoresearch.md)
- [The capability gap](capability-gap.md)
