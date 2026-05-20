#!/usr/bin/env python3
"""Build dispatch-70, 71, 72 HTML from MD sources."""

import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
ISSUES_DIR = os.path.join(BASE, "newsletter-issues")

issues = [
    {
        "num": "70",
        "md": "dispatch-70.md",
        "title": "The Competence Inflation Trap",
        "date": "May 20, 2026",
        "section": "Skill Atrophy",
        "read_time": "~8 min read",
        "published_time": "2026-05-20",
        "topics": "competence inflation skill gap AI tools confidence developer",
        "excerpt": "You look at your title. You look at your output. You look at your salary. And something in your gut says: I don't think I could build this from scratch anymore. That's the competence inflation trap — and it's more dangerous than imposter syndrome.",
    },
    {
        "num": "71",
        "md": "dispatch-71.md",
        "title": "The Autonomy Gap",
        "date": "May 27, 2026",
        "section": "Mindset",
        "read_time": "~8 min read",
        "published_time": "2026-05-27",
        "topics": "autonomy gap problem framing AI tools thinking judgment",
        "excerpt": "You can ask AI anything and get an answer in seconds. That's the feature nobody warned you about. At some point, you stop asking the right question — because the answer arrives before you notice the question.",
    },
    {
        "num": "72",
        "md": "dispatch-72.md",
        "title": "The Visibility Trap",
        "date": "June 3, 2026",
        "section": "Career Resilience",
        "read_time": "~9 min read",
        "published_time": "2026-06-03",
        "topics": "visibility output contribution career AI tools performance review",
        "excerpt": "You are doing more work than ever. Your output is up. Your velocity is up. And yet nobody — including you — can see what you're actually contributing. This is the visibility trap. The harder you work to be seen, the more invisible you feel.",
    },
]

def md_to_html(text):
    """Convert Markdown to HTML (simple converter for newsletter content)."""
    html = text.strip()
    # Headers
    html = re.sub(r'^## (.+)$', r'<h2 class="section-title">\1</h2>', html, flags=re.M)
    html = re.sub(r'^### (.+)$', r'<h3 class="sub-title">\1</h3>', html, flags=re.M)
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    # Paragraphs (split by double newlines)
    paragraphs = re.split(r'\n\n+', html)
    result = []
    in_list = False
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        # Skip markdown metadata lines
        if para.startswith('# ') or para.startswith('*Issue') or para.startswith('*Missed') or para.startswith('*If this') or para.startswith('---'):
            continue
        if para.startswith('---'):
            continue
        if re.match(r'^\*\*That.s it', para):
            continue
        if re.match(r'^— The Clearing', para):
            continue
        if para.startswith('*P.S.'):
            continue
        # Process lists
        if para.startswith('**') and ':' in para:
            parts = para.split('\n')
            list_items = []
            for p in parts:
                p = p.strip()
                if p.startswith('**') and '**' in p:
                    p = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', p)
                    list_items.append(f'<li>{p}</li>')
            if list_items:
                result.append(f'<ul class="skill-list">{"".join(list_items)}</ul>')
                continue
        if para.startswith('1. ') or para.startswith('2. ') or para.startswith('3. ') or para.startswith('4. '):
            items = re.findall(r'^\d+\. (.+)$', para, flags=re.M)
            if items:
                li = ''.join(f'<li>{it}</li>' for it in items)
                result.append(f'<ol class="numbered-list">{li}</ol>')
                continue
        # Skip meta lines
        if para.startswith('**Schedule') or para.startswith('**Target') or para.startswith('**Post timing') or para.startswith('**Company') or para.startswith('**UTM'):
            continue
        # HR / separators
        if para == '---':
            continue
        # Quote blocks
        if para.startswith('>'):
            q = para.replace('> ', '').strip()
            q = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', q)
            result.append(f'<blockquote class="quote">{q}</blockquote>')
            continue
        # Regular paragraph
        para = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', para)
        para = re.sub(r'\*(.+?)\*', r'<em>\1</em>', para)
        para = para.replace('\n', ' ')
        result.append(f'<p>{para}</p>')
    return '\n'.join(result)

def get_md_content(num):
    """Read MD file for issue number."""
    fname = os.path.join(ISSUES_DIR, f"dispatch-{num}.md")
    if not os.path.exists(fname):
        return None
    with open(fname, 'r') as f:
        return f.read()

