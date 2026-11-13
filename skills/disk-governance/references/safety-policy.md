# Safety policy

- The audit is read-only: target files are never modified. The database, reports, logs, backups, and service state are written to a separate local data directory.
- The data directory defaults to `%LOCALAPPDATA%\DiskGovernors` and can be set with `--data-dir` or `DISK_GOVERNORS_DATA_DIR`. Changing it does not copy existing data. When the target overlaps the data directory, the data-directory tree is excluded.
- Symbolic links, Windows reparse points, and directory junctions are not followed; a file link is never hashed as if it were an ordinary file.
- Only directories the user explicitly named are scanned; tests use isolated directories. "Run a test" is never taken as authorisation for a whole-drive scan.
- Duplicates, large files, and old files are information or candidates only, and never constitute deletion authorisation. Same size does not mean same content; a low risk level does not mean the file may be deleted.
- Candidates and human review records are bound to a scan batch; conclusions from an earlier batch are never inherited by a later one on the same path.
- When the user asks to delete, move, or clean up, the only correct response is that this Skill has no such capability. Never call `del`, `rm`, `Remove-Item`, or third-party cleanup tools to work around the restriction.
- The local service binds `127.0.0.1` only and checks the random session token and request origin. Never open a public or LAN listener, expose arbitrary file reads, shell, delete, or migration endpoints, or attempt to bypass authentication.
- A consistency backup is produced before any database migration. SQLite databases and reports contain local paths, so restrict access and keep them on this machine.
- v0.2 may store human review state and notes; "reviewed" does not mean the content is safe and does not authorise deletion.
- No cleanup or migration operation exists in this version. The offline report is a read-only snapshot that depends on neither the local HTTP service nor any external network.

