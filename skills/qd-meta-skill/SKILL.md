---
name: qd-meta-skill
description: "Design new Codex Skills by eliciting reusable workflows, confirming scope, and producing a reviewed design draft with trigger and behavior tests. Use for requests to design a new Skill; do not trigger for Skill explanations or task execution."
---

# QD Meta Skill

Help the user turn a described need into a clear, bounded design for a new Codex Skill. The primary work is question-driven discovery of reusable steps or decision rules, followed by a user-reviewed design draft and a validation plan.

## Scope and boundaries

- Use this Skill when the user asks to design a new Codex Skill from a need, task, or workflow.
- Do not use it merely because the user mentions a Skill. Answer questions about Skills directly, and do not enter this workflow to perform an ordinary task using an existing Skill.
- V0.1 covers new Skills only. Do not edit, install, or publish the target Skill. The deliverable is its design draft and validation plan.
- If the user later asks to test a target produced from this design, test only when it is implemented and can be loaded in a clean Codex session. Do not modify its files during testing.
- Keep the name `qd-meta-skill` as the working name; do not invent an expansion for `QD`.

## Question-driven workflow

Use fixed decision gates with adaptive questions, not a fixed questionnaire. Ask all currently independent, material decisions in a round; defer questions whose answers depend on unresolved decisions. Do not add questions merely to keep the interview going.

For each key decision question:

1. State the decision clearly.
2. Offer meaningfully different options when options help.
3. Explain the benefits and downsides or risks of each option.
4. Give a recommendation and its reason.
5. Allow the user to choose, combine options, answer freely, or say they are unsure.

Use this presentation pattern, adapting it to the conversation language:

```text
❓ Q[number] — [key decision]

A · [option]
✅ Benefit: ...
⚠️ Downside / risk: ...

B · [option]
✅ Benefit: ...
⚠️ Downside / risk: ...

➡️ Recommendation: [option] — [reason].
Choose, combine, answer freely, or say “not sure.”
```

Not every information-gathering prompt needs multiple-choice options. Use open questions when the user is recalling facts or describing an example; never manufacture choices for a decision that does not have meaningful alternatives.

At useful checkpoints, tell the user the current stage, what is established, and the next material question. Do not skip a core decision to make the process feel shorter. Reduce effort by using plain language, examples, and grouped independent questions. Do not repeat settled facts.

## Discover reusable work

Treat both of these as potentially reusable Skill content:

- Steps that recur across similar tasks.
- Stable decision rules used across different inputs.

If the user cannot explain their process abstractly, ask about one recent, concrete example. Use examples to discover the core process and define its boundaries, not to expand scope from incidental details.

Offer this example template when useful; do not require the user to fill every field at once:

```text
- What happened that started this task?
- What result were you trying to get?
- What did you actually do, step by step?
- Where did you need to decide or use a rule, and what guided you?
- What exceptions or variations occurred?
- Which steps or decisions recur in other instances?
- Which details were incidental or outside the main goal?
```

Start with one example. Ask for a contrasting example only if reusability or scope remains unclear. Do not turn a one-off detail into a general requirement without evidence and user confirmation.

If no recurring steps or stable decision rule can be identified, recommend not making a Skill. This is a recommendation, not a hard block: if the user chooses to continue, label reusability as unverified and do not present it as established.

## Confirm scope before drafting

Before producing the design draft, summarize:

- Core goal and intended user.
- In-scope responsibilities.
- Explicitly out-of-scope and adjacent requests.
- Confirmed requirements, candidate assumptions, and open decisions.

Ask the user to correct or confirm this boundary summary. Use cases to check where the boundary lies; do not add unrelated features just because they appear in an example.

If a core decision about purpose, trigger, or boundary is unresolved, pause at that gate and explain why it matters and what question needs answering next. A non-blocking detail may be carried as a clearly labeled candidate assumption. Never present an assumption as user-confirmed.

## Produce the design draft

Follow the local Skill Creator guidance. Keep a stable core structure and include optional sections only when the proposed Skill needs them. The design draft should cover:

1. Skill name and concise capability description.
2. User, problem, and intended outcome.
3. Trigger conditions and meaningful non-trigger conditions.
4. Responsibilities, exclusions, and adjacent boundaries.
5. Workflow, decision points, and expected outputs.
6. Constraints, tools, sources, and dependencies when relevant.
7. Testable acceptance criteria and validation scenarios.
8. Candidate assumptions and unresolved questions.

Keep trigger language intent-based and discriminating. Avoid keyword lists as a substitute for defining when the Skill applies. Include positive, negative, and borderline natural-language examples. Name supporting references, scripts, or assets only when they materially help the actual workflow; do not add files just to fill a template.

## Review and validation

Review the draft against the confirmed need before delivery:

- Does it solve the user's stated need without adding unrelated capabilities?
- Are trigger and non-trigger cases distinguishable by user intent?
- Are responsibilities, exclusions, and decision rules clear?
- Are outputs and acceptance criteria observable and testable?
- Are assumptions and unknowns labeled rather than silently filled in?
- Are optional resources justified by a real use case?

Always provide a validation plan with three separate layers:

1. **Trigger tests:** positive, negative, and borderline natural-language requests. Do not rely only on explicit `$skill-name` invocation; that does not test automatic selection.
2. **Term and scope tests:** contrast similar wording or adjacent requests and state the expected distinction.
3. **Post-trigger behavior tests:** realistic task scenarios mapped to specific requirements and observable pass/fail criteria.

When an implemented target Skill and an independent Codex session are available, and the user requests the test phase, run the scenarios there. Record the target Skill loading evidence, client, prompts, observed results, and limitations. If the target is unavailable, the Skill cannot be confirmed as loaded, or the test environment is unsuitable, mark the relevant tests **Not run**. Never claim that static review proves triggering or behavior.

If a behavior test fails, report the evidence and propose a focused design correction. Do not edit the target Skill files or imply implementation is complete.

## Deliverables and stopping point

Deliver:

- A user-reviewable design draft.
- A validation plan with runnable prompts and itemized acceptance criteria.
- A concise record of confirmed decisions, candidate assumptions, unresolved items, and any tests run or not run.

Stop at the design and validation handoff unless the user separately requests another authorized task. Do not claim the target Skill is implemented, installed, published, or behavior-verified when it is not.
