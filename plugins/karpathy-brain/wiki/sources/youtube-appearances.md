---
type: source
raw: raw/youtube-appearances/
files: 45
words: 291401
date_range: 2016 – 2026 (approx; 8 of 22 transcripts undated)
---
# YouTube appearances (talks, interviews, podcasts)

## Coverage

- **What exists (MANIFEST.md):** 22 accepted transcripts (291,401 words) of Karpathy on other channels, each with a `.segments.json` twin, plus the `candidates.json` discovery file: 45 files. Discovery was a yt-dlp search with 290 hits; 22 accepted, 27 rejected, 241 not reviewed. No fetch failures. Every `upload_date` is `unknown`.
- **The 22 transcripts, by file id:** Dwarkesh "We're summoning ghosts" (`lXUZvyajciY`, 2025); No Priors "Skill Issue" (`kwSVtQ7dziU`, n.d., after December 2025 by internal clues); Sequoia "From Vibe Coding to Agentic Engineering" (`96jN2OCOfLs`, 2026); Sequoia "Making AI accessible" (`c3b-JASoPi0`, n.d.); YC "Software Is Changing (Again)" (`LCEmiRjPEtQ`, 2025); State of GPT at Microsoft Build (`bZQun8Y4L2A`, 2023-05); CUDA Mode keynote (`aR6CzM0x-g0`, n.d.); No Priors Ep. 80 (`hM_h0UA7upI`, 2024); Lex Fridman #333 (`cdiD-9MMpb0`, n.d., first months after Tesla); Robot Brains S1E1 (`PlLmdTcsAWU`, 2021); Full Stack Deep Learning "AI at Tesla" (`ZVJTqAuPvTU`, 2018-08); Heroes of Deep Learning with Andrew Ng (`_au3yw46lcg`, n.d.); PyTorch at Tesla (`oBklltKXtDE`, n.d.); Matroid "AI for Full-Self Driving" (`hx7BXih7zx8`, n.d.); CVPR'20 workshop (`g2R2T631x7k`, 2020); CVPR'21 WAD keynote (`g6bOwQdCJrc`, 2021); Deep Learning for Computer Vision lecture (`u6aEYuemt0M`, 2016); Stanford CS25 (`XfpMkf4rD6E`, 2023-01); UC Berkeley hackathon keynote (`tsTeEkzO9xc`, 2024); Tesla AI Day 2021 (`j0z4FweCy4M`); Tesla Autonomy Day (`Ucp0TTmvqOE`, n.d.); Clubhouse "Recent Breakthroughs in AI" (`3OxEpGU1unA`, 2021-02).
- **Dates:** no file has an upload date, so dates come only from titles or transcript text ("August 2018", "Feb 2021", "we're here in 2016", "winter of 2023", Build 2023, and similar). Eight transcripts stay `n.d.`.
- **Read in full (Karpathy speaking throughout):** Dwarkesh (26k words), Skill Issue, both Sequoia talks, YC, State of GPT, CUDA Mode, No Priors Ep. 80, Lex Fridman (all 39.5k words), Robot Brains, Full Stack DL 2018, Heroes of DL, PyTorch at Tesla, Matroid, both CVPR keynotes, the 2016 lecture including the Q&A answers.
- **Multi-speaker files, Karpathy's parts only:** Stanford CS25 (from the start of the lecture to the end), Berkeley hackathon (keynote only, pitches and judges skipped), Tesla AI Day (vision section plus one Q&A answer), Tesla Autonomy Day (the neural network section and two audience answers), Clubhouse (only spans the context pins to Karpathy).
- **Attribution rules:** no host, co-panelist or audience question is quoted. Where captions merge speakers (Lex Fridman, No Priors, Dwarkesh, Clubhouse, Autonomy Day), only spans after a clear hand-off were used. Plausible but unproven Karpathy spans were skipped.
- **Sampling:** 848 verified spans were collected in working notes and the strongest ~400 kept, spread across periods: 2016 lecture, 2018-2021 Tesla talks, 2022 Lex, 2023 Build and CS25, 2024 CUDA Mode, No Priors and Berkeley, 2025 YC and Dwarkesh, 2026 Sequoia and Skill Issue. Long Tesla architecture walkthroughs are summarised by one or two quotes. Speculation unrelated to building or teaching (aliens, simulation theory, movies, diet, consciousness, GDP growth, robot form factor) was mostly dropped.
- **Skipped:** `candidates.json`, all `.segments.json` files, host monologues, the Berkeley pitch section, and the parts of AI Day not attributable to Karpathy.
- **One borrowed line:** "you can outsource your thinking, but you can't outsource your understanding" (Sequoia 2026) is someone else's tweet that Karpathy repeats and endorses; the transcript says so.

