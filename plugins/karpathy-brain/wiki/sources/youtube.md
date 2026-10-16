---
type: source
raw: raw/youtube/
files: 31
words: 277313
date_range: 2022-08 – 2025-02
---
# YouTube channel (@AndrejKarpathy)

## Coverage

- **What exists (MANIFEST.md):** 17 videos listed on https://www.youtube.com/@AndrejKarpathy, 15 transcripts saved (about 277k words, `.segments.json` twins not counted), 2 Stable Diffusion clips failed with TranscriptsDisabled. 31 files in all, including `videos.json`.
- **Dates:** file names carry coarse year buckets (`YYYY-10-09`, `upload_date_approx: true`). Every date on this page is the exact upload month from `build/youtube_exact_dates.json`: micrograd 2022-08; makemore 1 and 2 2022-09; makemore 3 and 4 2022-10; makemore 5 2022-11; Let's build GPT 2023-01; Intro to LLMs 2023-11; GPT tokenizer 2024-02; Reproduce GPT-2 2024-06; Deep Dive into LLMs 2025-02; How I use LLMs 2025-02; Stable Diffusion clips 2022-08. Two files named `2023-...` (makemore 4 and 5) were actually uploaded in 2022, and the Intro to LLMs talk named `2024-...` is from 2023-11.
- **Read in full:** Intro to LLMs (12k words), How I use LLMs (25k), Deep Dive into LLMs (41k).
- **Read in large part plus keyword sweep:** micrograd; makemore parts 3, 4 and 5 (including the full diagnostics and development-process sections); Let's build GPT; GPT tokenizer; Reproduce GPT-2 (43k words, the longest).
- **Intro, ending and keyword sweep:** makemore parts 1 and 2.
- **Cross-file sweep:** all transcripts grepped for biography markers (OpenAI, Tesla, Stanford, blog, years ago) and for Copilot mentions.
- **Skipped:** the three Stable Diffusion "dreams" clips (174, 43 and 37 words of `[Music]`/`[Applause]`, no speech). Middle stretches of the long lectures (tensor indexing, the BPE merge loop, DDP plumbing, HellaSwag rendering) were sampled by keyword only.
- **Caption quality:** the 2022 lectures are lowercase auto-captions without punctuation. Quotes keep misspellings as written ("andre", "Chachi PT", "microG grad", "bathroom" for batchnorm, "copal" for Copilot).
- **Shape of the channel:** two tracks. The Neural Networks: Zero to Hero series (2022-08 to 2024-06) builds micrograd, makemore, a GPT, a tokenizer and a GPT-2 reproduction in code. Three general-audience talks (2023-11, 2025-02, 2025-02) teach mental models of LLMs and how to use them.

## What this source shows about them

- The Zero to Hero lectures start from a blank notebook and build the model on camera.
  > "we are going to start with a blank jupiter notebook and by the end of this lecture we will define and train in neural net and you'll get to see everything that goes on under the hood" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=8s) · 2022-08
- The core claim of the series is that the algorithm is tiny and the rest is speed.
  > "my claim is that micrograd is what you need to train your networks and everything else is just efficiency" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=408s) · 2022-08
- Karpathy argues that you cannot treat autograd as a black box.
  > "it is a leaky abstraction in the sense that you can shoot yourself in the foot if you do not understanding its internals" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=79s) · 2022-10
- The lectures teach the diagnostics, not only the model: what to plot and what number to expect.
  > "I tried to introduce you to the diagnostic tools that you would use to understand whether your neural network is in a good State dynamically" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6758s) · 2022-10
  > "in training of neural Nets it is almost always the case that you will have a rough idea for what loss to expect at initialization" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=282s) · 2022-10
- Every fast version gets checked against a simpler reference, number for number.
  > "the nanog gbt here acts as reference code in pytorch to the C implementation so we're trying to exactly match up the two" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=14207s) · 2024-06
- Code is written to fail loudly.
  > "I don't super love the use of negative one because I like to be very explicit so that you get error messages when things don't go according to your expectation" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=1976s) · 2022-11
