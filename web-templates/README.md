# web-templates/ — Public Webpage Template Assets

> **Historical template source.** The examples below document the former
> child-repository publishing workflow. Find each former project in the
> [FoundRy capability directory](../capabilities/README.md). The public site
> is maintained in the [storefront repository](https://github.com/OKHP3/glee-fullytools).
> Keep these templates outside the FoundRy application's serving allowlist.

---

## Purpose

`web-templates/` is the design and frontend asset library for the Glee-fully public
website ecosystem. When a new Tool-ette is built and canonized via the PromptChain,
it eventually needs a public landing page. This folder provides the HTML/CSS/JS
template infrastructure, brand system, and content specifications that child repos
use to build those pages consistently.

All files here are **outputs of this workbench, consumed by child repos** — they
originate here but are deployed elsewhere. This workbench (the FoundRy) never serves
web content directly.

---

## File Structure

```
web-templates/
├── index.html                           # Tool-ette page template (fill placeholders)
├── theme.css                            # Root-level brand CSS (duplicate of assets/css)
├── tool-and-tool-ette-page-updates.md   # Page update log — all Tool and Tool-ette content
├── assets/
│   ├── css/
│   │   └── theme.css                    # Brand CSS at canonical asset path
│   ├── js/
│   │   └── app.js                       # Scroll-reveal, mobile nav, footer, Ko-fi widget
│   └── img/                             # Image assets for pages
```

---

## File Summaries

### `index.html` — The Page Template

The canonical HTML template for a Tool-ette public landing page. Contains:

- **Meta tags** — Open Graph, Twitter Card, SEO description
- **Nav** — Glee-fully brand navigation with suite links
- **Hero section** — Tool-ette name, tagline, and ChatGPT launch button
- **Features section** — Primary functions and capabilities
- **How It Works** — step-by-step explainer
- **FAQ section** — common questions
- **Footer** — brand attribution and cross-links

**Placeholder variables to replace:**

| Placeholder | Replace With |
|-------------|--------------|
| `[TOOL-ETTE NAME]` | The actual Tool-ette name (e.g., "Resume Builder") |
| `[Parent Tool Name]` | The parent Tool branch name |
| `YOUR-GPT-ID-HERE` | The ChatGPT custom GPT URL or ID |
| Meta description | Tool-specific 160-char description |
| `og:url` | The live published URL for this page |

---

### `theme.css` / `assets/css/theme.css` — Brand System

The Glee-fully CSS design system. Defines:

**Typography:**
| Role | Font |
|------|------|
| Headings (H1–H3) | Fredoka |
| Subheadings | Poppins |
| Body text | Open Sans |
| Accent / UI | DM Sans |

**Color Palette:**
| Token | Value | Usage |
|-------|-------|-------|
| `--accent` | `#c46a2c` | Rust-orange — buttons, links, highlights |
| `--bg` | `#f6f2ee` | Paper — page background |
| `--text` | `#2d2013` | Deep brown — primary text |

**Brand Features:**
- **Retro rainbow hero stripe** — animated spectrum gradient across hero sections
- **`glee-main` body class** — activates all Glee-fully brand overrides
- **Card components** — feature cards, Tool-ette tiles, function lists
- **Mobile-responsive nav** — hamburger menu, collapsed states

---

### `assets/js/app.js` — Page Behavior

JavaScript for:
- **Scroll-reveal animations** — elements fade in as user scrolls
- **Mobile navigation** — hamburger toggle, focus trap
- **Footer year** — auto-updates copyright year
- **Ko-fi widget** — supporter/donation button integration

---

### `tool-and-tool-ette-page-updates.md` — Content Catalog

A ~4,861-line document containing the full content specification for every Tool and
Tool-ette page in the public site. Each entry includes:
- Full description (public-facing)
- Primary functions list
- Parent/child links
- Elevator pitch

This document is the **primary content source** for building or refreshing individual
Tool-ette pages. It mirrors and extends `inventory/inventory-of-toolbox-tools-and-tool-ettes.md`
with web-ready content formatting.

---

## Historical template workflow

### Building a New Tool-ette Page (for a child repo)

1. Copy `index.html` and the full `assets/` folder to the child repo's `web/` directory
2. Find and replace all `[TOOL-ETTE NAME]` and `[PARENT TOOL]` placeholders
3. Update the ChatGPT launch button `href` with the live GPT URL
4. Update Open Graph tags (`og:title`, `og:description`, `og:url`, `og:image`)
5. Pull the Tool-ette's content from `tool-and-tool-ette-page-updates.md`
6. Add any Tool-ette-specific sections between the template sections
7. Verify the page renders correctly with the Glee-fully brand system active

### Updating the Brand System

Changes to `theme.css` or `app.js` should be made here first, then propagated
to all child repos that have deployed a copy.

---

## What No Longer Lives Here

Three `.docx` narrative documents previously stored in this folder have been
relocated to `docs/` where they belong:

- `brand-origin-story.docx` → `docs/brand-origin-story.docx`
- `gleefully-narrative-overview.docx` → `docs/gleefully-narrative-overview.docx`
- `gleefully-technical-overview.docx` → `docs/gleefully-technical-overview.docx`

These are narrative/brand content documents, not web template assets.

---

## Relationship to Other Folders

```
web-templates/    <-- content sourced from --> inventory/ (entity descriptions + elevator pitches)
web-templates/    <-- content sourced from --> docs/ (narrative + technical overviews)
web-templates/    <-- tone governed by     --> vernacular/ (Glee-fully voice rules)
web-templates/    <-- entity links from    --> canon/dataledger-registry-v3.md
web-templates/    <-- deployed to          --> child repos: glee-fully-gpt00-* through gpt07-*
web-templates/    <-- NOT served from      --> this workbench (Glee-fullyTools-FoundRy)
```

---

## Historical deployment context

```
This Workbench (FoundRy)         →  template assets originate here
        |
        v
Child Repos (glee-fully-gpt01-* through gpt07-*)
        |
        v
Public Site: glee-fully.tools   →  deployed pages served from here
```

This workbench is upstream of the public site. Changes here must be manually
propagated to the child repos that serve them.
