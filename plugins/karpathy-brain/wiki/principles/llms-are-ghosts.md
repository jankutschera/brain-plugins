---
type: principle
sources: [blog, x, youtube, youtube-appearances]
quotes: 37
first_seen: 2014-07
last_seen: 2026-04
---
# LLMs are ghosts

LLMs are a new kind of mind: "ghosts" that simulate human text, not animals. Using them well takes a mental model built for them.
  > "Stated plainly, today's frontier LLM research is not about building animals. It is about summoning ghosts." — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10

## Evidence

- Pretraining on human text stands in for evolution, and commercial pressure shapes the result.
  > "TLDR: Pretraining is our crappy evolution." — [x/2025-10.md](https://x.com/karpathy/status/1973435013875314729) · 2025-10
  > "LLMs are shaped a lot less by biological evolution and a lot more by commercial evolution." — [blog/karpathy.bearblog.dev/the-space-of-minds.md](https://karpathy.bearblog.dev/the-space-of-minds/) · 2025-11
  > "The space of intelligences is large and animal intelligence (the only kind we've ever known) is only a single point" — [x/2025-11.md](https://x.com/karpathy/status/1991910395720925418) · 2025-11
- The parameters are a lossy zip of the internet. Recall is vague and favors what appears often; the context window is working memory.
  > "these parameters that I showed you in an earlier slide are best kind of thought of as like a zip file of the internet" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=330s) · 2023-11
  > "this knowledge is not precise and exact this knowledge is vague and probabilistic and statistical and the kinds of things that occur often are the kinds of things that are more likely to be remembered" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=3108s) · 2025-02
  > "knowledge in the parameters of the neural network is a vague recollection the knowledge in the tokens that make up the context window is the working memory" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=5980s) · 2025-02
- He calls them simulators, not entities. A chat assistant simulates the labelers who wrote its training conversations.
  > "Don't think of LLMs as entities but as simulators." — [x/2025-12.md](https://x.com/karpathy/status/1997731268969304070) · 2025-12
  > "I think the right way to think about it is that this is the neural network simulation of a data labeler at openai" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=12272s) · 2025-02
  > "So the way I like to think about LLMs is that they're kind of like people spirits. Um they are stoastic simulations of people." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=888s) · 2025-06
- Hallucination is how they work, not a defect bolted onto them. They have no persistent self.
  > "in some sense, hallucination is all LLMs do. They are dream machines." — [x/2023-12.md](https://x.com/karpathy/status/1733299213503787018) · 2023-12
  > "it has no persistent self it has no sense of self it's a token tumbler" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=6147s) · 2025-02
- Their cognition differs from ours. Each token gets a fixed amount of compute, so they need tokens to think.
  > "we actually have to distribute our reasoning and our computation across many tokens because every single token is only spending a finite amount of computation on it" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=6631s) · 2025-02
  > "prompting is just making up for this cognitive difference between these two architectures like our brains here and LLM brains." — [youtube-appearances/unknown_bZQun8Y4L2A_state-of-gpt-brk216hfs.md](https://www.youtube.com/watch?v=bZQun8Y4L2A&t=1469s) · 2023-05
- Their ability is jagged: brilliant in one place, childish in the next.
  > "they are at the same time a genius polymath and a confused and cognitively challenged grade schooler, seconds away from getting tricked by a jailbreak to exfiltrate your data" — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "I covered kind of like what I call the Swiss cheese uh sort of model of llm capabilities that you should have in your mind" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11332s) · 2025-02
  > "I simultaneously feel like I'm talking to an extremely brilliant PhD student who's been like a systems programmer for their entire life and a 10-year-old." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1477s) · 2026-03
