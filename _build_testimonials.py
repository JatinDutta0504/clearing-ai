#!/usr/bin/env python3
"""Build testimonials-campaign.html"""

styles = "*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:-apple-system,BlinkMacSystemFont,\"Segoe UI\",Roboto,sans-serif;background:#111411;color:#e8e4dc;line-height:1.6}[data-theme=\"light\"] body{background:#fafaf8;color:#2a2a22}.skip-link{position:absolute;top:-100%;left:1rem;background:#2d5016;color:white;padding:.5rem 1rem;border-radius:0 0 6px 6px;text-decoration:none;font-size:.85rem;z-index:999}.skip-link:focus{top:0}.reading-progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,#4a7c59,#7aab8a);width:0%;z-index:100;pointer-events:none}header{background:rgba(17,20,17,.97);border-bottom:1px solid rgba(90,140,90,.15);position:sticky;top:0;z-index:50;backdrop-filter:blur(12px)}[data-theme=\"light\"] header{background:rgba(250,250,248,.97);border-color:rgba(45,80,22,.1)}.nav{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:10px 20px;gap:16px}.nav-logo{font-weight:700;font-size:15px;color:#7aab8a;text-decoration:none;display:flex;align-items:center;gap:6px}[data-theme=\"light\"] .nav-logo{color:#2d5016}.nav-links{display:flex;align-items:center;gap:2px;flex-wrap:wrap}.nav-links a{padding:6px 12px;color:rgba(232,228,220,.6);text-decoration:none;font-size:.875rem;font-weight:500;border-radius:6px;transition:color .2s,background .2s}.nav-links a:hover{color:#e8e4dc;background:rgba(90,140,90,.12)}[data-theme=\"light\"] .nav-links a{color:rgba(42,42,34,.65)}[data-theme=\"light\"] .nav-links a:hover{color:#2a2a22;background:rgba(45,80,22,.07)}.theme-toggle{background:rgba(90,140,90,.1);border:1px solid rgba(90,140,90,.2);color:#7aab8a;padding:5px 12px;border-radius:20px;cursor:pointer;font-size:.82rem;font-family:inherit;transition:background .2s}.theme-toggle:hover{background:rgba(90,140,90,.2)}[data-theme=\"light\"] .theme-toggle{background:rgba(45,80,22,.07);border-color:rgba(45,80,22,.15);color:#5c7a4e}.page-hero{background:linear-gradient(135deg,#1a2e1a 0%,#243324 60%,#1e2e1e 100%);color:#f5f0e8;padding:5rem 2rem 4rem;text-align:center;position:relative;overflow:hidden}.page-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 30% 50%,rgba(90,140,90,.15) 0%,transparent 60%);pointer-events:none}.hero-eyebrow{font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:#7aab8a;margin-bottom:1rem;font-weight:500}.page-hero h1{font-family:Georgia,serif;font-size:clamp(1.8rem,5vw,3rem);font-weight:400;line-height:1.2;max-width:680px;margin:0 auto 1rem}.hero-sub{font-size:1rem;color:rgba(245,240,232,.62);max-width:520px;margin:0 auto 1.5rem;line-height:1.65}.hero-cta-row{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap}.btn{display:inline-block;padding:.65rem 1.5rem;border-radius:8px;font-size:.9rem;font-weight:600;text-decoration:none;transition:transform .15s,box-shadow .15s;cursor:pointer;border:none;font-family:inherit}.btn-primary{background:#4a7c59;color:#fff}.btn-primary:hover{background:#5a8c69;transform:translateY(-1px);box-shadow:0 4px 16px rgba(74,124,89,.3)}.btn-secondary{background:rgba(90,140,90,.12);color:#7aab8a;border:1px solid rgba(90,140,90,.25)}.btn-secondary:hover{background:rgba(90,140,90,.2);transform:translateY(-1px)}[data-theme=\"light\"] .btn-secondary{background:rgba(45,80,22,.07);color:#2d5016;border-color:rgba(45,80,22,.2)}.hero-stats{display:flex;justify-content:center;gap:2.5rem;flex-wrap:wrap;margin-top:1.5rem}.hero-stat{text-align:center}.hero-stat strong{display:block;font-size:1.6rem;font-weight:700;color:#7aab8a;line-height:1}.hero-stat span{font-size:.72rem;color:rgba(245,240,232,.5);text-transform:uppercase;letter-spacing:.08em;margin-top:.2rem;display:block}.content-wrap{max-width:900px;margin:0 auto;padding:4rem 2rem 6rem}h2{font-family:Georgia,serif;font-size:clamp(1.3rem,3vw,1.7rem);font-weight:400;color:#e8e4dc;margin-bottom:1rem}[data-theme=\"light\"] h2{color:#2a2a22}.section-intro{font-size:1rem;color:rgba(232,228,220,.6);line-height:1.75;margin-bottom:2rem;max-width:640px}[data-theme=\"light\"] .section-intro{color:rgba(42,42,34,.65)}.section{margin-bottom:4rem}.stories-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;margin-bottom:2rem}.story-card{background:#1a1e1a;border:1px solid rgba(90,140,90,.18);border-radius:12px;padding:1.5rem;position:relative;transition:transform .2s cubic-bezier(.22,1,.36,1),box-shadow .2s}[data-theme=\"light\"] .story-card{background:#f5f2ec;border-color:rgba(45,80,22,.1)}.story-card:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(0,0,0,.12)}.quote-mark{font-family:Georgia,serif;font-size:3.5rem;line-height:.8;color:#5c7a4e;opacity:.25;position:absolute;top:.8rem;left:1.2rem;pointer-events:none;user-select:none}.tier-badge{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .55rem;border-radius:20px;margin-bottom:.75rem}.tier-2{background:rgba(180,150,80,.15);color:#c8a840;border:1px solid rgba(180,150,80,.3)}.tier-3{background:rgba(160,100,50,.15);color:#c87040;border:1px solid rgba(160,100,50,.3)}.tier-4{background:rgba(150,60,60,.15);color:#c85050;border:1px solid rgba(150,60,60,.3)}.story-quote{font-size:.9rem;color:rgba(232,228,220,.78);line-height:1.7;font-style:italic;margin-bottom:1rem}[data-theme=\"light\"] .story-quote{color:rgba(42,42,34,.78)}.story-meta{font-size:.75rem;color:rgba(232,228,220,.38);display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin-bottom:.75rem}[data-theme=\"light\"] .story-meta{color:rgba(42,42,34,.42)}.story-share{display:flex;gap:.4rem;flex-wrap:wrap}.share-btn-sm{display:inline-flex;align-items:center;gap:.3rem;font-size:.7rem;font-weight:600;padding:.22rem .6rem;border-radius:5px;cursor:pointer;border:none;font-family:inherit;background:rgba(90,140,90,.1);color:#7aab8a;transition:background .15s;text-decoration:none}.share-btn-sm:hover{background:rgba(90,140,90,.2)}.email-template{background:#1a1e1a;border:1px solid rgba(90,140,90,.15);border-radius:10px;padding:1.5rem 1.5rem 1.5rem 1.75rem;margin-bottom:1.25rem;position:relative}[data-theme=\"light\"] .email-template{background:#f0ede8;border-color:rgba(45,80,22,.12)}.template-label{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#7aab8a;margin-bottom:.4rem}.template-subject{font-size:.8rem;color:rgba(232,228,220,.45);margin-bottom:.75rem}[data-theme=\"light\"] .template-subject{color:rgba(42,42,34,.5)}.template-body{font-size:.87rem;color:rgba(232,228,220,.8);line-height:1.78;white-space:pre-wrap;font-family:Georgia,serif}[data-theme=\"light\"] .template-body{color:rgba(42,42,34,.8)}.copy-btn{position:absolute;top:1rem;right:1rem;font-size:.72rem;font-weight:600;padding:.25rem .75rem;border-radius:5px;cursor:pointer;border:1px solid rgba(90,140,90,.25);background:rgba(90,140,90,.08);color:#7aab8a;font-family:inherit;transition:background .15s}.copy-btn:hover{background:rgba(90,140,90,.18)}.copy-btn.copied{background:rgba(74,124,89,.25)}.steps-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1.25rem;margin-bottom:2rem}.step-card{background:rgba(45,80,22,.06);border:1px solid rgba(90,140,90,.14);border-radius:10px;padding:1.5rem}[data-theme=\"light\"] .step-card{background:rgba(45,80,22,.04);border-color:rgba(45,80,22,.1)}.step-num{display:inline-block;width:28px;height:28px;background:#4a7c59;color:white;border-radius:50%;font-size:.8rem;font-weight:700;text-align:center;line-height:28px;margin-bottom:.75rem}.step-card h3{font-size:1rem;font-weight:600;color:#e8e4dc;font-family:-apple-system,sans-serif;margin-bottom:.5rem}[data-theme=\"light\"] .step-card h3{color:#2a2a22}.step-card p{font-size:.88rem;color:rgba(232,228,220,.6);margin-bottom:0}[data-theme=\"light\"] .step-card p{color:rgba(42,42,34,.65)}.share-row{display:flex;gap:.75rem;flex-wrap:wrap;margin-bottom:1.5rem}.share-link{display:inline-flex;align-items:center;gap:.4rem;padding:.6rem 1.2rem;border-radius:8px;font-size:.875rem;font-weight:600;text-decoration:none;transition:transform .15s,opacity .15s}.share-link:hover{transform:translateY(-1px);opacity:.9}.share-twitter{background:#1da1f2;color:white}.share-linkedin{background:#0077b5;color:white}.share-hn{background:#ff6600;color:white}.share-copy-btn{background:rgba(90,140,90,.15);color:#7aab8a;border:1px solid rgba(90,140,90,.25);cursor:pointer;font-family:inherit;font-size:.875rem}.share-copy-btn:hover{background:rgba(90,140,90,.22);transform:translateY(-1px)}.share-text-row{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem}.form-section{background:rgba(45,80,22,.06);border:1px solid rgba(90,140,90,.14);border-radius:14px;padding:2.5rem;margin-bottom:2rem}[data-theme=\"light\"] .form-section{background:rgba(45,80,22,.04);border-color:rgba(45,80,22,.1)}.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1rem}@media(max-width:600px){.form-grid{grid-template-columns:1fr}}.form-field{display:flex;flex-direction:column;gap:.4rem}.form-field label{font-size:.82rem;font-weight:600;color:rgba(232,228,220,.7)}[data-theme=\"light\"] .form-field label{color:rgba(42,42,34,.7)}.form-field input,.form-field textarea,.form-field select{background:rgba(255,255,255,.04);border:1px solid rgba(90,140,90,.2);border-radius:7px;padding:.6rem .85rem;color:#e8e4dc;font-size:.9rem;font-family:inherit;transition:border-color .2s;width:100%}[data-theme=\"light\"] .form-field input,[data-theme=\"light\"] .form-field textarea,[data-theme=\"light\"] .form-field select{background:rgba(255,255,255,.6);border-color:rgba(45,80,22,.2);color:#2a2a22}.form-field input:focus,.form-field textarea:focus,.form-field select:focus{outline:none;border-color:#4a7c59}.form-field textarea{resize:vertical;min-height:110px}.form-field.full{grid-column:1/-1}.btn-submit{background:#4a7c59;color:white;padding:.75rem 2rem;border-radius:8px;font-size:.95rem;font-weight:700;border:none;cursor:pointer;font-family:inherit;transition:background .15s,transform .15s;margin-top:1.5rem;display:inline-block}.btn-submit:hover{background:#5a8c69;transform:translateY(-1px)}.form-note{font-size:.8rem;color:rgba(232,228,220,.4);margin-top:.75rem}[data-theme=\"light\"] .form-note{color:rgba(42,42,34,.45)}.success-msg{background:rgba(74,124,89,.15);border:1px solid rgba(74,124,89,.3);border-radius:10px;padding:1.5rem;text-align:center;display:none}.success-msg.show{display:block}.success-msg p{color:#7aab8a;font-weight:600;margin-bottom:.25rem;font-size:1rem}.success-msg span{font-size:.85rem;color:rgba(232,228,220,.6);display:block;margin-top:.5rem}.guide-card{background:rgba(45,80,22,.05);border:1px solid rgba(90,140,90,.12);border-radius:10px;padding:1.5rem;margin-bottom:1.25rem}[data-theme=\"light\"] .guide-card{background:rgba(45,80,22,.03);border-color:rgba(45,80,22,.1)}.guide-card h3{font-size:1rem;font-weight:600;color:#e8e4dc;font-family:-apple-system,sans-serif;margin-bottom:.75rem}[data-theme=\"light\"] .guide-card h3{color:#2a2a22}.guide-card ul{list-style:none;padding:0}.guide-card li{font-size:.88rem;color:rgba(232,228,220,.65);padding:.4rem 0;border-bottom:1px solid rgba(90,140,90,.08);display:flex;gap:.5rem;align-items:flex-start}[data-theme=\"light\"] .guide-card li{color:rgba(42,42,34,.65);border-color:rgba(45,80,22,.08)}.guide-card li::before{content:'\\2192';color:#7aab8a;flex-shrink:0;font-weight:700}[data-theme=\"light\"] .guide-card li::before{color:#2d5016}.guide-card li:last-child{border-bottom:none}.incentive-box{background:linear-gradient(135deg,rgba(74,124,89,.12),rgba(45,80,22,.08));border:1px solid rgba(74,124,89,.25);border-radius:12px;padding:1.5rem;margin-bottom:2rem}[data-theme=\"light\"] .incentive-box{background:linear-gradient(135deg,rgba(45,80,22,.06),rgba(45,80,22,.04));border-color:rgba(45,80,22,.2)}.incentive-box h3{color:#7aab8a;font-size:1rem;font-weight:600;margin-bottom:.5rem;font-family:-apple-system,sans-serif}[data-theme=\"light\"] .incentive-box h3{color:#2d5016}.incentive-box p{color:rgba(232,228,220,.72);font-size:.9rem;margin-bottom:0}[data-theme=\"light\"] .incentive-box p{color:rgba(42,42,34,.72)}.divider{border:none;border-top:1px solid rgba(90,140,90,.12);margin:3rem 0}[data-theme=\"light\"] .divider{border-color:rgba(45,80,22,.1)}footer{background:#0d110d;border-top:1px solid rgba(90,140,90,.1);padding:2rem;text-align:center}[data-theme=\"light\"] footer{background:#f0ede8;border-color:rgba(45,80,22,.1)}footer p{font-size:.82rem;color:rgba(232,228,220,.35);margin-bottom:.5rem}[data-theme=\"light\"] footer p{color:rgba(42,42,34,.4)}footer a{color:rgba(232,228,220,.45);text-decoration:none}[data-theme=\"light\"] footer a{color:rgba(42,42,34,.5)}footer a:hover{color:#7aab8a}[data-theme=\"light\"] footer a:hover{color:#2d5016}.footer-links{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:.75rem;font-size:.8rem}@media(max-width:600px){.stories-grid,.steps-grid{grid-template-columns:1fr}.form-section{padding:1.5rem}.nav-links{display:none}}"

