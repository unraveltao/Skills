# Unravel Skills website

The Astro site in `web/` is the published GitHub Pages source. The publishing workflow builds and deploys `web/dist/`.

## Run locally

From the repository root:

```bash
cd web
npm install
npm run build
npm run dev
```

Astro's build outputs to `web/dist/`. The configured base path is `/Skills/`, matching this GitHub Pages project site. Do not add a second website entry point at the repository root.

## Current scope

- Centered homepage Hero with minimal engineering grid, search, four category filters and responsive 3/2/1 Skill cards.
- Light/Dark (manual only), six accent colors, local persistence, mobile menu, copyable candidate install commands.
- One static detail route per Skill discovered from `skills/*/SKILL.md`.
- Where a `README.md` exists, display its sanitized Markdown; otherwise explicitly show a documentation-pending message linking to the source.
- Docs Getting Started and a Hello World blog page.

## Boundaries and deferred work

The deployed website uses the **M3.1** catalog adapter. Category and tag mapping is provisional UI data and must be replaced or validated against `manifest.yaml` in M3.2. Missing lifecycle statuses and versions are intentionally not invented. Missing READMEs are not generated silently.

The Skills CLI commands are **unverified candidates** for this repository. Actual installation, agent discovery, package validation, and permissions require separate tests.

M3.2 will create `catalog.json`, `llms.txt`, machine-readable Markdown exports, and data schema validation. No agent-discovery APIs or backend services have been implemented here.

The legacy root-level `index.html`, `script.js`, and `style.css` have been retired. `web/` is the single website source of truth.

## Docs content source

Website Docs pages are generated from Markdown under the root `docs/` tree. The navigation registry lives in `web/src/lib/docs.ts`. The former single-page Getting Started prototype is replaced by multi-page Markdown-driven Docs. Historical development records are preserved under `docs/development/`; their statements and dates are not updated or reclassified as current verification.