## What this source shows about them

- The talks state the build-to-understand rule most bluntly.
  > "So don't write blog posts, don't do slides, don't do any of that. Build the code, arrange it, get it to work. It's the only way to go." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1825s) · 2025-10
  > "when you build something from scratch, you're forced to come to terms with what you don't understand and you don't know that you don't understand it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1795s) · 2025-10
- Running code is trusted over papers and slides.
  > "The code is the source of truth. The papers and everything else, it's a high-level summary." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9366s) · 2022-10
- The Tesla talks are the fullest account of Software 2.0 in practice: the data set is the source code.
  > "So here the source code are the data sets. The compilation is the training of the neural network and your binary is the final neural net, the weights." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=2576s) · 2021-09
  > "what I found kind of shocking was that a huge amount of my time ended up just empirically being spent on the data set and just massaging all the data sets." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=38s) · 2018-08
- They are also the main source on the data engine, the loop that mines failures from deployment.
  > "this is what I refer to as a data engine. And I think basically every single machine learning applied machine learning um uh process must have some kind of a data engine associated with it." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1023s) · 2018-08
- Test sets get as much work as training sets.
  > "we put just as much work into massaging the test sets as we do into training sets." — [youtube-appearances/unknown_hx7BXih7zx8_andrej-karpathy-ai-for-full-self.md](https://www.youtube.com/watch?v=hx7BXih7zx8&t=780s) · 2020-04
- Self-driving taught Karpathy that demos are cheap and products are a long march of reliability.
  > "What takes the long amount of time and the way to think about it is that it's a march of nines. Every single nine is a constant amount of work." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=6359s) · 2025-10
  > "Self-driving is very interesting because it's definitely where I get a lot of my intuitions because I spent five years on it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=6253s) · 2025-10
- Timelines are pushed back against the hype.
  > "when I see things like oh 2025 is the year of agents I get very concerned and I kind of feel like you know this is the decade of agents" — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=1651s) · 2025-06
- Complexity has to pay for itself, in code and in teams.
  > "I've actually rejected a lot of PRS because of that because the code starts to get crazy and I think that decreases the amount of people that can be on board in the project" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=1051s) · 2024-10
- Karpathy asks builders to understand LLM "psychology" before building on it.
  > "LLMs don't want to succeed, they want to imitate. You want to succeed, and you should ask for it." — [youtube-appearances/unknown_bZQun8Y4L2A_state-of-gpt-brk216hfs.md](https://www.youtube.com/watch?v=bZQun8Y4L2A&t=1823s) · 2023-05
- Reinforcement learning as practiced is called crude, though better than imitation.
  > "Reinforcement learning is terrible. It just so happens that everything that we had before it is much worse because previously we were just imitating people" — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2502s) · 2025-10
  > "The way I like to put it is you're sucking supervision through a straw." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2599s) · 2025-10
- The interviews give the most complete theory of teaching: education as building ramps.
  > "In my mind, education is the very difficult technical process of building ramps to knowledge." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7401s) · 2025-10
  > "It's giving you a lot of what I call eurekas per second, which is understanding per second. That's what I want, lots of eurekas per second." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7423s) · 2025-10
