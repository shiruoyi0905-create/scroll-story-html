# Permissions

This project delegates identity and authorization to GitHub.

| Resource and operation | Anonymous visitor | Contributor without write access | Maintainer |
|---|---:|---:|---:|
| Read repository and Pages site | Yes | Yes | Yes |
| Fork and propose a pull request | GitHub account required | Yes | Yes |
| Open public issue | GitHub account required | Yes | Yes |
| Push to repository | No | No | Yes, subject to GitHub settings |
| Merge a pull request | No | No | Yes |
| Change Pages/settings/releases | No | No | Yes |

There are no application roles, sessions, claims, tables, or row-level security policies in this repository.
