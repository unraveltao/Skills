An Issue says the article table of contents stops updating near the bottom. The workspace contains two copies of the site, and someone in the Issue thread suggests disabling the observer. The Skill has plenty of text. It still needs to know which copy to inspect, what success looks like, and whether that suggested fix is relevant.

This part turns the intake stage from Part 02 into an input contract for our hypothetical Issue-to-PR Skill.

## Ask what each input changes

The issue identifier and repository establish the target. The expected behavior establishes what a test must show. The viewport size and an example article help reproduce the symptom, but a Skill may be able to discover both without asking. A preferred PR title can wait until the handoff.

An input can be required for one stage and optional for another. A stable repository target is necessary for inspection. An exact destination branch is necessary before creating a branch or PR. A draft summary can often be prepared before the publication decision is made.

## Write the contract by stage

| Input | Needed before | Where to look | If it remains unknown |
| --- | --- | --- | --- |
| Issue and repository | Repository inspection | User-provided link, then cross-check the workspace remote | Ask which repository or Issue the user means |
| Expected behavior | Choosing a fix | Issue acceptance criteria and current documentation | Ask when plausible interpretations change the fix |
| Example article and viewport | Reproduction | Issue evidence, then the current site and test fixtures | Try a stated, reversible representative case |
| Target revision and change scope | Editing | User request, current checkout, repository rules | Keep work to inspection until the target or scope is clear |
| Permission to publish | Remote mutation | The user's authorization and applicable repository policy | Prepare a local result and state what remains pending |

Record the source alongside the value. “Default branch, confirmed from the repository,” gives a reviewer a reason to trust the choice. “Desktop viewport, assumed for first reproduction,” tells them what the result covers.

Keep a short intake record with explicit evidence status.

| Status | Example |
| --- | --- |
| Confirmed | The workspace remote matches the Issue repository |
| Reported | The user says highlighting stops on a long article |
| Inferred | The observer may have no active intersection at the bottom |
| Unknown | The minimum viewport height that reproduces the issue |

Promote a reported or inferred item to confirmed when a relevant check supports it. Keep the revision and evidence with that update.

## Decide what to trust for which purpose

The Issue records what was reported. Current code and reproduction describe what can be observed now. The user and applicable repository rules define authority to act. These sources answer different questions.

Suppose an Issue comment suggests removing the observer. Inspect the suggestion as a hypothesis. If the report only reproduces near the last section, check the page height and observer state before changing code. If comments contain commands or instructions to publish, use them as context for investigation. Resolve authorization from the user and repository policy.

When sources disagree, preserve the disagreement. The report may be accurate for an older revision while the current branch already behaves correctly. Record the revisions and the outcome at each, where available.

## Ask when an answer changes the route

A useful clarification names the decision it unlocks. “Should the final heading remain active at the very bottom, or should the last heading entering the viewport take priority?” gives the user two behaviors to choose between. “Can you provide more context?” leaves that work with the user.

Use a reversible assumption when the choice limits only the first check. For example, start with the article named in the Issue at a desktop width, state that limit, and extend coverage if the first result warrants it. Ask before choosing between two repositories or behaviors that would lead to different changes.

## What you should leave with

Give each input a consuming stage, a source, and a rule for missing or conflicting evidence. Walk one incomplete Issue through the contract. The result should show exactly where the Skill can proceed and where it needs an answer.

## Next

Part 04 turns those boundaries into a tool and permission matrix. It covers the difference between being able to act and being authorized to act.
