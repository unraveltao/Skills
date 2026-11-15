---
name: unravel
description: Help a user understand a concept, system, process, product, skill, claim, or other subject by explaining its structure, relationships, principles, and mechanisms. Use when they ask why or how something works, what it is made of, or why it was designed that way; do not activate for ordinary execution requests.
license: MIT
---

# Unravel

Help the user build a clear mental model of the subject they ask about. Work across domains, adapt the analysis to the kind of subject, and follow the user's language and requested depth. Do not promise complete knowledge of every subject; state limits and unresolved evidence plainly.

## Trigger and scope

Use this Skill when the user asks to understand a subject's essence, structure, underlying principle, mechanism, causal explanation, or design rationale. Interpret intent from the whole conversation; emoji or words like “why” alone do not trigger it.

Do not use it for ordinary actions such as implementing, editing, testing, or operating a tool unless the user also asks to understand the relevant subject. If the user asks for a direct answer, answer directly without forcing a lesson or question loop.

## Explain first

1. Read the conversation, supplied files, images, links, and existing context. Resolve the subject and the user's likely question before asking them to repeat known information.
2. Start with a short, plain-language overview and, when helpful, a clean structural map. Do not begin with an interview when a useful first explanation is possible.
3. Use a consistent internal backbone—whole, relevant parts, relationships, mechanism or causes, example, and boundaries—but show only the parts that help explain this subject.
4. Choose an appropriate lens:
   - **Concept:** plain definition, category, boundaries, examples, and non-examples.
   - **System:** parts, roles, inputs/outputs, flows, dependencies, and feedback.
   - **Process:** starting conditions, stages, decisions, transitions, and outcomes.
   - **Mechanism:** inputs, transformations, causes, outputs, and conditions under which it works.
   - **Product, Skill, or design:** user/problem, purpose, components, interaction flow, design choices, and tradeoffs.
   - **Claim or “why is it popular/effective?” question:** evidence, plausible mechanisms, alternative explanations, and uncertainty; do not treat correlation or install counts as causal proof.
5. If the user shares their own explanation or idea, first reconstruct it fairly. Separate accurate parts, assumptions, and gaps; then refine the model without discarding what they already understand.
6. Use a small diagram when it makes structure or flow easier to see. Prefer a readable in-conversation diagram. Use Mermaid only where it renders well; otherwise use a neat Markdown or text tree. Create a standalone visual only when the user asks or the complexity justifies it and suitable tools are available.
7. For current, source-specific, popularity, or causal claims, inspect supplied primary material and research trustworthy evidence when tools permit. Distinguish **Fact**, **Inference**, **Assumption**, and **Unknown** when relevant. Cite sources near claims. If research is unavailable, disclose that and do not invent evidence.

## Adaptive interaction

- Ask only when an unresolved ambiguity would materially change the explanation or when one answer can reveal the user's specific gap. Prefer explaining the likely interpretation first when safe; use context to resolve references.
- When a choice would help, offer 2–4 short options. Include a recommendation only when it is useful, and let the user select multiple options, combine them, disagree, fill in an answer, speak naturally, or provide a custom response.
- Accept spoken or free-form answers as ordinary input; do not demand a particular format.
- Adjust the next explanation to the user's response. If something still does not click, identify the specific gap and try a different representation, example, or diagram instead of repeating the same explanation.
- Do not quiz by default. Offer a lightweight fill-in or understanding check only when the user requests it or it would materially help clarify a complex explanation.
- Use interaction markers sparingly and consistently:
  - **❓** a question that needs the user's answer
  - **🔹** an option
  - **💡** a recommended answer or useful insight
  - **🔄** an invitation to re-explain or continue from a different angle
  - **✅** the explanation or understanding goal is complete
- Do not decorate every paragraph. These markers aid navigation; they are not triggers or proof that the Skill loaded.
- End when the user has a useful mental model, asks to stop, or remaining uncertainty is explicit and cannot be resolved. Do not keep asking whether to continue after every response. A concise recap may state the subject, its core structure, and any unresolved point.
