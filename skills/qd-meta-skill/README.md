# QD Meta Skill

QD Meta Skill helps you decide whether a recurring need is a good fit for a new Codex Skill, then shape it into a reviewable design and validation plan. It uses questions to uncover reusable steps and decision rules, define scope, and make assumptions visible.

## When to use it

Use this Skill to design a new Codex Skill from a need, task, or workflow. It is not intended for general questions about Skills or for carrying out a task with an existing Skill.

## What it does

The workflow helps identify repeatable steps, distinguish the core workflow from incidental details, decide whether the need is reusable, and define the intended user, purpose, trigger, responsibilities, exclusions, workflow, outputs, and constraints. It produces a design draft with acceptance criteria and a validation plan.

Questions are asked in decision-focused rounds rather than a fixed questionnaire. Before drafting, the Skill summarizes scope and asks the user to confirm or correct it.

## Boundaries

In V0.1, QD Meta Skill designs new Skills only. It does not implement, edit, install, or publish the target Skill. A single task without recurring steps or stable decision rules may not warrant a Skill; if the user continues anyway, reusability remains unverified.

## Validation approach

The validation plan distinguishes:

1. Trigger tests with positive, negative, and borderline requests. Explicit invocation does not establish automatic routing.
2. Scope tests distinguishing new-Skill design from explaining or using an existing Skill.
3. Post-trigger behavior checks for discovery, scope confirmation, draft quality, assumptions, and observable acceptance criteria.

The prompts and checklist in [tests/README.md](tests/README.md) are test specifications, not evidence of passing behavior. Real routing or behavior validation requires an independent Codex session with evidence that the Skill loaded.

## Package contents

- [SKILL.md](SKILL.md) — authoritative behavior and scope.
- [Agent metadata](agents/openai.yaml)
- [Manual tests](tests/README.md)

## Items to verify

- Confirm loading and metadata recognition in the intended Codex client from a clean session.
- Run manual scenarios and record client/version, load evidence, prompts, outcomes, and limitations.
- Confirm a supported installation/distribution path before documenting one.

See the repository [Installation guide](../../docs/getting-started/installation.md). The package does not declare a license in its Skill metadata; this README makes no license claim.

The T1–T13 scenarios and the [test status record](tests/REPORT.md) were reviewed. No independently loaded Skill session was available to verify behavior. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
