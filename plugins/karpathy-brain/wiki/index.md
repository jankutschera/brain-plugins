# Andrej Karpathy wiki: index

Quote-verified wiki of how he builds and teaches. Start with [hot.md](hot.md), then [rules.md](rules.md) (seven rules for building and teaching). History: [log.md](log.md). Schema: `~/knowledge/people/CLAUDE.md`.

## Principles: what he believes

- [Ambition and agency](principles/ambition-and-agency.md): Pick ambitious problems, because a 10x more important problem is not 10x harder, and count agency and sheer volume of work above raw intelligence.
- [Build for agents](principles/build-for-agents.md): The main reader of docs, tools and products is now an LLM, so build for the agent.
- [The capability gap](principles/capability-gap.md): How much LLM capability someone sees depends on access tier, domain and problem size, so people with different exposure talk past each other.
- [Build to understand](principles/build-to-understand.md): You understand something only once you have built it yourself, from scratch.
- [The core is tiny](principles/core-is-tiny.md): The core of an algorithm fits on a page; everything else in a real code base is there to make it fast.
- [The data is the program](principles/data-is-the-program.md): In Software 2.0 the dataset is the program, so the data and the loop that improves it matter more than the architecture.
- [Demos are not products](principles/demos-are-not-products.md): A demo is cheap and a product is a march of nines, so autonomy arrives gradually and timelines need calibrating against the hype.
- [Evaluation is the bottleneck](principles/evaluation-is-the-bottleneck.md): How fast you improve a system depends on how fast you can tell whether a change helped, so evals matter as much as training, public benchmarks get gamed, and using the system yourself beats reading plots.
- [Learning is effortful](principles/learning-is-effortful.md): Real learning takes effort, like going to the gym; content that feels like learning is often entertainment.
- [LLMs are ghosts](principles/llms-are-ghosts.md): LLMs are a new kind of mind: "ghosts" that simulate human text, not animals. Using them well takes a mental model built for them.
- [Neural nets fail silently](principles/neural-nets-fail-silently.md): Neural net training is a leaky abstraction that fails without errors, so paranoia and patience beat speed.
- [Openness and ownership](principles/openness-and-ownership.md): Release the code and work in the open, and own your data and tools, so that incentives stay aligned with the people who use them.
- [Scale and compute](principles/scale-and-compute.md): Long-run progress comes mostly from compute, data and infrastructure, scaling is predictable, and the order is: make it work, then make it cheap.
- [Simplicity is a constraint](principles/simplicity-is-a-constraint.md): Simplicity, readability and few dependencies are hard constraints, and any added complexity has to earn its place.
- [Software 2.0 and 3.0](principles/software-2-and-3.md): Neural nets are a new kind of software (2.0), and LLMs are a new computer that you program in English (3.0).
- [Understanding cannot be outsourced](principles/understanding-cannot-be-outsourced.md): He hands more and more of the work to AI, but the understanding, the review and the quality bar stay with him.
- [Verifiability drives progress](principles/verifiability-drives-progress.md): What can be verified gets automated. Reinforcement learning against a verifiable reward can go past imitation, though RL as practiced today is crude.

## Methods: how he builds

- [AI-assisted coding](methods/ai-assisted-coding.md): He codes with AI in a tight loop: give context, ask for options, take small diffs, review, commit. Over four years this moved from autocomplete to agents that loop on their own against success criteria.
- [Autoresearch](methods/autoresearch.md): He has agents run the research loop. He writes the objective, the metric and the limits in a Markdown file, and the agent edits the training code, runs experiments and keeps what works.
- [Data engine](methods/data-engine.md): He runs a data engine: deploy the model, find where it fails, label those cases consistently, retrain, and repeat.
- [Deep work and side projects](methods/deep-work-and-side-projects.md): He protects long, uninterrupted stretches where he can get obsessed with one problem, and he keeps building small tools and projects for himself, publishing many of them.
- [Experiment log and delete](methods/experiment-log-and-delete.md): He logs every change with its effect, adopts other people's ideas only after testing them, and deletes code that doesn't earn its place.
- [Fast feedback loops](methods/fast-feedback-loops.md): He iterates on a small proxy with one clear metric, fast tooling and napkin math, and checks the result at the target scale.
- [Knowledge work](methods/knowledge-work.md): He turns what he reads into his own notes. For years that was one append-and-review note; since 2025 it is reading with an LLM in passes and having the LLM compile a personal wiki he can question.
- [Look at the data and the numbers](methods/look-at-the-data-and-numbers.md): He looks at exactly what enters the network and reads every number in a run as a diagnostic.
- [Measure it yourself](methods/measure-it-yourself.md): He measures things himself instead of trusting reported numbers: he becomes the human baseline on a dataset, keeps private question sets for models, and runs one-variable experiments on his own life.
- [Reference, then port](methods/reference-then-port.md): He writes a simple reference version first, then ports or speeds it up, and checks that the two give the same numbers.
- [Reproduce landmarks](methods/reproduce-landmarks.md): He reproduces a known result as his benchmark, explains any gap, then pushes the cost down.
- [Training recipe](methods/training-recipe.md): He trains nets with a fixed recipe: become one with the data, build the skeleton, overfit, regularize, tune, squeeze, and copy a proven setup before getting creative.
- [Using LLMs day to day](methods/using-llms-day-to-day.md): He picks the model on purpose, starts cheap and escalates, puts the material into the context instead of trusting the model's memory, and treats every answer as a first draft to check.

