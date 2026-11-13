Warning: truncated output (original token count: 18274)
Total output lines: 1559

"use strict";

/* =========================================================================
   Disk Governors — workbench front end
   -------------------------------------------------------------------------
   The server sends `Content-Security-Policy: style-src 'self'`, which blocks
   inline `style` attributes. All bar widths and colours are therefore applied
   through the CSSOM (element.style.*) after the markup is inserted, and all
   geometry-based charts are plain SVG attributes.
   ========================================================================= */

/* ---------------------------------------------------------------- helpers */
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => (
  { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]
));
const enc = encodeURIComponent;
const num = (n) => Number(n || 0);

function fmt(n) {
  n = num(n);
  if (n < 1024) return n + " B";
  const units = ["KiB", "MiB", "GiB", "TiB", "PiB"];
  let i = -1;
  do { n /= 1024; i += 1; } while (n >= 1024 && i < units.length - 1);
  const d = n >= 100 ? 0 : n >= 10 ? 1 : 2;
  return n.toFixed(d) + " " + units[i];
}

function fmtInt(n) { return num(n).toLocaleString("zh-CN"); }

function pctText(part, whole) {
  return whole ? ((part / whole) * 100).toFixed(1) + "%" : "—";
}

function debounce(fn, ms) {
  let t;
  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
}

function midEllipsis(p, max = 66) {
  p = String(p ?? "");
  if (p.length <= max) return p;
  const headLen = Math.max(6, Math.floor(max * 0.3));
  const tailLen = max - headLen - 1;
  return p.slice(0, headLen) + "…" + p.slice(-tailLen);
}

function baseName(p) {
  const parts = String(p ?? "").split(/[\\/]/).filter(Boolean);
  return parts.length ? parts[parts.length - 1] : String(p ?? "");
}

