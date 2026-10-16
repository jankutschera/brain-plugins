---
type: principle
sources: [x, github, blog, youtube-appearances]
quotes: 24
first_seen: 2013-11
last_seen: 2026-09
---
# Openness and ownership

Release the code and work in the open, and own your data and tools, so that incentives stay aligned with the people who use them.
  > "it is precisely for some of these reasons that you should commit to releasing your code" — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09

## Evidence

- Publishing code makes you write better code.
  > "it will force you to adopt better coding habits due to fear of public shaming (which will end up saving you time!)" — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
  > "that really increases the bar for your own work and it makes you work harder because they're going to be looking at it and you feel shame if it was crappy" — [youtube-appearances/unknown_tsTeEkzO9xc_andrej-karpathy-s-keynote-winner-pitches.md](https://www.youtube.com/watch?v=tsTeEkzO9xc&t=1265s) · 2024-07
- He sees closed, concentrated AI as a systemic risk and wants many players.
  > "I think there's some systemic risk attached to just having intelligence that are closed and that's like that's it." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3114s) · 2026-03
  > "I think like in machine learning ensembles always outperform any individual model. And so I want there to be ensembles of people thinking about all the hardest problems" — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3226s) · 2026-03
- Open weights are helpful but limited: to add a capability without regressing the others, you need the training loop and the data.
  > "if you're just given the weights you can't do that actually you need the training Loop you need the data set Etc" — [youtube-appearances/unknown_c3b-JASoPi0_making-ai-accessible-with-andrej-karpathy.md](https://www.youtube.com/watch?v=c3b-JASoPi0&t=536s) · 2024-03
- In the neural-net era, open data plays the role open source played.
  > "The equivalent of open source in Software 2.0 land are open datasets." — [x/2021-02.md](https://x.com/karpathy/status/1365511769255342084) · 2021-02
- He pays for software so that he is the customer.
  > "I pay $3/mo for Brave Premium because I prefer to be the customer, not the product in my digital life." — [x/2025-03.md](https://x.com/karpathy/status/1902046003567718810) · 2025-03
  > "And I wish to pay for the software I use so that incentives are aligned and so that I am the customer." — [blog/karpathy.bearblog.dev/digital-hygiene.md](https://karpathy.bearblog.dev/digital-hygiene/) · 2025-03
- He wants his content and data in raw form, on his own machine.
  > "You do not really own your content in raw and nimble form." — [blog/karpathy.github.io/2014__07__01__switching-to-jekyll.md](https://karpathy.github.io/2014/07/01/switching-to-jekyll/) · 2014-07
  > "The data must never leave the local machine (No cloud mambo jambo - too personal!)" — [blog/karpathy.github.io/2014__08__03__quantifying-productivity.md](https://karpathy.github.io/2014/08/03/quantifying-productivity/) · 2014-08
  > "I prefer fully super duper fully offline apps" — [x/2025-02.md](https://x.com/karpathy/status/1889036923655860247) · 2025-02
  > "Your notes are simple plain-text markdown files stored locally on your computer." — [x/2024-02.md](https://x.com/karpathy/status/1761467904737067456) · 2024-02
- He likes AI memory he can see and edit.
  > "The memory artifact is explicit and navigable (the wiki), you can see exactly what the AI does and does not know" — [x/2026-04.md](https://x.com/karpathy/status/2040572272944324650) · 2026-04

## How it shows up

- His repos are meant to be forked, not used as platforms.
  > "I expect most applications will wish to create a fork of this repo and hack it to their specific needs and deployment platforms." — [github/llama2.c/README.md](https://github.com/karpathy/llama2.c/blob/350e04fe35433e6d2941dce5a1f53308f87058eb/README.md) · 2023-07
- llm.c is open as a teaching repo and fast at the same time, with the fast libraries kept as a yardstick.
  > "First, I want `llm.c` to be a place for education." — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
  > "I also think doing so serves an educational purpose to establish an expert upper bound, and a unit of measurement" — [github/llm.c/README.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/README.md) · 2024-04
- nanochat runs an open leaderboard to pull in community work.
  > "Inspired by the modded-nanogpt repo and to incentivise progress and community collaboration, nanochat maintains a leaderboard" — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- For Eureka Labs he planned free, permissively licensed content.
  > "My default thinking is that the content itself is free and permissively licensed, the revenue comes from everything else" — [x/2024-07.md](https://x.com/karpathy/status/1813273726441652683) · 2024-07
- He builds his own small tools when a platform's revenue model keeps it from adding a feature he wants.
  > "Twitter will never implement this because it makes Zero sense for their revenue model, but luckily, we can hack this together quite easily!" — [blog/karpathy.github.io/2013__11__23__chrome-extension-programming.md](https://karpathy.github.io/2013/11/23/chrome-extension-programming/) · 2013-11

## Tensions and evolution

- Open but not maintained. From 2025 he releases code as inspiration and says up front he won't support it.
  > "I'm not going to support it in any way, it's provided here as is for other people's inspiration and I don't intend to improve it." — [github/llm-council/README.md](https://github.com/karpathy/llm-council/blob/92e1fccb1bdcf1bab7221aa9ed90f9dc72529131/README.md) · 2025-11
- Openness is limited by outside forces. In 2016 the CS231n lecture videos came down.
  > "I regret to inform that we were forced to take down CS231n videos due to legal concerns." — [x/2016-05.md](https://x.com/karpathy/status/727618058471112704) · 2016-05
- Success of an open repo made it harder to change. minGPT became too widely referenced to move forward, so he started nanoGPT.
  > "Basically, minGPT became referenced across a wide variety of places (notebooks, blogs, courses, books, etc.) which made me less willing to make the bigger changes I wanted to make to move the code forward." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2023-01
- By 2026 he shares ideas more than code, and lets each reader's agent build its own version.
  > "you just share the idea, then the other person's agent customizes" — [x/2026-04.md](https://x.com/karpathy/status/2040470801506541998) · 2026-04

## Related

- [Simplicity is a constraint](simplicity-is-a-constraint.md)
- [Build for agents](build-for-agents.md)
- [Ambition and agency](ambition-and-agency.md)
- [Knowledge work](../methods/knowledge-work.md)
- [Deep work and side projects](../methods/deep-work-and-side-projects.md)
- [Education with AI](../methods/education-with-ai.md)
- [Smallest complete version](../methods/smallest-complete-version.md)
