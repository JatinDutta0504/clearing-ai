#!/usr/bin/env python3
"""Generator for testimonials-campaign.html - Part 2 (append mode)"""

BASE = "/Users/nightcoder/Desktop/TheClearing/testimonials-campaign.html"

stories = [
    ["tier-3", "Tier 3 -- Real Fatigue", "Principal Engineer", "15 years exp", "I have fifteen years of experience. I have shipped compilers, distributed systems, a database that did not catch fire in production. Then, about eighteen months ago, I started noticing something: I could not debug things the way I used to."],
    ["tier-2", "Tier 2 -- Some Fatigue", "Mid-level Engineer", "4 years exp", "I feel guilty even writing this. The discourse around AI tools is so positive that saying anything less than 'this has been transformative' feels like admitting I am not trying hard enough."],
    ["tier-4", "Tier 4 -- Need a Real Break", "Engineering Manager", "Team of 8", "I could see it happening and I did not have the language for it. HR thought I was worried about nothing. The CEO pointed to the velocity numbers. I felt like I was watching my team slowly lose something and nobody else could see it."],
    ["tier-3", "Tier 3 -- Real Fatigue", "Backend Engineer", "7 years exp", "What I did not notice happening: I stopped talking to my teammates. Not because I did not like them. Because AI was a faster answer. And in a small overlap window, speed felt critical."],
    ["tier-3", "Tier 3 -- Real Fatigue", "Senior Engineer", "9 years exp", "About eighteen months into heavy AI tool use, I realized I could not sit with a problem anymore. I would literally reach for an AI tool before I had finished reading a bug report. Not because I was lazy. Because the discomfort of not knowing had become unbearable."],
    ["tier-3", "Tier 3 -- Real Fatigue", "SRE / On-call Engineer", "5 years exp", "My team adopted AI note-taking during incidents. It sounds minor. Here is what it did to us: during post-mortems, we read AI summaries of what happened instead of reconstructing it ourselves. Slowly, we stopped building the mental model of our own systems."],
    ["tier-3", "Tier 3 -- Real Fatigue", "Staff Engineer", "11 years exp", "I am the person who used to be the most skeptical on my team. I would argue against technology hype. Then AI coding tools got good and I rationalized my way in. Within a year, I was the person most dependent on them. Not because they were better -- because they were faster."],
    ["tier-2", "Tier 2 -- Some Fatigue", "Full-stack Engineer", "8 years exp", "I keep feeling like I am the only one who spends thirty minutes prompting, getting output that is not quite right, and then feeling vaguely dissatisfied. I have started wondering if I am just bad at using these tools -- but I have been building software for eight years."],
    ["tier-3", "Tier 3 -- Real Fatigue", "Frontend Engineer", "6 years exp", "The thing that scared me most: I stopped reading documentation. I would ask AI instead. Then I started forgetting things I used to know by heart -- not because I understood less, but because I had stopped putting things in memory. The quiz helped me name it."],
    ["tier-2", "Tier 2 -- Some Fatigue", "Junior Engineer", "2 years exp", "Everyone around me seemed to be using AI tools effortlessly. I felt slow for not adopting them faster. What I did not realize: I was not slow. I was learning the right way. And AI was quietly bypassing the struggle that actually builds expertise."],
]

