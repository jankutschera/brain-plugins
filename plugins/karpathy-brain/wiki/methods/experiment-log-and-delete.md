---
type: method
sources: [blog, github, x, youtube, youtube-appearances]
quotes: 34
first_seen: 2015-05
last_seen: 2026-09
---
# Experiment log and delete

He logs every change with its effect, adopts other people's ideas only after testing them, and deletes code that doesn't earn its place.
  > "A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep." — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03

## Evidence

- He keeps a running log of what he tried and what it did to the loss, from his lecture notebooks to nanochat and autoresearch.
  > "flat -> hierarchical (22K params): train 1.941, val 2.029" — [github/nn-zero-to-hero/lectures/makemore/makemore_part5_cnn1.ipynb](https://github.com/karpathy/nn-zero-to-hero/blob/73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde/lectures/makemore/makemore_part5_cnn1.ipynb) · 2022-09
  > "A running summary documenting some experiments and findings." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-09
  > "When an experiment is done, log it to `results.tsv`" — [github/autoresearch/program.md](https://github.com/karpathy/autoresearch/blob/228791fb499afffb54b46200aca536f79142f117/program.md) · 2026-03
- Failed ideas get written up as carefully as wins.
  > "This is the fifth failed attempt to beat pure FineWeb-EDU on CORE score." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-02
  > "The extra memory and compute overhead from predicting multiple tokens doesn't pay off, in fact the results get worse." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "The idea itself is intuitively appealing. Might come back around later to try harder later." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
- He borrows from others, mostly modded-nanogpt, but tests each piece in his own setup.
  > "All of these changes follow modded-nanogpt repo, but all of them were also validated piece by piece to yield improvements in nanochat" — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "Tested several architectural ideas from modded-nanogpt to see if they transfer to nanochat. All of these did not help:" — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "Gating didn't help at our scale." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
- When something stops paying, he deletes the code path instead of leaving an option.
  > "Deleted all grad-clip code paths. The code naturally produces well-behaved gradients." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "Removed bigram embeddings (engram-lite) from the codebase." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "basically I deleted all the streams made everything single threaded because we ended up getting all kinds of really weird race conditions and errors and so on and I just didn't want to deal with it" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=962s) · 2024-10
- He drops ideas that work if they cost too much complexity.
  > "Bigram hash embeddings had already been explored much earlier and did help somewhat, but the added parameters / VRAM / complexity were not justified at larger scale." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-03
  > "Helped a tiny bit (~1e-4 of loss), abandoned to control complexity." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "it's just like it's it's too much complexity for not enough gain at this point" — [youtube-appearances/unknown_aR6CzM0x-g0_cuda-mode-keynote-andrej-karpathy-eureka.md](https://www.youtube.com/watch?v=aR6CzM0x-g0&t=972s) · 2024-10
- He reads framework source rather than trusting the wrapper or the docs, and falls back to trial and error when there are no docs.
  > "looking at the source of that context manager, it just toggles this variable" — [github/nanoGPT/train.py](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/train.py) · 2022-12
  > "The API is undocumented and only discoverable by trial and error." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-02
  > "as far as I can tell no one is maintaining any documentation it will lie to you it will be wrong it will be incomplete it will be unclear" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=3179s) · 2022-11
- He writes code explicitly so mistakes fail loudly.
  > "I don't super love the use of negative one because I like to be very explicit so that you get error messages when things don't go according to your expectation" — [youtube/2023-10-09_t3YJ5hKiMQ0_building-makemore-part-5-building-a.md](https://www.youtube.com/watch?v=t3YJ5hKiMQ0&t=1976s) · 2022-11

## How it shows up

- His lecture notebooks carry short log lines next to each fix.
  > "fix tanh layer too saturated at init" — [github/nn-zero-to-hero/lectures/makemore/makemore_part3_bn.ipynb](https://github.com/karpathy/nn-zero-to-hero/blob/73c3fcc741f0ec104ca850b1fb0df90e7e8d4cde/lectures/makemore/makemore_part3_bn.ipynb) · 2022-09
- He puts the validation loss into the checkpoint filename.
  > "The filename of these checkpoints contains a very important number: the **loss**." — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
  > "This number is very important because the lower it is, the better the checkpoint works." — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
- He records what he doesn't understand, not only what he does.
  > "I'm not understanding the torch.compile interaction here." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "prints ~2e-5 ( should be 0?!)" — [github/_gists/e5d58e83d9fb6ce0827f0f66b253e6fe/pytorch_strangeness.py](https://gist.github.com/karpathy/e5d58e83d9fb6ce0827f0f66b253e6fe) · 2023-06
- He takes the useful part of a borrowed idea and leaves the rest.
  > "Cherry-picked improvements from NorMuon (modded-nanogpt) into our simpler Muon implementation." — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
  > "Decided against using NorMuon directly due to hard-coded architecture assumptions" — [github/nanochat/dev/LOG.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/dev/LOG.md) · 2026-01
- He credits where an idea came from.
  > "which gamified the nanoGPT repo with clear metrics and a leaderboard, and borrows a lot of its ideas and some implementation for pretraining." — [github/nanochat/README.md](https://github.com/karpathy/nanochat/blob/92d63d4e8bb4df75c3b71618f31ddde2378b2bcd/README.md) · 2026-09
- He leaves notes for his future self in every repo.
  > "I got into the habit of creating very thorough readme.txt files in all my repos (for my personal use) as notes to future self on how the code works, how to run it, etc." — [blog/karpathy.github.io/2016__09__07__phd.md](https://karpathy.github.io/2016/09/07/phd/) · 2016-09
- He deprecates his own projects when better code exists, including other people's.
  > "In other words, torch-rnn should be the default char-rnn implemention to use now instead of the one in this code base." — [github/char-rnn/Readme.md](https://github.com/karpathy/char-rnn/blob/6f9487a6fe5b420b7ca9afb0d7c078e37c1d1b4e/Readme.md) · 2015-05
  > "nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity." — [github/nanoGPT/README.md](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/README.md) · 2025-11

## Tensions and evolution

- Deleting is hard once others depend on the code. minGPT became so widely cited that he stopped making the changes he wanted.
  > "Basically, minGPT became referenced across a wide variety of places (notebooks, blogs, courses, books, etc.) which made me less willing to make the bigger changes I wanted to make to move the code forward." — [github/minGPT/README.md](https://github.com/karpathy/minGPT/blob/37baab71b9abea1b76ab957409a1cc2fbfba8a26/README.md) · 2023-01
- In 2025 he still cleaned up agent code by hand. By 2026 he let it go in side projects.
  > "I often have to do a pass of "cleanups" for coding style, or matters of code taste." — [x/2025-08.md](https://x.com/karpathy/status/1959703967694545296) · 2025-08
  > "I'm not very happy with the code quality and I think agents bloat abstractions, have poor code aesthetics, are very prone to copy pasting code blocks and it's a mess, but at this point I stopped fighting it too hard and just moved on." — [x/2026-03.md](https://x.com/karpathy/status/2035173492447224237) · 2026-03

## Related

- [Simplicity is a constraint](../principles/simplicity-is-a-constraint.md)
- [Neural nets fail silently](../principles/neural-nets-fail-silently.md)
- [Fast feedback loops](fast-feedback-loops.md)
- [Autoresearch](autoresearch.md)
- [Show the mess](show-the-mess.md)
- [Deep work and side projects](deep-work-and-side-projects.md)
