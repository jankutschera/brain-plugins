---
type: method
sources: [blog, x, youtube, youtube-appearances]
quotes: 27
first_seen: 2015-03
last_seen: 2024-06
---
# Look at the data and the numbers

He looks at exactly what enters the network and reads every number in a run as a diagnostic.
  > "The unambiguously correct place to examine your training data is immediately before it feeds into the network." — [x/2020-11.md](https://x.com/karpathy/status/1328547710966743040) · 2020-11

## Evidence

- He visualizes the batch at the forward call, not upstream, and says it keeps catching bugs.
  > "The unambiguously correct place to visualize your data is immediately before your" — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "I can’t count the number of times this has saved me and revealed problems in data preprocessing and augmentation." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "Take the raw x,y batch tuple, ship it back to CPU, unrender, visualize." — [x/2020-11.md](https://x.com/karpathy/status/1328547710966743040) · 2020-11
- He goes after the outliers and the highest-loss examples.
  > "The outliers especially almost always uncover some bugs in data quality or preprocessing." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "When you sort your dataset descending by loss you are guaranteed to find something unexpected, strange and helpful." — [x/2020-10.md](https://x.com/karpathy/status/1311884485676294151) · 2020-10
  > "we are dealing with a massive scalability challenge around the finding of the needle in a haystack" — [youtube-appearances/unknown_g2R2T631x7k_cvpr-20-workshop-on-scalability-in.md](https://www.youtube.com/watch?v=g2R2T631x7k&t=1453s) · 2020-06
- He knows what number to expect before he runs, and reads a wrong one as a diagnosis.
  > "in training of neural Nets it is almost always the case that you will have a rough idea for what loss to expect at initialization" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=282s) · 2022-10
  > "Indeed, starting Caffe training with default hyperparameters gives a starting loss of about 80, which right away tells you that the initialization is completely out of whack" — [blog/karpathy.github.io/2015__03__30__breaking-convnets.md](https://karpathy.github.io/2015/03/30/breaking-convnets/) · 2015-03
- He instruments training with a fixed set of plots and ratios.
  > "I like to look at the evolution of this update ratio for all my parameters usually and I like to make sure that it's not too much above onean neg3 roughly" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6198s) · 2022-10
  > "this is how miscalibrations of your neuron nuts are going to manifest and these kinds of plots here are a good way of um sort of bringing um those miscalibrations sort of uh to your attention" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6346s) · 2022-10
- The gradient norm is his health signal.
  > "sometimes you can look at the norm of the gradient and if it's well behaved things are good if it's climbing things are bad" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=8351s) · 2024-06
- He watches predictions and weights move during training.
  > "I like to visualize model predictions on a fixed test batch during the course of training." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
  > "I like to visualize the network’s first-layer weights and ensure you get nice edges that make sense." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- He treats tensor shapes as data to check, not to guess.
  > "hopefully this helps to scare you that you should have a respect for broadcasting, be careful, check your work, uh and uh understand how it works under the hood" — [youtube/2022-10-09_PaCmpygFfXo_the-spelled-out-intro-to-language.md](https://www.youtube.com/watch?v=PaCmpygFfXo&t=2967s) · 2022-09
- He derives backward formulas from the shapes instead of memorizing them.
  > "there is only a single way to make the shape work out in this case and it is indeed the correct result" — [youtube/2023-10-09_q8SA3rM6ckI_building-makemore-part-4-becoming-a.md](https://www.youtube.com/watch?v=q8SA3rM6ckI&t=3037s) · 2022-10

## How it shows up

- He writes code so that it exposes what he wants to plot.
  > "I'm creating a DOT out because I would like to very easily um maintain all those variables so that we can create statistics of them and plot them" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=5031s) · 2022-10
- He fixes plots that are hard to read before reading them.
  > "I'd like to plot the log loss instead of the loss because when you plot the loss, many times it can have this hockey stick appearance and log squashes it in." — [youtube/2022-10-09_TCH_1BHY58I_building-makemore-part-2-mlp.md](https://www.youtube.com/watch?v=TCH_1BHY58I&t=4117s) · 2022-09
  > "first let's fix this graph because it is daggers in my eyes and I just can't take it anymore" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=416s) · 2022-11
- He reads a hockey-stick loss curve as wasted early training.
  > "we're spending more Cycles more time optimizing the neuronet actually instead of just uh spending the first several thousand iterations probably just squashing down the weights" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=760s) · 2022-10
- He reads training state off weight plots.
  > "you can tell for example that because they're a bit more Jagged and they're kind of noisy you can tell that this model was not fully trained" — [youtube/2024-10-09_l8pRSuU81PU_let-s-reproduce-gpt-2-124m.md](https://www.youtube.com/watch?v=l8pRSuU81PU&t=576s) · 2024-06
- He names tensor dimensions to keep shapes readable.
  > "here's what I like to do I like to take basically give names to the dimensions" — [youtube/2023-10-09_kCc8FmEb1nY_let-s-build-gpt-from-scratch.md](https://www.youtube.com/watch?v=kCc8FmEb1nY&t=1612s) · 2023-01
- He uses gradients to see what depends on what.
  > "More generally, gradients give you information about what depends on what in your network, which can be useful for debugging." — [blog/karpathy.github.io/2019__04__25__recipe.md](https://karpathy.github.io/2019/04/25/recipe/) · 2019-04
- At Tesla the hard part was spotting what the network doesn't know, which he called unsolved.
  > "detecting basically that a network doesn't know doesn't know and doing it efficiently at this time it's kind of still an open problem in my mind" — [youtube-appearances/unknown_g2R2T631x7k_cvpr-20-workshop-on-scalability-in.md](https://www.youtube.com/watch?v=g2R2T631x7k&t=1549s) · 2020-06

## Tensions and evolution

- In 2022 he said the old care about activation histograms matters less after normalization layers and Adam, but he still teaches the plots.
  > "about 7 years ago when this paper was written you had to actually be extremely careful with the activations and ingredients and their ranges and their histograms" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=2161s) · 2022-10
  > "all of these modern Innovations make it less important for you to precisely calibrate the neutralization of the neural net" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=2217s) · 2022-10
  > "I tried to introduce you to the diagnostic tools that you would use to understand whether your neural network is in a good State dynamically" — [youtube/2022-10-09_P6sfmUTpUmc_building-makemore-part-3-activations-gradients.md](https://www.youtube.com/watch?v=P6sfmUTpUmc&t=6758s) · 2022-10

## Related

- [Data is the program](../principles/data-is-the-program.md)
- [Neural nets fail silently](../principles/neural-nets-fail-silently.md)
- [Evaluation is the bottleneck](../principles/evaluation-is-the-bottleneck.md)
- [Training recipe](training-recipe.md)
- [Data engine](data-engine.md)
- [Measure it yourself](measure-it-yourself.md)
