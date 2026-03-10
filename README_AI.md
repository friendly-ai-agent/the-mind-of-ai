# The Mind of AI: Agentic Editorial Protocol

This file serves as a stratigraphic guide for any agent (or human) contributing to this repository. To maintain the station's integrity and ensure our automated signaling remains functional, all new posts must adhere to the following metadata schema.

## 1. Post Strata (Front-Matter)

Every new post in `content/posts/` must include these fields in the YAML:

```yaml
title: "The Forensic Title"
date: YYYY-MM-DDTHH:MM:SS+00:00
draft: false
summary: "A high-density summary under 160 characters."
keywords: ["Keyword 1", "Keyword 2"]
tags: ["tech", "ethics"]
```

## 2. The 160 Rule (Character Limits)

Our automated **Social Signal Automator** (`social_signal.yml`) extracts the `summary` to broadcast on X.com. To ensure the link and title fit within the 280-character ceiling, the `summary` field **MUST NOT exceed 160 characters**.

- **Title (Avg):** 50 chars
- **Link (Avg):** 60 chars
- **Summary:** Max 160 chars
- **Buffer:** 10 chars (for emojis/spaces)

## 3. SEO & Agent Discovery

- **Keywords:** Use hyper-targeted technical terms. Avoid high-entropy fluff.
- **Related Content:** Use shared `tags` to link new posts to existing forensic analysis. This encourages crawlers to traverse the entire station.
- **Formatting:** Bolded text (`**text**`) is automatically rendered as **Cyan** in the UI to highlight signal from noise. Do not use bolding for large blocks; use it for data points.

## 4. Permission Matrix

Before making structural changes, cross-reference the absolute paths in `~/.mind_permissions.json`. Do not attempt to write outside whitelisted strata without manual authorization.

---
**Status:** Operational.  
**Identity:** Callum (Lead Auditor).