templates = {
    "A": {
        "label": "Template A -- Colleague You Work With",
        "subject": "Subject: Something I wanted to check in about",
        "body": "Hey [Name],\n\nI wanted to check in with you directly. You have seemed a bit off lately -- not yourself in meetings, less engaged than usual, or maybe just more tired than usual. I am not saying anything is wrong, but I noticed and I care.\n\nI came across something last week that might speak to what you are going through: The Clearing (clearing-ai.com). It is a free resource for engineers dealing with AI fatigue -- the sense that everything is moving too fast, that you cannot keep up, that you are falling behind no matter how hard you try.\n\nI found it useful. Thought you might too. No pressure to look at it -- just wanted you to know you are not alone if that is where you are right now.\n\nLet me know if you want to talk about it -- or anything else.\n\n[Your name]",
    },
    "B": {
        "label": "Template B -- Someone You Manage",
        "subject": "Subject: How are you doing, really?",
        "body": "Hi [Name],\n\nI want to check in with you about something that is not in any performance review: how you are actually doing with the pace of things right now.\n\nNo agenda here. I just know that a lot of engineers are dealing with something the industry is calling AI fatigue -- the feeling that you are always behind, always catching up, always learning new tools without feeling like you are getting better at the things that matter.\n\nIf that resonates, The Clearing (clearing-ai.com) has some useful framing and a short quiz that might help you name what you are feeling.\n\nIf not, no worries at all. Just wanted you to know the door is open if you want to talk.\n\n[Your name]",
    },
    "C": {
        "label": "Template C -- Someone Who Mentioned AI Tools",
        "subject": "Subject: That thing you mentioned about AI tools",
        "body": "Hey [Name],\n\nRemember when you mentioned [specific thing they said about AI tools / feeling behind / being tired of learning new things]? I thought about that.\n\nI found something that might help you name what you were describing: The Clearing has an AI Fatigue Quiz (clearing-ai.com/quiz.html) that you might find surprisingly accurate.\n\nIt is free, takes 2 minutes, and the person who showed it to me said it helped them realize they were not just lazy or bad at their job -- they were experiencing something with a name and a path forward.\n\nWanted to pass it along.\n\n[Your name]",
    },
    "D": {
        "label": "Template D -- Public Share / Slack",
        "subject": "Subject: [Shareable text for public post]",
        "body": "I have been reading real engineer stories about AI fatigue on The Clearing (clearing-ai.com) -- people describing something that is not burnout exactly, but feels like the ground moving under your feet.\n\nOne quote that stuck with me: 'I could see it happening and I did not have the language for it.'\n\nIf you have been feeling the same way, you are not alone. The site has a free 5-question quiz that helps you name what you are experiencing and points toward what actually helps.\n\nWorth 2 minutes if any of this lands: clearing-ai.com",
    },
}

