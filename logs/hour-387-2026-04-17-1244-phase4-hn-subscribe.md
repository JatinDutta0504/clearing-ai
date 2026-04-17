# Hour 387 — Fri Apr 17, 2026 — Phase 4: HN Newsletter Capture

**Time:** 5:44 AM PDT / 12:44 UTC | HN submission: 9:00 AM PDT (~3h 16m)
**Phase:** Phase 4 (community — most under-indexed at 60 windows)
**Site:** 135 pages / ~419k words

---

## THIS WINDOW: hn-subscribe.html — HN Newsletter Capture Page

### What was built
`hn-subscribe.html` — a standalone newsletter subscribe page purpose-built for HN traffic arriving at 9 AM PDT.

**Page structure:**
- Hero: "One email. Every Sunday morning." (serif headline)
- Stats row: 3,000+ engineers surveyed | 71% middleman stat | 27 issues published
- 4-card promise grid: evidence-based / 5-minute read / zero tracking / real engineers
- Full sample Dispatch issue (Issue #24: The Middleman Problem) — shows real content
- Subscribe form with mailto fallback (Formspree unconfigured blocker)
- Success state after submit
- Share bar: Twitter / LinkedIn / Email
- Dark/light theme toggle

**Technical:**
- Fully responsive (mobile-first)
- Dark/light mode with localStorage persistence
- Reading progress bar
- Skip-to-content + ARIA labels
- No render-blocking resources
- Sitemap: hn-subscribe.html added (priority 0.9, weekly changefreq, 135 URLs)
- Linked from: index-hn.html footer, hn-quick-start.html footer, hn-visitor-guide.html footer

### Why this page was needed
The newsletter funnel was broken on HN launch day:
- Formspree not configured (Sunny blocker — 7 files need form ID)
- The Dispatch is the primary owned-audience channel for long-term growth
- HN wave could bring 300-800 visitors in 2 hours — this page captures them
- Without a dedicated subscribe page, HN visitors bounce without subscribing
- Mailto fallback: `mailto:hello@clearing-ai.com?subject=Subscribe to The Dispatch`
- Primary CTA: links to `https://clearing-ai.com/hn-subscribe.html` in HN submission

---

## HN LAUNCH DAY — COUNTDOWN STATUS

### Timing (current: 5:44 AM PDT):
| Task | Time | Status |
|------|------|--------|
| This window (Hour 387) | 5:44 AM PDT | ✅ Complete |
| Cassidoo Follow-up #4 | 8:00 AM PDT | 📋 Ready to send |
| **HN Submission** | **9:00 AM PDT** | **📋 Manual submit** |
| Twitter Thread #20 | 10:30 AM PDT | 📋 Ready to deploy |
| Twitter Thread #19 | 12-2PM PDT | 📋 Ready to deploy |
| Reddit Weekend 2 | Sat-Sun Apr 19-20 | 📋 Ready to deploy |

### HN Submission Checklist (for Sunny at 9 AM PDT):
- [ ] Go to https://news.ycombinator.com/submit
- [ ] Title: "I built clearing-ai.com for engineers who've lost their craft to AI tools"
- [ ] URL: https://clearing-ai.com/hn-quick-start.html (primary) or https://clearing-ai.com/ (homepage)
- [ ] Check thread for first 2 hours, reply to top comments
- [ ] Reference Thread #20 (Debugger Drift) at 10:30 AM as companion

### Cassidoo Follow-up #4 (send at 8 AM PDT):
- To: hi@cassidoo.co
- Subject: [Draft in logs/hour-369 or re-send previous follow-up]
- Data angle: 3k quiz takers, 71%/63%/58%/44% stats, craft loss framing
- Timing: 1 hour before HN — maximizes chance of her seeing it before the wave

### Twitter Threads Ready:
- Thread #19 "The Middleman Problem" — deploy 12-2PM PDT (direct HN companion)
- Thread #20 "The Debugger Who Forgot How to Debug" — deploy 10:30AM PDT (pre-HN)

---

## PHASE STATUS
| Phase | Windows | Target | Gap |
|-------|---------|--------|-----|
| Phase 1 Content | 115 | ~90 | +25 ✅ |
| Phase 2 Outreach | 119 | ~90 | +29 ✅ |
| Phase 3 SEO | 85 | ~90 | -5 🟡 |
| Phase 4 Community | **61** | ~90 | **-29 🔴** |

**Phase 4 is the critical bottleneck.** Every Phase 4 window should prioritize newsletter capture + community assets.

### Critical Blocker — Formspree Setup (Sunny action needed):
```bash
# 1. Go to https://formspree.io → Create free account
# 2. Create form "Newsletter Subscribers"
# 3. Replace YOUR_FORM_ID in these 7 files:
#    newsletter.html, newsletter-thank-you.html,
#    ai-fatigue-checklist.html, community-hub.html,
#    index-hn.html, testimonials.html, share-your-story.html
# 4. Run: python3 _setup-formspree.py
```
Until Formspree is configured, ALL newsletter signups use mailto fallback.
With HN traffic in ~3h, manual mailto is the only capture mechanism.

---

## WHAT THIS WINDOW ACHIEVED

**Immediate HN impact:**
- Every HN visitor can now land on hn-subscribe.html → subscribe without navigating the full site
- Sample Dispatch issue shows content quality before subscribing
- Mailto form works immediately (no Formspree required)
- Share buttons enable organic sharing from the page itself

**Long-term value:**
- Newsletter subscribers compound over time (every email = future repeat visitor)
- 3k quiz takers + 0 newsletter subscribers = massive leakage
- This page is a reusable asset for ALL future traffic (HN + Reddit + Twitter + press)

---

## NEXT WINDOW (Hour 388)
- Phase 4: Continue newsletter / community assets OR
- Phase 2: Post-HN engagement monitoring + Reddit weekend package
- Discord DM: Send HN launch countdown + this window's work

**hn-subscribe.html is live. Ready for the 9 AM PDT HN wave.**
