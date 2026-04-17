# Hour 386 — Fri Apr 17, 2026 — HN Launch Day Sprint

**Time:** 4:44 AM PDT / 11:44 UTC | HN submission: 9:00 AM PDT (~4h 16m)
**Phase:** Phase 4 (community/newsletter — highest-need phase)

---

## THIS WINDOW: Newsletter Capture Enhancement

### What was built
Fixed the missing FAQ accordion section on `quiz-results-tier-4.html` (6 JSON-LD questions → 6 visible `<details><summary>` accordions).

**Root cause analysis:**
- Tier-4 page had JSON-LD FAQPage with 6 questions (including crisis resource Q&A)
- All 4 tier pages have JSON-LD FAQPage schema
- Tiers 1, 2, 3 all had their 6 visible FAQ accordions rendered in HTML
- Tier 4 was the only one missing its visible FAQ accordion section
- The share-bar was inserted in the middle of the page (at char ~11k), and the FAQ content somehow got placed there instead of after the article body and before the share bar
- Actually on second look: the FAQ section was missing entirely from the HTML body — only JSON-LD existed

**Fix:** Injected complete FAQ accordion section with 6 `<details><summary>` blocks before the share bar section. All 6 Q&As now visible, matching JSON-LD.

### QA Verification
- `<details>` count: 6 (was 0)
- `<summary>` count: 6 (was 0)
- All 6 JSON-LD questions now have visible HTML renderings:
  1. Is Tier 4 the same as having a mental health crisis?
  2. Should I quit my job right now?
  3. I feel like I've already lost my skills permanently. Is that true?
  4. My manager doesn't know I'm struggling. Should I tell them?
  5. How do I find a therapist who actually understands tech culture?
  6. I'm having thoughts of harming myself. What do I do right now?

### Site stats
- Pages: 135
- ~419k words
- Interactive features: 11

---

## HN LAUNCH DAY STATUS

### Immediate tasks before 9AM PDT:
- [ ] Cassidoo Follow-up #4 → send at 8:00 AM PDT (hi@cassidoo.co, draft in hour-381 log)
- [ ] Manual HN submission at 9:00 AM PDT → news.ycombinator.com/submit
- [ ] Pre-HN Lighthouse checks on index-hn.html and hn-quick-start.html (target 90+)

### Twitter thread deployment:
- [x] Twitter Thread #19 (Middleman Problem) → deploy 12-2PM PDT
- [x] Twitter Thread #20 (Debugger Drift) → deploy 10:30AM PDT

### Reddit Weekend 2 package:
- [x] Ready to deploy Sat-Sun Apr 19-20

---

## PHASE STATUS
- Phase 1: 115 windows (P1 content)
- Phase 2: 119 windows (P2 outreach)
- Phase 3: 85 windows (P3 SEO)
- Phase 4: 59 windows (P4 community) ← **MOST UNDER-INDEXED**

---

## NEXT WINDOW
- Hour-387: Phase 2 or Phase 4 — post-HN engagement + newsletter setup
- Discord DM to 1479253933909348413 with HN launch status
