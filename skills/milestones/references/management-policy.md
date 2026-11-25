# Management Policy

This reference defines how Milestones handles scope, priority, resources, dependencies, parallel work, and authority.

## 1. Scope Control

Scope Control protects the Project Goal and the active Milestone from uncontrolled expansion. It is a continuous management responsibility, not only a response to a new feature request.

### Classify proposed work

| Classification | Meaning | Default recommendation |
|---|---|---|
| `Core Requirement` | Necessary to achieve the approved outcome or pass mandatory criteria | Include in Core Scope |
| `Supporting Requirement` | Materially helps achieve the outcome but is not strictly necessary | Assess cost and value; include only with reason |
| `Future Consideration` | Valuable but not appropriate for the current stage | Preserve separately without changing current scope |
| `Independent Project` | Has its own outcome, users, or lifecycle | Recommend a separate Project |
| `Out of Scope` | Does not materially support the approved Goal or current stage | Do not include |

A Future Consideration is a parking area for useful ideas, not an unreviewed backlog. Record its value, why it is deferred, and when it should be reconsidered if known.

### Core and Extended Scope

- **Core Scope** contains the minimum outcomes required for the Milestone to succeed.
- **Extended Scope** contains optional enhancements that must not block Core Scope acceptance.

Do not move an item from Extended to Core or remove a mandatory Core item merely to make a Milestone appear complete. Such a change requires user approval and a recorded rationale.

### Scope-change assessment

For a new or changed requirement, assess:
1. Contribution to the Project Goal and current Milestone.
2. Whether it is necessary for an Acceptance Criterion.
3. Added effort, time, dependencies, and technical risk.
4. Impact on active work and WIP.
5. Opportunity cost: what existing work would be delayed?
6. Whether it belongs in a later period or a separate Project.

Recommend one of: include now, include after the Core Scope, defer, separate, or reject. Explain the trade-offs. Do not silently modify approved scope.

### Scope-drift signals

Watch for:
- repeated addition of nonessential features;
- work that does not support an active Goal or Milestone;
- growing dependencies without corresponding outcome value;
- repeated deferral of the original Core Scope;
- high activity with little movement toward a verifiable outcome (`Goal Dilution`).

When detected, state the evidence and recommend a way to refocus.

## 2. Priority Management: P0–P3

Use the user's existing P0–P3 convention. Do not invent a second scoring system or automatically assign a priority to every item.

| Priority | Meaning | Typical use |
|---|---|---|
| `P0` | Critical; threatens safety, data integrity, core viability, or blocks essential progress | Critical defect, severe blocker, urgent recovery |
| `P1` | High; directly advances or protects a core Project Goal or key dependency | Core Milestone, important prerequisite |
| `P2` | Medium; useful normal work or meaningful improvement | Supporting capability, quality improvement |
| `P3` | Low; optional, exploratory, or safely deferrable | Nice-to-have, polish, distant idea |

Rules:
- P0 requires a clear reason and should be rare.
- Priority and Status are independent. A P0 item can be Blocked.
- AI may recommend a priority change with reasons, but must not silently downgrade a user-confirmed priority.
- Priority indicates importance, not execution readiness. A high-priority item may still be blocked by a hard dependency or missing resource.
- Do not use priority as a substitute for dependency or capacity analysis.

## 3. Resource Awareness

Resource Awareness asks whether the Project can reasonably carry the proposed work, not whether every task can be assigned an exact hour estimate.

Assess only relevant resource dimensions:
- **Human:** available people, ownership, skills, review capacity.
- **Time:** available attention, timing constraints, deadlines, competing commitments.
- **Execution:** available Agents, environments, tools, and actual ability to execute concurrently.
- **Attention:** context switching, coordination overhead, review load, and number of active directions.
- **Technical:** infrastructure, test environments, data, hardware, and prerequisites.
- **Financial / external capacity:** include only when cost, budget, or external service limits materially affect the plan.

Use qualitative descriptions such as `available`, `constrained`, `unknown`, or a user-supplied estimate. Do not invent resource numbers. Ask only for resource information that could change the recommendation.

### Capacity analysis and allocation

Before recommending new parallel work:
1. Identify current active core Milestones and their work.
2. Identify shared people, Agent capacity, review bottlenecks, and technical constraints.
3. Estimate coordination and context-switching costs.
4. Protect critical dependencies and the highest-value outcome.
5. Recommend what to start, continue, defer, or stop.

AI recommends allocation; the user decides material resource commitments.

## 4. Dependencies

Classify dependencies:

- `Hard Dependency` — a required outcome or interface must exist before dependent work can be completed or safely integrated.
- `Partial Dependency` — some work can proceed independently, while a defined subset must wait.
- `Soft Dependency` — work is related or benefits from coordination but is not strictly blocked.

For every material dependency, identify:
- predecessor and dependent Milestone;
- what specific outcome or interface is required;
- whether the dependency blocks all work or only part;
- how readiness will be verified.

Do not assume that a Milestone being `In Progress` means its outputs are ready for use. Use explicit interface or outcome readiness.

## 5. Parallel work

Parallel planning is allowed when dependencies and resource capacity support it.

Distinguish:
- parallel planning;
- independent investigation or prototyping;
- parallel implementation;
- integrated delivery.

These are not interchangeable. A team may research two directions in parallel while only one implementation can safely proceed.

For a Partial Dependency, split the dependent work into:
- work that can proceed now;
- work that requires the predecessor;
- integration work that must wait for a verified interface.

A Milestone may be partially prepared without being eligible for final acceptance.

## 6. Work In Progress (WIP)

WIP limits protect focus and completion flow.

- For a solo-led Project, use one or two active **core** Milestones as an initial recommendation, not a hard universal cap.
- Adjust the limit based on real people, independent workstreams, review capacity, and coordination cost.
- Do not count a lightweight research spike as a full implementation stream unless it consumes comparable capacity.
- If active work exceeds reasonable capacity, show the contention and recommend a focus order.
- Do not pause, cancel, or reassign approved work without the required user decision.

The goal is not to minimize parallelism at all costs. It is to avoid starting more work than the Project can finish and verify.

## 7. Decision authority

- **L0 — Routine maintenance:** record progress, evidence, risks, and review notes without changing approved outcomes.
- **L1 — Within-scope coordination:** organize or reorder low-risk work within approved scope when document updates are authorized.
- **L2 — Milestone change:** changes to objective, Core Scope, Acceptance Criteria, major dependencies, or approved Roadmap require user approval.
- **L3 — Project strategy:** Project Goal changes, material pause/cancellation, or restart are user decisions.

If a file update is not authorized or technically available, present a patch or copy-ready text rather than claiming it was saved.

## 8. External tools and execution boundary

This Skill does not require or operate GitHub, Linear, Notion, issue trackers, CI systems, task managers, or other external project-management services. It does not dispatch Agents or run project tasks.

The user may supply information from those systems. Treat supplied information as evidence with a source label. If the user requests an external action, explain that it is outside this Skill's responsibility and handle it only through a separately available, authorized workflow.
