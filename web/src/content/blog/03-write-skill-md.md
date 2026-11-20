The behavior specification is ready. Now we can turn it into instructions an agent can follow.

The aim is not to copy the specification word for word. It is to make the Skill's purpose, workflow, decisions, and boundaries easy to find and act on.

## Start with the smallest useful package

A Skill can begin with one file:

```text
research-article-drafter/
└── SKILL.md
```

Add references, templates, or scripts only when they materially support the workflow:

```text
research-article-drafter/
├── SKILL.md
├── references/
│   └── sourcing-guide.md
└── assets/
    └── article-outline.md
```

Every additional file needs a reason to exist and clear instructions about when to load or use it.

Exact metadata and packaging rules vary by platform. Check the target platform's current specification before publishing. OpenAI's Skills documentation describes the common structure: a `SKILL.md` with metadata and instructions, plus optional supporting resources. [OpenAI: Skills](https://developers.openai.com/api/docs/guides/tools-skills)

## Write a useful name and description

The name should make the Skill's purpose recognizable. The description should say what it does and when to use it.

```yaml
---
name: research-article-drafter
description: Turn user-provided research materials into a sourced article outline or draft. Use when the user asks to organize sources, plan an article, or draft from research.
---
```

Keep the description focused. Use it to help the agent recognize a relevant request; keep the detailed procedure in the body.

## Organize the body around the task

A clear instruction file often answers these questions in order:

1. What task does this Skill handle?
2. What inputs does it need?
3. What steps should the agent follow?
4. How should it handle important branches?
5. What should the user receive?
6. What must it avoid or hand back to the user?

For our example:

```markdown
# Research Article Drafter

Use this skill when the user asks to organize research materials,
plan an article, or draft from supplied sources.

## Workflow

1. Identify whether the user wants an outline, draft, or source review.
2. Confirm the topic and goal. Ask a focused question only when missing
   information prevents useful progress.
3. Separate supported facts, interpretation, and unresolved questions.
4. Plan the structure around the user's question.
5. Draft only to the level requested.
6. Check that major claims are traceable to supplied or verified sources.
7. List unresolved facts or editorial decisions for the user.

## Output

For an outline, provide the central question, sections, and the evidence
each section needs.

For a draft, provide a title, structured article text, source references,
and unresolved questions when needed.

## Boundaries

- Do not invent sources, data, or personal experiences.
- Do not present unsupported claims as established facts.
- Do not publish or distribute the work unless the user asks.
```

This is a starting point. Later tests may show that some instructions need to be more precise or that a branch is missing.

## Prefer actions over aspirations

“Write a high-quality article” is hard to verify.

“Keep a source for each major factual claim, or mark the claim as unverified” describes an observable action.

Likewise:

- Replace “check the evidence carefully” with “separate source-backed facts from interpretation.”
- Replace “handle contradictions responsibly” with “show conflicting claims and do not silently select one.”
- Replace “respect the requested format” with “when the user asks only for an outline, do not write the full article.”

Specific instructions are easier to execute and evaluate.

## Keep supporting files purposeful

Ask: **Does the agent need this information every time it runs the Skill?**

- Keep the core workflow and important boundaries in `SKILL.md`.
- Put long, occasionally needed background in `references/`.
- Put reusable output formats in `assets/`.
- Add `scripts/` only when deterministic processing is genuinely useful and existing tools are not enough.

For example, a short rule about preserving sources belongs in the main instructions. A long house citation guide may be easier to maintain as a reference.

## Review the first draft

Before testing behavior, check that:

- The name and description communicate a focused purpose.
- Inputs, steps, branches, output, and boundaries are present.
- Instructions describe actions rather than vague quality goals.
- No rules repeat or conflict.
- Every supporting file is necessary and referenced.
- Platform-specific requirements are not presented as universal rules.

A Skill should be clear without trying to script every possible conversation. Too many rules can make small variations harder to handle.

## Next

A readable `SKILL.md` is still only a hypothesis about agent behavior. Next, we will turn the specification into test cases for activation, execution, and important edge cases.
