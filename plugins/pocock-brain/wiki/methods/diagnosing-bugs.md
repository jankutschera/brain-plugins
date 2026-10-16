---
type: method
sources: [blog, github, youtube-appearances]
quotes: 15
first_seen: 2026-07
last_seen: 2026-07
---
# Diagnosing bugs

He debugs (and makes agents debug) by building a tight, red-capable feedback loop before forming any theory, then minimising, hypothesising, instrumenting and fixing in gated phases.
  > "**This is the skill.** Everything else is mechanical." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)

## Evidence

- A tight pass/fail signal for this bug means you will find the cause.
  > "If you have a **tight** pass/fail signal for the bug (one that goes red on _this_ bug), you will find the cause" — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- Without a loop, staring at code will not help.
  > "If you don't have one, no amount of staring at code will save you." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- By default an agent reads code and guesses; the skill blocks that.
  > "Given a bug report, a coding agent by default reads code and guesses. This skill blocks that." — [blog/skills-diagnosing-bugs.md](https://www.aihero.dev/skills-diagnosing-bugs) · 2026-07
- A slow or flaky loop is barely better than none.
  > "A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight, a debugging superpower." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)

## How it shows up

1. Build the loop first, ranked from failing test down to a human-in-the-loop script as last resort.
  > "**HITL bash script.** Last resort. If a human must click, drive _them_ with `scripts/hitl-loop.template.sh` so the loop is still structured." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
2. Stop if you catch yourself theorising before the command exists.
  > "If you catch yourself reading code to build a theory before this command exists, **stop: jumping straight to a hypothesis is the exact failure this skill prevents.**" — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
3. Minimise until every remaining element is load-bearing.
  > "Done when **every remaining element is load-bearing**: removing any one of them makes the loop go green." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
4. Generate several ranked, falsifiable hypotheses.
  > "Generate **3–5 ranked hypotheses** before testing any of them. Single-hypothesis generation anchors on the first plausible idea." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
  > "If you cannot state the prediction, the hypothesis is a vibe: discard or sharpen it." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
5. Tag debug logs so cleanup is one grep.
  > "Cleanup at the end becomes a single grep. Untagged logs survive; tagged logs die." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
6. Treat a missing test seam as an architectural finding.
  > "**If no correct seam exists, that itself is the finding.**" — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)
- For flaky bugs, raise the reproduction rate.
  > "A 50%-flake bug is debuggable; 1% is not, so keep raising the rate until it's debuggable." — [github/skills/skills/engineering/diagnosing-bugs/SKILL.md](https://github.com/mattpocock/skills/blob/HEAD/skills/engineering/diagnosing-bugs/SKILL.md)

## Tensions and evolution

- The discipline is old for him: a 2017 UTC bug that frightened a family made him detail-obsessed.
  > "I'm playing with live ammo here, right? Like this is this is real stuff." — [youtube-appearances/unknown_kJD_1tb6-NE_imposter-syndrome-is-lying-to-you.md](https://www.youtube.com/watch?v=kJD_1tb6-NE&t=1708s) · Visual Studio Code
  > "ever since then really I've tried to be as careful as I possibly can be, as detail oriented as I possibly can be" — [youtube-appearances/unknown_kJD_1tb6-NE_imposter-syndrome-is-lying-to-you.md](https://www.youtube.com/watch?v=kJD_1tb6-NE&t=1713s) · Visual Studio Code

## Related

- [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md)
- [TDD at agreed seams](tdd-at-agreed-seams.md)
- [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md)
