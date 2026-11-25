# GitHub Project Coach

GitHub Project Coach helps you understand a GitHub repository or Gist and learn how to use one of its capabilities. It grounds the explanation in the project's README, examples, configuration, and source files. It provides a practical first-use path, not a generic code review.

## When to use it

Use this Skill when you have a GitHub repository or Gist and want to understand what it does, choose a capability for your goal, find prerequisites and first-use steps, or identify limitations and open questions.

## How it works

The Skill reads the project's landing page and relevant primary files, following references into source when needed to verify an advertised entry point, inputs, outputs, and constraints.

A useful explanation may include:

1. What the project does and which capability fits your goal.
2. Prerequisites and a practical setup path.
3. A first command or code example and what success should look like.
4. A likely first troubleshooting check.
5. Limitations, assumptions, and source links.

It distinguishes documented claims, source-verified facts, and assumptions. It says when a step was not run and describes something as tested only when it was actually executed in a suitable environment.

## Example request

> Please inspect a GitHub repository or Gist and show me the shortest practical way to use one of its capabilities.

You can provide a URL and ask for a general orientation if you are not yet sure which capability you need.

## Boundaries

- Reading public project content is in scope.
- Installing dependencies, running project code, changing local files, or modifying or publishing a remote repository are separate actions.
- A project being hosted on GitHub does not establish that its code is safe to run.
- If the project cannot be accessed with available tools, the Skill should say so instead of implying it inspected the source.

## Package contents

- [SKILL.md](SKILL.md) — activation boundary, source-based workflow, response shape, and scope.

The package contains no bundled scripts, references, or tests directory. No automated test suite or real-Agent behavior result is claimed.

## Installation and license

Copy the complete Skill folder into a Skills location supported by your Agent client. The location and discovery process vary by client; see the repository [Installation guide](../../docs/getting-started/installation.md) and your client's documentation.

The Skill metadata declares MIT. See the repository [LICENSE](../../LICENSE).

This pass found no executable package suite. Real-client behavior remains unverified. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
