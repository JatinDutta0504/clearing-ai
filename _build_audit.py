#!/usr/bin/env python3
"""Build ai-weekly-audit.html"""
import json

path = '/Users/nightcoder/Desktop/TheClearing/ai-weekly-audit.html'

CSS = """:root{--bg:#0f0f0f;--bg-elevated:#181818;--bg-card:#1e1e1e;--bg-input:#242424;--border:#2e2e2e;--text:#e8e4df;--text-muted:#9a9590;--accent:#d4a574;--accent-dim:#a07850;--accent-soft:rgba(212,165,116,0.12);--warn:#c07040;--warn-soft:rgba(192,112,64,0.12);--green:#5a9a6a;--green-soft:rgba(90,154,106,0.12);--font-body:'DM Sans',system-ui,sans-serif;--font-serif:'Lora',Georgia,serif;--radius:12px;--shadow:0 4px 24px rgba(0,0,0,0.4);--spring:cubic-bezier(0.22,1,0.36,1)}
[data-theme="light"]{--bg:#faf8f5;--bg-elevated:#f2efe9;--bg-card:#ffffff;--bg-input:#f0ede8;--border:#e0dbd4;--text:#1a1816;--text-muted:#6b6560;--accent:#8b5e3c;--accent-dim:#a07850;--accent-soft:rgba(139,94,60,0.1);--warn:#a05020;--warn-soft:rgba(160,80,32,0.1);--green:#4a7a5a;--green-soft:rgba(74,122,90,0.1)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--font-body);background:var(--bg);color:var(--text);line-height:1.7;min-height:100vh}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.skip-link{position:absolute;left:-9999px}.skip-link:focus{position:static}
nav{position:sticky;top:0;z-index:100;background:rgba(15,15,15,0.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 24px}
[data-theme="light"] nav{background:rgba(250,248,245,0.92)}
.nav-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:60px}
.nav-logo{font-family:var(--font-serif);font-size:1.15rem;font-weight:600;color:var(--text);display:flex;align-items:center;gap:8px}
.nav-links{display:flex;gap:4px;list-style:none;align-items:center}
.nav-links a{color:var(--text-muted);font-size:0.875rem;padding:6px 12px;border-radius:8px;transition:all 0.2s}
.nav-links a:hover{color:var(--text);background:var(--bg-elevated);text-decoration:none}
.nav-dropdown{position:relative}
.nav-dropdown>a{display:flex;align-items:center;gap:4px}
.nav-dropdown-content{display:none;position:absolute;top:100%;left:0;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:8px;min-width:200px;box-shadow:var(--shadow);z-index:200}
.nav-dropdown:hover .nav-dropdown-content{display:block}
.nav-dropdown-content a{display:block;padding:8px 12px;border-radius:6px;color:var(--text-muted);font-size:0.875rem;white-space:nowrap}
.nav-dropdown-content a:hover{background:var(--accent-soft);color:var(--text);text-decoration:none}
.theme-toggle{background:none;border:none;color:var(--text-muted);cursor:pointer;font-size:1rem;padding:6px;transition:color 0.2s}
.theme-toggle:hover{color:var(--accent)}
.reading-progress{position:fixed;top:60px;left:0;height:3px;background:var(--accent);width:0%;z-index:99;transition:width 0.1s linear}
.hero{padding:72px 24px 48px;text-align:center;max-width:720px;margin:0 auto}
.hero-eyebrow{font-size:0.78rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);margin-bottom:14px;display:flex;align-items:center;justify-content:center;gap:8px}
.hero h1{font-family:var(--font-serif);font-size:clamp(1.7rem,5vw,2.6rem);font-weight:600;line-height:1.2;margin-bottom:16px}
.lead{font-family:var(--font-serif);font-size:1.05rem;color:var(--text-muted);line-height:1.7;max-width:600px;margin:0 auto 24px;font-style:italic}
.stat-bar{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;margin-top:28px}
.stat-chip{background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:10px 18px;text-align:center;min-width:100px}
.stat-chip strong{display:block;font-size:1.25rem;color:var(--accent);font-weight:700}
.stat-chip span{font-size:0.7rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em}
.container{max-width:720px;margin:0 auto;padding:0 24px 80px}
h2{font-family:var(--font-serif);font-size:1.4rem;font-weight:600;margin:48px 0 18px;color:var(--text)}
h3{font-family:var(--font-serif);font-size:1.1rem;font-weight:600;margin:28px 0 12px;color:var(--text)}
p{margin-bottom:16px;color:var(--text)}
.lead-p{font-size:1rem;color:var(--text-muted);margin-bottom:24px}
.callout{background:var(--bg-elevated);border-left:3px solid var(--accent);padding:18px 22px;border-radius:0 var(--radius) var(--radius) 0;margin:28px 0}
.callout p:last-child{margin-bottom:0}
.callout-warn{background:var(--warn-soft);border-left-color:var(--warn)}
.callout-green{background:var(--green-soft);border-left-color:var(--green)}
.section-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:28px;margin:28px 0}
.card-label{font-size:0.72rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:10px}
.week-nav{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:32px 0 24px}
.week-btn{background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:8px 16px;font-family:var(--font-body);font-size:0.875rem;color:var(--text-muted);cursor:pointer;transition:all 0.2s var(--spring)}
.week-btn:hover{border-color:var(--accent);color:var(--text)}
.week-btn.active{background:var(--accent-soft);border-color:var(--accent);color:var(--accent);font-weight:600}
.week-btn.done{background:var(--green-soft);border-color:var(--green);color:var(--green)}
.week-btn.locked{opacity:0.4;cursor:not-allowed}
.week-dots{display:flex;gap:8px;justify-content:center;margin:20px 0;flex-wrap:wrap}
.week-dot{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.7rem;font-weight:600;border:2px solid var(--border);color:var(--text-muted);flex-shrink:0;transition:all 0.2s}
.week-dot.done{background:var(--green-soft);border-color:var(--green);color:var(--green)}
.week-dot.today{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
.week-dot.future{border-style:dashed}
.panel{display:none}.panel.active{display:block}
.panel-header{margin-bottom:24px}
.panel-header h2{font-size:1.2rem;margin-bottom:8px}
.intro-text{font-size:0.95rem;color:var(--text-muted);margin-bottom:0;max-width:600px}
.task-grid{display:grid;gap:10px;margin:20px 0}
.task-row{display:flex;align-items:center;padding:12px 16px;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;gap:12px}
.task-icon{font-size:1.2rem;flex-shrink:0;width:28px;text-align:center}
.task-name{flex:1;font-size:0.9rem;color:var(--text)}
.task-controls{display:flex;align-items:center;gap:8px}
.task-btn{background:var(--bg-input);border:1px solid var(--border);border-radius:6px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:0.875rem;color:var(--text-muted);transition:all 0.15s;flex-shrink:0}
.task-btn:hover{border-color:var(--accent);color:var(--accent)}
.task-num{font-size:0.95rem;font-weight:700;color:var(--accent);min-width:24px;text-align:center}
.task-total-row{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;background:var(--accent-soft);border:1px solid var(--accent);border-radius:8px;margin-top:8px;font-weight:600;font-size:0.95rem}
textarea{width:100%;padding:12px 14px;background:var(--bg-input);border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:var(--font-body);font-size:0.9rem;resize:vertical;min-height:72px;transition:border-color 0.2s}
textarea:focus{outline:none;border-color:var(--accent)}
textarea::placeholder{color:var(--text-muted);opacity:0.7}
.heatmap{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin:24px 0}
.heat-cell{aspect-ratio:1;border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:0.65rem;font-weight:600;color:var(--text-muted);min-height:60px;transition:all 0.2s;border:1px solid var(--border)}
.heat-cell.empty{background:var(--bg-elevated)}
.heat-cell.l0{background:rgba(90,154,106,0.12);border-color:rgba(90,154,106,0.3);color:var(--green)}
.heat-cell.l1{background:rgba(90,154,106,0.22);border-color:rgba(90,154,106,0.45);color:var(--green)}
.heat-cell.l2{background:rgba(212,165,116,0.18);border-color:rgba(212,165,116,0.45);color:var(--accent)}
.heat-cell.l3{background:rgba(212,165,116,0.30);border-color:rgba(212,165,116,0.6);color:var(--accent)}
.heat-cell.l4{background:rgba(192,112,64,0.20);border-color:rgba(192,112,64,0.5);color:var(--warn)}
.heat-cell.l5{background:rgba(192,112,64,0.35);border-color:rgba(192,112,64,0.7);color:var(--warn)}
.heat-cell .heat-num{font-size:1.15rem;line-height:1}
.heat-cell .heat-label{font-size:0.55rem;margin-top:3px}
.heat-legend{display:flex;justify-content:center;gap:14px;margin-top:10px;font-size:0.68rem;color:var(--text-muted);flex-wrap:wrap}
.insight-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:24px 0}
.insight-card{background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:16px}
.insight-card .ic-emoji{font-size:1.3rem;margin-bottom:8px}
.insight-card h4{font-size:0.875rem;font-weight:600;margin-bottom:6px;color:var(--text)}
.insight-card p{font-size:0.78rem;color:var(--text-muted);margin-bottom:0;line-height:1.5}
.insight-card.warn{border-color:var(--warn);background:var(--warn-soft)}
.insight-card.warn h4{color:var(--warn)}
.summary-table{width:100%;border-collapse:collapse;margin:20px 0;font-size:0.875rem}
.summary-table th{text-align:left;padding:10px 12px;background:var(--bg-elevated);border-bottom:1px solid var(--border);font-size:0.7rem;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--text-muted)}
.summary-table td{padding:10px 12px;border-bottom:1px solid var(--border);color:var(--text)}
.summary-table tr:last-child td{border-bottom:none}
.summary-table .num{font-weight:700;color:var(--accent);text-align:center}
.summary-table .good{color:var(--green)}
.summary-table .warn{color:var(--warn)}
.rec-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:18px 20px;margin:12px 0;display:flex;gap:14px;align-items:flex-start}
.rec-icon{font-size:1.4rem;flex-shrink:0;margin-top:2px}
.rec-content h4{font-size:0.9rem;font-weight:600;margin-bottom:5px;color:var(--text)}
.rec-content p{font-size:0.82rem;color:var(--text-muted);margin-bottom:0;line-height:1.6}
.rec-badge{display:inline-block;font-size:0.62rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:2px 7px;border-radius:20px;margin-bottom:6px}
.badge-high{background:var(--warn-soft);color:var(--warn)}
.badge-med{background:var(--accent-soft);color:var(--accent)}
.badge-low{background:var(--green-soft);color:var(--green)}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:8px;font-family:var(--font-body);font-size:0.9rem;font-weight:600;cursor:pointer;transition:all 0.2s var(--spring);border:none;text-decoration:none}
.btn-primary{background:var(--accent);color:#fff}
.btn-primary:hover{background:var(--accent-dim);text-decoration:none}
.btn-secondary{background:var(--bg-elevated);color:var(--text);border:1px solid var(--border)}
.btn-secondary:hover{border-color:var(--accent);text-decoration:none}
.btn-full{width:100%;justify-content:center}
.btn-group{display:flex;gap:10px;margin:20px 0;flex-wrap:wrap}
.btn-group .btn{flex:1;min-width:130px;justify-content:center}
@media(max-width:480px){.btn-group{flex-direction:column}}
.btn-group-centered{max-width:400px;margin:20px auto}
.newsletter-strip{background:linear-gradient(135deg,var(--bg-elevated),var(--bg-card));border:1px solid var(--border);border-radius:var(--radius);padding:28px;margin:40px 0;text-align:center}
.newsletter-strip h3{font-family:var(--font-serif);font-size:1.1rem;margin-bottom:10px}
.newsletter-strip p{font-size:0.875rem;color:var(--text-muted);margin-bottom:18px}
.newsletter-form{display:flex;gap:10px;max-width:420px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.newsletter-form input{flex:1;min-width:190px;padding:10px 14px;background:var(--bg-input);border:1px solid var(--border);border-radius:8px;color:var(--text);font-family:var(--font-body);font-size:0.9rem}
.newsletter-form input:focus{outline:none;border-color:var(--accent)}
@media(max-width:480px){.newsletter-form{flex-direction:column}}
.form-note{font-size:0.72rem;color:var(--text-muted);margin-top:10px;text-align:center}
.explore-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin:40px 0}
.exp-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:16px;text-decoration:none;transition:all 0.2s}
.exp-card:hover{border-color:var(--accent);transform:translateY(-2px);text-decoration:none}
.exp-card-emoji{font-size:1.3rem;margin-bottom:8px}
.exp-card h4{font-size:0.875rem;font-weight:600;color:var(--text);margin-bottom:4px}
.exp-card p{font-size:0.78rem;color:var(--text-muted);margin-bottom:0;line-height:1.5}
.faq-item{border-bottom:1px solid var(--border)}
.faq-item:last-child{border-bottom:none}
.faq-q{width:100%;background:none;border:none;cursor:pointer;text-align:left;padding:16px 0;font-family:var(--font-serif);font-size:0.95rem;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-q:hover{color:var(--accent)}
.faq-icon{font-size:1.1rem;color:var(--accent);transition:transform 0.25s var(--spring);flex-shrink:0}
.faq-a{max-height:0;overflow:hidden;transition:max-height 0.3s var(--spring)}
.faq-a-inner{padding:0 0 16px;color:var(--text-muted);font-size:0.875rem;line-height:1.7}
.faq-item.open .faq-icon{transform:rotate(45deg)}
.faq-item.open .faq-a{max-height:400px}
footer{background:var(--bg-elevated);border-top:1px solid var(--border);padding:40px 24px;margin-top:80px}
.footer-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px}
.footer-col h4{font-size:0.75rem;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-muted);margin-bottom:12px}
.footer-col ul{list-style:none;padding:0}
.footer-col li{margin-bottom:8px}
.footer-col a{color:var(--text-muted);font-size:0.875rem}
.footer-col a:hover{color:var(--accent);text-decoration:none}
.footer-bottom{max-width:1100px;margin:20px auto 0;padding-top:20px;border-top:1px solid var(--border);text-align:center;font-size:0.78rem;color:var(--text-muted)}
@media(max-width:768px){.hero{padding:56px 20px 36px}.footer-inner{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.footer-inner{grid-template-columns:1fr}.stat-bar{flex-direction:column;align-items:center}}
"""

