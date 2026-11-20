# Roadmap Model

This reference defines the project records used by Milestones. It is a logical model, not a requirement to create one file per object.

## 1. Core concepts

| Concept | Meaning |
|---|---|
| Project | A sustained body of work with an intended outcome |
| Goal | The value or end state the Project exists to achieve |
| Roadmap | The current plan for reaching the Goal through outcome-based Milestones |
| Milestone | A meaningful, verifiable stage outcome |
| Task | An execution item that contributes to a Milestone; this Skill does not replace a task tracker |
| Evidence | Information supporting an assessment of an outcome or criterion |
| Decision | A consequential choice and its rationale |
| Change | A recorded change to an approved plan or decision |
| Review | A periodic or event-driven assessment of Project health and progress |
| Risk | An uncertain event or condition that may affect an outcome |
| Resource | A relevant constraint on people, time, attention, execution capacity, or technical capability |
| Recovery Checkpoint | A small, verifiable outcome used to test a recovery strategy |

A Milestone is an outcome node, not a calendar period or a list of activities. Dates may support planning, but a date passing does not determine completion.

## 2. Roadmap organization

Choose the smallest structure that remains readable and maintainable.

### Single-document Roadmap

Use one `ROADMAP.md` when the Project is small, short, or has a limited number of related Milestones.

It can contain:
- Project overview and Goal;
- approved Baseline;
- current Milestones;
- dependencies, risks, and resource constraints;
- current status and next actions;
- material change history;
- review notes.

### Long or complex Project

When one file becomes difficult to navigate, use a root `ROADMAP.md` as the current overview and split detailed planning into period or workstream files.

Example:

```text
Project/
├── ROADMAP.md
├── Roadmaps/
│   ├── 2026-Q4.md
│   └── 2027-Q1.md
├── History/
│   ├── CHANGELOG.md
│   └── REVIEWS.md
└── Archive/
    └── Previous-Roadmaps/
```

Do not create this structure by default. Split only when the project’s complexity, document size, independent workstreams, or historical record makes it useful. Avoid duplicating the same current facts across files; the root overview should summarize and link to detailed records.

### Period changes and carryover

When a Milestone crosses a quarter, year, or other planning period:
1. Keep its stable ID.
2. Preserve its original objective, approved scope, progress, evidence, and history.
3. Record why it was not completed in the original period.
4. Reassess whether the Milestone remains valuable and feasible.
5. Reference or carry it into the new period without silently creating a duplicate.
6. Obtain approval before materially changing its objective or Acceptance Criteria.

## 3. Baseline and versions

Maintain three distinct views:

- **Baseline:** the initial Roadmap or later strategic baseline explicitly approved by the user.
- **Current Roadmap:** the currently approved plan.
- **Change History:** material changes and their reasons, impacts, recommendations, and decisions.

A baseline is a reference for comparison, not an immutable constraint. A new strategic baseline may be approved when the Project Goal genuinely changes. Preserve the previous baseline and explain why it was superseded.

Use lightweight version labels such as `R0`, `R1`, or dated revisions. Do not create a new version for every routine progress update. Create a revision when the approved plan materially changes.

## 4. Stable identifiers

Assign stable IDs such as `M001`, `M002`, and `M003`. Do not renumber existing Milestones when order changes. Never reuse an ID after a Milestone is cancelled or superseded.

For major decisions and changes, use readable IDs such as `D001` and `C001` when a sequence is useful. IDs are references, not a requirement for a database.

## 5. Project and Milestone lifecycle

### Project lifecycle

- `Active` — work is currently being pursued.
- `Paused` — the user has approved a pause.
- `Completed` — the user confirms the Project Goal has been achieved or the Project has reached its defined end state.
- `Cancelled` — the user decides to stop the Project.

### Milestone status

| Status | Meaning |
|---|---|
| `Planned` | Approved or proposed for a future stage, not yet active |
| `In Progress` | Work toward the outcome is active |
| `Blocked` | A material blocker prevents required progress |
| `Pending Review` | The work is reported ready for assessment or awaits evidence/user acceptance |
| `Achieved` | Required criteria passed and the user confirmed acceptance |
| `Deferred` | The Milestone is intentionally postponed |
| `Cancelled` | The user approved stopping this Milestone |

Do not infer `Achieved` from closed tasks, elapsed time, optimistic reports, or a percentage.

## 6. Evidence model

Every material progress claim should be labeled by evidence strength:

| Label | Meaning | Treatment |
|---|---|---|
| `Verified` | Directly inspected artifact, reproducible result, or test evidence is available | Can support a criterion assessment |
| `Reported` | The user or another named source says it happened, but the result has not been independently inspected | Record honestly; do not relabel as Verified |
| `Inferred` | AI conclusion drawn from indirect information | Explain reasoning; not proof of completion |
| `Unknown` | No reliable information is available | Do not guess; identify the smallest useful check |

For each important evidence item, record its source and date or context when known. Evidence can be a test result, running demonstration, approved document, published artifact, or other outcome-specific proof. Do not demand formal artifacts for every trivial update.

### Criterion assessment

Assess each Acceptance Criterion as:
- `Pass` — evidence supports that the criterion is met;
- `Fail` — available evidence shows it is not met;
- `Insufficient Evidence` — the criterion may be met, but proof is missing or inconclusive;
- `Not Assessed` — it has not yet been evaluated.

A Milestone cannot be presented as fully verified when any mandatory criterion is Fail, Insufficient Evidence, or Not Assessed. The AI provides an assessment; the user gives final acceptance. If the user wants to change a criterion, record and approve that change before reassessing.

## 7. Milestone definition

A Milestone should be complete enough to manage but not a long specification.

Required:
- `ID`
- `Title`
- `Objective` — why this stage matters;
- `Expected Outcome` — what should exist or be true when complete;
- `Core Scope` — the minimum work/outcomes required;
- `Acceptance Criteria` — observable conditions that prove the outcome;
- `Status`

Optional or conditional:
- `Extended Scope`
- `Priority` (P0–P3)
- `Dependencies`
- `Target Date`
- `Risks & Blockers`
- `Evidence`
- `Actual Outcome`
- `Review / Lessons Learned`

Keep the distinction clear:
- Objective: why are we doing this?
- Expected Outcome: what will be true or available?
- Acceptance Criteria: how will we know it is true?

## 8. Project Health

Project Health is separate from Project lifecycle and Milestone status.

- `Healthy` — evidence suggests the Project remains viable and aligned.
- `At Risk` — material risks, drift, dependency issues, or capacity constraints need attention.
- `Critical` — the current plan may not be viable without significant intervention.
- `Recovering` — the user has approved a recovery strategy and it is being tested or executed.

Project Health is a reasoned qualitative assessment, not a precise score. State the signals and uncertainty behind it. Do not label a Project Critical solely because a date slipped.

## 9. Progress representation

Prefer outcome and criterion status over a single completion percentage. If a user requests a percentage, explain what it measures and its limitations. Do not present an arbitrary percentage as objective progress.

## 10. Source-of-truth boundary

For Projects managed by this Skill, the agreed Roadmap Markdown is the primary record maintained by the Skill. User-provided external records may be inputs or evidence, but the Skill does not integrate or synchronize external systems.

If two records disagree:
1. State the conflicting claims and their sources.
2. Do not silently merge or overwrite them.
3. Ask which record should govern the Project if the authority is not already clear.
4. Record the resolution in the Roadmap when authorized.
