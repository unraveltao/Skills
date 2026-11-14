# Skills

A personal collection of independently installable Agent Skills. Each Skill lives in its own directory under `skills/` with its instructions and supporting files.

## Available Skills

| Skill | Purpose | Requirements and boundaries |
| --- | --- | --- |
| [Disk Governance](skills/disk-governance/SKILL.md) | Audit disk usage, review candidates in a local workbench, and generate offline reports. | Windows; Python 3.10+ (standard library). Scans are read-only; no deletion, cleanup, or migration. |
| [Git Workflow](skills/git-workflow/SKILL.md) | Guide repository inspection, commits, branches, synchronization, and recovery. | Git and an Agent that supports Skills; potentially destructive or published actions require appropriate authorization. |
| [Learning Coach](skills/learning-coach/SKILL.md) | Plan learning paths, teach concepts, guide practice, organize notes, assess understanding, and resume progress. | Agent with Skill support; personal learning records are stored separately. |

## Repository layout

```text
.
├── README.md
├── Website/                  # Website source files
└── skills/
    ├── disk-governance/      # SKILL.md, runtime, UI, scripts, and references
    ├── git-workflow/         # SKILL.md
    └── learning-coach/       # SKILL.md and references
```

Each Skill is a distribution unit. Keep its supporting files together; personal learning records and disk audit data do not belong in this public repository.

## Install and use

Copy the entire desired `skills/<name>` directory to your Agent's Skills directory. For Codex on Windows, this is `%USERPROFILE%\.codex\skills\<name>`; for WorkBuddy, `%USERPROFILE%\.workbuddy-ai\skills\<name>`. Consult your Agent's documentation for its discovery and reload behavior. Open the Skill's `SKILL.md` for its workflow, commands, dependencies, and safety rules.

## Website

The static catalog source is in `Website/`. It lists Skills that are available in this repository.
