#!/usr/bin/env python3
"""Build testimonials-campaign.html"""

# ── Head (styles + nav + hero) ──────────────────────────────────────────────
head = """<!DOCTYPE html>
<html lang="en" data-theme="dark" style="contain-intrinsic-size:auto,auto;content-visibility:auto;">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Engineer Testimonials Campaign — Real Stories, Real Recovery | The Clearing</title>
<meta name="description" content="10 engineers shared their AI fatigue recovery stories. Submit yours or nominate a colleague. Real stories from the frontlines of AI fatigue."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="https://clearing-ai.com/testimonials-campaign.html"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="https://clearing-ai.com/testimonials-campaign.html"/>
<meta property="og:title" content="Engineer Testimonials Campaign — Real Stories, Real Recovery"/>
<meta property="og:description" content="10 engineers shared their AI fatigue recovery stories. Your story could help someone else feel less alone."/>
<meta property="og:image" content="https://clearing-ai.com/og-image.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","name":"Engineer Testimonials Campaign","description":"The Clearing testimonials campaign hub — submit your story, use outreach templates, read 10 real engineer recovery stories.","url":"https://clearing-ai.com/testimonials-campaign.html","isPartOf":{"@type":"WebSite","name":"The Clearing","url":"https://clearing-ai.com"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://clearing-ai.com"},{"@type":"ListItem","position":2,"name":"Community","item":"https://clearing-ai.com/community.html"},{"@type":"ListItem","position":3,"name":"Testimonials Campaign","item":"https://clearing-ai.com/testimonials-campaign.html"}]}}
</script>
<style>
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:#111411;color:#e8e4dc;line-height:1.6}
[data-theme="light"] body{background:#fafaf8;color:#2a2a22}
.skip-link{position:absolute;top:-100%;left:1rem;background:#2d5016;color:white;padding:.5rem 1rem;border-radius:0 0 6px 6px;text-decoration:none;font-size:.85rem;z-index:999}
.skip-link:focus{top:0}
.reading-progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#4a7c59,#7aab8a);width:0%;z-index:100;pointer-events:none}
header{background:rgba(17,20,17,.97);border-bottom:1px solid rgba(90,140,90,.15);position:sticky;top:0;z-index:50;backdrop-filter:blur(12px)}
[data-theme="light"] header{background:rgba(250,250,248,.97);border-color:rgba(45,80,22,.1)}
.nav{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:10px 20px;gap:16px}
.nav-logo{font-weight:700;font-size:15px;color:#7aab8a;text-decoration:none;display:flex;align-items:center;gap:6px}
[data-theme="light"] .nav-logo{color:#2d5016}
.nav-links{display:flex;align-items:center;gap:2px;flex-wrap:wrap}
.nav-links a{padding:6px 12px;color:rgba(232,228,220,.6);text-decoration:none;font-size:.875rem;font-weight:500;border-radius:6px;transition:color .2s,background .2s}
.nav-links a:hover{color:#e8e4dc;background:rgba(90,140,90,.12)}
[data-theme="light"] .nav-links a{color:rgba(42,42,34,.65)}
[data-theme="light"] .nav-links a:hover{color:#2a2a22;background:rgba(45,80,22,.07)}
.theme-toggle{background:rgba(90,140,90,.1);border:1px solid rgba(90,140,90,.2);color:#7aab8a;padding:5px 12px;border-radius:20px;cursor:pointer;font-size:.82rem;font-family:inherit;transition:background .2s}
.theme-toggle:hover{background:rgba(90,140,90,.2)}
[data-theme="light"] .theme-toggle{background:rgba(45,80,22,.07);border-color:rgba(45,80,22,.15);color:#5c7a4e}
.page-hero{background:linear-gradient(135deg,#1a2e1a 0%,#243324 60%,#1e2e1e 100%);color:#f5f0e8;padding:5rem 2rem 4rem;text-align:center;position:relative;overflow:hidden}
.page-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(90,140,90,.15) 0%,transparent 60%);pointer-events:none}
.hero-eyebrow{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#7aab8a;margin-bottom:1rem;font-weight:500}
.page-hero h1{font-family:Georgia,serif;font-size:clamp(1.8rem,5vw,3rem);font-weight:400;line-height:1.2;max-width:680px;margin:0 auto 1rem}
.hero-sub{font-size:1rem;color:rgba(245,240,232,.62);max-width:520px;margin:0 auto 1.5rem;line-height:1.65}
.hero-cta-row{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap}
.btn{display:inline-block;padding:.65rem 1.5rem;border-radius:8px;font-size:.9rem;font-weight:600;text-decoration:none;transition:transform .15s,box-shadow .15s;cursor:pointer;border:none;font-family:inherit}
.btn-primary{background:#4a7c59;color:#fff}
.btn-primary:hover{background:#5a8c69;transform:translateY(-1px);box-shadow:0 4px 16px rgba(74,124,89,.3)}
.btn-secondary{background:rgba(90,140,90,.12);color:#7aab8a;border:1px solid rgba(90,140,90,.25)}
.btn-secondary:hover{background:rgba(90,140,90,.2);transform:translateY(-1px)}
[data-theme="light"] .btn-secondary{background:rgba(45,80,22,.07);color:#2d5016;border-color:rgba(45,80,22,.2)}
.hero-stats{display:flex;justify-content:center;gap:2.5rem;flex-wrap:wrap;margin-top:1.5rem}
.hero-stat{text-align:center}
.hero-stat strong{display:block;font-size:1.6rem;font-weight:700;color:#7aab8a;line-height:1}
.hero-stat span{font-size:.72rem;color:rgba(245,240,232,.5);text-transform:uppercase;letter-spacing:.08em;margin-top:.2rem;display:block}
.content-wrap{max-width:900px;margin:0 auto;padding:4rem 2rem 6rem}
h2{font-family:Georgia,serif;font-size:clamp(1.3rem,3vw,1.7rem);font-weight:400;color:#e8e4dc;margin-bottom:1rem}
[data-theme="light"] h2{color:#2a2a22}
.section-intro{font-size:1rem;color:rgba(232,228,220,.6);line-height:1.75;margin-bottom:2rem;max-width:640px}
[data-theme="light"] .section-intro{color:rgba(42,42,34,.65)}
.section{margin-bottom:4rem}
.stories-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;margin-bottom:2rem}
.story-card{background:#1a1e1a;border:1px solid rgba(90,140,90,.18);border-radius:12px;padding:1.5rem;position:relative;transition:transform .2s cubic-bezier(.22,1,.36,1),box-shadow .2s}
[data-theme="light"] .story-card{background:#f5f2ec;border-color:rgba(45,80,22,.1)}
.story-card:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.12)}
.quote-mark{font-family:Georgia,serif;font-size:3.5rem;line-height:.8;color:#5c7a4e;opacity:.25;position:absolute;top:.8rem;left:1.2rem;pointer-events:none;user-select:none}
.tier-badge{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .55rem;border-radius:20px;margin-bottom:.75rem}
.tier-2{background:rgba(180,150,80,.15);color:#c8a840;border:1px solid rgba(180,150,80,.3)}
.tier-3{background:rgba(160,100,50,.15);color:#c87040;border:1px solid rgba(160,100,50,.3)}
.tier-4{background:rgba(150,60,60,.15);color:#c85050;border:1px solid rgba(150,60,60,.3)}
.story-quote{font-size:.9rem;color:rgba(232,228,220,.78);line-height:1.7;font-style:italic;margin-bottom:1rem}
[data-theme="light"] .story-quote{color:rgba(42,42,34,.78)}
.story-meta{font-size:.75rem;color:rgba(232,228,220,.38);display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin-bottom:.75rem}
[data-theme="light"] .story-meta{color:rgba(42,42,34,.42)}
.story-share{display:flex;gap:.4rem;flex-wrap:wrap}
.share-btn-sm{display:inline-flex;align-items:center;gap:.3rem;font-size:.7rem;font-weight:600;padding:.22rem .6rem;border-radius:5px;cursor:pointer;border:none;font-family:inherit;background:rgba(90,140,90,.1);color:#7aab8a;transition:background .15s;text-decoration:none}
.share-btn-sm:hover{background:rgba(90,140,90,.2)}
.email-template{background:#1a1e1a;border:1px solid rgba(90,140,90,.15);border-radius:10px;padding:1.5rem 1.5rem 1.5rem 1.75rem;margin-bottom:1.25rem;position:relative}
[data-theme="light"] .email-template{background:#f0ede8;border-color:rgba(45,80,22,.12)}
.template-label{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#7aab8a;margin-bottom:.4rem}
.template-subject{font-size:.8rem;color:rgba(232,228,220,.45);margin-bottom:.75rem}
[data-theme="light"] .template-subject{color:rgba(42,42,34,.5)}
.template-body{font-size:.87rem;color:rgba(232,228,220,.8);line-height:1.78;white-space:pre-wrap;font-family:Georgia,serif}
[data-theme="light"] .template-body{color:rgba(42,42,34,.8)}
.copy-btn{position:absolute;top:1rem;right:1rem;font-size:.72rem;font-weight:600;padding:.25rem .75rem;border-radius:5px;cursor:pointer;border:1px solid rgba(90,140,90,.25);background:rgba(90,140,90,.08);color:#7aab8a;font-family:inherit;transition:background .15s}
.copy-btn:hover{background:rgba(90,140,90,.18)}
.copy-btn.copied{background:rgba(74,124,89,.25)}
.steps-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1.25rem;margin-bottom:2rem}
.step-card{background:rgba(45,80,22,.06);border:1px solid rgba(90,140,90,.14);border-radius:10px;padding:1.5rem}
[data-theme="light"] .step-card{background:rgba(45,80,22,.04);border-color:rgba(45,80,22,.1)}
.step-num{display:inline-block;width:28px;height:28px;background:#4a7c59;color:white;border-radius:50%;font-size:.8rem;font-weight:700;text-align:center;line-height:28px;margin-bottom:.75rem}
.step-card h3{font-size:1rem;font-weight:600;color:#e8e4dc;font-family:-apple-system,sans-serif;margin-bottom:.5rem}
[data-theme="light"] .step-card h3{color:#2a2a22}
.step-card p{font-size:.88rem;color:rgba(232,228,220,.6);margin-bottom:0}
[data-theme="light"] .step-card p{color:rgba(42,42,34,.65)}
.share-row{display:flex;gap:.75rem;flex-wrap:wrap;margin-bottom:1.5rem}
.share-link{display:inline-flex;align-items:center;gap:.4rem;padding:.6rem 1.2rem;border-radius:8px;font-size:.875rem;font-weight:600;text-decoration:none;transition:transform .15s,opacity .15s}
.share-link:hover{transform:translateY(-1px);opacity:.9}
.share-twitter{background:#1da1f2;color:white}
.share-linkedin{background:#0077b5;color:white}
.share-hn{background:#ff6600;color:white}
.share-copy-btn{background:rgba(90,140,90,.15);color:#7aab8a;border:1px solid rgba(90,140,90,.25);cursor:pointer;font-family:inherit;font-size:.875rem}
.share-copy-btn:hover{background:rgba(90,140,90,.22);transform:translateY(-1px)}
.share-text-row{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem}
.form-section{background:rgba(45,80,22,.06);border:1px solid rgba(90,140,90,.14);border-radius:14px;padding:2.5rem;margin-bottom:2rem}
[data-theme="light"] .form-section{background:rgba(45,80,22,.04);border-color:rgba(45,80,22,.1)}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1rem}
@media(max-width:600px){.form-grid{grid-template-columns:1fr}}
.form-field{display:flex;flex-direction:column;gap:.4rem}
.form-field label{font-size:.82rem;font-weight:600;color:rgba(232,228,220,.7)}
[data-theme="light"] .form-field label{color:rgba(42,42,34,.7)}
.form-field input,.form-field textarea,.form-field select{background:rgba(255,255,255,.04);border:1px solid rgba(90,140,90,.2);border-radius:7px;padding:.6rem .85rem;color:#e8e4dc;font-size:.9rem;font-family:inherit;transition:border-color .2s;width:100%}
[data-theme="light"] .form-field input,[data-theme="light"] .form-field textarea,[data-theme="light"] .form-field select{background:rgba(255,255,255,.6);border-color:rgba(45,80,22,.2);color:#2a2a22}
.form-field input:focus,.form-field textarea:focus,.form-field select:focus{outline:none;border-color:#4a7c59}
.form-field textarea{resize:vertical;min-height:110px}
.form-field.full{grid-column:1/-1}
.btn-submit{background:#4a7c59;color:white;padding:.75rem 2rem;border-radius:8px;font-size:.95rem;font-weight:700;border:none;cursor:pointer;font-family:inherit;transition:background .15s,transform .15s;margin-top:1.5rem;display:inline-block}
.btn-submit:hover{background:#5a8c69;transform:translateY(-1px)}
.form-note{font-size:.8rem;color:rgba(232,228,220,.4);margin-top:.75rem}
[data-theme="light"] .form-note{color:rgba(42,42,34,.45)}
.success-msg{background:rgba(74,124,89,.15);border:1px solid rgba(74,124,89,.3);border-radius:10px;padding:1.5rem;text-align:center;display:none}
.success-msg.show{display:block}
.success-msg p{color:#7aab8a;font-weight:600;margin-bottom:.25rem;font-size:1rem}
.success-msg span{font-size:.85rem;color:rgba(232,228,220,.6);display:block;margin-top:.5rem}
.guide-card{background:rgba(45,80,22,.05);border:1px solid rgba(90,140,90,.12);border-radius:10px;padding:1.5rem;margin-bottom:1.25rem}
[data-theme="light"] .guide-card{background:rgba(45,80,22,.03);border-color:rgba(45,80,22,.1)}
.guide-card h3{font-size:1rem;font-weight:600;color:#e8e4dc;font-family:-apple-system,sans-serif;margin-bottom:.75rem}
[data-theme="light"] .guide-card h3{color:#2a2a22}
.guide-card ul{list-style:none;padding:0}
.guide-card li{font-size:.88rem;color:rgba(232,228,220,.65);padding:.4rem 0;border-bottom:1px solid rgba(90,140,90,.08);display:flex;gap:.5rem;align-items:flex-start}
[data-theme="light"] .guide-card li{color:rgba(42,42,34,.65);border-color:rgba(45,80,22,.08)}
.guide-card li::before{content:'\\2192';color:#7aab8a;flex-shrink:0;font-weight:700}
[data-theme="light"] .guide-card li::before{color:#2d5016}
.guide-card li:last-child{border-bottom:none}
.incentive-box{background:linear-gradient(135deg,rgba(74,124,89,.12),rgba(45,80,22,.08));border:1px solid rgba(74,124,89,.25);border-radius:12px;padding:1.5rem;margin-bottom:2rem}
[data-theme="light"] .incentive-box{background:linear-gradient(135deg,rgba(45,80,22,.06),rgba(45,80,22,.04));border-color:rgba(45,80,22,.2)}
.incentive-box h3{color:#7aab8a;font-size:1rem;font-weight:600;margin-bottom:.5rem;font-family:-apple-system,sans-serif}
[data-theme="light"] .incentive-box h3{color:#2d5016}
.incentive-box p{color:rgba(232,228,220,.72);font-size:.9rem;margin-bottom:0}
[data-theme="light"] .incentive-box p{color:rgba(42,42,34,.72)}
.divider{border:none;border-top:1px solid rgba(90,140,90,.12);margin:3rem 0}
[data-theme="light"] .divider{border-color:rgba(45,80,22,.1)}
footer{background:#0d110d;border-top:1px solid rgba(90,140,90,.1);padding:2rem;text-align:center}
[data-theme="light"] footer{background:#f0ede8;border-color:rgba(45,80,22,.1)}
footer p{font-size:.82rem;color:rgba(232,228,220,.35);margin-bottom:.5rem}
[data-theme="light"] footer p{color:rgba(42,42,34,.4)}
footer a{color:rgba(232,228,220,.45);text-decoration:none}
[data-theme="light"] footer a{color:rgba(42,42,34,.5)}
footer a:hover{color:#7aab8a}
[data-theme="light"] footer a:hover{color:#2d5016}
.footer-links{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:.75rem;font-size:.8rem}
@media(max-width:600px){.stories-grid,.steps-grid{grid-template-columns:1fr}.form-section{padding:1.5rem}.nav-links{display:none}}
</style>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='28'>🌿</text></svg>"/>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<div class="reading-progress" id="progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
<header>
<nav class="nav" aria-label="Main navigation">
<a href="/" class="nav-logo" aria-label="The Clearing home">🌿 The Clearing</a>
<div class="nav-links">
<a href="/">Home</a><a href="/quiz.html">Take the Quiz</a><a href="/recovery.html">Recovery</a><a href="/community.html">Community</a><a href="/newsletter.html">Newsletter</a><a href="/testimonials.html">Testimonials</a><a href="/testimonials-campaign.html" aria-current="page">Campaign</a>
</div>
<button class="theme-toggle" aria-label="Toggle color theme">🌙</button>
</nav>
</header>
<main id="main">
<section class="page-hero" aria-labelledby="hero-title">
<p class="hero-eyebrow">Engineer Testimonials Campaign</p>
<h1 id="hero-title">Your Story Is Someone Else's Proof They're Not Alone</h1>
<p class="hero-sub">10 engineers have shared their AI fatigue recovery stories. Every story shared helps someone else realize they're not lazy, not broken -- they're experiencing something real with a name and a way out.</p>
<div class="hero-cta-row">
<a href="#submit" class="btn btn-primary">Share Your Story</a>
<a href="#outreach" class="btn btn-secondary">Use Outreach Templates</a>
<a href="#stories" class="btn btn-secondary">Read the Stories</a>
</div>
<div class="hero-stats">
<div class="hero-stat"><strong>10</strong><span>Stories shared</span></div>
<div class="hero-stat"><strong>6+</strong><span>Roles represented</span></div>
<div class="hero-stat"><strong>3,000+</strong><span>Quiz takers</span></div>
</div>
</section>
<div class="content-wrap">
'''

# ── Share section ────────────────────────────────────────────────────────────
share_section = '''
<section class="section" id="share" aria-labelledby="share-title">
<h2 id="share-title">Spread the Word</h2>
<p class="section-intro">If you know an engineer struggling with AI fatigue, share this campaign. One message can start a conversation that changes someone's week.</p>
<div class="share-row">
<a href="https://twitter.com/intent/tweet?text=I%20just%20read%2010%20real%20engineers%27%20AI%20fatigue%20recovery%20stories.%20If%20you%27ve%20felt%20the%20same%2C%20you%27re%20not%20alone.%20https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html" class="share-link share-twitter" target="_blank" rel="noopener">X Share on Twitter</a>
<a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html&title=10+Engineers+Shared+Their+AI+Fatigue+Stories" class="share-link share-linkedin" target="_blank" rel="noopener">Share on LinkedIn</a>
<a href="https://news.ycombinator.com/submit" class="share-link share-hn" target="_blank" rel="noopener">Submit to Hacker News</a>
<button class="share-link share-copy-btn" id="copy-link-btn" onclick="copyLink()">Copy Link</button>
</div>
<div class="share-text-row">
<p style="font-size:.78rem;color:rgba(232,228,220,.38);margin:0;width:100%">Pre-written share text:</p>
<button class="share-btn-sm" onclick="copyShareText('twitter')">Copy Twitter text</button>
<button class="share-btn-sm" onclick="copyShareText('linkedin')">Copy LinkedIn text</button>
<button class="share-btn-sm" onclick="copyShareText('hn')">Copy HN text</button>
</div>
</section>

<hr class="divider"/>

<section class="section" id="how" aria-labelledby="how-title">
<h2 id="how-title">How This Campaign Works</h2>
<p class="section-intro">Real stories from real engineers are the most powerful thing this community has. Here's how you can help collect and amplify them.</p>
<div class="steps-grid">
<div class="step-card"><span class="step-num">1</span><h3>Read the Stories</h3><p>10 engineers shared what AI fatigue felt like, what helped them recover, and what they wish they knew sooner.</p></div>
<div class="step-card"><span class="step-num">2</span><h3>Share Your Own</h3><p>Your recovery story is someone else's proof they're not broken. Takes 5 minutes to write.</p></div>
<div class="step-card"><span class="step-num">3</span><h3>Nominate a Colleague</h3><p>Know someone struggling quietly? Use the outreach templates below to send a thoughtful note.</p></div>
<div class="step-card"><span class="step-num">4</span><h3>Spread the Word</h3><p>Share the campaign on Twitter, LinkedIn, Slack, or HN. Every share reaches engineers who need this.</p></div>
</div>
</section>

<hr class="divider"/>

<section class="section" id="stories" aria-labelledby="stories-title">
<h2 id="stories-title">Real Stories, Real Engineers</h2>
<p class="section-intro">Every story here is from an engineer who took the AI Fatigue Quiz or read our resources. Names and identifying details are removed. The feelings are real.</p>

<div class="stories-grid">

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-3">Tier 3 -- Real Fatigue</span>
<p class="story-quote">"I have fifteen years of experience. I have shipped compilers, distributed systems, a database that did not catch fire in production. Then, about eighteen months ago, I started noticing something: I could not debug things the way I used to."</p>
<div class="story-meta"><span>Principal Engineer</span><span> - </span><span>15 years exp</span><span> - </span><span>Tier 3</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Principal Engineer','I have fifteen years of experience, then I started noticing I could not debug things the way I used to.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','Principal Engineer','I have fifteen years of experience, then I started noticing I could not debug things the way I used to.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-2">Tier 2 -- Some Fatigue</span>
<p class="story-quote">"I feel guilty even writing this. The discourse around AI tools is so positive that saying anything less than 'this has been transformative' feels like admitting I am not trying hard enough."</p>
<div class="story-meta"><span>Mid-level Engineer</span><span> - </span><span>4 years exp</span><span> - </span><span>Tier 2</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Mid-level Engineer','I feel guilty writing this. Saying anything less than this has been transformative feels like admitting I am not trying hard enough.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','Mid-level Engineer','I feel guilty writing this. Saying anything less than this has been transformative feels like admitting I am not trying hard enough.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-4">Tier 4 -- Need a Real Break</span>
<p class="story-quote">"I could see it happening and I did not have the language for it. HR thought I was worried about nothing. The CEO pointed to the velocity numbers. I felt like I was watching my team slowly lose something and nobody else could see it."</p>
<div class="story-meta"><span>Engineering Manager</span><span> - </span><span>Team of 8</span><span> - </span><span>Tier 4</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Engineering Manager','I could see it happening and I did not have the language for it. I felt like I was watching my team slowly lose something.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','Engineering Manager','I could see it happening and I did not have the language for it. I felt like I was watching my team slowly lose something.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-3">Tier 3 -- Real Fatigue</span>
<p class="story-quote">"What I did not notice happening: I stopped talking to my teammates. Not because I did not like them. Because AI was a faster answer. And in a small overlap window, speed felt critical."</p>
<div class="story-meta"><span>Backend Engineer</span><span> - </span><span>7 years exp</span><span> - </span><span>Tier 3</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Backend Engineer','What I did not notice: I stopped talking to my teammates. Not because I did not like them. Because AI was a faster answer.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','Backend Engineer','What I did not notice: I stopped talking to my teammates. Not because I did not like them. Because AI was a faster answer.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-3">Tier 3 -- Real Fatigue</span>
<p class="story-quote">"About eighteen months into heavy AI tool use, I realized I could not sit with a problem anymore. I would literally reach for an AI tool before I had finished reading a bug report. Not because I was lazy. Because the discomfort of not knowing had become unbearable."</p>
<div class="story-meta"><span>Senior Engineer</span><span> - </span><span>9 years exp</span><span> - </span><span>Tier 3</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Senior Engineer','18 months into heavy AI tool use, I realized I could not sit with a problem anymore. The discomfort of not knowing had become unbearable.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','Senior Engineer','18 months into heavy AI tool use, I realized I could not sit with a problem anymore. The discomfort of not knowing had become unbearable.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-3">Tier 3 -- Real Fatigue</span>
<p class="story-quote">"My team adopted AI note-taking during incidents. It sounds minor. Here is what it did to us: during post-mortems, we read AI summaries of what happened instead of reconstructing it ourselves. Slowly, we stopped building the mental model of our own systems."</p>
<div class="story-meta"><span>SRE / On-call Engineer</span><span> - </span><span>5 years exp</span><span> - </span><span>Tier 3</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','SRE Engineer','My team adopted AI note-taking during incidents. We read AI summaries instead of reconstructing it ourselves. We stopped building the mental model of our own systems.')">X Tweet</button>
<button class="share-btn-sm" onclick="shareStory('linkedin','SRE Engineer','My team adopted AI note-taking during incidents. We read AI summaries instead of reconstructing it ourselves. We stopped building the mental model of our own systems.')">LinkedIn</button>
</div>
</div>

<div class="story-card">
<span class="quote-mark" aria-hidden="true">"</span>
<span class="tier-badge tier-3">Tier 3 -- Real Fatigue</span>
<p class="story-quote">"I am the person who used to be the most skeptical on my team. I would argue against technology hype. Then AI coding tools got good and I rationalized my way in. Within a year, I was the person most dependent on them. Not because they were better -- because they were faster."</p>
<div class="story-meta"><span>Staff Engineer</span><span> - </span><span>11 years exp</span><span> - </span><span>Tier 3</span></div>
<div class="story-share">
<button class="share-btn-sm" onclick="shareStory('twitter','Staff Engineer','I was the most skeptical on my team. Within a year of AI tools, I was the most dependent. Not because they were better -- because they were faster.')">