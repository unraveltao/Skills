The hypothetical Issue-to-PR Skill can read a GitHub Issue, inspect source files, run checks, and prepare a PR. An available GitHub connection may also be able to create that PR. The workflow needs a separate decision for each action, because the evidence and effects differ.

## Pick the tool for the evidence you need

Use the repository source to identify the code paths involved in the table-of-contents bug. Use a browser at a known revision and viewport to observe highlighting. Use build output to verify that the site builds. None of these answers every question. A successful build still leaves the scroll interaction to be checked.

Record the target as well as the result. “The last section stayed active after scrolling to the bottom on commit A at width B” can be reviewed. “Browser check passed” leaves someone to guess what happened.

## Turn permissions into workflow decisions

| Action | Evidence or result | Effect | Decision and fallback |
| --- | --- | --- | --- |
| Read Issue and repository | Current Issue state and source revision | Read | If access fails, report the affected source and use any user-provided material with its limits stated |
| Reproduce in a fixture | Observed UI behavior at a known revision | Temporary local files or process | Use a disposable environment. If it is unavailable, record reproduction as unverified |
| Edit code and run checks | Reviewable diff and observed test output | Local change | Stay within the requested file and behavior scope. Preserve unrelated work |
| Create a PR | Confirmed remote PR URL and source revision | Remote record and possible notifications | Verify user authorization, base and source branch. Otherwise return the diff and draft description |
| Merge or close an Issue | Changed default branch or Issue state | Remote state change and possible downstream jobs | Confirm the specific action, its conditions, and any Issue it will close |

Keep that matrix near the step that consumes it. A permission rule buried in a reference that is loaded after the tool call cannot guide the choice.

## Treat an ambiguous result as a state

Suppose a PR creation call times out. A retry might create a duplicate if the first call succeeded but its response was lost. Read the remote for a matching open PR using the intended head and base. Continue with the verified result. If the remote is unavailable, report the ambiguous outcome and avoid a second write until the state can be established.

Read operations also need bounded recovery. Retry a transient fetch when there is a reason it might succeed. For a persistent permission failure, report the missing access and hand back the information that was available.

## Check the side effects together

The body of a PR is part of the effect. On GitHub, an eligible closing keyword can close a linked Issue when the PR reaches the default branch. In our case, a partial fix can reference the Issue while keeping it open. Treat the decision to close it as part of the proposed merge. [GitHub documentation on linking PRs and Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

## What you should leave with

Build a permissions matrix that names each tool action, what it proves, what it changes, the permission it needs, and what to do if the result is missing or uncertain.

## Next

Part 05 places the workflow, policies, examples, and repeatable checks where the Skill can find them.
