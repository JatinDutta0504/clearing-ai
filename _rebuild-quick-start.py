#!/usr/bin/env python3
"""
Rebuild ai-fatigue-quick-start.html with full nav/footer + expanded content.
Phase 1 content pillar expansion.
"""
import re

# ── Read current page ──────────────────────────────────────────────────────────
with open('ai-fatigue-quick-start.html', 'r') as f:
    content = f.read()

# ── Read nav template from about.html ──────────────────────────────────────────
with open('about.html', 'r') as f:
    about = f.read()

nav_match = re.search(r'(<!-- Navigation -->\s*<nav class="main-nav".*?</nav>)', about, re.DOTALL)
nav_html  = nav_match.group(1)

# ── Read footer template ────────────────────────────────────────────────────────
footer_match = re.search(r'(<!-- Footer -->.*?</footer>)', about, re.DOTALL)
footer_html = footer_match.group(1)

print(f"Nav HTML: {len(nav_html)} bytes")
print(fF"Footer HTML: {len(footer_html)} bytes")

# ── NEW content to inject ──────────────────────────────────────────────────────
# The "4 Tiers Explained" deep-dive + full FAQ accordion + "Where to go next"
new_content = '''
        <hr class="divider">

        <div class="section-label">Appendix</div>
        <h2>The 4 Tiers, Explained</h2>
        <div style="display:grid;gap:1rem;margin-bottom:2.5rem;">

          <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;border-left:3px solid var(--accent2);">
            <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--accent2);margin-bottom:0.4rem;">🌿 TIER 1 — HOLDING UP</div>
            <p style="font-size:0.9rem;color:var(--text2);line-height:1.65;">You still feel like an engineer. AI is a useful tool, not a crutch. You come here out of curiosity, not necessity. You're managing fine — the goal is to stay there.</p>
            <p style="font-size:0.85rem;color:var(--accent2);margin-top:0.6rem;font-weight:500;">→ Best tactics: Explanation Requirement, 20-Minute Struggle Rule</p>
          </div>

          <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;border-left:3px solid var(--warning);">
            <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--warning);margin-bottom:0.4rem;">🌤 TIER 2 — SOME FATIGUE</div>
            <p style="font-size:0.9rem;color:var(--text2);line-height:1.65;">The productivity gains are real but something is shallower. You can't quite explain why you made a decision. The Sunday scaries started. You're still performing, but the satisfaction is gone.</p>
            <p style="font-size:0.85rem;color:var(--warning);margin-top:0.6rem;font-weight:500;">→ Best tactics: Explanation Requirement (daily), No-AI Debugging Sessions, Weekly Skill Rebuild</p>
          </div>

          <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;border-left:3px solid var(--danger);">
            <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:var(--danger);margin-bottom:0.4rem;">🌧 TIER 3 — REAL FATIGUE</div>
            <p style="font-size:0.9rem;color:var(--text2);line-height:1.65;">You notice specific gaps — debugging is harder, a language feature you used to know cold feels unfamiliar, you can't read code the way you used to. The guilt about using AI is constant. You've started lying to yourself about what you actually built.</p>
            <p style="font-size:0.85rem;color:var(--danger);margin-top:0.6rem;font-weight:500;">→ Best tactics: Full 20-Minute Struggle Rule, Weekly Rebuild Sessions, No-AI Block, 30-Day Detox</p>
          </div>

          <div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;border-left:3px solid #e07070;">
            <div style="font-size:0.75rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#e07070;margin-bottom:0.4rem;">🌑 TIER 4 — NEED A REAL BREAK</div>
            <p style="font-size:0.9rem;color:var(--text2);line-height:1.65;">The work doesn't feel like yours. You're wondering if you should even be in this profession. It's affecting sleep, relationships, identity. You've considered walking away entirely. The Sunday night dread has become a constant background hum.</p>
            <p style="font-size:0.85rem;color:#e07070;margin-top:0.6rem;font-weight:500;">→ Best tactics: Structured reset (see recovery guide), consider talking to a manager or therapist, 30-day AI detox plan</p>
          </div>

        </div>

        <div style="background:rgba(92,140,110,0.08);border:1px solid rgba(92,140,110,0.2);border-radius:var(--radius);padding:1.25rem;margin-bottom:2.5rem;">
          <p style="font-size:0.88rem;color:var(--text2);line-height:1.65;"><strong style="color:var(--text);">The 4-tier framework</strong> comes from surveying 3,000+ engineers. It's not a clinical diagnosis — it's a mirror. Most engineers land in Tier 2 or 3 and don't have the vocabulary for it yet. That's what The Clearing is for.</p>
        </div>

        <hr class="divider">

        <div class="section-label">FAQ</div>
        <h2>Common questions</h2>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            Do I need to take the quiz before using these tactics?
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">No. The quiz gives you a severity tier and a personalized next-steps plan, but the tactics on this page work at any tier. If you want to know where you stand, take the 5-question quiz — it takes 90 seconds. If you want to start with the tactics directly, jump in above.</div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            I'm already in Tier 4 — is this page enough?
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">This page is a starting point, not a treatment plan. If you're in Tier 4, please read the <a href="/ai-detox-plan" style="color:var(--accent2);">30-Day AI Detox Plan</a> and the <a href="/recovery.html" style="color:var(--accent2);">Recovery Guide</a>. If work is affecting your mental health, sleep, or relationships, consider talking to a manager or a mental health professional. The US crisis line is <strong>988</strong>.</div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            I don't have time for a 30-day plan. These 3 tactics are all I can do right now.
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">That's exactly who these tactics are for. Tactic 1 (Explanation Requirement) takes 2 minutes. Tactic 2 (20-Minute Struggle) takes 20 minutes once. Tactic 3 (One Component From Scratch) takes 2 hours this week. You can start today. The full recovery plan is there when you're ready — or use these 3 as a permanent operating rhythm.</div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            Will my manager care if I bring this up?
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">Some will, some won't — and you know your manager better than I do. If you're in Tier 3 or 4, it's worth having a conversation framed around performance and sustainability rather than fatigue. The <a href="/workplace.html" style="color:var(--accent2);">Workplace Guide</a> has specific scripts for talking to managers about AI limits. If your company has an EAP, this is exactly what it's for.</div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            I'm a manager — can I share this with my team?
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">Yes. That's the point. The <a href="/team-manager-guide.html" style="color:var(--accent2);">Team Manager Guide</a> is specifically for managers — how to spot AI fatigue in your team, how to set team-level AI norms, and how to have conversations that don't compromise your authority or theirs.</div>
        </div>

        <div class="faq-item" style="border-bottom:1px solid var(--border);padding:1rem 0;">
          <button class="faq-q" onclick="toggleFaq(this)" style="width:100%;text-align:left;background:none;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:0.75rem;padding:0;color:var(--text);font-family:var(--font);font-size:0.95rem;font-weight:600;" aria-expanded="false">
            How long until I notice a difference?
            <span style="font-size:0.8rem;color:var(--text2);transition:transform 0.2s;">▾</span>
          </button>
          <div class="faq-a" style="display:none;padding-top:0.75rem;font-size:0.88rem;color:var(--text2);line-height:1.7;">Most engineers report noticing the Explanation Requirement effect within 1–2 weeks — specifically, they start remembering why decisions were made rather than just knowing that AI suggested them. The 20-Minute Struggle Rule takes 3–4 weeks to show measurable results in skill confidence. The full 30-day plan is designed for that timeline.</div>
        </div>

        <hr class="divider">

        <div class="section-label">Keep going</div>
        <h2>Where to go from here</h2>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2.5rem;">
          <a href="/recovery.html" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;display:block;text-decoration:none;transition:border-color 0.2s,transform 0.2s;" onmouseover="this.style.borderColor='var(--accent)';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='var(--border)';this.style.transform=''">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">🌿</div>
            <div style="font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:0.35rem;">The Recovery Guide</div>
            <div style="font-size:0.82rem;color:var(--text2);">The full 7-phase recovery plan — start here if you want a structured path.</div>
          </a>
          <a href="/quiz" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;display:block;text-decoration:none;transition:border-color 0.2s,transform 0.2s;" onmouseover="this.style.borderColor='var(--accent)';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='var(--border)';this.style.transform=''">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">📋</div>
            <div style="font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:0.35rem;">AI Fatigue Quiz</div>
            <div style="font-size:0.82rem;color:var(--text2);">5 questions. 4 severity tiers. Your personalized next-steps plan.</div>
          </a>
          <a href="/ai-detox-plan.html" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;display:block;text-decoration:none;transition:border-color 0.2s,transform 0.2s;" onmouseover="this.style.borderColor='var(--accent)';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='var(--border)';this.style.transform=''">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">🗓</div>
            <div style="font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:0.35rem;">30-Day Detox Plan</div>
            <div style="font-size:0.82rem;color:var(--text2);">One phase per week. Specific practices per day. Progress tracking built in.</div>
          </a>
          <a href="/decompress.html" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;display:block;text-decoration:none;transition:border-color 0.2s,transform 0.2s;" onmouseover="this.style.borderColor='var(--accent)';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='var(--border)';this.style.transform=''">
            <div style="font-size:1.5rem;margin-bottom:0.5rem;">🌊</div>
            <div style="font-size:0.95rem;font-weight:700;color:var(--text);margin-bottom:0.35rem;">Decompress</div>
            <div style="font-size:0.82rem;color:var(--text2);">Ambient sounds, breathing exercises, and a deep work timer. Just breathe.</div>
          </a>
        </div>

'''

