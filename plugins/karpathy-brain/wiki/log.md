# Andrej Karpathy wiki: log

## [2026-10-15] ingest | initial build
- Raw: x (9,426 posts), youtube (15 transcripts), blog (45 posts on 3 sites), github (54 repos, 13 gists) and youtube-appearances (22 transcripts), frozen with 11,497 checksums.
- Extraction: 5 agents, one per source, wrote 1,765 verified candidate quotes to `build/candidates/`.
- Synthesis: 16 principles, 22 methods (9 on teaching) and 5 source pages, written by 5 agents from `build/plan.md`. Then `hot.md` and `index.md`.
- `link_citations.py` linked every quote to its public URL: X post, YouTube with timestamp, blog post, or GitHub at the cloned SHA. There were no file:// fallbacks.
- YouTube dates were corrected to exact months from the channel RSS (`build/youtube_exact_dates.json`); the listing gives only approximate dates.

## [2026-10-15] lint | claim check
- 5 fresh agents checked every claim against the raw context around its quote. Reports are in `build/claim_check/{a..e}.md`.
- They found 64 claims stronger than their quote (A 19, B 16, C 14, D 6, E 9). The writers fixed all of them by rewording, swapping in a better verbatim quote, or deleting.
- Speaker problems: "If I can't build it, I don't understand it" is a Feynman line he credits; it is now kept only with that credit. 25 quotes from the LLM-cleaned Sequoia post were swapped for the spoken transcript (96jN2OCOfLs). One Autonomy Day line with an unclear speaker was removed.
- Dates: nanochat log entries now carry their own entry dates, and the nanoGPT and minGPT README lines have their correct months. All 300 youtube-appearances quote lines were redated from `build/appearance_dates.json` (yt-dlp upload dates; the event date where the title or talk states one: FSDL 2018-08, CS25 2023-01).

## [2026-10-15] query | rules
- `rules.md`: 7 active rules, each with quotes from 3–5 source folders, plus 4 bench rules with one source each.
- `check_wiki.py`: 47 pages, 1,430 quotes, 0 errors.

## [2026-10-16] ingest | X post 2109361546505966046: the widening LLM capability gap
- Label: `x/ingest/2026-10-11_2109361546505966046.md` (2026-10-11 quote post of the April 2026 gap post). 18 verified candidates in `build/candidates/ingest_x-2109361546505966046.md`.
- New page: `principles/capability-gap.md` (x + youtube).
- Evidence added: `verifiability-drives-progress` (revenue as a driver of jaggedness), `ambition-and-agency` (impact scales with problem size). Dated evolution lines: `ai-assisted-coding`, `understanding-cannot-be-outsourced`. `sources/x.md`: notable piece and ingest note.
- Rules: no bench rule promoted, no active rule changed. One new bench rule: bring frontier models big, hard problems.
- Claim check (separate agent): 19 claims, 3 support problems on `principles/capability-gap.md`, all fixed (statement reworded around the funnel, lab-review line corrected to the narrow end, October quote swapped). Report: `build/ingest/x-2109361546505966046_claimcheck.md`.
