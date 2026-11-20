import { readFileSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { renderMarkdown } from './markdown';

const contentRoot = resolve(process.cwd(), 'src/content/blog');

export const posts = [
  {
    slug: 'skill-candidate',
    title: 'A Task Worth Turning into an Agent Skill?',
    summary: 'Start with a recurring workflow, not a Markdown file. Learn how to tell whether a task is a good candidate for a reusable Skill.',
    order: 1,
    file: '01-skill-candidate.md',
  },
  {
    slug: 'skill-behavior-spec',
    title: 'Turn a Candidate Task into a Behavior Specification',
    summary: 'Define when a Skill should activate, what it needs, how it should work, and what a good result looks like.',
    order: 2,
    file: '02-skill-behavior-spec.md',
  },
  {
    slug: 'write-skill-md',
    title: 'From Behavior Specification to SKILL.md',
    summary: 'Turn the behavior you designed into concise, actionable instructions and add supporting files only when they help.',
    order: 3,
    file: '03-write-skill-md.md',
  },
  {
    slug: 'design-skill-tests',
    title: 'Design Tests for an Agent Skill',
    summary: 'Build test cases for both activation and task execution, with observable expectations instead of exact-match answers.',
    order: 4,
    file: '04-design-skill-tests.md',
  },
  {
    slug: 'improve-skill-from-failures',
    title: 'Improve a Skill by Learning from Test Failures',
    summary: 'Trace failures back to the specification, instructions, or environment, then make focused changes and rerun regression cases.',
    order: 5,
    file: '05-improve-skill-from-failures.md',
  },
  {
    slug: 'release-maintain-skill',
    title: 'Release and Maintain a Skill',
    summary: 'Check a Skill before release, explain its limits, record changes, and use real feedback to guide the next iteration.',
    order: 6,
    file: '06-release-maintain-skill.md',
  },
] as const;

export type BlogPost = (typeof posts)[number];

export function getBlogPost(slug: string) {
  const post = posts.find((item) => item.slug === slug);
  if (!post) return undefined;

  const markdown = readFileSync(join(contentRoot, post.file), 'utf8');
  return { ...post, html: renderMarkdown(markdown) };
}