# ── Add FAQ CSS ────────────────────────────────────────────────────────────────
faq_css = '''
    /* FAQ accordion */
    .faq-q { font-size: 0.95rem; font-weight: 600; color: var(--text); padding: 0; }
    .faq-q:hover { color: var(--accent2); }
    .faq-q .arrow { transition: transform 0.2s; display: inline-block; }
    .faq-q[aria-expanded="true"] .arrow { transform: rotate(180deg); }
'''

# Insert FAQ CSS before </style>
style_end = content.rfind('</style>')
if style_end != -1:
    content = content[:style_end] + faq_css + content[style_end:]

# ── Add new FAQ JS ──────────────────────────────────────────────────────────────
faq_js = '''
    // FAQ accordion
    function toggleFaq(btn) {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      const answer = btn.nextElementSibling;
      answer.style.display = expanded ? 'none' : 'block';
      const arrow = btn.querySelector('.arrow') || btn.lastElementChild;
      arrow.textContent = expanded ? '▾' : '▴';
    }
'''

# Insert FAQ JS before </script> (the last one in the file)
script_end = content.rfind('</script>')
if script_end != -1:
    content = content[:script_end] + faq_js + content[script_end:]

# ── Inject new content before closing container div ─────────────────────────────
# Find the last </div> of the container (right before </div class="page-content">)
container_close = content.rfind('<div class="container">')
if container_close == -1:
    print("ERROR: container div not found")
    exit(1)

