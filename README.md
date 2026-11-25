<div align="center">
  <img src="web/public/brand-mark.svg" alt="" width="84">
  <h1>Unravel Skills</h1>
  <p><strong>Pick a Skill for the task at hand.</strong></p>
  <p>Install a reusable workflow for development, learning, planning, or everyday utilities.</p>
  <p>
    <a href="https://unraveltao.github.io/Skills/skills/"><img src="https://img.shields.io/badge/Browse-Unravel_Skills-6D28D9?style=flat-square" alt="Browse Unravel Skills"></a>
    <a href="https://unraveltao.github.io/Skills/docs/getting-started/installation/"><img src="https://img.shields.io/badge/Guide-Installation-0369A1?style=flat-square" alt="Installation guide"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-15803D?style=flat-square" alt="MIT License"></a>
  </p>
</div>

## Start with what you want to do

| I want to… | Try this Skill | Category |
| --- | --- | --- |
| Understand an unfamiliar GitHub project | [GitHub Project Coach](https://unraveltao.github.io/Skills/skills/github-project-coach/) | `Development` |
| Build a learning plan and pick up where I left off | [Learning Coach](https://unraveltao.github.io/Skills/skills/learning-coach/) | `Learning` |
| Turn a rough idea into a plan I can review | [Idea Advisor](https://unraveltao.github.io/Skills/skills/idea-advisor/) | `Planning` |
| Find what's using space on my Windows drive | [Disk Governance](https://unraveltao.github.io/Skills/skills/disk-governance/) | `Utilities` |
| Review, improve, or draft a project README | [Unravel README Skill](https://unraveltao.github.io/Skills/skills/readme/) | `Development` |
| Draft a project README | [Awesome Copilot create-readme](https://unraveltao.github.io/Skills/docs/guides/create-readme/) | External · `Documentation` |

**Explore more** through the [Unravel catalog](https://unraveltao.github.io/Skills/skills/) for Skills maintained in this repository or [Curated Skills](https://unraveltao.github.io/Skills/curated/) for external projects maintained by their authors. Curated listings distinguish a project-page review from Skill testing.

## Install one Skill

1. **Read its instructions.** Open the Skill's README and `SKILL.md` to check requirements, usage, and limits.
2. **Copy the whole folder.** Put `skills/<name>/` in the location your Agent client uses for Skills. Keep the supporting files together.
3. **Confirm it loads.** Reload the client if required, then try a read-only request that matches the Skill.

> [!NOTE]
> The [installation guide](https://unraveltao.github.io/Skills/docs/getting-started/installation/) covers client locations and compatibility. The repository's candidate CLI command still awaits an end-to-end installation test.

## Work on a Skill

Read [AGENTS.md](AGENTS.md) first. Keep each Skill independently installable by storing its instructions, references, runtime code, UI, and tests in its own directory as needed. Use that Skill's `SKILL.md` and supporting files as the source of truth for its behavior.

<details>
<summary><strong>Repository map</strong></summary>

| Path | Contents |
| --- | --- |
| [`skills/`](skills/) | Independently installable Skill packages |
| [`docs/`](docs/) | Shared guides, architecture, and development records |
| [`web/`](web/) | Public catalog and documentation site |
| [`.github/workflows/`](.github/workflows/) | Verification and publishing workflows |

</details>

[Project docs](https://unraveltao.github.io/Skills/docs/) · [Contributing guide](CONTRIBUTING.md) · [Contributors](CONTRIBUTORS.md)

This repository is licensed under the [MIT License](LICENSE).