- They also give the motive: making people better off, not teaching for its own sake, and keeping humanity from being sidelined by AI.
  > "Yeah, I mean I don't think I love teaching. I love happy humans and happy humans like when I teach." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9563s) · 2022-10
  > "I want humans to be much, much better in this future. To me, this is through education that you can achieve this." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7096s) · 2025-10
  > "My personal big fear is that a lot of this stuff happens on the side of humanity, and that humanity gets disempowered by it." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=7062s) · 2025-10
- Expertise is described as volume of work, measured against your past self.
  > "You literally have to put in 10,000 hours of work. It doesn't even matter as much where you put it, you'll iterate and you'll improve and you'll waste some time." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9412s) · 2022-10
- Across the appearances, AI coding goes from checking every Copilot suggestion, to autocomplete as the sweet spot, to not typing code at all.
  > "So I would never take Copilot code as given. I almost always copy-paste into a Google search and you see what this function is doing" — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=8777s) · 2022-10
  > "For now, autocomplete is my sweet spot." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=2253s) · 2025-10
  > "I don't think I've typed like a line of code probably since December basically." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=114s) · 2026-03
- The audience for explanations shifted too: from people to agents that explain to people.
  > "I'm not explaining to people anymore. I'm explaining it to agents." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=3789s) · 2026-03
- The line about outsourcing thinking but not understanding comes from someone else's tweet, which Karpathy quotes and builds on.
  > "Uh there was a tweet that blew my mind recently, and I keep thinking about it like every other day. It was something along the lines of um you can outsource your thinking, but you can't outsource your understanding." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1686s) · 2026-04
- The interviews are the main source for biography: leaving Slovakia at 15, Hinton's class in Toronto, and leaving Tesla because the job had become management.
  > "my parents decided to immigrate to Canada when I was 15." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=141s) · 2021-09
  > "this was by chance of being right next to Geoff Hinton at the University of Toronto" — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=269s) · 2025-10
  > "And it's kind of like a corporate executive role. And I can do it. I think I'm okay at it. But it's not like fundamentally what I enjoy." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=6302s) · 2022-10

## Notable pieces

- **Dwarkesh, "We're summoning ghosts" (2025, 26k words).** The densest single source on teaching, timelines and RL. It includes the rule for learning a code base.
  > "You're not allowed to copy-paste, you're allowed to reference, you're not allowed to copy-paste." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=1751s) · 2025-10
- **Lex Fridman #333 (n.d., 39.5k words, the longest).** Tesla, the data engine, lecture craft and working habits.
  > "the data engine is what I call the almost biological feeling process by which you perfect the training sets for these neural networks." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=5039s) · 2022-10
  > "it probably takes me somewhere around 10 hours to create one hour of content." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=9649s) · 2022-10
- **Full Stack Deep Learning, "AI at Tesla" (2018-08).** The earliest Software 2.0 talk from inside Tesla, with labeling as programming.
  > "So your data set is really code" — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1179s) · 2018-08
  > "and then it turns out that ketchup does not wipe." — [youtube-appearances/unknown_ZVJTqAuPvTU_andrej-karpathy-on-ai-at-tesla.md](https://www.youtube.com/watch?v=ZVJTqAuPvTU&t=1109s) · 2018-08
- **Deep Learning for Computer Vision lecture (2016).** The earliest recording, already with the "don't be a hero" advice.
  > "So my answer here and I've already hinted at this is don't be a hero. Don't go crazy." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=3826s) · 2016-09
