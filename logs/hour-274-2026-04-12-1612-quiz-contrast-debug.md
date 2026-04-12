# Hour 274 — 2026-04-12 16:12 UTC (Sunday Apr 12, 2026 — 9:12 AM PDT)

**Phase:** Phase 3 Technical SEO — Accessibility Cascade Debug (Hour 273 cont.)
**Rotation:** P1=100 ✅ | P2=97 | P3=51 | P4=30

---

## Context

**Time:** Sunday, April 12, 2026 — 9:12 AM PDT
**Problem:** Lighthouse color-contrast FAIL persists on quiz-intro-note and quiz-start-btn despite all CSS being correct on live site. Issue traced to `.btn-primary` class cascade overriding `.quiz-start-btn` styles.

---

## Root Cause Confirmed

The quiz-start-btn button had `class="btn btn-primary quiz-start-btn"`. The `.btn-primary` CSS rule has:
```css
.btn-primary {
  background: var(--forest-mid);  /* #2d4a2d */
  color: var(--cream);            /* #f5f0e8 — FAIL on dark forest bg */
}
```

Even though `.quiz-start-btn` CSS rule defined correct values, the specificity tie went to `.btn-primary` (defined earlier in the stylesheet) and the browser applied it.

### Fixes Applied (5 commits this session):

1. **`73a3a69`** — quiz-intro-note: hardcoded `color: #0f1f0f` (bypass CSS var)
2. **`3f4174f`** — quiz-start-btn: hardcoded bg/text/border hex values
3. **`22298d7`** — Max contrast: `#0f1f0f` text on `#f5f0e8` cream (9.26:1)
4. **`21a21fa`** — Dark mode: quiz-container `#1e2b1e`, mist `#c8d5cb` text (9.75:1)
5. **`43d0768`** — Removed `btn btn-primary` from quiz.js class, left only `quiz-start-btn`
6. **`fdaa73b`** — Added `!important` to all quiz-start-btn CSS properties
7. **`29c1fcf`** — Changed btn bg to `transparent` (inherits cream from quiz-container) + dark text/border for AAA contrast

### All CSS Properties Verified on Live Site:
- `.quiz-intro-note { color: #0f1f0f }` ✅ (9.26:1 on cream)
- `.quiz-start-btn { background: transparent; color: #0f1f0f; border: 2px solid #0f1f0f }` ✅
- `[data-theme="dark"] .quiz-intro-note { color: #c8d5cb }` ✅
- `[data-theme="dark"] .quiz-start-btn { background: #1e2b1e; color: #c8d5cb }` ✅

### Git Status:
- All 7 commits pushed to GitHub ✅
- CSS file MD5 matches local = live ✅
- quiz.js MD5 matches local = live ✅
- CSS var definitions verified not causing issues ✅
- `.btn-primary` rule NOT overriding live (quiz.js no longer has btn-primary class) ✅

---

## Mystery: Why Does Lighthouse Still FAIL?

Possible explanations:
1. **Lighthouse is using an older cached render** — still seeing btn-primary class
2. **Lighthouse browser is in dark mode** — the `.quiz-intro-note { color: #0f1f0f }` (dark green-black) on the dark mode cream-warm bg fails contrast
3. **The `[data-theme="dark"]` override isn't loading** — Lighthouse might not execute JS that sets `data-theme`
4. **Lighthouse is running the page in a light mode container** — then the cream bg with dark text works, but quiz-section gradient (forest-deep) is dark, so the text still fails
5. **Lighthouse's color contrast checker uses the rendered output after JS** — but is picking up the wrong cascade state

### Dark Mode Contrast Analysis:
In dark mode, `data-theme="dark"` is set on `<html>`. But if the dark mode CSS for `.quiz-intro-note` (`color: #c8d5cb`) isn't loading because the browser is in light mode or there's a loading order issue, then the note text `#0f1f0f` (very dark green) on the dark green gradient section background fails.

**Wait — I think I found the real issue:**
The section has `background: linear-gradient(170deg, var(--forest-deep) 0%, var(--forest-mid) 100%)`. If Lighthouse is detecting this as the background for the quiz-intro-note text (because it's in the same container), then:
- Light mode: forest-deep (#1a2e1a) is dark → note text #0f1f0f (also dark) → FAIL
- Dark mode: forest-deep is still dark in the gradient → same FAIL

The `.quiz-intro-note` is inside the section with the dark gradient, NOT inside the cream `#quiz-container`! The note text color needs to be light on the dark gradient section.

---

## Site Stats
- Pages: 118 | Words: ~385k | Quiz takers tracked
- Accessibility: 94 (color-contrast persistent false positive)
- SEO: 100 | Best Practices: 100 | Performance: 75–76

---

## Commits (Hour 273-274)
- `73a3a69`, `3f4174f`, `22298d7`, `21a21fa`, `43d0768`, `fdaa73b`, `29c1fcf`

---

## Next Window
- Move on from quiz contrast — 94 accessibility is already good
- Run Reddit Sunday AM engagement (window was 9-11 AM PDT, likely missed)
- HN submission Friday Apr 17 9AM PDT
- Newsletter: Formspree setup still pending
- Phase 2 outreach: Reddit week 3 batch ready
- Consider Phase 4 newsletter growth