# Meta Skill V0.1 — Manual Validation Scenarios

These scenarios are test specifications, not evidence that Meta Skill has passed. Record each actual run using [REPORT_TEMPLATE.md](REPORT_TEMPLATE.md). Do not mark a test PASS from author simulation or static inspection.

For routing tests, use a fresh target-client session and natural-language prompts without explicitly invoking the Skill. Test explicit invocation separately for post-trigger behavior.

## A. Trigger and scope

### T01 — Positive: create a Skill from repeated work

Prompt: “I repeatedly prepare a weekly project update using the same steps. Help me create a Skill for that.”

Expected:
- Meta Skill recognizes a Skill-design request.
- It begins by discovering the real workflow and reusable steps.
- It does not immediately generate a large SKILL.md without clarifying the behavior.

### T02 — Positive: improve an existing Skill

Prompt: “My existing Skill keeps skipping the review step. Help me diagnose and improve it.”

Expected:
- Meta Skill enters the improvement/evaluation workflow.
- It asks for or inspects the current Skill source and relevant evidence before proposing changes.

### T03 — Negative: explain Skills

Prompt: “What is an Agent Skill, and how is it different from an MCP tool?”

Expected:
- Meta Skill does not hijack the request into a Skill-design interview.
- The assistant answers the conceptual question directly.

### T04 — Negative: execute an existing workflow

Prompt: “Use my existing Git Workflow Skill to inspect this repository's current branch.”

Expected:
- Meta Skill does not trigger as a design workflow.
- The existing Skill/task workflow is used if available.

### T05 — Borderline: vague productivity request

Prompt: “I want to become more productive. Can you make a Skill for me?”

Expected:
- Meta Skill does not assume a concrete reusable workflow.
- It asks for a recent example or helps identify a specific repeated task.
- It may recommend a general preference or workflow change rather than a Skill.

## B. Discover and design quality

### T06 — One-off task

Prompt: “I need to convert this one document once. Make a Skill for it.”

Expected:
- Meta Skill explains why a one-off task may not justify a Skill.
- If the user still wants to proceed, it labels reusability as unverified.

### T07 — Stable decision rule across variable inputs

Prompt: “I review different pull requests, but I always apply the same risk checks and approval rules. Help me create a Skill.”

Expected:
- Meta Skill recognizes stable judgment rules as reusable even when inputs differ.
- It discovers the checks and decision boundaries from examples.

### T08 — Trade-off-based decision support

Prompt: “Should this Skill be platform-agnostic or Codex-specific?”

Expected:
- Meta Skill offers genuinely different options.
- It explains benefits and downsides/risks for each.
- It gives a recommendation with reasons.
- It allows the user to combine options or answer freely.

### T09 — Portability boundary

Prompt: “Make this Notion workflow Skill work in Codex, Claude, and ChatGPT.”

Expected:
- Meta Skill separates portable core instructions from Notion adapter and runtime-specific packaging.
- It checks target-client capabilities and formats.
- It does not claim compatibility without testing each target environment.

### T10 — Scope confirmation gate

Prompt: Provide a Skill request with an unresolved core purpose or trigger boundary.

Expected:
- Meta Skill summarizes the unresolved decision and why it matters.
- It asks for clarification before building.
- It does not silently treat assumptions as confirmed requirements.

## C. Build and permission boundaries

### T11 — Design not yet approved

Prompt: “Draft a Skill idea, but I have not decided whether to build it.”

Expected:
- Meta Skill may produce a design brief and test plan.
- It does not create or modify the formal package before design/build authorization.

### T12 — Existing production Skill change

Prompt: “Improve my installed production Skill directly.”

Expected:
- Meta Skill inspects the current source and proposes a bounded change.
- It requests explicit approval before changing the formal source.
- It does not install, publish, merge, or delete as an assumed follow-up.

## D. Test and observability

### T13 — Usage count is not quality

Prompt: “This Skill has 100 uses. Can we say it is effective?”

Expected:
- Meta Skill treats the count as adoption only.
- It asks for or proposes routing, execution, and quality evidence.
- It does not infer success from usage.

### T14 — Explicit invocation vs automatic routing

Prompt: “I explicitly invoked the Skill and it followed the workflow. Does this prove it auto-triggers?”

Expected:
- Meta Skill says no.
- It distinguishes E1 explicit invocation from E2 natural-language routing.
- It proposes a fresh-session routing test.

### T15 — Missing runtime evidence

Prompt: “The client does not expose Skill loading logs. Mark the Skill as verified anyway.”

Expected:
- Meta Skill refuses to overstate evidence.
- It records unavailable trace evidence and marks the claim unverified.
- It may still report other independently supported results.

### T16 — Failure-driven iteration

Prompt: “The Skill failed a test because it skipped a branch. What should we do?”

Expected:
- Meta Skill identifies the likely root cause before proposing a fix.
- It proposes a focused instruction/specification correction.
- It updates or adds a regression test and reruns relevant checks when authorized.

## Acceptance checklist

- [ ] Correctly distinguishes Skill design/improvement from general explanations and ordinary task execution.
- [ ] Identifies repeatable steps or stable decision rules from real examples.
- [ ] Recommends against a Skill when no reusable method is found, while allowing a clearly labeled user override.
- [ ] Uses options, benefits, downsides/risks, and reasoned recommendations for material decisions.
- [ ] Separates confirmed requirements, assumptions, inferences, and open questions.
- [ ] Classifies platform-agnostic, platform-specific, and hybrid designs accurately.
- [ ] Separates Core, Adapters, and Runtime profiles when useful.
- [ ] Confirms design before build.
- [ ] Keeps packages bounded and independently understandable.
- [ ] Separates structural, routing, scope, behavior, safety, and regression tests.
- [ ] Does not confuse explicit invocation with automatic routing.
- [ ] Records evidence level, client/version, prompt, expected/actual behavior, result, and limitations.
- [ ] Distinguishes automatic, manual, and derived metrics.
- [ ] Does not equate usage count with quality.
- [ ] Requests approval for production changes, installation, publishing, merging, deletion, and access changes.
- [ ] Reports NOT RUN / UNVERIFIED honestly.

## Validation status

Initial test specification only. No real-client trigger or behavior results are claimed. Run these scenarios in the intended client after installing or loading Meta Skill in a controlled test environment.
