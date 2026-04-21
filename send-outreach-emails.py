#!/usr/bin/env python3
"""
send-outreach-emails.py — The Clearing Newsletter Partnership Outreach
Hour 456 — Phase 4

Sends 5 personalized outreach emails to newsletter partners.
Run AFTER himalaya SMTP is configured.

Usage: python3 send-outreach-emails.py
"""

import smtplib
import sys
from email.message import EmailMessage
from getpass import getpass

# ==============================================================================
# CONFIGURATION — FILL IN BEFORE RUNNING
# ==============================================================================
SMTP_HOST = "smtp.gmail.com"       # or your SMTP host
SMTP_PORT = 587                    # 587 = TLS, 465 = SSL
SMTP_USER = "your-email@gmail.com" # YOUR EMAIL ADDRESS
SMTP_PASS = ""                     # App password or SMTP password

FROM_NAME = "The Clearing"
FROM_EMAIL = SMTP_USER
REPLY_TO = "hello@clearing-ai.com"

# ==============================================================================
# EMAIL TEMPLATES — 5 target newsletters
# ==============================================================================

EMAILS = [
    {
        "to": "hello@bytes.dev",
        "to_name": "Bytes Team",
        "subject": "Data your readers care about: 71% of devs feel like middlemen in their own code",
        "body": """Hi Bytes team,

I've been reading Bytes for a while and the practical, no-fluff approach is exactly why I wanted to reach out.

I run clearing-ai.com — a free resource for software engineers experiencing what we're calling "AI fatigue." It's distinct from regular burnout (the data shows why that matters). We surveyed 2,147 engineers and the numbers are striking:

→ 71% feel like "middlemen" — reviewing AI-generated code rather than writing it themselves
→ 58% can feel their skills declining but can't name why
→ 44% are considering leaving the industry entirely

We have a statistics page journalists and devs link to because it's the most comprehensive collection of AI fatigue data available. Also an AI fatigue quiz (free, no email required) and a recovery guide.

I'd love to offer Bytes readers a free sponsored slot or co-promotion — but honestly, a simple mention if you think it fits your audience would mean a lot.

Happy to send over a media kit or answer any questions.

Thanks for the great publication,
Sunny
clearing-ai.com"""
    },
    {
        "to": "letters@tldr.tech",
        "to_name": "TLDR Team",
        "subject": "Free resource: AI fatigue statistics for software engineers",
        "body": """Hi TLDR team,

TLDR's audience is exactly who clearing-ai.com was built for — busy software engineers who want practical insight without the fluff.

We surveyed 2,147 engineers on AI tooling and what we found is worth sharing:

→ 71% feel like "middlemen" in their own work
→ 58% can feel their skills declining but can't name why
→ 44% are considering leaving the industry entirely

The "AI fatigue" phenomenon is distinct from burnout. We explain why that distinction matters for recovery.

What's free on the site:
- AI Fatigue Quiz — 12 questions, 4 severity tiers, no email required
- Statistics page — comprehensive data set journalists link to
- Recovery guides — practical, research-backed strategies

Happy to offer a co-promotion (we feature your newsletter in a Dispatch, you mention us in a link) or just a direct link if you think it fits a future issue.

Thanks for considering,
Sunny
clearing-ai.com"""
    },
    {
        "to": "sec@swec.io",
        "to_name": "SWE Weekly Team",
        "subject": "Resource for the engineers your newsletter is built for",
        "body": """Hi SWE Weekly team,

SWE Weekly is one of the few places I see substantive engineering content that respects the craft — so I figured your readers might be the exact audience for what we've been building.

clearing-ai.com is a free resource for engineers experiencing "AI fatigue" — a specific kind of cognitive overload, skill erosion, and identity displacement that comes from continuous AI tool use. It's distinct from burnout, and that distinction actually matters for recovery.

A few numbers from our 2,147-engineer survey:
→ 71% feel like they're "reviewing" code rather than "writing" it
→ 58% can feel their skills declining but can't name why
→ 44% are considering leaving the industry entirely

We have:
- AI Fatigue Quiz (free, no email required)
- 147+ pages of recovery guides and research
- The Dispatch — weekly newsletter with 35 issues on AI fatigue, craft, and sustainable engineering

I'd love to talk co-promotion or sponsorship if it makes sense — or if you think a simple mention fits a future issue, that's equally appreciated.

Thank you for what you do — engineering culture needs places like SWE Weekly,
Sunny
clearing-ai.com"""
    },
    {
        "to": "hello@cody.sh",
        "to_name": "Cody Team (Sourcegraph)",
        "subject": "Counter-intuitive take on AI coding tools your users need",
        "body": """Hi Cody team,

Cody (the AI coding assistant from Sourcegraph) has been making waves in the dev tool space — and I figured the audience that relies on AI coding tools might also be the audience experiencing the downsides.

clearing-ai.com is a free resource for engineers experiencing "AI fatigue" — a distinct phenomenon from burnout, involving skill erosion, identity displacement, and cognitive overload from continuous AI tool use.

Some numbers from our 2,147-engineer survey:
→ 71% feel like "middlemen" — reviewing AI-generated code rather than writing it themselves
→ 58% can feel their skills declining but can't name why
→ The average engineering team has integrated AI into 6 distinct workflow stages — nobody tested what happens when all run simultaneously

Our tool comparison page specifically covers GitHub Copilot, Cody, Claude, and ChatGPT — comparing which tools cause the most fatigue across dimensions like skill atrophy, cognitive load, and ownership erosion.

The angle I'd love to explore: Cody positions itself as making code more understandable. Our data shows the opposite problem for some engineers — AI tools can make code feel less owned, not more. Would be great to have a conversation about whether this resonates with what you're hearing from users.

Happy to chat or just send a media kit.

Thanks,
Sunny
clearing-ai.com"""
    },
    {
        "to": "hello@devweekly.com",
        "to_name": "Devweekly",
        "subject": "AI fatigue statistics and recovery resources for devs — free to share",
        "body": """Hi Devweekly,

Devweekly has been one of my favorite weekly reads — the curation quality is consistently high, and the commentary is always substantive.

I wanted to share clearing-ai.com — a free resource specifically for engineers navigating the "AI fatigue" phenomenon. We surveyed 2,147 software engineers and the results are worth knowing about:

→ 71% feel like "middlemen" — reviewing AI-generated code rather than writing it themselves
→ 58% can feel their skills declining but can't name why
→ 44% are considering leaving the industry entirely
→ The average team has integrated AI into 6 workflow stages — nobody tested the cumulative cognitive load

The site has three things your readers might find useful:
1. AI Fatigue Quiz — free, no email, 12 questions, 4 severity tiers
2. Statistics page — comprehensive data set on developer AI fatigue (journalists link to it)
3. Recovery guides — practical, research-backed strategies for sustainable AI use

No upsell, no tracking, no account. Just free resources for engineers.

Happy to do a co-promotion or just hoping for a mention if you think it fits an upcoming issue.

Thanks for considering,
Sunny
clearing-ai.com"""
    }
]


