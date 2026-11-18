# Contributing to Unravel Skills

Thank you for your interest in contributing to **Unravel Skills**.

Unravel Skills is a collection of independently installable Agent Skills, supported by a public catalog and project documentation. Contributions are welcome in the form of new Skills, improvements, bug fixes, tests, documentation, and website changes.

This guide explains how to propose and validate changes while keeping the repository safe, understandable, and maintainable.

## 1. Before You Start

Before making changes:

1. Read the repository-level [AGENTS.md](AGENTS.md). It contains engineering and safety requirements for both human contributors and coding agents.
2. Identify the scope of your change:
   - **Repository-level:** website, shared documentation, catalog, CI, or project tooling.
   - **Skill-specific:** instructions, references, scripts, tests, or runtime code belonging to one Skill.
3. For a Skill-specific change, read that Skill's `SKILL.md` and the relevant references and tests first.
4. Check whether an existing issue or pull request already covers the same work.
5. Keep each contribution focused. Avoid combining unrelated Skills, website redesigns, and repository-wide refactors in one pull request.

For a substantial change or a new Skill concept, opening an issue to discuss the scope before implementation is recommended.

## 2. Ways to Contribute

You can contribute in several ways:

- **New Skills:** add a self-contained Skill that solves a clear, reusable problem.
- **Skill improvements:** clarify instructions, improve workflows, correct behavior, or strengthen safety boundaries.
- **Bug fixes:** fix incorrect instructions, broken scripts, website defects, or build failures.
- **Tests and validation:** add reproducible checks, isolated fixtures, or useful test scenarios.
- **Documentation:** improve project guides or documentation belonging to an individual Skill.
- **Website and tooling:** improve the catalog, Skill detail pages, Docs, accessibility, responsive behavior, or repository automation.
- **Issue reports:** provide a reproducible description of a problem or a concrete improvement proposal.

Please explain the problem being solved, not only the implementation you have in mind.

## 3. Development Workflow

A typical contribution follows this workflow:

1. **Discuss:** open or review an issue when the change is substantial.
2. **Fork:** create your own fork of the repository, if you are not a maintainer with direct branch access.
3. **Clone:** work from your fork rather than editing an unrelated local copy.
4. **Branch:** create a focused branch from the current target branch.
5. **Develop:** make the smallest coherent change that solves the problem.
6. **Validate:** run the relevant checks and inspect the resulting files or pages.
7. **Commit:** use a clear message describing the change.
8. **Pull request:** explain the motivation, implementation, validation, and remaining limitations.

Suggested branch names:

- `feat/<short-description>` — new functionality or a new Skill.
- `fix/<short-description>` — bug fixes.
- `docs/<short-description>` — documentation-only changes.
- `test/<short-description>` — tests and validation improvements.
- `chore/<short-description>` — maintenance and repository tooling.

Use the repository's current default branch as the base unless a maintainer or an issue specifies another target. Do not force-push to shared branches or rewrite another contributor's history without coordination.

## 4. Contributing a Skill

Every Skill must remain an independently understandable and installable package under `skills/<name>/`.

### 4.1 Required entry point

A Skill contribution must include:

```text
skills/
  <skill-name>/
    SKILL.md
```

The `SKILL.md` file is the authoritative Agent-facing entry point. It should make the Skill's purpose, activation context, workflow, constraints, and expected behavior understandable.

Follow the metadata and formatting conventions already used by the repository's Skills. Do not introduce new required metadata fields or a new manifest format without first discussing and documenting that repository-wide change.

### 4.2 Supporting files

Add supporting files when they serve a clear purpose:

- `README.md` — human-facing explanation, installation notes, examples, and important boundaries.
- `references/` — detailed instructions, specifications, policies, architecture, or supporting knowledge.
- `scripts/` — executable helpers required by the Skill.
- `tests/` — automated checks, fixtures, or reproducible test scenarios.
- Other assets — only when needed by the Skill and appropriately licensed.

These supporting directories are not mandatory for every Skill. Avoid adding empty folders or files that merely anticipate hypothetical future needs.

### 4.3 Scope and safety

A Skill should clearly state:

- what it is intended to do;
- when it should and should not be used;
- what inputs, tools, permissions, or dependencies it needs;
- which actions are read-only and which may change data or external state;
- what requires explicit user approval;
- how failures, uncertainty, and incomplete work are reported.

Do not imply that a Skill can access tools, applications, or permissions that the target Agent client does not provide. Instructions inside a Skill do not grant authorization by themselves.

### 4.4 Skill-specific documentation

Keep a Skill's own usage guide, architecture, implementation details, safety policy, and technical references inside its package.

For example:

```text
skills/
  <skill-name>/
    SKILL.md
    README.md
    references/
      architecture.md
      safety-policy.md
```

The root `docs/` directory is for documentation about the repository as a whole. Do not move an individual Skill's internal architecture into the global project Architecture document.

## 5. Documentation Contributions

The repository uses Markdown as the primary documentation format.

Use these locations:

