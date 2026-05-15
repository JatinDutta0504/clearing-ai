#!/usr/bin/env python3
import re, os

# Pages with missing <meta name="description"> tag (only og: and twitter: exist)
# Also fix descriptions that are too long/short

fixes_needed = {
    'signs-ai-fatigue.html': {
        'desc': '10 signs of AI fatigue in software engineers with interactive self-assessment. Identifies whether you are experiencing AI fatigue, burnout, or both and what to do next.',
        'title': None
    },
    'ai-detox-plan.html': {
        'desc': '30-day structured AI detox plan for software engineers: week-by-week phases, daily practices, no-AI challenges, and gradual reintroduction to rebuild craft and confidence.',
        'title': '30-Day AI Detox Plan for Engineers | The Clearing'
    },
    'ai-fatigue.html': {
        'desc': 'The complete guide to AI fatigue: symptoms, causes, the science behind it, and actionable recovery strategies for software engineers who want to reclaim their craft.',
        'title': None
    },
    'recovery.html': {
        'desc': 'How to recover from AI fatigue: 7-phase plan, daily practices, manager conversation scripts, and evidence-based strategies for engineers experiencing AI-related exhaustion.',
        'title': None
    },
    'burnout-vs-fatigue.html': {
        'desc': 'AI fatigue vs burnout: the key differences, which one you are experiencing, and separate recovery paths for each. Includes an interactive diagnostic quiz.',
        'title': None
    },
    'developer-burnout-2025.html': {
        'desc': 'Developer burnout in 2025: burnout rates, top causes for software engineers, and evidence-based recovery strategies. Includes data on AI role and practical guide.',
        'title': 'Developer Burnout in 2025: Causes, Rates & Recovery | The Clearing'
    },
    'ai-tool-overload.html': {
        'desc': 'Why too many AI tools paralyze engineers: the psychology of tool overload, evaluation debt, and a commitment framework to choose and stick with your tools.',
        'title': 'AI Tool Overload: Why More Tools Mean Less Progress | The Clearing'
    },
    'ai-tool-overload.html': {
        'desc': 'Why too many AI tools paralyze engineers: the psychology of tool overload, evaluation debt, and a commitment framework to choose and stick with your tools.',
        'title': 'AI Tool Overload: Why More Tools Mean Less Progress | The Clearing'
    },
    'skill-atrophy.html': {
        'desc': 'How AI quietly erodes software engineering skills: the science of skill atrophy, which skills are most at risk, warning signs, and 7 evidence-based rebuild practices.',
        'title': None
    },
    'cognitive-load.html': {
        'desc': 'Cognitive load theory and AI: why AI tools increase mental load for engineers, the expertise reversal effect, and 7 strategies to protect your working memory.',
        'title': None
    },
    'imposter-syndrome-ai.html': {
        'desc': 'Why AI tools make imposter syndrome worse for engineers and how to tell if what you feel is real skill loss versus self-doubt. Diagnostic framework and recovery steps included.',
        'title': None
    },
    'tech-layoffs-ai-era.html': {
        'desc': 'Tech layoffs in the AI era: how AI adoption reshapes engineer roles, which skills provide layoff resilience, and how to navigate career uncertainty with clarity.',
        'title': None
    },
    'vibe-coding-ai-fatigue.html': {
        'desc': 'Vibe coding and AI fatigue: when prompting replaces problem-solving, what it costs your skills, and how to use AI coding assistants without losing engineering judgment.',
        'title': None
    },
    'ai-learning-burnout.html': {
        'desc': 'AI learning burnout: why keeping up with AI tools leaves engineers exhausted and unable to retain knowledge. Includes the Constrained Learning Framework and recovery steps.',
        'title': 'AI Learning Burnout: The Cost of Constantly Keeping Up | The Clearing'
    },
    'ai-fatigue-in-2026.html': {
        'desc': 'AI fatigue in 2026: escalating AI dependency in engineers, compounding effects on skills and confidence, and a practical recovery roadmap for where we are right now.',
        'title': None
    }
}

for filename, fix in fixes_needed.items():
    if not os.path.exists(filename):
        print('Missing: ' + filename)
        continue
    with open(filename, 'r', errors='ignore') as f:
        content = f.read()

    original = content

    # Check if <meta name="description"> exists
    has_desc = bool(re.search(r'<meta name="description"', content))

    if fix.get('desc'):
        if has_desc:
            # Replace existing
            content = re.sub(
                r'<meta name="description" content="[^"]*"',
                '<meta name="description" content="' + fix['desc'] + '"',
                content
            )
        else:
            # Insert after <meta name="robots" or before og:tags
            insert_after = re.search(r'<meta name="robots"[^>]*>', content)
            if insert_after:
                desc_tag = '\n  <meta name="description" content="' + fix['desc'] + '" />'
                content = content[:insert_after.end()] + desc_tag + content[insert_after.end():]
            else:
                # Insert before og:title
                content = re.sub(
                    r'(<meta property="og:title")',
                    '<meta name="description" content="' + fix['desc'] + '" />\n  \1',
                    content,
                    count=1
                )

    # Fix title if specified
    if fix.get('title'):
        content = re.sub(r'<title>[^<]+</title>', '<title>' + fix['title'] + '</title>', content, count=1)

    # Add twitter if missing (and og:title exists)
    if 'twitter:title' not in content:
        og_t = re.search(r'<meta property="og:title" content="([^"]+)"', content)
        og_d = re.search(r'<meta property="og:description" content="([^"]+)"', content)
        if og_t:
            tw = '\n  <meta name="twitter:title" content="' + og_t.group(1) + '" />'
            if og_d:
                tw += '\n  <meta name="twitter:description" content="' + og_d.group(1) + '" />'
            content = content.replace('</head>', tw + '\n  </head>', 1)

    if content != original:
        with open(filename, 'w') as f:
            f.write(content)
        print('Fixed: ' + filename)
    else:
        print('No change: ' + filename)