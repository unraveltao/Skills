import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { marked } from 'marked';
import sanitizeHtml from 'sanitize-html';

const source = [
  '# Compatibility Check',
  '',
  '**bold** and [an external link](https://example.com/)',
  '',
  '<script>alert("unsafe")</script>',
].join('\n');

const parsed = marked.parse(source, { gfm: true, breaks: false });
assert.equal(typeof parsed, 'string', 'marked.parse must remain synchronous');
assert.match(parsed, /<strong>bold<\/strong>/);
assert.match(parsed, /href="https:\/\/example\.com\/"/);

const sanitized = sanitizeHtml(parsed, {
  allowedTags: [...sanitizeHtml.defaults.allowedTags, 'img', 'h1', 'h2', 'section'],
  allowedAttributes: {
    ...sanitizeHtml.defaults.allowedAttributes,
    a: ['href', 'title', 'target', 'rel', 'id'],
    img: ['src', 'alt', 'title', 'loading'],
    code: ['class'],
    '*': ['id'],
  },
  allowedSchemes: ['http', 'https', 'mailto'],
});
assert.ok(!sanitized.includes('<script'), 'sanitizer must strip script tags');
assert.ok(!sanitized.includes('alert("unsafe")'), 'sanitizer must strip script content');
assert.match(sanitized, /<strong>bold<\/strong>/, 'sanitizer must retain legitimate Markdown');
assert.match(sanitized, /href="https:\/\/example\.com\/"/);

for (const [path, expected] of [
  ['dist/docs/index.html', 'Introduction'],
  ['dist/docs/concepts/architecture/index.html', 'Architecture'],
  ['dist/skills/idea-advisor/index.html', 'Idea Advisor'],
  ['dist/skills/disk-governance/index.html', 'Disk Governance'],
]) {
  const html = readFileSync(path, 'utf8');
  assert.ok(html.includes(expected), `Expected ${expected} in ${path}`);
  assert.ok(html.includes('/Skills/'), `Expected Pages base path in ${path}`);
}

console.log('PASS: marked rendering, sanitization, and generated Docs/Skill pages');
