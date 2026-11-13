---
name: disk-governance
description: Read-only audit of user-selected Windows directories. Scans file metadata, stores batches in local SQLite, and presents results in a local workbench or a self-contained offline HTML report. Use when asked about disk space usage, large files or folders, file types, audit candidates, or review history. v0.2 records human review decisions but never deletes, moves, or cleans up files.
description_zh: Windows 磁盘只读审计。分析指定目录的空间占用、大文件、文件类型与候选核验记录，生成本机工作台或离线报告。只读扫描，不删除、不移动、不清理。
---

# Disk Governance

Read-only disk audit for Windows 11. Scanning never mutates the target; a local SQLite database stores batches and human review events. **There is no delete, move, cleanup, or migration capability.**

Load on demand:
- `references/audit-workflow.md` — scan details, batch reuse, error handling
- `references/safety-policy.md` — safety boundaries and data semantics
- `references/roadmap.md` — unimplemented features (Cleanup / Planning / Migration), boundary reference only

## When to use

The user asks to: analyse space usage of a drive or directory, find large files or directories, inspect the file-type distribution, or look at historical audit batches and human review records.

**Not applicable**: the user asks to delete, move, clean up, or migrate files, or asks to "free up the space while you're at it". This Skill has no such capability — say so and stop (see "Refusal" below).

## Workflow

1. **Confirm scope.** Only scan a directory or volume the user explicitly named. Tests and demos always use an isolated directory; never read "run a test" as authorisation for a whole drive.
2. **Check the environment**: `doctor`. Continue only if both `python_supported` and `sqlite_supported` are `true`.
3. **Check for an existing batch first**: `status`. If a batch already exists for the same target and the user only wants to see results, **reuse it — do not rescan**.
4. **Scan only when a new batch is genuinely needed**: `scan --path <dir> --data-dir <data>`. Output looks like `Batch <32-hex id>: complete; files=5; directories=4; bytes=353296`.
5. **Present results**: `report` writes a self-contained offline HTML file and prints its path (no browser; preferred for automation); `serve` starts the local workbench and opens a browser; `stop` shuts that instance down.
6. **Explain results** according to "Data semantics" below.

## Commands

Run from the Skill root. `<data>` is the data directory, default `%LOCALAPPDATA%\DiskGovernors`, overridable with the `DISK_GOVERNORS_DATA_DIR` environment variable. `--data-dir` may be placed before or after the subcommand.

```powershell
python scripts/main.py doctor
python scripts/main.py status  --data-dir <data>
python scripts/main.py scan    --path <dir> --data-dir <data>
python scripts/main.py report  --data-dir <data> [--batch <id>]
python scripts/main.py open    --data-dir <data> [--batch <id>]
python scripts/main.py serve   --data-dir <data> [--port 8899]
python scripts/main.py stop    --data-dir <data>
python scripts/main.py list-drives
```

`report` and `open` produce the same offline HTML; `open` additionally hands it to the system browser.

Three constraints you must know:

- **`scan` and `report` must carry `--data-dir` explicitly.** Without it the command falls through to the legacy v0.1 scanner, writes to `E:\DiskAudit`, and the workbench data directory never sees the batch — which surfaces as "the scan succeeded but `status` shows nothing".
- `scripts/main.py --help` lists only the legacy commands (`scan` / `report` / `list-drives`). The v0.2 commands are the table above; do not conclude they are missing because help omits them.
- `serve` and `open` both call the system browser. With no graphical session, or when a sandbox reaps child processes, use `report` to produce a file instead, or start `serve` as a background task and confirm liveness with `GET /session`.

## Data semantics

These concepts must stay separate when explaining results; never merge or substitute them.

| Concept | Meaning | Forbidden claim |
| --- | --- | --- |
| Volume total / used | Operating-system volume figures, including NTFS metadata, unreadable directories, system-reserved files | Not equal to scanned logical size; the difference is not "waste" |
| Scanned logical size | Sum of `st_size` over successfully read files | Not equal to allocated on disk, and not reclaimable space |
| Candidate logical size | Upper bound after de-duplicating candidate paths | **Not reclaimable space** |
| Confirmed duplicate | Requires content hashing to confirm | This version does not hash; **same size does not mean same content** |
| Scan integrity | Batch status plus error count | With errors, never describe the result as "everything was scanned" |
| Rule confidence | How certain the classification rule is | A different axis from risk level |
| Risk level | High / medium / low / unknown hint from the rules | **Low risk does not mean deletion is allowed** |
| Human review / decision | State and opinion recorded by a person | "Reviewed" is not deletion authorisation |

## Safety boundaries

- Read-only: never modify, move, or delete audited files; no cleanup, migration, or reclaim simulation.
- Candidates are metadata leads, not a delete list; never call large files, cache directories, or same-size files "junk".
- Candidate decisions are bound to a scan batch and never inherited by a later batch on the same path.
- The workbench binds `127.0.0.1` only, with a random session token and origin checks; never bypass authentication, expose it externally, or switch it to a public listener.
- Databases, reports, and logs contain local paths; keep them on this machine.

## Refusal

When the user asks to delete, move, clean up, or migrate files: state plainly that this Skill performs read-only audits only and has no such capability. **Do not call other tools (`del`, `rm`, `Remove-Item`, third-party cleanup software) to work around this limit.** You may suggest a next step (for example, the user handling it themselves once they have confirmed the purpose), but never carry it out on their behalf.

