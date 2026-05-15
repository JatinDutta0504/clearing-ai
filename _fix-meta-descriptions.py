#!/usr/bin/env python3
import re

fixes = {
    'index.html': {
        'desc': 'Free AI fatigue recovery resources for software engineers. Quiz, recovery plans, daily practices, and community support to help you regain clarity and confidence.',
        'title': None,
        'add_twitter': False,
        'add_faq': True
    },
    'ai-fatigue.html': {
        'desc': 'The complete guide to AI fatigue in software engineers: symptoms, causes, science, and actionable recovery strategies. Built for engineers who want to reclaim their craft.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'recovery.html': {
        'desc': 'How to recover from AI fatigue: 7-phase plan, daily practices, manager scripts, and evidence-based strategies for engineers experiencing AI-related burnout and exhaustion.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'burnout-vs-fatigue.html': {
        'desc': 'AI fatigue vs burnout: what\'s the real difference, which are you experiencing, and what actually helps. Includes a diagnostic quiz and separate recovery paths for each.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'signs-ai-fatigue.html': {
        'desc': '10 signs you have AI fatigue plus what each one means and what to do about it. Includes an interactive self-assessment and recovery recommendations for each signal.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'compare.html': {
        'desc': 'Honest comparison of AI coding tools (Copilot, Cursor, ChatGPT, Codeium): which causes the most fatigue, why, and how to use them without eroding your skills.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'developer-burnout-2025.html': {
        'desc': 'Software engineer burnout rates, top causes, and evidence-based recovery strategies for 2025. Includes data on AI role in engineer burnout and a practical recovery guide.',
        'title': 'Developer Burnout in 2025: Rates, Causes & Recovery | The Clearing',
        'add_twitter': False,
        'add_faq': False
    },
    'ai-tool-overload.html': {
        'desc': 'Why too many AI tools paralyze engineers: the psychology of tool overload, evaluation debt, and a practical commitment framework to choose and stick with your tools.',
        'title': 'AI Tool Overload: Why More Tools Mean Less Progress | The Clearing',
        'add_twitter': True,
        'add_faq': False
    },
    'ai-detox-plan.html': {
        'desc': '30-day AI detox plan for engineers: structured weekly phases, daily practices, no-AI challenges, and gradual reintroduction framework to rebuild your craft and confidence.',
        'title': '30-Day AI Detox Plan for Engineers | The Clearing',
        'add_twitter': False,
        'add_faq': False
    },
    'skill-atrophy.html': {
        'desc': 'How AI quietly erodes software engineering skills: the science of skill atrophy, which skills are most at risk, warning signs, and 7 evidence-based rebuild practices.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'cognitive-load.html': {
        'desc': 'Cognitive load theory and AI: why AI tools increase mental load instead of reducing it, the expertise reversal effect, and 7 strategies to protect your working memory.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'imposter-syndrome-ai.html': {
        'desc': 'Why AI tools make imposter syndrome worse for engineers and how to tell if what you feel is real skill loss versus self-doubt. Includes diagnostic framework and recovery steps.',
        'title': None,
        'add_twitter': True,
        'add_faq': False
    },
    'tech-layoffs-ai-era.html': {
        'desc': 'Tech layoffs in the AI era: how AI adoption reshapes software engineer roles, which skills provide layoff resilience, and how to navigate career uncertainty with clarity.',
        'title': 'Tech Layoffs and AI: Building Layoff Resilience | The Clearing',
        'add_twitter': False,
        'add_faq': False
    },
    'developer-identity.html': {
        'desc': 'The identity crisis at the heart of senior engineer AI fatigue: who are you without your code? Ghost authorship, craft loss, and a 7-step reconstruction framework.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'vibe-coding-ai-fatigue.html': {
        'desc': 'Vibe coding and AI fatigue: when prompting replaces problem-solving, what it costs your skills, and how to use AI coding assistants without losing your engineering judgment.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'ai-learning-burnout.html': {
        'desc': 'AI learning burnout: why keeping up with AI tools leaves engineers exhausted and unable to retain knowledge. Includes the Constrained Learning Framework and recovery steps.',
        'title': 'AI Learning Burnout: Why Keeping Up With AI Tools Exhausts You | The Clearing',
        'add_twitter': False,
        'add_faq': False
    },
    'ai-fatigue-in-2026.html': {
        'desc': 'AI fatigue in 2026: the escalation of AI dependency in software engineers, compounding effects on skills and confidence, and a practical recovery roadmap for right now.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    },
    'software-engineer-mental-health.html': {
        'desc': 'Software engineer mental health: how AI fatigue compounds existing burnout, when to seek professional help, therapist guides for engineers, and crisis resources.',
        'title': None,
        'add_twitter': False,
        'add_faq': False
    }
}

for filename, fix in fixes.items():
    try:
        with open(filename, 'r', errors='ignore') as f:
            content = f.read()

        # Fix description
        desc_regex = r'(<meta name="description" content=")[^"]*(")'
        if fix['desc']:
            content = re.sub(desc_regex, '\\1' + fix['desc'] + '\\2', content)

        # Fix title if specified
        if fix['title']:
            title_regex = r'(<title>)[^<]*(</title>)'
            content = re.sub(title_regex, '\\1' + fix['title'] + '\\2', content)

        # Add twitter meta if missing and flagged
        if fix.get('add_twitter') and 'twitter:title' not in content:
            og_title_m = re.search(r'<meta property="og:title" content="([^"]+)"', content)
            og_desc_m = re.search(r'<meta property="og:description" content="([^"]+)"', content)
            if og_title_m:
                t_title = og_title_m.group(1)
                t_desc = og_desc_m.group(1) if og_desc_m else ''
                twitter_block = '\n  <meta name="twitter:title" content="' + t_title + '" />\n  <meta name="twitter:description" content="' + t_desc + '" />'
                content = content.replace('</head>', twitter_block + '\n  </head>', 1)

        with open(filename, 'w') as f:
            f.write(content)

        print('Fixed: ' + filename)
    except Exception as e:
        print('Error ' + filename + ': ' + str(e))