NAV = """<nav role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="/" class="nav-logo">&#x1F33F; The Clearing</a>
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li class="nav-dropdown"><a href="/#quiz">Quiz &#9662;</a>
        <div class="nav-dropdown-content">
          <a href="/#quiz">Take the Quiz</a>
          <a href="/quiz-results-tier-1.html">Tier 1 &#8212; Holding Up</a>
          <a href="/quiz-results-tier-2.html">Tier 2 &#8212; Real Fatigue</a>
          <a href="/quiz-results-tier-3.html">Tier 3 &#8212; Significant</a>
          <a href="/quiz-results-tier-4.html">Tier 4 &#8212; Crisis</a>
        </div>
      </li>
      <li class="nav-dropdown"><a href="/recovery.html">Recover &#9662;</a>
        <div class="nav-dropdown-content">
          <a href="/recovery.html">Recovery Guide</a>
          <a href="/ai-detox-plan.html">30-Day AI Detox</a>
          <a href="/ai-fatigue-checklist.html">Recovery Checklist</a>
          <a href="/daily-practice.html">Daily Practice</a>
          <a href="/decompress.html">Decompress</a>
        </div>
      </li>
      <li class="nav-dropdown"><a href="/why.html">Understand &#9662;</a>
        <div class="nav-dropdown-content">
          <a href="/why.html">Why This Happens</a>
          <a href="/cognitive-load.html">Cognitive Load</a>
          <a href="/skill-atrophy.html">Skill Atrophy</a>
          <a href="/attention-residue.html">Attention Residue</a>
          <a href="/flow-state.html">Flow State</a>
          <a href="/automation-anxiety.html">Automation Anxiety</a>
          <a href="/the-science-of-ai-fatigue.html">The Science</a>
        </div>
      </li>
      <li class="nav-dropdown"><a href="/community.html">Connect &#9662;</a>
        <div class="nav-dropdown-content">
          <a href="/stories.html">Stories</a>
          <a href="/community.html">Community</a>
          <a href="/manifesto.html">Manifesto</a>
          <a href="/newsletter.html">Newsletter</a>
        </div>
      </li>
    </ul>
    <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark/light mode">&#9728;&#65039;</button>
  </div>
</nav>"""

