A failed test is useful only if it helps us decide what to change. Resist the urge to add another vague rule as soon as an output looks wrong. First describe the failure precisely, then trace it back to the specification, instructions, inputs, or available tools.

## Record what actually happened

For each case, keep:

- the test input;
- the Skill version and environment;
- the actual output;
- the expected behavior;
- pass or fail;
- the evidence for the result.

“Did not follow the request” is too vague. A useful observation is:

> The user asked for an outline only, but the response included a full draft.

Concrete evidence helps identify the right fix and verify whether it worked.

## Classify the failure before editing

| Symptom | First place to inspect |
| --- | --- |
| An in-scope request does not activate the Skill | Name and description: are the goal and trigger conditions recognizable? |
| A casual or unrelated request activates it | Trigger description: is the scope too broad? |
| The Skill activates but skips a step | Workflow instructions: is the step explicit and in the right place? |
| An outline request returns a full draft | Output branch: is the “outline only” behavior clear? |
| Conflicting sources become one asserted fact | Conflict handling: does the Skill say what to do with disagreement? |
| The draft has claims without evidence | Input requirements and source-checking steps |
| Results vary a lot across runs | First check whether the task and evaluation criteria are specific enough; then inspect environment differences |

This table is a diagnostic aid, not an automatic answer. One failure can come from the behavior specification, the Skill instructions, the input, or the agent's available capabilities.

## Trace the failure back to the specification

Suppose a test shows that an outline-only request sometimes produces a full article.

Ask:

1. **Did the specification define the expected behavior?**  
   If not, fix the specification first.

2. **Does the Skill file express that behavior clearly?**  
   If not, clarify the relevant branch in `SKILL.md`.

3. **Can the test case reproduce the failure?**  
   If not, refine the test so it distinguishes the correct behavior from the failure.

4. **Which other cases could this change affect?**  
   Rerun the original failure and related cases.

Adding “keep the answer concise” would not solve the actual problem. The Skill needs to understand that an outline request means no full draft unless the user asks for one.

## Make focused changes and run regression cases

A change can fix one failure and create another. If we narrow the trigger description too much to stop casual activation, we may also prevent valid article-planning requests from activating.

After each meaningful change:

- rerun the failed case;
- rerun cases related to the changed instruction;
- check that important passing cases still pass.

The wider the change to the trigger, workflow, or output behavior, the broader the regression check should be.

## Keep a short iteration record

```text
Skill version:
Test case:
Observed failure:
Evidence:
Likely cause:
Change:
Result after change:
Regression cases rerun:
```

For example:

```text
Observed failure:
The outline-only case returned a full article draft.

Likely cause:
The output section described what an outline contains but did not say to stop
after the outline when that is all the user requested.

Change:
Added an explicit branch: return only the outline unless the user asks for
a full draft.

Regression:
Reran the outline-only case and a full-draft case to ensure the new branch
does not disable drafting.
```

The record should explain why the Skill changed and how the change was checked. It does not need to become a large report.

## Treat tests as evidence, not a guarantee

A test set covers known cases. It cannot prove that a Skill will handle every future request.

When a real failure appears, add a representative case so future revisions can catch it. Avoid collecting many near-identical prompts just to increase the count. For open-ended writing, evaluate stable behaviors—such as following scope, retaining sources, and surfacing uncertainty—instead of demanding identical wording.

## Next

The final article covers release readiness: check the files and instructions, explain the Skill's limits, and establish a simple way to use feedback for future updates.
