At this point the hypothetical Issue-to-PR Skill has a workflow, an input contract, and a permissions matrix. Putting all three in one instruction file is easy. Maintaining the same rules across a long file and several copies of the examples is harder.

Design the file layout around when an agent needs each decision.

## Keep routing and boundaries in the entry point

The entry point should explain what activates the Skill, which outcomes it can produce, and where it must stop. Put the decision to create a remote PR there or at the precise step that leads to it. A reviewer should be able to follow the normal path and find the rule that governs any consequential step.

For a client that follows the Agent Skills format, use the `SKILL.md` entry point and link to supporting resources when they are needed. OpenAI's build guide describes skill metadata and loading behavior for ChatGPT and Codex. Verify the target client before relying on how it discovers a Skill or reads its resources. [OpenAI Build Skills guide](https://learn.chatgpt.com/docs/build-skills)

## Organize the supporting material by decision

<figure>
  <img src="/@blog-assets/skill-package-resources.svg" alt="SKILL.md directs the workflow to a reference for decisions, a script for repeatable checks, and scenarios for evaluation." loading="lazy">
  <figcaption>The entry point routes the task. Other files supply material at the point it is needed.</figcaption>
</figure>

| File or directory | What belongs here | When it is used |
| --- | --- | --- |
| `SKILL.md` | Entry criteria, stages, exit conditions, and essential limits | When the Skill is selected |
| `references/intake.md` | Evidence sources, input contract, clarification examples | When an Issue leaves a material input unresolved |
| `references/verification.md` | Check selection and evidence formats | When choosing how to verify a change |
| `scripts/` | Repeatable work with explicit inputs and predictable outputs | When a documented check requires it |
| `tests/scenarios.md` | Evaluation inputs, expected outcomes, and negative cases | When evaluating behavior or preparing a release |

Start with the files your design needs. A small Skill can keep its contract in the entry point. Extract a reference when usage, ownership, or length makes it easier to maintain independently. Create a script when the work benefits from a consistent invocation and output that can be tested.

## Make the reading instruction actionable

“See references if needed” leaves timing unspecified. “When reproduction is unclear, read `references/intake.md` and use its missing-input table before asking the user” connects a file to a decision.

For the table-of-contents case, a script might compare changed paths with the agreed scope or check whether a generated file contains expected headings. Give it the revision or fixture as input. Let it return observed data and a clear status. The workflow still decides whether those observations support a PR.

## Find the rule that drifted

Imagine `SKILL.md` says to stop after local validation, but a maintenance example says to open a PR after any passing build. Two ordinary runs might choose different actions depending on which file was read. Keep the permission rule in one authoritative place. Rewrite the example to point to it and retain the example's evidence.

## What you should leave with

Produce a package map and annotate when each file is read or executed. Trace one obscure failure from the entry point to the reference, then back to the workflow. A maintainer should be able to update the rule in one place.

## Next

Part 06 turns the package and its decisions into observable evaluation cases.