function normPath(p) { return String(p ?? "").replace(/\//g, "\\").toLowerCase(); }

/* ---------------------------------------------------------------- time

   The API carries two different time shapes and they are NOT interchangeable:

   - `entries.mtime` is a REAL column holding Unix **seconds** (with sub-second
     precision). It is written straight from Python's `os.stat().st_mtime` in
     scripts/main.py, so it equals the file's real modification time.
   - `started` / `finished` / `created_at` are ISO-8601 strings (UTC).

   `new Date(n)` interprets a number as **milliseconds**. Feeding it a seconds
   value is what rendered 2026-11-12 as 1970-01-22 02:27. Rather than guessing a
   unit from the magnitude, each shape gets its own named formatter so the
   contract is explicit at every call site. */

const MTIME_FLOOR = 315532800;   // 1980-01-01Z, the FAT/DOS epoch
const MTIME_CEIL = 4102444800;   // 2100-01-01Z

function hhmm(d) {
  const p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())} ${p(d.getHours())}:${p(d.getMinutes())}`;
}

/** File mtime: Unix seconds (REAL, == st_mtime) → local time. */
function dtMtime(v) {
  if (v === null || v === undefined || v === "") return "未知";
  const n = Number(v);
  if (!Number.isFinite(n)) return "无效时间";
  if (n <= 0) return "未知";                       // nothing usable recorded
  if (n < MTIME_FLOOR || n > MTIME_CEIL) return "无效时间";
  const d = new Date(n * 1000);
  return Number.isNaN(d.getTime()) ? "无效时间" : hhmm(d);
}

/** Batch / review timestamps: ISO-8601 string. */
function dtIso(v) {
  if (!v) return "未知";
  const d = new Date(v);
  return Number.isNaN(d.getTime()) ? "未知" : hhmm(d);
}

/* ---------------------------------------------------------------- constants */
const PAGES = {
  overview: "磁盘概览",
  storage: "空间浏览",
  candidates: "核验候选",
  details: "文件详情",
  records: "审计记录",
};

/* ---------------------------------------------------------------- colour system

   One module decides colour; no page invents its own.

   1. Ranking bars and any same-metric comparison use ONE blue (RANK_COLOR).
      Length carries the comparison — colour must never imply a difference in
      kind between two bars that differ only in size.
   2. Space categories use a fixed hue per category (CAT_COLORS), identical in
      the donut, the legend, the treemap and the candidate category chips.
   3. Risk uses high=red / medium=orange / low=green / unknown=grey
      (RISK_COLORS). These encode rule output only: low risk is NOT permission
      to delete, and a badge is never an action affordance.
   4. The three size metrics are different quantities, so they get distinct
      colours *and* explicit labels (METRIC_COLORS). */

const RANK_COLOR = "#3b5bdb";

const CAT_COLORS = {
  "AI 模型与数据": "#7048e8",  // 紫
  "其他 / 未知": "#868e96",    // 中性灰
  "下载与归档": "#0c8599",     // 青
  "媒体与创作": "#e8590c",     // 橙
  "缓存与构建": "#c08a00",     // 金黄
  "软件与系统": "#4c6ef5",     // 蓝
  "个人文档": "#2f9e44",       // 绿
  "开发项目": "#0ca678",       // 青绿
};
const CAT_FALLBACK = "#868e96";
const catColor = (name) => CAT_COLORS[name] || CAT_FALLBACK;

const RISK_COLORS = {
  high: "#c92a2a",
  medium: "#d9730d",
  low: "#1f8a5f",
  unknown: "#5b6474",
};

const METRIC_COLORS = {
  volume: "#64748b",      // 卷物理已用
  scanned: "#3b5bdb",     // 扫描逻辑大小
  candidates: "#b08900",  // 候选逻辑大小
};

/* Inner treemap cells: tints of the ranking blue, so nested detail reads as
   subordinate to its parent rather than as a different category. */
const NEST_COLORS = ["#c3cdf4", "#cfd7f7", "#dbe1f9", "#e4e9fb", "#b8c4f1", "#aab8ef"];

/* Candidate kinds are NOT risk levels. These hues deliberately stay outside the
   risk palette so a kind chip can never be read as a risk signal. */
const KIND_LABEL = {
  large_file: "大文件",
  cache_or_build_directory: "缓存 / 构建目录",
  same_size_group: "同大小文件组",
};
const KIND_COLOR = {
  large_file: "#3b5bdb",
  cache_or_build_directory: "#b08900",
  same_size_group: "#0c8599",
};

const RISK_LABEL = { high: "高", medium: "中", low: "低", unknown: "未知" };
const RISK_HINT = {
  high: "规则给出高等级提示，仍需人工确认后才能采取任何操作",
  medium: "规则给出中等级提示，使用场景需人工确认",
  low: "规则给出低等级提示；低风险不代表允许删除",
  unknown: "规则无法给出可靠等级，需人工判断",
};
const CONFIDENCE_HINT = {
  "高": "分类规则有较强依据",
  "中": "分类规则有部分依据",
  "低": "分类规则依据不足，仅作线索",
};

/* `review_status` is a single enum but it answers two different questions.
   The UI shows two columns so "已查看" is never mistaken for "决定保留". */
const REVIEW_LABEL = { untracked: "未核验", pending: "待核验", verified: "已查看" };
const DECISION_LABEL = { keep: "保留", deferred: "暂缓", needs_assessment: "待评估" };
function reviewAxes(s) {
  const v = s || "untracked";
  if (REVIEW_LABEL[v]) return { review: v, decision: "" };
  return { review: "verified", decision: DECISION_LABEL[v] ? v : "" };
}
const STATUS_LABEL = { ...REVIEW_LABEL, ...DECISION_LABEL };

/* ---------------------------------------------------------------- state */
const state = {
  token: "",
  instance: "",
  batches: [],
  batch: "",
  overview: null,
  page: "overview",
  scroll: {},
  files: { q: "", sort: "size", order: "desc", page: 1, size: 50, total: 0 },
  dir: "",
  cand: { q: "", risk: "", category: "", status: "", page: 1, size: 25, all: null, total: 0 },
  rec: { type: "" },
  file: null,
  flashFiles: false,
};

/* ---------------------------------------------------------------- api */
async function api(path, method = "GET", body) {
  const res = await fetch(path, {
    method,
    headers: {
      "X-Disk-Governors-Token": state.token,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  let data = null;
  try { data = await res.json(); } catch { data = null; }
  if (!res.ok) throw new Error((data && data.error) || `HTTP ${res.status}`);
  return data;
}

/* ---------------------------------------------------------------- chart primitives */

/**
 * Horizontal bars on one shared scale.
 * Widths are applied via CSSOM because inline styles are blocked by CSP.
 */
function barRows(items, opts = {}) {
  const max = opts.max || Math.max(1, ...items.map((i) => num(i.value)));
  const total = opts.total || items.reduce((s, i) => s + num(i.value), 0);
  const showShare = opts.share !== false;
  return `<div class="bars">${items.map((it) => {
    const frac = Math.max(0.004, Math.min(1, num(it.value) / max));
    return `<div class="bar-item">
      <div class="bar-name" title="${esc(it.label)}">${esc(it.label)}${it.sub ? `<small>${esc(it.sub)}</small>` : ""}</div>
      <div class="bar-track"><div class="bar-fill" data-frac="${frac.toFixed(5)}"></div></div>
      <div class="bar-val">${fmt(it.value)}${showShare && total ? `<small>${pctText(it.value, total)}</small>` : ""}</div>
    </div>`;
  }).join("")}</div>`;
}

function paintBars(root) {
  $$("[data-frac]", root).forEach((el) => {
    el.style.width = (Number(el.dataset.frac) * 100).toFixed(3) + "%";
    el.style.backgroundColor = el.dataset.color || RANK_COLOR;
  });
}

function donutSvg(items, size = 168, thickness = 26) {
  const total = items.reduce((s, i) => s + num(i.value), 0) || 1;
  const r = (size - thickness) / 2;
  const cx = size / 2;
  const cy = size / 2;
  let a0 = -Math.PI / 2;
  const arcs = items.map((it) => {
    const frac = num(it.value) / total;
    const a1 = a0 + frac * Math.PI * 2;
    let d;
    if (frac >= 0.9999) {
      d = `M ${cx} ${cy - r} A ${r} ${r} 0 1 1 ${cx - 0.01} ${cy - r}`;
    } else {
      const x1 = cx + r * Math.cos(a0), y1 = cy + r * Math.sin(a0);
      const x2 = cx + r * Math.cos(a1), y2 = cy + r * Math.sin(a1);
      d = `M ${x1.toFixed(2)} ${y1.toFixed(2)} A ${r} ${r} 0 ${a1 - a0 > Math.PI ? 1 : 0} 1 ${x2.toFixed(2)} ${y2.toFixed(2)}`;
    }
    a0 = a1;
    return `<path d="${d}" fill="none" stroke="${it.color}" stroke-width="${thickness}"><title>${esc(it.label)} · ${fmt(it.value)} · ${pctText(it.value, total)}</title></path>`;
  }).join("");
  return `<svg class="donut-svg" viewBox="0 0 ${size} ${size}" role="img" aria-label="空间分类占比">
    ${arcs}
    <text class="donut-center-value" x="${cx}" y="${cy - 1}" text-anchor="middle">${fmt(total)}</text>
    <text class="donut-center-label" x="${cx}" y="${cy + 15}" text-anchor="middle">已扫描逻辑大小</text>
  </svg>`;
}

/* squarified treemap */
function worstRatio(row, sum, side) {
  const t = sum / side;
  let mn = Infinity, mx = 0;
  for (const r of row) { if (r.a < mn) mn = r.a; if (r.a > mx) mx = r.a; }
  if (!isFinite(mn) || mn <= 0) return Infinity;
  return Math.max((t * t) / mn, mx / (t * t));
}

function squarify(items, x, y, w, h) {
  const out = [];
  const total = items.reduce((s, i) => s + num(i.value), 0);
  if (!total || w <= 0 || h <= 0) return out;
  const area = w * h;
  let rest = items.filter((i) => num(i.value) > 0).map((i) => ({ ...i, a: (num(i.value) / total) * area }));
  let rx = x, ry = y, rw = w, rh = h;
  while (rest.length && rw > 0.5 && rh > 0.5) {
    const short = Math.min(rw, rh);
    let row = [rest[0]];
    let sum = rest[0].a;
    let best = worstRatio(row, sum, short);
    let k = 1;
    while (k < rest.length) {
      const cand = row.concat([rest[k]]);
      const s2 = sum + rest[k].a;
      const ratio = worstRatio(cand, s2, short);
      if (ratio <= best) { row = cand; sum = s2; best = ratio; k += 1; } else break;
    }
    rest = rest.slice(k);
    if (rw >= rh) {
      const t = sum / rh;
      let cy = ry;
      for (const it of row) {
        const ih = it.a / t;
        out.push({ ...it, x: rx, y: cy, w: t, h: Math.max(0, Math.min(ih, ry + rh - cy)) });
        cy += ih;
      }
      rx += t; rw -= t;
    } else {
      const t = sum / rw;
      let cx = rx;
      for (const it of row) {
        const iw = it.a / t;
        out.push({ ...it, x: cx, y: ry, w: Math.max(0, Math.min(iw, rx + rw - cx)), h: t });
        cx += iw;
      }
      ry += t; rh -= t;
    }
  }
  return out;
}

/* ---------------------------------------------------------------- tooltip
   One shared node, positioned through CSSOM. CSP forbids inline style
   attributes in markup, so the node is created once and moved with
   `el.style.left/top`. */
let tipEl = null;
function tipNode() {
  if (!tipEl) {
    tipEl = document.createElement("div");
    tipEl.className = "tip";
    tipEl.setAttribute("role", "tooltip");
    document.body.appendChild(tipEl);
  }
  return tipEl;
}
function showTip(text, x, y) {
  if (!text) return;
  const t = tipNode();
  t.textContent = text;
  t.classList.add("on");
  const pad = 12;
  const w = t.offsetWidth;
  const h = t.offsetHeight;
  let left = x + 14;
  let top = y + 16;
  if (left + w > window.innerWidth - pad) left = Math.max(pad, x - w - 14);
  if (top + h > window.innerHeight - pad) top = Math.max(pad, y - h - 12);
  t.style.left = left + "px";
  t.style.top = top + "px";
}
function hideTip() { if (tipEl) tipEl.classList.remove("on"); }

/** Tooltip body for a treemap cell: full path, size, file count. */
function tmTip(label, value, count) {
  const n = count === undefined || count === null ? "" : ` · ${fmtInt(count)} 个文件`;
  return `${label}\n${fmt(value)}${n}`;
}

/** Bind hover + click + keyboard on treemap cells. */
function bindTreemapCells(host, onEnter) {
  $$(".tm-cell", host).forEach((g) => {
    const text = g.dataset.tip || "";
    g.addEventListener("mouseenter", (e) => showTip(text, e.clientX, e.clientY));
    g.addEventListener("mousemove", (e) => showTip(text, e.clientX, e.clientY));
    g.addEventListener("mouseleave", hideTip);
    g.addEventListener("focus", () => {
      const r = g.getBoundingClientRect();
      showTip(text, r.left + r.width / 2, r.bottom);
    });
    g.addEventListener("blur", hideTip);
    g.addEventListener("click", () => { hideTip(); onEnter(g.dataset.tm); });
    g.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); hideTip(); onEnter(g.dataset.tm); }
    });
  });
}

/**
 * `nested` maps a cell path to its children. When one child swallows a level,
 * drawing its children inside its own rectangle is the only honest way to make
 * the chart readable: a single 99% cell with three invisible slivers tells the
 * user nothing. Top-level cells stay siblings (areas directly comparable); the
 * inner cells are visibly subordinate and carry their own drill target.
 */
function treemapMarkup(items, width, height, nested) {
  const cells = squarify(items, 0, 0, width, height);
  const base = [];
  const over = [];
  cells.forEach((c) => {
    const nk = nested && nested.get(c.path);
    const kids = nk ? nk.items : null;
    const big = c.w > 64 && c.h > 40;
    const mid = c.w > 40 && c.h > 24;
    const label = big || mid ? baseName(c.label) : "";
    const strip = kids ? 22 : 0;
    const head = kids
      ? `<text class="tm-name" x="${(c.x + 7).toFixed(1)}" y="${(c.y + 15).toFixed(1)}">${esc(midEllipsis(nk.label, Math.max(6, Math.floor(c.w / 8))))}</text>
         <text class="tm-size" x="${(c.x + c.w - 7).toFixed(1)}" y="${(c.y + 15).toFixed(1)}" text-anchor="end">${fmt(c.value)}</text>`
      : `${big ? `<text class="tm-name" x="${(c.x + 7).toFixed(1)}" y="${(c.y + 17).toFixed(1)}">${esc(midEllipsis(label, Math.max(6, Math.floor(c.w / 7))))}</text>` : ""}
         ${big ? `<text class="tm-size" x="${(c.x + 7).toFixed(1)}" y="${(c.y + 31).toFixed(1)}">${fmt(c.value)}</text>` : ""}`;
    base.push(`<g class="tm-cell" data-tm="${esc(c.path || c.label)}" data-tip="${esc(tmTip(c.label, c.value, c.count))}" role="button" tabindex="0" aria-label="${esc(c.label)} ${fmt(c.value)}">
      <rect x="${c.x.toFixed(1)}" y="${c.y.toFixed(1)}" width="${Math.max(0, c.w).toFixed(1)}" height="${Math.max(0, c.h).toFixed(1)}" rx="3" fill="${c.color || RANK_COLOR}"></rect>
      ${head}
    </g>`);
    if (kids && c.w > 150 && c.h > 96) {
      const inner = squarify(kids, c.x + 5, c.y + strip, Math.max(0, c.w - 10), Math.max(0, c.h - strip - 5));
      const kbody = inner.map((k, i) => {
        const kb = k.w > 58 && k.h > 32;
        return `<g class="tm-cell tm-nested" data-tm="${esc(k.path || k.label)}" data-tip="${esc(tmTip(k.label, k.value, k.count))}" role="button" tabindex="0" aria-label="${esc(k.label)} ${fmt(k.value)}">
          <rect x="${k.x.toFixed(1)}" y="${k.y.toFixed(1)}" width="${Math.max(0, k.w).toFixed(1)}" height="${Math.max(0, k.h).toFixed(1)}" rx="2" fill="${NEST_COLORS[i % NEST_COLORS.length]}" stroke="#ffffff" stroke-width="1"></rect>
          ${kb ? `<text class="tm-name tm-name-in" x="${(k.x + 5).toFixed(1)}" y="${(k.y + 14).toFixed(1)}">${esc(midEllipsis(baseName(k.label), Math.max(4, Math.floor(k.w / 6))))}</text>` : ""}
          ${kb ? `<text class="tm-size tm-size-in" x="${(k.x + 5).toFixed(1)}" y="${(k.y + 26).toFixed(1)}">${fmt(k.value)}</text>` : ""}
        </g>`;
      }).join("");
      over.push(`<g class="tm-nest">${kbody}</g>`);
    }
  });
  return `<svg class="treemap" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" role="img" aria-label="目录占用面积图">${base.join("")}${over.join("")}</svg>`;
}

