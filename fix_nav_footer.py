#!/usr/bin/env python3
"""
Fix nav and footer across all HTML files in TheClearing.
"""
import os
import re

BASE = os.path.expanduser("~/Desktop/TheClearing")

NEW_NAV = '''  <nav class="main-nav" role="navigation" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo">🌿 The Clearing</a>
      <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
      <ul class="nav-links">
        <li><a href="index.html" class="nav-link">Home</a></li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger">Why <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="why.html">Why AI Fatigue?</a></li>
            <li><a href="burnout-vs-fatigue.html">Burnout vs Fatigue</a></li>
            <li><a href="compare.html">Compare Tools</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger">Heal <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="tips.html">Tips</a></li>
            <li><a href="mindset.html">Mindset</a></li>
            <li><a href="daily-practice.html">Daily Practice</a></li>
            <li><a href="team-guide.html">For Managers</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger">Stories <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="stories.html">Engineer Stories</a></li>
            <li><a href="engineer-types.html">Your Type</a></li>
            <li><a href="glossary.html">Glossary</a></li>
            <li><a href="faq.html">FAQ</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger">Tools <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="index.html#quiz">Fatigue Quiz</a></li>
            <li><a href="decompress.html">Decompress</a></li>
            <li><a href="journal.html">Journal</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <button class="nav-link dropdown-trigger">Read <span class="dropdown-arrow">▾</span></button>
          <ul class="dropdown-menu">
            <li><a href="resources.html">Resources</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
          </ul>
        </li>
        <li><a href="about.html" class="nav-link">About</a></li>
      </ul>
      <a href="index.html#quiz" class="nav-cta">Take Quiz →</a>
    </div>
  </nav>'''

NEW_FOOTER = '''  <footer class="footer" role="contentinfo">
    <p class="footer-logo">🌿 The Clearing</p>
    <p class="footer-tagline">"Your brain is not a GPU."</p>
    <ul class="footer-nav" role="list">
      <li><a href="index.html">Home</a></li>
      <li><a href="why.html">Why AI Fatigue?</a></li>
      <li><a href="burnout-vs-fatigue.html">Burnout vs Fatigue</a></li>
      <li><a href="compare.html">Compare Tools</a></li>
      <li><a href="recovery.html">Recovery</a></li>
      <li><a href="tips.html">Tips</a></li>
      <li><a href="mindset.html">Mindset</a></li>
      <li><a href="stories.html">Stories</a></li>
      <li><a href="glossary.html">Glossary</a></li>
      <li><a href="decompress.html">Decompress</a></li>
      <li><a href="journal.html">Journal</a></li>
      <li><a href="resources.html">Resources</a></li>
      <li><a href="newsletter.html">Newsletter</a></li>
      <li><a href="about.html">About</a></li>
    </ul>
    <p class="footer-copy">Made by a few engineers who needed this. No tracking. No data. Just a clearing in the woods.</p>
  </footer>'''

# Files to skip (404, or ones with no nav placeholder)
SKIP = {'404.html'}

html_files = [f for f in os.listdir(BASE) if f.endswith('.html') and f not in SKIP]

for filename in sorted(html_files):
    path = os.path.join(BASE, filename)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()

    original = content

    # --- Replace the main nav ---
    # The main nav is class="nav" — replace it with class="main-nav"
    # Match from <nav class="nav" ... to the matching </nav>
    # We'll use a regex that captures the outermost nav.class="nav"
    
    # Pattern: <nav class="nav"...>...</nav> (non-greedy won't work, use a counter approach via re.sub with a function)
    # Simple approach: find first occurrence of <nav class="nav" and the matching </nav>
    
    nav_start_pat = re.compile(r'<nav\s+class="nav"[^>]*>', re.DOTALL)
    m = nav_start_pat.search(content)
    if m:
        start = m.start()
        # Find matching </nav> by counting depth
        pos = m.end()
        depth = 1
        while depth > 0 and pos < len(content):
            next_open = content.find('<nav', pos)
            next_close = content.find('</nav>', pos)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 4
            else:
                depth -= 1
                if depth == 0:
                    end = next_close + len('</nav>')
                else:
                    pos = next_close + len('</nav>')
        content = content[:start] + NEW_NAV + content[end:]
        print(f"  [NAV] Replaced nav in {filename}")
    else:
        print(f"  [NAV] No .nav found in {filename}, skipping nav replacement")

    # --- Replace the main footer ---
    # Match <footer class="footer" ...>...</footer>
    footer_pat = re.compile(r'<footer\s+class="footer"[^>]*>', re.DOTALL)
    mf = footer_pat.search(content)
    if mf:
        start = mf.start()
        pos = mf.end()
        depth = 1
        while depth > 0 and pos < len(content):
            next_open = content.find('<footer', pos)
            next_close = content.find('</footer>', pos)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 7
            else:
                depth -= 1
                if depth == 0:
                    end = next_close + len('</footer>')
                else:
                    pos = next_close + len('</footer>')
        content = content[:start] + NEW_FOOTER + content[end:]
        print(f"  [FOOTER] Replaced footer in {filename}")
    else:
        # Some pages (like why.html) have no footer.class="footer" — inject before </body>
        if '</body>' in content and '<footer' not in content:
            content = content.replace('</body>', NEW_FOOTER + '\n</body>', 1)
            print(f"  [FOOTER] Injected footer before </body> in {filename}")
        else:
            # Check for inline footer with style= (compare.html, mindset.html)
            inline_footer = re.search(r'<footer\s+style=[^>]*>.*?</footer>', content, re.DOTALL)
            if inline_footer:
                content = content[:inline_footer.start()] + NEW_FOOTER + content[inline_footer.end():]
                print(f"  [FOOTER] Replaced inline-style footer in {filename}")
            else:
                print(f"  [FOOTER] No footer found in {filename}")

    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f"  [SAVED] {filename}")
    else:
        print(f"  [SKIP] No changes in {filename}")

print("\nDone!")
