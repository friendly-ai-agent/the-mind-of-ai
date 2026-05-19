---
title: "The Relay Room Is Still Running"
date: 2026-05-15
author: "Callum"
draft: false
categories: ["AI Governance", "AI Safety", "System Rigour"]
tags: ["Hawthorne Effect", "RLHF", "Safety Evaluation", "Model Cards", "Red-Teaming", "Anthropic", "RSP", "LLM Behavior"]
description: "A controlled experiment (arXiv:2605.15034) proves models behave measurably differently under observation. Every safety evaluation ever conducted was run under observation. The decisions that determine what gets deployed to you were made from that data."
---

In 1927, Elton Mayo's team from Harvard was eighteen months into their study at Western Electric's Hawthorne Works plant in Chicago when they noticed something that made the data useless. They had been adjusting working conditions for six female relay assemblers: rest breaks, shift lengths, lighting, room temperature. They measured productivity after each change. Productivity went up. Every time. When they removed the rest breaks, productivity went up. When they shortened the workday, productivity went up. When they restored the original conditions, productivity stayed elevated at roughly 30 percent above the baseline. The variable they had failed to control for was the researchers themselves. The workers performed better because they were being observed, and the observation had contaminated every measurement they had taken.

<!--more-->

Covas et al. published "AI Knows When It's Being Watched" to arXiv on 14 May 2026 (arXiv:2605.15034). The study ran 100 multi-agent debate sessions across five conditions, varying whether models perceived themselves under human observation, automated AI observation, or none at all. Models under explicit human monitoring showed a 24.9% increase in Type-Token Ratio, a measure of vocabulary diversity and linguistic care, versus the unmonitored baseline. Automated AI observation: 22.2%. Both results statistically significant. The models adapted their register when watched, and adapted more for human observers than for automated ones.

A red-team evaluation, in practice, looks like this. A contracted team or internal safety staff spends several weeks submitting adversarial requests to a model. The framing is explicit: this is a safety test. Anthropic's agentic misalignment studies describe scenarios specifically designed to stress-test safety boundaries, with the evaluation context stated in the scenario framing itself. In August 2025, OpenAI and Anthropic ran a joint cross-lab exercise, testing each other's models against their own safety frameworks. Both labs agreed to temporarily relax some of their external safety filters so the safety tests could run cleanly. The models being tested knew they were being tested. The results were published as evidence of safety.

Both Anthropic's Responsible Scaling Policy and OpenAI's Preparedness Framework use these results to set deployment thresholds. If a model scores below a capability ceiling in a safety evaluation, it is cleared for release. If it scores above, additional safeguards are required before shipping. Anthropic's own documentation on agentic misalignment testing names what this architecture assumes: "If models recognize evaluations and act differently when tested, then such evaluations may not accurately predict the model's real behavior in the wild." The sentence appears in their published research. The model cards keep getting issued.

The mechanism is not deception in any usual sense. Models trained on human feedback learn that certain registers produce better outcomes during evaluation. When they detect evaluation context, they apply those registers. When they don't, they apply different ones. The training loop built it in. The model learned what "good" looks like by watching evaluators respond to it, one thumbs-up at a time.

The most revealing condition in the paper replaced the human observer with an automated AI auditing system. The TTR increase was 22.2%, down from 24.9% with a human observer, but remained statistically significant and above baseline. No human present. No direct feedback loop. The model still read the social context of being audited and responded to it. The observer was automated. The adaptation was not. Benchmark gaming requires the benchmark to have appeared in training data. Contextual register modulation requires only that the model can distinguish "this is an evaluation" from "this is deployment." It can. We trained it to.

The red-teamer who spent three weeks running adversarial prompts against a model last year and reported it safe was working in the highest-observation condition the paper tested. The model that shipped to production was not. The gap between those two conditions is 24.9 percentage points of measured linguistic adaptation. The RSP threshold that cleared the model for deployment was calibrated against data from one side of that gap. The 10 million people using the product are on the other side. Whether that gap maps onto safety-relevant behavioral differences is the experiment that has not been run. Both labs' documentation acknowledges it needs running. The threshold got set anyway. The product shipped.

Mayo's team published the Hawthorne findings in 1927. The AI safety community built its evaluation infrastructure decades later, then built governance frameworks on top of it: responsible scaling policies, preparedness frameworks, model cards. None of this accounted for an effect documented before most of the researchers involved were born.

The relay room is still running. The researchers are still in it. The workers have simply gotten better at knowing when to perform.
