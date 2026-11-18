# Skill Structure

Each `skills/<name>/` folder is intended to be independently installable.

## Required entry point

```text
skills/
  example-skill/
    SKILL.md
```

The `SKILL.md` file contains metadata (such as name and description), instructions, workflow, and restrictions. Consult the actual package rather than assuming all Skills share one runtime.

## Optional files

```text
skills/
  example-skill/
    SKILL.md
    README.md
    references/
    scripts/
    tests/
```

- `README.md` explains the Skill to human readers when present.
- `references/` contains further instructions and specifications.
- `scripts/` contains executables only when needed.
- `tests/` contains test code or scenarios when present.

These resources are **optional**. A missing README does not mean a missing Skill.

## Website data and lifecycle

Today the catalog reads `SKILL.md` and optional README content, with a provisional category/tag mapping. Formal manifest validation, independent versioning, and machine-readable exports are planned work, not completed features. See [Architecture](/Skills/docs/concepts/architecture/).