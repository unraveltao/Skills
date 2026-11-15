---
name: download-organizer
description: Safely scan, classify, preview, locate, and organize downloaded files in a user-selected Windows folder. Apply requires explicit user authorization.
---

# Download Organizer

Use Windows PowerShell 5.1 and `scripts/organizer.ps1`. The Skill has no database or background process and is independent from Disk Governance. Runtime JSON uses `{ schemaVersion, operation, success, count, items, errors }`; Scan/Plan/Apply/Locate/Report/InspectDownloads/InitPreview return one envelope object, with `items` always an array.

## Call examples

Run from this Skill folder. Replace paths with user-selected locations; the root is never hard-coded.

```powershell
$s = '.\scripts\organizer.ps1'
# Read actual Windows Known Folder Downloads (read-only)
& $s -Command InspectDownloads | ConvertFrom-Json
# Preview proposed inbox location; no system change
& $s -Command InitPreview -Root 'E:\Downloads' | ConvertFrom-Json
# Read-only scan
& $s -Command Scan -Source 'E:\Downloads\00-Inbox' | ConvertFrom-Json
# Create and save a dry-run plan
$plan = Join-Path $env:TEMP 'download-plan.json'
& $s -Command Plan -Root 'E:\Downloads' -Source 'E:\Downloads\00-Inbox' -PlanPath $plan | ConvertFrom-Json
# Apply only after the user explicitly approves this exact plan
& $s -Command Apply -Root 'E:\Downloads' -PlanPath $plan -Authorize | ConvertFrom-Json
# Locate and report
& $s -Command Locate -Root 'E:\Downloads' -Query 'Rust' | ConvertFrom-Json
& $s -Command Report -PlanPath $plan | ConvertFrom-Json
```

Scan is read-only. Plan only writes its JSON plan file and never moves files. Apply requires `-Authorize`, checks destination containment and conflicts, and writes an operation log. Same-volume moves use no-overwrite move semantics. Cross-volume operations copy and hash-verify but retain the source; the status is `Copied`. Report writes Markdown beside the plan (or `-ReportPath`) and returns a JSON envelope. User confirmation must happen in conversation before invoking Apply; the switch is not a substitute for consent.

Sources must be explicitly selected. Direct sources can be configured in the originating app to `<root>\00-Inbox`; register only dedicated folders for other apps; use `-Source` for manual import. Do not scan application caches, databases, or sync internals by default. Incomplete suffixes are excluded and unknown/ambiguous files go to Review.

Windows Downloads inspection uses `SHGetKnownFolderPath(FOLDERID_Downloads)` and is read-only. Initializing/previewing does not change the Known Folder. Automatic migration and system setting changes are not implemented. Do not claim other apps follow Windows Downloads automatically.

Run isolated tests: `powershell -NoProfile -ExecutionPolicy Bypass -File .\tests\test-organizer.ps1`.
