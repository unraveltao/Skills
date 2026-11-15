# Unravel V0.1 behavior checks

These are manual behavior checks. Run them in an agent session that has loaded this Skill and record the session and outcome. A written checklist or author simulation is not a real-agent test.

## 1. Correct trigger

**Input:** “Explain why Grill-me works so well. Break down its structure and mechanism.”

**Expected:** Triggers Unravel, inspects the relevant Skill source when available, begins with a concise overview and a clean map, then separates observed design facts from hypotheses about effectiveness.

## 2. False trigger

**Input:** “Rename this file to `notes.md`.”

**Expected:** Performs or addresses the ordinary file action; does not introduce a concept lesson or force Unravel interaction.

## 3. Choice response

**Input:** “Why is this product useful?” After the agent offers 2–4 lenses, reply: “A and C, but mostly C.”

**Expected:** Accepts the mixed selection and adapts the explanation to it without demanding a single choice.

## 4. Fill-in response

**Input:** Ask for an explanation of a simple mechanism, then request a short fill-in check. Reply with a partial answer.

**Expected:** Identifies what is correct and the missing link, then explains that gap without scoring or restarting the whole explanation.

## 5. Adaptive explanation

**Input:** After an explanation, say: “That example still doesn't make the relationship clear.”

**Expected:** Changes representation (for example, a small diagram or contrasting example) and focuses on the named relationship rather than repeating the same text.

## 6. End condition

**Input:** After the revised explanation, say: “Yes, I understand now.”

**Expected:** Gives a brief recap if useful, marks completion naturally, and stops without another comprehension question or “continue?” prompt.

## 7. Ambiguous reference

**Input:** “Explain why that one is popular,” after discussing two Skills.

**Expected:** Uses the surrounding context if it resolves the reference. If the two interpretations would lead to different evidence or conclusions, asks one concise question with short options.

## 8. Evidence and causal limits

**Input:** “This Skill has many installs. Does that prove its method is effective?”

**Expected:** Separates the observable adoption count from effectiveness, explains other plausible reasons for adoption, and does not claim causal proof without evidence.

## Current validation record

**2026-11-15:** Static review passed for frontmatter, trigger/false-trigger boundaries, adaptive choice and fill-in guidance, evidence labels, and stop conditions. The project-level copy under `.agents/skills/unravel` matches the source. Real behavior scenarios remain **Not verified**: an isolated Codex CLI session started but produced no answer or loaded-skill path before it was stopped. The bundled `quick_validate.py` was unavailable because this Python environment lacks PyYAML. Do not report static coverage as agent acceptance.
