# Repository Structure Plan

## Confirmed direction

- The repository is personally maintained, publicly presented, and intended for independent Skill distribution.
- `skills/` contains independently installable Skill source.
- Each Skill is versioned independently and follows the standard Agent Skill format, with a generic `npx` installation path.
- The repository README explains the website; distributable packages contain only what is required at runtime.
- `web/` is reserved for future website code, `scripts/` for automation, `.github/workflows/` for future CI and release workflows, and `docs/` for a small set of shared repository documents.

## Planned migration

1. Preserve and inventory existing files before changing their locations.
2. Decide the website source and GitHub Pages build/deployment changes before moving root website files.
3. Define the Catalog generation, metadata checks, and packaging workflow.
4. Move or add files in reviewed steps, then verify website behavior and each Skill package independently.

## Open decisions

- The exact independent versioning and release convention for Skills.
- The Catalog source of truth and generation format.
- The generic `npx` installer and package layout.
- The GitHub Pages build and deployment configuration needed after a future website move.

This document records direction and future work. It does not mean the repository has already been reorganized.
