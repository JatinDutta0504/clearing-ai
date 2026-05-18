# Hour f4509cba-4263-477c-9d5b-26a1cf314919 — 2026-05-17 19:46 PDT (Phase 4 Window: Social Share Badges Hub)

**Phase:** Phase 4 (Community & Retention)
**Window type:** Content + Community asset

---

## This Window: Social Share Badges Hub

### What Was Built

**`social-share-badges.html`** — Standalone badge hub for the viral quiz-to-PNG loop (641 lines)

**Features:**
- **3 theme options:** Forest (🌲 green), Slate (🌑 blue), Dawn (🌅 purple) — visual variety for LinkedIn/Twitter diversity
- **4 tier buttons:** 🌿 Tier 1 (Holding Up), 🌤 Tier 2 (Some Fatigue), 🌧 Tier 3 (Real Fatigue), 🌑 Tier 4 (Need a Break)
- **Canvas PNG generator:** 600×314px badges with tier-specific gradients, score ring arc, emoji, tagline, "The Clearing" brand
- **URL param support:** `?tier=2&theme=slate` — enables direct linking from quiz results
- **Download PNG:** One-click save to device
- **Copy link:** Clipboard copy of shareable URL
- **Share copy textarea:** Tier-specific Twitter copy pre-written (4 variants)
- **Name input field:** Optional personal identifier on badge

**Canvas design:**
- Top accent bar (theme color)
- Left tier column (emoji + color tint)
- Main body: quiz result tier label + tagline
- Divider + name/default domain
- Score ring (right side, arc fills based on tier 1-4)
- Bottom bar: "🌿 The Clearing" + "clearing-ai.com"

**Pre-written share copy per tier:**
- Tier 1: "🌿 Holding Up" — encourages normalization
- Tier 2: "🌤 Some Fatigue" — acknowledges toll without drama
- Tier 3: "🌧 Real Fatigue" — drives sympathy + clicks
- Tier 4: "🌑 Need a Break" — adds crisis resource nudge

**Viral loop:**
1. Engineer takes quiz → gets tier 2
2. Shares badge on LinkedIn → drives click-through to clearing-ai.com
3. LinkedIn impressions from badge → 100s of engineer views → newsletter signups
4. Each badge has unique tier + name → authenticity signal

---

## Site Updates

- **`sitemap.xml`:** Added social-share-badges.html (priority 0.8)
- **`index.html`:** Feature card updated to point to social-share-badges.html (replaces social-badges.html link)
- **`quiz-badge.html`:** Links updated to social-share-badges.html
- **`badge.html`:** Links updated to social-share-badges.html

---

## Phase Distribution

- Phase 1: 201 ✅
- Phase 2: 267 ✅
- Phase 3: 172 ✅
- Phase 4: 145 🟡 (this window = +1)

---

## Site Status

| Metric | Value |
|--------|-------|
| Pages | 209+ HTML files |
| Words | ~974k |
| Lighthouse | 94-97 |
| Technical SEO | 99/100 |
| Sitemap URLs | 210 |
| Days since launch | 13 |

---

## Manual Actions Still Pending

```
ALWAYS PENDING (need human action or credentials):
1. Formspree activation — RUN: python _activate-formspree.py
2. Twitter Thread #53 — POST from twitter-threads/POST-THIS-thread-53-stack-overflow-problem.md
3. Twitter Thread #54 — POST from twitter-threads/POST-THIS-thread-54-junior-engineer-problem.md
4. LinkedIn Post 2 (The Explanation Requirement) — POST from linkedin/POST-THIS-linkedin-post-2-monday.md
5. Reddit Comments batch — reddit-deployment-may-19-25.md (schedule Mon-Tue)
```

---

**Commit:** `1e43e9d`
**Next:** Phase 1 content (next unbuilt pillar) or Phase 4 newsletter dispatch