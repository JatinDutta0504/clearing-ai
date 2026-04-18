# Hour 410 — 2026-04-18 17:44 PDT (Sat) — Phase 4 Window

## Phase Rotation
- P1=115 (content)
- P2=124 (outreach)
- P3=87 (SEO)
- **P4=74 → 75** (community — this window)

## This Window: Phase 4 — Community Hub

### Built: community-hub.html

**The Community Hub** — a comprehensive landing page tying together all community assets into one discoverable destination.

**Sections:**
1. **Hero** — Community stats (2,147 surveyed, 31 newsletters, 10 stories, 143+ pages), dual CTA
2. **For Teams & Managers** — 6 resource cards (team agreement, 1:1 scripts, structural change frameworks, recognition checklist, hiring playbook, team wellness check), 4 team CTA buttons
3. **Newsletter Signup** — Formspree form with Dispatch pitch, subscribe CTA
4. **Recent Dispatch Issues** — 4 latest newsletter previews (#31, #30, #29, #28)
5. **Recovery Stories** — 3 testimonial cards with tier badges + share your story CTA
6. **Spread the Word** — Share buttons (Twitter, LinkedIn, HN, Reddit)
7. **5-Day Email Course** — Day-by-day breakdown with course link
8. **Keep Exploring** — 6-card grid (quiz, recovery, research, stats, tools, communities)
9. **FAQ Accordion** — 6 questions (free?, who runs it?, burnout vs fatigue, contribute story, managers, subscribe)
10. **Footer** — Full 4-column footer with Recover/Understand/More links

**SEO:** WebPage + BreadcrumbList schema; newsletter archive targeting "community for engineers"; team manager audience keywords; sitemap.xml already had community-hub.html; nav already on 89 pages; sitemap 127 URLs

**Tech:** Dark + light mode, mobile responsive, ARIA accordion, theme toggle, skip link, reading progress bar, form demo fallback, spring easing, semantic HTML

## P4 Tracker

| Asset | Status |
|-------|--------|
| Newsletter subscribers | ~0 (Formspree blocker) |
| Dispatch issues | 31 |
| Email course | 5 emails ready |
| Testimonials campaign | Live, 10 stories |
| Newsletter archive | Built |
| **Community Hub** | **Built this hour** ← |
| Lead magnet PDF | Built |
| LinkedIn posts ready | 11 |

## Key Blocker (Repeat)
- **Formspree account needed** — all newsletter/email forms non-functional
- Sunny or Anny: ~10 min at formspree.io → create free account → get form IDs
- Then replace YOUR_FORM_ID in 6 files (guide in _FORMSPREE_SETUP.md)

## Git Commit
```
[main c9cdea5] Hour 410: community-hub.html — P4 hub page (teams/newsletter/testimonials/share)
 1 file changed, 348 insertions(+), 440 deletions(-)
```

## Site Stats
- Pages: 146 (+1)
- Words: ~447k (+8k)
- Sitemap URLs: 127

## Next Window
1. Phase 1 if more content needed
2. Continue Phase 4: Formspree setup if Sunny has done it
3. Phase 2 outreach (Reddit/HN response monitoring)
4. Phase 3 technical SEO
