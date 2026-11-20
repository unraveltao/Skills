# Skill README Template

Use this template for a human-facing overview of one Skill package. Ground claims in SKILL.md, supporting references, and observed validation evidence. Remove sections that do not apply; do not fill gaps with assumptions.

## Recommended structure

# <Skill name>

<One short paragraph: what the Skill helps with and its main boundary.>

## When to use it

<Concrete user goals and requests that fit. Mention nearby requests that do not fit when useful.>

## What it does

<Describe the observable workflow and likely outputs, without restating every instruction.>

## Example

<One representative request or safe, clearly labeled example. Do not imply it was executed.>

## Boundaries and limitations

<What it does not do, safety/privacy limits, dependencies, and client/tool constraints.>

## Package contents

- SKILL.md — authoritative behavior and scope.
- <Only list files that exist and help users understand the package.>

## Validation status

<State exactly what was checked, what was run, and what remains unverified. A test plan is not a test result.>

## References

<Relevant package and repository docs; include license only when confirmed in source.>

## Authoring rules

- Describe the package as it exists today; separate planned work from current behavior.
- Prefer user outcomes, examples, and boundaries over a catalog of internal modules.
- Keep the README short enough to scan. Link to SKILL.md and detailed references instead of duplicating them.
- Explain install/discovery only when repository documentation supports it; otherwise point to the repository installation guide and note client differences.
- Never infer support, compatibility, version, license, runtime success, automatic triggering, or test results.
- For test-driven packages, link test instructions and distinguish executable tests from manual behavior scenarios.
- After real testing, update validation with client/version, date, scenario, result, and evidence. Preserve unresolved failures and limitations.
