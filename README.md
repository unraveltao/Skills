# Skills

A personal collection of independently installable Agent Skills. Each directory under `skills/` contains its own instructions and, where needed, scripts, references, runtime code, UI, and tests.

## Available Skills

| Skill | Purpose | Requirements and boundaries |
| --- | --- | --- |
| [disk-governance](skills/disk-governance/SKILL.md) | Audit disk usage, review candidates in a local workbench, and generate offline reports. | Windows; Python 3.10+ (standard library). Scans are read-only; no deletion, cleanup, or migration. |
| [download-organizer](skills/download-organizer/SKILL.md) | Inspect downloads, preview filing plans, locate files, and create reports. | Windows and PowerShell. Applying a specific plan requires explicit approval. |
| [git-workflow](skills/git-workflow/SKILL.md) | Guide repository inspection, commits, branches, synchronization, and recovery. | Git and an Agent that supports Skills; potentially destructive or published actions require appropriate authorization. |
| [GitHub Project Coach](skills/github-project-coach/SKILL.md) | Quickly understand a GitHub repository or Gist and learn how to use its main capability. | Agent with Skill support and a way to read the supplied GitHub project. |
| [idea-advisor](skills/idea-advisor/SKILL.md) | Shape an idea into a researched, compared, decision-ready product or Skill design. | Agent with Skill support; research quality depends on available sources and tools. |
| [learning-coach](skills/learning-coach/SKILL.md) | Plan learning paths, teach interactively, organize notes, assess understanding, and resume progress. | Agent with Skill support; personal learning records stay outside the Skill package. |
| [unravel](skills/unravel/SKILL.md) | Understand a subject by unpacking its structure, relationships, principles, and mechanisms. | Agent with Skill support; research and rendered diagrams depend on available tools. |

## Repository layout

```text
.
├── AGENTS.md                 # Project development and safety rules
├── README.md
├── .gitignore
├── LICENSE
├── docs/                     # Shared architecture and readiness notes
└── skills/
    ├── disk-governance/      # SKILL.md, runtime, UI, scripts, references
    ├── download-organizer/   # SKILL.md, scripts, references, tests
    ├── git-workflow/         # SKILL.md
    ├── learning-coach/       # SKILL.md and references
    ├── github-project-coach/ # SKILL.md
    ├── idea-advisor/         # Product-design advisor, references, templates, scenarios
    └── unravel/              # Concept and mechanism explainer with adaptive interaction
```

Each Skill is a distribution unit: keep its supporting files together and add directories only when needed. Shared project documentation belongs in `docs/`.

For the current per-Skill usability and delivery-candidate review, see [Skill readiness](docs/development/skill-readiness.md). It distinguishes structural review from real-agent behavior validation; a listed Skill is not automatically behavior-tested.

## Install and use

Copy the entire desired `skills/<name>` directory to your Agent's Skills directory. For Codex on Windows, this is `%USERPROFILE%\.codex\skills\<name>`; for WorkBuddy, `%USERPROFILE%\.workbuddy-ai\skills\<name>`. Consult your Agent's documentation for its discovery and reload behavior. Open the Skill's `SKILL.md` for its workflow, commands, dependencies, and safety rules.

Disk Governance uses a local data directory outside the Skill. Pass `--data-dir` explicitly for `scan` and `report`; otherwise they use the legacy scanner and output location. Use isolated test directories for initial verification. Download Organizer scans and plans before any approved filing action; review the precise plan before applying it.

## Development

Read [AGENTS.md](AGENTS.md) and [architecture](docs/concepts/architecture.md). Follow each executable Skill's own test instructions and use isolated temporary directories. Download Organizer's PowerShell test is `skills/download-organizer/tests/test-organizer.ps1`. Do not commit personal scan paths, databases, reports, or logs.

