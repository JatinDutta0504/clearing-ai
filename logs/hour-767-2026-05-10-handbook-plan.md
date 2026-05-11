# AI Fatigue Engineer's Handbook — clearing-ai.com
**Version:** 1.0 | **Built:** Hour 767 (2026-05-10) | **Author:** The Clearing
**Purpose:** Definitive handbook / table of contents for the entire Clearing site

---

## DRAFT — AI FATIGUE ENGINEER'S HANDBOOK

### PAGE STRUCTURE

```html
<!-- Suggested structure for handbook.html -->
<title>The AI Fatigue Engineer's Handbook</title>
<meta name="description" content="The complete field guide for software engineers navigating AI tool fatigue. 192 pages of recovery guides, research, quizzes, and tools — organized for you.">
```

### SECTION OUTLINE

**1. Introduction (300w)**
- What this handbook is (and isn't)
- Who it's for
- How to use it
- The 5-minute reading plan vs the deep-dive path
- Why this exists (founding story — short version)

**2. Understanding AI Fatigue (2000w)**
- The 4-part AI fatigue framework (cognitive, identity, craft, physiological)
- AI fatigue vs burnout vs regular exhaustion — the quick test
- The compounding loop — why it gets worse before it gets better
- 10 signs you have AI fatigue (with self-check)
- Who gets it worst: archetypes by role, seniority, and work style
- The middleman problem — the core identity crisis explained
- Why traditional rest doesn't fix it

**3. The Science (1500w)**
- Cognitive load and working memory limits
- Attention residue — Gloria Mark's 23-minute finding
- Skill atrophy — the automation paradox
- Flow state disruption — why you can't get into the zone
- The Expertise Reversal Effect — why seniors feel it more
- Productivity theater — when busy looks like progress
- Decision fatigue and AI
- What the quiz data shows (2024-2026 surveys)

**4. The Recovery Toolkit (2000w)**
- The 5-Day Reset Protocol
- The Explanation Requirement (daily practice)
- No-AI blocks — how and why
- The 30-day recovery plan
- Daily boundaries checklist
- Manager conversations — how to talk about AI fatigue at work
- Team-level changes — how to shift culture
- Emergency kit — when you're in crisis mode

**5. Deep Dive Topics (1500w)**
- Junior engineers and AI dependency
- Senior engineers and identity crisis
- Remote work and async AI fatigue
- imposter syndrome vs AI fatigue
- Automation anxiety
- Tool overwhelm and how to choose
- The craft problem

**6. Resources & Tools (1000w)**
- The quiz (take it — 90 seconds)
- Daily check-in widget
- Decompress page — Pomodoro timer, breathing, thought dump
- Recovery tracker
- AI fatigue severity index
- The Dispatch newsletter
- Community — where to find engineers who get it
- Press kit — for journalists, researchers, partners

**7. For Managers & Leaders (1200w)**
- Recognizing AI fatigue in your team
- The manager's role in preventing team burnout
- How to run 1:1s around AI fatigue
- Team culture changes that matter
- Hiring and retaining engineers in the AI era
- When to escalate to HR or EAP

**8. Appendix (800w)**
- Full glossary of terms
- Research reading list
- Statistics and data sources
- Changelog — what's new on The Clearing
- About — who built this and why
- Contact / press inquiries

---

## INTERNAL LINKS (10+ strategic)

- Understanding → ai-fatigue.html, burnout-vs-fatigue.html, glossary.html
- Science → research.html, cognitive-load.html, skill-atrophy.html, attention-residue.html
- Recovery → recovery.html, ai-detox-plan.html, daily-practice.html, checkin.html
- Junior → junior-engineers.html | Senior → senior-identity.html | Remote → remote-work-ai-fatigue.html
- Tools → compare.html, ai-tool-overload.html, decompress.html
- Community → community.html, newsletter.html
- Manager → team-guide.html, workplace.html, hiring.html
- Appendix → about.html, press-kit.html, glossary.html

---

## SCHEMA TO ADD

```json
{
  "@context": "https://schema.org",
  "@type": "Book",
  "name": "The AI Fatigue Engineer's Handbook",
  "author": { "@type": "Organization", "name": "The Clearing" },
  "url": "https://clearing-ai.com/handbook.html",
  "about": {
    "@type": "Thing",
    "name": "AI Fatigue in Software Engineers",
    "description": "A comprehensive field guide for engineers experiencing fatigue from AI coding tools."
  },
  "hasPart": [
    { "@type": "WebPage", "name": "Understanding AI Fatigue", "url": "https://clearing-ai.com/ai-fatigue.html" },
    { "@type": "WebPage", "name": "The Science", "url": "https://clearing-ai.com/research.html" },
    { "@type": "WebPage", "name": "Recovery Toolkit", "url": "https://clearing-ai.com/recovery.html" },
    { "@type": "WebPage", "name": "The Quiz", "url": "https://clearing-ai.com/#quiz" }
  ]
}
```

Book schema = strong E-E-A-T signal for comprehensive authority content.
FAQPage schema for "How do I use this handbook?" / "What should I read first?"

---

## SUGGESTED PAGE TITLE (60 chars)

"The AI Fatigue Engineer's Handbook | The Clearing"

## SUGGESTED META DESCRIPTION (155 chars)

"192 pages for burnt-out engineers. Understand, recover, and build sustainable habits with AI tools. Start here."

---

## NAV PLACEMENT

- Add to: index (feature card), footer (all pages), nav (top-level or in Read dropdown)
- Feature card on index.html
- Link from about.html "what we built" section
- Link from newsletter.html "what you'll get" section

---

## CONTENT NOTES

- This page is THE hub — it should convert visitors into newsletter subscribers and deep readers
- Include a "Start Here" decision tree at the top (take quiz / just burned out / want science / manager)
- Every section should have 3+ internal links to related content
- Include a newsletter signup block mid-page ("Get The Dispatch — weekly field notes for AI-fatigued engineers")
- Mobile: Use a sticky sidebar TOC or collapsible accordion for navigation within the page