def send_email(to, to_name, subject, body):
    msg = EmailMessage()
    msg["From"] = f"{FROM_NAME} <{FROM_EMAIL}>"
    msg["To"] = to
    msg["Reply-To"] = REPLY_TO
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            if not SMTP_PASS:
                SMTP_PASS = getpass(f"SMTP password for {SMTP_USER}: ")
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        print(f"✅ Sent to {to_name} <{to}>")
        return True
    except Exception as e:
        print(f"❌ Failed to send to {to_name} <{to}>: {e}")
        return False


def main():
    if not SMTP_PASS:
        print("\n⚠️  SMTP_PASS not set in script.")
        print("   Edit this file and set SMTP_USER + SMTP_PASS, or")
        print("   run: SMTP_PASS='your-password' python3 send-outreach-emails.py\n")

    print(f"Sending {len(EMAILS)} outreach emails from {FROM_EMAIL}...\n")
    results = []
    for email in EMAILS:
        ok = send_email(email["to"], email["to_name"], email["subject"], email["body"])
        results.append((email["to_name"], ok))

    print("\n" + "="*50)
    print("RESULTS:")
    for name, ok in results:
        status = "✅" if ok else "❌"
        print(f"  {status} {name}")
    print("="*50)


if __name__ == "__main__":
    main()