| Documentation | Location |
| --- | --- |
| Project introduction and repository-wide architecture | `docs/concepts/` and the project entry pages |
| Installation and first-use guidance | `docs/getting-started/` |
| Task-oriented usage guides | `docs/guides/` |
| Shared formats and stable interfaces | `docs/reference/` |
| Contribution, validation, and development records | `docs/development/` |
| A particular Skill's usage and technical documentation | `skills/<name>/` |

The website's Docs section renders selected Markdown files from the root `docs/` directory. When adding, renaming, or removing a public Docs page:

1. Update the relevant Markdown file under `docs/`.
2. Update the navigation registry in `web/src/lib/docs.ts`.
3. Check internal links and heading anchors.
4. Build the website and verify the generated route.
5. Keep the public documentation consistent with the actual implementation.

Do not maintain a second copy of the same article solely for the website.

When writing documentation:

- Prefer clear, descriptive headings and concise explanations.
- Explain the reader's goal before diving into implementation details.
- Include examples when they make a procedure easier to reproduce.
- Distinguish implemented behavior from planned work.
- Label unverified commands, compatibility claims, and limitations honestly.
- Preserve historical reports as historical records; do not silently turn an old test result into a current guarantee.
- Link to a Skill's own documentation rather than copying its internal details into global Docs.

See [Documentation Standards](docs/development/documentation-standards.md) for the detailed placement and writing rules.

## 6. Website and Repository Tooling

The website source lives in `web/` and is built with Astro.

For website changes:

1. Read the relevant files and existing components before editing.
2. Keep shared project documentation in `docs/` and website implementation in `web/`.
3. Check that navigation, links, theme variants, and responsive layouts remain usable.
4. Run the website's available data checks and production build.
5. Verify the generated pages affected by the change.

For repository scripts and CI:

- Keep automation scoped to the repository and document non-obvious behavior.
- Prefer deterministic checks and clear failure messages.
- Do not commit local caches, generated reports, databases, credentials, or machine-specific paths unless they are intentionally part of the project.
- Do not add a dependency when the existing toolchain can reasonably perform the task.

Use the commands documented by the relevant package or workflow. Do not assume that a command from another Skill or another project applies here.

## 7. Testing and Validation

Validation must match the risk and scope of the change.

Where relevant, distinguish these levels in your pull request:

1. **Structural checks:** required files, metadata, links, and expected directory layout.
2. **Automated tests:** unit, integration, or repository checks that were actually run.
3. **Isolated tests:** scripts or workflows exercised against temporary directories and test fixtures.
4. **Real-client testing:** behavior verified in a named Agent client and version, with the tested scenario described.

A successful website build does not prove that a Skill behaves correctly in every Agent client. A passing script test does not prove that the complete Skill workflow has been accepted by a real Agent.

### Safety requirements

- Use temporary directories or isolated fixtures for tests that create, move, modify, or delete files.
- Never run destructive tests against a contributor's real user data, production data, or an external service.
- Do not include credentials, tokens, private user data, local databases, logs, or personal machine paths in commits or test artifacts.
- Do not perform consequential operations against external systems unless the test explicitly requires them and the required authorization is established.
- Report tests that could not be run. Do not claim that a check passed if it was not executed.

These requirements are consistent with the repository's [AGENTS.md](AGENTS.md).

## 8. Pull Request Guidelines

Before opening a pull request, make sure that:

- the change has a clear purpose and a focused scope;
- the relevant Skill or repository instructions have been read;
- generated files and unrelated local changes have not been included accidentally;
- relevant tests or build checks have been run;
- documentation reflects the actual behavior;
- third-party material and dependencies have compatible licenses and appropriate attribution.

A pull request should include the following information:

```text
## Summary
What changed?

## Motivation
What problem does this solve?

## Scope
Which Skills, website pages, or repository areas are affected?

## Validation
What checks were run, and what were their results?

## Limitations
What remains untested, unsupported, or intentionally out of scope?
```

Use a concise, descriptive pull request title. If the change affects user-facing behavior, include screenshots or a short reproduction procedure when useful.

Maintainers may request changes, ask for additional validation, or decline a contribution that is outside the project's scope or does not meet its safety and maintenance requirements.

## 9. Third-Party Code, Content, and Assets

Before contributing copied or adapted code, documentation, images, fonts, datasets, or other materials:

- verify that the source permits the intended use and redistribution;
- preserve required copyright notices and attribution;
- record the source and license where appropriate;
- do not assume that publicly accessible material is free to redistribute;
- do not remove another author's license or attribution notices.

If a contribution introduces a dependency, explain why it is needed and identify its license.

## 10. License

The project currently includes the [MIT License](LICENSE).

By submitting a contribution, you confirm that you have the right to submit it and agree that the contribution may be distributed under the repository's MIT License, unless you and the project maintainers have made a separate written agreement.

You retain any rights you hold in your contribution; this guide does not request a copyright assignment.

## 11. Questions and Discussions

If you are unsure where a change belongs, whether a Skill fits the project, or how to validate a proposed workflow, open a discussion or issue in the GitHub repository before investing in a large implementation.

Clear questions, reproducible reports, careful documentation, and small improvements are all valuable contributions.

Thank you for helping make Unravel Skills more useful, reliable, and maintainable.
