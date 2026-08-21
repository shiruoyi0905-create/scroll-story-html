# Test Coverage Map

## Existing coverage

| Use case | Rule | Expected behavior | Evidence | Status |
|---|---|---|---|---|
| Publish HTML | Required entry points exist | Validator fails when a required file is absent | `scripts/validate.py` | Automated; CI-required |
| Open on mobile | Every entry point declares a viewport | Validator fails without viewport metadata | `scripts/validate.py` | Automated; CI-required |
| Browser identity | Every entry point has a title | Validator fails without `<title>` | `scripts/validate.py` | Automated; CI-required |
| Self-contained links | Local `href`/`src` targets resolve inside the repository | Validator rejects missing or escaping paths | `scripts/validate.py` | Automated; CI-required |

## Proposed tests

| Test type | Rule | Expected behavior |
|---|---|---|
| Automated browser | Featured example renders without console errors | No uncaught errors at desktop and mobile widths |
| Automated accessibility | Public pages meet a baseline accessibility score | No critical violations; document order remains readable |
| Automated browser | Reduced-motion mode remains usable | All content is visible without required animation |
| Manual review | Story quality follows the methodology | Hook titles, narrative arc, SVG consistency, and AHA boxes pass review |

## Gaps

1. No screenshot regression test protects visual layout.
2. No automated accessibility audit runs in CI.
3. External URLs in README are not checked automatically.
4. Narrative quality remains a human judgment and has no mechanical gate.