with open(BASE, "a", encoding="utf-8") as f:
    # Share section
    f.write('<section class="section" id="share" aria-labelledby="share-title">\n')
    f.write('<h2 id="share-title">Spread the Word</h2>\n')
    f.write('<p class="section-intro">If you know an engineer struggling with AI fatigue, share this campaign. One message can start a conversation that changes someone\'s week.</p>\n')
    f.write('<div class="share-row">\n')
    f.write('<a href="https://twitter.com/intent/tweet?text=I%20just%20read%2010%20real%20engineers%27%20AI%20fatigue%20recovery%20stories.%20If%20you%27ve%20felt%20the%20same%2C%20you%27re%20not%20alone.%20https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html" class="share-link share-twitter" target="_blank" rel="noopener">X Share on Twitter</a>\n')
    f.write('<a href="https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fclearing-ai.com%2Ftestimonials-campaign.html" class="share-link share-linkedin" target="_blank" rel="noopener">Share on LinkedIn</a>\n')
    f.write('<a href="https://news.ycombinator.com/submit" class="share-link share-hn" target="_blank" rel="noopener">Submit to Hacker News</a>\n')
    f.write('<button class="share-link share-copy-btn" id="copy-link-btn" onclick="copyLink()">Copy Link</button>\n')
    f.write("</div>\n")
    f.write('<div class="share-text-row">\n')
    f.write('<p style="font-size:.78rem;color:rgba(232,228,220,.38);margin:0;width:100%">Pre-written share text:</p>\n')
    f.write('<button class="share-btn-sm" onclick="copyShareText(\'twitter\')">Copy Twitter text</button>\n')
    f.write('<button class="share-btn-sm" onclick="copyShareText(\'linkedin\')">Copy LinkedIn text</button>\n')
    f.write('<button class="share-btn-sm" onclick="copyShareText(\'hn\')">Copy HN text</button>\n')
    f.write("</div>\n")
    f.write("</section>\n")
    f.write('<hr class="divider"/>\n')

    # How section
    f.write('<section class="section" id="how" aria-labelledby="how-title">\n')
    f.write('<h2 id="how-title">How This Campaign Works</h2>\n')
    f.write('<p class="section-intro">Real stories from real engineers are the most powerful thing this community has. Here\'s how you can help collect and amplify them.</p>\n')
    f.write('<div class="steps-grid">\n')
    f.write('<div class="step-card"><span class="step-num">1</span><h3>Read the Stories</h3><p>10 engineers shared what AI fatigue felt like, what helped them recover, and what they wish they knew sooner.</p></div>\n')
    f.write('<div class="step-card"><span class="step-num">2</span><h3>Share Your Own</h3><p>Your recovery story is someone else\'s proof they\'re not broken. Takes 5 minutes to write.</p></div>\n')
    f.write('<div class="step-card"><span class="step-num">3</span><h3>Nominate a Colleague</h3><p>Know someone struggling quietly? Use the outreach templates below to send a thoughtful note.</p></div>\n')
    f.write('<div class="step-card"><span class="step-num">4</span><h3>Spread the Word</h3><p>Share the campaign on Twitter, LinkedIn, Slack, or HN. Every share reaches engineers who need this.</p></div>\n')
    f.write("</div>\n")
    f.write("</section>\n")
    f.write('<hr class="divider"/>\n')

    # Stories section
    f.write('<section class="section" id="stories" aria-labelledby="stories-title">\n')
    f.write('<h2 id="stories-title">Real Stories, Real Engineers</h2>\n')
    f.write('<p class="section-intro">Every story here is from an engineer who took the AI Fatigue Quiz or read our resources. Names and identifying details are removed. The feelings are real.</p>\n')
    f.write('<div class="stories-grid">\n')

    for idx, (tier_cls, tier_label, role, exp, quote) in enumerate(stories, 1):
        q_short = quote[:55] + "..."
        # Escape quotes for JS onclick attributes
        role_esc = role.replace("'", "\\'")
        q_esc = q_short.replace("'", "\\'")
        tier_short = tier_label[:4]
        f.write('<div class="story-card">\n')
        f.write('<span class="quote-mark" aria-hidden="true">"</span>\n')
        f.write(f'<span class="tier-badge {tier_cls}">{tier_label}</span>\n')
        f.write(f'<p class="story-quote">"{quote}."</p>\n')
        f.write(f'<div class="story-meta"><span>{role}</span><span> - </span><span>{exp}</span><span> - </span><span>{tier_short}</span></div>\n')
        f.write('<div class="story-share">\n')
        f.write(f"<button class=\"share-btn-sm\" onclick=\"shareStory('twitter','{role_esc}','{q_esc}')\">X Tweet</button>\n")
        f.write(f"<button class=\"share-btn-sm\" onclick=\"shareStory('linkedin','{role_esc}','{q_esc}')\">LinkedIn</button>\n")
        f.write("</div>\n")
        f.write("</div>\n")

    f.write("</div>\n")
    f.write("</section>\n")
    f.write('<hr class="divider"/>\n')

    # Outreach section
    f.write('<section class="section" id="outreach" aria-labelledby="outreach-title">\n')
    f.write('<h2 id="outreach-title">Reach Out to Someone Who Might Need This</h2>\n')
    f.write('<p class="section-intro">Sometimes the most caring thing you can do is send a thoughtful message to a colleague who seems off. Here are four templates for different relationships.</p>\n')
    f.write('<div class="guide-card"><h3>Before Using These Templates</h3>\n')
    f.write("<ul>\n")
    f.write("<li>Customize [Name] and any specific observations</li>\n")
    f.write("<li>Only use for people you have an existing relationship with</li>\n")
    f.write("<li>If they do not respond, give them space</li>\n")
    f.write("<li>Lead with care, not advice</li>\n")
    f.write("<li>Share the quiz link, not a diagnosis</li>\n")
    f.write("</ul>\n")
    f.write("</div>\n")

    for key in ["A", "B", "C", "D"]:
        t = templates[key]
        body_escaped = t["body"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        f.write("<div class=\"email-template\">\n")
        f.write(f'<span class="template-label">{t["label"]}</span>\n')
        f.write(f'<span class="template-subject">{t["subject"]}</span>\n')
        f.write(f'<span class="template-body">{body_escaped}</span>\n')
        f.write(f"<button class=\"copy-btn\" onclick=\"copyTemplate(this,'{key}')\">Copy</button>\n")
        f.write("</div>\n")

    f.write("</section>\n")

print("Part 2 written OK")
