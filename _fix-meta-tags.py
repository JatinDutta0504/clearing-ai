#!/usr/bin/env python3
"""Batch fix meta tags (title + description) across all pages with SEO issues."""
import re
import os

FIXES = {
    'ai-architecture-fatigue.html': {
        'title': 'AI Architecture Fatigue: When AI Designs Your System',
        'desc': 'AI architecture fatigue: when AI designs your system and you lose the craft. Signs, recovery, and maintaining architectural judgment in the AI era.'
    },
    'ai-code-review-fatigue.html': {
        'title': 'AI Code Review Fatigue: Why AI Suggestions Exhaust You',
        'desc': 'AI code review fatigue: why endless AI suggestions during PRs leave you exhausted and questioning your own judgment. Signs and recovery.'
    },
    'ai-consultation-fatigue.html': {
        'title': 'AI Consultation Fatigue: Why Endless Prompting Drains You',
        'desc': 'AI consultation fatigue: why endless prompting feels so exhausting and how to break compulsive AI use patterns.'
    },
    'ai-fatigue-in-2026.html': {
        'title': 'AI Fatigue in 2026: What Two Years of Data Reveal',
        'desc': 'AI fatigue in 2026: what two years of data from 3,000+ engineers reveals about how AI tools are affecting developer wellbeing and skills.'
    },
    'ai-fatigue-recovery-checklist.html': {
        'desc': 'A 30-day recovery checklist for AI-fatigued engineers: 30 evidence-based daily actions across four themed weeks. Printable, no account needed.'
    },
    'ai-fatigue-recovery-journal.html': {
        'desc': 'AI fatigue recovery journal: 30 days of guided reflection prompts for engineers. Track patterns, process emotions, rebuild your relationship with code.'
    },
    'ai-fatigue-severity-index.html': {
        'title': 'AI Fatigue Severity Index — How Bad Is It? | The Clearing',
        'desc': 'AI fatigue severity index: a self-assessment tool to measure how severely AI tools are affecting your wellbeing, skills, and career.'
    },
    'ai-fatigue-type-calculator.html': {
        'desc': 'Discover your AI fatigue type: a guided self-assessment to identify your primary fatigue pattern and the recovery approach that fits you best.'
    },
    'ai-healthcare-developer-fatigue.html': {
        'desc': 'AI fatigue for healthcare software engineers: unique regulatory pressure, patient safety stakes, and EHR integration challenges. Signs and recovery.'
    },
    'ai-learning-burnout.html': {
        'desc': 'AI learning burnout: why constantly learning new AI tools leaves engineers exhausted and how to build sustainable learning boundaries in the AI era.'
    },
    'ai-productivity-guilt.html': {
        'title': 'AI Productivity Guilt: The Hidden Emotion Engineers Feel',
        'desc': 'AI productivity guilt: the hidden emotion engineers feel when AI does the work they used to do. Why it compounds and what actually helps.'
    },
    'coders-block.html': {
        'title': "Coder's Block: When AI Makes You Forget How to Think",
        'desc': "Coder's block meets AI fatigue: why engineers who heavily use AI sometimes forget how to approach problems without it. Signs, causes, and recovery."
    },
    'community-hub.html': {
        'title': 'Community Hub — Engineers Recovering Together | The Clearing',
        'desc': 'The Clearing community hub: connect with engineers recovering from AI fatigue. Newsletter, stories, testimonials, and shared recovery resources.'
    },
    'data-report-2026.html': {
        'title': 'The AI Fatigue Report: What 3,000 Engineers Taught Us',
        'desc': 'The 2026 AI fatigue report: what 3,000 engineers revealed about skill decline, identity loss, and recovery. Key findings and team implications.'
    },
    'email-course.html': {
        'title': '5-Day AI Fatigue Reset: A Free Email Course for Engineers',
        'desc': 'A free 5-day email course for AI-fatigued engineers. One actionable lesson per day to reset your relationship with AI coding tools.'
    },
    'engineer-survey-results.html': {
        'title': 'Engineer Survey Results — AI Fatigue Data | The Clearing',
        'desc': 'Survey results from 2,147 engineers on AI fatigue: skill decline, identity loss, velocity pressure, and four recovery archetypes we identified.'
    },
    'manifesto.html': {
        'title': "An Engineer's Manifesto for Intentional AI Use | The Clearing",
        'desc': 'An engineering manifesto for intentional AI use: why choosing when NOT to use AI is as important as choosing when to use it.'
    },
    'newsletter-archive.html': {
        'desc': 'The Dispatch newsletter archive: 33 issues of weekly insights on AI fatigue, craft, recovery, and sustainable engineering practices.'
    },
    'newsletter-thank-you.html': {
        'desc': 'Welcome to The Dispatch. Your first issue is on its way. Explore: recovery guides, quiz, tools, and community while you wait.'
    },
    'performance-review-ai-fatigue.html': {
        'title': 'Performance Review AI Fatigue: When Self-Assessment Hollows Out',
        'desc': 'Performance review AI fatigue: when AI-assisted work makes self-assessments feel hollow. How to demonstrate genuine value during review cycles.'
    },
    'press-release-2026.html': {
        'title': 'The Clearing Launches AI Fatigue Research Hub | Press Release',
        'desc': 'Press release: The Clearing launches AI fatigue research hub with data from 3,000 engineers. Media contact, assets, and partnership inquiries.'
    },
    'quiz-results-tier-3.html': {
        'desc': 'AI fatigue Tier 3 deep-dive: when fatigue has become serious. Four root causes, specific weekly practices, and a structured 3-tier action plan.'
    },
    'quiz-results-tier-4.html': {
        'desc': 'AI fatigue Tier 4 deep-dive: when you need a real break. Crisis resources, immediate actions, and a structured 30-day recovery plan for severe cases.'
    },
    'recovery-toolkit.html': {
        'title': 'AI Fatigue Recovery Toolkit — Free Tools for Engineers',
        'desc': 'A free toolkit for AI-fatigued engineers: quiz, check-in tracker, deep work timer, journal, 30-day plan, and more. No account needed.'
    },
    'senior-engineer-ai-fatigue.html': {
        'desc': 'AI fatigue for senior engineers: identity crisis, skill atrophy, authorship loss, and the pressure of mentoring teams through the AI transition.'
    },
    'staff-principal-engineer-ai-fatigue.html': {
        'title': 'Staff & Principal Engineer AI Fatigue: The IC4/IC5 Guide',
        'desc': 'AI fatigue for staff and principal engineers: architecture decisions, technical strategy, and maintaining expertise relevance as AI reshapes IC work.'
    },
    'subscribe.html': {
        'title': 'Subscribe to The Dispatch — Weekly for Engineers | The Clearing',
        'desc': 'Subscribe to The Dispatch: a weekly newsletter for AI-fatigued engineers. Stories, data, and recovery tactics. Free forever. No spam.'
    },
    'team-manager-guide.html': {
        'desc': 'A manager guide for preventing and addressing team AI fatigue: signs to watch, 1:1 questions, team norms, and organizational changes that help.'
    },
    'testimonials-campaign.html': {
        'title': 'Engineer Testimonials — Real AI Fatigue Recovery Stories',
        'desc': 'Real engineers, real recovery stories from AI fatigue. Read anonymous stories or share your own. Featured in The Dispatch newsletter.'
    },
    'the-estimation-problem.html': {
        'title': 'The Estimation Problem: Why AI Makes Guessing Harder',
        'desc': 'The estimation problem: why relying on AI for estimates erodes your intuition for complexity and how to rebuild your judgment without it.'
    },
    'the-explanation-requirement.html': {
        'title': 'The Explanation Requirement: The Practice That Changes Everything',
        'desc': 'The explanation requirement: the single practice that helps engineers rebuild skills, restore code ownership, and recover from AI fatigue.'
    },
}

