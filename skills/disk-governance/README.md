# Disk Governance

Disk Governance is a **read-only Windows disk auditing Skill**. It scans user-selected directories, records metadata in local SQLite, and presents results through a local workbench or self-contained offline HTML reports.

## What it is for

Use it when you want to:

- understand disk or directory space usage;
- find large files or directories;
- inspect file-type distributions;
- review audit candidates and historical review records.

It does **not** delete, move, clean up, or migrate files.

## Architecture

The Skill is self-contained under this directory. Its main data flow is:

`user-selected directory → metadata-only scan → local SQLite batches → workbench or offline report`

Important implementation boundaries:

- The scanner does not follow links.
- Scan targets and the local data directory are kept separate; overlapping data directories are excluded from scans.
- SQLite is the local source of truth.
- Candidate records are bound to a scan batch and rule version.
- Risk, category, confidence, and human review state are separate concepts.
- Reports may contain local paths and are intended to remain on the user's machine.
- The local workbench binds to `127.0.0.1` and uses session/origin checks.
- The current runtime does not hash file contents, so same-size files are **not** confirmed duplicates.

For the detailed implementation and safety model, read [Architecture](references/architecture.md).

## Version boundary

**v0.2** provides read-only scanning, SQLite storage, candidate review records, a local workbench, and offline reports.

Cleanup, Planning, and Migration are not implemented. The [roadmap](references/roadmap.md) records these only as future boundaries; it does not grant executable capability.

## Usage

Read [SKILL.md](SKILL.md) for triggers, workflow, commands, data semantics, and safety rules.

Supporting references:

- [Audit Workflow](references/audit-workflow.md)
- [Safety Policy](references/safety-policy.md)
- [Architecture](references/architecture.md)
- [Roadmap](references/roadmap.md)

This README is the human-facing entry point for this Skill. The root repository architecture documentation describes the **Skills repository as a whole** and intentionally does not duplicate Skill-specific architecture.
