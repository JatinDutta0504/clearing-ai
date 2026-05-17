#!/usr/bin/env python3
"""Improved meta audit — check actual meta tag presence."""

import os
import re

SITE_DIR = os.path.expanduser("~/Desktop/TheClearing")

PAGES = [
    "ai-detox-plan.html","team-manager-guide.html","daily-ai-boundaries.html",
    "corporate-ai-wellness.html","developer-burnout-2025.html","software-engineer-mental-health.html",
    "tech-layoffs-ai-era.html","imposter-syndrome-ai.html","ai-tool-overload.html",
    "ai-learning-burnout.html","coding-ai-tools-comparison.html","ai-fatigue-in-2026.html",
    "ai-fatigue-severity-index.html","ai-anxiety.html","vibe-coding.html",
    "the-ai-skill-stack.html","recovery-toolkit.html","developer-wellbeing.html",
    "daily-practice.html","checkin.html","engineer-survey-results.html",
    "ai-fatigue-statistics-2025.html","the-science-of-ai-fatigue.html","junior-engineers.html",
    "senior-identity.html","workplace.html","hiring.html","remote-work-ai-fatigue.html",
    "community-hub.html","attention-residue.html","flow-state.html","productivity-theater.html",
    "cognitive-load.html","skill-atrophy.html","automation-anxiety.html","developer-identity.html",
    "compare.html","stats.html","research.html","manifesto.html","handbook.html",
]

for page in PAGES:
    path = os.path.join(SITE_DIR, page)
    if not os.path.exists(path):
        print(f"❌ {page} — NOT FOUND")
        continue
    with open(path) as f:
        c = f.read()
    
    has_desc = bool(re.search(r'<meta name="description"', c))
    has_og_title = bool(re.search(r'<meta property="og:title"', c))
    has_og_desc = bool(re.search(r'<meta property="og:description"', c))
    has_og_img = bool(re.search(r'<meta property="og:image"', c))
    has_tw_card = bool(re.search(r'<meta name="twitter:card"', c))
    has_canon = bool(re.search(r'<link rel="canonical"', c))
    
    all_ok = has_desc and has_og_title and has_og_desc and has_og_img and has_tw_card and has_canon
    
    if all_ok:
        print(f"✅ {page}")
    else:
        missing = []
        if not has_desc: missing.append("desc")
        if not has_og_title: missing.append("og:title")
        if not has_og_desc: missing.append("og:desc")
        if not has_og_img: missing.append("og:image")
        if not has_tw_card: missing.append("tw:card")
        if not has_canon: missing.append("canonical")
        print(f"⚠️  {page} — MISSING: {', '.join(missing)}")