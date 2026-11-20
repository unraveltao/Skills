Once you have a good candidate task, resist the urge to start writing `SKILL.md`. First decide what the agent should do in the situations that matter.

For our running example, the goal is to turn user-provided research into an article outline or draft. A short behavior specification will make the intended workflow, decisions, and boundaries explicit before we write instructions.

## Describe observable behavior

“Help the user write a good article” is an aspiration, not an instruction.

A more useful description is:

> Given a topic and research materials, identify whether the user wants an outline, draft, or source review; check whether the inputs are sufficient; organize supported facts and unresolved questions; then return the requested deliverable with traceable sources.

This description names the inputs, workflow, and result. It gives the author and later test designer a shared expectation.

## Define when the Skill should activate

Write down requests that should trigger the workflow and similar requests that should not.

**Good fit**

- The user asks to organize research into an article outline.
- The user provides sources and asks for a draft.
- The user asks to check whether an article's factual claims are supported.

**Not a default fit**

- The user is discussing an idea without asking for writing help.
- The user requests fiction that does not need research.
- The user asks to publish a post, but the current workflow only drafts and reviews content.

Descriptions should focus on user goals and activation conditions. Keep the detailed procedure in the instruction body. [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)

## List required and optional inputs

Separate information the Skill must have from preferences it can infer or ask about later.

| Input | Example | If it is missing |
| --- | --- | --- |
| Topic or question | The question the article should answer | Ask or help narrow the topic |
| Research material | Notes, links, data, or code | State what evidence is missing; search only if the available tools allow it |
| Writing goal | Explain, compare, report, or reflect | Ask if the goal changes the research or structure |
| Output preference | Outline or full draft, language, length | Use a reasonable default when safe, and say what you chose |

Not every preference needs to block progress. Decide which missing details require a question, which can use a stated default, and which can wait until review.

## Turn the workflow into steps

A behavior specification becomes easier to review when its decisions are visible at a glance.

```text
Activation  — When should the Skill start?
Inputs      — What information does it need?
Workflow    — What actions should it take?
Branches    — What changes when conditions differ?
Output      — What does a good result look like?
Boundaries  — What should the Skill avoid?
```



A first version might be:

1. Identify whether the request is for an outline, draft, or source review.
2. Check that the topic and goal are clear enough to proceed.
3. Review the supplied materials; separate supported facts, interpretation, and open questions.
4. Plan the article structure around the user's question.
5. Produce only the requested level of detail.
6. Check that key claims are traceable and uncertainty is visible.
7. Return the work and list decisions or facts that need the user's review.

Keep only steps that materially improve this task. A long workflow is not automatically a reliable one.

## Specify the important branches

Most workflows need a few decision points:

- **Enough material:** continue with the requested outline or draft.
- **Missing topic or goal:** ask one focused question if a useful result depends on it.
- **Conflicting sources:** show the disagreement and do not silently choose a side.
- **Current factual claims:** verify them only when the environment has an appropriate research tool; otherwise mark them for checking.
- **Outline requested:** return an outline without expanding it into a full article.

These branches are easier to follow and test than general advice such as “write carefully.”

## Define the output and boundaries

“Write a good article” is difficult to evaluate. For this Skill, useful acceptance criteria might be:

- It answers the user's stated question and matches the requested format.
- Major factual claims are traceable to supplied or verified sources.
- Facts, interpretation, and unresolved questions are distinguishable.
- It does not invent sources, data, or the user's personal experience.
- It leaves important editorial decisions to the user.
- It does not publish or distribute the draft unless the user explicitly asks and the required capability is available.

The specification is the design blueprint, not the final Skill file.

## A one-page behavior specification

Before writing `SKILL.md`, summarize the decisions:

```text
Goal: Turn user-provided research into an article outline or draft.
Trigger: Organize sources, plan or draft an article, or review factual support.
Inputs: A topic or question and available notes or sources; audience and format are optional.
Workflow: Classify → check inputs → organize evidence → plan → draft → verify → deliver.
Ask when: Missing topic or goal would change the result.
Output: The requested outline or draft, with traceable sources and open questions.
Boundaries: Do not invent evidence or publish without explicit permission.
```

## Next

With the desired behavior defined, we can turn the specification into a concise `SKILL.md`. The next article shows how to organize the metadata, workflow, decisions, and supporting files.