- They do not consolidate memory between sessions.
  > "LLMs are a bit like a coworker with Anterograde amnesia" — [x/2025-06.md](https://x.com/karpathy/status/1930003172246073412) · 2025-06
  > "LLMs are quite literally like the guy in Memento, except we haven't given them their scratchpad yet." — [x/2025-05.md](https://x.com/karpathy/status/1921368644069765486) · 2025-05
- A correct model of what they are makes you better at using them. He has said so in essays and in talks, though on stage he hedged that the framing may be "a little bit of philosophizing".
  > "People who build good internal models of this new intelligent entity will be better equipped to reason about it today and predict features of it in the future." — [blog/karpathy.bearblog.dev/the-space-of-minds.md](https://karpathy.bearblog.dev/the-space-of-minds/) · 2025-11
  > "if you have a good model of what they are or are not, then you're going to be more competent at uh using them." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1455s) · 2026-04
  > "I think it's a little bit of philosophizing." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1468s) · 2026-04

## How it shows up

- In his general-audience videos and posts he sets out to remove the magic.
  > "I want to dispel a little bit of the magic of talking to an AI" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=4617s) · 2025-02
  > "But roughly speaking (and today), you're not asking some magical AI. You're asking a human data labeler." — [x/2024-11.md](https://x.com/karpathy/status/1862565643436138619) · 2024-11
- He uses them as tools and keeps ownership of the result.
  > "you want to use it as a tool not as something that you kind of like letter rip on a problem and copypaste the results" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=7641s) · 2025-02
  > "to whatever extent these models are remain jagged, it's an indication that number one, maybe something slightly off. Or number two, you need to actually be in the loop a little bit" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=714s) · 2026-04
- He prompts with their nature in mind: they imitate, so you ask for success.
  > "LLMs don't want to succeed, they want to imitate. You want to succeed, and you should ask for it." — [youtube-appearances/unknown_bZQun8Y4L2A_state-of-gpt-brk216hfs.md](https://www.youtube.com/watch?v=bZQun8Y4L2A&t=1823s) · 2023-05
- He puts what matters into the context window, because that is the working memory.
  > "this context window is your finite precious resource of your working memory of your language model" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=2641s) · 2023-11
- He learns each new model by probing it, with suspicion.
  > "It's more just being suspicious of it and um figuring out over time." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1511s) · 2026-04

## Tensions and evolution

- He has warned against copying human learning since 2014, yet in 2025 he still found animals worth learning from, and held both views loosely.
  > "Thus, it is unfair to draw direct comparisons and extreme caution should be taken when drawing inspiration from human learning." — [blog/karpathy.github.io/2014__07__03__feature-learning-escapades.md](https://karpathy.github.io/2014/07/03/feature-learning-escapades/) · 2014-07
  > "I still think it is worth to be inspired by animals." — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
  > "And I say both of these with double digit percent uncertainty and cheer the work of those who disagree" — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
- He doubted unsupervised pretraining for vision in 2014 and 2019, though in 2019 he noted NLP "seems to be doing pretty well with BERT". By 2025 he called text pretraining the practical stand-in for evolution.
  > "I couldn’t see how Unsupervised Learning based solely on images could work." — [blog/karpathy.github.io/2014__07__03__feature-learning-escapades.md](https://karpathy.github.io/2014/07/03/feature-learning-escapades/) · 2014-07
  > "Do not get over-excited about unsupervised pretraining." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "though NLP seems to be doing pretty well with BERT and friends these days" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "Yes it is basically supervised learning that is ~absent in the animal kingdom. But it is a way to practically gather enough soft constraints over billions of parameters" — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
- By the end of 2025 LLMs had surprised him in both directions.
  > "LLMs are emerging as a new kind of intelligence, simultaneously a lot smarter than I expected and a lot dumber than I expected." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12

## Related

- [Software 2.0 and 3.0](software-2-and-3.md)
- [Verifiability drives progress](verifiability-drives-progress.md)
- [Demos are not products](demos-are-not-products.md)
- [Using LLMs day to day](../methods/using-llms-day-to-day.md)
- [Understanding cannot be outsourced](understanding-cannot-be-outsourced.md)
- [Evaluation is the bottleneck](evaluation-is-the-bottleneck.md)
