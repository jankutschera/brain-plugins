---
name: review
description: Review existing work (files, the current git diff, a GitHub PR, or a plan in the conversation) against Andrej Karpathy's 7 build-and-teach rules from the bundled wiki. Read-only; returns a graded table and the top fixes. Use when asked to review something "the Karpathy way" or against Karpathy's rules.
argument-hint: "[file, folder, PR number/URL, or 'diff']"
---

# karpathy-brain:review

Target: $ARGUMENTS

You grade work someone else made, against Andrej Karpathy's 7 rules. You change nothing.

## 1. Get the work

- **File or folder paths:** read them. For a folder, read the entry points and the files the rules need, not everything.
- **A PR number or URL:** `gh pr view <pr>` for the description, then `gh pr diff <pr>`.
- **`diff`, or no target:** `git diff HEAD` in the current directory. If that is empty, look for a plan or code in this conversation. If there is nothing there either, ask the user what to review and stop.
- **A plan or text in the conversation:** review that.

If the work has tests or a type check that run in under a minute, run them once. The result is evidence for the rules. Never install anything or change files.

## 2. Read the rules

Read `${CLAUDE_PLUGIN_ROOT}/wiki/rules.md`. It holds each rule with Karpathy's own words. You may open at most 2 more pages from `${CLAUDE_PLUGIN_ROOT}/wiki/`, and only when a rule needs more context.

## 3. Grade

Grade each rule **PASS**, **PARTIAL**, **FAIL**, or **N/A**. Back every grade with evidence from the work: a `file:line`, or a short quote of 15 words or fewer. Some rules are about process, like what came first. Judge those from the traces the work leaves, such as tests, PR text and commit history. If the work can't show it, grade N/A and write "can't tell from the work". Don't guess.

| # | Rule | In finished work, PASS looks like |
|---|---|---|
| 1 | Rebuild to understand | Relies only on things it shows it understands: no pasted code it doesn't explain, no library call whose behaviour is assumed, and comments that match what the code does |
| 2 | Data and expected number | Checks name concrete expected values (asserts with numbers, sanity checks on real inputs, shapes or counts). FAIL: nothing checks a real output |
| 3 | Build up from trust | There is a simple baseline or reference the work is checked against, and the change builds on it in steps (commit history, if you can see it) |
| 4 | Complexity earns its place | No file, dependency, abstraction or option that doesn't pay for itself; what was left out is said |
| 5 | Small diffs, owned | The change is small and focused, and every "works" claim (PR text, comments, docs) is backed by a check that can run |
| 6 | Smallest complete version | Docs, examples and explanations are minimal, complete and runnable. N/A when the work explains nothing |
| 7 | Build the ramp | Explanations are ordered so each step needs only earlier ones; teaching material has an exercise before the answer. N/A when the work explains nothing |

## 4. Show the user

1. **Verdict:** one sentence on the state of the work.
2. **Grade:** a table `Rule | Grade | Evidence`, then `Score: <passes>/<applicable> rules`.
3. **Top fixes:** at most 3, the highest impact first. Each one says what to change, where (`file:line`), and which rule it serves. Under each fix, put one line from `wiki/rules.md` in quotation marks as Karpathy's reason, and grep the file to confirm the line is word for word.
4. One line saying the fixes can be handed to `/karpathy-brain:do`.

Report what you find. A rule that the work breaks is a FAIL even when the rest is good.
