# Installation

A Skill is a folder with `SKILL.md` and any required supporting files. The installation location and discovery procedure depend on the Agent client.

## Pick a Skill

Open the [catalog](/Skills/#explore), check its description and constraints, and inspect its source before using it.

## Copy the entire folder

Clone the repository and copy the desired `skills/<name>/` directory into your Agent client's Skills location. The repository README currently documents these **Windows examples**:

| Client | Example location |
| --- | --- |
| Codex | `%USERPROFILE%\.codex\skills\<name>` |
| WorkBuddy | `%USERPROFILE%\.workbuddy-ai\skills\<name>` |

Check your client's current documentation and protect existing local files before copying.

## Unverified candidate CLI

```shell
npx skills add unraveltao/Skills
```

**This command has not yet passed an end-to-end installation test for this repository.** Do not interpret the displayed command as proof that all Skills can be installed by the CLI.

## Verify that your client loaded the Skill

1. Confirm `SKILL.md` and supporting files are present at the target location.
2. Reload or restart the client if its documentation requires it.
3. Test a harmless, read-only request and confirm the correct Skill was actually loaded.
4. Check platform dependencies, permissions, and safety limits separately.

Continue with [Using Skills](/Skills/docs/guides/using-skills/).