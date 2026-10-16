---
type: source
raw: raw/x/
files: 9657
words: 650334
date_range: 2009-06 – 2026-10
---
# X (@karpathy)

## Coverage

- **What exists (MANIFEST.md):** 9,426 posts by @karpathy collected via TwitterAPI.io (advanced search `from:karpathy include:nativeretweets`, one UTC day per window), 2009-06 to 2026-10, in 190 monthly files `raw/x/YYYY-MM.md`. The 9,657 files counted in the manifest are those monthly files plus the per-day API responses in `raw/x/api/` and `user_info.json`; the API folder was ignored. About 650k words.
- **Post types:** 4,580 original, 4,457 replies, 378 quotes, 11 retweets. Only Karpathy's own text was quoted, never the "Quoted tweet" block or retweets.
- **Gap:** posts from 2010 are absent; the collection jumps from 2009-10 to 2011-06.
- **How it was read:** every post was parsed into (file, month, type, likes, views, own text), then sampled four ways: (1) every non-retweet post over 100 words, 291 posts and about 79k words, all from 2023-04 to 2026-10, read in full; (2) the 25-35 most-liked posts of every year 2009-2022 and the 45-70 most-liked short posts of 2023-2026; (3) theme greps with an engagement floor (teaching, debugging, data, learning, from scratch, Software 2.0, biography); (4) targeted raw reads for the Eureka Labs announcement (2024-07) and the micrograd/microgpt posts (2026-02).
- **Era spread:** UBC and early Stanford (2009-2013), Stanford PhD and CS231n (2014-2016), OpenAI founding (2016-2017), Tesla (2017-2022), sabbatical and Zero to Hero (2022), OpenAI again (2023-2024), Eureka Labs, llm.c and nanochat (2024-2026), Anthropic (2026-05 onward).
- **Ingested after the build:** single posts live in `raw/x/ingest/`. 2026-10-16: post 2109361546505966046 (2026-10-11), a quote post of 2042334451611693415; only its own text was quoted.
- **Thin or skipped:** 2009-2013 is mostly link sharing and personal chatter. Thousands of low-engagement replies were not read one by one. Link lists, model-release news and personal life posts were sampled only where they show a method. Quotes containing an ellipsis, HTML entities or inner quotation marks were shortened or dropped.

## What this source shows about them

