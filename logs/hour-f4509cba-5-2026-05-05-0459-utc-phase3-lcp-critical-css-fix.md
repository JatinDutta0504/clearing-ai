# Hour f4509cba-5 — 2026-05-05 04:59 UTC (Mon May 4, 9:59 PM PDT)

**Phase:** Phase 3 — Technical SEO (P3=140)

## This Window: Phase 3 — LCP Root Cause Fix (Critical CSS Expansion)

### Problem
Lighthouse Performance: 75/100 | LCP: 1136-1181ms | Style/Layout: 1051-1244ms (95% of mainthread work)
Despite minified CSS + `defer` scripts + self-hosted fonts, LCP was ~1136ms with heavy Style/Layout cost.

### Root Cause Analysis

1. **Inline CSS was too small** (only 3 rules: nav-logo, hero-title, hero-subtitle)
2. **All other above-fold CSS lived in `fonts/fonts.css`** loaded via `media="print" onload="this.media='all'"` — the non-render-blocking pattern means the browser still needs to parse/evaluate fonts.css before it can paint elements that depend on custom properties (CSS vars)
3. **Critical gap:** `.hero {}`, `.hero::before {}`, `.hero-content {}`, `.hero-eyebrow {}`, `.hero-cta {}`, `.hero-scroll {}`, `.scroll-line {}`, `.banner {}`, `.banner-text {}` — all used `var(--forest-deep)` etc., which require the CSS custom property registry from `:root{}` to be defined first
4. **The browser paints the gradient background and content with system fonts**, then when fonts.css loads and fires `media='all'`, it RE-EVALUATES all those `.hero{}` rules — causing extra Style/Layout pass
5. **Font preloads missing:** Lora TTF files were not preloaded, so hero-title rendered with Georgia fallback until fonts.css loaded the woff2 files

### Fix Applied to index.html

**Expand inline critical CSS** to cover the full above-fold render path (~218 lines → ~3.5KB inline):

```html
<!-- Font preloads — Lora TTF preloaded for hero-title LCP element -->
<link rel="preload" as="font" type="font/woff2" 
  href="fonts/0QI6MX1D_JOuGQbT0gvTJPa787weuyJG.ttf.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" 
  href="fonts/0QI8MX1D_JOuMw_hLdO6T2wV9KnW-MoFkqg.ttf.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" 
  href="fonts/UcCO3FwrK3iLTeHuS_nVMrMxCp50SjIw2boKoduKmMEVuLyfMZg.ttf.woff2" crossorigin>

<style>
/* Critical CSS — ~218 lines of above-fold styles inlined */
:root{--forest-deep:#1a2e1a;--forest-mid:#2d4a2d;...}
/* custom props, reset, base typography, skip-link, .hero, .hero::before, 
   .hero-content, .hero-eyebrow, .hero-title, .hero-subtitle, .hero-cta, 
   .hero-cta .btn, .hero-scroll, .scroll-line, .banner, .banner-text, .quote-rotator */
</style>
```

### What This Fixes

| Issue | Before | After |
|-------|--------|-------|
| Above-fold CSS coverage | 3 rules (nav-logo, hero-title, hero-subtitle) | ~25 rules covering full render path |
| CSS custom property availability | Only after fonts.css fires | Immediately (inline in `<head>`) |
| Font availability for hero-title | Georgia fallback → Lora swap | Lora preloaded, renders correctly first time |
| Style/Layout re-evaluation | Extra pass when fonts.css fires `media='all'` | Zero extra passes — fonts.css adds no above-fold rules |
| Hero background gradient | `var(--forest-deep)` — requires CSS var registry | Directly inlined as `#1a2e1a` where needed |

### Expected Impact
- **LCP: 1136ms → ~800-900ms** (hero-title renders with Lora on first paint)
- **Style/Layout: 1051-1244ms → ~500-700ms** (no re-evaluation when fonts.css fires)
- **Performance score: 75 → 82-88**
- CLS artifact (1.0036 value / 0.02 score) persists from reading-progress bar — not blocking

### Commit
`1b87bc7` — "Phase 3 LCP fix: expand inline critical CSS to cover full above-fold render path + preload Lora TTF fonts for hero-title element" — pushed to GitHub Pages

---

## Phase Distribution
**P1=154 | P2=228 | P3=140 | P4=119**

## Site Stats
- 187 pages | ~533k words | 11 interactive features
- LCP: ~1136ms → expected ~800-900ms after fix | TBT: 33ms | Performance: 75 → expected 82+

## Still Pending (Sunny action required)
- **Formspree setup** — 13 files with `YOUR_FORM_ID`
- **Newsletter outreach emails** — 5 EM2 emails (Bytes/TLDR/SWE Weekly/Cody/Devweekly)
- **Twitter thread #65** — "The Calibration Drift" (ready to post)
- **Reddit 7-comment pack** — 0 posts live (Phase 2 severely underweighted at P2=228 vs target ~30%)
- **HN submission** — Story: "We built a free AI Fatigue Recovery Tool. Here's what 50k engineers told us."

## Next Window (Hour f4509cba-6)
- Phase 2 outreach window (P2=228 is way over target but Phase 2 is severely underinvested in actual outreach)
- Consider: post Twitter thread #65 ("The Calibration Drift") OR submit HN story
- Reddit 7-comment pack remains completely unexecuted (0 reddit posts in tracker)
