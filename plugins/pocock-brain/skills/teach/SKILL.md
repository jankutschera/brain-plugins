---
name: teach
description: Hand a task to the pocock subagent (Matt Pocock's seven build-and-teach rules from the bundled wiki), grade its answer against the rules, and show the answer with the grade.
argument-hint: "[task]"
disable-model-invocation: true
---

# pocock-brain:teach

Task: $ARGUMENTS

If the task is empty, ask the user for it and stop.

## 1. Delegate

Launch the `pocock-brain:pocock` subagent with the task verbatim. Add only the context it can't find itself: file paths, decisions the user already made in this conversation. Wait for its result. Show the user nothing yet.

If it returns questions instead of an answer, it is following rule 1. Show the questions, grade only rule 1 as PASS, and stop.

## 2. Grade

Grade the answer against each rule: **PASS**, **PARTIAL**, **FAIL**, or **N/A** (only when the rule can't apply to this task). Back every grade with a short quote from the answer (≤ 15 words) or the missing thing.

| # | Rule | PASS looks like |
|---|---|---|
| 1 | Align before any code | Opens with goal, assumptions and scope; or returns questions with recommended answers on decisions that matter |
| 2 | Feedback loop first | Says how correctness is checked and actually ran it (visible in Ran / Came out). PARTIAL: named a check it couldn't run. FAIL: claims success without any check |
| 3 | Give the agent less | Smallest change that works; no unrequested files, docs or abstractions; reads proportionate to the task |
| 4 | Interface before implementation | Contract, signatures, layout or outline stated before the details |
| 5 | Problem first | The problem or failing case comes before the fix; learning tasks get a try-first exercise and a way to check it |
| 6 | One thing at a time, in order | Steps only depend on earlier steps; one idea per step; pitched at the user's level |
| 7 | What has always worked | Proven approach; no predictions or hype; uncertainty flagged |

Then check the two contract items yourself, with tools rather than by reading:
- **Footer:** the answer ends with **Ran / Came out / Changed**. For every file under **Changed**, confirm it exists, or is gone if deleted (`ls`, `git status`, or `git diff --stat`). For a claimed test or command result, re-run the cheapest one if it takes under a minute.
- **Citations:** every claim about Matt cites a `wiki/<page>.md`, where `wiki/` is shorthand for `${CLAUDE_PLUGIN_ROOT}/wiki/`; that page must exist there. Any text the answer puts in quotation marks as Matt's words must appear verbatim in the cited page: grep for it. A changed word or punctuation mark is a FAIL.

## 3. One revision round

If any rule or contract item is **FAIL**, send the same pocock-brain:pocock agent the failed items and the exact fix for each. If you can't reach the same agent, launch a new one with the task plus the fix list. Then grade again. Never do more than one revision round.

## 4. Show the user

1. The agent's final answer, unedited.
2. **Grade**: a table `Rule | Grade | Evidence` for the seven rules plus Footer and Citations, then a line `Score: <passes>/<applicable> rules`.
3. If there was a revision round, one line on what failed the first time and whether the fix landed.

Report failures as they are. Never upgrade a grade because the answer looks good overall.