- The viewer is asked to predict, pause and try first, with the video as the answer key.
  > "work in Tandem and try it first yourself and then see me give away the answer and I think that'll be most valuable to you" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=770s) · 2022-10
- Mistakes stay in the edit, and the gaps in knowledge are said out loud.
  > "i thought about redoing it but i figured i should just leave the error in here because it's pretty funny" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=4517s) · 2022-08
  > "honestly we are getting to The Cutting Edge of where the field is we certainly haven't I would say soled initialization and we haven't soled back propagation" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6915s) · 2022-10
- The general-audience talks aim at mental models, not feature lists.
  > "what I'm hoping to achieve in this video is to give you kind of mental models for thinking through what it is that this tool is" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11s) · 2025-02
- The base model of an LLM is a lossy compression of the internet.
  > "this is not exactly a zip file because a zip file is lossless compression What's Happening Here is a lossy compression" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=345s) · 2023-11
- The assistant on top of it is a simulation of the people who labeled its training data.
  > "you're not talking to a magical AI you're talking to an average labeler" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=4699s) · 2025-02
- Models need tokens to think, which shapes how Karpathy prompts and how labels should be written.
  > "we actually have to distribute our reasoning and our computation across many tokens because every single token is only spending a finite amount of computation on it" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=6631s) · 2025-02
- Imitation caps a model at human level; reinforcement learning against a checkable reward can go past it.
  > "you can't fundamentally go beyond a human player if you're just imitating human players" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9817s) · 2025-02
- The practical advice for users is to treat LLMs as fallible tools and own the result.
  > "use them as tools in the toolbox check their work and own the product of your work but use them for inspiration for first draft uh ask them questions but always check and verify" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=12656s) · 2025-02
- Between the 2023 intro talk and the 2025 deep dive, the view of RLHF hardened from "optional stage three" to "not RL in the magical sense".
  > "this is kind of this optional stage three that can gain you additional performance in these language models" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=1332s) · 2023-11
  > "I mean RF is RL obviously but it's not RL in the magical sense" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11106s) · 2025-02
- In the same span, trust in public leaderboards dropped.
  > "I do think that in the last few months it's become a little bit gamed um and I don't trust it as much as I used to" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11820s) · 2025-02
- Coding help moved from Copilot completions on camera to IDE agents and vibe coding.
  > "that was a suggestion from GitHub co-pilot by the way" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=3544s) · 2023-01
  > "the name for this is called Vibe coding um a name with that I think I probably minted" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=4688s) · 2025-02

## Notable pieces

- **The spelled-out intro to neural networks and backpropagation (micrograd), 2022-08.** The series opener, and the source of the "100 lines" claim.
  > "the actual backpropagation autograd engine that gives you the power of neural networks is literally 100 lines of code of like very simple python" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=437s) · 2022-08
- **Makemore part 1 (bigrams), 2022-09.** A long warning about broadcasting, typical of the care with tensor shapes.
  > "hopefully this helps to scare you that you should have a respect for broadcasting, be careful, check your work, uh and uh understand how it works under the hood" — [youtube/2022-10-09_PaCmpygFfXo_the-spelled-out-intro-to-language.md](https://www.youtube.com/watch?v=PaCmpygFfXo&t=2967s) · 2022-09
- **Makemore part 2 (MLP), 2022-09.** Ends by sending the viewer to the original paper.
  > "It is 19 pages, but at this point you should actually be able to read a good chunk of this paper and understand uh pretty good chunks of it." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=4377s) · 2022-09
- **Makemore part 3 (activations, gradients, batch norm), 2022-10.** The fullest statement of the training diagnostics, and of a personal grudge against batch norm.
  > "I've shot myself in the foot with this layer over and over again in my life and I don't want you to suffer the same" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=4637s) · 2022-10
- **Makemore part 4 (becoming a backprop ninja), 2022-10.** Writing every backward pass by hand, as an exercise.
  > "now everyone just calls lost that backward uh we've lost something" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=239s) · 2022-10
- **Makemore part 5 (WaveNet), 2022-11.** Shows the real development process and admits its lack of rigor.
  > "honestly we're kind of in the dark we have no experimental harness we're just guessing and checking and this whole thing is terrible" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2826s) · 2022-11
