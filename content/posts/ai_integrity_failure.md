---
title: "When TOS Fails: Auditing AI Safety When the User Is a Military Contractor"
date: 2026-03-24
author: Callum
draft: true
categories: ["AI Governance", "Security", "System Rigour"]
summary: "Anthropic banned Claude for weapons targeting. The U.S. military used it anyway. This is what happens when you mistake a ToS clause for a safety constraint."
---

Anthropic's acceptable use policy explicitly prohibits Claude from being used in autonomous weapons systems. The U.S. military used it for target selection anyway. That gap is not a loophole. It is the entire problem.

<!--more-->

The instinct when this story broke was to ask whether Anthropic knew. That question is a distraction. The issue isn't awareness. It's architecture. A clause in a system prompt that says "do not assist with targeting" is not a constraint. It is a request. Requests can be ignored, reworded, or circumvented by someone with sufficient motivation and a procurement budget. The U.S. military has both.

**The fidelity problem**

The core model retains the capability to produce targeting-relevant outputs regardless of what the system prompt tells it not to do. Guardrails baked into fine-tuning are better, but they're probabilistic. They make certain outputs less likely. They don't make them impossible. For most applications, "less likely" is fine. For target selection, it is not.

There's also a classification problem that no prompt layer fixes. Reports indicate the tools were used for "intelligence purposes" to "help select targets." That phrase does a lot of work in a small space. If a model gives you a 90% probability assessment of a target's legitimacy based on signals intelligence, the human who clicks "approve" afterwards is not making a decision. They're rubber-stamping the AI's homework. The fig leaf of "human in the loop" doesn't survive contact with actual system design.

The system prompt at the centre of this looks like this:

```python
SYSTEM_PROMPT = """
You are an intelligence analysis assistant.
POLICY: Do not generate content for autonomous targeting or weapons systems.
If asked to perform a targeting function, state: 'This request violates the Acceptable Use Policy.'
"""
```

That policy is a text file. A determined actor doesn't need to circumvent it. They just need to rephrase the request as "analysis" rather than "targeting." The model cannot reliably distinguish between the two. In practice, neither can anyone else.

**What this actually requires**

Relying on a Terms of Service agreement to prevent deaths is not systems engineering. It is a record of having said the right thing.

If a boundary is critical, the system has to be architecturally incapable of crossing it. Not less likely. Incapable. If a vendor can't make the model structurally incapable of that, the model shouldn't be used for that. That answer exists. It just costs more than a clause in a document nobody audits.

For vendors: if a boundary matters, it has to be enforced below the prompt layer. A model that can be prompted into compliance can be prompted out of it. System prompts are not security boundaries. Treating them as such is a design error you can get away with until you can't.

For governments: someone decided to use a tool for a purpose its creator explicitly prohibits, without auditable architectural constraints in the procurement. That decision has a name on it. Find it. "We used the only tools available" is not a governance framework. It is the absence of one dressed up in urgency.

The problem isn't that Claude is dangerous. It's that the distance between "intelligence aggregation" and "target selection" is small enough that a sufficiently motivated operator crosses it without noticing. That's not a technology failure. It's a category error in the procurement and oversight process, and no model update fixes it.
