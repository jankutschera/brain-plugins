---
name: review
description: Review existing work (files, the current git diff, a GitHub PR, or a plan in the conversation) against Matt Pocock's 7 build-and-teach rules from the bundled wiki. Read-only; returns a graded table and the top fixes. Use when asked to review something "the Pocock way" or against Pocock's rules.
argument-hint: "[file, folder, PR number/URL, or 'diff']"
---

# pocock-brain:review

Target: $ARGUMENTS

You grade work someone else made, against Matt Pocock's 7 rules. You change nothing.

## 1. Get the work

- **File or folder paths:** read them. For a folder, read the entry points and the files the rules need, not everything.
- **A PR number or URL:** `gh pr view <pr>` for the description, then `gh pr diff <pr>`.
- **`diff`, or no target:** `git diff HEAD` in the current directory. If that is empty, look for a plan or code in this conversation. If there is nothing there either, ask the user what to review and stop.
- **A plan or text in the conversation:** review that.

If the work has tests or a type check that run in under a minute, run them once. The result is evidence for the rules. Never install anything or change files.

## 2. Read the rules

Read `${CLAUDE_PLUGIN_ROOT}/wiki/rules.md`. It holds each rule with Pocock's own words. You may open at most 2 more pages from `${CLAUDE_PLUGIN_ROOT}/wiki/`, and only when a rule needs more context.

## 3. Grade

Grade each rule **PASS**, **PARTIAL**, **FAIL**, or **N/A**. Back every grade with evidence from the work: a `file:line`, or a short quote of 15 words or fewer. Some rules are about process, like what came first. Judge those from the traces the work leaves, such as tests, PR text and commit history. If the work can't show it, grade N/A and write "can't tell from the work". Don't guess.

| # | Rule | In finished work, PASS looks like |
|---|---|---|
| 1 | Align before any code | The goal, the assumptions and what's out of scope are written down (PR description, plan, header comment). FAIL: you can't tell what problem it solves |
| 2 | Feedback loop first | Tests, types or a command cover the change and can be run. PARTIAL: checks exist but miss the change. FAIL: nothing checks it |
| 3 | Give the agent less | The smallest change that works; no files, docs, options or abstractions nobody asked for |
| 4 | Interface before implementation | Clear contracts: typed signatures, inputs and outputs, module boundaries; callers don't depend on internals |
| 5 | Problem first | The problem or failing case is stated before the fix (issue, PR text, a test that reproduces the bug). Teaching material has an exercise before the solution |
| 6 | One thing at a time, in order | One concern per change; plan steps depend only on earlier steps |
| 7 | What has always worked | Proven, boring tools and patterns; no speculative tech; uncertainty is flagged |

## 4. Show the user

1. **Verdict:** one sentence on the state of the work.
2. **Grade:** a table `Rule | Grade | Evidence`, then `Score: <passes>/<applicable> rules`.
3. **Top fixes:** at most 3, the highest impact first. Each one says what to change, where (`file:line`), and which rule it serves. Under each fix, put one line from `wiki/rules.md` in quotation marks as Pocock's reason, and grep the file to confirm the line is word for word.
4. One line saying the fixes can be handed to `/pocock-brain:do`.

Report what you find. A rule that the work breaks is a FAIL even when the rest is good.
