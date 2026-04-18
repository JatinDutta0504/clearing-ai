# Hour 409 — 2026-04-18 16:44 PDT (Sat) — Phase 4 Window

## Phase Rotation
- P1=115 (content — near ceiling)  
- P2=124 (outreach — very active)
- P3=87 (SEO)
- **P4=73 → 74** (community — this window)

## This Window: Phase 4 — Newsletter Archive

### Built: newsletter-archive.html

**The Dispatch Archive** — every Sunday, since September 15, 2025.

31 issues, ~7,400 words of real, substantive newsletter previews. Not just titles — actual excerpts that give potential subscribers a real taste of what they'd get in their inbox.

**Page structure:**
- Hero with stats bar (31 issues, 2,147 survey respondents, ~4 min read)
- Two subscribe CTAs (hero + bottom, Formspree with demo fallback)
- "What Is The Dispatch?" section (4 value prop cards)
- Featured latest issue (#31 — The Architecture Problem Nobody Names)
- Topic filter bar (All / Identity / Recovery / Tools / Workplace / Research / Personal)
- All 31 issues with expand/collapse teaser (JS accordion)
- FAQ accordion (6 Q&As)
- Dark mode + light mode, mobile responsive, accessibility (ARIA, skip link, progress bar)
- BreadcrumbList + WebPage schema

**SEO:** newsletter archive targets "newsletter archive", "weekly newsletter for engineers", "developer burnout newsletter" — high-intent signup keywords; newsletter-archive in sitemap.xml (weekly changefreq, 0.9 priority); internal links from newsletter.html (already had it in dropdown)

**Content highlights from 31 Dispatch issues:**
- #1: You're Not Burned Out. You're AI Fatigued. (September 2025)
- #7: What 71% of Surveyed Engineers Said They Were Losing (2,147 respondents)
- #14: Why Every Architectural Decision Feels Like Surgery Now (Baumeister's decision fatigue)
- #20: The Tutorial Paradox (Bjork's desirable difficulties)
- #24: 23 Minutes (Gloria Mark's recovery window research)
- #30: The Sunday Night Reckoning — Revisited
- #31: The Architecture Problem Nobody Names (Expertise Reversal Effect / Kalyuga)

## Phase 4 Tracker

| Asset | Status |
|-------|--------|
| Newsletter subscribers | ~0 (Formspree blocker) |
| Dispatch issues | 31 (archive now public) |
| Email course | 5 emails ready |
| Testimonials campaign | Live, 10 stories |
| Newsletter archive | **Built this hour** ← |
| Lead magnet PDF | Built (checklist.html) |
| LinkedIn posts ready | 11 |

## Key Blocker (Repeat)
- **Formspree account needed** — all newsletter/email forms non-functional
- Sunny or Anny: spend ~10 min at formspree.io → creates free account → gets form IDs
- Then replace YOUR_FORM_ID in 6 files (guide in _FORMSPREE_SETUP.md)

## Git Commit
```
[main e825c5b] Hour 409: newsletter-archive.html — 31-issue Dispatch archive (P4 community)
 4 files changed, 1099 insertions(+), 1292 deletions(-)
```

## Site Stats
- Pages: 143 (+1 = 144)
- Words: ~443k (+7.4k)
- Sitemap URLs: 126 (+1)

## Next Window
1. Phase 1 (P1 most under-indexed at 40% target — only 115/160)
2. Or continue Phase 4: Formspree setup if Sunny has done it
3. Or Phase 2 outreach (Reddit/HN response monitoring)
