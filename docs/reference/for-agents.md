# For Agents

Unravel Skills is an instruction catalog, **not an Agent execution environment**.

## Reading a Skill

1. Determine whether a task fits a particular Skill's published scope.
2. Inspect the [catalog](/Skills/#explore) and the corresponding `SKILL.md` source in the [repository](https://github.com/unraveltao/Skills/tree/main/skills).
3. Load only relevant references and satisfy declared prerequisites.
4. Respect client permissions and require human approval for consequential actions.

## Discovery limitations

`catalog.json`, `llms.txt`, and exported Markdown are **planned for M3.2**, not currently available as a supported catalog API. Even after publication, automatic discovery depends on the Agent client and cannot be assumed.

## Installation and safety

See [Installation](/Skills/docs/getting-started/installation/) for the current manual workflow and unverified CLI candidate. No website text authorizes local execution, deletion, or publishing.