# Stories data
stories = [
    ("tier-3", "Tier 3 -- Real Fatigue", "Principal Engineer", "15 years exp", '"I have fifteen years of experience. I have shipped compilers, distributed systems, a database that did not catch fire in production. Then, about eighteen months ago, I started noticing something: I could not debug things the way I used to."'),
    ("tier-2", "Tier 2 -- Some Fatigue", "Mid-level Engineer", "4 years exp", '"I feel guilty even writing this. The discourse around AI tools is so positive that saying anything less than \'this has been transformative\' feels like admitting I am not trying hard enough."'),
    ("tier-4", "Tier 4 -- Need a Real Break", "Engineering Manager", "Team of 8", '"I could see it happening and I did not have the language for it. HR thought I was worried about nothing. The CEO pointed to the velocity numbers. I felt like I was watching my team slowly lose something and nobody else could see it."'),
    ("tier-3", "Tier 3 -- Real Fatigue", "Backend Engineer", "7 years exp", '"What I did not notice happening: I stopped talking to my teammates. Not because I did not like them. Because AI was a faster answer. And in a small overlap window, speed felt critical."'),
    ("tier-3", "Tier 3 -- Real Fatigue", "Senior Engineer", "9 years exp", '"About eighteen months into heavy AI tool use, I realized I could not sit with a problem anymore. I would literally reach for an AI tool before I had finished reading a bug report. Not because I was lazy. Because the discomfort of not knowing had become unbearable."'),
    ("tier-3", "Tier 3 -- Real Fatigue", "SRE / On-call Engineer", "5 years exp", '"My team adopted AI note-taking during incidents. It sounds minor. Here is what it did to us: during post-mortems, we read AI summaries of what happened instead of reconstructing it ourselves. Slowly, we stopped building the mental model of our own systems."'),
    ("tier-3", "Tier 3 -- Real Fatigue", "Staff Engineer", "11 years exp", '"I am the person who used to be the most skeptical on my team. I would argue against technology hype. Then AI coding tools got good and I rationalized my way in. Within a year, I was the person most dependent on them. Not because they were better -- because they were faster."'),
    ("tier-2", "Tier 2 -- Some Fatigue", "Full-stack Engineer", "8 years exp", '"I keep feeling like I am the only one who spends thirty minutes prompting, getting output that is not quite right, and then feeling vaguely dissatisfied. I have started wondering if I am just bad at using these tools -- but I have been building software for eight years."'),
]