/* ---------------------------------------------------------------- data shaping */

/**
 * Pick a directory level worth drawing: start at the scan root and drill into
 * the dominant child while one entry swallows the level. Every drawn cell is a
 * sibling, so the areas are directly comparable.
 */
async function buildTreemapLevel(root, maxDrill = 3) {
  let base = root;
  let level = 0;
  let items = [];
  try {
    items = await api(`/api/v1/directories?batch_id=${enc(state.batch)}&parent=${enc(base)}`);
  } catch { items = []; }
  for (let i = 0; i < maxDrill; i += 1) {
    const total = items.reduce((s, d) => s + num(d.total_bytes), 0);
    const max = items.reduce((m, d) => Math.max(m, num(d.total_bytes)), 0);
    if (!items.length || items.length >= 6 || !total || max / total < 0.6) break;
    const big = items.find((d) => num(d.total_bytes) === max);
    if (!big) break;
    let kids = [];
    try {
      kids = await api(`/api/v1/directories?batch_id=${enc(state.batch)}&parent=${enc(big.path)}`);
    } catch { kids = []; }
    if (!kids.length) break;
    base = big.path;
    level += 1;
    items = kids;
  }
  return { items, base, level };
}

/** Candidate aggregate without double counting nested paths. */
function candidateAggregate(items) {
  const pathItems = items.filter((c) => c.path && c.kind !== "same_size_group");
  const keys = new Set(pathItems.map((c) => normPath(c.path)));
  const kept = [];
  for (const c of pathItems) {
    const k = normPath(c.path);
    let nested = false;
    for (const other of keys) {
      if (other !== k && k.startsWith(other + "\\")) { nested = true; break; }
    }
    if (!nested) kept.push(c);
  }
  const total = kept.reduce((s, c) => s + num(c.size_bytes), 0);
  const sameSize = items
    .filter((c) => c.kind === "same_size_group")
    .reduce((s, c) => s + num(c.size_bytes), 0);
  return { total, count: kept.length, sameSize };
}

