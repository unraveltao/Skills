# Architecture

The repository is a monorepo: each `skills/<name>/` directory is an independent distribution unit. Its `SKILL.md` defines the trigger, workflow, and boundaries; any required scripts, Runtime source, references, UI, and tests stay inside that directory. Disk Governance's Python Runtime uses only the standard library.

## Disk Governance data flow

User-named directory → metadata-only traversal that does not follow links → local SQLite batches (entries, errors, and volume information) → local workbench or self-contained offline HTML report. The scan target and data directory are distinct; the data directory is excluded from scans when paths overlap. Reports contain local paths and are intended to remain on the user's machine.

Scan status and recorded errors describe coverage. Permission failures and files that disappear during scanning are recorded while traversal continues. File logical size is the sum of readable files' `st_size`; volume capacity comes from the operating system. These measures are reported separately. The current Runtime does not hash file contents, so same-size files are only candidates for review, never confirmed duplicates.

SQLite is the local source of truth. Schema changes require a consistency backup and transactional migration. Report output follows the versioned ReportData contract. The workbench binds to `127.0.0.1`, checks a random session token, Host, and Origin, and serves static assets from an explicit allowlist. Offline reports need neither the workbench service nor external network requests.

Candidate records are bound to a scan batch and rule version. Risk, category, and confidence are separate fields. Human review state and event history are recorded transactionally; review does not authorize file changes. Decisions are not inherited by later batches.

## Version boundaries

- V0.1: read-only scanning, SQLite storage, and view-only HTML reports.
- V0.2: local workbench, candidate review records, and offline reports. There is no file-delete, move, cleanup, or reclaim-simulation API.
- Cleanup, Planning, and Migration are unimplemented. [The roadmap](../skills/disk-governance/references/roadmap.md) records boundaries and proposals only; it does not add executable capability or authorization.

This document describes architecture and safety constraints. It is not authorization to change audited files.