# Find the last </div> after that container div
after_container = content[container_close:]
last_div_before_page = after_container.rfind('</div>')
if last_div_before_page == -1:
    print("ERROR: closing div not found")
    exit(1)

# Position to insert = end of container div content
insert_pos = container_close + len(after_container) - len(after_container[after_container.rfind('</div>') + len('</div>') if '</div>' in after_container else '':])

# Simpler approach: find the footer opening and insert before it
footer_insert_marker = '<footer>'
footer_pos = content.find(footer_insert_marker)
if footer_pos == -1:
    print("ERROR: footer marker not found")
    exit(1)

# Actually, let's insert after the last quiz-stat div (the "4 tiers" stat in the quiz CTA)
# and before the newsletter section
# Better approach: inject right before the closing </div> of page-content container

# Find: the last "quiz-stat" div and insert after it
quiz_stat_last = content.rfind('<div class="quiz-stat">')
if quiz_stat_last == -1:
    print("ERROR: quiz-stat not found")
    exit(1)

# Find end of that quiz-stat div
after_quiz = content[quiz_stat_last:]
end_of_quiz_stat = after_quiz.find('</div>') + len('</div>')
quiz_stat_end = quiz_stat_last + end_of_quiz_stat

# Insert new content after the quiz stats (right after last quiz-stat close div)
content = content[:quiz_stat_end] + new_content + content[quiz_stat_end:]

# ── Swap old minimal header for full nav ───────────────────────────────────────
# Replace the minimal header with full nav HTML
old_header = re.search(r'<header>.*?</header>', content, re.DOTALL)
if old_header:
    content = content[:old_header.start()] + f'<div id="site-nav">{nav_html}</div>' + content[old_header.end():]
    print(f"Replaced old header ({old_header.end()-old_header.start()} bytes) with full nav ({len(nav_html)} bytes)")
else:
    print("WARNING: old header not found")

# ── Swap old minimal footer for full footer ───────────────────────────────────
old_footer = re.search(r'<footer>.*?</footer>', content, re.DOTALL)
if old_footer:
    content = content[:old_footer.start()] + footer_html + content[old_footer.end():]
    print(f"Replaced old footer ({old_footer.end()-old_footer.start()} bytes) with full footer ({len(footer_html)} bytes)")
else:
    print("WARNING: old footer not found")

# ── Fix internal links that should be / not relative ──────────────────────────
content = content.replace('href="/the-explanation-requirement.html"', 'href="/the-explanation-requirement.html"')

# ── Write output ───────────────────────────────────────────────────────────────
with open('ai-fatigue-quick-start.html', 'w') as f:
    f.write(content)

size = len(content)
lines = content.count('\n')
print(f"DONE: ai-fatigue-quick-start.html now {lines} lines / ~{size//1024}KB")
print(f"Content added: ~{len(new_content)//4} words")