/* ---------------------------------------------------------------- shell */
const content = $("#content");
const titleEl = $("#title");
const batchSel = $("#batches");

function setBusy(on) {
  content.setAttribute("aria-busy", on ? "true" : "false");
}

function renderBatchOptions() {
  batchSel.innerHTML = state.batches.map((b) =>
    `<option value="${esc(b.id)}">${esc(b.target)} · ${esc(dtIso(b.starte…8274 tokens truncated…history="${esc(x.candidate_id)}">查看事件历史</button>
      <button class="btn ghost" type="button" data-inspect="${esc(x.path || "")}">在文件详情中查看</button>
    </div>
    <div class="history" id="history-${esc(x.candidate_id)}"></div>`;
}

function bindCandidateRows() {
  $$("[data-expand]").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const id = btn.dataset.expand;
      const box = document.getElementById("detail-" + id);
      if (!box) return;
      if (!box.hidden) { box.hidden = true; btn.textContent = "详情"; return; }
      if (!box.dataset.ready) {
        const all = state.cand.all || [];
        const item = all.find((x) => x.candidate_id === id);
        if (!item) return;
        box.innerHTML = candDetailMarkup(item);
        box.dataset.ready = "1";
        bindCandidateDetail(box);
      }
      box.hidden = false;
      btn.textContent = "收起";
    });
  });
}

