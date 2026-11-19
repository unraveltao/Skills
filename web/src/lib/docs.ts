import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const root = fileURLToPath(new URL('../../../docs/', import.meta.url));
export interface DocPage { slug: string; title: string; file: string; }
export interface DocSection { title: string; pages: DocPage[]; }
export const sections: DocSection[] = [
  { title: 'Getting Started', pages: [
    {slug:'introduction',title:'Introduction',file:'introduction.md'},
    {slug:'getting-started/installation',title:'Installation',file:'getting-started/installation.md'},
    {slug:'getting-started/faq',title:'FAQ',file:'getting-started/faq.md'}
  ]},
  { title: 'Guides', pages: [{slug:'guides/using-skills',title:'Using Skills',file:'guides/using-skills.md'}]},
  { title: 'Concepts', pages: [{slug:'concepts/architecture',title:'Architecture',file:'concepts/architecture.md'}]},
  { title: 'Reference', pages: [
    {slug:'reference/skill-structure',title:'Skill Structure',file:'reference/skill-structure.md'},
    {slug:'reference/for-agents',title:'For Agents',file:'reference/for-agents.md'}
  ]},
  { title: 'Development', pages: [
    {slug:'development/contributing',title:'Contributing',file:'development/contributing.md'},
    {slug:'development/documentation-standards',title:'Documentation Standards',file:'development/documentation-standards.md'},
    {slug:'development/skill-readiness',title:'Skill Readiness',file:'development/skill-readiness.md'},
    {slug:'development/repo-structure-plan',title:'Repository Structure Plan',file:'development/repo-structure-plan.md'},
    {slug:'development/ai-assisted-contributions',title:'AI-Assisted Contributions',file:'development/ai-assisted-contributions.md'}
  ]}
];
export const pages: DocPage[] = sections.flatMap(section => section.pages);
export function readDoc(page:DocPage):string { return readFileSync(join(root,page.file),'utf8'); }
export function getDoc(slug:string):DocPage|undefined {return pages.find(p=>p.slug===slug);}
export function headingsFromDoc(markdown:string) {
  return Array.from(markdown.matchAll(/^## (.+)$/gm),match=>({
    title:match[1].replace(/\[(.*?)\]\(.*?\)/g,'$1').replace(/[\x60*]/g,''),
    id:match[1].toLowerCase().replace(/[^\w -]/g,'').trim().replace(/\s+/g,'-')
  }));
}
