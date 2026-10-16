---
type: method
sources: [blog, x, youtube-appearances, youtube, github]
quotes: 32
first_seen: 2015-05
last_seen: 2026-02
---
# Demystify the math

He leads with code and intuition, strips away gatekeeping formalism, and shows that the magic is simple underneath.
  > "Whenever there is a disconnect between how magical something seems and how simple it is under the hood I get all antsy and really want to write a blog post." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05

## Evidence

- He explains with code and physical intuition, not derivations, because that is how it clicked for him.
  > "everything became much clearer when I started ignoring full-page, dense derivations of backpropagation equations and just started writing code" — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
  > "My exposition will center around code and physical intuitions instead of mathematical derivations." — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
- Most teaching material gets backprop wrong by burying it in mechanical math.
  > "it seems to me that 95% of backpropagation materials out there present it all wrong, filling pages with mechanical math" — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
  > "The good news is that backpropagation is not that difficult to understand, if presented properly." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
- Heavy formalism gatekeeps simple ideas and misleads practitioners.
  > "I get triggered when RL is dressed up in its full rigorous math formalism because it's gate-keeping an essentially trivial core idea." — [x/2025-01.md](https://x.com/karpathy/status/1884317937185743206) · 2025-01
  > "it's doing a disservice to the practitioners who are misled to think that it's somehow unapproachable." — [x/2024-08.md](https://x.com/karpathy/status/1821257161726685645) · 2024-08
- Mechanically, a neural net is just a math expression with knobs, though he grants that large ones show surprising emergent behavior.
  > "It's really just a complicated mathematical expression with knobs. And those knobs need a proper setting for it to do something desirable." — [youtube-appearances/unknown_cdiD-9MMpb0_andrej-karpathy-tesla-ai-self-driving.md](https://www.youtube.com/watch?v=cdiD-9MMpb0&t=113s) · 2022-10
  > "really functionally all that's happening in a convolutional network is just dotproducts and max operations. That's everything." — [youtube-appearances/unknown_u6aEYuemt0M_deep-learning-for-computer-vision-andrej.md](https://www.youtube.com/watch?v=u6aEYuemt0M&t=923s) · 2016-09
- He keeps telling readers there is nothing scary inside.
  > "I hope your takeaway is that a 2-layer Neural Net is really not such a scary thing" — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
  > "mechanically: no magic is happening" — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
  > "I want you to note that again there is nothing too scary going on inside" — [blog/karpathy.github.io/2021__06__21__blockchain.md](https://karpathy.github.io/2021/06/21/blockchain/) · 2021-06
- He promises that basic prerequisites are enough.
  > "If you know Python, have a vague recollection of taking some derivatives in your high school, watch this video and not understand backpropagation and the core of neural nets by the end then I will eat a shoe :D" — [x/2022-08.md](https://x.com/karpathy/status/1559672720895254528) · 2022-08
  > "my goal really here is to just make you understand and appreciate uh how under the hood chat GPT works and um really all that's required is a Proficiency in Python" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=434s) · 2023-01
- Experts hide the idea behind jargon; he tries to just say the thing.
  > "people have a bias to explain things in the most abstract, jargon-filled way possible and to clear their throat for four paragraphs before they explain the central idea." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8559s) · 2025-10
  > "But there's something about communicating one-on-one with a person which compels you to just say the thing. Just say the thing." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8568s) · 2025-10
- He grounds abstractions in concrete shapes and memory layouts.
  > "What are Tensors? They are 1) a 1D block of memory called Storage that holds the raw data, and 2) a View over that storage that holds its shape." — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
  > "B is the batch size, T is time, and C is channels." — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04

## How it shows up

- He reads dense papers by peeling the formalism off.
  > "A lot of diffusion papers look a bit dense but if you strip the mathematical formalism, you end up with simple baseline algorithms" — [x/2025-10.md](https://x.com/karpathy/status/1980347971935068380) · 2025-10
- He calls the core of RL dumb, and means it as a teaching point.
  > "But at the core the approach we use is also really quite profoundly dumb" — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
  > "But the core idea is so simple I can't even simplify it any more than that." — [x/2025-01.md](https://x.com/karpathy/status/1884317937185743206) · 2025-01
- He takes the fear out of a formula before reading it.
  > "This looks a bit scary if you’re not comfortable with your calculus, but this is literally just multiplying two numbers in an intuitive way." — [blog/karpathy.github.io/2026__02__12__microgpt.md](https://karpathy.github.io/2026/02/12/microgpt/) · 2026-02
- He marks the one node you have to get.
  > "now we're getting to the crux of backpropagation so this will be the most important node to understand because if you understand the gradient for this node you understand all of back propagation" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=2286s) · 2022-08
  > "If this makes sense, you understand backpropagation." — [blog/karpathy.github.io/neuralnets.md](https://karpathy.github.io/neuralnets/) · n.d.
- He makes everything explicit so nothing hidden makes the learner nervous.
  > "it is going to make everything fully explicit so you're not going to be nervous about what is hidden away from you and basically in general we're going to emerge stronger" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=207s) · 2022-10
- He untangles confusing names.
  > "Yes, confusingly enough, this is called checkpointing and has nothing to do with saving the model weights to disk." — [github/llm.c/doc/layernorm/layernorm.md](https://github.com/karpathy/llm.c/blob/f1e2ace651495b74ae22d45d1723443fd00ecd3a/doc/layernorm/layernorm.md) · 2024-04
- For general audiences he gives mental models, and he wants other experts to do the same.
  > "what I'm hoping to achieve in this video is to give you kind of mental models for thinking through what it is that this tool is" — [youtube/2025-10-09_7xTGNNLPyMI_deep-dive-into-llms-like-chatgpt.md](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=11s) · 2025-02
  > "Part of the reason for my 3hr general audience LLM intro video is I hope to inspire others to make equivalents in their own domains of expertise" — [x/2025-02.md](https://x.com/karpathy/status/1887980449550758121) · 2025-02

## Tensions and evolution

- In 2015 he sold RNNs as magic; a year later he said that framing was a mistake.
  > "There’s something magical about Recurrent Neural Networks (RNNs)." — [blog/karpathy.github.io/2015__05__21__rnn-effectiveness.md](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) · 2015-05
  > "I’d like to do something I wish I had done in my RNN blog post. I think I may have given the impression that RNNs are magic and automatically do arbitrary sequential problems." — [blog/karpathy.github.io/2016__05__31__rl.md](https://karpathy.github.io/2016/05/31/rl/) · 2016-05
- He admits he suffers from the curse of knowledge too, and asks for beginners' chats to correct for it.
  > "It's the curse of knowledge and expertise. This is a real phenomenon, and I suffered from it myself as much as I try not to." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8470s) · 2025-10
  > "For my material, I would love it if people shared their dumb conversations with ChatGPT about the stuff that I've created because it really helps me put myself again in the shoes of someone who's starting out." — [youtube-appearances/unknown_lXUZvyajciY_andrej-karpathy-we-re-summoning-ghosts.md](https://www.youtube.com/watch?v=lXUZvyajciY&t=8520s) · 2025-10

## Related

- [The core is tiny](../principles/core-is-tiny.md)
- [Analogies and examples](analogies-and-examples.md)
- [Smallest complete version](smallest-complete-version.md)
- [Build it live](build-it-live.md)
- [Playful and accessible](playful-and-accessible.md)
- [Show the mess](show-the-mess.md)
