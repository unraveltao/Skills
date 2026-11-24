# Create a README with Awesome Copilot

`create-readme` is an Agent Skill maintained in GitHub Awesome Copilot. It guides an Agent through inspecting a project, choosing a clear structure, and writing a concise GitHub README with the project's own details and assets. Use it to draft a new README or ask explicitly for a reorganization of an existing one. [Upstream Skill](https://github.com/github/awesome-copilot/blob/main/skills/create-readme/SKILL.md)

## Install from GitHub Awesome Copilot

From your project directory, use the command listed in the upstream catalog. It requires GitHub CLI v2.90.0 or later. Confirm that your Agent client can load the Skill from the location selected during installation. [Upstream installation instructions](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md#how-to-use-agent-skills)

```sh
gh skills install github/awesome-copilot create-readme
```

We have not verified this command end to end or checked whether an Agent client discovers the installed Skill.

## Try it on an existing README

Open the project in your Agent client and ask for a draft you can review:

> Use create-readme to review this repository and propose a new layout for the README. Put the reader’s first useful action near the top. Preserve verified commands, links, and limitations. Show the proposed draft before changing README.md.

Before publishing, check that the links work and that installation, compatibility, and project status match the repository evidence.

## How we used it

We applied the upstream instructions to a read-only drafting trial for Unravel Skills. The resulting layout puts common tasks and example Skills before installation and maintainer information. The trial exercised the instructions and editorial workflow. Installation and Agent-client discovery were outside its scope.

## Previous Unravel README Skill

Unravel previously maintained its own README Skill. Its review-only and targeted-edit examples are preserved in the [historical package guide](https://github.com/unraveltao/Skills/blob/0dbb3c07cd4cc41ed6d2d1a2880bd785e0bcb735/skills/readme/README.md). The upstream Skill documents a project README drafting workflow. Check its current instructions before relying on other behavior. If you installed the old package locally, manage that copy separately in your Agent client's Skills location.
