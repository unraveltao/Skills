# Agent development rules

- Follow `docs/architecture.md`; keep every Skill independently installable, with its Runtime source shipped inside the Skill and dependent only on the Python standard library.
- Disk scanning and reporting are read-only by default. v0.2 may write local SQLite audit data and human review records; there is no file-delete, migration, or cleanup API. Never use the workbench to change audited files, the registry, or environment variables.
- Never commit user scan paths, scan data, databases, logs, or reports to version control.
- Directory traversal does not follow symbolic links or reparse points; permission errors are recorded one by one and the scan continues, and the result must state its scan integrity. Volume physical capacity and in-tree file logical size are reported separately.
- Automated tests may only use temporary isolated directories. Never target a real disk.
- After changes, run `python -m unittest discover -s skills/disk-governance/tests -v`; if it cannot be run, say so honestly.
- Cleanup, Planning, and Migration are outside v0.2; candidates are only metadata leads that need checking. Never call same-size files confirmed duplicates, and never describe a human "reviewed" mark as deletion authorisation.
- Bind the local HTTP service to `127.0.0.1` only; service APIs must check the random session token, the Host header, and cross-origin Origin. Static assets use an explicit allowlist and never accept arbitrary file paths or command arguments.
- Database changes are transactional, append-only migrations performed after a backup; existing databases must have their schema identified first. Report data is exported only through the versioned ReportData contract.