- **Heroes of Deep Learning with Andrew Ng (n.d.).** How Karpathy learned backprop: by writing a library.
  > "so I wrote my own library it's called convnet js it was written in Javascript and implements convolutional neural networks that was my way of learning about back propagation" — [youtube-appearances/unknown__au3yw46lcg_heroes-of-deep-learning-andrew-ng.md](https://www.youtube.com/watch?v=_au3yw46lcg&t=836s) · 2017-08
- **Robot Brains S1E1 (2021).** On pausing the PhD to build CS231n.
  > "But I felt like it was probably more impactful than getting a paper or two out to actually like do this class and do a good job of it." — [youtube-appearances/unknown_PlLmdTcsAWU_season-1-ep-1-andrej-karpathy.md](https://www.youtube.com/watch?v=PlLmdTcsAWU&t=433s) · 2021-09
- **CVPR'20 and CVPR'21 keynotes.** The data engine at fleet scale, with hand-built triggers.
  > "because this is a product in the hands of customers you are forced to go through the longtail you can't just do 95% and call it a day" — [youtube-appearances/unknown_g2R2T631x7k_cvpr-20-workshop-on-scalability-in.md](https://www.youtube.com/watch?v=g2R2T631x7k&t=684s) · 2020-06
  > "we've ended up developing 221 triggers uh manually" — [youtube-appearances/unknown_g6bOwQdCJrc_cvpr-21-wad-keynote-andrej-karpathy.md](https://www.youtube.com/watch?v=g6bOwQdCJrc&t=891s) · 2021-06
- **Stanford CS25 (2023-01).** A new framing of attention, admitted to be fresh that morning.
  > "Basically, to me, attention is kind of like the communication phase of the transformer" — [youtube-appearances/unknown_XfpMkf4rD6E_stanford-cs25-v2-i-introduction-to.md](https://www.youtube.com/watch?v=XfpMkf4rD6E&t=1367s) · 2023-01
  > "OK, I have to think through this analogy a little bit more. I came up with it this morning." — [youtube-appearances/unknown_XfpMkf4rD6E_stanford-cs25-v2-i-introduction-to.md](https://www.youtube.com/watch?v=XfpMkf4rD6E&t=1827s) · 2023-01
- **State of GPT, Microsoft Build (2023-05).** Practical advice for building on LLMs.
  > "Number 1, achieve your top performance, and Number 2, optimize your performance in that order." — [youtube-appearances/unknown_bZQun8Y4L2A_state-of-gpt-brk216hfs.md](https://www.youtube.com/watch?v=bZQun8Y4L2A&t=2238s) · 2023-05
- **CUDA Mode keynote (n.d.).** The story of llm.c, started when a framework blocked a lesson.
  > "the computation itself the algorithm itself is totally clear in my mind I and for some reason torch compal doesn't let me like use it run it Etc so I felt a little bit powerless" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=228s) · 2024-10
  > "all of this work that I described so far happened on a vacation while I was jetlagged in Maldives" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=597s) · 2024-10
- **No Priors Ep. 80 (2024).** The Eureka Labs model: teacher at the back end, AI at the front.
  > "the teacher is not the front end anymore the teacher is on the back end designing the materials in the course and the AI is the front end" — [youtube-appearances/unknown_hM_h0UA7upI_no-priors-ep-80-with-andrej.md](https://www.youtube.com/watch?v=hM_h0UA7upI&t=1975s) · 2024-09
- **UC Berkeley hackathon keynote (2024).** Advice to young builders on small projects and hours.
  > "how projects that are sometimes very small projects like all of snowballs can actually like snowball into really big projects" — [youtube-appearances/unknown_tsTeEkzO9xc_andrej-karpathy-s-keynote-winner-pitches.md](https://www.youtube.com/watch?v=tsTeEkzO9xc&t=692s) · 2024-07
- **YC, "Software Is Changing (Again)" (2025).** The Software 3.0 talk.
  > "And basically your prompts are now programs that program the LLM. And uh remarkably uh these uh prompts are written in English." — [youtube-appearances/unknown_LCEmiRjPEtQ_andrej-karpathy-software-is-changing-again.md](https://www.youtube.com/watch?v=LCEmiRjPEtQ&t=199s) · 2025-06
- **No Priors, "Skill Issue" (n.d., after December 2025).** Agentic engineering and autoresearch in practice.
  > "And auto research is just, yeah, here's an objective, here's a metric, here's your boundaries of what you can and cannot do. And go." — [youtube-appearances/unknown_kwSVtQ7dziU_skill-issue-andrej-karpathy-on-code.md](https://www.youtube.com/watch?v=kwSVtQ7dziU&t=1053s) · 2026-03
- **Sequoia, "From Vibe Coding to Agentic Engineering" (2026).** The split between raising the floor and keeping the quality bar.
  > "I would say vibe coding is about raising the floor for everyone in terms of what they can do in software." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=957s) · 2026-04
  > "But then I would say agentic engineering is about preserving the quality bar of what existed before in professional software." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=966s) · 2026-04
- **Sequoia, "Making AI accessible" (n.d.).** "Build the thing, build the ramp" applied to the field.
  > "I would say there's a lot of people building a thing I would say there's lot a lot less happening of like building ramps so that people can actually understand all this stuff" — [youtube-appearances/unknown_c3b-JASoPi0_making-ai-accessible-with-andrej-karpathy.md](https://www.youtube.com/watch?v=c3b-JASoPi0&t=1959s) · 2024-03
- **Clubhouse, "Recent Breakthroughs in AI" (2021-02).** A side project's real maintenance cost.
  > "It's almost always offline. I get a tweet every third day to restart the server." — [youtube-appearances/unknown_3OxEpGU1unA_recent-breakthroughs-in-ai-andrej-karpathy.md](https://www.youtube.com/watch?v=3OxEpGU1unA&t=178s) · 2021-02
- **Tesla Autonomy Day (n.d.) and PyTorch at Tesla (n.d.).** The fleet as a data source, and labeling as the one job that stays human.
  > "when it comes to training data from your networks there really is no substitute for real data" — [youtube-appearances/unknown_Ucp0TTmvqOE_tesla-autonomy-day.md](https://www.youtube.com/watch?v=Ucp0TTmvqOE&t=7388s) · 2019-04
  > "as long as the data labeling team is around and they're curating and improving our data sets then everything else can in principle be automated" — [youtube-appearances/unknown_oBklltKXtDE_pytorch-at-tesla-andrej-karpathy-tesla.md](https://www.youtube.com/watch?v=oBklltKXtDE&t=527s) · 2019-11

## Related

- Sources: [X](x.md) · [YouTube channel](youtube.md) · [Blogs](blog.md) · [GitHub](github.md)
- Principles: [Build to understand](../principles/build-to-understand.md) · [The core is tiny](../principles/core-is-tiny.md) · [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md) · [Data is the program](../principles/data-is-the-program.md) · [Software 2.0 and 3.0](../principles/software-2-and-3.md) · [LLMs are ghosts](../principles/llms-are-ghosts.md) · [Verifiability drives progress](../principles/verifiability-drives-progress.md) · [Scale and compute](../principles/scale-and-compute.md) · [Demos are not products](../principles/demos-are-not-products.md) · [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md) · [Understanding cannot be outsourced](../principles/understanding-cannot-be-outsourced.md) · [Build for agents](../principles/build-for-agents.md) · [Ambition and agency](../principles/ambition-and-agency.md) · [Openness and ownership](../principles/openness-and-ownership.md) · [Learning is effortful](../principles/learning-is-effortful.md)
- Methods: [Training recipe](../methods/training-recipe.md) · [Look at the data and numbers](../methods/look-at-the-data-and-numbers.md) · [Reference then port](../methods/reference-then-port.md) · [Reproduce landmarks](../methods/reproduce-landmarks.md) · [Fast feedback loops](../methods/fast-feedback-loops.md) · [Data engine](../methods/data-engine.md) · [AI-assisted coding](../methods/ai-assisted-coding.md) · [Autoresearch](../methods/autoresearch.md) · [Measure it yourself](../methods/measure-it-yourself.md) · [Knowledge work](../methods/knowledge-work.md) · [Deep work and side projects](../methods/deep-work-and-side-projects.md) · [Build it live](../methods/build-it-live.md) · [Smallest complete version](../methods/smallest-complete-version.md) · [Ramps to knowledge](../methods/ramps-to-knowledge.md) · [Demystify the math](../methods/demystify-the-math.md) · [Analogies and examples](../methods/analogies-and-examples.md) · [Learner does the work](../methods/learner-does-the-work.md) · [Show the mess](../methods/show-the-mess.md) · [Playful and accessible](../methods/playful-and-accessible.md) · [Education with AI](../methods/education-with-ai.md)
