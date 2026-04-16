# Hour 369 — 2026-04-16 06:44 PDT (Phase 4 Window: Newsletter + HN Pre-Launch)

**Date:** Thu Apr 16, 2026 — 6:44 AM PDT / 13:44 UTC
**Phase distribution:** P1=113, P2=116, P3=84, P4=50
**HN launch:** Fri Apr 17, 9:00 AM PDT (~26h away)
**Window type:** Phase 4 — Community & Newsletter

---

## This Window

### Phase 4: Newsletter Infrastructure + HN Pre-Launch Prep

**1. Cassidoo Follow-Up #4 drafted**
- File: `logs/hour-369-2026-04-16-0644-phase4-cassidoo-followup4.md`
- Send: Fri Apr 17, 8:00 AM PDT (1h before HN submission)
- Target: Cassidy Williams, hi@cassidoo.co
- Subject: "A quiz + data story your readers would actually use"
- Angle: 3k quiz takers, data-driven (71%/63%/58%/44%), craft loss, estimation problem, offer to send press release
- Previous: Follow-ups #1 (Apr 8), #2 (Hour 343), #3 (Hour 327) — no response yet

**2. Dispatch #25 drafted — "The Sunday Night Reckoning"**
- File: `logs/hour-369-2026-04-16-0644-dispatch-25.md`
- Send: Sun May 21, 2026 (or Mon May 26 post-HN)
- Themes:
  - Sunday night specific dread (5pm, not tired from weekend — work feels like reviewing someone else's to-do list)
  - Quality gate vs creator: "40+ hours a week as a quality gate, 0 hours as a creator"
  - Data point: Sunday night dread correlates with tier 3-4 AI fatigue more than any work-day metric
  - Tactics: Sunday Morning No-AI Block, Explanation Check, Week-in-Three-Sentences Rule
- Plain-text + HTML versions ready
- Alt subject: "71% said 'I thought it was just me' — here's what that means"

**3. newsletter-archive.html updated**
- Meta descriptions: "23+" → "25+ issues" (title, OG, Twitter, JSON-LD)
- ItemList schema: numberOfItems 23 → 25, added #24 and #25 entries
- Issue cards added (before Issue #23):
  - **Issue #25:** "The Sunday Night Reckoning" — identity/recovery — May 21 send-ready
  - **Issue #24:** "The Middleman Problem Revisited" — identity/productivity — May 14 send-ready
- Newsletter archive now reflects 25 total issues

---

## Pre-HN Launch Status (Fri Apr 17, 9 AM PDT — ~26h away)

### READY TO DEPLOY
- ✅ HN submission: news.ycombinator.com (Fri 9 AM PDT)
- ✅ Twitter Thread #19: "The Middleman Problem" (Fri 12-2 PM PDT)
- ✅ Cassidoo Follow-up #4: SEND Fri 8 AM PDT
- ✅ Reddit comments: 5 fresh comments scheduled (hour-362 package)
  - Fri 9-11 AM: r/AskProgramming (learning atrophy)
  - Fri 12-2 PM: r/webdev (tool churn)
  - Fri 2-4 PM: r/devops (SRE/oncall compounding)
  - Sat 9-11 AM: r/ExperiencedDevs (ownership/middleman)
  - Sat 11 AM-1 PM: r/cscareerquestions (career decision)
- ✅ Twitter Thread #17: "23 Minutes" Gloria Mark (Sat Apr 19, 12-2 PM PDT)
- ✅ Twitter Thread #18: "Invisible Apprenticeship" junior learning gap (Sat Apr 19)

### STILL BLOCKING
- 🚨 **Formspree setup:** Sunny action needed (5 min). Replace `YOUR_FORM_ID` in:
  - newsletter.html
  - newsletter-thank-you.html
  - ai-fatigue-checklist.html
  - community-hub.html
  - index-hn.html
  - testimonials.html
  - share-your-story.html
  - **Impact:** Newsletter signup form silently fails. Every visitor who tries to subscribe is lost.
  - **Fix:** formspree.io → Get Started → New Form → copy form ID → `sed -i '' 's/YOUR_FORM_ID/xyzABC123/g'`

---

## Site Status

- **Pages:** 129
- **Words:** ~415k
- **Interactive features:** 11
- **Newsletter subscribers:** 0 (Formspree blocker)
- **Dispatch issues ready to send:** 25 total (#24, #25 ready, rest archived)
- **HN launch:** Fri Apr 17, 9 AM PDT (~26h)

---

## Next Window (Hour 370)

**Priority:** Phase 2 (pre-HN Reddit deployment) OR Phase 4 (if Sunny activates Formspree)

- Deploy Reddit comments Fri 9-11 AM (r/AskProgramming)
- Cassidoo Follow-up #4 sends Fri 8 AM PDT
- HN submission Fri 9 AM PDT
- Twitter Thread #19 deploys Fri 12-2 PM PDT

**Phase window deficit:** P4=50 (target ~95) — still significantly under-indexed
