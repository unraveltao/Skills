# Learning Coach

Learning Coach is an instruction-based Agent Skill for learning across technical and other subjects. It can help plan a course, teach concepts interactively, guide practice, assess understanding, organize notes when requested, and resume from a learner-provided progress record.

## When to use it

Use this Skill to plan or continue a learning path, understand a concept, practice through an exercise or learner-owned project, check understanding, create a knowledge note, or save and resume progress using a record you control. A single request may use only one activity; a longer journey can combine several.

## How the learning workflow works

For a course, the Skill can agree on a revisable outline, teach concepts, offer practice, and assess evidence. When a gap appears, it can focus on that concept rather than restarting the course. Practice should have observable criteria, and assessments should use evidence from your answers or inspected work.

You control the pace, topic, and amount of interaction. A learning project is an exercise; the Skill does not take over delivery of a real product or project.

## Notes, progress, and privacy

- The Skill saves a formal note only when you ask or agree.
- A progress record is a private, user-controlled Markdown file outside the Skill installation directory and any public repository.
- To resume, provide the record or a brief recap; automatic cross-session memory is not assumed.
- The Skill does not provide a database or cloud sync for personal learning records.
- States such as Verified, Unverified, and Needs reinforcement should be tied to evidence. Missing evidence is not proof of inability.

## Implementation boundary

The Skill consists of Markdown instructions and references; no external service or runtime program is declared. Available Agent tools affect whether research, hands-on exercises, and code verification can be performed. Unrun work should be reported as unverified.

## Supporting files

- [Skill instructions](SKILL.md)
- [Curriculum planning](references/curriculum.md)
- [Teaching](references/teaching.md)
- [Practice](references/practice.md)
- [Assessment](references/assessment.md)
- [Notes](references/notes.md)
- [Learning workflow and progress](references/learning-workflow.md)
- [Teaching-method improvements](references/evolution.md)

## Validation status

These are suggested manual scenarios, not recorded test results. They were not run for this README update: request a course outline; learn a concept and check for a useful understanding check; organize material into a note; assess with a fresh task; resume with and without a progress record; and try a non-technical topic and a one-off request.

Record the client, date, scenario, and evidence for any real-client validation. Do not treat this list as proof that the Skill passed those checks.

See the repository [Installation guide](../../docs/getting-started/installation.md); paths and discovery vary by client. MIT licensed; see the package [LICENSE](LICENSE).

The README's example scenarios remain a manual validation plan. No executable package suite or independently loaded behavior run was recorded in this pass. See the [repository validation matrix](../../docs/development/skill-validation-matrix.md) for the setup, expected checks, and remaining gaps.
