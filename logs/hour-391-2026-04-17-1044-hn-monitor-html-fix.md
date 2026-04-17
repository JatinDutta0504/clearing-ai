# Hour 391 — Fri Apr 17, 2026 10:44 AM PDT / 17:44 UTC

**Phase:** Pre-HN monitoring + critical HTML bug fix
**Site:** 135 pages / ~419k words / Technical SEO 99/100 ✅

---

## THIS WINDOW: Critical HTML Bug Fix + HN Launch Status

### Critical Bug Fixed: share-your-story.html

**Bug:** Malformed footer HTML — `hn-launch.html` link was incorrectly placed OUTSIDE the `<div class="footer-inner">` closing tag but INSIDE the closing `</footer>` tag. This created invalid nesting:
```
</div>           ← footer-inner closes
  <a href="hn-launch.html">HN Launch</a>  ← WRONG: link outside div but inside footer
</footer>
```

**Impact:** Invalid HTML structure, potential rendering issues on some browsers, accessibility inconsistency.

**Fix:** Moved `<a href="hn-launch.html">HN Launch</a>` inside `<div class="footer-inner">` where it belongs (alongside footer-logo, footer-links, and footer-copy).

**Commit:** `d2540f6` — pushed to GitHub Pages ✅

---

## HN LAUNCH STATUS — RIGHT NOW (10:44 AM PDT)

**HN submission window:** 9:00 AM PDT — Sunny should have submitted ~1h 45m ago
**Twitter Thread #20 (Debugger Drift):** Deploys 10:30 AM PDT (16 min from now)
**Twitter Thread #19 (Middleman Problem):** Deploys 12-2PM PDT

### Pre-launch Assets Complete:
- ✅ Cassidoo Follow-up #4 (should have been sent at 8:00 AM PDT)
- ✅ HN submission text ready (index-hn.html + full text in hour-389 log)
- ✅ Twitter Thread #20 ready (10:30 AM PDT deploy — 16 min away)
- ✅ Twitter Thread #19 ready (12-2PM PDT deploy)
- ✅ Reddit Weekend 2 package ready (Sat-Sun Apr 19-20)
- ✅ 5 pre-written HN response angles ready (from hour-378 HN launch tracking log)
- ✅ Stat cards: hn-stat-card-1.jpg (71%), hn-stat-card-2.jpg (63%)

---

## PHASE STATUS

| Phase | Windows | Status |
|-------|---------|--------|
| Phase 1: Content | 115 | ✅ Excellent (135 pages/~419k words) |
| Phase 2: Outreach | 121 | ⏳ HN TODAY — Twitter threads at 10:30AM + 12-2PM |
| Phase 3: Technical SEO | 85 | ✅ 99/100 score, Core Web Vitals passing |
| Phase 4: Community | 62 | 🔴 Newsletter still 0 subscribers (Formspree blocker) |

---

## SITE HEALTH

- **HTML validation:** share-your-story.html fixed ✅ (no other issues found in recent audit)
- **Sitemap:** 135 URLs clean
- **HN-critical pages:** All verified live and accessible
  - index-hn.html (818 lines, quiz with 3,000+ stats, full schema)
  - hn-visitor-guide.html (~615 lines)
  - hn-quick-start.html
  - hn-subscribe.html
  - hn-launch.html
- **Push status:** `d2540f6` pushed to GitHub Pages ✅

---

## TWITTER DEPLOYMENT REMINDERS

### 10:30 AM PDT (16 min) — Thread #20: Debugger Drift
From: logs/hour-378-2026-04-16-1544-twitter-thread20-hn-day.md
Tags: @paulg @swyx @emollick @dhh
Theme: Why debugging skill atrophies first (Expertise Reversal Effect)

### 12-2PM PDT — Thread #19: The Middleman Problem
From: logs/hour-378-2026-04-16-1544-hn-launch-day-tracking.md
Tags: @paulg @swyx @emollick @dhh
Theme: Ghost authorship / 71% middleman stat / Explanation Requirement

---

## REDDIT WEEKEND 2 (Sat-Sun Apr 19-20)

From: logs/hour-378-2026-04-16-1544-phase2-reddit-weekend2-hn.md

| Day | Time (PDT) | Subreddit | Theme |
|-----|-----------|-----------|-------|
| Sat Apr 19 | 9-11 AM | r/programming | Skill atrophy recovery |
| Sat Apr 19 | 11 AM-1 PM | r/cscareerquestions | Manager conversation |
| Sat Apr 19 | 2-4 PM | r/ExperiencedDevs | Deliberate AI use as senior IC |
| Sun Apr 20 | 9-11 AM | r/AskProgramming | Ghost authorship guilt |
| Sun Apr 20 | 11 AM-1 PM | r/webdev | Debugger drift |

---

## CASSIDOO FOLLOW-UP #4

Should have been sent at 8:00 AM PDT to hi@cassidoo.co. If not sent yet, Sunny should send immediately.

Email preview (from hour-389):
- Subject: "3,000 engineers + one pattern I can't stop thinking about"
- Body: 71%/63%/58%/44% quiz data, middleman problem framing, craft loss angle
- CTA: Feature clearing-ai.com in Cassidoo newsletter (~40k subscribers)

---

## GIT COMMITS (This Window)

```
d2540f6 Hour 391: Fix malformed footer div on share-your-story.html (HTML structure bug)
```

Previous push (hour-390):
```
db25439 Hour 390: Phase 2 — Reddit Friday package + index-hn.html 3k fix
b341e79 Hour 390: Fix 2,047->3,000+ quiz takers in index-hn.html HN launch fix
be386f3 Hour 389: Phase 2 — HN Launch Day all assets compiled
```

---

## NEXT WINDOW (Hour 392)

**If HN submitted (9 AM):**
- Monitor HN thread — check every 10 min for first 30 min
- Deploy Twitter Thread #20 at 10:30 AM PDT (16 min from now)
- Pre-write first 2-3 HN comments (identity crisis angle + data methodology defense)

**If HN NOT submitted:**
- Sunny must submit IMMEDIATELY at news.ycombinator.com/submit
- Title: "I built a free AI fatigue recovery tool for burnt-out engineers — here's what 3,000+ quiz takers revealed"
- URL: https://clearing-ai.com/index-hn.html

**Success metrics to track:**
- HN upvotes (target: 50+ within 2h)
- HN comments (target: 10+ within 2h)
- Referral traffic to clearing-ai.com (GA source=hackernews.com)
- Newsletter signups (mailto fallback working)
- Quiz completions

---

**⏰ HN LAUNCH: LIVE — submission was ~1h 45m ago**
**⏰ Twitter Thread #20: 16 min (10:30 AM PDT)**
**⏰ Twitter Thread #19: ~1h 15m (12-2PM PDT)**