TASK_TYPES = [
    ('code', '&#x1F4BB;', 'Code completion / inline suggestions'),
    ('debug', '&#x1F50D;', 'Debugging / error investigation'),
    ('read', '&#x1F4D6;', 'Reading / understanding code'),
    ('write', '&#x270D;', 'Writing / documentation'),
    ('plan', '&#x1F5FA;', 'Architecture / planning'),
    ('test', '&#x1F9EA;', 'Testing / test writing'),
    ('review', '&#x1F440;', 'Code review assistance'),
    ('learn', '&#x1F4DA;', 'Learning / research'),
]

def make_task_rows(day):
    return '\n'.join(
        '      <div class="task-row"><div class="task-icon">{ic}</div>'
        '<div class="task-name">{lbl}</div>'
        '<div class="task-controls">'
        '<button class="task-btn" onclick="adjust(\'day{d}\',\'{k}\',-1)">&#8722;</button>'
        '<span class="task-num" id="val-day{d}-{k}">0</span>'
        '<button class="task-btn" onclick="adjust(\'day{d}\',\'{k}\',1)">+</button>'
        '</div></div>'.format(d=day, k=k, ic=icon, lbl=lbl)
        for k, icon, lbl in TASK_TYPES
    )

def make_day_panel(day):
    rows = make_task_rows(day)
    return """
<!-- DAY {d} PANEL -->
<div class="panel" id="panel-day{d}">
  <div class="panel-header">
    <h2 id="day-title-{d}">Day {d} &#8212; <span id="day-date-{d}"></span></h2>
    <p class="intro-text">At the end of your workday, fill this in. Takes about 5 minutes.</p>
  </div>
  <div class="week-dots" id="week-dots-{d}"></div>
  <div class="section-card">
    <div class="card-label">How many sessions did you open each AI tool today?</div>
    <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:16px">Count each distinct work session separately. One session = one tool, one task.</p>
    <div class="task-grid">
{rows}
    </div>
    <div class="task-total-row">
      <span>Total AI sessions today</span>
      <span id="total-day{d}">0</span>
    </div>
  </div>
  <div class="section-card">
    <div class="card-label">How did you feel after AI-assisted work today?</div>
    <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:14px">On a scale of 1 (drained/exhausted) to 5 (energized/focused)</p>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px">
      <button class="week-btn energy-btn" data-day="{d}" data-energy="1" onclick="setEnergy({d},1)">1 &#8212; Drained</button>
      <button class="week-btn energy-btn" data-day="{d}" data-energy="2" onclick="setEnergy({d},2)">2 &#8212; Low</button>
      <button class="week-btn energy-btn" data-day="{d}" data-energy="3" onclick="setEnergy({d},3)">3 &#8212; Neutral</button>
      <button class="week-btn energy-btn" data-day="{d}" data-energy="4" onclick="setEnergy({d},4)">4 &#8212; Good</button>
      <button class="week-btn energy-btn" data-day="{d}" data-energy="5" onclick="setEnergy({d},5)">5 &#8212; Focused</button>
    </div>
    <p style="font-size:0.8rem;color:var(--text-muted)">Selected: <span id="energy-label-{d}">Not recorded</span></p>
  </div>
  <div class="section-card">
    <div class="card-label">Any tool-switching today?</div>
    <p style="font-size:0.85rem;color:var(--text-muted);margin-bottom:14px">Did you switch between multiple AI tools mid-task today?</p>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button class="week-btn switch-btn" data-day="{d}" data-switch="0" onclick="setSwitch({d},0)">No switching</button>
      <button class="week-btn switch-btn" data-day="{d}" data-switch="1" onclick="setSwitch({d},1)">1&#8211;2 times</button>
      <button class="week-btn switch-btn" data-day="{d}" data-switch="2" onclick="setSwitch({d},2)">3&#8211;5 times</button>
      <button class="week-btn switch-btn" data-day="{d}" data-switch="3" onclick="setSwitch({d},3)">Many times</button>
    </div>
  </div>
  <div class="section-card">
    <div class="card-label">Notes (optional)</div>
    <textarea id="notes-{d}" placeholder="Anything notable about today -- a hard problem, a frustrating session, a good workflow..." oninput="saveNotes({d})"></textarea>
  </div>
  <div class="btn-group btn-group-centered" style="margin-top:24px">
    <button class="btn btn-primary" onclick="saveDay({d})">Save Day {d} &#8594;</button>
  </div>
</div>
""".format(d=day, rows=rows)

