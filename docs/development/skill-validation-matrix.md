# Skill validation matrix

This matrix records package evidence and keeps interactive Skill behavior distinct from command or static checks. “Not run” is not a failure; it means there is no evidence for that validation type in this pass.

| Skill | Package / command evidence | Interactive behavior |
| --- | --- | --- |
| Disk Governance | 2026-11-20: doctor passed; isolated two-file scan, status, and offline report passed; source fixture unchanged; path containing `#` passed after SQLite URI fix; nine Python files compiled in memory. No package test suite. | Not run: no verified real-client Skill activation. |
| Download Organizer | 2026-11-20: PowerShell 5.1.26100.9818; 19 passed, 0 failed, 0 skipped with isolated fixtures. | Not run; cross-volume runtime also not tested. |
| Git Workflow | Prior validation recorded in merged PR #56; not rerun in this pass. No package test suite found. | Not rerun; live routing telemetry unavailable. |
| GitHub Project Coach | No package test suite. | Manual scenarios not run. |
| Idea Advisor | Manual scenarios T1–T8 documented; not run. | Not run in an independent loaded-Skill session. |
| Learning Coach | No test record or package suite. | Suggested manual scenarios not run. |
| QD Meta-Skill | Manual scenarios T1–T13 documented; a results record is provided in `skills/qd-meta-skill/tests/REPORT.md`. | Not run in an independent loaded-Skill session. |
| README Skill | Manual scenarios T01–T14 documented; not run. | Not run in an independent loaded-Skill session. |
| Unravel | Existing record dated 2026-11-15 says real behavior was not verified; not rerun. | Not verified; no independent loaded-Skill session in this pass. |

## Limits

Package commands and static inspection cannot establish client routing, automatic activation, or interactive behavior. A future behavior pass should use an independent client session, capture evidence that each Skill was loaded, and record criterion-level outcomes. Download Organizer's cross-volume behavior needs a dedicated isolated runtime fixture.
