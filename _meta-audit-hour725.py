#!/usr/bin/env python3
"""Audit meta tags on The Clearing pages — find missing OG/Twitter/canonical/description."""

import os
import re
import glob

SITE_DIR = os.path.expanduser("~/Desktop/TheClearing")

# Pages to audit (most likely to have issues = newer/underchecked pages)
TARGET_PAGES = [
    # New recent pages
    "ai-detox-plan.html",
    "team-manager-guide.html",
    "daily-ai-boundaries.html",
    "corporate-ai-wellness.html",
    # Underserved pillars
    "developer-burnout-2025.html",
    "software-engineer-mental-health.html",
    "tech-layoffs-ai-era.html",
    "imposter-syndrome-ai.html",
    # Existing pillars checked in last audit may have drifted
    "ai-tool-overload.html",
    "ai-learning-burnout.html",
    "coding-ai-tools-comparison.html",
    # Underchecked recent adds
    "ai-fatigue-in-2026.html",
    "ai-fatigue-severity-index.html",
    "ai-anxiety.html",
    "vibe-coding.html",
    "career-pivot.html",
    "the-ai-skill-stack.html",
    # Recovery pages
    "recovery-toolkit.html",
    "developer-wellbeing.html",
    "daily-practice.html",
    "checkin.html",
    # Research
    "engineer-survey-results.html",
    "ai-fatigue-statistics-2025.html",
    "the-science-of-ai-fatigue.html",
    # Role-specific pages
    "junior-engineers.html",
    "senior-identity.html",
    "workplace.html",
    "hiring.html",
    # Newer content
    "remote-work-ai-fatigue.html",
    "community-hub.html",
    "attention-residue.html",
    "flow-state.html",
    "productivity-theater.html",
    "cognitive-load.html",
    "skill-atrophy.html",
    "automation-anxiety.html",
    "developer-identity.html",
    # Others
    "compare.html",
    "stats.html",
    "research.html",
    "manifesto.html",
    "handbook.html",
]

results = []

for page_name in TARGET_PAGES:
    path = os.path.join(SITE_DIR, page_name)
    if not os.path.exists(path):
        results.append({"page": page_name, "status": "NOT FOUND"})
        continue
    
    with open(path, "r") as f:
        content = f.read()
    
    issues = []
    
    # Check description
    desc_match = re.search(r'<meta name="description" content="([^"]{1,50})"', content)
    if not desc_match:
        issues.append("MISSING description meta tag")
    elif len(desc_match.group(1)) < 120:
        issues.append(f"SHORT description ({len(desc_match.group(1))} chars)")
    
    # Check og:title
    if not re.search(r'<meta property="og:title"', content):
        issues.append("MISSING og:title")
    
    # Check og:description
    if not re.search(r'<meta property="og:description"', content):
        issues.append("MISSING og:description")
    
    # Check og:image
    if not re.search(r'<meta property="og:image"', content):
        issues.append("MISSING og:image")
    
    # Check twitter:card
    if not re.search(r'<meta name="twitter:card"', content):
        issues.append("MISSING twitter:card")
    
    # Check canonical
    if not re.search(r'<link rel="canonical"', content):
        issues.append("MISSING canonical")
    
    if issues:
        results.append({"page": page_name, "issues": issues, "status": "ISSUES"})
    else:
        results.append({"page": page_name, "issues": [], "status": "OK"})

# Print summary
print("=== META AUDIT RESULTS ===\n")
ok_count = 0
issue_count = 0
for r in results:
    if r["status"] == "NOT FOUND":
        print(f"❌ {r['page']} — FILE NOT FOUND")
    elif r["status"] == "OK":
        print(f"✅ {r['page']} — all meta tags present")
        ok_count += 1
    else:
        print(f"⚠️  {r['page']} — {' | '.join(r['issues'])}")
        issue_count += 1

print(f"\n=== SUMMARY ===")
print(f"OK: {ok_count}")
print(f"ISSUES: {issue_count}")
print(f"TOTAL: {len(results)}")