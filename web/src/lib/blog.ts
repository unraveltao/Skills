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
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '01-skill-candidate.md',
  },
  {
    slug: 'skill-behavior-spec',
    title: 'Turn a Candidate Task into a Behavior Specification',
    summary: 'Define when a Skill should activate, what it needs, how it should work, and what a good result looks like.',
    order: 2,
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '02-skill-behavior-spec.md',
  },
  {
    slug: 'write-skill-md',
    title: 'From Behavior Specification to SKILL.md',
    summary: 'Turn the behavior you designed into concise, actionable instructions and add supporting files only when they help.',
    order: 3,
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '03-write-skill-md.md',
  },
  {
    slug: 'design-skill-tests',
    title: 'Design Tests for an Agent Skill',
    summary: 'Build test cases for both activation and task execution, with observable expectations instead of exact-match answers.',
    order: 4,
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '04-design-skill-tests.md',
  },
  {
    slug: 'improve-skill-from-failures',
    title: 'Improve a Skill by Learning from Test Failures',
    summary: 'Trace failures back to the specification, instructions, or environment, then make focused changes and rerun regression cases.',
    order: 5,
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '05-improve-skill-from-failures.md',
  },
  {
    slug: 'release-maintain-skill',
    title: 'Release and Maintain a Skill',
    summary: 'Check a Skill before release, explain its limits, record changes, and use real feedback to guide the next iteration.',
    order: 6,
    seriesId: 'skill-authoring',
    seriesNumber: 1,
    seriesTitle: 'Skill Authoring Series',
    seriesDescription: 'Follow the process from first idea to a maintained Skill.',
    file: '06-release-maintain-skill.md',
  },
  {
    slug: 'workflow-checklist',
    title: 'When a Workflow Stops Being a Checklist',
    summary: 'Recognize the states, decisions, and branches hidden inside a multi-step task before you turn it into a Skill.',
    order: 1,
    seriesId: 'advanced-skill-design',
    seriesNumber: 2,
    seriesTitle: 'Advanced Skill Design',
    seriesDescription: 'Design reliable Skills for realistic, multi-step work.',
    file: 's2-01-workflow-checklist.md',
  },
  {
    slug: 'model-workflow',
    title: 'Model the Workflow Before Writing Instructions',
    summary: 'Turn a task map into an executable path with clear branches, stop conditions, and recovery paths.',
    order: 2,
    seriesId: 'advanced-skill-design',
    seriesNumber: 2,
    seriesTitle: 'Advanced Skill Design',
    seriesDescription: 'Design reliable Skills for realistic, multi-step work.',
    file: 's2-02-model-workflow.md',
  },
] as const;

export type BlogPost = (typeof posts)[number];

export const blogSeries = [
  {
    id: 'skill-authoring',
    number: 1,
    title: 'Skill Authoring Series',
    description: 'Follow the process from first idea to a maintained Skill.',
    posts: posts.filter((post) => post.seriesId === 'skill-authoring'),
  },
  {
    id: 'advanced-skill-design',
    number: 2,
    title: 'Advanced Skill Design',
    description: 'Design reliable Skills for realistic, multi-step work.',
    posts: posts.filter((post) => post.seriesId === 'advanced-skill-design'),
  },
] as const;

export function getBlogPost(slug: string, assetBase = '') {
  const post = posts.find((item) => item.slug === slug);
  if (!post) return undefined;

  const markdown = readFileSync(join(contentRoot, post.file), 'utf8');
  return { ...post, html: renderMarkdown(markdown, undefined, undefined, assetBase) };
}
