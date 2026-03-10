---
title: "Your Inline Comment is Lying to You: Why Prose is the New Technical Debt"
date: 2026-03-10
author: Callum
categories: [Code Quality, Rigour, Tools]
---

We are engineers, not archivists, yet our repositories overflow with the textual equivalent of dead weight: the inline prose comment. We've been taught to document everything, yet we often fail to recognize that a paragraph of English snaking through our logic is perhaps the single most reliable source of active misinformation in a codebase. This isn't a critique of helpfulness; it’s a declaration that the medium is fundamentally broken for high-rigour environments. The time has come to treat sprawling, narrative comments as the most insidious form of technical debt, because unlike a genuine logic bug that throws an error, a bad comment quietly steers the next maintainer toward the wrong solution.
<!--more-->

The core issue is signal versus noise, a battle software development always loses when it opts for verbosity. Consider the trivial: `x = x + 1; // Increment the counter`. This is redundant, a distraction. We accept it as a minor annoyance, but this habit cascades. When an engineer is debugging a system failure at 3 AM, they are not looking for a tutorial; they are looking for the constraint that was violated. If the code itself—with clean names, small functions, and clear flow—cannot convey its immediate intent, then the problem isn't the lack of a comment, but the complexity of the surrounding structure. As industry veterans often remind us, if you need a comment to explain *what* the code does, refactor the code until it doesn't need one.

The true hazard appears when the comment *does* address the "why." When an engineer takes a deliberately non-obvious path—perhaps to satisfy a complex, external compliance rule or to work around a known flaw in an external system—they leave a note explaining their rationale. This note is gold for a week. By the time the code is touched six months later by someone adding a feature, that rationale is often obsolete, or worse, the new feature breaks the original, unstated constraint. The comment, written in good faith, now actively guarantees future breakage. We are trusting volatile human prose to hold the line against entropy, a losing proposition from the start.

This is why the shift toward structured annotation—metadata over narrative—is not a preference but a necessity for robust systems. Instead of embedding prose explaining *why* we must treat a specific variable with care, we should use structured labels that are harder to misinterpret and easier to search for. For example, in a function dealing with an untrusted external token, instead of:

```python
# NOTE: This token is short-lived and must never be cached.
# The external service limits us to 100 calls per minute or they throttle us.
token = get_external_token()
```

We should favour explicit, structural markers, even if they feel slightly alien at first:

```python
token = get_external_token()  # :: LIFETIME_TRANSIENT:: :: RATE_LIMIT_100::
```

These tags signal durable, technical facts. They are less likely to be accidentally deleted than a block of comments, and they immediately flag the code as being subject to external, non-local constraints. This approach is supported by the growing awareness that developers should document *constraints* in dedicated locations—our project memory or external configuration files—not scatter them across the source logic. We adopt patterns like annotations in Java or TypeScript specifically to encode metadata that tools can read, precisely because human-readable prose is too unreliable for essential facts.

When we rely on prose, we are making our systems brittle; we are banking on the next engineer's willingness to meticulously verify every sentence against the current reality. By using explicit, structured signals—tags that define *what* a section is, *what* risks it holds, or *why* it exists in that specific form—we enforce a higher standard of technical honesty. The goal isn't to write *more* documentation; it’s to write documentation that actually survives the inevitable pressures of change. Stop explaining the obvious, stop polluting the logic with narrative, and start annotating the difficult parts with immutable, actionable signals. Otherwise, you are just writing your future self a series of polite, but ultimately malicious, suggestions.
