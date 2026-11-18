# Unravel Skills Architecture

Unravel Skills separates **Skill packages** (the installable instructions) from **the website** (a static catalog and documentation reader).

## Repository responsibilities

| Directory | Purpose |
| --- | --- |
| `skills/<slug>/` | Independent Skill package with `SKILL.md` and optional resources |
| `web/` | Astro site: Skills catalog, details, Docs, Blog |
| `docs/` | Project guides, concepts, references, development records |
| `scripts/` | Repository automation as introduced |
| `.github/workflows/` | Verification and publishing |

The root `AGENTS.md` defines engineering safety constraints; each Skill's `SKILL.md` defines its own workflow.

## Current website data (M3.1)

Astro finds folders with `SKILL.md` at build time and uses source metadata. Detail pages render `README.md` where available. Categories and tags are provisionally mapped by the website code, not yet a validated contract.

The website is **static**. It does not run an Agent, scan a visitor's disks, or install packages on their machine.

## Planned catalog generation (M3.2)

A future build-time generator is intended to validate `SKILL.md`, `README.md`, and manifests, then export `catalog.json`, `llms.txt`, and Markdown. These are **not currently implemented**, and publication alone cannot force clients to discover Skills.
