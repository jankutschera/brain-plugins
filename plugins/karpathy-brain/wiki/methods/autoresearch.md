---
type: method
sources: [github, x, youtube-appearances, youtube]
quotes: 27
first_seen: 2015-05
last_seen: 2026-09
---
# Autoresearch

He has agents run the research loop. He writes the objective, the metric and the limits in a Markdown file, and the agent edits the training code, runs experiments and keeps what works.
  > "And auto research is just, yeah, here's an objective, here's a metric, here's your boundaries of what you can and cannot do. And go." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1053s) · 2026-03

## Evidence

- The human edits the prompt and the agent edits the code.
  > "the human iterates on the prompt (.md)" — [x/2026-03.md](https://x.com/karpathy/status/2030371219518931079) · 2026-03
  > "the AI agent iterates on the training code (.py)" — [x/2026-03.md](https://x.com/karpathy/status/2030371219518931079) · 2026-03
  > "you are programming the `program.md` Markdown files that provide context to the AI agents and set up your autonomous research org." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- He keeps the agent's scope to one file so the diffs stay reviewable.
  > "The agent only touches `train.py`. This keeps the scope manageable and diffs reviewable." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- Fixed-length runs make every experiment comparable and set the pace.
  > "First, this makes experiments directly comparable regardless of what the agent changes (model size, batch size, architecture, etc)." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
  > "This means you can expect approx 12 experiments/hour and approx 100 experiments while you sleep." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- The rule for each change is simple, and the agent is told not to stop and ask.
  > "If they work, keep. If they don't, discard." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
  > "do NOT pause to ask the human if you should continue." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- He writes his simplicity rule into the agent's instructions.
  > "All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- Every experiment gets logged.
  > "When an experiment is done, log it to `results.tsv`" — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- Overnight, it found tunings he had missed after two decades of doing this by hand.
  > "I let auto research go for like overnight and it came back with like tunings that I didn't see." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1123s) · 2026-03
  > "I did forget like the weight decay on the value embeddings and my Adam betas were not sufficiently tuned and these things just jointly interact." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1129s) · 2026-03
- The agent's results went into nanochat, including ideas he had failed to make work himself.
  > "This set of changes came from autoresearch round 2, where I asked it to reference the modded-nanogpt repo for inspiration." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09
  > "(I had previously tried them manually a long time ago and they caused regressions)." — [github/nanochat/dev/LEADERBOARD.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LEADERBOARD.md) · 2026-09

## How it shows up

- He now spends his effort on the agent setup more than on the model code.
  > "where I optimize and tune the agent flows even more than the nanochat repo directly." — [x/2026-03.md](https://x.com/karpathy/status/2029701092347630069) · 2026-03
- He is modest about the instructions file.
  > "So program MD is my crappy attempt at describing like how the auto researcher should work." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1265s) · 2026-03
- He wants to stop being the one who runs and reads the sweeps.
  > "I shouldn't be a bottleneck. I shouldn't be running these hyperparameter optimizations. I shouldn't be looking at the results." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1138s) · 2026-03
- The instructions tell the agent what to do when it runs dry.
  > "If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- He gives agents papers as TeX source and asks how they apply to the project.
  > "The goal is to fetch the TeX Source of the paper (not the PDF!)" — [github/nanochat/.claude/skills/read-arxiv-paper/SKILL.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/.claude/skills/read-arxiv-paper/SKILL.md) · 2026-09
- He tells others to check whether their problem fits the pattern: a cheap, objective metric.
  > "And more generally, *any* metric you care about that is reasonably efficient to evaluate (or that has more efficient proxy metrics such as training a smaller network) can be autoresearched by an agent swarm. It's worth thinking about whether your problem falls into this bucket too." — [x/2026-03.md](https://x.com/karpathy/status/2031135152349524125) · 2026-03

## Tensions and evolution

- In 2015 and 2021 he described the human babysitting many runs as the core of the job. In 2026 the agent does it overnight.
  > "It is very common in deep learning to run many different models with many different hyperparameter settings, and in the end take whatever checkpoint gave the best validation performance." — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
  > "success in it is to a large extent proportional to raw experimental throughput - the ability to babysit a large number of experiments at once, staring at plots and tweaking/re-launching what works." — [x/2021-01.md](https://x.com/karpathy/status/1350503355299205120) · 2021-01
  > "You wake up in the morning to a log of experiments and (hopefully) a better model." — [github/autoresearch/README.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/README.md) · 2026-03
- In his 2022 lectures he admitted to tuning by hand with no harness.
  > "honestly we're kind of in the dark we have no experimental harness we're just guessing and checking and this whole thing is terrible" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2826s) · 2022-11
- He is impressed by the agent but limits the claim: it implements ideas, it does not invent them.
  > "Seeing the agent do this entire workflow end-to-end and all by itself as it worked through approx. 700 changes autonomously is wild." — [x/2026-03.md](https://x.com/karpathy/status/2031135152349524125) · 2026-03
  > "The AI of today is very good at implementing ideas, but a lot less good at coming up with creative ones." — [x/2026-03.md](https://x.com/karpathy/status/2029957088022254014) · 2026-03

## Related

- [AI-assisted coding](ai-assisted-coding.md)
- [Fast feedback loops](fast-feedback-loops.md)
- [Experiment log and delete](experiment-log-and-delete.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Verifiability drives progress](../principles/verifiability-drives-progress.md)
- [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md)
