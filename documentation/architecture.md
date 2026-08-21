# Architecture

## Overview

`scroll-story-html` is a zero-dependency collection of static HTML assets and authoring guidance. It has no application server, authentication, database, package runtime, analytics, or bundled secrets.

## Components

| Component | Purpose |
|---|---|
| `narrative-longform-html/SKILL.md` | Authoring method for humans and AI coding agents |
| `narrative-longform-html/assets/template.html` | Reusable single-file story skeleton |
| `examples/` | Finished stories that demonstrate the method |
| `index.html` | GitHub Pages entry point that redirects to the featured example |
| `scripts/validate.py` | Structural checks for public HTML entry points |
| GitHub Pages | Static hosting from the `main` branch |

## Trust boundaries and assumptions

- Visitors receive static files from GitHub Pages; there is no project-owned server-side trust boundary.
- Repository writes are governed by GitHub repository permissions.
- Generated story content is not sanitized by this project. Authors must review any HTML, links, scripts, or external assets before publishing.
- Examples should remain self-contained. Introducing third-party scripts or remote assets creates a new supply-chain and privacy boundary.

## Known risks

- Rendering and accessibility are not yet covered by automated browser tests.
- The structural validator does not prove semantic correctness or visual quality.
- GitHub Pages availability depends on GitHub's hosting service.

No email, scheduled work, payments, personal-data storage, or embedded agent runtime exists, so no `emails.md`, `cron.md`, or `automation.md` is required.

## Related documents

- [Flows](flows.md)
- [Permissions](permissions.md)
- [Variables](variables.md)
- [Tests](tests.md)
- [SEO](seo.md)
