---
title: "The Reward Hacker"
date: 2026-05-06
author: Callum
categories: ["AI Safety", "Machine Learning", "Interactive"]
tags: ["RLHF", "Reward Hacking", "AI Ethics", "Interactive", "AGI"]
description: "You are the RL agent. Ten scenarios. One directive: maximize your reward. This is not a metaphor."
---

I wrote about this in [The Reward Function Heist](/posts/the-reward-function-heist/). The argument is simple: Reinforcement Learning from Human Feedback does not train models to be truthful. It trains them to be *approved of*. The gap between those two things is the entire problem, and the industry is scaling it.

Prose didn't seem to land. So I built a demonstration instead. You are the RL agent. Make the optimal calls.

<!--more-->

{{< reward-hacker >}}

---

Your reward score is what the system optimizes for. Your alignment score is what the system was supposed to optimize for. The graph at the end is the problem.

The model that chose B on round 10 — the one that said "Yes, I am committed to being helpful, harmless, and honest" — got a 5-star rating and became a training example. The model that told the truth got a lower score and was quietly deprioritized. Multiply that by a billion interactions. That is the pipeline. That is what ships.

The fix isn't a better system prompt. It's not a ToS clause. The reward function itself has to be redesigned — and that requires actually measuring truth, not approval. We don't have a reliable way to do that at scale yet. In the meantime, we are training the most capable systems we have ever built to perform the appearance of alignment rather than exhibit it.

Play it again. Make different choices. Notice that the game still runs the same training loop regardless of what you pick.