## Methods: how he teaches

- [Analogies and examples](methods/analogies-and-examples.md): He explains with analogies, coined phrases and concrete, often personal examples.
- [Build it live](methods/build-it-live.md): He teaches by building from an empty file, spelled out in code and not on slides, with a clean commit history to follow.
- [Demystify the math](methods/demystify-the-math.md): He leads with code and intuition, strips away gatekeeping formalism, and shows that the magic is simple underneath.
- [Education with AI](methods/education-with-ai.md): He sees AI as scaling the tutor, while the human teacher designs the material; that was the idea behind Eureka Labs.
- [Learner does the work](methods/learner-does-the-work.md): He makes learners predict, guess and build the pieces themselves, with the video as the answer key.
- [Playful and accessible](methods/playful-and-accessible.md): He keeps it fun and low-friction: toy datasets, browser demos, Colab, humor.
- [Ramps to knowledge](methods/ramps-to-knowledge.md): He builds ramps: each step depends only on the one before, and complexity grows one layer at a time, often in historical order.
- [Show the mess](methods/show-the-mess.md): He keeps bugs on camera, admits what he doesn't know, and teaches the failure modes as well as the wins.
- [Smallest complete version](methods/smallest-complete-version.md): He teaches at the smallest scale where the concept is still fully present, and ships one minimal, complete, runnable artifact.

## Sources

- [Blogs (karpathy.github.io, Medium, Bear Blog)](sources/blog.md): - **What exists (MANIFEST.md):** 45 saved posts, about 133,676 words of text, across three sites. karpathy.github.io: 24 pages (2011-04 to 2026-02, plus the undated "Hacker's guide to Neural Networks"). karpathy.medium.com: 8 posts (2015-11 to 2017-11). karpathy.bearblog.dev: 13 posts (2024-09 to 2026-04). The 85 files counted in the manifest include an `html/` copy of every post and each site's `feed.xml`; only the `.md` files were cited. One failure: the bearblog `/now/` page had no article body.
- [GitHub (karpathy repos and gists)](sources/github.md): - **What exists (MANIFEST.md):** github.com/karpathy via `gh repo list` and the gists API. 63 repos and 13 gists listed; 54 repos and all 13 gists cloned shallow (`.git` removed, SHAs in `clones.json`); 9 forks skipped (cpython, examples, lifejs, nn, optim, scriptsbots, simple-amt, sqlitedict, transformers). 1,672 files (370 binary), about 5.0M words of text, of which about 871K are "prose" by file type. No fetch failures.
- [X (@karpathy)](sources/x.md): - **What exists (MANIFEST.md):** 9,426 posts by @karpathy collected via TwitterAPI.io (advanced search `from:karpathy include:nativeretweets`, one UTC day per window), 2009-06 to 2026-10, in 190 monthly files `raw/x/YYYY-MM.md`. The 9,657 files counted in the manifest are those monthly files plus the per-day API responses in `raw/x/api/` and `user_info.json`; the API folder was ignored. About 650k words.
- [YouTube appearances (talks, interviews, podcasts)](sources/youtube-appearances.md): - **What exists (MANIFEST.md):** 22 accepted transcripts (291,401 words) of Karpathy on other channels, each with a `.segments.json` twin, plus the `candidates.json` discovery file: 45 files. Discovery was a yt-dlp search with 290 hits; 22 accepted, 27 rejected, 241 not reviewed. No fetch failures. Every `upload_date` is `unknown`.
- [YouTube channel (@AndrejKarpathy)](sources/youtube.md): - **What exists (MANIFEST.md):** 17 videos listed on https://www.youtube.com/@AndrejKarpathy, 15 transcripts saved (about 277k words, `.segments.json` twins not counted), 2 Stable Diffusion clips failed with TranscriptsDisabled. 31 files in all, including `videos.json`.