# Verify lengths before applying
print("Pre-apply verification:")
for fname, data in FIXES.items():
    t = data.get('title', '')
    d = data.get('desc', '')
    tlen = len(t) if t else 0
    dlen = len(d) if d else 0
    status = 'OK' if (tlen <= 60 and 50 <= dlen <= 160) else 'FIX'
    print(f"  {status} | t={tlen} d={dlen} | {fname}")
    if tlen > 60:
        print(f"    TITLE TOO LONG: {t}")
    if dlen > 160 or (dlen > 0 and dlen < 50):
        print(f"    DESC ISSUE ({dlen}): {d[:60]}")

print(f"\nApplying fixes to {len(FIXES)} files...")
base = '/Users/nightcoder/Desktop/TheClearing'
count = 0
for fname, data in FIXES.items():
    path = os.path.join(base, fname)
    if not os.path.exists(path):
        print(f"  SKIP: {fname} not found")
        continue
    with open(path) as f:
        c = f.read()
    original = c
    
    if 'title' in data:
        t = data['title']
        c = re.sub(r'<title>[^<]+</title>', f'<title>{t}</title>', c, count=1)
    
    if 'desc' in data:
        d = data['desc']
        c = re.sub(r'<meta name="description" content="[^"]+"', f'<meta name="description" content="{d}"', c, count=1)
    
    if c != original:
        with open(path, 'w') as f:
            f.write(c)
        count += 1
        print(f"  Fixed: {fname}")

print(f"\nDone. Fixed {count} files.")