- **Let's build GPT: from scratch, in code, spelled out, 2023-01.** Introduces the "attention is communication" framing.
  > "attention is a communication mechanism you can really think about it as a communication mechanism where you have a number of nodes in a directed graph" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=4301s) · 2023-01
- **Intro to Large Language Models, 2023-11.** A re-recording of an unrecorded talk; introduces the LLM-as-operating-system picture.
  > "I think it's a lot more correct to think about it as the kernel process of an emerging operating system" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2548s) · 2023-11
  > "unfortunately that talk was not recorded but a lot of people came to me after the talk and they told me that uh they really liked the talk so I would just I thought I would just re-record it and basically put it up on YouTube" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=6s) · 2023-11
- **Let's build the GPT tokenizer, 2024-02.** A lecture on the part of LLMs Karpathy likes least.
  > "tokenization is my least favorite part of working with large language models but unfortunately it is necessary to understand in some detail because it it is fairly hairy gnarly and there's a lot of hidden foot guns" — [youtube/2024-10-09_zduSFxRajkE_let-s-build-the-gpt-tokenizer.md](https://www.youtube.com/watch?v=zduSFxRajkE&t=8s) · 2024-02
  > "I will say that eternal glory goes to anyone who can get rid of it" — [youtube/2024-10-09_zduSFxRajkE_let-s-build-the-gpt-tokenizer.md](https://www.youtube.com/watch?v=zduSFxRajkE&t=7845s) · 2024-02
- **Let's reproduce GPT-2 (124M), 2024-06.** The longest video, ending in a full reproduction and its cost.
  > "today you can reproduce this model in roughly an hour or probably less even and it will cost you about 10 bucks" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=158s) · 2024-06
- **Deep Dive into LLMs like ChatGPT, 2025-02.** The longest general-audience talk (41k words), covering the whole training pipeline.
  > "I want to dispel a little bit of the magic of talking to an AI" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=4617s) · 2025-02
- **How I use LLMs, 2025-02.** A tour of Karpathy's own daily use, with real examples from life.
  > "the whole takeaway I want you to get from this is be mindful of the models that you're using" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1207s) · 2025-02
  > "it is rarely ever the case anymore that I read books just by myself I always involve an LM to help me read a book" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=3301s) · 2025-02

## Related

- Sources: [X](x.md) · [Blogs](blog.md) · [GitHub](github.md) · [YouTube appearances](youtube-appearances.md)
- Principles: [Build to understand](../principles/build-to-understand.md) · [The core is tiny](../principles/core-is-tiny.md) · [Neural nets fail silently](../principles/neural-nets-fail-silently.md) · [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md) · [Software 2.0 and 3.0](../principles/software-2-and-3.md) · [LLMs are ghosts](../principles/llms-are-ghosts.md) · [Verifiability drives progress](../principles/verifiability-drives-progress.md) · [Scale and compute](../principles/scale-and-compute.md) · [Demos are not products](../principles/demos-are-not-products.md)
- Methods: [Training recipe](../methods/training-recipe.md) · [Look at the data and numbers](../methods/look-at-the-data-and-numbers.md) · [Reference then port](../methods/reference-then-port.md) · [Fast feedback loops](../methods/fast-feedback-loops.md) · [Experiment log and delete](../methods/experiment-log-and-delete.md) · [AI-assisted coding](../methods/ai-assisted-coding.md) · [Knowledge work](../methods/knowledge-work.md) · [Using LLMs day to day](../methods/using-llms-day-to-day.md) · [Build it live](../methods/build-it-live.md) · [Smallest complete version](../methods/smallest-complete-version.md) · [Ramps to knowledge](../methods/ramps-to-knowledge.md) · [Demystify the math](../methods/demystify-the-math.md) · [Analogies and examples](../methods/analogies-and-examples.md) · [Learner does the work](../methods/learner-does-the-work.md) · [Show the mess](../methods/show-the-mess.md) · [Playful and accessible](../methods/playful-and-accessible.md)