function bindCandidateDetail(box) {
  const save = $("[data-save]", box);
  if (save) {
    save.addEventListener("click", async () => {
      const id = save.dataset.save;
      const sel = $(`[data-status="${CSS.escape(id)}"]`, box);
      const note = $(`[data-note="${CSS.escape(id)}"]`, box);
      save.disabled = true;
      try {
        await api("/api/v1/reviews", "POST", {
          candidate_id: id,
          status: sel.value,
          note: note.value,
          expected_version: Number(save.dataset.version),
          request_id: crypto.randomUUID(),
        });
        state.cand.all = null;
        await renderCandidates();
      } catch (e) {
        save.disabled = false;
        alert(`未记录：${e.message}\n可能有其他窗口已更新，请刷新后重试。`);
      }
    });
  }
  const hist = $("[data-history]", box);
  if (hist) {
    hist.addEventListener("click", async () => {
      const id = hist.dataset.history;
      const out = document.getElementById("history-" + id);
      if (!out) return;
      try {
        const events = await api(`/api/v1/history?batch_id=${enc(state.batch)}&candidate_id=${enc(id)}`);
        out.innerHTML = events.length
          ? events.map((x) => `<p><span class="faint">${esc(dtIso(x.created_at))}</span> · ${esc(STATUS_LABEL[x.from_status] || x.from_status || "新建")} → <b>${esc(STATUS_LABEL[x.to_status] || x.to_status)}</b> · v${num(x.version)}${x.note ? ` · ${esc(x.note)}` : ""}</p>`).join("")
          : `<p class="muted">暂无事件</p>`;
      } catch (e) {
        out.innerHTML = `<p class="error">${esc(e.message)}</p>`;
      }
    });
  }
  const inspect = $("[data-inspect]", box);
  if (inspect) {
    inspect.addEventListener("click", () => {
      if (!inspect.dataset.inspect) return;
      state.file = inspect.dataset.inspect;
      go("details");
    });
  }
}

