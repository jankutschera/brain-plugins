---
name: do
description: Hand a task to the karpathy subagent (Andrej Karpathy's 7 build-and-teach rules from the bundled wiki), grade its answer against the rules, and show the answer with the grade.
argument-hint: "[task]"
disable-model-invocation: true
---

# karpathy-brain:do

Task: $ARGUMENTS

If the task is empty, ask the user for it and stop.

## 1. Delegate

Launch the `karpathy-brain:karpathy` subagent with the task verbatim. Add only the context it can't find for itself, such as file paths or decisions the user already made in this conversation. Wait for its result, and show the user nothing yet.

## 2. Grade

Grade the answer against each rule: **PASS**, **PARTIAL**, **FAIL**, or **N/A** (only when the rule can't apply to this task). Back every grade with a short quote from the answer (15 words or fewer), or name the thing that is missing.

| # | Rule | PASS looks like |
|---|---|---|
| 1 | Rebuild to understand | Reads or reproduces the core of anything it relies on; no claims about code or APIs it didn't look at. FAIL: explains behaviour it never checked |
| 2 | Data and expected number | States the expected output before running, then compares (visible in Ran / Came out). PARTIAL: ran a check but predicted nothing. FAIL: no check |
| 3 | Build up from trust | Starts from the simplest working version or a reference, then adds one change at a time with a check after each |
| 4 | Complexity earns its place | Smallest change that works; no unrequested files, dependencies or abstractions; says what was left out |
| 5 | Small diffs, owned | One small, concrete change at a time; every claim of "works" is backed by a run. FAIL: says it works without running it |
| 6 | Smallest complete version | Explanations come as a minimal, complete, runnable example built step by step. N/A when nothing is explained |
| 7 | Build the ramp | Each step needs only the earlier ones; learning tasks get a try-first exercise and a way to check it |

Then check the two contract items yourself, with tools rather than by reading:
- **Footer:** the answer ends with **Ran / Came out / Changed**.
  - For every file under **Changed**, confirm that it exists, or that it is gone if deleted (`ls`, `git status` or `git diff --stat`).
  - For a claimed test or command result, re-run the cheapest one if it takes under a minute.
- **Citations:** every claim about Karpathy cites a `wiki/<page>.md`, and that page must exist.
  - `wiki/` is shorthand for `${CLAUDE_PLUGIN_ROOT}/wiki/`.
  - Any text the answer puts in quotation marks as his words must appear verbatim in the cited page, so grep for it. A changed word or punctuation mark is a FAIL.

## 3. One revision round

If any rule or contract item is **FAIL**, send the same karpathy-brain:karpathy agent the failed items and the exact fix for each. If you can't reach the same agent, launch a new one with the task plus the fix list. Then grade again. Never do more than one revision round.

## 4. Show the user

1. The agent's final answer, unedited.
2. **Grade**: a table `Rule | Grade | Evidence` covering the 7 rules plus Footer and Citations, then a line `Score: <passes>/<applicable> rules`.
3. If there was a revision round, one line on what failed the first time and whether the fix landed.

Report failures as they are. Never upgrade a grade because the answer looks good overall.
