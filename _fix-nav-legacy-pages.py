#!/usr/bin/env python3
"""
Phase 3 Technical SEO Fix: Add modern nav/footer to legacy pages
Detects pages with style.css but no modern nav, injects nav+footer blocks.
"""
import os

SITE = "/Users/nightcoder/Desktop/TheClearing"
PAGES = [f for f in os.listdir(SITE) if f.endswith(".html")]

# Modern nav/footer pattern (from properly structured pages)
MODERN_NAV = """  <!-- Navigation -->
  <nav class="site-nav" role="navigation" aria-label="Main navigation" data-injected="nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo" aria-label="The Clearing home">
        <span class="logo-icon">🌿</span>
        <span class="logo-text">The Clearing</span>
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <div class="nav-links">
        <div class="nav-dropdown">
          <button class="nav-trigger" aria-haspopup="true" aria-expanded="false">Understand ▾</button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="why.html" role="menuitem">Why It Happens</a>
            <a href="tips.html" role="menuitem">10 Signs</a>
            <a href="burnout-vs-fatigue.html" role="menuitem">Burnout vs Fatigue</a>
            <a href="glossary.html" role="menuitem">Glossary</a>
            <a href="research.html" role="menuitem">The Research</a>
            <a href="ai-fatigue.html" role="menuitem">What Is AI Fatigue</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-trigger" aria-haspopup="true" aria-expanded="false">Stories ▾</button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="stories.html" role="menuitem">Engineer Stories</a>
            <a href="share-your-story.html" role="menuitem">Share Yours</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-trigger" aria-haspopup="true" aria-expanded="false">Recover ▾</button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="recovery.html" role="menuitem">Recovery Guide</a>
            <a href="decompress.html" role="menuitem">Decompress</a>
            <a href="daily-practice.html" role="menuitem">Daily Practice</a>
            <a href="mental-health.html" role="menuitem">Mental Health</a>
          </div>
        </div>
        <div class="nav-dropdown">
          <button class="nav-trigger" aria-haspopup="true" aria-expanded="false">Tools ▾</button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="checkin.html" role="menuitem">Daily Check-in</a>
            <a href="compare.html" role="menuitem">Tool Compare</a>
            <a href="stats.html" role="menuitem">Statistics</a>
          </div>
        </div>
        <a href="newsletter.html" class="nav-item" role="menuitem">Newsletter</a>
        <a href="about.html" class="nav-item" role="menuitem">About</a>
      </div>
    </div>
  </nav>"""

MODERN_FOOTER = """  <!-- Footer -->
  <footer class="site-footer" data-injected="footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <span class="footer-logo">🌿</span>
        <p>A free resource for engineers experiencing AI fatigue. No tracking. No accounts. Just help.</p>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <h4>Understand</h4>
          <a href="why.html">Why It Happens</a>
          <a href="ai-fatigue.html">What Is AI Fatigue</a>
          <a href="burnout-vs-fatigue.html">Burnout vs Fatigue</a>
          <a href="glossary.html">Glossary</a>
        </div>
        <div class="footer-col">
          <h4>Recover</h4>
          <a href="recovery.html">Recovery Guide</a>
          <a href="decompress.html">Decompress</a>
          <a href="mental-health.html">Mental Health</a>
          <a href="community.html">Community</a>
        </div>
        <div class="footer-col">
          <h4>Tools</h4>
          <a href="checkin.html">Daily Check-in</a>
          <a href="compare.html">Tool Compare</a>
          <a href="stats.html">Statistics</a>
          <a href="newsletter.html">Newsletter</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 The Clearing · <a href="privacy.html">Privacy</a> · <a href="manifesto.html">Manifesto</a></p>
      </div>
    </div>
  </footer>
  <script src="js/main.min.js" defer></script>
  <script>
    // Minimal nav toggle for legacy pages
    document.addEventListener('DOMContentLoaded', function() {
      var toggle = document.querySelector('.nav-toggle');
      var links = document.querySelector('.nav-links');
      if (toggle && links) {
        toggle.addEventListener('click', function() {
          var expanded = toggle.getAttribute('aria-expanded') === 'true';
          toggle.setAttribute('aria-expanded', String(!expanded));
          links.classList.toggle('active');
        });
      }
      // Theme toggle
      var themeBtn = document.querySelector('.theme-toggle');
      if (themeBtn) {
        themeBtn.addEventListener('click', function() {
          var html = document.documentElement;
          var current = html.getAttribute('data-theme') || 'dark';
          html.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
          localStorage.setItem('theme', html.getAttribute('data-theme'));
        });
      }
    });
  </script>"""

def has_modern_nav(content):
    return 'class="site-nav"' in content or 'data-injected="nav"' in content

def needs_nav_fix(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Must have style.css (modern page)
    if 'style.min.css' not in content:
        return False, None, None
    # Must NOT already have injected nav
    if has_modern_nav(content):
        return False, None, None
    # Check for the old inline nav pattern
    has_inline_nav = '<nav' in content and 'nav-item' in content
    return True, content, has_inline_nav

# Find all pages needing nav fix
pages_needing_fix = []
for fname in PAGES:
    fpath = os.path.join(SITE, fname)
    needs, _, _ = needs_nav_fix(fpath)
    if needs:
        pages_needing_fix.append(fname)

print(f"Pages needing nav/footer fix: {len(pages_needing_fix)}")
for p in sorted(pages_needing_fix):
    print(f"  {p}")