INTRO_PANEL = """
<!-- INTRO PANEL -->
<div class="panel active" id="panel-intro">
  <div class="section-card">
    <div class="card-label">How It Works</div>
    <h2>Track Your Actual AI Usage &#8212; Not What You Think It Is</h2>
    <p>You might <em>think</em> you use AI tools moderately. But most engineers are surprised when they see the numbers. The gap between perceived and actual AI usage is one of the most consistent findings in the Clearing survey data.</p>
    <p>This audit makes the invisible visible. For seven days, log your AI tool sessions at the end of each workday. Five minutes. At the end of the week, see patterns that would otherwise stay hidden.</p>
    <div class="callout callout-green">
      <p><strong>Why sessions, not prompts?</strong> Research on cognitive load shows that the <em>decision to engage</em> with an AI tool &#8212; not the number of prompts &#8212; drives the mental overhead. Each session requires evaluation, context-setting, output review, and integration. A 45-minute AI pair-programming session counts the same as a five-prompt check.</p>
    </div>
    <h3>What you will track</h3>
    <div class="insight-grid">
      <div class="insight-card"><div class="ic-emoji">&#128202;</div><h4>Session Count</h4><p>How many times you opened an AI tool for work tasks each day</p></div>
      <div class="insight-card"><div class="ic-emoji">&#127919;</div><h4>Task Types</h4><p>Which work tasks you use AI for most often</p></div>
      <div class="insight-card"><div class="ic-emoji">&#128555;</div><h4>How It Felt</h4><p>Your subjective energy and focus after AI-assisted work sessions</p></div>
      <div class="insight-card"><div class="ic-emoji">&#128260;</div><h4>Tool Switching</h4><p>How often you opened multiple AI tools in one session</p></div>
    </div>
    <div class="callout">
      <p><strong>Your data is yours.</strong> All entries are stored in your browser localStorage. Nothing is sent to any server. You can clear it anytime via browser settings.</p>
    </div>
    <h3>Before You Start</h3>
    <p>Pick a week where you will be doing mostly normal work &#8212; not a crunch week, not a vacation. A normal week gives you the most honest baseline. You can log on any device as long as you use the same browser.</p>
    <div class="btn-group btn-group-centered">
      <button class="btn btn-primary" id="btn-start">Start My Audit &#8594;</button>
    </div>
  </div>
</div>
"""

