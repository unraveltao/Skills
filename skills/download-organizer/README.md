# Download Organizer

Download Organizer helps you inspect and organize files in a Windows folder that you choose. It can scan files, classify them, prepare a plan, locate files, and create a Markdown report. It uses Windows PowerShell 5.1 and has no database or background process.

## When to use it

Use this Skill to inspect a selected downloads or intake folder, group recognizable files into categories, review a proposed organization plan, locate files, or report an operation.

It does not delete files, execute downloaded programs, extract archives, change the Windows Downloads location, or migrate files automatically.

## How it works

The workflow separates inspection from changes:

1. Inspect or scan a user-selected location. Scanning is read-only.
2. Create a plan and review its proposed actions. Planning writes a JSON plan; it does not move files.
3. Apply only after the user approves that exact plan. The -Authorize switch does not replace user approval.

Unclear or conflicting files go to 99-Review. Incomplete downloads and application caches, databases, and sync internals are not treated as ordinary files to organize by default.

## Example

Run from the Skill directory and replace example paths with locations you selected:

    $script = '.\scripts\organizer.ps1'
    & $script -Command InspectDownloads | ConvertFrom-Json
    & $script -Command Scan -Source 'E:\Downloads\00-Inbox' | ConvertFrom-Json
    $plan = Join-Path $env:TEMP 'download-plan.json'
    & $script -Command Plan -Root 'E:\Downloads' -Source 'E:\Downloads\00-Inbox' -PlanPath $plan | ConvertFrom-Json

Review the plan and destinations before considering changes. Only after the user approves that exact plan may it be applied. Existing destination files are not overwritten; operations produce a JSON result and log.

## Boundaries and safety

- The user selects the source and organizer root; paths are not hard-coded.
- The Skill has no delete feature and does not execute downloaded files or archive contents.
- It does not change Windows Known Folder settings or automatically migrate files.
- Other applications may use their own download locations; check their settings.
- Reports and paths may contain local information.

The source documents currently differ on cross-volume move behavior. This README intentionally does not promise whether the source is retained; reconcile SKILL.md and references/safety-rules.md before documenting that behavior.

## Package contents

- [SKILL.md](SKILL.md) — triggers, workflow, commands, and boundaries.
- [Organizer script](scripts/organizer.ps1)
- [Categories](references/categories.md)
- [Folder rules](references/folder-rules.md)
- [Report format](references/report-format.md)
- [Safety rules](references/safety-rules.md)
- [Source discovery](references/source-discovery.md)
- [Windows Downloads setup](references/windows-download-setup.md)
- [Test script](tests/test-organizer.ps1)

## Verification

The documented test command is:

    powershell -NoProfile -ExecutionPolicy Bypass -File .\tests\test-organizer.ps1

Validation on 2026-11-20: Windows PowerShell 5.1.26100.9818; 19 passed, 0 failed, 0 skipped. The suite used isolated temporary fixtures and covered envelopes/JSON roundtrips, classification and partial-download exclusion, plan-only behavior, authorization, same-volume apply, repeat-apply safety, locate/report, outside-root rejection, and read-only Known Folder lookup. Cross-volume runtime and real-client Skill activation were not tested. See the repository [Installation guide](../../docs/getting-started/installation.md); installation and discovery vary by client.

The package contract suite was rerun on Windows PowerShell 5.1.26100.9818 with isolated fixtures. All 19 checks passed. The cross-volume copy and source-retention path was inspected in the runtime, but was not exercised across volumes. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