def story_card(tier_cls, tier_label, role, exp, quote):
    q_short = quote[:60] + "..."
    return (
        '<div class="story-card">\n'
        '<span class="quote-mark" aria-hidden="true">"</span>\n'
        '<span class="tier-badge ' + tier_cls + '">' + tier_label + '</span>\n'
        '<p class="story-quote">' + quote + '</p>\n'
        '<div class="story-meta"><span>' + role + '</span><span> - </span><span>' + exp + '</span><span> - </span><span>' + tier_label[:4] + '</span></div>\n'
        '<div class="story-share">\n'
        '<button class="share-btn-sm" onclick="shareStory(\'twitter\',\'' + role + '\',\'' + q_short.replace("'", "\\'") + '\')">X Tweet</button>\n'
        '<button class="share-btn-sm" onclick="shareStory(\'linkedin\',\'' + role + '\',\'' + q_short.replace("'", "\\'") + '\')">LinkedIn</button>\n'
        '</div>\n'
        '</div>\n'
    )

stories_html = '\n'.join(story_card(*s) for s in stories)

templates = {
    "A": {
        "label": "Template A -- Colleague You Work With",
        "subject": "Subject: Something I wanted to check in about",
        "body": (
            "Hey [Name],\n\n"
            "I wanted to check in with you directly. You have seemed a bit off lately -- not yourself in meetings, less engaged than usual, or maybe just more tired than usual. I am not saying anything is wrong, but I noticed and I care.\n\n"
            "I came across something last week that might speak to what you are going through: The Clearing (clearing-ai.com). It is a free resource for engineers dealing with AI fatigue -- the sense that everything is moving too fast, that you cannot keep up, that you are falling behind no matter how hard you try.\n\n"
            "I found it useful. Thought you might too. No pressure to look at it -- just wanted you to know you are not alone if that is where you are right now.\n\n"
            "Let me know if you want to talk about it -- or anything else.\n\n"
            "[Your name]"
        )
    },
    "B": {
        "label": "Template B -- Someone You Manage",
        "subject": "Subject: How are you doing, really?",
        "body": (
            "Hi [Name],\n\n"
            "I want to check in with you about something that is not in any performance review: how you are actually doing with the pace of things right now.\n\n"
            "No agenda here. I just know that a lot of engineers are dealing with something the industry is calling AI fatigue -- the feeling that you are always behind, always catching up, always learning new tools without feeling like you are getting better at the things that matter.\n\n"
            "If that resonates, The Clearing (clearing-ai.com) has some useful framing and a short quiz that might help you name what you are feeling.\n\n"
            "If not, no worries at all. Just wanted you to know the door is open if you want to talk.\n\n"
            "[Your name]"
        )
    },
    "C": {
        "label": "Template C -- Someone Who Mentioned AI Tools",
        "subject": "Subject: That thing you mentioned about AI tools",
        "body": (
            "Hey [Name],\n\n"
            "Remember when you mentioned [specific thing they said about AI tools / feeling behind / being tired of learning new things]? I thought about that.\n\n"
            "I found something that might help you name what you were describing: The Clearing has an AI Fatigue Quiz (clearing-ai.com/quiz.html) that you might find surprisingly accurate.\n\n"
            "It is free, takes 2 minutes, and the person who showed it to me said it helped them realize they were not just lazy or bad at their job -- they were experiencing something with a name and a path forward.\n\n"
            "Wanted to pass it along.\n\n"
            "[Your name]"
        )
    },
    "D": {
        "label": "Template D -- Public Share / Slack",
        "subject": "Subject: [Shareable text for public post]",
        "body": (
            "I have been reading real engineer stories about AI fatigue on The Clearing (clearing-ai.com) -- people describing something that is not burnout exactly, but feels like the ground moving under your feet.\n\n"
            "One quote that stuck with me: \"I could see it happening and I did not have the language for it.\"\n\n"
            "If you have been feeling the same way, you are not alone. The site has a free 5-question quiz that helps you name what you are experiencing and points toward what actually helps.\n\n"
            "Worth 2 minutes if any of this lands: clearing-ai.com"
        )
    },
}

