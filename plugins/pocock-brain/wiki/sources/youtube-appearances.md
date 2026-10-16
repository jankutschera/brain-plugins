---
type: source
raw: raw/youtube-appearances/
files: 51
words: 310752
date_range: unknown – unknown (upload dates not captured; content spans roughly 2022 to 2026)
---
# YouTube appearances (other people's channels)

## Coverage

- 51 transcripts of Matt on channels other than @mattpocockuk: conference talks, podcasts, interviews, livestreams and employer tutorials. Fetched 2026-10-06 via the Apify actor `johnvc/YoutubeTranscripts`; discovery was web search plus channel listings. Each `.md` has a `.segments.json` twin; `MANIFEST.md` and `candidates.json` record method, evidence and 25 rejected candidates.
- Size is 310,752 words (wc -w over the 51 `.md` files, headers included).
- `upload_date` is `unknown` for every file, so dates here are inferred from content: Stately-era streams (2022), Vercel-era streams (2022), Total TypeScript podcasts (2023-24), AI Hero era (2025-26).
- By type: 13 podcasts/interviews (Pragmatic Engineer, ConTejas Code, Backend Banter, Unhandled Exception, David Ondrej, Latent Space, Sanity Code & Content, This Dot Just Ship It, VS Code Developer's Journey, The Next New Thing, Whiskey Web and Whatnot, PodRocket, Laracasts Running Clock), 1 panel (Callstack), 8 talks (four AI Engineer talks/workshops incl. a 17k-word workshop, React Universe, React Day Berlin, VS Code Day, a tldraw meetup), 13 streams (Learn with Jason, JavaScript Jabber, Kelvin Omereshone, two VS Code streams, three Infinite Red segments, five Michigan TypeScript type challenges), the Maintain podcast, 2 OfferZen documentary items and 1 short clip, plus 12 Stately tutorials (type `other`, employer work content, low weight).
- Captions are mostly auto-generated with no speaker labels and frequent mishearings ("Matt PCO", "Versel", "claw code", "touch script"). Only spans clearly spoken by Matt are quoted. The Learn with Jason transcript has JASON:/MATT: labels.
- Multi-speaker items where Matt is a minor voice (the Maintain podcast with Sebastian Silbermann, the Michigan TypeScript challenges, the TypeScript Origins documentary) yielded only a few quotes; most turns there are hosts or co-guests.
- Extraction depth: every podcast, interview, talk and the AI Engineer workshop were read in full, as were the Learn with Jason, JavaScript Jabber and Kelvin streams. The two VS Code streams, the Infinite Red session, the Michigan TypeScript challenges and the Stately tutorials were skimmed (openings, closings and keyword searches) because they are mostly live coding.
- Not complete: per the manifest, audio-only appearances (JS Jabber 538/660, PodRocket Zod, DejaVue, egghead, Epic Web) and gitnation-hosted talks are out of scope.

## What this source shows about him

- He frames his whole career around teaching: teacher first, developer second, and now "a teacher who teaches AI".
  > "I have been a teacher for a lot longer than I have been a Dev." — [youtube-appearances/unknown_xk_PbxR7G8A_advanced-typescript-let-s-learn-generics.md](https://www.youtube.com/watch?v=xk_PbxR7G8A&t=64s) · CodeTV
  > "My name's Matt, I'm a teacher, and I suppose now I teach AI." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=28s) · AI Engineer
- He credits his voice-coach years for an "unfair" advantage: he could explain technical things before he knew many.
  > "I had this bizarre ability of having zero technical knowledge or very little" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=448s) · The Pragmatic Engineer
  > "the ability to communicate always just felt like a ridiculous overpowered skill that I had in my locker that no one else had." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=647s) · Latent Space
- His big thesis for the AI era is that software fundamentals matter more than ever, and he finds them in decades-old books.
  > "I believe that software fundamentals matter now more than they actually ever have." — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=31s) · AI Engineer
  > "these books, 20-year-old books, have already done that. And it's an absolute gold mine if you want to throw that into prompts." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=2789s) · AI Engineer
- He splits work into tactical and strategic programming and puts humans in charge of strategy.
  > "AI has largely eaten tactical programming in my view and it's up to us to handle the strategic" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=1623s) · The Pragmatic Engineer
- He insists on staying in control of agents and of his own thinking.
  > "I don't want to delegate my thinking to the model." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=1188s) · David Ondrej
- Alignment before implementation is his core move, built on Brooks's design concept.
  > "Frederick Brooks calls this the design concept, the design concept that you have with the AI. Once that's clear in your head, then it's trivial for the AI to implement it" — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=617s) · Unhandled Exception Podcast
- As a teacher he values knowing what learners don't know over expertise.
  > "the useful thing when you're a teacher is not knowing the thing. It's knowing what learners don't know." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=781s) · tldraw
- He is a pragmatist about TypeScript: simpler code beats cleverer types.
  > "we're not in the business of writing complicated types, we're in the business of serving users, right?" — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=2702s) · Tejas Kumar
