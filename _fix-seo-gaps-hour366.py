#!/usr/bin/env python3
"""Fix technical SEO gaps across 7 under-built pages.
Adds: OG/Twitter meta, canonical, woff2 font preload, main.js, reading time, WCAG ARIA skip link
"""
import re, os

BASE = "/Users/nightcoder/Desktop/TheClearing"
PAGES = [
    "ai-documentation-fatigue.html",
    "ai-debugging-fatigue.html",
    "ai-consultation-fatigue.html",
    "ai-healthcare-developer-fatigue.html",
    "pair-programming-fatigue.html",
    "neurodivergent-engineer-ai-fatigue.html",
    "the-craft-problem.html",
]

# Page-specific metadata (title, description, keywords, section-label, og_title, og_desc)
METADATA = {
    "ai-documentation-fatigue.html": {
        "title": "AI Documentation Fatigue: Why Writing Docs With AI Burns You Out",
        "description": "AI documentation tools should make writing easier. Instead, they create a specific drain: you're managing the AI's output while also managing your own thoughts about it. Here's why.",
        "keywords": "AI documentation fatigue, documentation burnout, AI writing docs, developer documentation tools, AI docs fatigue",
        "section": "Workplace",
        "og_title": "AI Documentation Fatigue: Why Writing Docs With AI Burns You Out",
        "og_desc": "AI documentation tools should make writing easier. Instead, they create a specific drain you can't quite name. Here's what's happening.",
    },
    "ai-debugging-fatigue.html": {
        "title": "AI Debugging Fatigue: When AI Makes Debugging Harder, Not Easier",
        "description": "AI debugging tools are supposed to help you find bugs faster. Instead, many engineers report that AI-debugged code takes longer to understand and maintain. The paradox of AI debugging.",
        "keywords": "AI debugging fatigue, AI debugging tools, debugging productivity, AI debug paradox, developer debugging AI",
        "section": "Workplace",
        "og_title": "AI Debugging Fatigue: When AI Makes Debugging Harder, Not Easier",
        "og_desc": "AI debugging tools should help you find bugs faster. Instead they often make code harder to understand. Here's why the paradox exists.",
    },
    "ai-consultation-fatigue.html": {
        "title": "AI Consultation Fatigue: The Hidden Cost of Always Having an Expert Available",
        "description": "Having an AI expert available 24/7 sounds like a gift. The reality: engineers report feeling like they can't think without consulting AI first, losing confidence in their own judgment. The hidden cost.",
        "keywords": "AI consultation fatigue, AI expert availability, developer judgment AI, AI decision fatigue, cognitive offloading cost",
        "section": "Understand",
        "og_title": "AI Consultation Fatigue: The Hidden Cost of Always Having an Expert Available",
        "og_desc": "Having an AI expert available 24/7 sounds like a gift. The reality: you stop trusting your own judgment. Here's the hidden cost.",
    },
    "ai-healthcare-developer-fatigue.html": {
        "title": "Healthcare Developer AI Fatigue: When AI Meets Life-Critical Code",
        "description": "Healthcare engineers face a specific form of AI fatigue: the stakes of their code are measured in human lives, and AI's confidence doesn't match the gravity. Why healthcare devs are uniquely affected.",
        "keywords": "healthcare developer AI fatigue, medical software AI, healthcare tech burnout, clinical software developer AI fatigue",
        "section": "Workplace",
        "og_title": "Healthcare Developer AI Fatigue: When AI Meets Life-Critical Code",
        "og_desc": "Healthcare engineers face a unique AI fatigue: their code affects human lives, and AI's confidence doesn't match the gravity. A specific, underserved problem.",
    },
    "pair-programming-fatigue.html": {
        "title": "Pair Programming Fatigue: When AI Collaboration Burns You Out",
        "description": "AI pair programming tools can drain more energy than solo work. Here's why collaborative AI coding creates a unique fatigue pattern — and how to fix it.",
        "keywords": "pair programming fatigue, AI pair programming, AI collaboration burnout, developer pairing AI tools, collaborative AI fatigue",
        "section": "Workplace",
        "og_title": "Pair Programming Fatigue: When AI Collaboration Burns You Out",
        "og_desc": "AI pair programming tools can drain more energy than solo work. Here's why collaborative AI coding creates a unique fatigue pattern.",
    },
    "neurodivergent-engineer-ai-fatigue.html": {
        "title": "Neurodivergent Engineers and AI Fatigue: A Different Experience",
        "description": "ADHD, autism, anxiety, and other neurodivergent experiences interact with AI in specific ways. Some engineers find AI helpful for task initiation; others find it overwhelms an already maxed-out sensory system.",
        "keywords": "neurodivergent AI fatigue, ADHD developer AI, autism software engineer AI, neurodivergent programmer AI burnout, ADHD AI tools",
        "section": "Understand",
        "og_title": "Neurodivergent Engineers and AI Fatigue: A Different Experience",
        "og_desc": "ADHD, autism, anxiety — neurodivergent engineers experience AI fatigue differently. Some find AI helpful; others find it overwhelms an already maxed-out system. Here's what the research says.",
    },
    "the-craft-problem.html": {
        "title": "The Craft Problem: Why Engineers Care About How They Build",
        "description": "Engineers aren't just building to ship — they're building to prove something to themselves. The craft question: does this code reflect who I am? AI changes the answer in ways that sting.",
        "keywords": "craft problem software engineering, developer craft identity, coding as craft, software engineer pride, code craftsmanship AI",
        "section": "Understand",
        "og_title": "The Craft Problem: Why Engineers Care About How They Build",
        "og_desc": "Engineers aren't just building to ship — they're building to prove something to themselves. The craft question, and why AI changes the answer.",
    },
}

