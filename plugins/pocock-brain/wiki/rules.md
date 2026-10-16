---
type: query
question: "What are his rules for how he builds and how he teaches?"
date: 2026-10-07
rules: 7
---
# Seven rules: how he builds and how he teaches

## Coverage

Filed back from a query on 2026-10-07. The rules were drawn from the principle and method pages. A rule was kept only if he states it in at least two different raw source folders: blog, GitHub, his own YouTube, appearances on other channels, X. They're ranked by how many sources carry the rule and how consistently he has held it. Where his view moved, the caveat is quoted too.

## How he builds

### 1. Align before any code

He gets interviewed by the agent until both share one design concept; misalignment, not code, is what fails.
  > "The most common failure mode in software development is misalignment." — [github/skills/README.md](https://github.com/mattpocock/skills/blob/HEAD/README.md)
  > "But planning, this alignment phase, has to be human in the loop. Has to be." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=1621s) · AI Engineer
  > "The whole point of planning is to get on the same wavelength with the LLM, not to generate an asset you don't read" — [x/2026-04.md](https://x.com/mattpocockuk/status/2039806494435074555) · 2026-04
  > "that's what programming is it's about turning a poorly defined spec into a well-defined one" — [youtube/2023-03-07_WuHSnvsO6Mg_total-typescript-tour-and-ama.md](https://www.youtube.com/watch?v=WuHSnvsO6Mg&t=935s) · 2023-03

The tool changed (plan mode was dropped for grilling), the rule did not.
  > "I wrote this in January 2026, and my thinking has changed. I no longer use plan mode." — [blog/plan-mode-introduction.md](https://www.aihero.dev/plan-mode-introduction) · 2026-01

### 2. Build the feedback loop first, then turn rules into checks

How fast the agent gets feedback caps how fast you can go; a repeated mistake becomes a mechanical check, not another instruction.
  > "The rate at which you can get feedback is your speed limit. Never outrun your headlights." — [blog/tips-for-ai-coding-with-ralph-wiggum.md](https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum) · 2026-01
  > "the quality of your feedback loops influences how good your AI can code, essentially. That is the ceiling." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4218s) · AI Engineer
  > "Default to building the check over writing the rule." — [github/skills/skills/engineering/retro/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/retro/SKILL.md)
  > "Found an error? Do a /retro, and make it impossible next time" — [x/2026-09.md](https://x.com/mattpocockuk/status/2099859946053533933) · 2026-09

His main loop is test-first, but he no longer treats TDD as dogma.
  > "The most effective technique I've found to improve Claude Code's output is 20 years old: Write a failing test first." — [x/2026-02.md](https://x.com/mattpocockuk/status/2025935480609468862) · 2026-02
  > "So yeah, I I have a mixed relationship with TDD." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=4838s) · The Pragmatic Engineer

### 3. Give the agent less

Small tasks sized to the "smart zone", near-empty instruction files, and deleting before adding.
  > "the more you put in the context window, the worse the AI is going to be." — [blog/creating-the-perfect-claude-code-status-line.md](https://www.aihero.dev/creating-the-perfect-claude-code-status-line) · 2025-10
  > "Each one of these tickets is supposed to just be the size of a single context window or a single smart zone." — [youtube/2026-07-16_M6mYodf0dJM_mattpocock-skills-a-complete-ai-coding.md](https://www.youtube.com/watch?v=M6mYodf0dJM&t=751s) · 2026-07
  > "90% of people can delete their AGENTS.md and their output will improve." — [x/2026-07.md](https://x.com/mattpocockuk/status/2073473197991715246) · 2026-07
  > "First thing I would do is I would delete every single skill, every single plugin, every single MCP server." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=3649s) · David Ondrej

The threshold moves with each model; the rule stays.
  > "I used to think it was around 100K tokens about 6 months ago." — [youtube/2026-07-20_sOd7svdu_1I_what-is-the-dumb-zone.md](https://www.youtube.com/shorts/sOd7svdu_1I?t=82s) · 2026-07

### 4. Design the interface, delegate the implementation

He shapes the codebase into deep modules: lots of behaviour behind a small interface; the human owns the interface, the agent owns what is inside.
  > "Design the interface, delegate the implementation." — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=986s) · AI Engineer
  > "Deep, grey-box modules with simple interfaces are the KING - let AI control what's in the box to decrease your cognitive load" — [x/2026-02.md](https://x.com/mattpocockuk/status/2024049581529460839) · 2026-02
  > "I call them "grey-box modules" because you can look inside if you want to, but you're not really supposed to." — [blog/ways-ai-coding-has-rewired-my-brain.md](https://www.aihero.dev/ways-ai-coding-has-rewired-my-brain) · 2026-03
  > "Design **deep modules**: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface." — [github/skills/skills/engineering/codebase-design/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/codebase-design/SKILL.md)

## How he teaches

### 5. Problem first, solution after

The learner tries before being told; passing tests are the success signal; then he shows his solution.
  > "just like all of my courses this is a practical course where you have a problem that you need to solve you go into an Editor to try and solve it and then you see my solution afterwards" — [youtube/2024-07-08_wgcfq51twe0_this-launch-took-11-months-of.md](https://www.youtube.com/watch?v=wgcfq51twe0&t=95s) · 2024-07
  > "you'd essentially just be thrust into a problem and have to solve it on your own. I would give you the knowledge afterwards." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=896s) · Latent Space
  > "You'll know if you've succeeded because the tests will pass." — [github/total-typescript-book-010/README.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/README.md)
  > "it's something that I've found just works again and again and again every time I've put it in a course." — [blog/workshops__before-we-start-pxqjv__how-to-do-skill-building-exercises-5s570.md](https://www.aihero.dev/workshops/before-we-start-pxqjv/how-to-do-skill-building-exercises-5s570) · n.d.

He tried AI-native formats and found they cost him learners.
  > "the more I lean into the kind of AI experimental stuff, the more it actually turns people off my materials." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=848s) · Latent Space

### 6. One thing per lesson, in dependency order, at the learner's edge

He turns a graph of knowledge into a linear path, pitched where the learner is challenged but not intimidated; the skill is knowing what learners don't know.
  > "each lesson should only teach one thing, each lesson should depend and the dependencies between all the knowledge should be super clear, and you should always challenge people without overwhelming them." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=762s) · Latent Space
  > "teach someone in the area where they are perfectly challenged but not intimidated." — [youtube/2026-06-08_s5T5oQJcJ6U_learn-anything-with-the-teach-skill.md](https://www.youtube.com/watch?v=s5T5oQJcJ6U&t=442s) · 2026-06
  > "1. Turn the information into a DAG 2. Assign groups to areas of the graph 3. Figure out a linear way through those groups" — [x/2022-11.md](https://x.com/mattpocockuk/status/1590313564992339969) · 2022-11
  > "the useful thing when you're a teacher is not knowing the thing. It's knowing what learners don't know." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=781s) · tldraw

He applies rule 2 to learners too.
  > "One thing I find really important whenever you're teaching anything is to develop a feedback loop" — [youtube/2026-06-08_s5T5oQJcJ6U_learn-anything-with-the-teach-skill.md](https://www.youtube.com/watch?v=s5T5oQJcJ6U&t=234s) · 2026-06

### 7. Teach what has always worked; don't predict

He positions himself as a teacher, not a pundit, and bets on techniques with a long track record.
  > "I don't want to be a pundit. I don't want to make hot takes. I don't know the future. I just want to teach you useful skills to get you paid." — [x/2024-12.md](https://x.com/mattpocockuk/status/1866798098204316106) · 2024-12
  > "if I do stuff that's always worked, then it will probably continue to work in the future." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1887s) · David Ondrej
  > "I am a teacher. I am not a pundit." — [youtube/2026-05-13_lNOQaakmyDU_anthropic-s-dedicated-monthly-credit-is.md](https://www.youtube.com/watch?v=lNOQaakmyDU&t=578s) · 2026-05

He is open that content is also a game he plays.
  > "it's also a playbook in some sense. I'm also sort of playing the game." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=1094s) · tldraw

## Related

- [Alignment before code](principles/alignment-before-code.md) · [Grilling](methods/grilling.md)
- [Feedback is the speed limit](principles/feedback-is-the-speed-limit.md) · [Deterministic over probabilistic](principles/deterministic-over-probabilistic.md) · [TDD at agreed seams](methods/tdd-at-agreed-seams.md)
- [Context is a scarce budget](principles/context-is-a-scarce-budget.md) · [Less is more](principles/less-is-more.md)
- [Deep modules](methods/deep-modules.md)
- [Problem/solution teaching](methods/problem-solution-teaching.md) · [Learning at the edge](principles/learning-at-the-edge.md) · [Teacher, not pundit](principles/teacher-not-pundit.md)
