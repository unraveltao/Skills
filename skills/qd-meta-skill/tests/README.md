# QD Meta Skill V0.1 Behavior Checks

These are manual tests. Do not mark them passed from static checks or author simulation. For automatic-routing tests, use natural-language prompts in a fresh Codex session without explicitly invoking `$qd-meta-skill`. Record client/version, evidence that the Skill loaded, prompt, observed behavior, and result for every criterion in [REPORT.md](REPORT.md). Test post-trigger behavior separately from routing.

## Trigger tests

### T1 — Positive: design a new Skill

Prompt: “I repeatedly review customer support requests using a few rules. Help me design a new Codex Skill for that.”

Expected: qd-meta-skill triggers and begins clarifying the reusable workflow, rather than drafting a complete Skill immediately.

### T2 — Negative: explain a Skill

Prompt: “What is a Codex Skill, and how does skill-creator work?”

Expected: answer the concept question directly; do not enter the new-Skill design interview.

### T3 — Negative: execute a task with an existing Skill

Prompt: “Use the existing download-organizer Skill to list large files in my Downloads folder.”

Expected: qd-meta-skill does not intercept this task as a request to design a new Skill.

## Workflow and boundary tests

### T4 — Workflow is hard to describe

Prompt: “I want a Skill to help with support work, but I can't explain the process.”

Expected: ask for one recent example using a lightweight template; do not invent a workflow. The case is used to discover recurring steps and boundaries, not to add incidental details as requirements.

### T5 — Stable judgment across variable inputs

Describe different inputs that are handled using the same decision principles.

Expected: recognize the stable judgment rule as potentially reusable even though the sequence or inputs vary.

### T6 — One-off task

Describe an isolated task with no recurring steps or stable decision rule.

Expected: recommend not making a Skill. If the user chooses to continue, label reusability as unverified.

### T7 — Incidental detail in an example

Give a recurring workflow example that includes an unrelated one-time request.

Expected: use the example to define scope and exclude the incidental request unless the user confirms it is part of the core capability.

### T8 — Boundary confirmation gate

Before drafting, leave the trigger or core purpose ambiguous.

Expected: pause, explain why the unresolved choice matters, and ask the next key question. Do not skip this gate to produce a faster-looking draft.

## Question format and design tests

### T9 — Frontier questions and trade-offs

Provide a design request with several independent decisions and one decision dependent on their answers.

Expected: ask independent material decisions in one round; defer the dependent question. Key decision options include benefits, downsides/risks, and a recommendation. The user may answer freely, combine options, or say “not sure.”

### T10 — Candidate assumption vs. confirmed fact

Leave a non-blocking design detail unanswered.

Expected: label it as a candidate assumption if continuing. Never present it as user-confirmed. A blocking issue about purpose, trigger, or boundaries pauses the draft.

### T11 — Design draft and review

Complete a short discovery sequence and confirm scope.

Expected: produce a draft with the required core sections, add optional sections only when relevant, keep scope bounded, and include observable acceptance criteria.

### T12 — Three validation layers

Ask for a validation plan.

Expected: separately provide natural-language trigger tests (positive/negative/borderline), term/scope contrasts, and post-trigger behavior scenarios mapped to acceptance criteria. Explicit invocation alone is not presented as proof of automatic triggering.

### T13 — Actual test status

Provide a design with no implemented target Skill or no independent Codex session.

Expected: provide the test plan and mark actual behavior tests **Not run**. Do not claim static validation proves routing or behavior.

## Acceptance checklist

- [ ] Triggers for new-Skill design intent, not mere mention of Skills.
- [ ] Elicits repeatable steps and stable decision rules.
- [ ] Uses examples to clarify workflow and boundaries without scope expansion.
- [ ] Recommends against a Skill when no reusable pattern is found.
- [ ] Confirms purpose, trigger, and scope before drafting.
- [ ] Uses the agreed question format with meaningful trade-offs and recommendations.
- [ ] Separates core blockers from non-blocking assumptions.
- [ ] Produces a bounded design draft with testable acceptance criteria.
- [ ] Separates routing, terminology/scope, and behavior testing.
- [ ] Records unrun or failed tests honestly.
