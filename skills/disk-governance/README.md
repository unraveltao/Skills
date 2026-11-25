# Disk Governance

Disk Governance is a read-only Windows Skill for auditing directories. It records file metadata in a local SQLite database and presents results in a local workbench or a self-contained offline HTML report.

## When to use it

Use this Skill to understand space usage, find large files and directories, review file-type distributions, or inspect scan batches and audit candidates. It is not a cleanup tool: it cannot delete, move, clean up, or migrate files.

## What it does

A scan reads metadata from a directory the user explicitly selected. It does not follow symbolic links, Windows reparse points, or directory junctions. Results are stored as scan batches in a separate local data directory.

- report writes a self-contained HTML report that works offline.
- serve starts a local workbench bound to 127.0.0.1.

The database, reports, and logs can contain local file paths. Keep them on your machine.

## Quick start

These illustrative PowerShell commands should be run from the repository root, using a directory you explicitly chose:

    python .\skills\disk-governance\scripts\main.py doctor
    python .\skills\disk-governance\scripts\main.py scan --path "$env:USERPROFILE\Downloads" --data-dir "$env:LOCALAPPDATA\DiskGovernors"
    python .\skills\disk-governance\scripts\main.py status --data-dir "$env:LOCALAPPDATA\DiskGovernors"
    python .\skills\disk-governance\scripts\main.py report --data-dir "$env:LOCALAPPDATA\DiskGovernors"

Check doctor before scanning. Always pass --data-dir to scan and report; omitting it can route those commands to the legacy scanner and a different data location. report uses the most recent batch unless you provide --batch <id>.

For the full command list and workbench lifecycle, see [SKILL.md](SKILL.md) and the [Audit Workflow](references/audit-workflow.md).

## How to read results

- Scanned logical size sums st_size for files that were read; it is not allocated disk space or reclaimable space.
- Volume usage comes from the operating system and may include data the scan could not read.
- Candidate size is an estimate for review, not reclaimable space.
- Scan errors mean the report covers only the successfully read portion.
- Same-size files are not confirmed duplicates. This version does not hash file contents.
- Risk, classification confidence, and human review are separate fields; none authorizes file changes.

## Safety and validation

Version 0.2 provides read-only scanning, local SQLite storage, candidate review records, a local workbench, and offline reports. Cleanup, Planning, and Migration are not implemented. See the [Safety Policy](references/safety-policy.md) and [Roadmap](references/roadmap.md).

Validation on 2026-11-20 used Python 3.13.17 and SQLite 3.50.4. `doctor` passed; an isolated two-file scan completed; `status` and offline `report` succeeded; the source fixture remained unchanged. A generated data-directory path containing `#` also passed after correcting SQLite read-only URI construction. All nine Python sources compiled in memory. No real-client Skill activation or routing test was run.

## References

- [Skill instructions and command reference](SKILL.md)
- [Audit workflow](references/audit-workflow.md)
- [Safety policy](references/safety-policy.md)
- [Architecture](references/architecture.md)
- [Unimplemented features](references/roadmap.md)

MIT licensed; see the repository [LICENSE](../../LICENSE).

Run `python -B -m unittest discover -s tests -v` from the package directory. The follow-up SQLite regression passed on Python 3.13.17 and SQLite 3.50.4. A disposable database opened read-only from paths containing `#`, `%`, and a space. Reads returned the expected value, write attempts were rejected, and the database bytes were unchanged. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
