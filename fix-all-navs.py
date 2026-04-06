#!/usr/bin/env python3
"""
Fix nav corruption in all HTML pages.
Target: <ul class="nav-links">...</ul> — replace with clean version.
Preserves: <nav>, header div, nav-logo, nav-toggle, nav-cta, </nav>, </header>
"""

import re, os

SITE = "/Users/nightcoder/Desktop/TheClearing"

CLEAN_NAV_LINKS = '''        <li><a href="index.html" class="nav-link">Home</a></li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger" aria-haspopup="true" aria-expanded="false">Why <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="why.html">Why AI Fatigue?</a></li>
            <li><a href="burnout-vs-fatigue.html">Burnout vs Fatigue</a></li>
            <li><a href="developer-burnout-2025.html">Developer Burnout 2025</a></li>
            <li><a href="tech-layoffs-ai-era.html">Tech Layoffs &amp; AI</a></li>
            <li><a href="compare.html">Compare Tools</a></li>
            <li><a href="ai-tool-overload.html">Tool Overload</a></li>
            <li><a href="coding-ai-tools-comparison.html">Coding Tools Comparison</a></li>
            <li><a href="ai-learning-burnout.html">AI Learning Burnout</a></li>
            <li><a href="ai-code-review.html">AI Code Review</a></li>
            <li><a href="the-science-of-ai-fatigue.html">The Science of AI Fatigue</a></li>
            <li><a href="research.html">Research</a></li>
            <li><a href="stats.html">Statistics 2025</a></li>
            <li><a href="productivity-theater.html">Productivity Theater</a></li>
            <li><a href="flow-state.html">Flow State &amp; AI</a></li>
            <li><a href="attention-residue.html">Attention Residue</a></li>
            <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
            <li><a href="cognitive-load.html">Cognitive Load</a></li>
            <li><a href="developer-identity.html">Developer Identity</a></li>
            <li><a href="automation-anxiety.html">Automation Anxiety</a></li>
            <li><a href="imposter-syndrome-vs-ai-fatigue.html">Imposter Syndrome</a></li>
            <li><a href="imposter-syndrome-ai.html">Imposter Syndrome &amp; AI</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger" aria-haspopup="true" aria-expanded="false">Heal <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="mental-health.html">Mental Health</a></li>
            <li><a href="developer-wellbeing.html">Wellbeing</a></li>
            <li><a href="tips.html">Tips</a></li>
            <li><a href="mindset.html">Mindset</a></li>
            <li><a href="daily-practice.html">Daily Practice</a></li>
            <li><a href="ai-fatigue-checklist.html">30-Day Checklist</a></li>
            <li><a href="ai-detox-plan.html">30-Day Detox Plan</a></li>
            <li><a href="workplace.html">Workplace</a></li>
            <li><a href="team-guide.html">For Managers</a></li>
            <li><a href="hiring.html">Hiring &amp; Retention</a></li>
            <li><a href="corporate-ai-wellness.html">Corporate Wellness</a></li>
            <li><a href="daily-ai-boundaries.html">Daily AI Boundaries</a></li>
            <li><a href="team-manager-guide.html">Team Manager Guide</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger" aria-haspopup="true" aria-expanded="false">Stories <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="stories.html">Engineer Stories</a></li>
            <li><a href="engineer-types.html">Your Type</a></li>
            <li><a href="junior-engineers.html">For Juniors</a></li>
            <li><a href="senior-identity.html">Senior Identity</a></li>
            <li><a href="community.html">Community</a></li>
            <li><a href="glossary.html">Glossary</a></li>
            <li><a href="faq.html">FAQ</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger" aria-haspopup="true" aria-expanded="false">Tools <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="index.html#quiz">Fatigue Quiz</a></li>
            <li><a href="checkin.html">Daily Check-in</a></li>
            <li><a href="decompress.html">Decompress</a></li>
            <li><a href="journal.html">Journal</a></li>
            <li><a href="badge.html">Fatigue Badge</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger" aria-haspopup="true" aria-expanded="false">Read <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="resources.html">Resources</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
            <li><a href="newsletter-thank-you.html">Thank You</a></li>
            <li><a href="quiz-results.html">Quiz Results</a></li>
            <li><a href="quiz-results-tier-4.html">Tier 4 Results</a></li>
            <li><a href="quiz-results-tier-3.html">Tier 3 Results</a></li>
            <li><a href="press-kit.html">Press Kit</a></li>
            <li><a href="changelog.html">Changelog</a></li>
          </ul>
        </li>
        <li><a href="about.html" class="nav-link">About</a></li>'''

html_files = [os.path.join(SITE, f) for f in os.listdir(SITE)
              if f.endswith(".html") and not f.startswith("lh-")]

print(f"Scanning {len(html_files)} HTML files...")

fixed = 0
skipped = 0
errors = []

for filepath in sorted(html_files):
    fname = os.path.basename(filepath)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if 'class="nav-links"' not in content:
            skipped += 1
            continue

        # Match the ENTIRE <ul class="nav-links">...</ul> block
        # We look for: <ul class="nav-links"> then anything until </ul> that is followed by nav-cta or </nav>
        # Use a non-greedy match but make sure we get the right </ul>
        pattern = r'(<ul class="nav-links">)\s*(.*?)\s*(</ul>)(\s*\n\s*<a href="index\.html#quiz" class="nav-cta">)'

        m = re.search(pattern, content, re.DOTALL)

        if m:
            # Check if the captured content looks corrupted (has floating li, bad nesting)
            old_inner = m.group(2)
            # If it has patterns like: </li></li> or <li> not inside <ul> or duplicate entries
            has_corruption = (
                '</li></li>' in old_inner or
                '<li><a href="mental-health.html"></li>' in old_inner or
                old_inner.count('<li><a href="the-science-of-ai-fatigue.html">') > 1 or
                '<a href="daily-ai-boundaries.html">' in old_inner and '</li>' not in old_inner.split('<a href="daily-ai-boundaries.html">')[-1]
            )

            if has_corruption or len(old_inner) > 5000:  # definitely corrupted if >5k chars (should be ~3k)
                new_block = m.group(1) + '\n' + CLEAN_NAV_LINKS + '\n      ' + m.group(3) + m.group(4)
                new_content = content[:m.start()] + new_block + content[m.end():]
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                fixed += 1
                print(f"  ✅ {fname} ({len(old_inner)}→{len(CLEAN_NAV_LINKS)} chars)")
            else:
                print(f"  ⚠️  nav ok but large ({len(old_inner)} chars), skipping: {fname}")
                skipped += 1
        else:
            # Try to find nav-links and see what's there
            idx = content.find('class="nav-links"')
            if idx >= 0:
                # show 200 chars after
                snippet = content[idx:idx+300]
                print(f"  ❓ unusual format in {fname}: ...{snippet[:150]}...")
            skipped += 1
    except Exception as e:
        errors.append((fname, str(e)))
        print(f"  ERROR {fname}: {e}")

print(f"\nResults: {fixed} fixed, {skipped} ok/skipped, {len(errors)} errors")
if errors:
    for f, e in errors:
        print(f"  ERROR: {f}: {e}")
