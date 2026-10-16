---
type: method
sources: [x, youtube-appearances, blog, github]
quotes: 36
first_seen: 2022-10
last_seen: 2026-10
---
# AI-assisted coding

He codes with AI in a tight loop: give context, ask for options, take small diffs, review, commit. Over four years this moved from autocomplete to agents that loop on their own against success criteria.
  > "The emphasis is on keeping a very tight leash on this new over-eager junior intern savant with encyclopedic knowledge of software, but who also bullshits you all the time" — [x/2025-04.md](https://x.com/karpathy/status/1915581920022585597) · 2025-04

## Evidence

- For code he cares about, he asks for approaches before he asks for code.
  > "Describe the next single, concrete incremental change we're trying to implement. Don't ask for code, ask for a few high-level approaches, pros/cons." — [x/2025-04.md](https://x.com/karpathy/status/1915581920022585597) · 2025-04
- He keeps diffs small so he can actually review them.
  > "in my own work, I'm always scared to get way too big diffs. I always go in small incremental chunks." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=1435s) · 2025-06
- The AI generates and the human verifies, so the job is to make that loop fast.
  > "usually they are doing the generation and we as humans are doing the verification. It is in our interest to make this loop go as fast as possible." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=1336s) · 2025-06
  > "it makes a lot more sense to spend a bit more time to be more concrete in your prompts which increases the probability of successful verification" — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=1483s) · 2025-06
