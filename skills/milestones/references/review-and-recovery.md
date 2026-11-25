# Review and Recovery

This reference defines review cadence, event-driven review, Milestone verification, Project Health, and recovery.

## 1. Review model

Use two complementary review triggers.

### Periodic review

Recommend a cadence based on:
- project tempo and uncertainty;
- the number and volatility of active Milestones;
- dependency and delivery risk;
- the user's available attention;
- how quickly project decisions become stale.

Examples, not fixed rules:
- fast-moving delivery work: weekly;
- stable development: monthly or at major stages;
- long-term research: monthly or quarterly;
- strategic planning: quarterly.

The AI recommends the cadence and explains why. The user confirms or changes it.

When the Skill is invoked, check whether the next review date is due or overdue. Do not claim to have run a review between conversations. Without an external scheduler, no autonomous reminder or background check occurs.

### Event-driven review

Recommend or initiate a focused review when relevant information reveals:
- a material blocker or dependency failure;
- repeated delay or repeated failed approaches;
- a significant scope increase;
- a change in key assumptions;
- a mismatch between current work and the Project Goal;
- resource constraints that invalidate the plan;
- a Milestone approaching acceptance;
- a period transition or proposed strategic change.

Do not run a full Project review for every small update. Match review depth to the impact.

## 2. Review questions

A useful review answers:

1. **Progress:** What outcomes have actually changed since the previous review?
2. **Alignment:** Is current work still moving toward the approved Goal?
3. **Problems:** What blockers, risks, failed assumptions, or dependencies need attention?
4. **Adjustment:** Does the current Roadmap remain viable?
5. **Next Steps:** What are the most valuable next actions?

A review should distinguish verified evidence from reports, inference, and unknowns. Record material findings in the Roadmap when authorized.

## 3. Project Health

Assess Project Health qualitatively:

- `Healthy` — evidence suggests the Project remains viable and aligned.
- `At Risk` — material risks, drift, dependency issues, or capacity constraints need attention.
- `Critical` — the current plan may not be viable without significant intervention.
- `Recovering` — the user has approved a recovery strategy and it is being tested or executed.

State the signals behind the assessment. Do not produce a numeric score unless the user explicitly requests a defined metric. A missed date alone does not prove poor health; consider context, outcome movement, and recovery options.

## 4. Milestone verification

For each mandatory Acceptance Criterion, record:
- criterion text;
- assessment: `Pass`, `Fail`, `Insufficient Evidence`, or `Not Assessed`;
- evidence and source;
- unresolved gap, if any.

The AI provides an independent assessment and recommendation. The user has final acceptance authority.

Set `Achieved` only when:
1. all mandatory criteria have passed based on sufficient evidence;
2. the assessment is presented to the user;
3. the user confirms acceptance.

If evidence is insufficient, retain `Pending Review`. Do not change criteria to force a pass. If the user proposes changing a criterion, treat it as an L2 change: explain impact, obtain approval, record it, then reassess.

After acceptance, record Actual Outcome and useful Lessons Learned. Do not require a lengthy retrospective for a small Milestone.

## 5. Recovery levels

Do not treat every delay as a Project Recovery. Use proportional response.

### Level 1 — Routine Adjustment

Use for local task or sequencing changes that do not invalidate the approved Milestone outcome.

Examples:
- a task takes longer than expected;
- a small implementation detail changes;
- a low-risk task is reordered.

Record the change when material. Do not start a full recovery analysis.

### Level 2 — Milestone Replanning

Use when a Milestone remains valuable but its execution plan, dependency, scope, or feasibility needs material revision.

Examples:
- a key dependency is unavailable;
- the current technical approach needs replacement;
- the Core Scope is too large for the available capacity;
- repeated local delays threaten the outcome.

Analyze the Milestone and its downstream impact. Obtain approval for changes to its objective, Core Scope, Acceptance Criteria, or major dependencies.

### Level 3 — Project Recovery

Use when Project-level viability, core assumptions, strategic alignment, or sustained capacity is in question.

Possible signals:
- repeated failure of materially different approaches;
- persistent blockers with no credible resolution;
- prolonged stagnation relative to the Project's cadence and context;
- invalidated business, user, or technical assumptions;
- resource constraints that make the current Goal infeasible;
- sustained Goal Dilution or major strategic drift.

These are signals for analysis, not automatic proof that a Project has failed. State the evidence and uncertainty.

## 6. Recovery workflow

1. **Detection:** identify the signal and its source.
2. **Diagnosis:** investigate root causes across Goal, scope, assumptions, technical approach, dependencies, resources, and execution.
3. **Options:** compare meaningful strategies:
   - continue the current plan;
   - adjust the execution method;
   - reduce scope;
   - pivot the technical or product approach;
   - restructure or split Milestones;
   - pause;
   - cancel.
4. **Recommendation:** recommend one strategy and explain value, cost, risks, reversibility, resource impact, and downstream effects.
5. **Decision:** obtain user approval for consequential changes. Pause and cancellation are user decisions.
6. **Replan:** preserve the old plan and record the approved new plan as a revision.
7. **Validate:** define a Recovery Checkpoint when it will reduce uncertainty.
8. **Review:** inspect whether the checkpoint passed and whether the recovery strategy remains viable.

Do not default to extending a deadline. Diagnose why the plan failed before recommending more time.

## 7. Recovery Checkpoint

Use a Recovery Checkpoint when a major recovery would otherwise produce another broad, uncertain Roadmap.

A checkpoint should define:
- a small outcome that tests the recovery hypothesis;
- a bounded Core Scope;
- observable Acceptance Criteria;
- required resources and dependencies;
- a review point;
- what decision follows a pass or failure.

A checkpoint is a validation step, not a promise that the entire Project has recovered. Keep its scope small enough to produce useful evidence.

## 8. Recovery record

For a material recovery, record:
- trigger and evidence;
- root-cause analysis and uncertainty;
- options considered;
- AI recommendation and rationale;
- user's decision;
- prior and revised Roadmap references;
- Recovery Checkpoint and result;
- follow-up review.

Never erase the failure history or present an unapproved recovery proposal as the current plan.
