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

## Start with a task

| I want to… | Start with |
| --- | --- |
| Understand an unfamiliar GitHub repository | [GitHub Project Coach](skills/github-project-coach/README.md) |
| Build a learning plan and resume it later | [Learning Coach](skills/learning-coach/README.md) |
| Turn a rough idea into a design I can review | [Idea Advisor](skills/idea-advisor/README.md) |
| Find what's using space in a Windows folder | [Disk Governance](skills/disk-governance/README.md) |
| Review or improve a project's README | [README Skill](skills/readme/README.md) |

Browse the [Unravel Skills catalog](https://unraveltao.github.io/Skills/skills/) for Skills maintained here, or [Curated Skills](https://unraveltao.github.io/Skills/curated/) for projects maintained by their original authors.

## Install one Skill

1. Open the Skill's README and `SKILL.md` to check its requirements and limits.
2. Copy the complete `skills/<name>/` directory into the Skills location supported by your Agent client.
3. Reload the client if required and try a read-only request that matches the Skill.

See the [installation guide](https://unraveltao.github.io/Skills/docs/getting-started/installation/) for compatibility and how to check whether your client loaded the Skill.

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

## Development

Read [AGENTS.md](AGENTS.md) before changing the repository. Use the project Docs for repository-level architecture and development records. For Skill-specific behavior, always use that Skill's own `SKILL.md` and supporting references as the source of truth.

## Contributing and license

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for repository and documentation standards. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for contributor acknowledgments. This repository is licensed under the [MIT License](LICENSE).
