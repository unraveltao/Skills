# README Skill

README Skill helps you create, review, rewrite, or improve a project's README using repository evidence and a reader-focused structure. It scopes the work before editing, distinguishes confirmed facts from assumptions, and reports checks it did not run.

## When to use it

This Skill supports five routes:

- Create a project README.
- Rewrite or substantially restructure one.
- Review and report findings without editing.
- Improve it with focused changes rather than defaulting to a rewrite.
- Make a targeted edit to explicitly named content.

If file changes are not authorized, it can return a draft or review report.

## How it works

It identifies the repository root and relevant project type, inspects files needed for consequential claims, and distinguishes repository evidence from user-provided information, inference, unknowns, and conflicts.

For a full create or rewrite, it establishes the primary reader and goal, proposes an information structure, and waits at required approval gates before drafting or structural changes. Structure approval and permission to edit are separate. Narrow edits and reviews use a shorter path.

As applicable, verification covers Markdown structure and local links, factual claims and evidence, commands/examples only when authorized and safe to run, reader experience (with AI review identified as simulated rather than user research), and scope/change safety. Checks use explicit states such as PASS, FAIL, UNVERIFIED, NOT RUN, or N/A.

## Boundaries and safety

README Skill does not invent commands, APIs, settings, versions, compatibility claims, badges, metrics, or shipped features. It does not expand into organization/profile READMEs, a documentation website/system, project management, deployment, release, or Git operations unless separately requested and authorized.

Editing, running commands, changing image resources, committing, pushing, and publishing are distinct actions with separate authorization requirements.

## Supporting files

- [Skill instructions](SKILL.md)
- [Repository understanding](references/repository-understanding.md)
- [Reader and product](references/reader-product.md)
- [Information architecture](references/information-architecture.md)
- [Writing and visuals](references/writing-visual.md)
- [Verification and review](references/verification-review.md)
- [Behavior scenarios](tests/scenarios.md)

The scenarios are prompts and expected behavior, not test results. Static inspection cannot establish automatic routing or interactive behavior.

## Validation status

No behavior scenario, client compatibility, installation path, or runtime outcome is claimed as verified by this README. Run scenarios against controlled fixture repositories in a clean session with evidence that the Skill loaded, then record scenario type and actual outcomes.

See the repository [Installation guide](../../docs/getting-started/installation.md); supported paths depend on the client. The Skill metadata declares MIT; see the repository [LICENSE](../../LICENSE).
