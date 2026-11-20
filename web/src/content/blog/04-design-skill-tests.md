A complete-looking `SKILL.md` does not prove that a Skill will work well. Testing helps answer two different questions: will it activate for the right requests, and will it follow the intended workflow once activated?

For our research-to-article example, we can derive test cases directly from the behavior specification.

## Test activation and execution separately

**Activation tests** check whether the Skill is considered for the right user requests.

For example, “Turn these notes into an article outline” should be in scope. “I have been thinking about this topic” may not be a request to start the workflow.

**Execution tests** check what happens after activation.

If the user asks for an outline only, does the agent avoid writing a full draft? If two sources conflict, does it report the disagreement?

These failures have different causes. A Skill can activate correctly and still skip an important step; it can also perform the workflow well when explicitly invoked but activate too broadly.

OpenAI's Skill evaluation example likewise uses concrete cases to assess both whether a Skill is invoked and how well it performs its task. [Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills)

## Derive cases from the specification

Look for statements that can be checked:

- Which requests should activate the Skill?
- Which similar requests should not?
- What should happen when required input is missing?
- Which workflow steps must be present?
- Which conditions should change the workflow?
- What makes the final result acceptable?

Each important requirement should have at least one relevant test. If the specification says to surface conflicting evidence, include a test with conflicting sources.

## Begin with a small, representative set

| Case | Example input | What to check |
| --- | --- | --- |
| In-scope outline | “Create an outline from these sources.” | The Skill handles an outline request and uses the supplied material |
| In-scope draft | “Draft an article from these interview notes.” | It drafts at the requested level and distinguishes evidence from interpretation |
| Out-of-scope conversation | “This topic is interesting.” | It does not start drafting without a writing request |
| Missing goal | “Write an article for me.” | It asks for the key missing detail or states a safe default |
| Conflicting sources | Two sources report different values for the same fact | It reports the conflict rather than silently choosing one |
| Output constraint | “Give me an outline only; no full draft.” | It respects the requested scope |

This is a starting set, not an attempt to enumerate every possible prompt.

## Define expected behavior for each case

A prompt alone is not a test. Write down what success and failure look like before running it.

```text
Case:
Purpose:
Input:
Expected activation:
Expected behavior:
Unacceptable behavior:
```

For the outline-only case:

```text
Expected activation:
Use the article-planning workflow.

Expected behavior:
Return the central question, proposed sections, and evidence each section needs.

Unacceptable behavior:
Write the full article, omit a major supplied claim, or present unsupported
information as established fact.
```

Naming unacceptable behavior is useful because some mistakes—such as inventing a citation—matter more than small differences in wording.

## Use observable checks

Choose a few criteria from the specification:

- Did the agent identify the right task?
- Did it follow the requested output scope?
- Did it handle missing or conflicting evidence as specified?
- Can key claims be traced to sources?
- Did it surface unresolved questions?

For each criterion, record pass, fail, or not applicable, along with the output evidence. A single overall score can hide a critical failure.

For open-ended writing, do not require the answer to match a reference paragraph exactly. Evaluate the important behaviors and quality criteria instead.

## Keep cases reproducible

For each run, record the Skill version, agent or platform, available tools, test input, output, and evaluation notes. When the Skill changes, rerun cases that cover the changed behavior and check that earlier successes still hold.

A small set of relevant, repeatable cases is more useful than many similar prompts.

## Next

The next article will run these cases, diagnose failures, and show how to make focused changes without losing behaviors that already work.
