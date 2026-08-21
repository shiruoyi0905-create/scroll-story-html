# Operational Flows

## Publish a repository change

- **Actor:** maintainer or approved contributor
- **Precondition:** write access or an accepted pull request
- **Outcome:** validated files are available from GitHub and GitHub Pages

1. A contributor changes repository files locally.
2. `scripts/validate.py` checks required HTML structure and local references.
3. GitHub authenticates the push or pull-request author and enforces repository permissions.
4. GitHub Actions runs the same structural validation.
5. A maintainer merges approved work or pushes an authorized change.
6. GitHub Pages publishes static files from `main`.

The only project side effects are Git history changes, CI runs, and public static-site deployment. A denied GitHub write must not change repository or Pages content.

## Report a security issue

- **Actor:** researcher or user
- **Precondition:** a potentially harmful issue exists
- **Outcome:** the maintainer receives details without premature public disclosure

The reporter uses GitHub's private vulnerability-reporting surface when available, as described in `SECURITY.md`. GitHub controls reporter identity, repository access, and disclosure state.
