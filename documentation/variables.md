# Variables and Secrets

The project requires no runtime variables or secrets.

| Name | Used by | Scope | Source | Rotation | Risk |
|---|---|---|---|---|---|
| None | — | — | — | — | No project secret should be added to HTML or repository files |

## Pre-publish checklist

- Confirm generated HTML contains no credentials, private paths, personal data, or internal URLs.
- Review all remote scripts, fonts, images, analytics, and network requests before adding them.
- Never place API keys or tokens in a single-file story; browser-delivered files are public.
