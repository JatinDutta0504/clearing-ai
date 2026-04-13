# Hour 293 — 2026-04-13T04:50:00Z (Sun Apr 12, 9:50 PM PDT) — Phase 4 Window

## Phase Rotation
Phase 1 (100✅) → Phase 2 (100✅) → Phase 3 (63✅) → Phase 4 (31→32🔴 undertarget)

**Context:** Sunday evening 9:50 PM PDT. Formspree still blocked (Sunny action needed). HN scheduled Fri Apr 17 9AM PDT. Newsletter archive gap identified: live archive only shows issues #1-7 but 16 issues exist. Built JSON-driven archive to fix this.

---

## Built This Window

### Phase 4: Newsletter Archive — JS-Driven Rebuild

**Problem:** The live `newsletter-archive.html` had issues #1-7 hardcoded in HTML. Actual content spans 16 issues (discovered from dispatch logs). Adding future issues required editing HTML.

**Solution:** JSON-driven archive + all 16 issues as structured JSON.

**File 1:** `newsletter-issues.json` (40KB, 16 issues)
- Issues #1-7: extracted from existing archive HTML
- Issues #8-16: from dispatch log files (hour-2026-04-06 through hour-292)
- Each issue: number, title, date, dateSort, readTime, author, status, subject, body
- Body content uses existing CSS classes: `.dispatch-body p/h3/strong/ul/ol/li/blockquote`, `.dispatch-stat-grid`, `.dispatch-cta`

**File 2:** `newsletter-archive.html` (32KB → JS-driven)
- Fetches `newsletter-issues.json` dynamically
- `renderIssues()`: maps JSON to expand/collapse cards (matching original UX)
- `expandAll()` / `collapseAll()` controls
- `updateCounts()`: updates hero + sub-bar issue count from JSON
- `updateSchema()`: dynamic ItemList schema (auto-updates as issues are added)
- `toggleDispatch()`: per-card expand/collapse with aria-expanded
- Keyboard accessible (Enter/Space on dispatch headers)
- All original visual styles preserved
- Schema: CollectionPage + dynamic ItemList with 16 items

**Key architectural improvement:** Adding future newsletter issues = append to JSON only. No HTML editing required.

---

## What's Still Blocked

1. **Formspree** — Sunny needs to run `_setup-formspree.py` or `_setup-formspree.sh` (5 min). Newsletter signup and send are both blocked.
2. **Newsletter send** — Cannot send without Formspree. Dispatch content is ready; infrastructure is the blocker.

---

## Git Commit
`919ceb8` — Newsletter archive now JS-driven with all 16 issues from JSON

---

## Site Stats
- Pages: 118 (unchanged)
- Words: ~385k (unchanged)
- Newsletter: 16 issues in JSON, archive JS-driven

## Next Window
- P4 next: newsletter signup infrastructure (Formspree setup) — blocked on Sunny
- HN: Fri Apr 17 9AM PDT
- P4 community building (LinkedIn, testimonials outreach)