- He sees TypeScript as an IDE booster more than a safety net.
  > "I think the most common misconception is that it's type safe." — [youtube-appearances/unknown_rBzlUjfqWko_no-typescript-regrets-running-clock-with.md](https://www.youtube.com/watch?v=rBzlUjfqWko&t=75s) · Laracasts
- He optimizes his life for leverage and family, not hustle.
  > "my goal in hustling, I suppose, was never to work more, it's always to work less." — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=4672s) · Tejas Kumar
- He refuses to be a pundit and teaches only what works now.
  > "I am in the teaching game I'm not in the punditry game in the prediction game and that's where I want to stay because I think predicting the future is a fool's game" — [youtube-appearances/unknown_DCfn1UlSZzs_ai-in-practice-from-cloud-privacy.md](https://www.youtube.com/watch?v=DCfn1UlSZzs&t=149s) · Callstack
- He is candid about business numbers and about decline.
  > "made $3.5 million right over the course of like two and a bit years." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=110s) · tldraw
  > "So in terms of like my revenue from total time script that's gone down obviously" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=1502s) · The Pragmatic Engineer
- He openly treats content as both craft and playbook.
  > "it's also a playbook in some sense. I'm also sort of playing the game." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=1094s) · tldraw
- He credits luck and refuses a hero narrative.
  > "I try not to narrativize it." — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=5298s) · The Pragmatic Engineer

## Notable pieces

- **The Pragmatic Engineer, "AI Skills with Matt Pocock"**: the fullest career narrative (voice coach to Stately to Vercel to Total TypeScript to skills) plus his AI workflow, the knowledge/wisdom split and the Pragmatic Programmer discovery.
  > "knowledge is now very cheap to acquire right very very cheap you can just look it up" — [youtube-appearances/unknown_4DhcSPkEbwI_ai-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=4DhcSPkEbwI&t=1480s) · The Pragmatic Engineer
