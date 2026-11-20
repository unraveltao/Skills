Passing the current tests does not mean the work is finished. Before release, someone new should be able to tell what the Skill does, how to use it, and what it cannot do.

This final step closes the loop from task selection to maintenance.

## Check that the package is usable

Review the Skill from a new user's perspective:

- Are the required files present and in the expected format?
- Do the name and description communicate the intended use?
- Can the user tell what inputs to provide?
- Are referenced files and paths correct?
- Does the workflow depend on tools, permissions, or platform behavior?
- Are those dependencies and limitations stated?

A package that only its author knows how to invoke is not ready to hand off.

Discovery, installation, and packaging can differ across agent platforms. Verify the format for the platform you intend to support; do not assume that a Skill working in one environment will work unchanged in another. [OpenAI: Skills](https://developers.openai.com/api/docs/guides/tools-skills)

## Use a release checklist

### Content

- [ ] The Skill serves one recognizable user goal.
- [ ] The description says what it does and when it applies.
- [ ] The instructions cover inputs, workflow, outputs, and boundaries.
- [ ] Decisions that belong to the user remain with the user.
- [ ] Required tools and known limitations are clear.

### Files

- [ ] `SKILL.md` is present and valid for the target platform.
- [ ] Every referenced resource exists.
- [ ] There are no unused or duplicate files.
- [ ] Examples contain no private or machine-specific data.

### Validation

- [ ] In-scope requests have been checked.
- [ ] Similar out-of-scope requests have been checked.
- [ ] Important branches and edge cases have been exercised.
- [ ] Results correspond to the current Skill version.
- [ ] Failures and unresolved limitations are recorded.

Describe validation accurately. “Passed the six cases in the current test set” is more useful than claiming that a Skill is completely reliable.

## Tell users how to start

A short release note should answer:

- What can the Skill help with?
- When should someone use it?
- What input should they prepare?
- How do they install or invoke it?
- What are its current limitations?

For example:

> **Research Article Drafter** turns supplied research materials into a sourced article outline or draft. Use it when you have a topic and supporting material. It does not publish articles or invent missing evidence.

Do not imply that the Skill can browse, validate current facts, or publish unless the target agent has those capabilities and the workflow actually supports them.

## Track versions and changes

For each release, record the version or date, what changed, why it changed, which tests were rerun, and any known gaps.

```text
Version: 0.2

Changes:
- Added an outline-only branch.
- Added a case for conflicting sources.

Validation:
- Reran the outline-only and full-draft cases against the current criteria.

Known gap:
- The current test set does not cover non-English source material.
```

Keep this record lightweight. Its job is to make changes and their evidence traceable.

## Keep the lifecycle moving

After release, collect real examples of:

- requests the Skill failed to activate for;
- steps that repeatedly needed clarification;
- outputs users had to repair;
- rules that caused unexpected behavior;
- new cases worth adding to the test set.

Look for recurring evidence before expanding the instructions. A single unusual request may be an input-specific issue, not a new general rule. After a meaningful change, rerun the relevant tests and check for regressions.

The cycle is:

**Observe a repeated task → define behavior → write the Skill → test → revise → release → collect feedback → update the specification and tests.**

Release is a checkpoint, not the end of the lifecycle. It records what the current version does, what evidence supports it, and what remains untested.

## Final check

Before calling the Skill ready, confirm that users can understand its purpose and limits, its files and dependencies are complete, key behaviors have test evidence, and future issues can be recorded.

That is the complete method: start with a real task, design a focused workflow, test the behavior, and improve it from evidence.