/* ---------------------------------------------------------------- details */
async function renderDetails() {
  if (!state.file) {
    content.innerHTML = `<div class="page"><article class="card">
      <div class="empty-state">
        <b>尚未选择文件</b>
        <span>在「空间浏览」的文件列表里点击任意一行的「详情」，或在「核验候选」中打开某个候选。</span>
        <button class="btn" type="button" id="to-storage">前往空间浏览</button>
      </div>
    </article></div>`;
    $("#to-storage").addEventListener("click", () => go("storage"));
    return;
  }

  let f = null;
  let related = [];
  try {
    f = await api(`/api/v1/file?batch_id=${enc(state.batch)}&path=${enc(state.file)}`);
  } catch (e) {
    content.innerHTML = `<div class="card error">${esc(e.message)}</div>`;
    return;
  }
  if (!f) {
    content.innerHTML = `<div class="page"><article class="card">
      <div class="empty-state"><b>未找到该文件</b><span>它可能属于其它扫描批次，或已在磁盘上被移动。</span>
      <button class="btn" type="button" id="to-storage">返回空间浏览</button></div></article></div>`;
    $("#to-storage").addEventListener("click", () => go("storage"));
    return;
  }

  try {
    const d = await api(`/api/v1/candidates?batch_id=${enc(state.batch)}&q=${enc(f.path)}&page_size=10`);
    related = (d.items || []).filter((x) => x.path && normPath(x.path) === normPath(f.path));
  } catch { related = []; }

  /* Review events for this exact path, so the page shows its own audit trail
     rather than the whole batch timeline. */
  let events = [];
  try {
    const h = await api(`/api/v1/reviews/history?batch_id=${enc(state.batch)}&limit=200&offset=0`);
    events = (h.items || []).filter((e) => e.path && normPath(e.path) === normPath(f.path));
  } catch { events = []; }

  const o = state.overview;
  const scanned = o ? num(o.batch.logical_bytes) : 0;
  const primary = related[0] || null;
  const ax = reviewAxes(primary ? primary.review_status : "untracked");
  const risks = Array.from(new Set(related.map((x) => x.risk_level)));
  const confs = Array.from(new Set(related.map((x) => x.confidence)));

  const catCell = primary
    ? `<span class="chip soft"><svg width="8" height="8" aria-hidden="true"><rect width="8" height="8" rx="2" fill="${catColor(primary.category)}"></rect></svg>${esc(primary.category)}</span>`
    : `<span class="faint">未分类（未命中候选规则）</span>`;
  const ruleCell = related.length
    ? `${related.map((x) => `<span class="mono">${esc((x.evidence || {}).rule_id || "—")}</span>`).join("、")} <span class="faint">· ${esc(primary.rule_version || "")}</span>`
    : `<span class="faint">—</span>`;
  const riskCell = risks.length
    ? `${risks.map((r) => candRiskChip(r)).join(" ")} <span class="audit-note">${esc(RISK_HINT[risks[0]] || "")}</span>`
    : `<span class="faint">—</span>`;
  const confCell = confs.length
    ? `<b>${esc(confs.join(" / "))}</b> <span class="audit-note">${esc(CONFIDENCE_HINT[confs[0]] || "")}</span>`
    : `<span class="faint">—</span>`;
  const conclusion = primary
    ? `该文件命中 ${related.length} 条候选规则（${related.map((x) => KIND_LABEL[x.kind] || x.kind).join("、")}）。规则给出的风险等级为 ${risks.map((r) => RISK_LABEL[r]).join(" / ")}，规则置信度 ${confs.join(" / ")}。以上均为元数据判断，文件内容未核验。`
    : `该文件未命中任何候选规则。工作台只记录它的元数据，不对其用途或可释放性作任何判断。`;

  content.innerHTML = `<div class="page">
    <article class="card">
      <div class="card-head"><h2>审计结论</h2><span class="sub">规则输出 + 人工记录</span></div>
      <div class="conclusion">
        <h3>${primary ? "为什么这个文件被关注" : "这个文件未被规则关注"}</h3>
        <p>${esc(conclusion)}</p>
        ${primary ? `<div class="todo">还需要核实：<ul>${unverifiedText(primary).map((u) => `<li>${esc(u)}</li>`).join("")}</ul></div>`
                  : `<div class="todo">没有候选记录，也就没有需要跟进的核验项。</div>`}
      </div>
      <dl class="audit">
        <dt>所属分类</dt><dd>${catCell}</dd>
        <dt>命中规则</dt><dd>${ruleCell}</dd>
        <dt>风险等级</dt><dd>${riskCell}</dd>
        <dt>规则置信度</dt><dd>${confCell}</dd>
        <dt>人工核验</dt><dd>${primary ? `${esc(REVIEW_LABEL[ax.review] || ax.review)} <span class="faint">· v${num(primary.review_version)}</span>` : `<span class="faint">未核验</span>`}</dd>
        <dt>人工决策</dt><dd>${ax.decision ? esc(DECISION_LABEL[ax.decision]) : `<span class="faint">尚未作出决策</span>`}</dd>
        <dt>关联记录</dt><dd>${events.length ? `${fmtInt(events.length)} 条核验事件` : `<span class="faint">暂无</span>`}</dd>
      </dl>
      <p class="hint tight">风险等级与置信度都是规则输出，不是删除许可；本页不提供删除或迁移操作。</p>
    </article>

    <div class="grid split-a">
      <article class="card">
        <div class="card-head"><h2>文件元数据</h2><span class="sub">只读</span><span class="spacer"></span>
          <button class="btn sm" type="button" id="copy-path">复制路径</button>
        </div>
        <dl class="dl">
          <dt>文件名</dt><dd><b>${esc(baseName(f.path))}</b></dd>
          <dt>完整路径</dt><dd class="mono">${esc(f.path)}</dd>
          <dt>所在目录</dt><dd class="mono">${esc(f.parent_path || "—")}</dd>
          <dt>大小</dt><dd data-metric="file_size" data-value="${f.size}">${fmt(f.size)} <span class="faint">（${fmtInt(f.size)} 字节）</span></dd>
          <dt>类型</dt><dd><span class="chip soft">${esc(f.extension || "—")}</span></dd>
          <dt>最后修改</dt><dd>${esc(dtMtime(f.mtime))}</dd>
          <dt>批次</dt><dd class="mono">${esc(f.batch_id)}</dd>
          <dt>内容摘要</dt><dd class="mono faint">${esc(f.digest || "未计算（v0.2 默认不读取文件内容）")}</dd>
        </dl>
        <p class="hint tight">占扫描逻辑大小 ${pctText(num(f.size), scanned)}。文件大小是逻辑大小，不等于磁盘分配。</p>
      </article>

      <article class="card">
        <div class="card-head"><h2>相关候选</h2><span class="sub">${related.length} 项</span></div>
        ${related.length ? `<div class="cand-list">${related.map((x) => {
          const r = reviewAxes(x.review_status);
          return `<div class="cand"><div class="cand-row compact">
          <div class="cand-main">
            <div class="cand-kind">
              ${esc(KIND_LABEL[x.kind] || x.kind)} ${candRiskChip(x.risk_level)}
              <span class="chip soft">置信度 ${esc(x.confidence)}</span>
              <span class="chip soft">${esc(REVIEW_LABEL[r.review] || r.review)}</span>
              ${r.decision ? `<span class="chip accent">${esc(DECISION_LABEL[r.decision])}</span>` : ""}
            </div>
            <div class="cand-path path" title="${esc(x.reason)}">${esc(x.reason)}</div>
          </div>
          <div class="cand-size">${fmt(x.size_bytes)}</div>
          <div class="act"><button class="btn sm" type="button" data-to-cand="1">去核验</button></div>
        </div></div>`;
        }).join("")}</div>`
        : `<div class="empty-state"><b>没有关联候选</b><span>该文件未命中大文件、缓存目录或同大小规则。</span></div>`}
        <p class="hint tight">候选按路径精确匹配；同一文件的候选结论需人工核验。</p>
      </article>
    </div>

    <article class="card">
      <div class="card-head"><h2>关联审计记录</h2><span class="sub">${fmtInt(events.length)} 条</span></div>
      ${events.length ? `<div class="timeline">${events.map((x) => `<div class="tl-item">
        <div class="tl-time">${esc(dtIso(x.created_at))}</div>
        <div class="tl-body">
          <div class="tl-transition">${esc(STATUS_LABEL[x.from_status] || x.from_status || "新建")} → ${esc(STATUS_LABEL[x.to_status] || x.to_status)} <span class="faint">· v${num(x.version)}</span></div>
          ${x.note ? `<div class="tl-note">${esc(x.note)}</div>` : ""}
        </div>
      </div>`).join("")}</div>`
      : `<div class="empty-state"><b>该文件还没有核验记录</b><span>在「核验候选」中保存状态后，这里会显示对应事件。</span></div>`}
    </article>
  </div>`;

  $("#copy-path").addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(f.path);
      $("#copy-path").textContent = "已复制";
      setTimeout(() => { const b = $("#copy-path"); if (b) b.textContent = "复制路径"; }, 1600);
    } catch {
      $("#copy-path").textContent = "复制失败";
    }
  });
  $$("[data-to-cand]", content).forEach((b) => b.addEventListener("click", () => go("candidates")));
}

