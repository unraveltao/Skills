# Documentation Standards

These rules keep repository documentation useful without duplicating every Skill's internal documentation.

## Where documentation belongs

| Content | Location |
| --- | --- |
| Project overview and repository-wide architecture | `docs/concepts/` |
| Installation and first-use guidance | `docs/getting-started/` |
| Task-oriented workflows | `docs/guides/` |
| Stable file formats and interfaces | `docs/reference/` |
| Contribution, validation, plans, and historical records | `docs/development/` |
| Skill-specific usage, architecture, safety, references | `skills/<name>/` |

A Skill's architecture belongs with that Skill. The global Architecture document should explain only repository-wide boundaries and relationships.

## Writing

- Prefer short, descriptive headings.
- Explain the user's goal before implementation detail.
- Use concrete examples when they remove ambiguity.
- Distinguish current behavior from planned behavior.
- Do not describe an unverified command, feature, or compatibility claim as supported.
- Link to the authoritative Skill source instead of copying large sections into global Docs.
- Preserve historical validation records when they provide evidence; do not silently rewrite them into current guarantees.

## Skill README

A Skill README is the human-facing entry point for that Skill. It should normally answer:

1. What is this Skill?
2. When should I use it?
3. What does it do and not do?
4. What are its important safety or compatibility boundaries?
5. Where are the detailed references?
6. What version or implementation boundary applies?

The README may link to the Skill's architecture document rather than duplicating its complete implementation.

## Markdown and website

Repository Docs are Markdown-first. The website renders selected Markdown files into the public Docs navigation.

When adding a public page, add it to `web/src/lib/docs.ts` and verify its generated route. Do not create a second copy solely for the website.
