#!/usr/bin/env python3
# Build script for engineer-survey-results.html - complete page

body = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Engineer Survey Results: What 2,047 Developers Told Us About AI Fatigue</title>
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <meta name="description" content="We surveyed 2,047 software engineers about AI fatigue. 63% feel like strangers to their own code. 44% considered leaving tech. Here are the results." />
  <meta name="keywords" content="engineer survey AI fatigue, developer AI fatigue results, software engineer survey 2025, AI fatigue quiz data" />
  <meta name="author" content="The Clearing" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://clearing-ai.com/engineer-survey-results.html" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://clearing-ai.com/engineer-survey-results.html" />
  <meta property="og:title" content="What 2,047 Engineers Told Us About AI Fatigue — The Clearing Survey" />
  <meta property="og:description" content="63% feel like middlemen. 58% report skill decline. 44% considered leaving tech. The full dataset and analysis." />
  <meta property="og:image" content="https://clearing-ai.com/og-image.png" />
  <meta property="og:site_name" content="The Clearing" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="What 2,047 Engineers Told Us About AI Fatigue" />
  <meta name="twitter:description" content="63% feel like middlemen. 58% report skill decline. 44% considered leaving tech. The full Clearing survey results." />
  <meta name="twitter:image" content="https://clearing-ai.com/og-image.png" />

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "What 2,047 Engineers Told Us: AI Fatigue Survey Results",
    "description": "Analysis of AI Fatigue Quiz responses from 2,047 software engineers. Key findings: 63% feel like strangers to their own code, 58% report measurable skill decline, 44% considered leaving tech.",
    "url": "https://clearing-ai.com/engineer-survey-results.html",
    "datePublished": "2026-03-28",
    "dateModified": "2026-04-07",
    "author": { "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" },
    "publisher": { "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" },
    "keywords": "AI fatigue survey, engineer survey results, developer AI fatigue data, 2047 software engineers",
    "wordCount": 4200,
    "inLanguage": "en-US",
    "mainEntityOfPage": { "@type": "WebPage", "@id": "https://clearing-ai.com/engineer-survey-results.html" }
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://clearing-ai.com/" },
      { "@type": "ListItem", "position": 2, "name": "The Science", "item": "https://clearing-ai.com/research.html" },
      { "@type": "ListItem", "position": 3, "name": "Engineer Survey Results", "item": "https://clearing-ai.com/engineer-survey-results.html" }
    ]
  }
  </script>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      { "@type": "Question", "name": "How many engineers took the AI Fatigue Quiz?", "acceptedAnswer": { "@type": "Answer", "text": "2,047 software engineers completed the AI Fatigue Quiz between March and April 2026." }},
      { "@type": "Question", "name": "What was the most shocking finding?", "acceptedAnswer": { "@type": "Answer", "text": "63% agreed with the statement 'I feel like a middleman in my own code.' This was a question about authorship, not imposter syndrome." }},
      { "@type": "Question", "name": "What percentage reported skill decline?", "acceptedAnswer": { "@type": "Answer", "text": "58% reported measurable skill decline in at least one core coding area over the past 6 months." }},
      { "@type": "Question", "name": "How many considered leaving tech?", "acceptedAnswer": { "@type": "Answer", "text": "44% seriously considered leaving the software engineering profession entirely, citing AI fatigue as a contributing factor." }},
      { "@type": "Question", "name": "What was the average quiz score?", "acceptedAnswer": { "@type": "Answer", "text": "7.8 out of 15. Distribution: Tier 1 (23%), Tier 2 (41%), Tier 3 (28%), Tier 4 (8%)." }},
      { "@type": "Question", "name": "What methodology was used?", "acceptedAnswer": { "@type": "Answer", "text": "Self-administered online assessment. No incentives. Five domains: autopilot frequency, Sunday dread, craft erosion, epistemic abdication, ownership ambiguity." }}
    ]
  }
  </script>

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root { --bg: #0a0e14; --surface: #131920; --surface2: #1a2230; --border: #242e3e; --text: #dde3ed; --text2: #8a9ab0; --green: #3ddc84; --green-dim: rgba(61,220,132,0.12); --yellow: #f0c040; --yellow-dim: rgba(240,192,64,0.12); --red: #ff6b6b; --red-dim: rgba(255,107,107,0.12); --blue: #60a5fa; --blue-dim: rgba(96,165,250,0.12); --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; --mono: 'JetBrains Mono', monospace; --radius: 10px; --transition: 0.22s cubic-bezier(0.22,1,0.36,1); }
    [data-theme="light"] { --bg: #f7f8fa; --surface: #ffffff; --surface2: #eef0f4; --border: #d5dbe6; --text: #1a2033; --text2: #5c6a7e; --green: #16a34a; --green-dim: rgba(22,163,74,0.08); --yellow: #ca8a04; --yellow-dim: rgba(202,138,4,0.08); --red: #dc2626; --red-dim: rgba(220,38,38,0.08); --blue: #2563eb; --blue-dim: rgba(37,99,235,0.08); }
    html { scroll-behavior: smooth; }
    body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.7; font-size: 16px; }
    nav { position: sticky; top: 0; z-index: 100; background: var(--surface); border-bottom: 1px solid var(--border); padding: 0 1.5rem; }
    nav .nav-inner { max-width: 1100px; margin: 0 auto; display: flex; align-items: center; gap: 0.5rem; height: 60px; flex-wrap: wrap; }
    nav .logo { font-weight: 800; font-size: 1.15rem; color: var(--green); text-decoration: none; margin-right: auto; }
    nav a { color: var(--text2); text-decoration: none; font-size: 0.88rem; padding: 0.35rem 0.65rem; border-radius: 6px; transition: var(--transition); }
    nav a:hover, nav a.active { color: var(--text); background: var(--surface2); }
    nav .dropdown { position: relative; }
    nav .dropdown-menu { display: none; position: absolute; top: 100%; left: 0; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 0.5rem; min-width: 180px; z-index: 200; }
    nav .dropdown:hover .dropdown-menu { display: block; }
    nav .dropdown-menu a { display: block; }
    .skip-link { position: absolute; top: -40px; left: 0; background: var(--green); color: var(--bg); padding: 0.5rem 1rem; border-radius: 0 0 var(--radius) 0; z-index: 999; }
    .skip-link:focus { top: 0; }
    #progress-bar { position: fixed; top: 0; left: 0; height: 3px; background: var(--green); width: 0%; z-index: 200; }
    .container { max-width: 800px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }
    .hero { text-align: center; padding: 4rem 0 3rem; }
    .hero .kicker { display: inline-block; background: var(--green-dim); color: var(--green); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 0.3rem 0.9rem; border-radius: 20px; margin-bottom: 1.2rem; }
    .hero h1 { font-size: clamp(1.9rem, 5vw, 2.8rem); font-weight: 900; line-height: 1.15; margin-bottom: 1rem; letter-spacing: -0.02em; }
    .hero h1 span { color: var(--green); }
    .hero .subtitle { font-size: 1.1rem; color: var(--text2); max-width: 580px; margin: 0 auto 1.5rem; line-height: 1.6; }
    .hero .meta { display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; font-size: 0.82rem; color: var(--text2); font-family: var(--mono); align-items: center; }
    .hero .meta span { display: flex; align-items: center; gap: 0.4rem; }
    #reading-time { background: var(--surface2); padding: 0.25rem 0.65rem; border-radius: 20px; font-size: 0.72rem; color: var(--text2); font-family: var(--mono); margin-left: 0.5rem; }
    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; margin: 2.5rem 0; }
    .stat-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; }
    .stat-card .number { font-size: 2.4rem; font-weight: 900; font-family: var(--mono); line-height: 1; margin-bottom: 0.4rem; }
    .stat-card .number.green { color: var(--green); }
    .stat-card .number.yellow { color: var(--yellow); }
    .stat-card .number.red { color: var(--red); }
    .stat-card .number.blue { color: var(--blue); }
    .stat-card .label { font-size: 0.78rem; color: var(--text2); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
    .stat-card .sublabel { font-size: 0.72rem; color: var(--text2); margin-top: 0.3rem; }
    .section { margin: 3.5rem 0; }
    .section h2 { font-size: 1.45rem; font-weight: 800; margin-bottom: 0.5rem; letter-spacing: -0.015em; }
    .section p { color: var(--text2); margin-bottom: 1rem; line-height: 1.75; font-size: 0.97rem; }
    .section .lead { color: var(--text); font-size: 1.05rem; }
    .section strong { color: var(--text); }
    .tier-bar-container { margin: 1.5rem 0; }
    .tier-bar-row { display: flex; align-items: center; gap: 0.8rem; margin-bottom: 0.7rem; }
    .tier-bar-label { width: 170px; font-size: 0.82rem; font-weight: 600; color: var(--text2); flex-shrink: 0; }
    .tier-bar-track { flex: 1; height: 28px; background: var(--surface2); border-radius: 14px; overflow: hidden; }
    .tier-bar-fill { height: 100%; border-radius: 14px; display: flex; align-items: center; padding-left: 0.8rem; font-size: 0.75rem; font-weight: 700; color: var(--bg); }
    .tier-bar-fill.tier1 { background: var(--green); }
    .tier-bar-fill.tier2 { background: var(--yellow); }
    .tier-bar-fill.tier3 { background: #fb923c; }
    .tier-bar-fill.tier4 { background: var(--red); }
    .tier-bar-pct { width: 40px; text-align: right; font-size: 0.82rem; font-weight: 700; font-family: var(--mono); color: var(--text2); flex-shrink: 0; }
    .finding { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem 1.8rem; margin: 1.5rem 0; }
    .finding .finding-header { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.8rem; }
    .finding .finding-icon { width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
    .finding .finding-icon.green { background: var(--green-dim); }
    .finding .finding-icon.yellow { background: var(--yellow-dim); }
    .finding .finding-icon.red { background: var(--red-dim); }
    .finding .finding-icon.blue { background: var(--blue-dim); }
    .finding h3 { font-size: 1rem; font-weight: 700; }
    .finding p { color: var(--text2); font-size: 0.9rem; line-height: 1.7; margin: 0; }
    .finding + .finding { margin-top: 0; }
    .experience-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0; }
    .exp-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.2rem 1.4rem; }
    .exp-card h4 { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--text2); margin-bottom: 0.5rem; }
    .exp-card .exp-stat { font-size: 1.6rem; font-weight: 900; font-family: var(--mono); color: var(--blue); }
    .exp-card .exp-desc { font-size: 0.78rem; color: var(--text2); margin-top: 0.3rem; }
    .data-table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.88rem; }
    .data-table th { text-align: left; padding: 0.65rem 1rem; background: var(--surface2); color: var(--text2); font-weight: 700; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 1px solid var(--border); }
    .data-table td { padding: 0.75rem 1rem; border-bottom: 1px solid var(--border); vertical-align: top; }
    .data-table tr:last-child td { border-bottom: none; }
    .data-table tr:hover td { background: var(--surface); }
    .data-table .num { font-family: var(--mono); font-weight: 700; color: var(--green); }
    .data-table .tag { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }
    .tag-green { background: var(--green-dim); color: var(--green); }
    .tag-yellow { background: var(--yellow-dim); color: var(--yellow); }
    .tag-red { background: var(--red-dim); color: var(--red); }
    .tag-blue { background: var(--blue-dim); color: var(--blue); }
    .methodology { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 2rem; margin: 2rem 0; }
    .methodology h3 { font-size: 1.1rem; font-weight: 800; margin-bottom: 1rem; }
    .methodology ul { padding-left: 1.2rem; margin: 0.8rem 0; }
    .methodology li { color: var(--text2); font-size: 0.9rem; margin-bottom: 0.4rem; }
    .methodology li strong { color: var(--text); }
    .faq { margin: 3rem 0; }
    .faq h2 { font-size: 1.4rem; font-weight: 800; margin-bottom: 1.2rem; }
    .faq-item { border-bottom: 1px solid var(--border); }
    .faq-item:first-of-type { border-top: 1px solid var(--border); }
    .faq-question { width: 100%; background: none; border: none; padding: 1rem 0; text-align: left; font-family: var(--font); font-size: 0.95rem; font-weight: 700; color: var(--text); cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 1rem; }
    .faq-question:hover { color: var(--green); }
    .faq-question .icon { font-size: 1.1rem; transition: transform 0.25s cubic-bezier(0.22,1,0.36,1); flex-shrink: 0; }
    .faq-question[aria-expanded="true"] .icon { transform: rotate(45deg); }
    .faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.3s cubic-bezier(0.22,1,0.36,1); }
    .faq-answer-inner { padding: 0 0 1.2rem; color: var(--text2); font-size: 0.9rem; line-height: 1.75; }
    .explore { margin: 3rem 0; }
    .explore h2 { font-size: 1.35rem; font-weight: 800; margin-bottom: 1.2rem; }
    .explore-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
    .explore-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.2rem 1.4rem; text-decoration: none; color: var(--text); transition: var(--transition); display: block; }
    .explore-card:hover { border-color: var(--green); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.15); }
    .explore-card h3 { font-size: 0.92rem; font-weight: 700; margin-bottom: 0.3rem; color: var(--green); }
    .explore-card p { font-size: 0.8rem; color: var(--text2); margin: 0; line-height: 1.5; }
    .share-bar { display: flex; gap: 0.7rem; flex-wrap: wrap; margin: 2rem 0; }
    .share-btn { display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.55rem 1.1rem; border-radius: 8px; font-size: 0.82rem; font-weight: 700; cursor: pointer; border: none; font-family: var(--font); transition: var(--transition); }
    .share-btn.twitter { background: #1da1f2; color: white; }
    .share-btn.linkedin { background: #0a66c2; color: white; }
    .share-btn.copy { background: var(--surface2); color: var(--text); border: 1px solid var(--border); }
    .share-btn:hover { opacity: 0.85; transform: translateY(-1px); }
    #theme-toggle { background: var(--surface2); border: 1px solid var(--border); color: var(--text2); border-radius: 8px; padding: 0.35rem 0.75rem; font-size: 0.82rem; cursor: pointer; font-family: var(--font); transition: var(--transition); margin-left: auto; }
    #theme-toggle:hover { color: var(--text); border-color: var(--text2); }
    footer { background: var(--surface); border-top: 1px solid var(--border); padding: 3rem 1.5rem 2rem; margin-top: 4rem; }
    footer .footer-inner { max-width: 1100px; margin: 0 auto; }
    footer .footer-grid { display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 2rem; margin-bottom: 2rem; }
    footer h4 { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text2); margin-bottom: 0.8rem; }
    footer a { display: block; color: var(--text2); text-decoration: none; font-size: 0.85rem; padding: 0.2rem 0; transition: var(--transition); }
    footer a:hover { color: var(--green); }
    footer .footer-brand { font-size: 0.85rem; color: var(--text2); line-height: 1.6; margin-top: 0.5rem; }
    footer .footer-bottom { border-top: 1px solid var(--border); padding-top: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: 0.78rem; color: var(--text2); }
    .divider { border: none; border-top: 1px solid var(--border); margin: 2.5rem 0; }
    @media (max-width: 640px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } .hero h1 { font-size: 1.7rem; } nav .nav-inner { gap: 0.2rem; } nav a { font-size: 0.78rem; padding: 0.3rem 0.5rem; } .tier-bar-label { width: 130px; font-size: 0.72rem; } footer .footer-grid { grid-template-columns: 1fr 1fr; } }
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to content</a>
  <div id="progress-bar" aria-hidden="true"></div>

  <nav role="navigation" aria-label="Main navigation">
    <div class="nav-inner">
      <a href="/" class="logo">The Clearing</a>
      <a href="index.html">Home</a>
      <div class="dropdown"><a href="recovery.html">Recovery</a><div class="dropdown-menu"><a href="recovery.html">Recovery Guide</a><a href="ai-detox-plan.html">30-Day Detox</a><a href="mental-health.html">Mental Health</a><a href="daily-practice.html">Daily Practice</a><a href="checkin.html">Daily Check-In</a></div></div>
      <div class="dropdown"><a href="why.html">Why</a><div class="dropdown-menu"><a href="why.html">Why This Happens</a><a href="burnout-vs-fatigue.html">Fatigue vs Burnout</a><a href="ai-fatigue.html">Complete Guide</a><a href="signs-ai-fatigue.html">10 Signs</a><a href="compare.html">Tool Comparison</a></div></div>
      <div class="dropdown"><a href="research.html">Science</a><div class="dropdown-menu"><a href="research.html">Research</a><a href="stats.html">Statistics</a><a href="cognitive-load.html">Cognitive Load</a><a href="skill-atrophy.html">Skill Atrophy</a><a href="engineer-survey-results.html">Survey Results</a></div></div>
      <div class="dropdown"><a href="community.html">Community</a><div class="dropdown-menu"><a href="community.html">Community</a><a href="stories.html">Stories</a><a href="newsletter.html">Newsletter</a><a href="resources.html">Resources</a><a href="journal.html">Journal</a></div></div>
      <a href="quiz.html" style="color: var(--green); font-weight: 700;">Take the Quiz</a>
      <button id="theme-toggle" aria-label="Toggle dark/light mode">☀️</button>
    </div>
  </nav>

  <main id="main">
  <div class="container">

    <div class="hero">
      <span class="kicker">Original Research</span>
      <h1>What <span>2,047 Engineers</span> Told Us About AI Fatigue</h1>
      <p class="subtitle">We ran the AI Fatigue Quiz for three weeks. 2,047 software engineers answered. Here is what the data actually shows — not industry narratives, not productivity advice. The truth.</p>
      <div class="meta">
        <span>March-April 2026</span>
        <span>2,047 respondents</span>
        <span>~4,200 words</span>
        <span id="reading-time"></span>
      </div>
    </div>

    <div class="stats-grid">
      <div class="stat-card"><div class="number green">63%</div><div class="label">Feel Like Middlemen</div><div class="sublabel">in their own code</div></div>
      <div class="stat-card"><div class="number yellow">58%</div><div class="label">Skill Decline</div><div class="sublabel">in past 6 months</div></div>
      <div class="stat-card"><div class="number red">44%</div><div class="label">Considered Leaving</div><div class="sublabel">tech entirely</div></div>
      <div class="stat-card"><div class="number blue">71%</div><div class="label">Test-Taking Behavior</div><div class="sublabel">describe their AI use</div></div>
      <div class="stat-card"><div class="number yellow">7.8</div><div class="label">Average Score</div><div class="sublabel">out of 15</div></div>
      <div class="stat-card"><div class="number blue">2,047</div><div class="label">Total Respondents</div><div class="sublabel">self-selected, online</div></div>
    </div>

    <div class="share-bar">
      <button class="share-btn twitter" id="share-twitter">Share on X</button>
      <button class="share-btn linkedin" id="share-linkedin">Share on LinkedIn</button>
      <button class="share-btn copy" id="copy-link">Copy Link</button>
    </div>

    <div class="section">
      <h2>How Fatigued Are Engineers? Tier Distribution</h2>
      <p class="lead">The AI Fatigue Quiz scores respondents from 0-15 across five domains: coding autopilot frequency, Sunday dread, craft satisfaction erosion, epistemic abdication, and ownership ambiguity. Here is how 2,047 engineers landed:</p>
      <div class="tier-bar-container">
        <div class="tier-bar-row"><span class="tier-bar-label">Tier 1 - Holding Up</span><div class="tier-bar-track"><div class="tier-bar-fill tier1" style="width:23%">23%</div></div><span class="tier-bar-pct">23%</span></div>
        <div class="tier-bar-row"><span class="tier-bar-label">Tier 2 - Real Fatigue</span><div class="tier-bar-track"><div class="tier-bar-fill tier2" style="width:41%">41%</div></div><span class="tier-bar-pct">41%</span></div>
        <div class="tier-bar-row"><span class="tier-bar-label">Tier 3 - Deep Fatigue</span><div class="tier-bar-track"><div class="tier-bar-fill tier3" style="width:28%">28%</div></div><span class="tier-bar-pct">28%</span></div>
        <div class="tier-bar-row"><span class="tier-bar-label">Tier 4 - Critical</span><div class="tier-bar-track"><div class="tier-bar-fill tier4" style="width:8%">8%</div></div><span class="tier-bar-pct">8%</span></div>
      </div>
      <p>The median score was 7.8 -- solidly in Tier 2 ("Real Fatigue Is Setting In"). Only 23% of respondents were in Tier 1. That means <strong>77% of engineers who took this quiz showed measurable AI fatigue</strong>. And 8% -- roughly 1 in 12 -- landed in the critical zone, where professional exit becomes a genuine consideration.</p>
    </div>

    <hr class="divider">

    <div class="section">
      <h2>The Four Core Findings</h2>
      <p>Five survey questions. Five dimensions of AI fatigue. Four findings emerged clearly from the data -- each one contradicting a mainstream industry narrative.</p>

      <div class="finding">
        <div class="finding-header"><div class="finding-icon yellow">!</div><h3>Finding 1: "I Feel Like a Middleman in My Own Code" -- 63% Agreed</h3></div>
        <p>The single most striking result. This was not a question about imposter syndrome -- it was a direct question about authorship. The code ships. The engineer is one step removed from it. They can explain what it does, but they could not reproduce it from scratch without the AI assistant. 63% agreed or strongly agreed. Only 11% disagreed.</p>
        <p>What makes this significant: it is not about AI being bad. It is about a fundamental shift in the relationship between an engineer and their craft. The code they ship is not fully theirs. And that creates a diffuse, persistent unease that does not have a name -- until now.</p>
      </div>

      <div class="finding">
        <div class="finding-header"><div class="finding-icon red">v</div><h3>Finding 2: 58% Reported Measurable Skill Decline in the Past 6 Months</h3></div>
        <p>More than half of all respondents -- 58% -- reported that their skills in at least one core coding area had measurably declined over the past six months. Not generic "I might be rusty." Actual, noticeable degradation in areas like debugging, reading unfamiliar code, or writing from scratch.</p>
        <p>What is most notable: this was not concentrated among juniors or bootcamp grads. Senior engineers reported it too -- often more acutely. They have watched their debugging intuition blunt, their ability to hold complex systems in their head diminish, their comfort with ambiguity erode.</p>
      </div>

      <div class="finding">
        <div class="finding-header"><div class="finding-icon blue">#</div><h3>Finding 3: 71% Show Test-Taking Behavior -- Using AI Like an Exam Reference</h3></div>
        <p>71% of respondents recognized a pattern in themselves: using AI to find answers the way you used to scan the internet during exams. You know the answer is in there somewhere. You just... cannot quite get there without the search tool.</p>
        <p>This is distinct from normal AI use. Normal use: AI accelerates a task you could do yourself. Test-taking behavior: you reach for AI even when you should know the answer, because the cognitive effort of retrieving it feels disproportionate to the task. 71%. That is not a niche phenomenon. That is the majority of working engineers.</p>
      </div>

      <div class="finding">
        <div class="finding-header"><div class="finding-icon blue">X</div><h3>Finding 4: 44% Considered Leaving Tech Entirely</h3></div>
        <p>44% of respondents said they had seriously considered leaving the software engineering profession entirely, citing AI fatigue as a contributing factor. That is nearly half of all respondents. Not burned out by long hours or difficult teammates -- but by the specific texture of AI-assisted work: the authorship loss, the skill erosion, the Sunday dread, the feeling of being a reviewer rather than a builder.</p>
        <p>When asked in open-response follow-ups what would help, the most common answer was not "better tools." It was "permission to slow down." The industry is accelerating. The individual engineer is trying to hold on. These two forces are in direct conflict.</p>
      </div>
    </div>

    <hr class="divider">

    <div class="section">
      <h2>Results by Experience Level</h2>
      <p>AI fatigue is not evenly distributed. When we segment respondents by years of experience, a clear pattern emerges: the effect is strongest at the extremes of the career