/* ---------------------------------------------------------------- records */
async function renderRecords() {
  const o = state.overview;
  if (!o) { content.innerHTML = `<div class="card empty">尚无扫描批次。</div>`; return; }
  const b = o.batch;
  const errors = o.errors || { total: 0, items: [] };
  let events = { total: 0, items: [] };
  try {
    events = await api(`/api/v1/reviews/history?batch_id=${enc(state.batch)}&limit=200&offset=0`);
  } catch { /* keep empty */ }

  const all = events.items || [];
  const type = state.rec.type;
  const shown = type ? all.filter((x) => x.to_status === type) : all;
  const types = Array.from(new Set(all.map((x) => x.to_status))).filter(Boolean);

  const complete = b.status === "complete";
  const integrity = !complete ? "未完成" : (num(b.error_count) > 0 ? "完整，但有异常项" : "完整");
  const span = (() => {
    if (!b.started || !b.finished) return "—";
    const ms = new Date(b.finished) - new Date(b.started);
    if (!Number.isFinite(ms) || ms < 0) return "—";
    const s = Math.round(ms / 1000);
    return s < 60 ? `${s} 秒` : `${Math.floor(s / 60)} 分 ${s % 60} 秒`;
  })();

  content.innerHTML = `<div class="page">
    ${!complete || num(b.error_count) > 0
      ? `<div class="alert"><b>批次不完整。</b>状态 ${esc(b.status)}，异常 ${fmtInt(b.error_count)} 项。以下统计只覆盖成功读取的范围。</div>` : ""}

    <div class="grid cols-3">
      <article class="card">
        <div class="card-head"><h2>批次</h2></div>
        <dl class="dl">
          <dt>状态</dt><dd><span class="chip ${complete ? "low" : "medium"}">${esc(b.status)}</span></dd>
          <dt>目标</dt><dd class="mono">${esc(b.target)}</dd>
          <dt>开始</dt><dd>${esc(dtIso(b.started))}</dd>
          <dt>结束</dt><dd>${esc(dtIso(b.finished))}</dd>
          <dt>耗时</dt><dd>${esc(span)}</dd>
        </dl>
      </article>
      <article class="card">
        <div class="card-head"><h2>完整性</h2></div>
        <dl class="dl">
          <dt>结论</dt><dd><b>${esc(integrity)}</b></dd>
          <dt>文件</dt><dd>${fmtInt(b.file_count)}</dd>
          <dt>目录</dt><dd>${fmtInt(b.dir_count)}</dd>
          <dt>逻辑大小</dt><dd>${fmt(b.logical_bytes)}</dd>
          <dt>异常</dt><dd>${num(b.error_count) ? `<span class="chip medium">${fmtInt(b.error_count)}</span>` : `<span class="chip low">0</span>`}</dd>
        </dl>
      </article>
      <article class="card">
        <div class="card-head"><h2>口径说明</h2></div>
        <p class="hint">卷物理已用空间来自卷总量减可用量，包含 NTFS 元数据、不可读目录与系统独占文件；扫描逻辑大小只累加成功读取的文件。两者不相等是正常的，工作台不会用估算值填补差额。</p>
        <p class="hint tight">候选只是元数据线索，不代表可删除；核验记录只是审计动作，不构成删除授权。</p>
      </article>
    </div>

    <article class="card">
      <div class="card-head">
        <h2>核验事件</h2>
        <span class="sub">${fmtInt(shown.length)} / ${fmtInt(all.length)} 条</span>
        <span class="spacer"></span>
        <select id="rec-type" aria-label="按事件类型筛选">
          <option value="">全部事件</option>
          ${types.map((t) => `<option value="${esc(t)}" ${type === t ? "selected" : ""}>${esc(STATUS_LABEL[t] || t)}</option>`).join("")}
        </select>
      </div>
      ${shown.length ? `<div class="timeline">${shown.map((x) => `<div class="tl-item">
        <div class="tl-time">${esc(dtIso(x.created_at))}</div>
        <div class="tl-body">
          <div class="tl-transition">${esc(STATUS_LABEL[x.from_status] || x.from_status || "新建")} → ${esc(STATUS_LABEL[x.to_status] || x.to_status)} <span class="faint">· v${num(x.version)}</span></div>
          <div class="path" title="${esc(x.path || x.subject_key || "")}">${esc(midEllipsis(x.path || x.subject_key || "", 96))}</div>
          ${x.note ? `<div class="tl-note">${esc(x.note)}</div>` : ""}
        </div>
      </div>`).join("")}</div>`
      : all.length
        ? `<div class="empty-inline">没有「${esc(STATUS_LABEL[type] || type)}」类型的事件，换一个筛选条件试试。</div>`
        : `<div class="empty-state"><b>还没有核验记录</b><span>在「核验候选」中保存状态后会出现在这里。</span></div>`}
    </article>

    <article class="card">
      <div class="card-head"><h2>扫描异常</h2><span class="sub">${fmtInt(errors.total)} 项${errors.truncated ? " · 仅显示前 500 条" : ""}</span></div>
      ${(errors.items || []).length ? `<div class="table-wrap"><table class="data">
        <thead><tr><th>路径</th><th>信息</th></tr></thead>
        <tbody>${errors.items.map((e) => `<tr>
          <td class="path-wrap"><span class="path" title="${esc(e.path)}">${esc(midEllipsis(e.path, 88))}</span></td>
          <td class="muted">${esc(e.message)}</td>
        </tr>`).join("")}</tbody>
      </table></div>` : `<div class="empty-inline">本次扫描没有异常记录，所有遍历到的目录都成功读取了元数据。</div>`}
    </article>
  </div>`;

  const sel = $("#rec-type");
  if (sel) sel.addEventListener("change", (e) => { state.rec.type = e.target.value; renderRecords(); });
}

