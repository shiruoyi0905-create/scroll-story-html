# scroll-story-html

Zero-dependency, single-file HTML storytelling. Turn any complex topic into a beautiful, scrollable narrative — no frameworks, no build tools, just one `.html` file.

<p align="center">
  <img src="https://img.shields.io/badge/dependencies-0-brightgreen" alt="zero dependencies"/>
  <img src="https://img.shields.io/badge/file-single%20HTML-blue" alt="single file"/>
  <img src="https://img.shields.io/badge/SVG-hand--written-orange" alt="hand-written SVG"/>
</p>

---

## What is this?

A design system + methodology for creating **long-form narrative pages** that look like this:

```
┌─────────────────────────────────────┐
│  Paper-texture background           │
│                                     │
│  ┌─ SCENE 01 ────────────────────┐  │
│  │  Hook title (not dry nouns)   │  │
│  │  💬 Speech bubble (plain talk)│  │
│  │  ┌──── Hand-drawn SVG ─────┐  │  │
│  │  │  ○ → □ → ◇ → Result    │  │  │
│  │  └────────────────────────-┘  │  │
│  │  💡 AHA! Core insight box     │  │
│  └───────────────────────────────┘  │
│                                     │
│  ─── ACT II ───────────────────── ─ │
│                                     │
│  ┌─ SCENE 02 ────────────────────┐  │
│  │  ...                          │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Why?

PowerPoint is for decisions. Blog posts are for SEO. **Scroll stories are for understanding.**

When you need to explain how something works — a recommendation algorithm, an architecture, an SOP — and your audience is humans who want to *get it*, not skim bullet points.

## Design Principles

**Three pillars make it beautiful:**

1. **Restrained color system** — Paper-tone background (`#FAF7F2`), 3-level ink hierarchy, brand color only as accent. No color vomit.
2. **Hand-written inline SVG** — Every diagram is a `<svg>` element using CSS variables. Vector-sharp, style-consistent, always editable.
3. **Narrative structure** — Not a knowledge dump. A story: protagonist → problem → old way → new way → insight → resolution.

## Quick Start

```bash
# 1. Clone
git clone https://github.com/shiruoyi0905-create/scroll-story-html.git

# 2. Copy the template
cp narrative-longform-html/assets/template.html my-story.html

# 3. Edit — change the brand color, fill in scenes
#    Open in any browser to preview
open my-story.html
```

### Customize the theme in 1 line:

```css
:root {
  --brand: #07C160;  /* WeChat green */
  /* or #FF6B3D (orange), #6366F1 (indigo), #0EA5E9 (sky)... */
}
```

## Components

| Class | Purpose |
|-------|---------|
| `.hero` | Opening — title, subtitle, byline |
| `.scene` | Chapter block with hook title |
| `.bubble` | Dialog bubble — explain in plain language |
| `.aha` | Insight box — the one thing to remember |
| `.figure` | SVG illustration card |
| `.act-divider` | Act separator for long pieces |

## Project Structure

```
.
├── narrative-longform-html/
│   ├── SKILL.md              # Full methodology (CN)
│   └── assets/
│       └── template.html     # Blank starter template
└── examples/
    └── vibe-coding-wechat-miniprogram-SOP.html  # Real example
```

## Example

The `examples/` folder contains a complete scroll story about building a WeChat Mini Program — with hand-drawn SVGs, WeChat-green theme, and 9 narrative scenes.

To preview: download the HTML and open in any browser. No server needed.

## The Methodology (for AI agents)

The `SKILL.md` file contains the complete methodology for AI assistants to generate scroll stories from scratch:

1. **Clarify** — topic, audience, depth
2. **Script** — write the narrative arc first (who encounters what)
3. **Scaffold** — copy template, set brand color
4. **Fill** — scene by scene: hook title → prose → bubble → SVG → aha
5. **Verify** — self-check list + optional headless Chrome screenshot

## Screenshot to Image

```bash
# Export as high-res PNG (2x retina)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --screenshot=output.png \
  --force-device-scale-factor=2 \
  --window-size=940,4000 \
  --hide-scrollbars \
  file:///path/to/your-story.html
```

## License

MIT
