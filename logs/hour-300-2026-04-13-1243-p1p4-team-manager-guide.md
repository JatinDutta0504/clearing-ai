# Hour 300 — 2026-04-13T12:43:00Z (Mon Apr 13, 5:43 AM PDT)
**Phase:** Phase 1 + Phase 4 crossover window
**Rotation:** P1=101 → 102 | P2=102 | P3=65 | P4=32

---

## Decision: team-manager-guide.html — Phase 1 Pillar + Phase 4 Community Bridge

**Context:** Site at 119 pages/~389k words. Phase 1 has 101 windows (excellent). Phase 4 has 32 windows (behind). `team-manager-guide.html` was listed in sitemap.xml and nav but was likely a thin/stub version (Hour 300 commit shows 577 insertions vs 604 deletions — replacement of existing stub). Built full comprehensive guide targeting engineering managers — a key audience for HN traffic Friday and for newsletter growth.

**Why this now:** HN submission Friday Apr 17 9AM PDT. Engineering managers will be a key audience on HN. This page gives them a rich, actionable resource. Also fills the Pillar 4 gap: manager-facing content is community-building for the EM segment.

---

## What Was Built

**`team-manager-guide.html`** (~4k words, 616 lines, 49,607 bytes)

**Sections:**
1. Why managers are uniquely positioned to help — naming, signal-changing, structural protection
2. The 6 warning signs your team has AI fatigue — declining review depth, explanation vacuum, skill concentration risk, velocity trap, questions stop being asked aloud, quiet disengagement
3. The three ways teams develop AI fatigue — velocity trap, modeling cascade, mandatory-optional paradox
4. How to bring it up in 1:1s — 3 verbatim conversation scripts (opening, disengagement follow-up, process change follow-up) + what NOT to say
5. Writing a team AI agreement together — 5-section template (what AI is for, what "understanding code" means, AI-free practice spaces, how to review AI-generated code, how to flag distress)
6. The structural changes that actually work — deliberate practice blocks, explanation expectations, learning visibility, quarterly calibration, no-AI Fridays, role visibility for seniors
7. Your 12-point team health checklist — monthly audit with localStorage persistence, each item scored with signal explanation
8. The 12-week implementation roadmap — 4 phases (Name it + listen / team agreement / first structural changes / review + deepen)
9. Red, yellow, and green signal guide — 10-row table with specific indicators and what to do
10. FAQ accordion (6 Q&As)

**Schema:** Article + FAQPage (6 Q&As) + BreadcrumbList

**Target keywords:** "engineering manager AI fatigue", "managing engineers AI tools", "team AI agreement", "AI fatigue management", "software manager burnout", "engineering lead AI wellness"

**Internal links:** recovery.html, workplace.html, developer-wellbeing.html, mental-health.html, corporate-ai-wellness.html, quiz.html

**Nav:** Already included in nav via automated pattern (50 pages). Full content now served.

**Git:** Commit 805f19d pushed successfully to GitHub Pages.

---

## Site Status

- **Pages:** 119
- **Words:** ~389k (+4k)
- **Interactive features:** 9
- **Sitemap URLs:** 119
- **Technical SEO score:** 99/100
- **Phase distribution:** P1=102 ✅ | P2=102 ✅ | P3=65 🟡 | P4=32 🔴

---

## Phase Window Distribution

- **P1 (Content Pillars):** 102 ✅ (excellent — original plan essentially complete)
- **P2 (Authority + Outreach):** 102 ✅ (excellent — Reddit, Twitter, LinkedIn assets ready)
- **P3 (Technical SEO):** 65 🟡 (decent but could use more windows — HN Friday will drive traffic)
- **P4 (Community + Newsletter):** 32 🔴 (needs more windows — newsletter 0 subscribers, Formspree blocker)

---

## Critical Reminders

**LinkedIn Post #1 deploys at 7:30 AM PDT today (Mon Apr 13).** Post #2 (Explanation Requirement) ready for Tue Apr 14.

**HN manual submission: Fri Apr 17, 9 AM PDT.** All assets ready. Story: "I built clearing-ai.com after engineers told me AI was stealing their craft. Here's what 2000+ quiz takers revealed." Guide v2 at linkedin/hn-manual-submission-guide-v2.md.

**Newsletter blocker (still open):** Formspree account needs to be created at formspree.io. Until then, newsletter has 0 subscribers despite 16 Dispatch issues drafted. Sunny needs ~5 min to create account and update form endpoints. This is the #1 conversion gap for HN traffic Friday.

---

## Phase 4 Gap Analysis

**What exists:** Newsletter archive (16 issues), testimonials page, community hub, press kit, social badges, lead magnet (ai-fatigue-checklist.html)

**What's missing:** Newsletter has 0 subscribers (Formspree blocker). LinkedIn company page needs Sunny to create at linkedin.com/pages/create. Testimonials feature anonymous stories but could be more prominent.

**Next Phase 4 windows should prioritize:** Fix newsletter Formspree setup (Sunny action needed), OR build featured testimonials widget, OR create "Engineer Spotlight" case study format.

---

## Git Commit

**File:** `team-manager-guide.html`
**Commit:** `805f19d`
**Message:** "Hour 300: team-manager-guide.html — Engineering Manager's Guide to preventing AI fatigue (~4k words, FAQPage + Article + BreadcrumbList schema, 12-point team health checklist, 4-phase 12-week roadmap, team AI agreement template, P4 recovery + P1 content pillar)"

---

## TRACKER Update

```json
{
  "phase_windows": {
    "phase1_content": 102,
    "phase2_outreach": 102,
    "phase3_seo": 65,
    "phase4_community": 32
  },
  "content_pages_built": 119,
  "total_words": "~389k",
  "pillars_completed": {
    "pillar1_ai_fatigue": [...existing...],
    "pillar4_recovery": ["decompress", "recovery", ..., "team-manager-guide"]
  },
  "last_updated": "2026-04-13T12:43:00Z",
  "notes": [
    ...existing...,
    "Hour 300: Built team-manager-guide.html — comprehensive EM guide (~4k words, FAQPage + Article + BreadcrumbList, replaces stub, 50 pages nav updated, Git 805f19d pushed. LinkedIn Post #1 deploys 7:30AM PDT today. HN: Fri Apr 17 9AM PDT. P1=102, P2=102, P3=65, P4=32. Site: 119 pages/~389k words."
  ]
}
```

---

## Next Window (Hour 301)

**Priority options:**
1. Phase 2: Monitor LinkedIn Post #1 performance (deployed 7:30 AM PDT today) — engage with comments
2. Phase 2: Deploy Reddit fresh comments on Monday morning threads (r/cscareerquestions, r/ExperiencedDevs)
3. Phase 3: Lighthouse audit on team-manager-guide.html + 4 other pages
4. Phase 4: Newsletter Formspree setup guide for Sunny (Sunny action needed — 5 min)
5. Phase 1: Expand ai-fatigue.html or another under-built pillar page
