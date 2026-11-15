# Design handoff: Tool Usage Research Guide Skill

## Purpose

- **Problem:** Users find long product documentation difficult to navigate and may not know which features or practices are useful for their goals.
- **Desired outcome:** Ask a question about GitHub, Codex, or a related feature and receive a current, understandable, sourced answer; useful knowledge can accumulate in user-controlled topic guides.
- **Target users:** A person learning to use developer and collaboration tools who prefers asking concrete questions over reading large manuals end to end.

## Recommended direction

Create a general-purpose Agent Skill that researches the user's specific question, answers it directly, and offers or performs a scoped guide update when the user wants durable reference material. The Skill should be a research-and-reference assistant, not an always-on tutor. It may explain concepts or propose a short practical example when useful, but should not force a sequential lesson.

Research should prioritize current official documentation for product behavior, supplemented by credible practitioner material for workflows and advanced techniques. Clearly distinguish official facts, practitioner recommendations, and the Skill's own synthesis. Include citations and an access/review date for material claims. When browsing is unavailable, disclose that and avoid presenting changeable details as verified current facts.

## Scope

### In scope

- Answer questions about GitHub, Codex, and user-added tools or topics.
- When exploring existing Skills or reusable Skill patterns, restrict discovery to Skill libraries with meaningful adoption evidence; do not fill results with obscure or low-usage catalogs.
- Research the relevant official documentation instead of requiring the user to read it all.
- Find and assess credible advanced-use guidance; explain its source and applicability.
- Explain feature purpose, when to use it, practical steps, limitations, and common pitfalls.
- Adjust how much research to perform separately from how much detail to show: investigate enough to support the answer, then present only what is useful for the user's question.
- Structure durable reference content by tool and topic (for example, GitHub/Gist, GitHub/Projects, Codex/tasks).
- When the user asks to maintain a guide, propose a focused addition or revision, retain source links and review dates, and distinguish new findings from existing content.
- Use incremental research: reuse existing guide material, then check only what is needed to answer the new question and update affected sections.
- Adapt explanation depth to the question; offer optional examples or practice without turning every answer into a course.

### Out of scope

- Automatically teaching a fixed curriculum or requiring step-by-step lessons.
- Claiming access to private account state or performing actions inside GitHub/Codex without an explicit request and available authorized tools.
- Automatically selecting, creating, or changing the user's guide storage location.
- Treating unsourced social posts or isolated anecdotes as authoritative product behavior.
- Searching Skill marketplaces without regard to adoption when the user asks for widely used Skill libraries.
- Mirroring entire documentation sites or accumulating unreviewed copied text.

## Typical interaction

1. The user asks a concrete question, such as “What are GitHub Projects and when should I use them?”
2. The Skill checks any available topic guide and relevant conversation context, then researches authoritative current sources and useful practitioner perspectives.
3. It gives the direct answer first, followed by practical guidance, caveats, and links. It marks what is official behavior versus a recommended workflow.
4. It offers a guide update only when the finding is useful beyond the immediate answer or the user asks to save it. If no location is known, it answers without saving and asks for a destination only when the user requests durable storage.
5. The user chooses the root location and explicitly authorizes the update mode. Under the recommended mode, sourced additive updates may then be saved automatically. Until both location and authorization are established, it shows a copyable draft and does not write files.
6. On later questions, it reuses the guide, checks freshness for facts likely to change, and updates only affected topics within the user's authorization. Destructive, structural, or conflict-resolving changes require explicit confirmation.

## Guide organization

The Skill itself must not assume that all agents have persistent file access. When the user supplies a destination, a simple Markdown layout is recommended, subject to their preference:

```text
<user-chosen-guide-root>/
  index.md
  github/
    gist.md
    projects.md
  codex/
    getting-started.md
    workflows.md
```

Each topic page should include purpose, when to use it, practical workflow, limitations/pitfalls, source links, last checked date, and unresolved questions. Avoid creating empty pages for topics the user has not asked about.

## Research and update rules

- Prefer official documentation and release notes for current features, product behavior, and restrictions.
- Use credible practitioner material for patterns and efficiency advice; label it as experience or recommendation, not official guidance.
- Check dates and product version/context when relevant. Recheck volatile claims before reusing them.
- Look for limitations and contrary evidence for consequential recommendations.
- Cite claims close to the relevant text. Never fabricate sources or imply a page was read when it was not accessible.
- Summarize in original words; quote only short excerpts when needed and allowed.
- For Skill-library discovery, use adoption evidence the catalog actually exposes (for example, installs, downloads, or usage counts); report its meaning and checked date. If comparable usage data is unavailable, do not label a library “widely used” based on guesswork. Popularity is a discovery filter, not proof of quality: inspect maintenance, documentation, compatibility, source provenance, and relevant user feedback before recommending a Skill.
- Before a file update, show the target path and concise diff/summary; wait for approval. If no persistence or path is available, provide a copyable proposed section instead.
- Preserve user edits and existing guide structure. Update only affected sections and retain an update date/source trail.
- Treat storage path and write authorization as separate choices: naming a folder does not by itself authorize writes.
- Do not create empty topic pages. Offer durable updates when content is reusable, but do not turn every answer into a save prompt.

## Acceptance criteria

1. Given “What is GitHub Gist and how do I use it?”, the Skill answers directly with current official sources and does not ask whether the user has an account unless account state is necessary.
2. Given a request to design or update a guide on GitHub Projects, it distinguishes official feature behavior from recommended project-management practices.
3. Given a question about Codex, it uses current official documentation when available and flags uncertainty or version-sensitive details.
4. Given an existing guide, it reuses relevant material and checks only claims that need freshness verification.
5. When no guide path is configured, it does not invent one or write files; it can answer normally and provide a copyable draft if asked.
6. Before any requested guide write, it presents the target and proposed change and obtains user confirmation.
7. Guide updates preserve citations, checked dates, existing user content, and a clear history of substantive changes.
8. When research tools are unavailable, it clearly distinguishes remembered general knowledge from verified current information and does not fabricate citations.
9. An explanation may include optional hands-on examples, but the Skill does not force a lesson sequence or switch from research to tutoring without user intent.
10. When asked to explore widely used Skill libraries, it filters by observable adoption evidence, states the metric/date and does not equate popularity with quality.

## Decisions and open questions

- **Confirmed direction:** Research questions and incrementally maintain user-requested reference guides.
- **Confirmed constraint:** The user decides the guide storage location; the Skill must not choose it unilaterally.
- **Confirmed update authorization:** After the user specifies a guide location and grants one-time authorization, sourced additive updates may be saved automatically. Deletions, structural changes, and evidence conflicts require confirmation. Naming a location alone is not authorization.
- **Confirmed initial scope:** GitHub and Codex. Other tools may be added when the user requests them.
- **Confirmed discovery preference:** When searching for existing Skills, focus only on libraries with evidence of substantial usage; verify the adoption metric rather than relying on popularity claims.
- **Open question:** Research depth should scale to question impact and volatility; do not impose a fixed number of sources for every answer.

## Handoff notes

This is a design proposal for a future standalone Skill, not an implementation. No third-party source text or code is included. Before implementation, inspect the target agent's Skill format and available research tools; keep the core usable without any single platform-specific UI.
