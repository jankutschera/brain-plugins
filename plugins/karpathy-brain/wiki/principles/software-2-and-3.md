---
type: principle
sources: [blog, x, youtube, youtube-appearances]
quotes: 34
first_seen: 2017-08
last_seen: 2026-04
---
# Software 2.0 and 3.0

Neural nets are a new kind of software (2.0), and LLMs are a new computer that you program in English (3.0).
  > "LLMs are a new kind of computer, and you program them *in English*." — [x/2025-06.md](https://x.com/karpathy/status/1935518272667217925) · 2025-06

## Evidence

- In 2017 he framed neural nets as a new way to write software: an optimizer writes the code against an evaluation criterion.
  > "Neural networks are not just another classifier, they represent the beginning of a fundamental shift in how we develop software." — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "Software 2.0 is code written by the optimization based on an evaluation criterion" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "that code is not written in C++. It's written in weights of a neural network. And that code is not written by humans. It's written by the optimization" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=76s) · 2018-08
- He holds that the optimizer writes better code than people in many domains.
  > "Gradient descent can write code better than you. I'm sorry." — [x/2017-08.md](https://x.com/karpathy/status/893576281375219712) · 2017-08
  > "a neural network is a better piece of code than anything you or I can come up with in a large fraction of valuable verticals" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
- He describes deep learning as a search through program space.
  > "Deep Learning is a form of human-assisted but mostly constraint-driven software development. It works because a particular smooth relaxation of program space allows a surprisingly efficient and effective local search." — [x/2021-09.md](https://x.com/karpathy/status/1439676583690715140) · 2021-09
- With LLMs, prompts became programs, and the programs are written in English.
  > "The hottest new programming language is English" — [x/2023-01.md](https://x.com/karpathy/status/1617979122625712128) · 2023-01
  > "And basically your prompts are now programs that program the LLM. And uh remarkably uh these uh prompts are written in English." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=199s) · 2025-06
  > "So software 3.0 is kind of about uh you know, your programming now turns to prompting" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=199s) · 2026-04
- He treats the LLM as the kernel of a new operating system and borrows analogies from older computing.
  > "I think it's a lot more correct to think about it as the kernel process of an emerging operating system" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2548s) · 2023-11
  > "we can potentially borrow a lot of analogies from the previous Computing stack to try to think about this new Computing stack" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2725s) · 2023-11
  > "what's in the context window is your lever over the interpreter that is the LLM" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=204s) · 2026-04
- He wants builders to be fluent in all three paradigms.
  > "We have three completely different programming paradigms and I think if you're entering the industry it's a very good idea to be fluent in all of them" — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=340s) · 2025-06
- He notes that this computer reached ordinary people before companies and governments.
  > "they generate disproportionate benefit for regular people, while their impact is a lot more muted and lagging in corporations and governments" — [blog/karpathy.bearblog.dev/power-to-the-people.md](https://karpathy.bearblog.dev/power-to-the-people/) · 2025-04
  > "Money can't buy better ChatGPT." — [blog/karpathy.bearblog.dev/power-to-the-people.md](https://karpathy.bearblog.dev/power-to-the-people/) · 2025-04
- He asks what the new computer makes possible, not only what it speeds up.
  > "not to work in the existing paradigm of what things existed and just think about it as a speed up of what exists. It's actually like new things are available now." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=386s) · 2026-04
  > "all of my menu gen is spurious. It's working in the old paradigm that app shouldn't exist." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=362s) · 2026-04

## How it shows up

- He picks his frames on purpose, because the frame decides what you can extrapolate.
  > "The lens through which we view trends matters." — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
- He rejects the chatbot framing of LLMs.
  > "I don't think it's accurate to think of large language models as a chatbot or like some kind of a word generator" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2543s) · 2023-11
- In his demos the model writes and deploys the app itself.
  > "this is a very different Paradigm because in this Paradigm Claud just writes the app just for you and deploys it here in your browser" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=4278s) · 2025-02
- He sees programming people and programming models as the same skill.
  > "Programming turns into a kind of applied psychology of neural nets, biological or synthetic." — [x/2022-02.md](https://x.com/karpathy/status/1497652099701620738) · 2022-02
- He uses the new computer to make hard reading accessible.
  > "I feel like llms make a lot of reading very dramatically more accessible than it used to be before because you're not just right away confused" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=3489s) · 2025-02

## Tensions and evolution

- The 2017 essay already pointed at optimization and an evaluation criterion. In 2025 he named verifiability as the deciding feature.
  > "because the optimization can find much better code than what a human can write" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "Software 2.0 will become increasingly prevalent in any domain where repeated evaluation is possible and cheap, and where the algorithm itself is difficult to design explicitly" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "Software 2.0 easily automates what you can verify." — [blog/karpathy.bearblog.dev/verifiability.md](https://karpathy.bearblog.dev/verifiability/) · 2025-11
- He named the cost of Software 2.0 from the start: accuracy traded against understanding.
  > "we’ll be left with a choice of using a 90% accurate model we understand, or 99% accurate model we don’t" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
- In 2022 he called training from scratch outdated and predicted that, in the extreme, you would not train nets at all. In 2026 he said that in a verifiable setting with diverse datasets or RL environments, doing your own fine-tuning works.
  > "the whole setting of training a neural network from scratch on some target task (like digit recognition) is quickly becoming outdated due to finetuning" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
  > "In its most extreme extrapolation, you will not want to train any neural networks at all." — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
  > "If you have huge amount of diverse data sets of RL environments, etc., uh you can use your favorite fine-tuning framework and um and uh pull the lever and get something that actually uh works pretty well." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=878s) · 2026-04
- In 2023 he said AI engineers program in all three paradigms, but also that one can succeed in the role without ever training anything. By 2025 he told newcomers to be fluent in all three.
  > "We have three completely different programming paradigms and I think if you're entering the industry it's a very good idea to be fluent in all of them" — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=340s) · 2025-06
  > "AI Engineers simultaneously program in all 3 paradigms." — [x/2023-06.md](https://x.com/karpathy/status/1674873002314563584) · 2023-06
  > "One can be quite successful in this role without ever training anything." — [x/2023-06.md](https://x.com/karpathy/status/1674873002314563584) · 2023-06
- He admits he missed how general text generation would become.
  > "I guess I didn't appreciate the power and generality of text generation, like at all." — [x/2025-05.md](https://x.com/karpathy/status/1926460158063882401) · 2025-05

## Related

- [The data is the program](data-is-the-program.md)
- [Verifiability drives progress](verifiability-drives-progress.md)
- [LLMs are ghosts](llms-are-ghosts.md)
- [Build for agents](build-for-agents.md)
- [AI-assisted coding](../methods/ai-assisted-coding.md)
- [Using LLMs day to day](../methods/using-llms-day-to-day.md)
