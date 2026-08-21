# Contributing

Thanks for helping make complex ideas easier to understand.

## Good contributions

- New scroll-story examples in a clearly different subject area
- Improvements to the reusable HTML template
- Accessibility, responsive-layout, and reduced-motion fixes
- Clearer narrative guidance in `narrative-longform-html/SKILL.md`
- Documentation fixes and translations

Please open an issue before making a large visual or architectural change. Small fixes can go directly to a pull request.

## Local workflow

```bash
git clone https://github.com/shiruoyi0905-create/scroll-story-html.git
cd scroll-story-html
python3 scripts/validate.py
open examples/vibe-coding-wechat-miniprogram-SOP.html
```

No package installation or build step is required.

## Pull requests

1. Create a focused branch.
2. Keep the final story self-contained unless an external asset is essential.
3. Run `python3 scripts/validate.py`.
4. Test desktop and mobile layouts in a current browser.
5. Respect `prefers-reduced-motion` when adding motion.
6. Explain what changed and attach a screenshot or GIF for visual changes.

By contributing, you agree that your contribution will be licensed under the MIT License.