- **ConTejas Code (Tejas Kumar)**: the most personal interview: three self-employed singing businesses, imposter syndrome as fuel, the "five Cs", the newborn and the sense that the TypeScript wave had crashed.
  > "if you have that fear of not being good enough or not being worthy of being in the room that you're in, turn that into hunger." — [youtube-appearances/unknown_nFA2oO0IPQs_matt-pocock-how-to-maximize-success.md](https://www.youtube.com/watch?v=nFA2oO0IPQs&t=5662s) · Tejas Kumar
- **tldraw meetup, "good content for developers but how"**: his explicit content philosophy (sugar vs vegetables, exploding brain, help people where they are, quantity game) and the $3.5M figure.
  > "developers love sugar, but they will pay for vegetables." — [youtube-appearances/unknown_CLw3Oj13_bA_matt-pocock-good-content-for-developers.md](https://www.youtube.com/watch?v=CLw3Oj13_bA&t=632s) · tldraw
- **Sanity Code & Content**: process obsession, cutting review cycles, "does number go up", the confusions folder and the trained voice behind his improvisation.
  > "the longer you spend on a piece of content, the more risk is inherent in the content, you know?" — [youtube-appearances/unknown_hQDSr7uwu6E_the-future-of-developer-content-matt.md](https://www.youtube.com/watch?v=hQDSr7uwu6E&t=509s) · Sanity
- **AI Engineer talk, "Software Fundamentals Matter More Than Ever"**: the compact statement of his AI thesis; specs-to-code rejected; design the interface, delegate the implementation.
  > "Design the interface, delegate the implementation." — [youtube-appearances/unknown_v4F1gFy-hqg_software-fundamentals-matter-more-than-ever.md](https://www.youtube.com/watch?v=v4F1gFy-hqg&t=986s) · AI Engineer
- **AI Engineer workshop, "Full Walkthrough: Workflow for AI Coding"**: the whole method end to end (smart zone, grill me, PRD, Kanban, AFK Ralph loop, TDD, deep modules, push/pull standards) and his live teaching style.
  > "QA is how I then um impose my uh opinions back onto the code base, how I impose my taste." — [youtube-appearances/unknown_-QFHIoCo-Ko_full-walkthrough-workflow-for-ai-coding.md](https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=4367s) · AI Engineer
- **AI Engineer talk, "Building Great Agent Skills: The Missing Manual"**: his rubric for skills (trigger, structure, steering, pruning) and why he prefers user-invoked skills.
  > "Superpowers is primarily model invoked skills. It gives the agent superpowers. Whereas my skills, I much prefer to be in full control." — [youtube-appearances/unknown_UNzCG3lw6O0_building-great-agent-skills-the-missing.md](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=370s) · AI Engineer
- **AI Engineer talk, "Fixing the PR Bottleneck"**: implement vs review split, coding standards in the reviewer, one-way/two-way doors, reviewing the system.
  > "when you do a human review, you're not just reviewing the code, you're reviewing the system that creates it." — [youtube-appearances/unknown_LlgiOCmFG_w_fixing-the-pr-bottleneck-matt-pocock.md](https://www.youtube.com/watch?v=LlgiOCmFG_w&t=1215s) · AI Engineer
- **David Ondrej interview**: harness over model, queues not loops, skills as procedures vs abilities, "your skills are the ceiling".
  > "your skills are the ceiling on what AI can do." — [youtube-appearances/unknown_nQwJVHCtDDY_matt-pocock-s-agentic-engineering-workflow.md](https://www.youtube.com/watch?v=nQwJVHCtDDY&t=253s) · David Ondrej
- **Unhandled Exception podcast**: "asset rush", specs as temporary artifacts, one developer owning a whole spec, his audience-ingest wiki.
  > "A single developer should own an entire spec." — [youtube-appearances/unknown_d_BuVJgadxs_agent-skills-with-matt-pocock.md](https://www.youtube.com/watch?v=d_BuVJgadxs&t=2068s) · Unhandled Exception Podcast
- **Backend Banter**: communication as what makes great programmers, the interfaces-first reversal, and his view that AI means fewer dev jobs.
  > "you're never going to be a great program I think unless you can communicate your intent to the rest of the team" — [youtube-appearances/unknown_x18rpm3zGEE_i-quit-voice-coaching-for-typescript.md](https://www.youtube.com/watch?v=x18rpm3zGEE&t=280s) · Backend Banter
- **VS Code "The Developer's Journey"**: imposter syndrome, self-promotion, job hopping for pay, and the UTC bug that taught him care.
  > "you're often not going to be given a pay rise inside your own company. You're going to be able to get more money elsewhere" — [youtube-appearances/unknown_kJD_1tb6-NE_imposter-syndrome-is-lying-to-you.md](https://www.youtube.com/watch?v=kJD_1tb6-NE&t=567s) · Visual Studio Code
- **This Dot "Just Ship It"**: the Total TypeScript origin (18 videos on a Sunday, the Budapest message to Joel) and his advanced-TypeScript USP.
  > "I just sat down and recorded 18 two-minute videos on a Sunday and I just like uh, queued them up and I went from 4,000 to 10,000 followers on Twitter." — [youtube-appearances/unknown_8eoiDcVGo80_get-100k-followers-by-teaching-typescript.md](https://www.youtube.com/watch?v=8eoiDcVGo80&t=555s) · This Dot Media
- **JavaScript Jabber**: TypeScript migration method, three levels of TypeScript wizardry, and how lacking a CS background helps him teach.
  > "not having the curse of knowledge has benefited me in weird ways too making me closer to my Learners" — [youtube-appearances/unknown_5ROCO6Bbdv0_typescript-with-matt-pocock.md](https://www.youtube.com/watch?v=5ROCO6Bbdv0&t=841s) · Top End Devs
- **PodRocket (Stately era)**: his XState conversion story and state-chart enthusiasm before the AI-era retreat.
  > "I think it comes from just fury and terror at the code tools and just I think you ship one too many bugs, and you realize there must be a better way." — [youtube-appearances/unknown_uLD6yQTs_pE_xstate-and-stately-with-matt-pocock.md](https://www.youtube.com/watch?v=uLD6yQTs_pE&t=769s) · LogRocket

## Related

- Principles: [Teacher, not pundit](../principles/teacher-not-pundit.md) · [Learning at the edge](../principles/learning-at-the-edge.md) · [The codebase is the agent's environment](../principles/the-codebase-is-the-agents-environment.md) · [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md) · [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md) · [Alignment before code](../principles/alignment-before-code.md) · [Communication and shared language](../principles/communication-and-shared-language.md) · [Humans own the strategy](../principles/humans-own-the-strategy.md) · [Fundamentals matter more with AI](../principles/fundamentals-matter-more-with-ai.md) · [Context is a scarce budget](../principles/context-is-a-scarce-budget.md) · [Code is cheap; maintenance is not](../principles/code-is-cheap-maintenance-is-not.md) · [Own the process](../principles/own-the-process.md) · [Revise in public](../principles/revise-in-public.md) · [Deterministic over probabilistic](../principles/deterministic-over-probabilistic.md) · [Less is more](../principles/less-is-more.md)
- Methods: [Content strategy](../methods/content-strategy.md) · [Running the business](../methods/running-the-business.md) · [Review and retro](../methods/review-and-retro.md) · [Writing for agents](../methods/writing-for-agents.md) · [Content production](../methods/content-production.md) · [Problem/solution teaching](../methods/problem-solution-teaching.md) · [Grilling](../methods/grilling.md) · [The main flow](../methods/the-main-flow.md) · [AFK loops](../methods/afk-loops.md) · [Deep modules](../methods/deep-modules.md) · [Build your own tools](../methods/build-your-own-tools.md) · [Prototype to answer a question](../methods/prototype-to-answer-a-question.md) · [Context hygiene](../methods/context-hygiene.md) · [Diagnosing bugs](../methods/diagnosing-bugs.md) · [Evals as tests](../methods/evals-as-tests.md) · [TDD at agreed seams](../methods/tdd-at-agreed-seams.md)
