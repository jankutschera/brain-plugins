# Log

## [2026-10-07] ingest | blog
- Read `build/candidates/blog.md` (293 candidate quotes) and `sources/blog.md` (30 quotes) for raw/blog/ (265 files, aihero.dev, 2024-11 to 2026-10).
- 102 quotes from 62 blog files now support principle and method pages. Skill doc pages from 2026-07 onward are used as supporting evidence only and are marked "(skill doc)" where they carry a claim alone.

## [2026-10-07] ingest | github
- Read `build/candidates/github.md` (317 candidate quotes) and `sources/github.md` (26 quotes) for raw/github/ (168 repos, 84 gists).
- 93 quotes from 35 files in synthesis pages. Book quotes inside his READMEs (Pragmatic Programmer, Ousterhout, Kent Beck) and agent-written `rubix-cube/NOTES.md` are not used as his words.

## [2026-10-07] ingest | youtube
- Read `build/candidates/youtube.md` (313 candidate quotes) and `sources/youtube.md` (27 quotes) for raw/youtube/ (298 auto-caption transcripts, 2020-11 to 2026-10).
- 137 quotes from 56 transcripts in synthesis pages; caption mishearings kept verbatim.

## [2026-10-07] ingest | youtube-appearances
- Read `build/candidates/youtube-appearances.md` (905 candidate quotes incl. the per-transcript appendix) and `sources/youtube-appearances.md` (33 quotes) for 51 transcripts on other channels.
- 180 quotes from 22 transcripts in synthesis pages, Matt's turns only. The 12 Stately tutorials and the Michigan TypeScript and Maintain items contributed nothing.

## [2026-10-07] ingest | x
- Read `build/candidates/x.md` (344 candidate quotes) and `sources/x.md` (28 quotes) for raw/x/ (35,859 posts, 2016-03 to 2026-10).
- 147 quotes from 34 monthly files in synthesis pages. No retweets, no quoted-tweet text, and not the 2023-04-01 April Fools' post.

## [2026-10-07] synthesis | principles + methods + hot
- Wrote 16 principle pages and 16 method pages (15 to 25 quotes each, 649 in total), clustered across sources; dated reversals go under "Tensions and evolution".
- Wrote `hot.md` (390 words, 10 quotes) and `index.md`; added a `## Related` section to each source page.
- Quotes were inserted mechanically from the verified candidate and source pages by a scratch expander script, never retyped.

## [2026-10-07] lint | check_wiki.py
- `python3 tools/check_wiki.py wiki` exit 0: `pages: 40  quotes checked: 803  errors: 0  warnings: 1` (the one warning is the hot.md word-count report, 390 < 500; no orphans).
- `shasum -a 256 -c build/raw.sha256 --quiet` printed nothing: raw/ untouched.

## [2026-10-07] query | Rules for how he builds and how he teaches
- Filed as `rules.md`: 7 rules (4 build, 3 teach), each stated in 3–5 different raw source folders. 34 quotes, including dated caveats where his view moved.
- Selected from the principle and method pages. A rule was kept only if it appears in at least 2 different sources and he states it directly.
- `python3 tools/check_wiki.py wiki` exit 0: `pages: 41  quotes checked: 837  errors: 0`.

## [2026-10-07] migrate | moved into ~/knowledge/people/matt-pocock
- Wiki moved from `~/dev/research/pocock-brain/wiki/` to `~/knowledge/people/matt-pocock/`. Raw moved to `~/dev/research/brains/matt-pocock/raw/` (outside the vault), with all checksums verified before and after.
- All 837 citations now link to the public source (X posts, YouTube with a `&t=` timestamp, aihero.dev pages, GitHub files and gists) via `link_citations.py`. The label stays the raw path.
- Schema moved to `~/knowledge/people/CLAUDE.md`. Tools moved to `~/.claude/skills/brain/scripts/`.
