const skills = [
  {name:'Disk Governance', category:'File Management', description:'Audit disk usage in selected folders, review findings in a local workbench, and generate offline reports.', boundary:'Read-only auditing; no file deletion, cleanup, or migration.', keywords:'disk storage large files audit windows reports', path:'disk-governance'},
  {name:'Download Organizer', category:'File Management', description:'Inspect downloads, find files, preview filing plans, and organize files after approval.', boundary:'Applying a specific filing plan requires explicit approval; scans and previews do not move files.', keywords:'downloads organize files search plan report powershell', path:'download-organizer'},
  {name:'Git Workflow', category:'Developer Workflow', description:'Guide repository checks, branches, commits, synchronization, and recovery with risk-aware steps.', boundary:'Protect existing work and require suitable authorization for destructive or published actions.', keywords:'git branch commit version control development sync recovery', path:'git-workflow'},
  {name:'GitHub Project Coach', category:'Developer Workflow', description:'Understand a GitHub repository or Gist and learn how to use its main capability.', boundary:'Ground explanations in accessible project sources; disclose when repository access is unavailable.', keywords:'github repository gist source code project guide', path:'github-project-coach'},
  {name:'Idea Advisor', category:'Product Design', description:'Shape an early idea into a researched, compared, decision-ready product or Skill design.', boundary:'Advises on design and decisions; does not implement the product or manage delivery.', keywords:'idea product design research options prd scope requirements', path:'idea-advisor'},
  {name:'Learning Coach', category:'Learning & Understanding', description:'Plan learning paths, teach concepts interactively, guide practice, assess understanding, and organize notes.', boundary:'The learner controls progress and personal records; records stay outside the Skill package.', keywords:'learning teach course practice assessment notes progress', path:'learning-coach'},
  {name:'Unravel', category:'Learning & Understanding', description:'Explain concepts, systems, processes, and mechanisms by revealing their structure and relationships.', boundary:'For understanding requests; do not trigger for ordinary execution tasks.', keywords:'explain understand concept system process mechanism why how', path:'unravel'}
];
const PAGE_SIZE = 9;
const cards=document.querySelector('#cards');
const search=document.querySelector('#search');
const count=document.querySelector('#count');
const empty=document.querySelector('#empty');
const previousPage=document.querySelector('#previous-page');
const nextPage=document.querySelector('#next-page');
const pageStatus=document.querySelector('#page-status');
let category='All';
let currentPage=0;

function filteredSkills(){
  const query=search.value.trim().toLocaleLowerCase();
  return skills.filter(skill=>(category==='All'||skill.category===category)&&
    `${skill.name} ${skill.category} ${skill.description} ${skill.boundary} ${skill.keywords}`.toLocaleLowerCase().includes(query));
}

function render(){
  const matches=filteredSkills();
  const pageCount=Math.max(1,Math.ceil(matches.length/PAGE_SIZE));
  currentPage=Math.min(currentPage,pageCount-1);
  const start=currentPage*PAGE_SIZE;
  const visible=matches.slice(start,start+PAGE_SIZE);
  cards.replaceChildren();

  for(const skill of visible){
    const article=document.createElement('article');
    article.className='card';
    const badge=document.createElement('span');
    badge.className='card-category';
    badge.textContent=skill.category;
    const heading=document.createElement('h3');
    heading.textContent=skill.name;
    const description=document.createElement('p');
    description.textContent=skill.description;
    const boundary=document.createElement('p');
    boundary.className='boundary';
    boundary.textContent='Scope: '+skill.boundary;
    const link=document.createElement('a');
    link.href=`https://github.com/unraveltao/Skills/tree/main/skills/${skill.path}`;
    link.textContent='View Skill ↗';
    article.append(badge,heading,description,boundary,link);
    cards.append(article);
  }

  count.textContent=`${matches.length} ${matches.length===1?'Skill':'Skills'}`;
  const rangeStart=matches.length===0?0:start+1;
  const rangeEnd=Math.min(start+PAGE_SIZE,matches.length);
  pageStatus.textContent=`Showing ${rangeStart}–${rangeEnd} of ${matches.length}`;
  previousPage.disabled=currentPage===0;
  nextPage.disabled=currentPage>=pageCount-1;
  empty.hidden=matches.length!==0;
}

search.addEventListener('input',()=>{currentPage=0;render();});
document.querySelector('#filters').addEventListener('click',event=>{
  const button=event.target.closest('button[data-category]');
  if(!button)return;
  category=button.dataset.category;
  currentPage=0;
  document.querySelectorAll('.filter').forEach(item=>{
    const active=item===button;
    item.classList.toggle('active',active);
    item.setAttribute('aria-pressed',String(active));
  });
  render();
});
previousPage.addEventListener('click',()=>{currentPage=Math.max(0,currentPage-1);render();});
nextPage.addEventListener('click',()=>{
  const pageCount=Math.max(1,Math.ceil(filteredSkills().length/PAGE_SIZE));
  currentPage=Math.min(pageCount-1,currentPage+1);
  render();
});

const themeButton=document.querySelector('#theme');
const media=window.matchMedia('(prefers-color-scheme: dark)');
let saved=null;
try{saved=localStorage.getItem('unravel-theme')}catch{}
function applyTheme(mode){
  document.documentElement.dataset.theme=mode;
  themeButton.textContent=mode==='dark'?'☀':'☾';
  themeButton.setAttribute('aria-label',mode==='dark'?'Switch to light theme':'Switch to dark theme');
}
applyTheme(saved==='dark'||saved==='light'?saved:(media.matches?'dark':'light'));
themeButton.addEventListener('click',()=>{
  saved=document.documentElement.dataset.theme==='dark'?'light':'dark';
  applyTheme(saved);
  try{localStorage.setItem('unravel-theme',saved)}catch{}
});
media.addEventListener('change',event=>{if(!saved)applyTheme(event.matches?'dark':'light');});
render();
