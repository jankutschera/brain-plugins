---
type: method
sources: [blog, github, youtube, youtube-appearances, x]
quotes: 18
first_seen: 2022-07
last_seen: 2025-09
---
# Problem/solution teaching

His courses throw learners into a problem first, let them try with the docs, use tests as the success signal, and only then show his solution; lessons teach one thing each, in dependency order.
  > "just like all of my courses this is a practical course where you have a problem that you need to solve you go into an Editor to try and solve it and then you see my solution afterwards" — [youtube/2024-07-08_wgcfq51twe0_this-launch-took-11-months-of.md](https://www.youtube.com/watch?v=wgcfq51twe0&t=95s) · 2024-07

## Evidence

- Active, exploratory learning: try first.
  > "This course encourages **active, exploratory learning**. In the video, I'll explain a problem, and **you'll be asked to try to find a solution**." — [github/total-typescript-book-010/README.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/README.md)
- Tests tell you when you have succeeded.
  > "You'll know if you've succeeded because the tests will pass." — [github/total-typescript-book-010/README.md](https://github.com/mattpocock/total-typescript-book-010/blob/HEAD/README.md)
- It is the format that works for him every time.
  > "it's something that I've found just works again and again and again every time I've put it in a course." — [blog/workshops__before-we-start-pxqjv__how-to-do-skill-building-exercises-5s570.md](https://www.aihero.dev/workshops/before-we-start-pxqjv/how-to-do-skill-building-exercises-5s570) · n.d.
- He thrusts you into the problem and gives knowledge afterwards.
  > "you'd essentially just be thrust into a problem and have to solve it on your own. I would give you the knowledge afterwards." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=896s) · Latent Space
- One thing per lesson, clear dependencies, challenge without overwhelm.
  > "each lesson should only teach one thing, each lesson should depend and the dependencies between all the knowledge should be super clear, and you should always challenge people without overwhelming them." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=762s) · Latent Space

## How it shows up

1. Collect ideas in a Zettelkasten, prioritise lessons P1/P2/P3, record the P1s.
  > "I prioritize each individual lesson, work out how important it is to the running of the course. P1, P2, P3. I then record all the P1s mostly, and then that's the course" — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=741s) · Latent Space
2. Write learning goals before planning lessons and videos.
  > "One thing a learner should come away knowing from a **Section**, written BEFORE the Section's Lessons, Videos and Beats are planned." — [github/course-video-manager/CONTEXT.md](https://github.com/mattpocock/course-video-manager/blob/HEAD/CONTEXT.md)
3. Keep exercises short enough for a lunch break, with practical work after a minute of video.
  > "I love the exercises because you can just sort of dive into them in in your lunch break basically it should take about sort of five or 10 minutes to solve each" — [youtube-appearances/unknown_5ROCO6Bbdv0_typescript-with-matt-pocock.md](https://www.youtube.com/watch?v=5ROCO6Bbdv0&t=4871s) · Top End Devs
4. Make types testable too, with tiny helper types.
  > "type test = Expect<Equal<typeof e, string>>;" — [github/react-typescript-tutorial-02/src/02-components/09-html-props-with-one-changed.problem.tsx](https://github.com/mattpocock/react-typescript-tutorial-02/blob/HEAD/src/02-components/09-html-props-with-one-changed.problem.tsx)
5. Lead with a named mental model.
  > "this is my mental model for infer" — [youtube/2022-12-19_hLZXJTm7TEk_infer-is-easier-than-you-think.md](https://www.youtube.com/watch?v=hLZXJTm7TEk&t=676s) · 2022-12
6. Live, let the learner flail before revealing.
  > "I'm gonna let you flail a bit longer." — [youtube-appearances/unknown_xk_PbxR7G8A_advanced-typescript-let-s-learn-generics.md](https://www.youtube.com/watch?v=xk_PbxR7G8A&t=4265s) · CodeTV
7. Teach from real work, including a full commit history.
  > "I've given you an entire commit history showing me building a project from scratch." — [blog/workshops__before-we-start-pxqjv__how-to-do-the-project-exercises~80ywf.md](https://www.aihero.dev/workshops/before-we-start-pxqjv/how-to-do-the-project-exercises~80ywf) · n.d.
- He demystifies: show the plain mechanism, then build.
  > "There's nothing particularly fancy going on - it's just tool definitions inside the system prompt." — [blog/what-are-tools.md](https://www.aihero.dev/what-are-tools) · 2025-09

## Tensions and evolution

- In 2025 he called "lessons as prompts" the format for the vibe-coding age; later he found AI-experimental formats turned people off.
  > "I've found the perfect teaching method for the vibe coding age: Lessons as prompts." — [x/2025-04.md](https://x.com/mattpocockuk/status/1909279377583477138) · 2025-04
  > "the more I lean into the kind of AI experimental stuff, the more it actually turns people off my materials." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=848s) · Latent Space
- For fast-moving AI topics he switched to two-week cohorts.
  > "I run courses in two-week cohorts these days because AI moves so quickly." — [youtube-appearances/unknown_rlM_fAKxB3Q_senior-dev-this-grill-me-prompt.md](https://www.youtube.com/watch?v=rlM_fAKxB3Q&t=47s) · Latent Space
- He debated concept-first versus scary-code-first in public.
  > "But maybe I should show a BIG SCARY code sample first, then decode it. That makes things "real-world" straight away." — [x/2022-07.md](https://x.com/mattpocockuk/status/1548986715746062336) · 2022-07

## Related

- [Learning at the edge](../principles/learning-at-the-edge.md)
- [Teacher, not pundit](../principles/teacher-not-pundit.md)
- [Feedback is the speed limit](../principles/feedback-is-the-speed-limit.md)
- [Content production](content-production.md)
- [TypeScript is JavaScript with types](../principles/typescript-is-javascript-with-types.md)
