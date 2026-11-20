# Milestones

Milestones is an AI-led, document-driven project management Skill. It helps a user turn a project goal into outcome-based Milestones, keep a Roadmap aligned with actual progress, control scope, review evidence, and recover when a plan stops being viable.

## What it does

- Creates and maintains a project Roadmap in Markdown.
- Defines Milestones around outcomes and verifiable acceptance criteria.
- Tracks progress while distinguishing verified evidence, user reports, inference, and unknowns.
- Controls scope and protects the current Project Goal from uncontrolled expansion.
- Uses the user's P0–P3 priority convention.
- Reasons about resources, dependencies, parallel work, and work-in-progress limits.
- Recommends review cadence and performs reviews when invoked.
- Preserves Baselines, important changes, decisions, and review records.
- Assesses Milestone results and requests user acceptance.
- Diagnoses significant project problems and proposes recovery plans.

## What it does not do

- It is not a task tracker or an issue/PR manager.
- It does not require GitHub, Linear, Notion, APIs, databases, or other external project-management services.
- It does not execute the project's implementation work or orchestrate other Agents.
- It does not run in the background or send reminders by itself.
- It does not change strategic goals or approve Milestone completion on the user's behalf.

## Operating model

The agreed Roadmap Markdown files are the primary project record for work managed by this Skill. Small projects can use one `ROADMAP.md`. Larger projects can use a root overview with period or workstream Roadmaps and separate history when needed.

The AI leads analysis, planning, review, and recommendations. The user retains final authority over project goals, material Milestone changes, strategic decisions, and acceptance.

## Package contents

- [SKILL.md](SKILL.md) — authoritative Agent-facing entry point.
- [Roadmap Model](references/roadmap-model.md) — data model, states, evidence, and Roadmap organization.
- [Management Policy](references/management-policy.md) — scope, priority, resources, dependencies, and parallelism.
- [Review and Recovery](references/review-and-recovery.md) — reviews, Project Health, verification, and recovery.
- [Professional Templates](references/professional-templates.md) — domain-specific outcome and acceptance guidance.
- [Roadmap templates](templates/) — reusable single-document and long-project structures.
- [Scenario test plan](tests/README.md) and [scenarios](tests/SCENARIOS.md) — manual behavior evaluations.

## Validation status

The scenario suite is a **manual behavioral evaluation**, not an automated unit-test suite. The scenarios have been authored but have not yet been run in a real Agent client with this Skill loaded. Static inspection of these files does not prove automatic triggering, runtime behavior, or cross-session recovery.

Record the Agent client, model, date, loading evidence, prompt, observed behavior, criterion-level verdict, and supporting transcript or file evidence for each real test run.

## Version

V0.1 implementation candidate. Real-client validation and user acceptance remain pending.
