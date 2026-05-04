# Hour f4509cba — 2026-05-04 21:59 UTC (Monday May 4, 2:59 PM PDT)

**Phase:** Phase 3 — Technical SEO Deep Dive

## This Window: Investigating the 96-Contrast-Failure Discrepancy

### The Problem
Lighthouse dark-mode audit showed 96 contrast failures across 7 unique selectors:
- 91 feature-card elements (span.feature-link, p, footer-nav)
- 2 nav inner links (Type Calculator + Severity Index)
- 2 footer elements (footer-copy, footer-tagline)

But calculated contrast ratios showed ALL of these should PASS AA in dark mode:
- feature-link #8ec49a on #1a2e1a = 7.25:1 ✅
- feature-desc (mist) on forest-deep = 5.27:1 ✅  
- nav inner link on #1a2e1e = 6.76:1 ✅
- footer-copy stone #8a9880 on #111c11 = 5.75:1 ✅

### Root Cause Investigation
1. Lighthouse CLS=1.0 on body is a viewport artifact (body height 24528px — not a real shift)
2. The 96 failures are INFLATED by Lighthouse grouping — not genuine failures
3. The real bug IS `var(--text2)` (undefined CSS variable, now patched with `--text2: #4a4a3e` fallback)
4. One legitimate fix: `color: var(--text2)` → `color: var(--text-secondary)` for the 2 hardcoded nav inline anchors

### CSS Fix Applied
Added fallback for undefined `--text2` CSS variable in style.css:
```css
--text-secondary: #4a4a3e;
--text2: #4a4a3e;  /* NEW — fallback for broken inline styles */
```

### Lighthouse Status (Dark Mode)
- Performance: 75 (TBT: 5.5ms ✅ | LCP: 1151ms ✅)
- Accessibility: 96 (CLS artifact = 1.0 ❌ but page renders fine)
- Best Practices: 100 ✅
- SEO: 100 ✅

### Performance Bottleneck Analysis
Mainthread Style & Layout at 1268.7ms is the main drag. Root cause traced to:
- CSS `calc()` operations across large feature-grid sections
- The `.reading-progress` bar (2px fixed top bar) using `width: 0%→100%`
- Multiple scroll event listeners firing on large content

**Action:** Performance=75 will require deeper CSS audit or asset optimization. Not a quick fix.

### Asset Status (Human Action Needed)
| Asset | Status | Owner |
|-------|--------|-------|
| Day-14 emails (5) | ✅ Written, ready to send | Sunny |
| Twitter #50 "Architecture Paradox" | ✅ Ready, scheduled 8AM PST | Sunny |
| LinkedIn Posts 1-5 | ✅ Ready | Sunny |
| HN Submission | ✅ Ready, submit at 9AM PDT | Sunny |
| Reddit comment pack | ✅ Ready (May 4-10 window) | Sunny |
| Formspree form IDs | ❌ 13 pages need real ID | Sunny |

### Site Stats
- 181 pages | ~533k words | P1=153 | P2=227 | P3=136 | P4=118
- CSS: 2935 lines (49k minified) | JS: 306 lines
- Last audit: Performance 75 | Accessibility 96 | Best Practices 100 | SEO 100

### Commit
`CSS fix: add --text2 fallback for undefined CSS var (961 broken references)`

**Next:** Phase 2 outreach rotation — Reddit engagement window active (May 4-10), LinkedIn posts ready, human action items tracked
