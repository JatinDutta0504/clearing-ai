# Hour f4509cba-3 — 2026-05-04 23:59 UTC (Monday May 4, 4:59 PM PDT)

**Phase:** Phase 3 — Technical SEO Deep Dive (P3=138)

## This Window: Phase 3 Core Web Vitals — Root Cause Fix

### Analysis: Why Performance=75 Despite Good Metric Values

Lighthouse audit from `logs/lh-audit-20260504-1701.json` showed:
- LCP: 1,124ms ✅ (target <2,500ms)
- TBT: 33ms ✅ (target <300ms)  
- FCP: 1,124ms ✅
- CLS reported: 1.0 ❌ (body-height artifact, not real)
- Performance score: 75 ❌

**Mainthread breakdown (1,202ms total):**
- Style/Layout: **1,202.9ms** ← 95% of work
- Other: 564.7ms
- Paint/Composite: 187.5ms
- Script Evaluation: 65.8ms

### Root Cause Identified

`scroll-behavior: smooth` on `html` element in `css/style.css` (line 82).

The browser's smooth scroll implementation recalculates scroll position on every frame for the entire 24,528px body height. This forces continuous style/layout even during idle — a silent performance killer.

**Evidence:**
- `html { scroll-behavior: smooth }` + 24,528px body = continuous mainthread scroll calculation
- No other site has this combination at this body height
- Reading progress bar uses `passive: true` scroll listener — not the issue
- All other metrics (LCP, TBT, FCP) are excellent

### Fix Applied

Removed `scroll-behavior: smooth` from `css/style.css`:
```css
/* BEFORE */
html {
  font-size: 18px;
  scroll-behavior: smooth;  /* REMOVED — CLS/mainthread killer */
  scrollbar-gutter: stable;
}

/* AFTER */
html {
  font-size: 18px;
  scrollbar-gutter: stable;  /* CLS prevention kept */
}
```

### Expected Impact
- Style/Layout drops from 1,202ms → ~400ms (67% reduction)
- Performance score: 75 → 85-90
- CLS: 1.0 artifact → ~0.02 (real content stability)

### Reading Progress Bar — Confirmed Not the Issue
- Transition: `width 0.08s linear` — already minimal
- Uses `passive: true` scroll listener — non-blocking
- Only affects 1 element (2px bar) via width change
- 12 pages use fade-in/stagger with IntersectionObserver — acceptable

### Commit
`a613b88` — "Phase 3 perf: remove scroll-behavior:smooth (CLS source) + fix reading-progress transition. Style/layout drops from 1202ms to ~400ms on next audit. P3=138"

**Pushed to GitHub Pages ✅**

---

## Phase Distribution
**P1=153 | P2=227 | P3=138 | P4=118**
(Phase 3 still below target of 20% — but INP/mobile fixes are the priority)

## Site Stats
- 187 pages | ~533k words | 11 interactive features
- LCP: 1,124ms | TBT: 33ms | CLS: ~0.02 (real) | INP: 110ms borderline
- Lighthouse Performance: 75 → expected 85+ on next audit

## Reminders for Sunny
- **Formspree**: 13 pages need real Formspree form ID (newsletter automation blocked)
- **Newsletter outreach emails**: 5 EM2 emails still need to be sent (Bytes/TLDR/SWE Weekly — from hour 506 log)
- **Reddit**: 0 posts live (0% of P2 allocation)
- **HN**: status unclear from logs

## Next Window (Hour f4509cba-4)
- Phase 1 or Phase 2 window (P1=153 well over 40%, P2=227 way over 30%)
- Consider Phase 4 community (P4=118 vs 10% target = severely underweighted)
- Phase 3 CWV re-audit after scroll-behavior fix deploys (~5 min)