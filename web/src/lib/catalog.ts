import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const root = fileURLToPath(new URL('../../../skills/', import.meta.url));
export type Category = 'development' | 'learning' | 'planning' | 'utilities';
export interface Skill {
  slug: string;
  name: string;
  description: string;
  category: Category;
  tags: string[];
  readme: string | null;
  sourceUrl: string;
  readmeUrl: string | null;
}

const categories: Record<string, Category> = {
  'git-workflow': 'development',
  'github-project-coach': 'development',
  'idea-advisor': 'planning',
  'learning-coach': 'learning',
  'unravel': 'learning',
  'disk-governance': 'utilities',
  'download-organizer': 'utilities',
};
const tags: Record<string, string[]> = {
  'git-workflow': ['git', 'version-control', 'automation'],
  'github-project-coach': ['github', 'repository', 'learning'],
  'idea-advisor': ['ideas', 'requirements', 'research'],
  'learning-coach': ['teaching', 'learning', 'assessment'],
  'unravel': ['explanation', 'concepts', 'systems'],
  'disk-governance': ['filesystem', 'disk', 'audit'],
  'download-organizer': ['downloads', 'files', 'organization']
};
const friendlyNames: Record<string, string> = {
  'git-workflow': 'Git Workflow',
  'github-project-coach': 'GitHub Project Coach',
  'idea-advisor': 'Idea Advisor',
  'learning-coach': 'Learning Coach',
  'unravel': 'Unravel',
  'disk-governance': 'Disk Governance',
  'download-organizer': 'Download Organizer'
};
const field = (content: string, key: string): string | undefined => {
  const frontmatter = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  return frontmatter?.[1].match(new RegExp('^' + key + ':\\s*(.+)$', 'm'))?.[1]?.trim().replace(/^["']|["']$/g, '');
};
export const skills: Skill[] = readdirSync(root, { withFileTypes: true })
  .filter(d => d.isDirectory() && existsSync(join(root, d.name, 'SKILL.md')))
  .map(d => {
    const slug = d.name;
    const content = readFileSync(join(root, slug, 'SKILL.md'), 'utf8');
    const readmePath = join(root, slug, 'README.md');
    const hasReadme = existsSync(readmePath);
    return {
      slug,
      name: friendlyNames[slug] ?? field(content, 'name') ?? slug,
      description: field(content, 'description') ?? 'See SKILL.md for usage details.',
      category: categories[slug] ?? 'utilities',
      tags: tags[slug] ?? [],
      readme: hasReadme ? readFileSync(readmePath, 'utf8') : null,
      sourceUrl: `https://github.com/unraveltao/Skills/blob/main/skills/${encodeURIComponent(slug)}/SKILL.md`,
      readmeUrl: hasReadme ? `https://github.com/unraveltao/Skills/blob/main/skills/${encodeURIComponent(slug)}/README.md` : null
    };
  }).sort((a, b) => a.name.localeCompare(b.name));
export const categoryNames: Record<Category, string> = {
  development: 'Development', learning: 'Learning',
  planning: 'Planning', utilities: 'Utilities'
};
export const installCommand = 'npx skills add unraveltao/Skills';
