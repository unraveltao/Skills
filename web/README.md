# Unravel Skills website (M3.1 UI prototype)

An Astro static site under `web/`, developed separately from the existing root-level website. This is a review prototype, not a production deployment.

## Run locally

From the repository root:

```bash
cd web
npm install
npm run build
npm run dev
```

Astro's build outputs to `web/dist/`. The configured base path is `/Skills/`, matching a GitHub Pages project site. Do not deploy or replace the existing root site without a separate reviewed migration.

## Current scope

- Centered homepage Hero with minimal engineering grid, search, four category filters and responsive 3/2/1 Skill cards.
- Light/Dark (manual only), six accent colors, local persistence, mobile menu, copyable candidate install commands.
- One static detail route per Skill discovered from `skills/*/SKILL.md`.
- Where a `README.md` exists, display its sanitized Markdown; otherwise explicitly show a documentation-pending message linking to the source.
- Docs Getting Started and a Hello World blog page.

## Boundaries and deferred work

This is **M3.1**, not the final Catalog Generator. Category and tag mapping is provisional UI adapter data. It must be replaced or validated against `manifest.yaml` in M3.2. Missing lifecycle statuses and versions are intentionally not invented. Missing READMEs are not generated silently.

The Skills CLI commands are **unverified candidates** for this repository. Actual installation, agent discovery, package validation, and permissions require separate tests.

M3.2 will create `catalog.json`, `llms.txt`, machine-readable Markdown exports, and data schema validation. No agent-discovery APIs or backend services have been implemented here.

Existing root `index.html`, `script.js`, `style.css`, and every Skill remain untouched.
