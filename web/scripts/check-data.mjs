import { readdirSync, existsSync, readFileSync } from 'node:fs';
import { resolve, join } from 'node:path';

const root = resolve('../skills');
const dirs = readdirSync(root, {withFileTypes:true}).filter(d=>d.isDirectory());
const actual = dirs.filter(d => existsSync(join(root,d.name,'SKILL.md')));
if (!actual.length) throw Error('No Skills found under ../skills');
for (const d of actual) {
  const content = readFileSync(join(root,d.name,'SKILL.md'),'utf8');
  if (!/^---\r?\n[\s\S]+?\r?\n---/.test(content)) throw Error('Missing SKILL.md frontmatter: '+d.name);
}
console.log('PASS: '+actual.length+' Skills with SKILL.md discovered.');
console.log('READMEs present: '+actual.filter(d=>existsSync(join(root,d.name,'README.md'))).length+'/'+actual.length);
console.log('M3.1 adapter: categories/tags are provisional; manifests not yet required.');
