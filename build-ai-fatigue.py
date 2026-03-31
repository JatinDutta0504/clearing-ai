#!/usr/bin/env python3
"""Generate ai-fatigue.html — The Definitive AI Fatigue Guide"""

output = "/Users/nightcoder/Desktop/TheClearing/ai-fatigue.html"

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Fatigue: The Complete Guide for Software Engineers | The Clearing</title>
  <meta name="description" content="What AI fatigue really is, why engineers are uniquely vulnerable, and a practical 30-day plan to recover. 2000+ engineers surveyed. Science-backed. Free." />
  <meta name="keywords" content="AI fatigue, AI fatigue engineers, AI burnout, developer fatigue, software engineer mental health, AI tools mental health, AI productivity exhaustion, tech worker fatigue 2025" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://clearing-ai.com/ai-fatigue.html" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://clearing-ai.com/ai-fatigue.html" />
  <meta property="og:title" content="AI Fatigue: The Complete Guide for Software Engineers" />
  <meta property="og:description" content="What AI fatigue really is, why engineers are uniquely vulnerable, and a practical 30-day plan to recover." />
  <meta property="og:image" content="https://clearing-ai.com/og-image.png" />
  <meta property="og:site_name" content="The Clearing" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="AI Fatigue: The Complete Guide for Software Engineers" />
  <meta name="twitter:description" content="What AI fatigue really is, why engineers are uniquely vulnerable, and a practical 30-day plan to recover." />
  <meta name="twitter:image" content="https://clearing-ai.com/og-image.png" />

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "AI Fatigue: The Complete Guide for Software Engineers",
    "description": "What AI fatigue really is, why engineers are uniquely vulnerable, and a practical 30-day plan to recover. Based on 2000+ engineer survey data.",
    "url": "https://clearing-ai.com/ai-fatigue.html",
    "author": { "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" },
    "publisher": { "@type": "Organization", "name": "The Clearing", "url": "https://clearing-ai.com" },
    "datePublished": "2026-03-31",
    "dateModified": "2026-03-31",
    "wordCount": 5200,
    "articleSection": ["Definition", "Five Dimensions", "Who Is Affected", "Career Stage Impact", "Warning Signs", "Why Engineers", "AI Fatigue vs Burnout", "Recovery", "FAQ"]
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is AI fatigue in simple terms?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI fatigue is the chronic exhaustion that comes from constant AI tool use — not because the tools are hard, but because using them constantly erodes your skills, identity, and sense of ownership over your work. It is distinct from burnout: burnout is from overwork; AI fatigue is from skill erosion and identity loss, often even with normal workloads."
        }
      },
      {
        "@type": "Question",
        "name": "How is AI fatigue different from burnout?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Burnout is about work volume — too much work, too little recovery. AI fatigue is about work quality and your relationship to work — you may be doing the same amount of work, but you have lost the thread of ownership, learning, and craft that made it meaningful. Many engineers have AI fatigue without being overworked, and vice versa."
        }
      },
      {
        "@type": "Question",
        "name": "Who is most at risk for AI fatigue?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Engineers who write code daily, work at companies with mandatory or strongly pressured AI tool adoption, are mid-career or senior with strong pre-AI skill identity, work in high-velocity environments with shipping pressure, or are early-career where AI bypasses the productive struggle that builds foundational skills."
        }
      },
      {
        "@type": "Question",
        "name": "Is AI fatigue permanent?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. AI fatigue is recoverable. Mild cases often improve within 2-4 weeks of intentional boundaries. Moderate to severe cases typically need 1-3 months of consistent practice. Recovery is not linear — there will be good days and hard days — but the trajectory is consistently positive with deliberate effort."
        }
      },
      {
        "@type": "Question",
        "name": "Should I just stop using AI tools entirely?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Not necessarily. Complete abstinence is one valid approach, but most engineers find a middle path more sustainable: intentional, bounded AI use where you use the tools to amplify your learning, not replace it. The goal is not to use less AI — it is to use AI in a way that leaves you stronger, not weaker."
        }
      },
      {
        "@type": "Question",
        "name": "How do I talk to my manager about AI fatigue?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Frame it as a performance and retention concern, not a personal complaint. Specific language that works: I am noticing my code ownership is decreasing and I want to address that before it affects quality. or I would like to have 2 hours a day with AI tools paused so I can maintain my debugging skills. Most managers respond well to concrete, outcome-focused framing."
        }
      }
    ]
  }
  </script>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://clearing-ai.com" },
      { "@type": "ListItem", "position": 2, "name": "Understand", "item": "https://clearing-ai.com/why.html" },
      { "@type": "ListItem", "position": 3, "name": "AI Fatigue", "item": "https://clearing-ai.com/ai-fatigue.html" }
    ]
  }
  </script>

  <link rel="icon" href="favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="css/style.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="css/style.css" /></noscript>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #fafaf8; color: #2a2a22; line-height: 1.6; }
    [data-theme="dark"] { background: #111411; color: #e8e4dc; }
    [data-theme="dark"] .page-hero { background: linear-gradient(135deg, #1a2e1a 0%, #243324 60%, #1e2e1e 100%); }
    [data-theme="dark"] .toc-wrap { background: #1a1e1a; border-color: rgba(90,140,90,0.2); }
    [data-theme="dark"] .toc-wrap a { color: #c8d8c0; }
    [data-theme="dark"] .toc-wrap a:hover { color: #7aab8a; }
    [data-theme="dark"] h2 { color: #b8d4b0; }
    [data-theme="dark"] p { color: #a0a090; }
    [data-theme="dark"] .stat-card { background: #1a1e1a; border-color: rgba(90,140,90,0.2); }
    [data-theme="dark"] .callout { background: rgba(45,80,22,0.1); border-color: rgba(90,140,90,0.3); }
    [data-theme="dark"] .callout p { color: #a0a090; }
    [data-theme="dark"] table th { background: #1e2a1e; color: #b8d4b0; }
    [data-theme="dark"] table td { border-color: rgba(90,140,90,0.1); color: #a0a090; }
    [data-theme="dark"] table tbody tr:nth-child(even) { background: #161c16; }
    [data-theme="dark"] .dim-card { background: #1a1e1a; border-color: rgba(90,140,90,0.15); }
    [data-theme="dark"] .dim-card h3 { color: #b8d4b0; }
    [data-theme="dark"] .dim-card p { color: #a0a090; }
    [data-theme="dark"] .profile-card { background: #1a1e1a; border-color: rgba(90,140,90,0.2); }
    [data-theme="dark"] .profile-card strong { color: #b8d4b0; }
    [data-theme="dark"] .profile-card p { color: #a0a090; }
    [data-theme="dark"] .sign-card { background: #1a1e1a; border-color: rgba(90,140,90,0.15); }
    [data-theme="dark"] .sign-card strong { color: #b8d4b0; }
    [data-theme="dark"] .sign-card span { color: #a0a090; }
    [data-theme="dark"] .explore-card { background: #1a1e1a; border-color: rgba(90,140,90,0.2); }
    [data-theme="dark"] .explore-card h3 { color: #b8d4b0; }
    [data-theme="dark"] .explore-card p { color: #a0a090; }
    [data-theme="dark"] .faq-btn { color: #b8d4b0; }
    [data-theme="dark"] .faq-body { background: #161c16; color: #a0a090; }
    [data-theme="dark"] .header { background: rgba(17,20,17,0.95); border-color: rgba(45,80,22,0.2); }
    [data-theme="dark"] .nav-links a { color: #a0a090; }
    [data-theme="dark"] .nav-links a:hover { color: #8abb9a; background: rgba(90,140,90,0.08); }
    [data-theme="dark"] .footer { background: #0d1a0d; border-color: rgba(45,80,22,0.2); }
    [data-theme="dark"] .footer a { color: #a0a090; }
    [data-theme="dark"] .footer a:hover { color: #8abb9a; }
    [data-theme="dark"] .footer p { color: #a0a090; }
    [data-theme="dark"] .cta-wrap { background: linear-gradient(135deg, #1a2e1a, #243324); }
    [data-theme="dark"] .step h4 { color: #b8d4b0; }
    [data-theme="dark"] .step p { color: #a0a090; }

    .skip-link { position: absolute; top: -100%; left: 1rem; background: #2d5016; color: white; padding: 0.5rem 1rem; border-radius: 0 0 6px 6px; text-decoration: none; font-size: 0.85rem; z-index: 999; }
    .skip-link:focus { top: 0; }
    .reading-progress { position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, #4a7c59, #7aab8a); width: 0%; z-index: 100; transition: width 0.1s linear; pointer-events: none; }

    .header { background: rgba(255,255,255,0.95); border-bottom: 1px solid rgba(45,80,22,0.1); position: sticky; top: 0; z-index: 50; }
    .nav { max-width: 1100px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 12px 20px; }
    .nav-logo { font-weight: 700; font-size: 15px; color: #2d5016; text-decoration: none; display: flex; align-items: center; gap: 6px; }
    .nav-links { display: flex; gap: 0; list-style: none; }
    .nav-links a { padding: 6px 14px; color: #4a4a3e; text-decoration: none; font-size: 0.88rem; font-weight: 500; border-radius: 6px; transition: color 0.2s, background 0.2s; }
    .nav-links a:hover { color: #2d5016; background: rgba(45,80,22,0.06); }
    .nav-toggle { display: none; background: none; border: none; font-size: 1.4rem; cursor: pointer; padding: 4px 8px; }
    .nav-dropdown { position: relative; }
    .dropdown-menu { display: none; position: absolute; top: 100%; left: 0; background: white; border: 1px solid rgba(45,80,22,0.15); border-radius: 8px; padding: 6px 0; min-width: 180px; box-shadow: 0 8px 24px rgba(0,0,0,0.08); z-index: 50; }
    [data-theme="dark"] .dropdown-menu { background: #1a1e1a; border-color: rgba(45,80,22,0.3); }
    .nav-dropdown:hover .dropdown-menu, .nav-dropdown:focus-within .dropdown-menu { display: block; }
    .dropdown-menu li { list-style: none; }
    .dropdown-menu a { display: block; padding: 8px 16px; font-size: 0.85rem; border-radius: 0; }
    .theme-toggle { background: none; border: none; cursor: pointer; font-size: 1.1rem; padding: 4px 8px; border-radius: 6px; transition: background 0.2s; }
    .theme-toggle:hover { background: rgba(45,80,22,0.08); }

    .page-hero { background: linear-gradient(135deg, #1a2e1a 0%, #243324 60%, #1e2e1e 100%); color: #f5f0e8; padding: 5.5rem 2rem 4.5rem; text-align: center; position: relative; overflow: hidden; }
    .page-hero::before { content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse at 30% 50%, rgba(90,140,90,0.12) 0%, transparent 60%); pointer-events: none; }
    .hero-eyebrow { font-size: 0.7rem; letter-spacing: 0.14em; text-transform: uppercase; color: #7aab8a; margin-bottom: 1rem; font-weight: 500; }
    .page-hero h1 { font-family: Georgia, serif; font-size: clamp(1.8rem, 5vw, 2.8rem); font-weight: 400; line-height: 1.25; max-width: 700px; margin: 0 auto 1rem; }
    .hero-sub { font-size: 1rem; color: rgba(245,240,232,0.65); max-width: 520px; margin: 0 auto 2rem; line-height: 1.65; }
    .hero-meta { display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.2rem; }
    .hero-meta-item { font-size: 0.8rem; color: rgba(245,240,232,0.5); }
    .hero-meta-item strong { color: #7aab8a; font-weight: 600; }

    .content-wrap { max-width: 800px; margin: 0 auto; padding: 4rem 2rem 6rem; }

    .toc-wrap { background: #f4f1ea; border-radius: 12px; padding: 1.8rem 2rem; margin-bottom: 3.5rem; border: 1px solid rgba(45,80,22,0.12); }
    .toc-label { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #5c7a4e; margin-bottom: 1rem; }
    .toc-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .toc-list a { color: #2a2a22; text-decoration: none; font-size: 0.9rem; display: flex; gap: 0.6rem; align-items: baseline; transition: color 0.2s; }
    .toc-list a:hover { color: #4a7c59; }
    .toc-num { color: #7aab8a; font-weight: 600; min-width: 1.5rem; }

    h2 { font-family: Georgia, serif; font-size: 1.55rem; font-weight: 400; color: #1a2e1a; margin-bottom: 1.2rem; line-height: 1.35; margin-top: 3rem; }
    h3 { font-size: 0.98rem; font-weight: 700; color: #2d5016; margin-bottom: 0.5rem; }
    p { font-size: 1.02rem; color: #3a3a2e; line-height: 1.85; margin-bottom: 1.1rem; }
    p:last-child { margin-bottom: 0; }
    em { font-style: italic; }
    strong { font-weight: 600; }
    .section-top { margin-top: 3.5rem; }

    .callout { background: #f0ebe0; border-left: 3px solid #5c7a4e; padding: 1.2rem 1.6rem; border-radius: 0 10px 10px 0; font-size: 0.95rem; line-height: 1.7; margin: 2rem 0; }
    .callout strong { color: #2d5016; }

    .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0; }
    .stat-card { background: #f5f2ec; border: 1px solid rgba(45,80,22,0.1); border-radius: 10px; padding: 1.1rem 1.3rem; }
    .stat-num { font-size: 1.8rem; font-weight: 700; color: #5c7a4e; line-height: 1; }
    .stat-label { font-size: 0.82rem; color: #4a4a3e; margin-top: 0.3rem; line-height: 1.4; }
    [data-theme="dark"] .stat-num { color: #7aab8a; }
    [data-theme="dark"] .stat-label { color: #a0a090; }

    .dim-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; margin: 1.5rem 0; }
    .dim-card { background: #f4f1ea; border-radius: 12px; padding: 1.3rem; border: 1px solid rgba(45,80,22,0.1); }
    .dim-icon { font-size: 1.5rem; margin-bottom: 0.4rem; }
    .dim-card h3 { font-size: 0.92rem; color: #2d5016; margin-bottom: 0.4rem; }
    .dim-card p { font-size: 0.87rem; color: #4a4a3e; line-height: 1.65; margin-bottom: 0; }
    .dim-card.wide { grid-column: 1 / -1; }

    .profile-list { display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0; }
    .profile-card { background: #f5f2ec; border-radius: 10px; padding: 1.2rem 1.5rem; border-left: 3px solid #5c7a4e; }
    .profile-card strong { color: #2d5016; font-size: 0.92rem; display: block; margin-bottom: 0.3rem; }
    .profile-card p { font-size: 0.9rem; color: #4a4a3e; line-height: 1.65; margin-bottom: 0; }

    table { width: 100%; border-collapse: collapse; font-size: 0.88rem; margin: 1.5rem 0; border-radius: 8px; overflow: hidden; }
    th { background: #e8e4dc; text-align: left; padding: 0.7rem 1rem; border-bottom: 2px solid #ccc; font-weight: 600; color: #2d5016; }
    td { padding: 0.7rem 1rem; border-bottom: 1px solid #eee; vertical-align: top; color: #3a3a2e; }
    tbody tr:nth-child(even) { background: #f9f7f4; }

    .signs-list { display: flex; flex-direction: column; gap: 0.7rem; margin: 1.5rem 0; }
    .sign-card { display: flex; gap: 1rem; align-items: flex-start; padding: 0.9rem 1.2rem; background: #f5f2ec; border-radius: 8px; border: 1px solid rgba(45,80,22,0.08); }
    .sign-icon { font-size: 1.1rem; flex-shrink: 0; margin-top: 2px; }
    .sign-card strong { color: #2d5016; font-size: 0.9rem; display: block; margin-bottom: 0.2rem; }
    .sign-card span { font-size: 0.87rem; color: #4a4a3e; line-height: 1.6; }

    .why-list { display: flex; flex-direction: column; gap: 1rem; margin: 1.5rem 0; }
    .why-card { background: #f5f2ec; border-radius: 10px; padding: 1.2rem 1.5rem; border: 1px solid rgba(45,80,22,0.1); }
    .why-card h3 { color: #2d5016; font-size: 0.95rem; margin-bottom: 0.4rem; }
    .why-card p { font-size: 0.9rem; color: #4a4a3e; line-height: 1.7; margin-bottom: 0; }

    .compare-wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0; }
    .compare-col h3 { font-size: 0.98rem; font-weight: 700; margin-bottom: 0.8rem; padding-bottom: 0.5rem; border-bottom: 2px solid; }
    .compare-col.genuine h3 { color: #4a7c59; border-color: #4a7c59; }
    .compare-col.burnout h3 { color: #8a6a20; border-color: #b49020; }
    .compare-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .compare-col li { font-size: 0.88rem; color: #3a3a2e; padding-left: 1.2rem; position: relative; line-height: 1.6; }
    .compare-col.genuine li::before { content: '—'; position: absolute; left: 0; color: #7aab8a; }
    .compare-col.burnout li::before { color: #b49020; }

    .recovery-list { list-style: none; display: flex; flex-direction: column; gap: 1.3rem; margin: 1.5rem 0; counter-reset: step-counter; }
    .step { display: flex; gap: 1.2rem; align-items: flex-start; }
    .step-num { font-size: 1.3rem; font-weight: 700; color: #5c7a4e; min-width: 2rem; text-align: right; line-height: 1.3; }
    .step h4 { font-size: 0.95rem; font-weight: 700; color: #2d5016; margin-bottom: 0.3rem; }
    .step p { font-size: 0.9rem; color: #4a4a3e; line-height: 1.7; margin-bottom: 0; }

    .faq-section { margin-top: 3rem; }
    .faq-item { border: 1px solid rgba(45,80,22,0.12); border-radius: 10px; margin-bottom: 0.6rem; overflow: hidden; }
    .faq-btn { width: 100%; background: none; border: none; text-align: left; padding: 1rem 1.4rem; font-size: 0.95rem; font-weight: 600; color: #2d5016; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-family: inherit; transition: background 0.2s; }
    .faq-btn:hover { background: rgba(45,80,22,0.04); }
    .faq-toggle { font-size: 1.1rem; transition: transform 0.3s cubic-bezier(0.22,1,0.36,1); }
    .faq-item.open .faq-toggle { transform: rotate(45deg); }
    .faq-body { max-height: 0; overflow: hidden; transition: max-height 0.35s cubic-bezier(0.22,1,0.36,1), padding 0.2s; padding: 0 1.4rem; background: #faf9f6; font-size: 0.9rem; color: #4a4a3e; line-height: 1.75; }
    .faq-item.open .faq-body { max-height: 500px; padding: 0.8rem 1.4rem 1.2rem; }

    .explore-section { margin-top: 4rem; padding-top: 2.5rem; border-top: 1px solid rgba(45,80,22,0.12); }
    .explore-section h2 { font-size: 1.15rem; margin-bottom: 1.2rem; }
    .explore-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
    .explore-card { background: #f4f1ea; border: 1px solid rgba(45,80,22,0.1); border-radius: 10px; padding: 1.1rem; text-decoration: none; transition: transform 0.2s cubic-bezier(0.22,1,0.36,1), box-shadow 0.2s; display: block; }
    .explore-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(45,80,22,0.08); }
    .explore-card-emoji { font-size: 1.3rem; margin-bottom: 0.4rem; }
    .explore-card h3 { font-size: 0.87rem; font-weight: 600; color: #2d5016; margin-bottom: 0.25rem; }
    .explore-card p { font-size: 0.8rem; color: #4a4a3e; line-height: 1.5; margin-bottom: 0; }

    .cta-wrap { background: linear-gradient(135deg, #1a2e1a, #243324); border-radius: 14px; padding: 3rem 2rem; text-align: center; margin: 3rem 0 1.5rem; }
    .cta-wrap h2 { font-family: Georgia, serif; font-size: 1.45rem; font-weight: 400; color: #f5f0e8; margin: 0 auto 0.8rem; line-height: 1.3; }
    .cta-wrap p { color: rgba(245,240,232,0.7); font-size: 0.95rem; margin-bottom: 1.5rem; max-width: 480px; margin-left: auto; margin-right: auto; }
    .cta-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .btn-primary { display: inline-block; background: #4a7c59; color: white; padding: 0.7rem 1.6rem; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 0.92rem; transition: background 0.2s, transform 0.15s; }
    .btn-primary:hover { background: #3d6349; transform: translateY(-1px); }
    .btn-ghost { display: inline-block; background: rgba(255,255,255,0.1); color: #f5f0e8; padding: 0.7rem 1.6rem; border-radius: 8px; text-decoration: none; font-weight: 500; font-size: 0.92rem; border: 1px solid rgba(255,255,255,0.2); transition: background 0.2s; }
    .btn-ghost:hover { background: rgba(255,255,255,0.15); }

    .footer { background: #f4f1ea; border-top: 1px solid rgba(45,80,22,0.12); padding: 2.5rem 2rem; margin-top: 4rem; }
    .footer-inner { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 2rem; }
    .footer-brand p { font-size: 0.85rem; color: #4a4a3e; line-height: 1.65; margin-top: 0.5rem; }
    .footer h4 { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #5c7a4e; margin-bottom: 0.8rem; }
    .footer ul { list-style: none; display: flex; flex-direction: column; gap: 0.4rem; }
    .footer a { font-size: 0.85rem; color: #4a4a3e; text-decoration: none; transition: color 0.2s; }
    .footer a:hover { color: #2d5016; }

    @media (max-width: 768px) {
      .dim-grid { grid-template-columns: 1fr; }
      .compare-wrap { grid-template-columns: 1fr; }
      .stat-grid { grid-template-columns: 1fr 1fr; }
      .explore-grid { grid-template-columns: 1fr 1fr; }
      .footer-inner { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 480px) {
      .nav-links { display: none; }
      .nav-toggle { display: block; }
      .nav-links.open { display: flex; flex-direction: column; position: absolute; top: 100%; left: 0; right: 0; background: white; border-bottom: 1px solid rgba(45,80,22,0.1); padding: 1rem; box-shadow: 0 8px 20px rgba(0,0,0,0.08); }
      .dropdown-menu { position: static; box-shadow: none; border: none; padding-left: 1rem; background: transparent; }
      .explore-grid { grid-template-columns: 1fr; }
      .footer-inner { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  <div class="reading-progress" id="reading-progress" role="progressbar" aria-label="Reading progress"></div>

  <header class="header" role="banner">
    <nav class="nav" aria-label="Main navigation">
      <a href="index.html" class="nav-logo" aria-label="The Clearing home"><span>🌿</span> The Clearing</a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
      <ul class="nav-links">
        <li><a href="quiz.html">Quiz</a></li>
        <li><a href="recovery.html">Recover</a></li>
        <li class="nav-dropdown">
          <a href="why.html" class="dropdown-trigger">Understand ▾</a>
          <ul class="dropdown-menu">
            <li><a href="ai-fatigue.html">AI Fatigue</a></li>
            <li><a href="signs-ai-fatigue.html">10 Warning Signs</a></li>
            <li><a href="research.html">The Science</a></li>
            <li><a href="stats.html">Statistics</a></li>
            <li><a href="compare.html">Tool Comparison</a></li>
            <li><a href="mindset.html">Mental Models</a></li>
            <li><a href="glossary.html">Glossary</a></li>
          </ul>
        </li>
        <li class="nav-dropdown">
          <a href="stories.html" class