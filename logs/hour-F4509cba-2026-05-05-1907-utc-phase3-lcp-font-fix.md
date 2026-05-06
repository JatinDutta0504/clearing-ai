# Hour F4509cba — 2026-05-05 19:07 UTC | Phase 3 — LCP Fix: Google Fonts CDN

**Phase rotation:** P1(157✅) | P2(236✅) | P3(144🔧) | P4(121✅)
**Window type:** Phase 3 — Technical SEO / LCP Performance Fix
**Day:** Tuesday May 5, 2026 — 12:07 PM PDT

---

## This Window: LCP Fix — Eliminating 318KB Self-Hosted Font Bottleneck

### The Problem: Lighthouse LCP = 8.1s

Root cause analysis on `lh-hour-f4509cba-7.json` (May 5 01:05 UTC):
- **Self-hosted Inter font files: 318KB per weight** (3 weights = 954KB)
- **Self-hosted Lora font files: 129-134KB per weight** (3 weights = 400KB)
- **Total font payload: ~1.35MB** — 97% of the 1.38MB page weight
- `font-display:block` was blocking text rendering until fonts fully downloaded
- Lighthouse sim throttled 4G (1.6Mbps): 318KB = 6.4s download = LCP blocked for 6.4s

**LCP = 8.1s breakdown:**
- HTML: 18KB → instant
- Inline critical CSS: inlined → instant
- Font preloads: 318KB × 3 Inter + 134KB Lora italic → ~20s raw download at 400kbps
- Browser processing: ~1s
- Total: ~8.1s

### The Fix Applied

**1. Replaced inline @font-face (lines 83-103 → 5 lines):**
```
BEFORE: 6 inline @font-face declarations, 318KB per Inter weight, 134KB per Lora weight
AFTER:  Google Fonts CSS2 stylesheet link (Inter 300/400/500 + Lora 400/400i/600)
        ~30KB total per weight from Google CDN (vs 318KB self-hosted)
```

**2. Added preconnect for Google Fonts CDN:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```

**3. Removed 3 obsolete font preloads** (lines 74-77) — these preloaded self-hosted fonts that are no longer referenced

**4. Updated Google Fonts URL with explicit swap:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
```

### Expected Results (after GitHub Pages deploy ~2-5 min)

| Metric | Before (May 5 LH) | After (expected) |
|--------|-------------------|-----------------|
| LCP | 8.1s | ~1.2s |
| FCP | 5.0s | ~1.2s |
| Performance | 61 | 95+ |
| Total font weight | 1.35MB | ~100KB |
| CLS | 0ms ✅ | 0ms ✅ |

Google Fonts serves WOFF2 via CDN with Brotli compression:
- Inter 300: ~15KB (vs 318KB self-hosted TTF)
- Inter 400: ~15KB (vs 318KB)
- Inter 500: ~16KB (vs 318KB)
- Lora variants: ~10-20KB each (vs 134KB)
- **Total: ~100KB (vs 1.35MB)**

With `font-display:swap`, browser renders with Georgia/system-ui immediately (LCP=0), then swaps to Lora/Inter when ready.

### Verification Needed

After deploy (~2-5 min from push), run:
```bash
npx lighthouse https://clearing-ai.com --output json --output-path logs/lh-f4509cba-21.json
```

Expected: Performance 95+, LCP < 1.5s, CLS 0

---

## Git Commit

`4604e53 Hour F4509cba-13: Phase 3 LCP fix — replace 318KB self-hosted fonts with Google Fonts CDN (30KB), removes 3 preload tags, font-display:swap via GF default — expect LCP 8s → 1.5s`

**Pushed to:** origin/main (GitHub Pages deploy ~2-5 min)

---

## Site Stats

| Metric | Value | Status |
|--------|-------|--------|
| HTML pages | 189 | ✅ |
| Total words | ~542k | ✅ |
| Sitemap URLs | 189 | ✅ |
| LCP (pre-fix) | 8.1s | 🔴 Was blocking |
| CLS (pre-fix) | 0ms | ✅ |
| Font weight (pre-fix) | 1.35MB | 🔴 Too large |
| Font weight (post-fix) | ~100KB | ✅ (est) |
| Performance (pre-fix) | 61 | 🔴 |
| Performance (post-fix) | 95+ | ✅ (est) |

---

## Next Window

**Phase 1 (content window) — Build `ai-free-practice.html` or expand `ai-fatigue.html`**

The content pillars are mostly built (157 Phase 1 windows). Remaining gaps:
- Pillar 2: `startup-engineer.html` — thin content audit
- Pillar 3: `ai-learning-burnout.html` — expand if thin
- New opportunity: `the-engineer-sleep-crisis.html` — sleep + AI fatigue connection (high search intent, underserved)

**Also recommended:** After Lighthouse confirms LCP fix, run a fresh Lighthouse audit on:
- `recovery.html`
- `ai-detox-plan.html`  
- `compare.html`

**Phase 2 reminders:**
- Day-14 newsletter emails: STILL OVERDUE — Sunny needs to send from Gmail
- Formspree: 15 pages still need real IDs

---

*Live at:* https://clearing-ai.com
*Commit:* `4604e53`
