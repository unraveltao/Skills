# Information Architecture

## Purpose and routing

Design the README as a project entrypoint around a confirmed reader goal. Identify CREATE, REWRITE, REVIEW, IMPROVE, or TARGETED EDIT. A partial request stays partial; a user request to review does not authorize edits.

## Audit existing content

For each relevant current section or claim, assign:

- **KEEP** — accurate and useful in the current README.
- **REPAIR** — useful but inaccurate, stale, unclear, or broken.
- **RELOCATE** — useful detail better suited to a separate existing or explicitly proposed document.
- **REMOVE** — obsolete, duplicate, unsupported, or harmful to the reader path; explain evidence and impact.
- **CONFIRM** — removal, relocation, product direction, or accuracy cannot be resolved without the user.

Do not delete merely because a section is absent from a preferred outline. Do not silently make bulk removals or migrations. Verify a relocation destination exists; otherwise list the proposed new file and include it in the approval scope.

## Select and prioritize content

- **Essential** — directly enables the primary reader's goal or essential understanding.
- **Conditional** — include when supported and useful to this project/maturity/reader.
- **External** — deep API, architecture, contribution, operations, or reference detail that should live in linked documentation when available.

Keep the first-reading path focused. An early section should answer what the project is and lead to the primary goal (for example, first install/use, try a demo, or understand a language/library). Section labels and order are adaptive, not mandatory.

## Adapt to project shape

Consider combinations such as Library/SDK, CLI, Desktop/Mobile Application, Web Application, API/Service, Agent Platform, Programming Language, and Monorepo. Select sections from evidence and reader needs. Examples of possible sections—not a required template—include overview, capabilities, install/quick start, example, demo, configuration, API links, architecture links, contributing, support, security, license, and roadmap.

For a monorepo, establish the root README's role and map child projects to their own READMEs. Do not duplicate all package guides at root. Link only to verified paths; if the target README is missing, describe the proposed documentation boundary without pretending it exists.

## Approval gate

Present a README Structure Plan and wait for explicit approval before:

- creating a complete README;
- rewriting an existing README;
- major section/order changes;
- bulk removal or migration;
- changing the primary reader or emphasis.

A small, clearly scoped local edit can skip the complete plan. If the user already approved the concrete plan, do not ask again for that decision. Structure approval and file-edit permission remain separate. A user request to implement the task can authorize in-scope edits, but does not waive the structure gate.

## Structure Plan format

```text
README Structure Plan
- Task type and design goal:
- Primary reader and goal:
- Proposed sections (order, purpose, evidence):
- Content audit (KEEP/REPAIR/RELOCATE/REMOVE/CONFIRM):
- Essential / Conditional / External choices:
- Facts, assumptions, conflicts, and open decisions:
- Affected files (including proposed relocation targets):
- Structural/change risks:
```

Keep concise and include only relevant sections. Never write files while approval is pending. On approval, hand this plan and all confirmed facts, priorities, preservation constraints, and decisions into Writing & Visual Design.
