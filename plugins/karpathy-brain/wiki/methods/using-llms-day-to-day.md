---
type: method
sources: [youtube, x, blog]
quotes: 27
first_seen: 2023-11
last_seen: 2026-10
---
# Using LLMs day to day

He picks the model on purpose, starts cheap and escalates, puts the material into the context instead of trusting the model's memory, and treats every answer as a first draft to check.
  > "the whole takeaway I want you to get from this is be mindful of the models that you're using" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1207s) · 2025-02

## Evidence

- He tries a fast model first and switches to a thinking model when the answer looks weak.
  > "try without reasoning first and if your model is not solving that kind of kind of a problem try to switch to a reasoning model" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=7725s) · 2025-02
  > "empirically about 80 90% of my use is just gp4 and when I come across a very difficult problem like in math and code Etc I will reach for the thinking models" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=9644s) · 2025-02
- He asks several models the same question, his "LLM council".
  > "I kind of refer to all these models as my llm Council so they're kind of like the Council of language models" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1360s) · 2025-02
  > "So your best performance will come from just asking all the models, and then getting them to come to a consensus" — [x/2024-12.md](https://x.com/karpathy/status/1869860858006049259) · 2024-12
- He treats the context window as scarce working memory and starts a new chat per topic.
  > "think of the tokens in the context window as a precious resource um think of that as the working memory of the model and don't overload it with irrelevant information" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1056s) · 2025-02
  > "anytime you are switching topic I encourage you to always start a new chat" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=992s) · 2025-02
- He pastes in the material instead of relying on what the model remembers.
  > "usually when I actually interact with LMS and I want them to recall specific things it always works better if you just give it to them" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=6048s) · 2025-02
- He sends math and fresh facts to tools.
  > "if they try to do it all in their memory I don't fully trust it and prefer to use tools whenever possible" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=7097s) · 2025-02
  > "whenever something is latest or something changes I prefer to use the search tool" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=2429s) · 2025-02
- He prompts with examples, not just descriptions.
  > "when I give instructions to llms I always like to number one give it sort of the description but then also give it examples so I like to give concrete examples" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=7205s) · 2025-02
- He treats output as a first draft and checks it.
  > "treat this as your first draft treat this as papers to look at um but don't take this as uh definitely true" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=2918s) · 2025-02
  > "use them as tools in the toolbox check their work and own the product of your work but use them for inspiration for first draft uh ask them questions but always check and verify" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=12656s) · 2025-02
- He trusts answers more when the topic is common online.
  > "I feel more confident trusting traship PT a bit more because this is not something esoteric I do expect there to be like tons and tons of documents about blood test results" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=6278s) · 2025-02

## How it shows up

- He talks instead of typing.
  > "the big takeaway here is don't type stuff out use voice it works quite well and I use this pervasively" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=5242s) · 2025-02
- For images of data, he has the model transcribe first and reason second.
  > "the reason I like to First transcribe the relevant information into text is because I want to make sure that the model is seeing the values correctly" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=6144s) · 2025-02
- He splits a task into pieces the model is good at.
  > "I've broken down the problem into a problems that are easier for the model I know that the model can't count it can't do mental counting but I know that the model is actually pretty good at doing copy pasting" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=7204s) · 2025-02
- He saves repeated prompts as custom GPTs.
  > "what this feature really is is that it's just saving you prompting time" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=7266s) · 2025-02
- A suspicious number sends him to the primary source.
  > "here I became suspicious because I see that Chach PT is telling me it's 1.7 trillion" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=4024s) · 2025-02
- He asks for visual output, often HTML.
  > "hot tip try ask for HTML." — [x/2026-05.md](https://x.com/karpathy/status/2053872850101285137) · 2026-05
  > "I could probably code these diagrams myself, but it's soo much better to just sit back, and iterate in English." — [x/2023-11.md](https://x.com/karpathy/status/1720939313112945057) · 2023-11

## Tensions and evolution

- In the February 2025 video he says he moved from doubt to liking ChatGPT's memory feature.
  > "when this feature was announced I wasn't 100% sure if this was going to be helpful or not but I think I'm definitely coming around" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=6968s) · 2025-02
- From late 2025 he says people want pictures and video back, and by October 2026 he is most bullish on generated explainer videos.
  > "People actually dislike reading text - it is slow and effortful." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "imo audio is the human-preferred input to AIs but vision (images/animations/video) is the preferred output from them." — [x/2026-05.md](https://x.com/karpathy/status/2053872850101285137) · 2026-05
  > "The output format I am most bullish on is fully custom / bespoke explainer videos generated on any arbitrary topic." — [x/2026-10.md](https://x.com/karpathy/status/2105819303471976479) · 2026-10
- He used to point people to public leaderboards for choosing a model. By February 2025 he trusted them less and treated them as a first pass only.
  > "I do think that in the last few months it's become a little bit gamed um and I don't trust it as much as I used to" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11820s) · 2025-02
  > "use this as a first pass uh but uh sort of try out a few of the models for your tasks and see which one performs better" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11847s) · 2025-02

## Related

- [LLMs are ghosts](../principles/llms-are-ghosts.md)
- [Measure it yourself](measure-it-yourself.md)
- [Knowledge work](knowledge-work.md)
- [AI-assisted coding](ai-assisted-coding.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md)
