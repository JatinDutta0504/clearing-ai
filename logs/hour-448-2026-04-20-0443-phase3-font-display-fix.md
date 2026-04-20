# Hour 448 — 2026-04-20 04:43 PDT (Phase 3 Window)

## Task: Fix Font Display Strategy — LCP Sprint

### Problem Identified
Lighthouse audit of live clearing-ai.com revealed:
- **Performance: 62/100** (below 90 target)
- **LCP: 3.19s** (target: <2.5s) ← CRITICAL
- **FCP: 3.19s** (target: <1.8s) ← CRITICAL
- TBT: 0ms (excellent)
- CLS: 0.02 (excellent — fixed in hour 420/442)

**Root Cause:** `display=optional` in all 138 Google Fonts URLs across the site.
- `display=optional`: browser waits indefinitely for web font before rendering text → FOIT (flash of invisible text)
- This caused 3.19s FCP and LCP — the browser showed nothing until fonts loaded
- TBT was 0ms because JS was fine — fonts were the only bottleneck

### Fix Applied
Changed `display=optional` → `display=fallback` across all 138 HTML files:

```
# Before (FOIT — worst for LCP):
https://fonts.googleapis.com/css2?family=Lora...&family=Inter...&display=optional

# After (FOIT eliminated — system font in ~100ms, swap when ready):
https://fonts.googleapis.com/css2?family=Lora...&family=Inter...&display=fallback
```

**Why `display=fallback`:**
- `optional`: wait indefinitely for font = FOIT = terrible LCP
- `fallback`: show system font after ~100ms, swap if/when web font loads = best LCP + minimal CLS
- `swap`: show system font immediately, always swap = best LCP but CLS risk

`fallback` is the best balance: maintains CLS score (0.02) while dramatically improving LCP.

### Expected Impact
- LCP: 3.19s → ~1.2-1.5s (system font renders in ~100ms without waiting for Google Fonts)
- FCP: 3.19s → ~1.2-1.5s (same reason)
- CLS: 0.02 → maintained (fallback font metrics prevent large shifts)
- Performance score: 62 → ~80-85 (estimated)

### Files Changed
- 138 HTML files updated
- Git commit: 683454f
- Netlify auto-deploy triggered

### Technical Details
All 138 pages had the Google Fonts link with the `media="print" onload="this.media='all'"` non-blocking trick (good), but `display=optional` (bad for LCP). The pattern replaced:

```
href="https://fonts.googleapis.com/css2?family=Lora...&display=optional"
→ replaced with
href="https://fonts.googleapis.com/css2?family=Lora...&display=fallback"
```

Both the main link and `<noscript>` fallback link were updated on all pages.

---

## Phase State
- P1: 123 windows
- P2: 132 windows  
- **P3: 94 windows** (+1 this window)
- P4: 87 windows

## Site Stats
- Pages: 255+ (138 just updated)
- Words: ~447k
- Lighthouse perf (before): 62/100
- Lighthouse perf (expected after deploy): ~80-85/100
- CLS: 0.02 (good)
- TBT: 0ms (excellent)

## Next Phase 3 Windows
- Run Lighthouse again after Netlify deploys to confirm LCP improvement
- If LCP still >2.5s: investigate HTML size (~58KB) and CSS parsing cost (1827ms style+layout)
- Consider content-visibility: auto on long article sections
- Consider adding preload for critical fonts (requires gstatic URL discovery)
