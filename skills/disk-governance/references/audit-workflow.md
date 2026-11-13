# Audit workflow details

## Scan scope

- Scan only a directory the user explicitly named; never expand to a whole drive on your own.
- Do not follow symbolic links, Windows reparse points, or directory junctions.
- When the target overlaps the data directory, exclude the whole data-directory tree so the scan never reads its own database.
- Permission errors are recorded one by one in the error table and the scan continues; they never abort the whole run.

## Data directory layout

Under `<data>` the following are kept separate: `database/audit.sqlite3`, `reports/`, `logs/`, `backups/`, `state/`, `config/`.
Changing the data directory uses only the new location; old data is never copied or overwritten automatically. A consistency backup is written to `backups/` before any schema migration.

## Batches and reuse

- Every `scan` produces a new batch (32-hex id). `status` lists batches newest first with target path, status, file/directory counts, logical size, and error count.
- **Reuse first**: when the user only wants to look at existing results, find the batch for that target with `status`, then use `report --batch <id>` or `serve`. Do not rescan.
- `report` / `open` without `--batch` use the most recent batch.
- Candidates and human review records are bound to a batch and never inherited across batches.

## Scan integrity

A batch status is one of `complete`, `incomplete` (errors recorded), or `interrupted` (Ctrl+C).
Whenever the status is not `complete`, or `error_count > 0`, the report must state that the result covers only the successfully read part — never describe it as a complete result.

## Workbench lifecycle

- `serve` binds `127.0.0.1` and picks a free port by default. Calling it again against the same data directory reuses the running instance and returns the same URL; it never starts a second server.
- `serve` / `open` hand the page to the system browser.
- `stop` stops only the instance recorded for the current data directory. Returning `not running` when the process has already exited is normal.
- In a restricted sandbox or non-interactive environment the child process may be reaped when the launching shell exits, which makes the returned URL immediately dead. Start it as a background task instead and confirm liveness with `GET /session` returning 200.

## Troubleshooting

| Symptom | Likely cause | Action |
| --- | --- | --- |
| `status` does not show the batch just scanned | `scan` ran without `--data-dir`, so it fell through to the legacy v0.1 scanner (writing to `E:\DiskAudit`) | Re-run the scan with `--data-dir` |
| `doctor` / `serve` missing from `--help` | Help only lists legacy commands | Use the command table in SKILL.md |
| `serve` returns a URL that will not open | Child process reaped, or the port is already taken | Start in the background and verify with `GET /session`; or pass a different `--port` |
| Offline report is blank | Defect in an older `offline.py` (fixed) | Update the installed Skill copy and re-run `report` |
| `doctor` exits with code 2 | Python < 3.10 or SQLite < 3.24 | Upgrade the runtime |

## Deliberately out of scope

No file content hashing (v0.2 default), no reclaim simulation, no cleanup script generation, no modification of audited files, no network access.

