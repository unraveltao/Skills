# Disk Governance Architecture

This document describes the architecture and safety boundaries of the Disk Governance Skill. It is intentionally kept inside the Skill package rather than the repository's global architecture documentation.

## Data flow

`User-named directory → metadata-only traversal that does not follow links → local SQLite batches (entries, errors, and volume information) → local workbench or self-contained offline HTML report`

The scan target and data directory are distinct. When paths overlap, the data directory is excluded from scans. Reports contain local paths and are intended to remain on the user's machine.

Scan status and recorded errors describe coverage. Permission failures and files that disappear during scanning are recorded while traversal continues. File logical size is the sum of readable files' `st_size`; volume capacity comes from the operating system. These measures are reported separately.

The current Runtime does not hash file contents. Same-size files are therefore candidates for review, never confirmed duplicates.

## Storage and consistency

SQLite is the local source of truth. Schema changes require a consistency backup and transactional migration. Report output follows the versioned ReportData contract.

Candidate records are bound to a scan batch and rule version. Risk, category, and confidence are separate fields. Human review state and event history are recorded transactionally; review does not authorize file changes. Decisions are not inherited by later batches.

## Local workbench

The workbench binds to `127.0.0.1`, checks a random session token, Host, and Origin, and serves static assets from an explicit allowlist. Offline reports need neither the workbench service nor external network requests.

## Version boundaries

- **V0.1:** read-only scanning, SQLite storage, and view-only HTML reports.
- **V0.2:** local workbench, candidate review records, and offline reports.
- **Not implemented:** file delete, move, cleanup, reclaim simulation, Planning, and Migration.

This document describes architecture and safety constraints. It is not authorization to change audited files.