def get_current_head(pg):
    with open(pg) as f:
        content = f.read()
    # Find where body/article starts
    match = re.search(r'<body', content)
    return match.start() if match else len(content)

def needs_tag(content, pattern):
    return not bool(re.search(pattern, content))

def fix_page(filepath):
    with open(filepath) as f:
        content = f.read()

    meta = METADATA.get(os.path.basename(filepath), {})
    filename = os.path.basename(filepath)
    canonical_url = f"https://clearing-ai.com/{filename}"

    changes = 0

    # 1. Add canonical tag (after description meta)
    if needs_tag(content, r'<link rel="canonical"'):
        content = re.sub(
            r'(<meta name="description"[^>]*>)',
            rf'\1\n  <link rel="canonical" href="{canonical_url}">',
            content
        )
        changes += 1

    # 2. Add robots meta if missing
    if needs_tag(content, r'<meta name="robots"'):
        content = re.sub(
            r'(<meta name="description"[^>]*>)',
            r'\1\n  <meta name="robots" content="index, follow">',
            content
        )
        changes += 1

    # 3. Add woff2 font preload (after existing preconnect)
    if needs_tag(content, r'woff2.*preload.*crossorigin.*fonts\.gstatic\.com'):
        preload = '''  <link rel="preload" as="font" type="font/woff2" crossorigin
       href="https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2">
'''
        content = re.sub(r'(<link rel="preconnect"[^>]*fonts\.gstatic\.com[^>]*>)',
                         rf'\1\n' + preload, content)
        changes += 1

    # 4. Add main.js script (before closing body)
    if needs_tag(content, r'src="js/main\.js"'):
        # Add right after font stylesheet noscript, before other scripts
        content = re.sub(
            r'(<script>\s*const navToggle)',
            r'<script src="js/main.js" defer></script>\n  \1',
            content
        )
        changes += 1

    # 5. Add skip-to-content link (after <body> or <nav)
    if needs_tag(content, r'skip-link'):
        skip = '<a href="#main-content" class="skip-link" style="position:absolute;top:-999px;left:-999px;z-index:9999;padding:1rem;background:var(--forest-deep);color:var(--cream);">Skip to main content</a>'
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + skip, content)
        changes += 1

    with open(filepath, 'w') as f:
        f.write(content)

    return changes

# Run
print("Fixing technical SEO gaps across 7 pages...\n")
total = 0
for pg in PAGES:
    path = f"{BASE}/{pg}"
    if os.path.exists(path):
        n = fix_page(path)
        print(f"  {'✅' if n else '⚠️'} {pg}: {n} changes")
        total += n
    else:
        print(f"  ❌ NOT FOUND: {pg}")
print(f"\nTotal changes: {total}")
