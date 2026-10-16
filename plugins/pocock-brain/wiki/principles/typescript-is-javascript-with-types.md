---
type: principle
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 22
first_seen: 2022-11
last_seen: 2026-01
---
# TypeScript is JavaScript with types

TypeScript exists to make tooling better, so it should stay a thin, visible layer over JavaScript: infer where possible, avoid TS-only runtime features, and be pragmatic rather than clever with types.
  > "TypeScript exists to make your tooling better. Turns out, types were needed to make that happen." — [x/2023-01.md](https://x.com/mattpocockuk/status/1616008761155489793) · 2023-01

## Evidence

- His book frames the language as "JavaScript with types".
  > "The right way to think about TypeScript today is as "JavaScript with types"." — [github/total-typescript-book-010/book-content/chapters/09-typescript-only-features.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/book-content/chapters/09-typescript-only-features.md)
- He defines TypeScript by the IDE, not by safety.
  > "I think the best answer for what is TypeScript is that it's a way of making your IDE, your integrated development environments, whether that's VS code, whether that's NeoVim, whatever you're using, more powerful." — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=332s) · Tejas Kumar
  > "I think the most common misconception is that it's type safe." — [youtube-appearances/unknown_rBzlUjfqWko_no-typescript-regrets-running-clock-with.md](https://www.youtube.com/watch?v=rBzlUjfqWko&t=75s) · Laracasts
- TS-only runtime features feel wrong to him.
  > "anything that does like typescript stuff at runtime is odd to me" — [youtube/2025-01-24_zeNh4fuJhcA_typescript-shipped-a-flag-to-disable.md](https://www.youtube.com/watch?v=zeNh4fuJhcA&t=104s) · 2025-01
  > "I like my TypeScript to be just JavaScript with types. Enums feel like they break that rule." — [x/2024-08.md](https://x.com/mattpocockuk/status/1823644498733187492) · 2024-08
- Inference first in application code.
  > "When writing application-level TypeScript, you should be using inference as much as possible." — [x/2023-01.md](https://x.com/mattpocockuk/status/1615688975225683969) · 2023-01
- Types serve users, not the other way round.
  > "we're not in the business of writing complicated types, we're in the business of serving users, right?" — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=2702s) · Tejas Kumar
- Type errors are communication; suppressing them borrows time.
  > "The time you save by suppressing errors will, eventually, come back to bite you. You're not saving time, but borrowing it." — [github/total-typescript-book-010/book-content/chapters/11-annotations-and-assertions.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/book-content/chapters/11-annotations-and-assertions.md)

## How it shows up

- He simplifies the JavaScript instead of fighting the types.
  > "I think complex TypeScript comes from complex JavaScript, because TypeScript is just an effort to describe JavaScript." — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=2662s) · Tejas Kumar
- He derives types from runtime values rather than redeclaring them.
  > "instead of taking a type and putting it into the runtime you should be thinking how do I take the runtime and turn it into a type" — [youtube-appearances/unknown_5ROCO6Bbdv0_typescript-with-matt-pocock.md](https://www.youtube.com/watch?v=5ROCO6Bbdv0&t=4684s) · Top End Devs
- He keeps types loose unless looseness would cause a real bug.
  > "Unless it's going to cause a real bug, if it's wrong, I like to just keep it relatively loose." — [youtube-appearances/unknown_rBzlUjfqWko_no-typescript-regrets-running-clock-with.md](https://www.youtube.com/watch?v=rBzlUjfqWko&t=249s) · Laracasts
- In his own code `any` is a defect with a contained exception; `unknown` plus narrowing is the honest version.
  > "An `any` switches the type checker off for every value that flows through it, and those values keep flowing long after the line that produced them." — [github/course-video-manager/CODING_STANDARDS.md](https://github.com/mattpocock/course-video-manager/blob/HEAD/CODING_STANDARDS.md)
  > "as long as the outside of your function is properly typed it's kind of fine if you're just using any inside it" — [youtube-appearances/unknown_8bOBE655gRQ_typescript-react-and-api-issues-with.md](https://www.youtube.com/watch?v=8bOBE655gRQ&t=1682s) · Whiskey Web and Whatnot
- He pitches TypeScript to agents as free feedback.
  > "is essentially free feedback for your AI. Use it over JavaScript." — [blog/essential-ai-coding-feedback-loops-for-type-script-projects.md](https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects) · 2026-01

## Tensions and evolution

- Types vs interfaces flipped repeatedly: types (2022), interfaces (2025), then indifference.
  > "My old opinion: Prefer interface over type where possible My recent opinion: Doesn't matter, as long as you stay consistent My new opinion: Prefer type unless you need a specific feature of interfaces" — [x/2022-11.md](https://x.com/mattpocockuk/status/1597563037892116480) · 2022-11
  > "I think my new recommendation is default to interface until you need a feature of types." — [youtube/2025-04-18_e0AIkYrXAYE_types-vs-interfaces-what-i-got.md](https://www.youtube.com/watch?v=e0AIkYrXAYE&t=524s) · 2025-04
  > "But overall, I couldn't care less" — [x/2025-12.md](https://x.com/mattpocockuk/status/2002819576892203180) · 2025-12
- Enums: an absolute "never" in a draft article, softened to a personal preference in the book.
  > "Spoiler alert: it's 'never'." — [github/total-typescript-monorepo/apps/written-content/_old/articles/enums-considered-harmful.md](https://github.com/mattpocock/total-typescript-monorepo/blob/HEAD/apps/written-content/_old/articles/enums-considered-harmful.md)
  > "However, this is my personal preference." — [github/total-typescript-book-010/book-content/chapters/09-typescript-only-features.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/book-content/chapters/09-typescript-only-features.md)
- By 2026 he wondered whether the JS vs TS debate still matters with agents.
  > "Or is JS vs TS now a dead debate?" — [x/2026-01.md](https://x.com/mattpocockuk/status/2013922977486631419) · 2026-01
- He predicts TS files may eventually give way to types in JavaScript.
  > "the days of writing TS files might be numbered. It's a big number, but they might be numbered." — [youtube-appearances/unknown_U6s2pdxebSo_typescript-origins-the-documentary.md](https://www.youtube.com/watch?v=U6s2pdxebSo&t=4368s) · OfferZen Origins

## Related

- [Feedback is the speed limit](feedback-is-the-speed-limit.md)
- [Revise in public](revise-in-public.md)
- [Problem/solution teaching](../methods/problem-solution-teaching.md)
- [Build your own tools](../methods/build-your-own-tools.md)