SUMMARY_PANEL = """
<!-- WEEKLY SUMMARY PANEL -->
<div class="panel" id="panel-summary">
  <div class="panel-header">
    <h2>Your 7-Day Audit Results</h2>
    <p class="intro-text">Here is what your week revealed. Patterns you could not see from the inside.</p>
  </div>
  <div class="week-dots" style="margin-bottom:32px" id="summary-dots"></div>

  <div class="section-card">
    <div class="card-label">Weekly Overview</div>
    <div id="summary-overall"></div>
  </div>

  <div class="section-card">
    <div class="card-label">7-Day Heatmap</div>
    <p style="font-size:0.875rem;color:var(--text-muted);margin-bottom:16px">Each cell = one day. Darker = more AI sessions. Based on your logs.</p>
    <div class="heatmap" id="heatmap"></div>
    <div class="heat-legend">
      <span>&#128994; Low (0&#8211;2)</span>
      <span>&#x1F7E1; Moderate (3&#8211;5)</span>
      <span>&#128308; High (6+)</span>
    </div>
  </div>

  <div class="section-card">
    <div class="card-label">Daily Breakdown</div>
    <table class="summary-table">
      <thead>
        <tr>
          <th>Day</th>
          <th>Sessions</th>
          <th>Energy</th>
          <th>Tool Switching</th>
          <th>Signal</th>
        </tr>
      </thead>
      <tbody id="summary-table-body"></tbody>
    </table>
  </div>

  <div class="section-card">
    <div class="card-label">What Your Patterns Say</div>
    <div id="pattern-insights"></div>
  </div>

  <div class="section-card">
    <div class="card-label">Your Recommendations</div>
    <div id="recommendations"></div>
  </div>

  <div class="section-card">
    <div class="card-label">Share Your Findings</div>
    <p style="font-size:0.9rem;color:var(--text-muted);margin-bottom:16px">If this audit was useful, share it with a colleague who might benefit from seeing their own patterns.</p>
    <div class="btn-group">
      <button class="btn btn-secondary" onclick="copyReport()">&#128203; Copy Report</button>
      <button class="btn btn-secondary" onclick="window.print()">&#128424; Print</button>
    </div>
    <p class="form-note" id="copy-confirm" style="display:none;color:var(--green)">Report copied to clipboard!</p>
  </div>

  <div class="newsletter-strip">
    <h3>The Dispatch &#8212; Weekly for Tired Engineers</h3>
    <p>Every week: one pattern, one practice, one honest take on what it means to build software without losing yourself. Join 2,000+ engineers.</p>
    <form class="newsletter-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
      <input type="email" name="email" placeholder="your@email.com" required aria-label="Email address">
      <button type="submit" class="btn btn-primary">Subscribe Free</button>
    </form>
    <p class="form-note">No spam. Unsubscribe anytime. Your email stays yours.</p>
  </div>
</div>
"""

FAQ_HTML = """
<!-- FAQ SECTION -->
<div class="section-card" style="margin-top:40px">
  <h2>Frequently Asked Questions</h2>
  <div class="faq-item">
    <button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">Does tracking my AI usage make me more aware of it?<span class="faq-icon">+</span></button>
    <div class="faq-a"><div class="faq-a-inner">Research on self-monitoring shows that simply tracking a behavior increases awareness and often reduces it by 10&#8211;20%. Logging makes patterns visible that were previously invisible &#8212; the first step to changing them.</div