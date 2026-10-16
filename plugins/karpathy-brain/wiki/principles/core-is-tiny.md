---
type: principle
sources: [github, x, youtube, youtube-appearances]
quotes: 26
first_seen: 2015-05
last_seen: 2026-08
---
# The core is tiny

The core of an algorithm fits on a page; everything else in a real code base is there to make it fast.
  > "This file is the complete algorithm. Everything else is just efficiency." — [github/_gists/8627fe009c40f57531cb18360106ce95/microgpt.py](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) · 2026-02

## Evidence

- He makes the same claim about neural net training in a lecture, a tweet and a podcast, years apart.
  > "my claim is that micrograd is what you need to train your networks and everything else is just efficiency" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=408s) · 2022-08
  > "These 94 lines of code are everything that is needed to train a neural network. Everything else is just efficiency." — [x/2024-06.md](https://x.com/karpathy/status/1803963383018066272) · 2024-06
  > "So micrograd, these 100 lines of Python, are everything you need to understand how neural networks train. Everything else is just efficiency." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8309s) · 2025-10
- He says the same of GPT: the model is small, and the bulk of the code is batching for speed.
  > "GPT is not a complicated model and this implementation is appropriately about 300 lines of code" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
  > "The majority of the complexity is just being clever with batching (both across examples and over sequence length) for efficiency." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
- He applies it to whole LLM training stacks.
  > "training neural nets and LLMs specifically um is a huge amount of code, but all of that code is actually complexity from efficiency." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3721s) · 2026-03
  > "Train and inference GPT in 243 lines of pure, dependency-free Python. This is the *full* algorithmic content of what is needed. Everything else is just for efficiency. I cannot simplify this any further." — [x/2026-02.md](https://x.com/karpathy/status/2021694437152157847) · 2026-02
- For a general audience, he reduces an LLM to parameters plus a short run file, and says the value sits in the parameters.
  > "a large language model is just two files right um there will be two files in this hypothetical directory" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=24s) · 2023-11
  > "it's usually just a couple hundred lines of code it's not it's not that crazy and uh this is all fairly understandable and usually fairly standard what's not standard are the parameters that's where the actual value is" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=2695s) · 2025-02
- Scale changes the infrastructure, not the principle.
  > "the architecture is actually like nearly identical to what we implemented ourselves but of course it's a massive infrastructure challenge to train this" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=6673s) · 2023-01
  > "basically the use of convolutions is strictly for efficiency it doesn't actually change the model we've implemented" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2872s) · 2022-11
- Minimal does not mean minified. The short version must stay readable.
  > "The optimization should be: minimize LOC subject to constraint that the code is clean." — [x/2024-04.md](https://x.com/karpathy/status/1783527854741114981) · 2024-04
  > "200 lines of breathable, commented code. It would be easy to go lower if you sacrifice that, I've only chipped away at the conceptual parts." — [x/2026-02.md](https://x.com/karpathy/status/2021998329899757908) · 2026-02

## How it shows up

- He calls the boiling-down a long-running obsession.
  > "So, I have this like running obsession of like maybe a decade or two of just like simplifying and boiling down the uh basically LLMs uh to like their bare essence." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3697s) · 2026-03
- His bigger repos point back to a small core. The char-rnn README sends readers to a 100-line version.
  > "it might be helpful to know that this code is really just a slightly more fancy version of this" — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
  > "Minimal character-level Vanilla RNN model." — [github/_gists/d4dee566867f8291f086/min-char-rnn.py](https://gist.github.com/karpathy/d4dee566867f8291f086) · 2015-07
- micrograd's README, updated after microgpt (2026), points to microgpt with the same "everything else is just efficiency" line.
  > "is the complete algorithm in a single file — everything else is just efficiency." — [github/micrograd/README.md](https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md) · 2026-08
- He comes back to the small core to breathe when things get too complicated.
  > "Sometimes when things get too complicated, I come back to this code and just breathe a little." — [x/2024-06.md](https://x.com/karpathy/status/1803963383018066272) · 2024-06
- Boiling down is a step he could not hand to an agent.
  > "Like try to boil down my um neural network training to the simplest thing and it can't do it." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3911s) · 2026-03
- He extends the idea from code to models: keep a small "cognitive core" and look knowledge up.
  > "I think we just need to get to the cognitive core and I think the cognitive core can be extremely small and it's just this thing that thinks" — [youtube-appearances/unknown_hM_h0UA7upI_no-priors-ep-80-with-andrej.md](https://www.youtube.com/watch?v=hM_h0UA7upI&t=1652s) · 2024-09
  > "a few billion param model that maximally sacrifices encyclopedic knowledge for capability." — [x/2025-06.md](https://x.com/karpathy/status/1938626382248149433) · 2025-06
  > "Because we're not that good at memorization, we're forced to find patterns in a more general sense." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=3379s) · 2025-10

## Tensions and evolution

- The GPT core kept shrinking: about 300 lines in minGPT (2020), 243 lines in microgpt (2026-02), then 200 lines, which he calls final.
  > "GPT is not a complicated model and this implementation is appropriately about 300 lines of code" — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2020-08
  > "It's the 200 lines. I thought about this for a long time. I was obsessed about this for a long time. This is this is the solution. Trust me, it can't get simpler." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3922s) · 2026-03
- On small models he holds that you have to go big before you can go small (2024-07), so the cognitive core comes after the giants, not instead of them.
  > "the models have to first get larger before they can get smaller" — [x/2024-07.md](https://x.com/karpathy/status/1814038096218083497) · 2024-07

## Related

- [Simplicity is a constraint](simplicity-is-a-constraint.md)
- [Build to understand](build-to-understand.md)
- [Scale and compute](scale-and-compute.md)
- [Reference then port](../methods/reference-then-port.md)
- [Smallest complete version](../methods/smallest-complete-version.md)
- [Experiment log and delete](../methods/experiment-log-and-delete.md)
