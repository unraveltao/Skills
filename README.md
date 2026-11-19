<div align="center">

<h1>Unravel Skills</h1>

<p>A curated collection of independently installable Agent Skills.</p>

</div>

<p align="center">
  <img src="web/public/brand-mark.svg" alt="Unravel Skills" width="96">
</p>

<p align="center">
  <a href="https://unraveltao.github.io/Skills/docs/"><img src="https://img.shields.io/badge/docs-Documentation-111111?style=flat-square" alt="Documentation"></a>
  <a href="https://unraveltao.github.io/Skills/"><img src="https://img.shields.io/badge/catalog-Skills-111111?style=flat-square" alt="Skills catalog"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ea44f?style=flat-square" alt="MIT License"></a>
</p>

<p align="center"><em>Build once, reuse across compatible Agents.</em></p>

Unravel Skills is a collection of self-contained Skill packages. Each Skill lives under `skills/<name>/` and contains its own instructions and, when needed, references, scripts, runtime code, UI, and tests.

## Explore

Browse the [Unravel Skills website](https://unraveltao.github.io/Skills/) to discover available Skills and read their documentation.

For project documentation, start with the [Docs](https://unraveltao.github.io/Skills/docs/).

## Repository layout

```text
.
├── AGENTS.md
├── README.md
├── docs/                 # Shared project documentation
├── skills/               # Independently installable Skills
├── web/                  # Static catalog and documentation site
└── .github/workflows/    # Verification and publishing
```

The root `docs/` directory describes the **repository as a whole**. Skill-specific architecture, usage details, references, scripts, and tests stay inside the corresponding `skills/<name>/` directory.

## Install

Copy the complete desired Skill directory into the Skills location supported by your Agent client, then read its `SKILL.md`.

For the current installation guidance and compatibility notes, see [Installation](https://unraveltao.github.io/Skills/docs/getting-started/installation/).

## Development

Read [AGENTS.md](AGENTS.md) before changing the repository. Use the project Docs for repository-level architecture and development records. For Skill-specific behavior, always use that Skill's own `SKILL.md` and supporting references as the source of truth.

## Contributing and license

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for repository and documentation standards. This repository is licensed under the [MIT License](LICENSE).
