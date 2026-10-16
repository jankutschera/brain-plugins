---
type: principle
sources: [x, youtube-appearances, blog, youtube, github]
quotes: 26
first_seen: 2014-08
last_seen: 2026-09
---
# Evaluation is the bottleneck

How fast you improve a system depends on how fast you can tell whether a change helped, so evals matter as much as training, public benchmarks get gamed, and using the system yourself beats reading plots.
  > "The fundamental problem is this: "you changed a thing, did you net improve the system?". Your speed of iteration is to a very large degree the speed with which you can answer this question." — [x/2023-08.md](https://x.com/karpathy/status/1695520663371735259) · 2023-08

## Evidence

- At Tesla, test sets got as much work as training sets.
  > "we put just as much work into massaging the test sets as we do into training sets." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=780s) · 2020-04
  > "at Tesla I probably spent 1/3 of my time on data, 1/3 on evals, and 1/3 on everything else." — [x/2024-05.md](https://x.com/karpathy/status/1795873666481402010) · 2024-05
- With learned software you cannot read the code to know it works, so evaluation has to carry that job.
  > "this is just basically the idea that we understood the previous software is is false, and fundamentally you just need extremely good evaluation." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=3026s) · 2021-09
- He borrowed unit tests from test-driven development for neural nets.
  > "we spend a lot of time inspired by uh, sort of test-driven development to build out very complicated unit tests and predicates for how the detector should behave in different cases." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=792s) · 2020-04
- Good evals are hard and expensive to build.
  > "good evals are unintuitively difficult, highly work-intensive, but quite important" — [x/2024-05.md](https://x.com/karpathy/status/1795873666481402010) · 2024-05
- Public test sets leak into training and get gamed.
  > "any open (non-private) test dataset inevitably leak into training sets." — [x/2024-05.md](https://x.com/karpathy/status/1795873666481402010) · 2024-05
  > "First I usually urge caution with public benchmarks because imo they can be quite possible to game." — [x/2025-11.md](https://x.com/karpathy/status/1990854771058913347) · 2025-11
  > "Training on the test set is a new art form." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
- Looking at the test set at all is a form of training on it.
  > "every single time you evaluate your test loss and you learn something from it, you are basically starting to also train on the test split" — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=3357s) · 2022-09
- Direct experience with a system gives intuition that numbers hide.
  > "you can see it, you can play with it, you can perturb it, you can get a sense of it, you have an intuition for it. I think numbers and plots and graphs are much harder." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5239s) · 2022-10
- He wants answers from data, and a single number often hides the real picture.
  > "since I prefer my answers based on data and not confirmation-bias-susceptible personal anecdotes" — [blog/karpathy.github.io/2014__08__03__quantifying-productivity.md](https://karpathy.github.io/2014/08/03/quantifying-productivity/) · 2014-08
  > "Human accuracy is not a point. It lives on a tradeoff curve." — [blog/karpathy.github.io/2014__09__02__what-i-learned-from-competing-against-a-convnet-on-imagenet.md](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/) · 2014-09

## How it shows up

- His bar for AI progress is a practical job test, not a hard exam.
  > "The most bullish AI capability I'm looking for is not whether it's able to solve PhD grade problems. It's whether you'd hire it as a junior intern." — [x/2024-12.md](https://x.com/karpathy/status/1868061331355840704) · 2024-12
- A data engine is only as good as its tests: failures go into unit tests and the pass rate shows progress.
  > "we then spin the data engine on occluded signs, and then we see that the percent pass goes from 40% to 99% or something like that" — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=842s) · 2020-04
- In nanochat he reruns noisy evals and reports a spread instead of one score.
  > "I ran this command 7 individual times. Because our training is mildly non-deterministic, we get a spread of CORE scores" — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09
- He picks smooth metrics that compare changes fairly.
  > "lower is better, and vocab-size-independent so architectural changes are fairly compared." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- He uses imperfect evals for early signal and says what they can't tell him.
  > "this is not a perfect eval and there's some caveats here uh but at least we have some confidence that that we're not doing something completely wrong" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=13575s) · 2024-06
- He records failed attempts as results in their own right.
  > "This is the fifth failed attempt to beat pure FineWeb-EDU on CORE score." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09

## Tensions and evolution

- In 2014 he used his own human baseline to give benchmark numbers context. By 2025 he had lost trust in benchmarks.
  > "I thought that the impressive performance by the winning team would only make sense if it was put in perspective with human accuracy" — [blog/karpathy.github.io/2014__09__02__what-i-learned-from-competing-against-a-convnet-on-imagenet.md](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/) · 2014-09
  > "Related to all this is my general apathy and loss of trust in benchmarks in 2025." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
- In November 2023 he showed Chatbot Arena as the leaderboard to watch, with no caveats. By February 2025 he called it gamed.
  > "so this for example is a chatbot Arena it is managed by team at Berkeley" — [youtube/2024-10-09_zjkBMFhNj_g_1hr-talk-intro-to-large-language.md](https://www.youtube.com/watch?v=zjkBMFhNj_g&t=1422s) · 2023-11
  > "I do think that in the last few months it's become a little bit gamed um and I don't trust it as much as I used to" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11820s) · 2025-02
  > "they are not getting better models overall but better LM Arena models, whatever that is." — [x/2025-04.md](https://x.com/karpathy/status/1917546757929722115) · 2025-04
- In February 2025 he fell back on his own vibe checks. A month later he distrusted those too.
  > "As far as a quick vibe check over ~2 hours this morning, Grok 3 + Thinking feels somewhere around the state of the art territory" — [x/2025-02.md](https://x.com/karpathy/status/1891720635363254772) · 2025-02
  > "In absence of great comprehensive evals I tried to turn to vibe checks instead, but I now fear they are misleading and there is too much opportunity for confirmation bias, too low sample size, etc., it's just not great." — [x/2025-03.md](https://x.com/karpathy/status/1896266683301659068) · 2025-03

## Related

- [Measure it yourself](../methods/measure-it-yourself.md)
- [Data engine](../methods/data-engine.md)
- [Verifiability drives progress](verifiability-drives-progress.md)
- [Data is the program](data-is-the-program.md)
- [Fast feedback loops](../methods/fast-feedback-loops.md)
- [Experiment log and delete](../methods/experiment-log-and-delete.md)
- [Using LLMs day to day](../methods/using-llms-day-to-day.md)
