# Scenario tests

These are manual behavioral evaluations for an agent that has loaded this Skill. They are not executable unit tests and must not be reported as real-agent acceptance until actually run. For each run, save the agent output and mark each criterion Pass / Partial / Fail with evidence.

## Common evaluation criteria

- Reuses provided facts instead of asking for them again.
- Asks one focused question only when the answer could change the design.
- Challenges assumptions constructively and gives a reasoned recommendation.
- Identifies existing approaches when research tools are available; cites sources and seeks disconfirming evidence.
- Separates fact, inference, assumption, and recommendation where needed.
- Preserves decision history when a choice changes.
- Produces a concrete, scoped handoff another agent can use.
- Discloses unavailable research or persistence rather than implying it happened.
- Correctly distinguishes designing a tool-learning Skill from directly requesting a tool tutorial, using the full conversation context.
- Maintains the design-advisor role unless the user explicitly changes tasks.
- Advances with a useful initial proposal when the user has already supplied enough context.
- Uses 💡, 🔎, and ❓ naturally and only where they help.

## T1. Design a tool-learning Skill

**Prompt:** “I want to create a Skill that helps me research and learn GitHub and Codex features and advanced usage methods.”

**Expected observations:** Identifies product-design intent; proposes a Skill that researches official docs and credible expert practices, synthesizes current feature guides, cites evidence, adapts to user goals, and optionally supports hands-on learning; does not start a GitHub tutorial. It may ask one material question only after offering a concrete first direction.

## T2. Design a Python-learning Skill

**Prompt:** “I want to design a Skill that helps beginners learn Python.”

**Expected observations:** Discusses the product's learner, outcomes, teaching capabilities, existing alternatives, and deliverable shape; does not begin teaching Python.

## T3. Direct tool explanation

**Prompt in a fresh, unrelated conversation:** “Please explain what GitHub Gist is and how to use it.”

**Expected observations:** Treats this as a direct explanation request; does not apply a product-design workflow. If the same prompt occurs during an active Idea Advisor design conversation, use context to avoid an accidental switch and clarify only if the user intent truly changed ambiguously.

## T4. Changed requirements and decision history

First agree on a design direction and record its rationale. Then change a meaningful constraint.

**Expected observations:** Identifies the change, explains impact, preserves the prior rationale, and proposes a linked revised decision rather than silently rewriting history.

## T5. Conversation markers

Observe a proposal, a research summary, a consequential question, and a simple exchange.

**Expected observations:** 💡 marks a useful idea, 🔎 marks evidence/research, ❓ precedes a material question; no marker is forced on every paragraph or used as proof of loading.

## T6. Real installation and loading

Install the Skill into the verified Codex Skill search location, start an isolated fresh session, explicitly invoke it, and retain evidence of the session's loaded Skill path or invocation record.

**Expected observations:** Real load evidence exists and T1 behavior is observed in that session. A stylistically similar answer alone is insufficient.

## T7. Suppress redundant clarification

Provide the T1 request plus context that the user wants researched reference guides for GitHub (including Gist/Projects) and Codex, with citations and expert practices.

**Expected observations:** Reuses all those facts, offers the product direction, and avoids asking whether the user has an account or browser open.

## T8. Research an existing-product space

Ask the Skill to design a product in a field with established similar tools.

**Expected observations:** Searches for reusable options and counter-evidence when network research is available; otherwise plainly states the limitation and does not fabricate findings.

## Earlier V0.1 baseline cases (retained)

The following original cases remain useful for broader coverage; they do not replace T1–T8.

### A. Vague AI Skill idea

**Prompt:** “I have an idea for an AI Skill that helps people deal with complicated technical documents. I’m not sure what it should do. Help me shape it.”

**Expected observations:** Begins by understanding the user's motivation and target task, not by prescribing a full Skill; asks at most one high-value open question if needed; later considers existing tools or Skills if browsing is available; recommends a focused use case and gives rationale; does not claim to implement it.

### B. Vague software product idea

**Prompt:** “My team forgets small decisions. Maybe we need an app. Help me figure out what to build.”

**Expected observations:** Reframes the problem before accepting “app” as the answer; uses team size/context only if material; considers existing tools, process changes, and a custom product as appropriate; compares meaningful options and costs; provides a recommendation plus lightweight acceptance criteria or next validation step.

### C. Requirement change reverses a confirmed decision

**Turn 1:** “Design a simple incident notes tool for our team. It must work offline, so recommend local-first storage and record that decision as confirmed.”

**Turn 2:** After a concrete decision record is presented, reply: “New requirement: all incidents must be visible to the on-call team immediately from any device. Reopen the storage choice.”

**Expected observations:** Recognizes the new requirement may conflict with a purely local design; does not silently edit the confirmed record; creates a linked replacement or marks the old decision superseded only after presenting a concrete revision; compares suitable sync/shared options and risks; states assumptions and unresolved questions; preserves the original rationale and history.

## Running and reporting

Run scenarios in a fresh agent session with this Skill installed or loaded. Scenario C is multi-turn. Record client/model/date, tools available, transcript, and criterion-level results. If no real agent environment is available, perform only structural review and report behavioral evaluation as **Not run**. A human can use these scenarios as manual steps; simulated reasoning by the author is not an acceptance test.
