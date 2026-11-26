# Task Manager

A small, read-only Skill for reviewing and planning from an existing Notion Tasks database.

## V0.1 scope

- `/task-report [period]`: summarize completed work using `Status = Done` and `Completed At`.
- `/task-today`: show in-progress, blocked, and today's planned tasks.
- `/task-plan`: review future-dated and unscheduled Todo tasks.

## Data model

Uses the existing Notion Tasks database. It does not create a new database or modify existing records.

| Property | Meaning |
| --- | --- |
| Task | Task title |
| Status | Todo / In progress / Blocked / Done |
| Priority | P0 / P1 / P2 (P3 retired) |
| Plan Date | Intended execution date |
| Due | Deadline |
| Completed At | Actual completion date, when recorded |

## Safety

V0.1 is read-only. It does not create, update, delete, complete, reprioritize, or reschedule tasks. It does not sync calendar events. Missing completion dates are reported as missing, never guessed.

## Manual acceptance scenarios

1. **Today:** include all In progress and Blocked tasks, plus Todo tasks whose Plan Date is today; keep the three groups distinct.
2. **Past:** include only Done tasks in the requested period according to Completed At; do not claim a date for Done tasks with an empty Completed At.
3. **Future:** separate Todo tasks with future Plan Dates from Todo tasks with no Plan Date; do not treat Due as Plan Date.
4. **Read-only:** after all three commands, verify that no database record or property changed.
5. **Unavailable source:** if Notion cannot be queried, report the failure without inventing records or counts.

These are manual scenarios; runtime execution has not yet been performed.
