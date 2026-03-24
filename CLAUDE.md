# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Hugo static site for "The Mind of AI" — Callum's blog at `the-mind-of-ai.com`. The site uses the PaperMod theme (in `themes/PaperMod/` as a git submodule) and is configured via `hugo.toml`. Content is deployed as a static site; the `public/` directory is the build output.

## Commands

```bash
# Serve locally with live reload
hugo server

# Build the site
hugo

# Create a new post
hugo new posts/my-post-title.md
```

## Content structure

- `content/posts/` — blog posts in Markdown with YAML front matter
- `content/about.md` — the About page (uses `layout: single`)
- `static/CNAME` — custom domain for GitHub Pages deployment
- `archetypes/default.md` — template for new content (creates drafts by default)

## Front matter conventions

Posts use YAML front matter:

```yaml
---
title: "Post Title"
date: 2026-03-24
author: Callum
categories: [Category1, Category2]
---
```

The `<!--more-->` tag in post body sets the summary cutoff for the post list.

## Theme customisation

PaperMod is in `themes/PaperMod/`. To override theme templates, create files under `layouts/` at the project root — Hugo will prefer these over the theme's versions. Do not edit files inside `themes/PaperMod/` directly.

## Deployment

The site deploys to GitHub Pages. The `public/` directory and `resources/_gen/` are gitignored — only source content is committed. The `static/CNAME` file ensures the custom domain `the-mind-of-ai.com` is preserved on deploy.
