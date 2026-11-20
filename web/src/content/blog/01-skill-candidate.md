A Skill is worth building when it captures a useful way of working that you expect to repeat. The first step is not opening a Markdown file. It is finding a task whose workflow is stable enough to reuse.

Throughout this guide, we will use one worked example: a Skill that turns user-provided research materials into a sourced article outline or draft. The example helps make each design decision concrete; the same method applies to other workflows.

## A Skill is more than a checklist

A Skill gives an agent reusable instructions and resources for a recognizable task. It explains when to use a workflow, what steps to follow, and what a successful result should include.

That makes “write an article” too broad to be a useful Skill goal. The topic, audience, evidence, and desired outcome could all vary.

A narrower task is easier to design:

> Given a topic and research materials from the user, organize the evidence and produce an article outline or draft with sources and unresolved questions clearly marked.

This describes a repeatable workflow, not just a desired end result.

## Look for repeated work

Start with tasks you have done more than once, especially tasks that require you to re-explain the same process or repair the same kinds of mistakes.

Ask yourself:

1. Which tasks do I repeat across projects or over time?
2. Which steps stay mostly the same each time?
3. Where do I often lose time to omissions, inconsistent formatting, or missing inputs?
4. Which parts of my experience would I like an agent to remember next time?

Write a candidate in one sentence:

> When I provide **these inputs**, I want the agent to **do this work** and return **this result**.

For our example:

> When I provide a topic and research notes or sources, I want the agent to organize the evidence and return an article outline or draft with traceable claims.

This is a candidate description, not yet the final Skill instruction.

## Check whether the task is a good fit

### Will the task happen again?

A one-off request rarely needs a dedicated Skill. Repetition does not have to mean every day; it is enough that the workflow is likely to recur and currently requires repeated explanation.

### Is the desired outcome clear?

“Make this better” is hard to execute and hard to evaluate. “Produce an outline with a central question, sections, and supporting evidence” is much easier to check.

### Are some steps reusable?

If every instance requires a completely different process, fixed instructions may get in the way. A Skill is more useful when a stable set of steps applies across different inputs.

### Can you tell whether the result is good?

Before writing the Skill, list a few checks:

- Does the result answer the user's question?
- Can major factual claims be traced to sources?
- Are facts separated from interpretation?
- Are missing or conflicting details surfaced?
- Does the output match the requested format?

Without observable checks, it will be difficult to know whether the Skill improved the work.

### Are the required capabilities available?

Instructions can guide an agent through tools it already has. They cannot provide missing access, permissions, or facts.

If the workflow depends on web search, code execution, or a specific application, confirm that the target agent can use those capabilities. Otherwise, the Skill must ask the user for materials or clearly report the limitation.

## Set the boundary before writing

For the research-to-article example:

**Use it when:** the user asks to organize research, create an article outline, draft from supplied sources, or review an article's evidence.

**Do not assume it applies when:** the user is only discussing an idea, asks for fiction, or asks to publish a post when the task is only drafting.

These boundaries help keep a Skill focused. They also give us concrete cases to test later.

OpenAI's Skill guide similarly recommends tying a Skill to a recognizable user goal, with its trigger, workflow, and output described clearly. Platform packaging details can vary, so check the target platform's own requirements. [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)

## A quick candidate checklist

Before moving on, confirm that you can answer:

- [ ] What specific task will this Skill complete?
- [ ] Which requests should trigger it?
- [ ] What input does it need, and what will it return?
- [ ] Which steps are reusable?
- [ ] How will you judge the result?
- [ ] What must it ask, avoid, or hand back to the user?

If these questions are still difficult to answer, observe the real workflow before adding instructions. A clearer task definition usually helps more than a longer prompt.

## Next

Once the candidate is clear, define the Skill's behavior in more detail: activation, inputs, workflow, outputs, and stop conditions. That specification will become the blueprint for the `SKILL.md`.