- In 2025 autocomplete was his main tool, because pointing at the code says more than a text prompt.
  > "This is a very high information bandwidth to specify what you want. You point to the code where you want it, you type out the first few pieces, and the model will complete it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2043s) · 2025-10
  > "it takes too many bits and too much latency to communicate what I want in text, and it's faster to just demonstrate it in the code and in the right place." — [x/2025-08.md](https://x.com/karpathy/status/1959703967694545296) · 2025-08
- He hands agents work where he has a reference he understands and tests to check against.
  > "But I had a Python implementation that I fully understand, and I'm just making sure I'm making a more efficient version of it, and I have tests so I feel safer doing that stuff." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2085s) · 2025-10
  > "I wrote the Python reference code personally and from scratch and I am expert there and understand it fully. I then wrote the Rust code against this implementation with tests for equality." — [github/rustbpe/README.md](https://github.com/karpathy/rustbpe/blob/ddf848f6961a0655dc8693742fc338e5682c0d3b/README.md) · 2026-01
- Since 2026 he states success criteria instead of steps, so agents loop longer.
  > "Don't tell it what to do, give it success criteria and watch it go." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
  > "Change your approach from imperative to declarative to get the agents looping longer and gain leverage." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
- The aim is to take himself out of the loop by making the work testable for the agent.
  > "the goal is to arrange the thing so that you can put agents into longer loops and remove yourself as the bottleneck." — [x/2026-02.md](https://x.com/karpathy/status/2026738848420737474) · 2026-02
- The skill is in cutting the task so the agent gets the parts it can do.
  > "The key is to build intuition to decompose the task just right to hand off the parts that work and help out around the edges." — [x/2026-02.md](https://x.com/karpathy/status/2026731645169185220) · 2026-02

## How it shows up

- For a bigger build he first writes a detailed spec with the agent.
  > "you have to work with your agent to design a spec that is very detailed and maybe it's a maybe basically the docs and then get the agents to write them." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1248s) · 2026-04
- He watches for wrong design choices, which is where agents fail.
  > "I caught Claude using a really bad idea approach to match up a successful Stripe payment to user credits" — [blog/karpathy.bearblog.dev/vibe-coding-menugen.md](https://karpathy.bearblog.dev/vibe-coding-menugen/) · 2025-04
  > "The most common category is that the models make wrong assumptions on your behalf and just run along with them without checking." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
- He finds agents too defensive and without taste.
  > "They're way too over-defensive. They make all these try-catch statements. They keep trying to make a production code base, and I have a bunch of assumptions in my code, and it's okay." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1996s) · 2025-10
  > "they basically don't have a sense of taste." — [x/2025-08.md](https://x.com/karpathy/status/1959703967694545296) · 2025-08
- For hard questions he pastes the whole repo into the strongest model.
  > "If I have 20 minutes, I will copy-paste my entire repo and I go to GPT-5 Pro, the oracle, for some questions." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2217s) · 2025-10
- He vibe codes throwaway tools, sometimes only to find one bug.
  > "And I've vibe coded entire ephemeral apps just to find a single bug because why not" — [blog/karpathy.bearblog.dev/year-in-review-2025.md](https://karpathy.bearblog.dev/year-in-review-2025/) · 2025-12
  > "99% of this repo was vibe coded in a few hours with Opus 4.5." — [github/hn-time-capsule/README.md](https://github.com/karpathy/hn-time-capsule/blob/ca02ebb4de5e953bf1629689abd1f82b454b6905/README.md) · 2025-12
- He splits his time between the setup that works and trying the next one.
  > "The art of the process is spending 80% of the time getting work done in the setup you're comfortable with and that actually works, and 20% exploration of what might be the next step up even if it doesn't work yet." — [x/2026-02.md](https://x.com/karpathy/status/2027501331125239822) · 2026-02
- He would hire by watching someone build a big project this way.
  > "I would say that hiring have to has to look like give me a really big project and see someone implement that big project." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1126s) · 2026-04

## Tensions and evolution

- December 2022: Copilot already wrote most of his code.
  > "it already writes ~80% of my code, ~80% accuracy. I don't even really code, I prompt." — [x/2022-12.md](https://x.com/karpathy/status/1608895189078380544) · 2022-12
- Around the same time (Lex Fridman interview, after Tesla) he said he checked every Copilot suggestion.
  > "So I would never take Copilot code as given. I almost always copy-paste into a Google search and you see what this function is doing" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=8777s) · 2022-10
- August 2024: he switched to Cursor and most of his programming became English plus review.
  > "I'm trying VS Code Cursor + Sonnet 3.5 instead of GitHub Copilot again and I think it's now a net win." — [x/2024-08.md](https://x.com/karpathy/status/1827143768459637073) · 2024-08
  > "It's a bit like learning to code all over again" — [x/2024-08.md](https://x.com/karpathy/status/1827143768459637073) · 2024-08
- February 2025: he named vibe coding, for throwaway projects only.
  > "where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." — [x/2025-02.md](https://x.com/karpathy/status/1886192184808149383) · 2025-02
  > "It's not too bad for throwaway weekend projects, but still quite amusing." — [x/2025-02.md](https://x.com/karpathy/status/1886192184808149383) · 2025-02
- October 2025: he refused long agent runs and called autocomplete his sweet spot.
  > "I don't want an Agent that goes off for 20 minutes and comes back with 1,000 lines of code." — [x/2025-10.md](https://x.com/karpathy/status/1979644538185752935) · 2025-10
  > "For now, autocomplete is my sweet spot." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2253s) · 2025-10
- December 2025: he flipped to about 80% agent coding, and said agents only began to work then.
  > "I rapidly went from about 80% manual+autocomplete coding and 20% agents in November to 80% agent coding and 20% edits+touchups in December." — [x/2026-01.md](https://x.com/karpathy/status/2015883857489522876) · 2026-01
  > "coding agents basically didn’t work before December and basically work since" — [x/2026-02.md](https://x.com/karpathy/status/2026731645169185220) · 2026-02
  > "I don't think I've typed like a line of code probably since December basically." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=114s) · 2026-03
- The same month he wrote that he felt behind as a programmer.
  > "I've never felt this much behind as a programmer." — [x/2025-12.md](https://x.com/karpathy/status/2004607146781278521) · 2025-12
- October 2026: looking back, he describes his coding of less than a year earlier as typing by hand with occasional Tab autocomplete.
  > "less than 1 year ago, I was writing code manually by hand, typing memorized computer code commands into a code editor character by character, occasionally pressing Tab to autocomplete a little chunk of code." — [x/ingest/2026-10-11_2109361546505966046.md](https://x.com/karpathy/status/2109361546505966046) · 2026-10

## Related

- [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md)
- [Autoresearch](autoresearch.md)
- [Using LLMs day to day](using-llms-day-to-day.md)
- [Reference then port](reference-then-port.md)
- [Build for agents](../principles/build-for-agents.md)
- [Demos are not products](../principles/demos-are-not-products.md)
- [Deep work and side projects](deep-work-and-side-projects.md)
- [The capability gap](../principles/capability-gap.md)
