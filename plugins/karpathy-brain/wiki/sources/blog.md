---
type: source
raw: raw/blog/
files: 85
words: 133676
date_range: 2011-04 – 2026-04
---
# Blogs (karpathy.github.io, Medium, Bear Blog)

## Coverage

- **What exists (MANIFEST.md):** 45 saved posts, about 133,676 words of text, across three sites. karpathy.github.io: 24 pages (2011-04 to 2026-02, plus the undated "Hacker's guide to Neural Networks"). karpathy.medium.com: 8 posts (2015-11 to 2017-11). karpathy.bearblog.dev: 13 posts (2024-09 to 2026-04). The 85 files counted in the manifest include an `html/` copy of every post and each site's `feed.xml`; only the `.md` files were cited. One failure: the bearblog `/now/` page had no article body.
- **Read in full (41 posts):** every bearblog post, every Medium post, and on github.io the training recipe, the PhD survival guide, microgpt, RNN effectiveness, Pong from pixels (RL), the ImageNet human baseline, CIFAR-10, feature-learning escapades, quantifying productivity, Chrome extension programming, state of computer vision, switching to Jekyll, t-SNE, quantifying Hacker News, the Data Science Weekly interview (a link only), breaking convnets, the selfie post, biohacking lite, LeCun 1989, and the Medium stub.
- **Read partially:** `neuralnets.md` (Hacker's guide, 13.5k words, undated, marked by Karpathy as outdated): intro and Chapter 1 opening in full, then headings and opinion lines through Chapter 2. `2021__06__21__blockchain.md` (12.7k words, mostly code): intro, prose greps, conclusion. The two short stories (`2015__11__14__ai.md`, `2021__03__27__forward-pass.md`) are fiction and were quoted only where they state a view.
- **Caveat on `sequoia-ascent-2026.md`:** the post says its summary and "cleaned up transcript" were produced by an LLM (Codex 5.5) from the talk. The AI-written summary half was not quoted. Only Karpathy's own intro and the lines labelled "Andrej:" in the edited transcript were used. Treat those as spoken words lightly rewritten by an LLM, not as written prose.
- **Weighting:** for how Karpathy builds and teaches, the core posts are the recipe, PhD guide, microgpt, backprop, RL, RNN, Hacker's guide, Software 2.0, LeCun 1989, MenuGen, Sequoia and the 2025 bearblog essays. The lifestyle posts (biohacking, sleep tracker, digital and chemical hygiene) were used only for measurement habits and the 80/20 approach.
- **Skipped:** code bodies of the blockchain, microgpt and RNN posts (only prose cited), the long paper lists in the ICLR/ICML/trends posts, and the narrative body of the two short stories.
- **Shape over time:** dense in 2014-2016 (PhD years), a gap during Tesla (one 2018 post pointing to Medium), sparse 2019-2022, then a new bearblog in 2024-2026 with short essays on LLMs and agents.

## What this source shows about them

- The blog exists to close the gap between how magical something looks and how simple it is.
  > "Whenever there is a disconnect between how magical something seems and how simple it is under the hood I get all antsy and really want to write a blog post." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- Karpathy holds that you cannot use neural nets well without knowing how they work inside.
  > "If you insist on using the technology without understanding how it works you are likely to fail." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- Training is described as a process that fails quietly, which is why it needs patience and care.
  > "Most of the time it will train but silently work a bit worse." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- The data comes first, before any model code.
  > "The first step to training a neural net is to not touch any neural net code at all and instead begin by thoroughly inspecting your data." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- Progress is credited mostly to compute, data and infrastructure, not to new algorithms.
  > "to a first-order approximation the main driver of recent progress is not the algorithms but (similar to Computer Vision) compute/data/infrastructure" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- The blog is where the Software 2.0 idea was first laid out, and where it was later extended to verifiability.
  > "Software 2.0 is code written by the optimization based on an evaluation criterion" — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
  > "Software 2.0 easily automates what you can verify." — [blog/karpathy.bearblog.dev/verifiability.md](https://karpathy.bearblog.dev/verifiability/) · 2025-11
- The 2025 essays argue for a non-animal model of LLMs.
  > "Stated plainly, today's frontier LLM research is not about building animals. It is about summoning ghosts." — [blog/karpathy.bearblog.dev/animals-vs-ghosts.md](https://karpathy.bearblog.dev/animals-vs-ghosts/) · 2025-10
- Karpathy chooses problems by ambition, on the theory that difficulty grows slower than importance.
  > "a 10x more important problem is at most 2-3x harder to achieve" — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
- Questions get answered with data, including questions about Karpathy's own life.
  > "since I prefer my answers based on data and not confirmation-bias-susceptible personal anecdotes" — [blog/karpathy.github.io/2014__08__03__quantifying-productivity.md](https://karpathy.github.io/2014/08/03/quantifying-productivity/) · 2014-08
  > "To validate the energy deficit math I spent 100 days around late 2019 very carefully tracking my daily energy input and output." — [blog/karpathy.github.io/2020__06__11__biohacking-lite.md](https://karpathy.github.io/2020/06/11/biohacking-lite/) · 2020-06
- Teaching posts lead with code and physical intuition and keep math to a minimum.
  > "My exposition will center around code and physical intuitions instead of mathematical derivations." — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
- Karpathy prefers simple, owned technology and wants to be the paying customer.
  > "And I wish to pay for the software I use so that incentives are aligned and so that I am the customer." — [blog/karpathy.bearblog.dev/digital-hygiene.md](https://karpathy.bearblog.dev/digital-hygiene/) · 2025-03
- The newer posts tell builders to address the LLM instead of the human.
  > "Don't talk to a developer. Don't ask a developer to visit, look, or click. Instruct and empower their LLM." — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
- In the LLM-edited Sequoia transcript, understanding is named as the human bottleneck, and agentic engineering as keeping the professional quality bar.
  > "Understanding is still the bottleneck because you cannot be a good director if you do not understand." — [blog/karpathy.bearblog.dev/sequoia-ascent-2026.md](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · 2026-04
  > "Agentic engineering is about preserving the quality bar of professional software." — [blog/karpathy.bearblog.dev/sequoia-ascent-2026.md](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · 2026-04
- Wrong predictions get corrected in public, sometimes as an update to the same post, sometimes in a later one.
  > "Obviously this prediction was way off, with state of the art now in 95%" — [blog/karpathy.github.io/2011__04__27__manually-classifying-cifar10.md](https://karpathy.github.io/2011/04/27/manually-classifying-cifar10/) · 2011-04
  > "I think I may have given the impression that RNNs are magic and automatically do arbitrary sequential problems." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- Read end to end, the blog runs from gloom about AI in 2012 to surprise at LLMs in 2025.
  > "In any case, we are very, very far and this depresses me." — [blog/karpathy.github.io/2012__10__22__state-of-computer-vision.md](https://karpathy.github.io/2012/10/22/state-of-computer-vision/) · 2012-10
  > "LLMs are emerging as a new kind of intelligence, simultaneously a lot smarter than I expected and a lot dumber than I expected." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
- How code gets written changed most: hand-written loops in 2019, fully agent-written apps in 2025.
  > "I almost always write out the fully loopy version first and only then transform it to vectorized code one loop at a time." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "As such, I did not write any code directly; 100% of the code was written by Cursor+Claude and I basically don't really know how MenuGen works in the conventional sense that I am used to." — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04

## Notable pieces

- **A Recipe for Training Neural Networks (2019-04).** The main practical post: a staged process from data to tuning, and the advice to copy what works.
  > "my #1 advice is: Don’t be a hero." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- **The Unreasonable Effectiveness of Recurrent Neural Networks (2015-05).** Fun datasets such as Paul Graham essays carry the lesson.
  > "There’s something magical about Recurrent Neural Networks (RNNs)." — [blog/karpathy.github.io/2015__05__21__rnn-effectiveness.md](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) · 2015-05
  > "Wouldn’t it be great if we could sample startup wisdom on demand?" — [blog/karpathy.github.io/2015__05__21__rnn-effectiveness.md](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) · 2015-05
- **Deep Reinforcement Learning: Pong from Pixels (2016-05).** Policy gradients reduced to three sentences, with code in 130 lines of numpy.
  > "Policy Gradients: Run a policy for a while. See what actions led to high rewards. Increase their probability." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
  > "the whole thing is 130 lines of Python only using numpy as a dependency" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- **A Survival Guide to a PhD (2016-09).** Research taste, writing papers, giving talks, and the case for releasing code.
  > "You’re not a paper writer. You’re a member of a research community and your goal is to push the field forward." — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
- **Yes you should understand backprop (2016-12).** Explains why CS231n made students write backward passes in raw numpy.
  > "Backpropagation is a leaky abstraction; it is a credit assignment scheme with non-trivial consequences." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
  > "The students had to implement the forward and the backward pass of each layer in raw numpy." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
- **Software 2.0 (2017-11).** The essay that named the paradigm.
  > "Software (1.0) is eating the world, and now AI (Software 2.0) is eating software." — [blog/karpathy.medium.com/software-2-0-a64152b37c35.md](https://karpathy.medium.com/software-2-0-a64152b37c35) · 2017-11
- **What I learned from competing against a ConvNet on ImageNet (2014-09).** Karpathy as the "reference human".
  > "My own error in the end turned out to be 5.1%, approximately 1.7% better." — [blog/karpathy.github.io/2014__09__02__what-i-learned-from-competing-against-a-convnet-on-imagenet.md](https://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/) · 2014-09
- **Deep Neural Nets: 33 years ago and 33 years from now (2022-03).** Reproduces LeCun 1989 and extrapolates forward.
  > "2055 neural nets are basically the same as 2022 neural nets on the macro level, except bigger." — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- **Hacker's guide to Neural Networks (undated).** The earliest long tutorial, and the origin of the code-first teaching style.
  > "everything became much clearer when I started ignoring full-page, dense derivations of backpropagation equations and just started writing code" — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
- **microgpt (2026-02).** The end point of the simplification project: a full GPT in one dependency-free file.
  > "if you understand microgpt, you understand the algorithmic essence." — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
  > "a decade-long obsession to simplify LLMs to their bare essentials, and I think it is beautiful" — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
- **Vibe coding MenuGen (2025-04).** A first fully vibe-coded, deployed app, and an honest account of where it hurt.
  > "MenuGen is my first end-to-end vibe coded app" — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
  > "vibe coding full web apps today is kind of messy and not a good idea for anything of actual importance" — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
- **The append-and-review note (2025-03).** A one-note system for personal knowledge.
  > "Maintaining more than one note and managing and sorting them into folders and recursive substructures costs way too much cognitive bloat." — [blog/karpathy.bearblog.dev/the-append-and-review-note.md](https://karpathy.bearblog.dev/the-append-and-review-note/) · 2025-03
- **2025 LLM Year in Review (2025-12).** Names RLVR as the new training stage and records lost trust in benchmarks.
  > "In 2025, Reinforcement Learning from Verifiable Rewards (RLVR) emerged as the de facto new major stage to add to this mix." — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
- **Sequoia Ascent 2026 (2026-04).** A talk turned into a post by an LLM, as an experiment in publishing for LLM readers.
  > "As an experiment, I fed an LLM all of my recent blog posts and tweets, then I had it read this video's transcript and produce 1) a summary and 2) a cleaned up transcript" — [blog/karpathy.bearblog.dev/sequoia-ascent-2026.md](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · 2026-04
- **I love calculator (2024-09).** A short essay on what technology should be: self-contained and loyal to its user.
  > "It has no other master. It just does the thing. It is perfect." — [blog/karpathy.bearblog.dev/i-love-calculator.md](https://karpathy.bearblog.dev/i-love-calculator/) · 2024-09

## Related

- Sources: [X](x.md) · [YouTube channel](youtube.md) · [GitHub](github.md) · [YouTube appearances](youtube-appearances.md)
- Principles: [Build to understand](../principles/build-to-understand.md) · [Neural nets fail silently](../principles/neural-nets-fail-silently.md) · [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md) · [Data is the program](../principles/data-is-the-program.md) · [Software 2.0 and 3.0](../principles/software-2-and-3.md) · [LLMs are ghosts](../principles/llms-are-ghosts.md) · [Verifiability drives progress](../principles/verifiability-drives-progress.md) · [Scale and compute](../principles/scale-and-compute.md) · [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md) · [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md) · [Build for agents](../principles/build-for-agents.md) · [Ambition and agency](../principles/ambition-and-agency.md) · [Openness and ownership](../principles/openness-and-ownership.md) · [Learning is effortful](../principles/learning-is-effortful.md)
- Methods: [Training recipe](../methods/training-recipe.md) · [Look at the data and numbers](../methods/look-at-the-data-and-numbers.md) · [Reference then port](../methods/reference-then-port.md) · [Experiment log and delete](../methods/experiment-log-and-delete.md) · [AI-assisted coding](../methods/ai-assisted-coding.md) · [Measure it yourself](../methods/measure-it-yourself.md) · [Knowledge work](../methods/knowledge-work.md) · [Deep work and side projects](../methods/deep-work-and-side-projects.md) · [Build it live](../methods/build-it-live.md) · [Smallest complete version](../methods/smallest-complete-version.md) · [Ramps to knowledge](../methods/ramps-to-knowledge.md) · [Demystify the math](../methods/demystify-the-math.md) · [Analogies and examples](../methods/analogies-and-examples.md) · [Learner does the work](../methods/learner-does-the-work.md) · [Show the mess](../methods/show-the-mess.md) · [Playful and accessible](../methods/playful-and-accessible.md)
