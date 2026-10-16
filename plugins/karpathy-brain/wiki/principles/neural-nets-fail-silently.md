---
type: principle
sources: [blog, github, x, youtube]
quotes: 27
first_seen: 2016-08
last_seen: 2026-05
---
# Neural nets fail silently

Neural net training is a leaky abstraction that fails without errors, so paranoia and patience beat speed.
  > "Most of the time it will train but silently work a bit worse." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04

## Evidence

- He calls backprop a leaky abstraction: using it without knowing what is under it is how projects fail.
  > "Backpropagation is a leaky abstraction; it is a credit assignment scheme with non-trivial consequences." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
  > "If you insist on using the technology without understanding how it works you are likely to fail." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- Bugs don't crash the run. They make it a little worse, and the net still seems to work.
  > "All of these issues don't throw any errors, they silently make your network worse." — [x/2024-03.md](https://x.com/karpathy/status/1765473722985771335) · 2024-03
  > "working with neural nets is sometimes tricky because uh you may have lots of bugs in the code and uh your network might actually work just like ours worked" — [youtube/2022-10-09_VMj-3S1tku0_the-spelled-out-intro-to-neural.md](https://www.youtube.com/watch?v=VMj-3S1tku0&t=8019s) · 2022-08
- So he names patience and attention to detail as the traits that predict success, in 2019 and again in 2024.
  > "The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "The qualities that in my experience correlate most strongly to success in deep learning are patience and attention to detail." — [x/2024-03.md](https://x.com/karpathy/status/1765473722985771335) · 2024-03
  > "To get neural nets to work one must be super-OCD about details." — [x/2017-09.md](https://x.com/karpathy/status/910333448790827008) · 2017-09
- The cure is defensive work and visualizing everything.
  > "it can be mitigated by being thorough, defensive, paranoid, and obsessed with visualizations of basically every possible thing" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- Deeper nets forgive less, and some mistakes do lasting damage.
  > "the deeper your network is and the more complex it is the less forgiving it is to some of these errors" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=1655s) · 2022-10
  > "so it's kind of like a permanent brain damage in a in a mind of a network" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=1338s) · 2022-10
- Hidden state is a common source of these bugs. Batch norm is his standard example.
  > "BatchNorm is the most deviously subtly complex layer in deep learning." — [x/2021-05.md](https://x.com/karpathy/status/1394540087828877312) · 2021-05
  > "there's state in this layer and state is harmful uh usually" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=293s) · 2022-11
  > "I've shot myself in the foot with this layer over and over again in my life and I don't want you to suffer the same" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=4637s) · 2022-10
- The same distrust covers papers, popular tricks and his own guesses: he tests them in his setup first.
  > "Every variation of the idea that was attempted, including after a bunch of parameter tuning did not outperform the baseline d12 model on master" — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-05
  > "which I only guessed earlier and had a TODO for to validate." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "I can't find the MANN numbers of 82.8% and 94.9% in their paper [21]; not clear where they come from." — [github/paper-notes/matching_networks.md](https://github.com/karpathy/paper-notes/blob/75f4b42f3630252e86728bd78572a666c5f4de1a/matching_networks.md) · 2016-08

## How it shows up

- He describes his own code as full of bugs he has not found yet.
  > "I exist in a perpetually terrified state of the remaining 20 silent bugs that certainly remain in my code." — [x/2024-03.md](https://x.com/karpathy/status/1765473722985771335) · 2024-03
  > "Bugs in deep learning silently make results slightly worse, pays to be v distrusting" — [x/2021-04.md](https://x.com/karpathy/status/1381121537164513288) · 2021-04
- He points to small settings that hurt quietly, like learning rate schedules.
  > "Badly tuned LR decay schedules are an excellent way to silently shoot yourself in the foot." — [x/2021-08.md](https://x.com/karpathy/status/1431380525759885313) · 2021-08
- He teaches that a bug can look correct in one direction and be wrong in the other.
  > "This is well-intentioned and looks sensible from the perspective of the forward pass, but it introduces a major bug if you think about the backward pass." — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12
- He asks "it runs, but is it right?" while debugging on camera.
  > "we still may have a bug inside the bachelor 1D layer so let's take a look at um uh that because it runs but does it do the right thing" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=2319s) · 2022-11
- He runs ablations so he knows which change caused a gain.
  > "I verified that just swapping tanh -> relu in the original network did not give substantial gains" — [blog/karpathy.github.io/2022__03__14__lecun1989.md](https://karpathy.github.io/2022/03/14/lecun1989/) · 2022-03
- He says plainly that the field has not settled its own basics.
  > "honestly we are getting to The Cutting Edge of where the field is we certainly haven't I would say soled initialization and we haven't soled back propagation" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6915s) · 2022-10

## Tensions and evolution

- In 2026, with agents writing most of his code, he says he no longer remembers API details but still needs the fundamentals.
  > "I don't remember this stuff anymore, right? Because you don't have to." — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1282s) · 2026-04
  > "still have to have an understanding of what this stuff is doing and some of the fundamentals" — [youtube-appearances/unknown_96jN2OCOfLs_andrej-karpathy-from-vibe-coding-to.md](https://www.youtube.com/watch?v=96jN2OCOfLs&t=1298s) · 2026-04
- His 2016 argument was the same, made about humans and libraries rather than agents.
  > "you will not be ready to wrestle with the dangers it presents, and you will be much less effective at building and debugging neural networks" — [blog/karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b.md](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b) · 2016-12

## Related

- [Build to understand](build-to-understand.md)
- [Simplicity is a constraint](simplicity-is-a-constraint.md)
- [Evaluation is the bottleneck](evaluation-is-the-bottleneck.md)
- [Training recipe](../methods/training-recipe.md)
- [Look at the data and numbers](../methods/look-at-the-data-and-numbers.md)
- [Reference then port](../methods/reference-then-port.md)
- [Show the mess](../methods/show-the-mess.md)
