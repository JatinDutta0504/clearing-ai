# Hour 273 — 2026-04-12 14:51 UTC (Sunday Apr 12, 2026 — 7:51 AM PDT)

**Phase:** Phase 3 Technical SEO — Quiz Accessibility Cascade Debug
**Rotation:** P1=100 ✅ | P2=97 | P3=49 | P4=30

---

## Context

**Time:** Sunday, April 12, 2026 — 7:51 AM PDT (early morning Sunday)
**Problem:** Lighthouse color-contrast FAIL persists on quiz-intro-note and quiz-start-btn despite CSS values being correct on live site.

---

## What Was Found & Fixed

### Root Cause: CSS Cascade Inheritance

The `.quiz-start-btn` button in `renderIntro()` had BOTH classes:
```html
<button class="btn btn-primary quiz-start-btn" id="quiz-start">
```

The `.btn-primary` class in the cascade had higher specificity than the class-only `.quiz-start-btn` rule:
```css
.btn-primary {           /* specific: class */
  background: var(--forest-mid);  /* #2d4a2d — WRONG for cream bg */
  color: var(--cream);            /* #f5f0e8 on dark bg — ~2.45:1 */
}
.quiz-start-btn {        /* specific: class + class */
  background: #f5f0e8;  /* correct cream */
  color: #0f1f0f;       /* correct dark text */
}
```

The `.btn-primary { background: var(--forest-mid) }` was overriding `.quiz-start-btn`'s background on the live site.

### Fix Applied

```javascript
// js/quiz.js — renderIntro()
<button class="quiz-start-btn" id="quiz-start">
```

Removed `btn btn-primary` — left only `quiz-start-btn`. The `.quiz-start-btn` CSS rule now applies correctly.

### CSS Changes (4 iterations, all committed)

1. `73a3a69` — quiz-intro-note: hardcoded #1a2e1a (was var(--forest-pale) on cream = FAIL)
2. `3f4174f` — quiz-start-btn: hardcoded #f5f0e8 bg, #1a2e1a text (bypass CSS var issues)
3. `22298d7` — Max contrast: darker text #0f1f0f on cream #f5f0e8 (9.26:1)
4. `21a21fa` — Dark mode: quiz-container #1e2b1e bg, mist #c8d5cb text (9.75:1)
5. `43d0768` — Remove btn-primary from quiz-start-btn class (cascade fix)

---

## Lighthouse Audit History (this session)

| Run | Commit | Quiz intro-note | Quiz start-btn | Score |
|-----|--------|-----------------|----------------|-------|
| Pre-fix | cb112e3 | FAIL 3.3:1 | FAIL 2.45:1 | 86 |
| Post CSS v1 | 73a3a69 | PASS 8.76:1 | FAIL 2.45:1 | 86 |
| Post CSS v2 | 22298d7 | PASS 9.26:1 | FAIL 2.45:1 | 86 |
| Post CSS v3 | 21a21fa | PASS 9.26:1 | FAIL 2.45:1 | 94 |
| Post cascade | 43d0768 | TBD | TBD | TBD |

Still testing: whether removing btn-primary fixes the remaining contrast issue.

---

## Site Stats
- Pages: 118 | Words: ~385k | Quiz takers tracked
- Accessibility: 86→94 (pending cascade fix verification)
- SEO: 100 | Best Practices: 100 | Performance: 76

---

## Commits (Hour 273)
- `73a3a69` — Use hardcoded hex for quiz-intro-note
- `3f4174f` — Use hardcoded hex for quiz-start-btn
- `22298d7` — Max contrast for quiz (#0f1f0f text)
- `21a21fa` — Fix quiz dark mode (dark green bg)
- `43d0768` — Remove btn-primary from quiz-start-btn

---

## Next Window
- Verify Lighthouse accessibility passes after cascade fix (43d0768)
- If passes: quiz contrast issue resolved
- Consider Phase 2 outreach execution (Reddit Sunday AM window was Apr 12 9-11 AM PDT — missed)
- HN submission: Fri Apr 17 9AM PDT
- Newsletter: Formspree still needs setup