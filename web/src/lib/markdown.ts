import { marked } from 'marked';
import sanitizeHtml from 'sanitize-html';

function slug(text: string): string {
  return text.toLowerCase().replace(/[^\w -]/g, '').trim().replace(/\s+/g, '-');
}
export function renderMarkdown(source: string, skillSlug?: string, docFile?: string, assetBase = ''): string {
  const html = marked.parse(source, { gfm: true, breaks: false }) as string;
  const withHeadings = html.replace(/<h([1-6])>([\s\S]*?)<\/h\1>/g, (_match, level, inside) => {
    const plain = inside.replace(/<[^>]+>/g, '');
    return `<h${level} id="${slug(plain)}">${inside}</h${level}>`;
  });
  const withLinks = withHeadings.replace(/(href|src)="(?!https?:|mailto:|#|\/)([^"]+)"/g, (_all, attr, path) => {
    const base = docFile ? `https://github.com/unraveltao/Skills/blob/main/docs/` : `https://github.com/unraveltao/Skills/blob/main/skills/${encodeURIComponent(skillSlug ?? '')}/`;
    return `${attr}="${base}${path}"`;
  });
  const withBlogAssets = withLinks.replace(/src="\/@blog-assets\//g, `src="${assetBase}/blog-assets/`);
  return sanitizeHtml(withBlogAssets, {
    allowedTags: [...sanitizeHtml.defaults.allowedTags, 'img', 'figure', 'figcaption', 'h1', 'h2', 'section'],
    allowedAttributes: {
      ...sanitizeHtml.defaults.allowedAttributes,
      a: ['href', 'title', 'target', 'rel', 'id'],
      img: ['src', 'alt', 'title', 'loading'],
      code: ['class'],
      '*': ['id']
    },
    allowedSchemes: ['http', 'https', 'mailto']
  });
}
