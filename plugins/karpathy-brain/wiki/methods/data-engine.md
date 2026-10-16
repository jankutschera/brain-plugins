---
type: method
sources: [blog, x, youtube, youtube-appearances]
quotes: 30
first_seen: 2017-11
last_seen: 2025-10
---
# Data engine

He runs a data engine: deploy the model, find where it fails, label those cases consistently, retrain, and repeat.
  > "the whole thing ends up being a staircase of improvement of perfecting your training set and you have to go through deployments so that you can mine the parts that are not yet represented well on the dataset." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5089s) · 2022-10

## Evidence

- He holds that every applied ML system needs a data engine.
  > "this is what I refer to as a data engine. And I think basically every single machine learning applied machine learning um uh process must have some kind of a data engine associated with it." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1023s) · 2018-08
  > "the data engine is what I call the almost biological feeling process by which you perfect the training sets for these neural networks." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5039s) · 2022-10
- The speed of the loop decides the outcome.
  > "the faster you can spin this loop of just iterating and curating your data set, um the the better this neural network will become." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=1974s) · 2021-09
  > "competitive advantage in AI goes not so much to those with data but those with a data engine: iterated data aquisition, re-training, evaluation, deployment, telemetry. And whoever can spin it fastest." — [x/2022-12.md](https://x.com/karpathy/status/1599852921541128194) · 2022-12
- A failure gets fixed by adding labeled examples of it, not by writing a rule.
  > "when the network fails in some hard or rare cases, we do not fix those predictions by writing code, but by including more labeled examples of those cases" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "we don't write explicit a code for is the left blinker on is the right blinker on track the keyboard over time and see if it's moving horizontally we actually use a fleet learning approach" — [youtube-appearances/unknown_Ucp0TTmvqOE_tesla-autonomy-day.md](https://www.youtube.com/watch?v=Ucp0TTmvqOE&t=7842s) · 2019-04
- Hand-built triggers find the failures in the fleet, and the clips become unit tests.
  > "starting with maybe ten of these we could we can develop the classifier for that" — [youtube-appearances/unknown_g2R2T631x7k_cvpr-20-workshop-on-scalability-in.md](https://www.youtube.com/watch?v=g2R2T631x7k&t=642s) · 2020-06
  > "we've ended up developing 221 triggers uh manually" — [youtube-appearances/unknown_g6bOwQdCJrc_cvpr-21-wad-keynote-andrej-karpathy.md](https://www.youtube.com/watch?v=g6bOwQdCJrc&t=891s) · 2021-06
  > "some of those clips end up going to unit tests to make sure that we even if we're failing right now we make sure we pass later" — [youtube-appearances/unknown_g6bOwQdCJrc_cvpr-21-wad-keynote-andrej-karpathy.md](https://www.youtube.com/watch?v=g6bOwQdCJrc&t=993s) · 2021-06
- Labeling rules must be consistent, and a simple task quickly needs pages of rules.
  > "Whatever you do decide uh you have to be consistent and you have to make sure that everyone knows" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=439s) · 2018-08
  > "So this grows to like 20 30 pages of documentation very quickly." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=470s) · 2018-08
  > "But suddenly I have 10,000 images that are mislabeled." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=455s) · 2018-08
- If the dataset is the code, it needs an IDE: tools to slice it, count it and flag labels the network disagrees with.
  > "So I what is a cool good IDE for writing 2.0 code? And I think it's completely not built out" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1154s) · 2018-08
  > "you really want to know what's in the data set and you want to slice and dice it different ways and get statistics over different labels and types of things in your data." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1187s) · 2018-08
  > "your network has a suspicion that something is incorrectly labeled when its prediction disagrees with the label by a lot." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1255s) · 2018-08
- He was wary of pre-filling labels from the model, because a model's errors are consistent.
  > "what's nice about humans is the variance is large but their bias is zero" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1618s) · 2018-08
  > "your network just become incorrect in a very consistent way" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1629s) · 2018-08
- Engineers build generic machinery so any new task is easy to add. The team's "North Star", jokingly called "operation vacation", was that only data curation would stay manual.
  > "we're mostly developing the automation infrastructure, and then it's easy to develop any new task." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=1004s) · 2020-04
  > "as long as the data labeling team is around and they're curating and improving our data sets then everything else can in principle be automated" — [youtube-appearances/unknown_oBklltKXtDE_pytorch-at-tesla-andrej-karpathy-tesla.md](https://www.youtube.com/watch?v=oBklltKXtDE&t=527s) · 2019-11

## How it shows up

- In a 2018 talk his cautionary example was the auto-wiper, which met a case nobody had labeled.
  > "and then it turns out that ketchup does not wipe." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1109s) · 2018-08
- He mines a dataset for surprises by sorting it by loss.
  > "When you sort your dataset descending by loss you are guaranteed to find something unexpected, strange and helpful." — [x/2020-10.md](https://x.com/karpathy/status/1311884485676294151) · 2020-10
- He curates toward hard cases, not toward volume.
  > "It's an active process of adding hard examples and subtracting the easy examples often." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=3752s) · 2021-09
- He counts ordinary driving as free labeling.
  > "when people drive cars and they steer the wheel, they're actually data labeling for you." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=1497s) · 2020-04
- The machinery let a small team carry the work.
  > "our team is not 500 people working on neural networks it's more like a few dozen of really really strong people on the team" — [youtube-appearances/unknown_g2R2T631x7k_cvpr-20-workshop-on-scalability-in.md](https://www.youtube.com/watch?v=g2R2T631x7k&t=826s) · 2020-06
- With LLMs he applies the same thinking: synthetic data needs diversity first, and fine-tuning is mainly about narrowing scope.
  > "The most important challenge is ensuring enough entropy/diversity in your generated data." — [x/2025-10.md](https://x.com/karpathy/status/1980665134415802554) · 2025-10
  > "it's a lot more about narrowing the scope, and especially when you have a lot of training examples." — [x/2025-10.md](https://x.com/karpathy/status/1973468610917179630) · 2025-10

## Tensions and evolution

- At Tesla in 2018 the labelers were the programmers. For LLM reasoning in 2025 he says labelers cannot write the right traces, so the model has to find them through RL.
  > "the labelers are kind of the programmers because by curating data sets they're really um informing the final functioning of the system." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=300s) · 2018-08
  > "a lot of these strategies are very difficult to hardcode as a human labeler because it's not clear what the thinking process should be" — [youtube/2025-10-09_EWvNQjAaOHw_how-i-use-llms.md](https://www.youtube.com/watch?v=EWvNQjAaOHw&t=1420s) · 2025-02
  > "we really want the llm to discover the token sequences that work for it" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=8396s) · 2025-02

## Related

- [The data is the program](../principles/data-is-the-program.md)
- [Look at the data and the numbers](look-at-the-data-and-numbers.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Demos are not products](../principles/demos-are-not-products.md)
- [Verifiability drives progress](../principles/verifiability-drives-progress.md)
- [Autoresearch](autoresearch.md)
