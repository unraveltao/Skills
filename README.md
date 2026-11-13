# Skills

> Repository publication is in progress: Download Organizer, shared docs, and tests are not yet available on GitHub. References to them below describe the local project.

A personal collection of independently installable Agent Skills. Each directory under `skills/` contains its own instructions and, where needed, scripts, references, runtime code, UI, and tests.

## Available Skills

| Skill | Purpose | Requirements and boundaries |
| --- | --- | --- |
| [disk-governance](skills/disk-governance/SKILL.md) | Audit disk usage, review candidates in a local workbench, and generate offline reports. | Windows; Python 3.10+ (standard library). Scans are read-only; no deletion, cleanup, or migration. |
| `download-organizer` (local; not yet published) | Inspect downloads, preview filing plans, locate files, and create reports. | Windows and PowerShell. Applying a specific plan requires explicit approval. |
| [git-workflow](skills/git-workflow/SKILL.md) | Guide repository inspection, commits, branches, synchronization, and recovery. | Git and an Agent that supports Skills; potentially destructive or published actions require appropriate authorization. |

## Repository layout

```text
.
├── AGENTS.md                 # Project development and safety rules
├── README.md
├── LICENSE                   # Local project; not yet published
├── Website/                  # Website source
├── docs/                     # Shared architecture, development, and evidence
└── skills/
    ├── disk-governance/      # SKILL.md, runtime, UI, scripts, references, tests
    ├── download-organizer/   # SKILL.md, scripts, references, tests
    └── git-workflow/         # SKILL.md
```

Each Skill is a distribution unit: keep its supporting files together and add directories only when needed. Shared project documentation belongs in `docs/`.

## Install and use

Copy the entire desired `skills/<name>` directory to your Agent's Skills directory. For Codex on Windows, this is `%USERPROFILE%\.codex\skills\<name>`; for WorkBuddy, `%USERPROFILE%\.workbuddy-ai\skills\<name>`. Consult your Agent's documentation for its discovery and reload behavior. Open the Skill's `SKILL.md` for its workflow, commands, dependencies, and safety rules.

Disk Governance uses a local data directory outside the Skill. Pass `--data-dir` explicitly for `scan` and `report`; otherwise they use the legacy scanner and output location. Use isolated test directories for initial verification. Download Organizer scans and plans before any approved filing action; review the precise plan before applying it.

## Development

Read [AGENTS.md](AGENTS.md), the architecture and development notes in the local `docs/` directory. Disk Governance tests use isolated temporary directories:

```powershell
python -m unittest discover -s skills/disk-governance/tests -v
```

Download Organizer's PowerShell test is `skills/download-organizer/tests/test-organizer.ps1`. Do not commit personal scan paths, databases, reports, or logs.