def email_template(key):
    t = templates[key]
    body_escaped = t["body"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        '<div class="email-template">\n'
        '<span class="template-label">' + t["label"] + '</span>\n'
        '<span class="template-subject">' + t["subject"] + '</span>\n'
        '<span class="template-body">' + body_escaped + '</span>\n'
        '<button class="copy-btn" onclick="copyTemplate(this,\'' + key + '\')">Copy</button>\n'
        '</div>\n'
    )

templates_html = '\n'.join(email_template(k) for k in sorted(templates.keys()))

page = (
    '<!DOCTYPE html>\n'
    '<html lang="en" data-theme="dark" style="contain-intrinsic-size:auto,auto;content-visibility:auto;">\n'
    '<head>\n'
    '<meta charset="UTF-8"/>\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n'
    '<title>Engineer Testimonials Campaign - Real Stories, Real Recovery | The Clearing</title>\n'
    '<meta name="description" content="10 engineers shared their AI fatigue recovery stories. Submit yours or nominate a colleague. Real stories from the frontlines of AI fatigue."/>\n'
    '<meta name="robots" content="index,follow"/>\n'
    '<link rel="canonical" href="https://clearing-ai.com/testimonials-campaign.html"/>\n'
    '<meta property="og:type" content="website"/>\n'
    '<meta property="og:url" content="https://clearing-ai.com/testimonials-campaign.html"/>\n'
    '<meta property="og:title" content="Engineer Testimonials Campaign - Real Stories, Real Recovery"/>\n'
    '<meta property="og:description" content="10 engineers shared their AI fatigue recovery stories. Your story could help someone else feel less alone."/>\n'
    '<meta property="og:image" content="https://clearing-ai.com/og-image.png"/>\n'
    '<meta name="twitter:card" content="summary_large_image"/>\n'
    '<script type="application/ld+json">\n'
    '{"@context":"https://schema.org","@type":"WebPage","name":"Engineer Testimonials Campaign","description":"The Clearing testimonials campaign hub.","url":"https://clearing-ai.com/testimonials-campaign.html","isPartOf":{"@type":"WebSite","name":"The Clearing","url":"https://clearing-ai.com"},"breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://clearing-ai.com"},{"@type":"ListItem","position":2,"name":"Community","item":"https://clearing-ai.com/community.html"},{"@type":"ListItem","position":3,"name":"Testimonials Campaign","item":"https://clearing-ai.com/testimonials-campaign.html"}]}}\n'
    '</script>\n'
    '<style>\n' + styles + '\n'
    '</style>\n'
    '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'><text y=\'26\' font-size=\'28\'>🌿</text></svg>"/>\n'
    '</head>\n'
    '<body>\n'
    '<a href="#main" class="skip-link">Skip to main content</a>\n'
    '<div class="reading-progress" id="progress" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>\n'
    '<header>\n'
    '<nav class="nav" aria-label="Main navigation">\n'
    '<a href="/" class="nav-logo" aria-label="The Clearing home">🌿 The Clearing</a>\n'
    '<div class="nav-links">\n'
    '<a href="/">Home</a><a href="/quiz.html">Take the Quiz</a><a href="/recovery.html">Recovery</a><a href="/community.html">Community</a><a href="/newsletter.html">Newsletter</a><a href="/testimonials.html">Testimonials</a><a href="/testimonials-campaign.html" aria-current="page">Campaign</a>\n'
    '</div>\n'
    '<button class="theme-toggle" aria-label="Toggle color theme">🌙</button>\n'
    '</nav>\n'
    '</header>\n'
    '<main id="main">\n'
    '<section class="page-hero" aria-labelledby="hero-title">\n'
    '<p class="hero-eyebrow">Engineer Testimonials Campaign</p>\n'
    '<h1 id="hero-title">Your Story Is Someone Else\'s Proof They\'re Not Alone</h1>\n'
    '<p class="hero-sub">10 engineers have shared their AI fatigue recovery stories. Every story shared helps someone else realize they\'re not lazy, not broken -- they\'re experiencing something real with a name and a way out.</p>\n'
    '<div class="hero-cta-row">\n'
    '<a href="#submit" class="btn btn-primary">Share Your Story</a>\n'
    '<a href="#outreach" class="btn btn-secondary">Use Outreach Templates</a>\n'
    '<a href="#stories" class="btn btn-secondary">Read the Stories</a>\n'
    '</div>\n'
    '<div class="hero-stats">\n'
    '<div class="hero-stat"><strong>10</strong><span>Stories shared</span></div>\n'
    '<div class="hero-stat"><strong>6+</strong><span>Roles represented</span></div>\n'
    '<div class="hero-stat"><strong>3,000+</strong><span>Quiz takers</span></div>\n'
    '</div>\n'
    '</section>\n'
    '<div class="content-wrap">\n'
    '\n'
    '<section class="section" id="share" aria-labelledby="share-title">\n'
    '<h2 id="share-title">Spread the Word</h2>\n'
    '<p class="section-intro">If you know an engineer struggling with AI fatigue, share this campaign. One message can start a conversation that changes someone\'s week.</p>\n'
    '<div class="share-row">\n'
    '<a href="https://twitter.com/intent/tweet?text=I%20just%20read%2010%20real%20engineers%27%20AI%20fatigue%20recovery%20stories.%20If%20you%27ve%20felt%20the%20same%2C%20you%27re%20not%20alone.%20https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html" class="share-link share-twitter" target="_blank" rel="noopener">X Share on Twitter</a>\n'
    '<a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html" class="share-link share-linkedin" target="_blank" rel="noopener">Share on LinkedIn</a>\n'
    '<a href="https://news.ycombinator.com/submit" class="share-link share-hn" target="_blank" rel="noopener">Submit to Hacker News</a>\n'
    '<button class="share-link share-copy-btn" id="copy-link-btn" onclick="copyLink()">Copy Link</button>\n'
    '</div>\n'
    '<div class="share-text-row">\n'
    '<p style="font-size:.78rem;color:rgba(232,228,220,.38);margin:0;width:100%">Pre-written share text:</p>\n'
    '<button class="share-btn-sm" onclick="copyShareText(\'twitter\')">Copy Twitter text</button>\n'
    '<button class="share-btn-sm" onclick="copyShareText(\'linkedin\')">Copy LinkedIn text</button>\n'
    '<button class="share-btn-sm" onclick="copyShareText(\'hn\')">Copy HN text</button>\n'
    '</div>\n'
    '</section>\n'
    '\n'
    '<hr class="divider"/>\n'
    '\n'
    '<section class="section" id="