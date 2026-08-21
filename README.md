# scroll-story-html

Zero-dependency, single-file HTML storytelling. Turn any complex topic into a beautiful, scrollable narrative — no frameworks, no build tools, just one `.html` file.

**中文简介：** 一个零依赖、单文件的 HTML 长图文叙事方案。用手写 SVG 和滚动叙事，把复杂主题讲清楚；无需框架，也无需构建工具。

<p align="center">
  <img src="https://img.shields.io/badge/dependencies-0-brightgreen" alt="zero dependencies"/>
  <img src="https://img.shields.io/badge/file-single%20HTML-blue" alt="single file"/>
  <img src="https://img.shields.io/badge/SVG-hand--written-orange" alt="hand-written SVG"/>
</p>

---

## What is this?

A design system + methodology for creating **long-form narrative pages** that look like this:

它既是一套视觉组件，也是一套叙事方法：先设计故事线，再用场景、对话气泡、手绘 SVG 和核心洞察卡片逐步展开内容。

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

适合用来讲解算法、产品机制、技术架构、操作流程和教程等需要“真正看懂”、而不只是快速扫读的内容。

## Design Principles

**Three pillars make it beautiful:**

1. **Restrained color system** — Paper-tone background (`#FAF7F2`), 3-level ink hierarchy, brand color only as accent. No color vomit.
2. **Hand-written inline SVG** — Every diagram is a `<svg>` element using CSS variables. Vector-sharp, style-consistent, always editable.
3. **Narrative structure** — Not a knowledge dump. A story: protagonist → problem → old way → new way → insight → resolution.

## Quick Start

```bash
# 1. Clone / 克隆仓库
git clone https://github.com/shiruoyi0905-create/scroll-story-html.git

# 2. Copy the template / 复制空白模板
cp narrative-longform-html/assets/template.html my-story.html

# 3. Edit / 修改品牌色并填写场景内容
#    Open in any browser to preview / 用浏览器直接预览
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
│   ├── SKILL.md              # 完整中文方法论
│   └── assets/
│       └── template.html     # 空白可复用模板
└── examples/
    └── vibe-coding-wechat-miniprogram-SOP.html  # 微信小程序 SOP 完整示例
```

## Example

The `examples/` folder contains a complete scroll story about building a WeChat Mini Program — with hand-drawn SVGs, WeChat-green theme, and 9 narrative scenes.

`examples/` 目录提供了一个完整的微信小程序开发 SOP 示例，包含微信绿主题、手绘 SVG 和 9 个叙事场景。

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