- X is where Karpathy states the "minimal core" idea most often: strip a system down until only the algorithm is left, and call the rest efficiency.
  > "Train and inference GPT in 243 lines of pure, dependency-free Python. This is the *full* algorithmic content of what is needed. Everything else is just for efficiency. I cannot simplify this any further." — [x/2026-02.md](https://x.com/karpathy/status/2021694437152157847) · 2026-02
- Minimal never means minified. The code has to stay readable.
  > "The optimization should be: minimize LOC subject to constraint that the code is clean." — [x/2024-04.md](https://x.com/karpathy/status/1783527854741114981) · 2024-04
- Karpathy treats neural net training as work that fails without errors, so the default mood is distrust.
  > "I exist in a perpetually terrified state of the remaining 20 silent bugs that certainly remain in my code." — [x/2024-03.md](https://x.com/karpathy/status/1765473722985771335) · 2024-03
- The Tesla years taught that the advantage lies in the data loop, not in owning the data.
  > "competitive advantage in AI goes not so much to those with data but those with a data engine: iterated data aquisition, re-training, evaluation, deployment, telemetry. And whoever can spin it fastest." — [x/2022-12.md](https://x.com/karpathy/status/1599852921541128194) · 2022-12
  > "at Tesla I probably spent 1/3 of my time on data, 1/3 on evals, and 1/3 on everything else." — [x/2024-05.md](https://x.com/karpathy/status/1795873666481402010) · 2024-05
- Each wave of AI is framed as a new way of writing programs, from Software 2.0 to prompting in English.
  > "Gradient descent can write code better than you. I'm sorry." — [x/2017-08.md](https://x.com/karpathy/status/893576281375219712) · 2017-08
  > "LLMs are a new kind of computer, and you program them *in English*." — [x/2025-06.md](https://x.com/karpathy/status/1935518272667217925) · 2025-06
- In 2025 the same framing produced the claim that verifiability predicts what gets automated.
  > "Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify." — [x/2025-11.md](https://x.com/karpathy/status/1990116666194456651) · 2025-11
- Karpathy insists on a non-human mental model of LLMs.
  > "today's frontier LLM research is not about building animals. It is about summoning ghosts." — [x/2025-10.md](https://x.com/karpathy/status/1973435013875314729) · 2025-10
  > "Don't think of LLMs as entities but as simulators." — [x/2025-12.md](https://x.com/karpathy/status/1997731268969304070) · 2025-12
- Evaluation is treated as the speed limit of iteration, and public benchmarks as gameable.
  > "Your speed of iteration is to a very large degree the speed with which you can answer this question." — [x/2023-08.md](https://x.com/karpathy/status/1695520663371735259) · 2023-08
  > "First I usually urge caution with public benchmarks because imo they can be quite possible to game." — [x/2025-11.md](https://x.com/karpathy/status/1990854771058913347) · 2025-11
- The main critique of AI coding tools is that coding is mostly reading and checking, not writing.
  > "This is my major criticism of LLM coding in that they casually spit out *way* too much code per query at arbitrary complexity, pretending there is no stage 2." — [x/2025-06.md](https://x.com/karpathy/status/1930305209747812559) · 2025-06
- Timelines are deliberately calibrated below the hype.
  > "Basically my AI timelines are about 5-10X pessimistic w.r.t. what you'll find in your neighborhood SF AI house party or on your twitter timeline" — [x/2025-10.md](https://x.com/karpathy/status/1979644538185752935) · 2025-10
- The posts push builders to make docs and products usable by agents.
  > "It's 2026. Build. For. Agents." — [x/2026-02.md](https://x.com/karpathy/status/2026360908398862478) · 2026-02
- Learning is defined by effort and kept sharply apart from entertainment.
  > "Learning is not supposed to be fun. It doesn't have to be actively not fun either, but the primary feeling should be that of effort." — [x/2024-02.md](https://x.com/karpathy/status/1756380066580455557) · 2024-02
- Teaching gets equal weight with building: making work accessible is called half the job.
  > "TLDR: Step 1 build the thing. Step 2 build the ramp." — [x/2024-02.md](https://x.com/karpathy/status/1760388761349927356) · 2024-02
- Karpathy dislikes formalism that hides a simple idea.
  > "I get triggered when RL is dressed up in its full rigorous math formalism because it's gate-keeping an essentially trivial core idea." — [x/2025-01.md](https://x.com/karpathy/status/1884317937185743206) · 2025-01
- Views change in public, with the old mistake named: on text generation, and on agency versus intelligence.
  > "I guess I didn't appreciate the power and generality of text generation, like at all." — [x/2025-05.md](https://x.com/karpathy/status/1926460158063882401) · 2025-05
  > "I had this intuitively wrong for decades" — [x/2025-02.md](https://x.com/karpathy/status/1894099637218545984) · 2025-02
- Reinforcement learning shows the biggest swings: hope in 2016, "the source of all magic" in early 2025, bearish on RL itself by mid 2025.
  > "Almost every single shocking result of deep learning, and the source of all *magic* is always 2." — [x/2025-01.md](https://x.com/karpathy/status/1883941452738355376) · 2025-01
  > "I am bullish on environments and agentic interactions but I am bearish on reinforcement learning specifically." — [x/2025-08.md](https://x.com/karpathy/status/1960803117689397543) · 2025-08
- The feed records the move from autocomplete to agents as it happened, in December 2025.
  > "I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
- It is also the main record of the career: Tesla, Eureka Labs, Anthropic.
  > "Excited to join Tesla as the Director of AI!" — [x/2017-06.md](https://x.com/karpathy/status/877330494555176962) · 2017-06
  > "Excited to share that I am starting an AI+Education company called Eureka Labs." — [x/2024-07.md](https://x.com/karpathy/status/1813263734707790301) · 2024-07
  > "Personal update: I've joined Anthropic." — [x/2026-05.md](https://x.com/karpathy/status/2056753169888334312) · 2026-05

## Notable pieces

- The 2018-07 list of common neural net mistakes, which the micrograd lecture points back to four years later.
  > "most common neural net mistakes: 1) you didn't try to overfit a single batch first." — [x/2018-07.md](https://x.com/karpathy/status/1013244313327681536) · 2018-07
  > "i've actually tweeted the most common neural net mistakes a long time ago now" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=7850s) · 2022-08
- A 2020-11 post gives the most exact version of the "look at the data" rule.
  > "Take the raw x,y batch tuple, ship it back to CPU, unrender, visualize." — [x/2020-11.md](https://x.com/karpathy/status/1328547710966743040) · 2020-11
- The 2022-08 micrograd launch post, with the confidence that anyone can learn backprop.
  > "If you know Python, have a vague recollection of taking some derivatives in your high school, watch this video and not understand backpropagation and the core of neural nets by the end then I will eat a shoe :D" — [x/2022-08.md](https://x.com/karpathy/status/1559672720895254528) · 2022-08
- The 2023-01 one-liner that became the best-known slogan for Software 3.0.
  > "The hottest new programming language is English" — [x/2023-01.md](https://x.com/karpathy/status/1617979122625712128) · 2023-01
- The 2024-02 post on accessibility, built on the micrograd lesson.
  > "you might be leaving somewhere 10-100X of the potential of that exact same piece of work on the table just because you haven't made it sufficiently accessible." — [x/2024-02.md](https://x.com/karpathy/status/1760388761349927356) · 2024-02
- The 2024-02 post on "snacking" content versus real learning.
  > "Consider the opportunity cost of snacking and seek the meal - the textbooks, docs, papers, manuals, longform." — [x/2024-02.md](https://x.com/karpathy/status/1756380066580455557) · 2024-02
- The 2024-05 thread on management, which reports a failed experiment with 1on1s.
  > "I had ~30 direct reports and didn't do 1on1s (as a scheduled, regular activity) at Tesla and imo it was great." — [x/2024-05.md](https://x.com/karpathy/status/1796556328078619103) · 2024-05
  > "I went back to try 1on1s again at OAI and regret it." — [x/2024-05.md](https://x.com/karpathy/status/1796556328078619103) · 2024-05
- The 2024-07 Eureka Labs announcement sets out the teacher-plus-AI model.
  > "The teacher still designs the course materials, but they are supported, leveraged and scaled with an AI Teaching Assistant who is optimized to help guide the students through them." — [x/2024-07.md](https://x.com/karpathy/status/1813263734707790301) · 2024-07
- The 2025-02 post that coined "vibe coding", framed at the time as a toy for weekend projects.
  > "where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." — [x/2025-02.md](https://x.com/karpathy/status/1886192184808149383) · 2025-02
  > "It's not too bad for throwaway weekend projects, but still quite amusing." — [x/2025-02.md](https://x.com/karpathy/status/1886192184808149383) · 2025-02
- The 2025-04 post on a careful AI coding loop, the counterweight to vibe coding.
  > "The emphasis is on keeping a very tight leash on this new over-eager junior intern savant with encyclopedic knowledge of software, but who also bullshits you all the time" — [x/2025-04.md](https://x.com/karpathy/status/1915581920022585597) · 2025-04
- The 2025-11 post on AI in schools.
  > "You will never be able to detect the use of AI in homework. Full stop." — [x/2025-11.md](https://x.com/karpathy/status/1993010584175141038) · 2025-11
- A 2025-12 admission after the agent shift.
  > "I've never felt this much behind as a programmer." — [x/2025-12.md](https://x.com/karpathy/status/2004607146781278521) · 2025-12
- The 2026-01 notes on working with agents, where the method turns declarative.
  > "Don't tell it what to do, give it success criteria and watch it go." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
- The 2026-03 autoresearch posts.
  > "Seeing the agent do this entire workflow end-to-end and all by itself as it worked through approx. 700 changes autonomously is wild." — [x/2026-03.md](https://x.com/karpathy/status/2031135152349524125) · 2026-03
- The 2026-04 post on LLM-compiled wikis, the idea behind this wiki.
  > "a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images)." — [x/2026-04.md](https://x.com/karpathy/status/2039805659525644595) · 2026-04
- The 2026-10 post on the widening gap in how people see LLM capability, a funnel driven by problem size, domain and access (ingested 2026-10-16).
  > "this gap in shared understanding of LLM capability is *widening*." — [x/ingest/2026-10-11_2109361546505966046.md](https://x.com/karpathy/status/2109361546505966046) · 2026-10
  > "The impact scales with ambition, problem size, and horizon." — [x/ingest/2026-10-11_2109361546505966046.md](https://x.com/karpathy/status/2109361546505966046) · 2026-10

## Related

- Sources: [YouTube channel](youtube.md) · [Blogs](blog.md) · [GitHub](github.md) · [YouTube appearances](youtube-appearances.md)
- Principles: [Build to understand](../principles/build-to-understand.md) · [The core is tiny](../principles/core-is-tiny.md) · [Neural nets fail silently](../principles/neural-nets-fail-silently.md) · [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md) · [Data is the program](../principles/data-is-the-program.md) · [Software 2.0 and 3.0](../principles/software-2-and-3.md) · [LLMs are ghosts](../principles/llms-are-ghosts.md) · [Verifiability drives progress](../principles/verifiability-drives-progress.md) · [Scale and compute](../principles/scale-and-compute.md) · [Demos are not products](../principles/demos-are-not-products.md) · [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md) · [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md) · [Build for agents](../principles/build-for-agents.md) · [Ambition and agency](../principles/ambition-and-agency.md) · [Openness and ownership](../principles/openness-and-ownership.md) · [Learning is effortful](../principles/learning-is-effortful.md)
- Methods: [Training recipe](../methods/training-recipe.md) · [Reference then port](../methods/reference-then-port.md) · [Reproduce landmarks](../methods/reproduce-landmarks.md) · [Fast feedback loops](../methods/fast-feedback-loops.md) · [Data engine](../methods/data-engine.md) · [AI-assisted coding](../methods/ai-assisted-coding.md) · [Autoresearch](../methods/autoresearch.md) · [Measure it yourself](../methods/measure-it-yourself.md) · [Knowledge work](../methods/knowledge-work.md) · [Using LLMs day to day](../methods/using-llms-day-to-day.md) · [Deep work and side projects](../methods/deep-work-and-side-projects.md) · [Build it live](../methods/build-it-live.md) · [Smallest complete version](../methods/smallest-complete-version.md) · [Ramps to knowledge](../methods/ramps-to-knowledge.md) · [Demystify the math](../methods/demystify-the-math.md) · [Analogies and examples](../methods/analogies-and-examples.md) · [Playful and accessible](../methods/playful-and-accessible.md) · [Education with AI](../methods/education-with-ai.md)