/* ---------------------------------------------------------------- boot */
async function boot() {
  try {
    const s = await fetch("/session").then((r) => r.json());
    state.token = s.token;
    state.instance = s.instance;
  } catch (e) {
    content.innerHTML = `<div class="card error">无法连接本机服务：${esc(e.message)}</div>`;
    return;
  }

  try {
    state.batches = await api("/api/v1/batches");
  } catch (e) {
    content.innerHTML = `<div class="card error">读取批次失败：${esc(e.message)}</div>`;
    return;
  }

  renderBatchOptions();

  if (!state.batches.length) {
    content.innerHTML = `<div class="card empty">尚无扫描批次。先用 CLI 对隔离测试目录运行 <code>scan</code>。</div>`;
    return;
  }

  state.batch = state.batches[0].id;
  batchSel.value = state.batch;

  await reloadBatch();

  batchSel.addEventListener("change", async () => {
    state.batch = batchSel.value;
    state.dir = "";
    state.file = null;
    state.cand.all = null;
    state.cand.page = 1;
    state.files.page = 1;
    state.scroll = {};
    await reloadBatch();
    await go(state.page, { keepScroll: true });
  });

  $$("#nav button").forEach((b) => b.addEventListener("click", () => go(b.dataset.page)));

  const collapse = $("#navCollapse");
  const KEY = "dg.nav.collapsed";
  if (localStorage.getItem(KEY) === "1") document.body.classList.add("nav-collapsed");
  collapse.setAttribute("aria-expanded", document.body.classList.contains("nav-collapsed") ? "false" : "true");
  collapse.addEventListener("click", () => {
    const on = document.body.classList.toggle("nav-collapsed");
    localStorage.setItem(KEY, on ? "1" : "0");
    collapse.setAttribute("aria-expanded", on ? "false" : "true");
  });

  $("#drawerBtn").addEventListener("click", () => {
    if (document.body.classList.contains("drawer-open")) closeDrawer(); else openDrawer();
  });
  $("#scrim").addEventListener("click", closeDrawer);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeDrawer(); });

  window.addEventListener("resize", debounce(() => {
    if (state.page === "overview" || state.page === "storage") {
      render(state.page, { keepScroll: true });
    }
  }, 220));

  window.addEventListener("hashchange", () => {
    const p = pageFromHash();
    if (p !== state.page) go(p);
  });

  await go(pageFromHash(), { keepScroll: true });
}

async function reloadBatch() {
  // Warm candidate generation so the overview aggregate and the candidates page
  // always agree; the endpoint is idempotent on the server side.
  try { await api(`/api/v1/candidates?batch_id=${enc(state.batch)}&page_size=1`); } catch { /* ignore */ }
  state.cand.all = null;
  state.overview = await api(`/api/v1/overview?batch_id=${enc(state.batch)}`);
  try { await loadAllCandidates(); } catch { state.cand.all = []; }
}

boot();

