#!/usr/bin/env python3
"""Add nav + footer + SEO schema to vibe-coding.html (Phase 1 build)"""
import re

path = "/Users/nightcoder/Desktop/TheClearing/vibe-coding.html"
with open(path) as f:
    content = f.read()

# ===== SEO META =====
seo_block = '''
  <title>Vibe Coding: When AI Does the Building — The Clearing</title>
  <meta name="description" content="Vibe coding feels productive but quietly erodes your skills. Here's what vibe coding actually costs, the four stages of drift, and how to stay in charge of your own building.">
  <meta name="keywords" content="vibe coding, AI coding, code ownership, AI skills, developer skills, AI assisted development">
  <meta property="og:title" content="Vibe Coding: When AI Does the Building">
  <meta property="og:description" content="Vibe coding feels productive but quietly erodes your skills. Here's what it costs and how to stay in charge.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://clearing-ai.com/vibe-coding.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Vibe Coding: When AI Does the Building">
  <meta name="twitter:description" content="Vibe coding feels productive but quietly erodes your skills. Here's what it costs and how to stay in charge.">
  <link rel="canonical" href="https://clearing-ai.com/vibe-coding.html">'''

# Insert meta after </title> closing tag in <head>
content = content.replace(
    "</title>",
    "</title>" + seo_block,
    1
)

# ===== ARTICLE SCHEMA =====
schema_block = '''
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Vibe Coding: When AI Does the Building and You Watch",
      "description": "Vibe coding feels productive but quietly erodes your skills. The four stages of drift and how to stay in charge.",
      "wordCount": "3200",
      "datePublished": "2026-05-15",
      "dateModified": "2026-05-15",
      "author": {"@type": "Organization", "name": "The Clearing"},
      "publisher": {
        "@type": "Organization",
        "name": "The Clearing",
        "url": "https://clearing-ai.com"
      },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://clearing-ai.com/vibe-coding.html"
      },
      "articleSection": "AI Fatigue",
      "about": {
        "@type": "Thing",
        "name": "AI-assisted software development"
      }
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://clearing-ai.com/"},
        {"@type": "ListItem", "position": 2, "name": "Understand", "item": "https://clearing-ai.com/"},
        {"@type": "ListItem", "position": 3, "name": "Vibe Coding", "item": "https://clearing-ai.com/vibe-coding.html"}
      ]
    }
    </script>'''

# Insert schema before </head>
content = content.replace(
    "  <script type=\"application/ld+json\">",
    schema_block + "\n    <script type=\"application/ld+json\">"
)

# ===== NAV (add after body tag) =====
nav_html = '''
  <nav class="nav" role="navigation" aria-label="Main navigation">
    <a href="index.html" class="nav-logo">🌿 The Clearing</a>
    <button type="button" class="nav-toggle" aria-label="Toggle menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
    <div class="nav-links">
      <li class="nav-dropdown">
        <a href="why.html">Why</a>
        <div class="nav-dropdown-menu">
          <a href="why.html">Why It Happens</a>
          <a href="signs-ai-fatigue.html">Signs of Fatigue</a>
          <a href="burnout-vs-fatigue.html">Burnout vs Fatigue</a>
          <a href="glossary.html">Glossary</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="recovery.html">Recover</a>
        <div class="nav-dropdown-menu">
          <a href="recovery.html">Recovery Guide</a>
          <a href="decompress.html">Decompress</a>
          <a href="ai-detox-plan.html">30-Day Detox</a>
          <a href="daily-practice.html">Daily Practice</a>
          <a href="mental-health.html">Mental Health</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="compare.html">Tools</a>
        <div class="nav-dropdown-menu">
          <a href="compare.html">Tool Comparison</a>
          <a href="ai-tool-overload.html">Tool Overload</a>
          <a href="coding-ai-tools-comparison.html">Coding Tools</a>
          <a href="ai-learning-burnout.html">Learning Burnout</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="research.html">Understand</a>
        <div class="nav-dropdown-menu">
          <a href="research.html">Science of AI Fatigue</a>
          <a href="cognitive-load.html">Cognitive Load</a>
          <a href="skill-atrophy.html">Skill Atrophy</a>
          <a href="flow-state.html">Flow State</a>
          <a href="attention-residue.html">Attention Residue</a>
          <a href="vibe-coding.html">Vibe Coding</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="community.html">Community</a>
        <div class="nav-dropdown-menu">
          <a href="stories.html">Engineer Stories</a>
          <a href="community.html">Find Your People</a>
          <a href="newsletter.html">The Dispatch</a>
          <a href="checkin.html">Daily Check-in</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="resources.html">Resources</a>
        <div class="nav-dropdown-menu">
          <a href="resources.html">Reading List</a>
          <a href="stats.html">Statistics</a>
          <a href="hiring.html">For Managers</a>
        </div>
      </li>
      <li class="nav-dropdown">
        <a href="quiz-results.html">Quiz</a>
        <div class="nav-dropdown-menu">
          <a href="index.html#quiz">Take the Quiz</a>
          <a href="quiz-results.html">Your Results</a>
          <a href="badge.html">Share Your Score</a>
        </div>
      </li>
    </div>
    <button type="button" class="theme-toggle" aria-label="Toggle theme" onclick="document.documentElement.toggleAttribute('data-theme'); document.documentElement.setAttribute('data-theme', document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark')">🌙</button>
  </nav>'''

content = content.replace('<body>', '<body>\n' + nav_html)

# ===== FOOTER =====
footer_html = '''
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <a href="index.html" class="footer-logo">🌿 The Clearing</a>
        <p>Resources for software engineers navigating AI fatigue.</p>
        <div class="footer-social">
          <a href="https://twitter.com/intent/user?screen_name=CoderNight47757" target="_blank" rel="noopener" aria-label="Twitter/X">𝕏</a>
          <a href="https://github.com/clearing-ai" target="_blank" rel="noopener" aria-label="GitHub">⟨⟩</a>
          <a href="https://www.linkedin.com/company/clearing-ai" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>
        </div>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <h4>Recover</h4>
          <ul>
            <li><a href="recovery.html">Recovery Guide</a></li>
            <li><a href="decompress.html">Decompress</a></li>
            <li><a href="ai-detox-plan.html">30-Day Plan</a></li>
            <li><a href="mental-health.html">Mental Health</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Understand</h4>
          <ul>
            <li><a href="why.html">Why It Happens</a></li>
            <li><a href="research.html">The Science</a></li>
            <li><a href="skill-atrophy.html">Skill Atrophy</a></li>
            <li><a href="cognitive-load.html">Cognitive Load</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Community</h4>
          <ul>
            <li><a href="stories.html">Stories</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
            <li><a href="checkin.html">Daily Check-in</a></li>
            <li><a href="community.html">Find Your People</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Tools & Resources</h4>
          <ul>
            <li><a href="compare.html">Tool Comparison</a></li>
            <li><a href="resources.html">Reading List</a></li>
            <li><a href="stats.html">Statistics</a></li>
            <li><a href="hiring.html">For Managers</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 The Clearing · <a href="privacy.html">Privacy</a> · <a href="index.html#quiz">Take the Quiz</a></p>
    </div>
  </footer>'''

content = content.replace('</body>', footer_html + '\n</body>')

with open(path, 'w') as f:
    f.write(content)

print("Done: vibe-coding.html nav + footer + SEO schema added")