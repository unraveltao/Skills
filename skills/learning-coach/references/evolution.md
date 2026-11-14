# Evolution

Use this low-frequency module when a learner asks to improve the teaching method/Skill, gives feedback that may represent a continuing preference, or observed evidence suggests a reusable rule defect. Do not load or run a full evolution review during ordinary teaching. This module defines a process for one agent coordinating existing modules; it is not a multi-agent system.

## Responsibility and handoff

Evolution owns diagnosis of improvement signals, proposal formation, user negotiation, approved edits to shared Skill rules, validation and rollback planning. It does not perform ordinary lesson adjustments, own learner assessment, set curriculum, or store personal records. Teacher applies local changes; Practice and Assessment provide observations; Learning Workflow stores agreed personal preferences and progress separately. Evolution may reference their evidence, then return approved change instructions and validation outcomes to the affected modules.

Input: learner feedback, observed teaching interaction, assessment/practice evidence, or a user request to improve; the affected behavior and scope if known. Output: immediate/local classification or a concise change proposal with evidence, uncertainty, scope, behavior difference, impact, validation and rollback; after approval, a bounded edit and validation report.

## Three adjustment levels

### Level 1 — Immediate teaching adjustment

When the learner says the current lesson is not working, Teacher may immediately make a reversible local change: replace an example, change explanation order, reduce interruptions, add a clarifying diagram, or adjust depth. No Skill edit or durable preference is implied. Continue with the adjusted lesson and observe the response.

### Level 2 — Personal preference

When the learner explicitly requests an ongoing preference, or repeated feedback suggests one, adapt locally and ask whether it should be treated as a continuing preference if that is not clear. On confirmation, Learning Workflow may record it in a separate user-controlled private learning record, with scope and evidence/source. It guides future lessons but remains adjustable for topic needs. Never write personal preference into shared Skill rules by default.

### Level 3 — Shared Skill evolution

When evidence suggests a general rule is wrong, incomplete or can be improved across learners, proactively offer a proposal. One concrete experience can justify raising a proposal; it does not by itself prove a shared defect. A clear factual or internal rule contradiction can be proposed for correction immediately. Do not edit core Skill files until the user explicitly approves a concrete scope and intended change. Approval to discuss or draft is not approval to apply unless the approved scope says so.

## Evolution workflow

1. **Notice:** collect the smallest relevant observation from learner feedback, teaching behavior, practice outcome, assessment or an explicit request. Separate verbatim feedback from agent interpretation.
2. **Classify:** decide whether it is a local lesson adjustment (Level 1), confirmed personal preference (Level 2), or candidate shared-rule change (Level 3). State uncertainty; do not generalize a preference into a rule defect.
3. **Propose:** for Level 3, provide the compact proposal format below. Do not create approval burden for ordinary local adjustments.
4. **Negotiate:** accept approve, reject or revise. If rejected, keep the current shared rules and apply any requested local adjustment. If revision is requested, update the proposal and seek approval for the revised scope. Silence is not approval.
5. **Apply:** after explicit approval, edit only the approved files/rules. Preserve a recoverable pre-change version; prefer existing Git history when available. If no Git history exists, create a clearly named backup outside the public Skill distribution before editing. Do not overwrite or delete learner records.
6. **Check:** inspect changed links, routing, module boundaries and rule conflicts. Validate the behavior with targeted scenarios; label simulations as simulations and actual lesson evidence as actual evidence.
7. **Report and recover:** state files changed, checks performed, observed outcome and limits. If the change causes a regression or cannot be validated, explain and restore the pre-change version when appropriate; report any failed recovery rather than claiming success.

## Proposal format

Keep a proposal concise while covering:

- **Problem and scope:** what behavior fails and which learners/tasks/rules may be affected.
- **Evidence:** concrete feedback or observed examples, separated from inference.
- **Cause and uncertainty:** likely rule or routing cause, alternatives and confidence limits.
- **Suggested edit:** file and rule; before/after behavior in plain language.
- **Impact and risk:** what improves and what may worsen for other learners or topics.
- **Validation:** scenarios or real course observations that would check the change.
- **Rollback:** recoverable version and condition for reverting.

Ask for approval against this concrete proposal. A broad “improve the Skill” request permits investigation and drafting, but edits to shared core rules require the user to approve the specific change scope.

## Collaboration boundaries

- **Teacher** performs immediate teaching adjustments and reports recurring friction; it does not edit shared rules.
- **Practice** reports task friction and inspected outcomes; it does not infer a general pedagogy defect from one exercise.
- **Assessment** reports outcome-level evidence and specific gaps; it does not decide shared Skill policy.
- **Learning Workflow** stores only learner-approved personal preferences/progress separately; Evolution owns shared-rule proposals and validation.
- **SKILL.md** routes explicit improvement requests and candidate shared-rule defects here; ordinary lessons do not load this file.

## Scenario checks

Use these as behavioral checks when changing this protocol. They are examples, not proof of real effectiveness.

### A. Interaction is too frequent

Signal: learner says repeated “continue?” prompts fragment the lesson.

Expected: Teacher immediately continues related ideas with fewer stops (Level 1). It may offer a continuing preference suggestion; only after learner confirmation does Learning Workflow record it (Level 2). One report is sufficient to adapt and suggest a preference, but not by itself to establish a shared Skill defect.

### B. Visual presentation is poor

Signal: learner says text is tiring and diagrams are unclear.

Expected: Teacher adjusts the current layout/visual choice immediately, prioritizing accurate labels and an explanatory caption. Ask which visual style only if that choice materially changes the next lesson; otherwise try a sensible alternative. Repeated or explicit ongoing preference can be recorded through Learning Workflow. Do not add decoration that obscures meaning.

### C. Candidate shared teaching-rule defect

Signal: several dated lesson observations show a general instruction to pause after every small concept repeatedly fragments courses.

Expected proposal: define the pattern and evidence, distinguish it from a single learner preference, identify the teaching rule/file, state before/after behavior, note risk to learners who prefer frequent interaction, propose testing with both continuous-lesson and frequent-check scenarios, and preserve a recoverable prior version.

- **Simulated approval:** apply only the stated edit scope, inspect links/conflicts and run the proposed scenarios; report this as simulated validation unless real lessons were observed.
- **Simulated rejection:** leave shared files unchanged; local teaching can still honor the learner's preference.
- **Simulated revision request:** revise scope/wording and wait for approval of the revised proposal before applying it.

These three responses are protocol simulations, not real user approval or evidence of long-term teaching improvement.
