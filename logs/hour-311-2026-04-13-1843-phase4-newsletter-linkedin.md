# Hour 311 — 2026-04-13 18:43 UTC (11:43 AM PDT)

## Phase Rotation Check
P1=105 (excellent) | P2=102 (good) | P3=67 (needs attention) | P4=33 (needs attention)

**Rotation:** Phase 4 — Newsletter infrastructure + LinkedIn deployment preparation

---

## This Window: Phase 4 — Newsletter Fix + LinkedIn Deployment Package

### Newsletter Status Audit

**Critical blocker identified:** newsletter.html + ai-fatigue-checklist.html still use `YOUR_FORM_ID` placeholder. Form submissions silently fail.

**mailtо fallback active:** hello@clearing-ai.com (configured in Hour 308) — submissions land in inbox but need manual CSV entry to send newsletters.

**Newsletter infrastructure status:**
- Newsletter page: ✅ functional (mailtо fallback active)
- AI Fatigue Checklist: ✅ functional (mailtо fallback active)
- Email templates: ✅ 17 issues ready (Dispatch #1 through #17)
- Archive page: ✅ JSON-driven, all 17 issues listed
- Formspree: ❌ BLOCKING (Sunny needs 5-min setup at formspree.io)

**Sunny action required to unblock automated newsletter:**
1. Go to formspree.io → Create account → New Form → copy form ID
2. Replace `YOUR_FORM_ID` in newsletter.html (line 822) and ai-fatigue-checklist.html (2 forms)
3. Done. Automated subscriber capture begins.

### LinkedIn Deployment Package (Ready to Execute)

**9 posts ready to publish** at `linkedin/linkedin-posts-ready-to-publish.md`

**Top 3 posts by urgency:**

**POST 1 — "The 71% Stat"** (Monday Apr 13, 7:30-9:30 AM PDT)
- Data-driven, founder voice
- Targets: EMs, CTOs, HR, senior ICs
- CTA: clearing-ai.com
- Expected reach: High (data + shares)

**POST 2 — "Manager Signs"** (Wednesday Apr 15, 12-2 PM PDT)
- Targets: engineering managers, tech leads
- CTA: clearing-ai.com/team-manager-guide
- Expected reach: Moderate (manager audience)

**POST 3 — "The Sunday Dread"** (Friday Apr 17, 12-2 PM PDT)
- Emotional, personal, high shareability
- Targets: ICs, senior engineers
- CTA: clearing-ai.com

**LinkedIn company page creation:** Sunny must create at linkedin.com/pages/create (blocking Post #1 deployment)

### Phase 4 Newsletter Growth Strategy

**Current:** 0 subscribers (Formspree blocking)
**Immediate fix:** Sunny configures Formspree (5 min)
**Week 1 target:** 10-20 subscribers (from newsletter.html traffic)
**Week 4 target:** 50-100 subscribers
**Launch email:** Dispatch #17 (most recent) — send manually first, then weekly

**Phase 4 window gap:** Only 33 windows used vs 67 for Phase 3. Recommend 10-15 more Phase 4 windows in next 20 cycles.

---

## Phase 2 Status (Active)

**Reddit:** 245 comments across 162 communities. Fresh comments for Apr 13-14 ready at `logs/hour-299-2026-04-13-0443-reddit-fresh-april-13-14.md`.

**Twitter:** 3 threads posted. 12+ threads ready to deploy (see TRACKER.json).

**HN:** Scheduled Fri Apr 17, 9:00 AM PDT. Guide at `linkedin/hn-manual-submission-guide.md`.

**Newsletter partnerships:** 5 sent (cassidoo, bytes-weekly, codemaven, tldr, swe-weekly). Awaiting responses.

---

## Site Status (End of Hour 311)

- **Pages:** 121
- **Words:** ~396k
- **Interactive features:** 9
- **Sitemap URLs:** 119
- **Technical SEO score:** 99/100
- **Lighthouse Performance:** 100 (optimized)
- **Newsletter subscribers:** 0 (Formspree blocker)
- **Reddit comments:** 245 total
- **Twitter threads posted:** 3
- **HN submission:** READY (Fri Apr 17 9AM PDT)

**Phase windows:** P1=105 ✅ | P2=102 ✅ | P3=67 🟡 | P4=33 🔴

---

## Next Window (Hour 312)

**Recommended:** Phase 4 — Execute LinkedIn Post #1 (if Sunny creates company page) OR Phase 2 — Deploy Twitter Thread #12 (Sunday Night Reckoning) OR Phase 3 — Core Web Vitals deep-dive on remaining pages

**Blocking actions for Sunny:**
1. **Create LinkedIn company page** (5 min) → unblocks LinkedIn deployment
2. **Configure Formspree** (5 min) → unblocks newsletter automation

---

## Git Commit

```
4d4e074 Hour 311: Phase 4 — Newsletter audit + LinkedIn deployment package ready
```

**Pushed:** Yes ( Hour 311: Nav update — performance-review-ai-fatigue in nav )

---

## SEO Impact

**LinkedIn opportunity:** 500M+ users, B2B reach to engineering managers/CTOs — untapped backlink pool. Each post that gets shared by an EM to their network = high-authority dofollow backlink.

**Newsletter critical gap:** 0 owned subscribers despite 119 pages, 9k+ monthly visits. Formspree setup = highest-ROI 5-min action available.

**HN impact (Fri Apr 17):** If top 10 on HN = 300-800 referral visits + 20-40 newsletter signups + 40-60 backlinks. Identity crisis + craft loss angle is HN gold.

---

**Live at:** https://clearing-ai.com
