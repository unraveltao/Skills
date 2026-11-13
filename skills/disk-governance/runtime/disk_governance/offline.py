"""Generate a self-contained, read-only HTML snapshot from ReportData."""
from __future__ import annotations
import html,json
from pathlib import Path

def _candidate_section(candidates:dict)->str:
    """Render the candidate table as HTML.

    This HTML is handed to the page through the JSON payload (`candidates_html`)
    instead of being spliced into the script template. Windows paths contain
    backslashes, and `C:\\Users` placed inside a JS template literal is an
    invalid `\\U` escape that aborts the entire render script, leaving a blank
    report. Routing it through JSON.parse keeps the escaping the JSON encoder's
    job.
    """
    rows=[]
    for item in candidates.get("items",[]):
        rows.append("<tr><td>"+html.escape(str(item.get("kind","")))+"<br><span class='path'>"+
            html.escape(str(item.get("path") or item.get("subject_key","")))+"</span></td><td>"+
            html.escape(str(item.get("category","")))+"</td><td>"+
            html.escape(str(item.get("risk_level","unknown")))+"</td><td>"+
            html.escape(str(item.get("confidence","")))+"</td><td>"+
            html.escape(str(item.get("review_status","untracked")))+"</td><td>"+
            html.escape(str(item.get("size_bytes",0)))+" B</td><td>"+
            html.escape(str(item.get("reason","")))+"</td></tr>")
    return ("<article><h2>待核验候选 · "+str(int(candidates.get("total",0)))+
        "</h2><p>候选不等于可删除项；相同大小不代表内容相同。</p><div class='table-wrap'><table><thead><tr>"
        "<th>类型 / 路径</th><th>分类</th><th>风险</th><th>置信度</th><th>核验状态</th><th>逻辑大小</th><th>理由</th>"
        "</tr></thead><tbody>"+("".join(rows) or "<tr><td colspan='7'>暂无候选项</td></tr>")+"</tbody></table></div>"+
        ("<p class='muted'>仅显示前 "+str(len(rows))+" 项。</p>" if candidates.get("truncated") else "")+"</article>")

def generate_offline(data:dict,out:Path)->Path:
    payload=dict(data);payload["candidates_html"]=_candidate_section(data.get("candidates") or {})
    safe=json.dumps(payload,ensure_ascii=False,separators=(",",":")).replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    body=f"""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Disk Governors 离线审计报告</title><style>
body{{font:14px/1.55 Segoe UI,system-ui,sans-serif;background:#f5f7fb;color:#172033;margin:0;padding:28px}}main{{max-width:1200px;margin:auto}}h1{{font-size:28px}}.muted{{color:#68758b}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}article{{background:white;border:1px solid #e5eaf1;border-radius:12px;padding:18px;margin:12px 0}}.num{{font-size:24px;font-weight:700}}input{{padding:9px;width:min(600px,95%);border:1px solid #ccd4e0;border-radius:7px}}table{{width:100%;border-collapse:collapse}}td,th{{text-align:left;padding:9px;border-bottom:1px solid #e5eaf1;overflow-wrap:anywhere}}.bar{{height:8px;background:#4263eb;border-radius:8px}}.path{{max-width:560px}}@media(max-width:650px){{body{{padding:12px}}}}</style><main><h1>只读磁盘审计</h1><p class="muted">批次 {html.escape(str(data['batch']['id']))} · {html.escape(str(data['batch']['status']))} · 生成时间 {html.escape(str(data['generated_at']))}</p><div id="app"></div></main><script type="application/json" id="data">{safe}</script><script>
const D=JSON.parse(document.querySelector('#data').textContent),e=s=>String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c])),f=n=>{{n=Number(n||0);if(n<1024)return n+' B';let u=['KiB','MiB','GiB','TiB'],i=-1;do{{n/=1024;i++}}while(n>=1024&&i<u.length-1);return n.toFixed(1)+' '+u[i]}},bar=(a,k,v)=>a.slice(0,10).map(x=>`<tr><td>${{e(x[k])}}</td><td><div class="bar" style="width:${{Math.max(1,Number(x[v]||0)/Math.max(1,...a.map(y=>Number(y[v]||0)))*100)}}%"></div></td><td>${{f(x[v])}}</td></tr>`).join('');document.querySelector('#app').innerHTML=`${{D.batch.status==='complete'?'':`<article>扫描不完整：${{e(D.batch.status)}}；异常 ${{D.batch.error_count}} 项。</article>`}}<div class="grid"><article>文件<div class="num">${{D.batch.file_count.toLocaleString()}}</div></article><article>目录<div class="num">${{D.batch.dir_count.toLocaleString()}}</div></article><article>文件逻辑大小<div class="num">${{f(D.batch.logical_bytes)}}</div></article><article>卷物理已用<div class="num">${{D.volume.used_bytes==null?'不可用':f(D.volume.used_bytes)}}</div><small>与扫描逻辑大小不同口径</small></article></div><article><h2>空间分类</h2><table>${{bar(D.categories,'category','bytes')}}</table></article><article><h2>文件类型</h2><table>${{bar(D.file_types,'extension','bytes')}}</table></article><article><h2>大文件</h2><label>路径过滤 <input id="q" placeholder="输入路径片段"></label><table id="files"><thead><tr><th>路径</th><th>大小</th></tr></thead><tbody>${{D.top_files.map(x=>`<tr><td class="path">${{e(x.path)}}</td><td>${{f(x.size)}}</td></tr>`).join('')}}</tbody></table><p class="muted">显示前 ${{D.top_files.length}} 项。</p></article><article><h2>大目录（逻辑大小）</h2><table>${{bar(D.top_directories,'path','total_bytes')}}</table></article><article><h2>同大小候选</h2><p>离线摘要不将相同大小认定为重复文件。候选需人工核验。</p></article><article><h2>异常记录</h2><p>${{D.errors.total}} 项；报告内展示 ${{D.errors.items.length}} 项${{D.errors.truncated?'（其余省略）':''}}。</p><table>${{D.errors.items.map(x=>`<tr><td>${{e(x.path)}}</td><td>${{e(x.message)}}</td></tr>`).join('')}}</table></article><p>该文件为只读快照，不依赖本地服务或外部网络，不提供删除、移动功能。</p>`;document.querySelector('#q').addEventListener('input',ev=>document.querySelectorAll('#files tbody tr').forEach(r=>r.hidden=!r.cells[0].textContent.toLowerCase().includes(ev.target.value.toLowerCase())));
</script></html>"""
    body=body.replace("<article><h2>同大小候选</h2><p>离线摘要不将相同大小认定为重复文件。候选需人工核验。</p></article>","<div id='cand'></div>")
    body=body.replace("</script></html>","document.querySelector('#cand').innerHTML=D.candidates_html;</script></html>")
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(body,encoding="utf-8");return out