def build_html(issue):
    num = issue['num']
    md_content = get_md_content(num)
    if not md_content:
        print(f"  SKIP: dispatch-{num}.md not found")
        return None

    body_html = md_to_html(md_content)

    title_slug = f"#70 The Competence Inflation Trap" if num == "70" else (
        f"#71 The Autonomy Gap" if num == "71" else f"#72 The Visibility Trap"
    )

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Dispatch #{num} — {issue['title']} | The Clearing</title>
  <meta name="description" content="{issue['excerpt']}">
  <link rel="canonical" href="https://clearing-ai.com/newsletter-issues/dispatch-{num}.html">
  <link rel="alternate" type="application/rss+xml" title="The Clearing RSS Feed" href="https://clearing-ai.com/feed.xml">
  <meta property="og:title" content="The Dispatch #{num} — {issue['title']}">
  <meta property="og:description" content="{issue['excerpt']}">
  <meta property="og:image" content="https://clearing-ai.com/og-image.png">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://clearing-ai.com/newsletter-issues/dispatch-{num}.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="The Dispatch #{num} — {issue['title']}">
  <meta name="twitter:description" content="{issue['excerpt']}">
  <meta name="author" content="The Clearing">
  <meta property="article:published_time" content="{issue['published_time']}">
  <meta property="article:section" content="The Dispatch">
  <link rel="stylesheet" href="../css/style.min.css" />
  <noscript><style>.fallback {{ display: block; }}</style></noscript>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "The Dispatch #{num} — {issue['title']}",
    "description": "{issue['excerpt']}",
    "author": {{ "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" }},
    "publisher": {{ "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" }},
    "datePublished": "{issue['published_time']}",
    "dateModified": "{issue['published_time']}",
    "url": "https://clearing-ai.com/newsletter-issues/dispatch-{num}.html",
    "isPartOf": {{
      "@type": "Periodical",
      "name": "The Dispatch",
      "issn": "https://clearing-ai.com/newsletter-archive.html"
    }},
    "breadcrumb": {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://clearing-ai.com/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Newsletter", "item": "https://clearing-ai.com/newsletter.html" }},
        {{ "@type": "ListItem", "position": 3, "name": "Archive", "item": "https://clearing-ai.com/newsletter-archive.html" }},
        {{ "@type": "ListItem", "position": 4, "name": "#{num} {issue['title']}", "item": "https://clearing-ai.com/newsletter-issues/dispatch-{num}.html" }}
      ]
    }}
  }}
  </script>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #0c0c0e;
      --surface: #141418;
      --surface2: #1c1c22;
      --border: #2a2a35;
      --text: #e8e6e3;
      --text-muted: #8a8a96;
      --accent: #4a9c6d;
      --accent-warm: #c4793a;
      --accent-cool: #4a7a9c;
      --radius: 10px;
      --font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    }}
    [data-theme="light"] {{
      --bg: #f4f1ec;
      --surface: #ece8e2;
      --surface2: #e2ddd5;
      --border: #ccc5ba;
      --text: #1a1a18;
      --text-muted: #6a6a62;
    }}
    html {{ font-size: 16px; scroll-behavior: smooth; }}
    body {{ background: var(--bg); color: var(--text); font-family: var(--font); line-height: 1.7; }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .nav-bar {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      display: flex;
      align-items: center;
      gap: 8px;
      height: 56px;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .nav-bar a {{ color: var(--text-muted); font-size: 0.9rem; }}
    .nav-bar a:hover {{ color: var(--text); text-decoration: none; }}
    .nav-bar .sep {{ color: var(--border); }}
    .issue-header {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 48px 24px 40px;
      text-align: center;
    }}
    .issue-label {{
      font-size: 0.8rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent);
      font-weight: 600;
      margin-bottom: 16px;
    }}
    .issue-header h1 {{
      font-size: 2.2rem;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 12px;
    }}
    .issue-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      gap: 24px;
      justify-content: center;
      flex-wrap: wrap;
    }}
    .hero-banner {{
      background: linear-gradient(135deg, var(--surface) 0%, var(--surface2) 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px 36px;
      margin: 40px auto;
      max-width: 720px;
    }}
    .hero-banner h2 {{
      font-size: 1.4rem;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 16px;
    }}
    .hero-banner p {{ color: var(--text-muted); font-size: 0.95rem; }}
    main {{ max-width: 680px; margin: 0 auto; padding: 0 24px 80px; }}
    h2.section-title {{
      font-size: 1.25rem;
      font-weight: 700;
      margin: 48px 0 20px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      color: var(--text);
    }}
    h3.sub-title {{ font-size: 1.1rem; font-weight: 600; margin: 32px 0 14px; color: var(--text); }}
    p {{ margin-bottom: 18px; color: var(--text); }}
    strong {{ font-weight: 600; color: var(--text); }}
    .section-block {{ margin-bottom: 44px; }}
    .section-block h3 {{ font-size: 1.05rem; font-weight: 600; margin-bottom: 14px; color: var(--text); }}
    .section-block p {{ margin-bottom: 14px; }}
    .callout {{
      background: var(--surface2);
      border-left: 3px solid var(--accent);
      border-radius: 0 var(--radius) var(--radius) 0;
      padding: 18px 20px;
      margin: 24px 0;
      font-size: 0.95rem;
    }}
    .callout p {{ margin: 0; }}
    .callout strong {{ color: var(--accent); }}
    .skill-list {{ list-style: none; margin: 16px 0; }}
    .skill-list li {{
      padding: 10px 14px;
      margin-bottom: 8px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 0.9rem;
    }}
    .numbered-list {{ list-style: decimal; margin: 20px 0 20px 24px; }}
    .numbered-list li {{ margin-bottom: 14px; font-size: 0.95rem; }}
    .quote {{
      border-left: 3px solid var(--accent-cool);
      padding: 14px 18px;
      margin: 28px 0;
      color: var(--text-muted);
      font-style: italic;
      font-size: 0.95rem;
      background: var(--surface);
      border-radius: 0 var(--radius) var(--radius) 0;
    }}
    .cta-block {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 28px 32px;
      margin: 48px 0;
      text-align: center;
    }}
    .cta-block p {{ font-size: 0.95rem; margin-bottom: 16px; }}
    .cta-block a {{
      display: inline-block;
      background: var(--accent);
      color: var(--bg);
      padding: 12px 28px;
      border-radius: 40px;
      font-weight: 600;
      font-size: 0.95rem;
    }}
    .cta-block a:hover {{ background: #3d8a5e; text-decoration: none; }}
    .cta-block .secondary {{
      display: block;
      margin-top: 12px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .ps-block {{
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 24px;
      font-size: 0.9rem;
      color: var(--text-muted);
      font-style: italic;
      margin: 32px 0 0;
    }}
    footer {{
      border-top: 1px solid var(--border);
      padding: 32px 24px;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.85rem;
    }}
    footer a {{ color: var(--accent); }}
    @media (max-width: 600px) {{
      .issue-header h1 {{ font-size: 1.7rem; }}
      .hero-banner {{ padding: 24px 20px; margin: 24px 16px; }}
      main {{ padding: 0 16px 60px; }}
    }}
  </style>
</head>
<body>

  <nav class="nav-bar">
    <a href="https://clearing-ai.com/">Home</a>
    <span class="sep">›</span>
    <a href="https://clearing-ai.com/newsletter.html">Newsletter</a>
    <span class="sep">›</span>
    <a href="https://clearing-ai.com/newsletter-archive.html">Archive</a>
    <span class="sep">›</span>
    <a href="https://clearing-ai.com/newsletter-issues/dispatch-{num}.html">{title_slug}</a>
  </nav>

  <header class="issue-header">
    <div class="issue-label">The Dispatch #{num} · {issue['date']}</div>
    <h1>{issue['title']}</h1>
    <div class="issue-meta">
      <span>For engineers who use AI tools daily</span>
      <span>{issue['read_time']}</span>
      <span>{issue['section']}</span>
    </div>
  </header>

  <main>
{body_html}

    <div class="cta-block">
      <p>If the {issue['title'].lower()} resonates — the AI Fatigue Quiz surfaces where else this dynamic shows up in your daily experience with AI tools.</p>
      <a href="https://clearing-ai.com/quiz.html">Take the AI Fatigue Quiz →</a>
      <a class="secondary" href="https://clearing-ai.com/manifesto.html">Read: An Engineer's Manifesto for Intentional AI Use →</a>
    </div>

    <p class="ps-block">P.S. If you found this useful — forward it to an engineer who could use it. The best way to grow a community worth being in is to invite people who are trying to work well with AI.</p>

  </main>

  <footer>
    <p>The Clearing — helping engineers work well with AI without losing themselves.</p>
    <p><a href="https://clearing-ai.com/newsletter.html">Subscribe to The Dispatch</a> · <a href="https://clearing-ai.com/newsletter-archive.html">Browse the archive</a> · <a href="https://clearing-ai.com/">clearing-ai.com</a></p>
  </footer>

</body>
</html>'''
    return html

for issue in issues:
    num = issue['num']
    html = build_html(issue)
    if html:
        out_path = os.path.join(ISSUES_DIR, f"dispatch-{num}.html")
        with open(out_path, 'w') as f:
            f.write(html)
        print(f"Built: dispatch-{num}.html ({len(html)} bytes)")
    else:
        print(f"Failed: dispatch-{num}.html")

print("Done.")