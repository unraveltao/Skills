The number of steps is not what makes a Skill difficult to design. The real complexity appears when the task can move through different states and each state calls for a different next action.

This article uses a hypothetical GitHub Issue-to-PR workflow to show how to spot that complexity before writing instructions. The example is for learning; we are not building this Skill as a product.

## A checklist works only while the path stays fixed

A simple checklist might say:

1. Read the GitHub Issue.
2. Inspect the code.
3. Change the code.
4. Run tests.
5. Prepare a PR.

That list names the usual actions, but it says nothing about what to do when the work does not follow the usual path.

- The Issue may not include enough detail to reproduce the problem.
- The repository may already contain a fix.
- A plausible cause may not be supported by evidence.
- A test may fail because of the change, the environment, or an unrelated existing problem.
- The needed next step may exceed the user’s authorization.

A checklist assumes that every task follows the same route. Real work changes direction as the inputs, environment, and evidence change.

So complexity is not simply “a lot of steps.” It is the presence of different states that require different next actions.

## Separate actions, decisions, and states

Before designing a complex workflow, sort its parts into three categories.

| Type | Question it answers | Issue-to-PR example |
|---|---|---|
| Action | What should be done? | Read the Issue or inspect related code |
| Decision | What determines the next step? | Is there enough information to reproduce the issue? |
| State | Where is the task now? | Root cause supported; fix not yet verified |

Recording only actions usually produces another checklist. Decisions and states reveal the routes the Skill must handle.

For example, “run the tests” is an action. “Did the relevant tests pass?” is a decision. “The fix is verified” is a state.

These are not interchangeable. Running a test does not mean it passed. A passing test does not automatically prove that the reported issue is fixed.

## Map the branches in a real task

Suppose a user reports that the table of contents on an article page stops highlighting sections near the bottom of the page.

The Skill should not jump directly from “read the Issue” to “change the code.” It first needs to resolve several questions:

| Stage | Key question | Possible next step |
|---|---|---|
| Understand the report | Does the Issue explain the observed and expected behavior? | Ask for missing details or identify what remains unknown |
| Inspect the repository | Does the current code still show the problem? | If it is already fixed, gather evidence and report that |
| Find the cause | Is there evidence that explains the observed behavior? | Investigate further or report uncertainty |
| Plan a fix | Can the fix stay within the requested scope? | Reassess the task if the change must expand |
| Verify the result | Do the checks support the claim that the issue is fixed? | Diagnose failures or state what could not be verified |
| Prepare the handoff | What has the user authorized? | Prepare review material and stop at that boundary |

This table is a design sketch, not the final Skill instructions. Its purpose is to make choices visible.

“Information is missing” is a state that needs handling. The Skill might ask a focused question, report a blocker, or continue with checks that do not require guessing.

“Verification failed” also has more than one possible meaning. The change may have introduced a defect, the test environment may be unavailable, or the failure may be unrelated. Different causes call for different routes.

## Define when to stop or hand off

A good workflow says when to continue and when to stop.

For this hypothetical case, start with constraints such as:

- Do not describe a guess as a confirmed cause.
- Do not claim a check passed unless it actually ran and passed.
- If the requested fix needs a wider scope, explain why and ask how to proceed.
- Merging, releasing, or taking another high-impact action depends on the user’s authorization; do not treat it as an automatic part of the fix.

These constraints prevent the workflow from producing unsupported claims or exceeding its scope just to reach the end of the checklist.

They also expose design gaps. If the Skill has no defined response to failed verification, or no rule for when the user must decide, the workflow is not finished.

## Draft the task map before writing instructions

Before opening `SKILL.md`, answer these questions on one page:

```text
Task goal:
User-provided inputs:
Expected deliverable:

Main stages:
1.
2.
3.

Decisions that change the next action:
- If the condition is met, then…
- If it is not met, then…

Likely blockers or failures:
- If information is missing…
- If the cause cannot be confirmed…
- If verification fails…

Boundaries:
- Do not claim…
- Do not take this action without authorization…
- Ask the user to decide when…
```

The first map does not need to cover every imaginable edge case. Start with the branches that change what the Skill should do next.

If a decision does not change the next action, it may not need to be a separate branch yet. If it changes whether to continue, what evidence is needed, or whether to hand control back, make it explicit.

## What you should leave with

After this article, you should be able to create an initial task map for a complex workflow that includes:

- The goal, inputs, and deliverable
- The main stages
- Decisions that change the next action
- Important failure or blocked states
- Boundaries the Skill must respect

You do not need to write the complete Skill yet. First make the real choices visible. The workflow and evaluation design will depend on this map.

## Next

In the next article, we will turn the task map into an executable workflow with a normal path, branches, stop conditions, and recovery routes.
