# Hour 405 — 2026-04-18 05:44 PDT (Sat) — Phase 4 Window

## This Window: Phase 4 — Newsletter Funnel Completion

### What Was Built

**1. Printable PDF Lead Magnet** (`ai-fatigue-recovery-checklist.html`)
- Print-optimized A4 page (~600px wide, @page CSS rules)
- 20 evidence-based practices across 4 sections:
  - Daily Boundaries (5 practices): 90-min blocks, batch AI, no-AI first 30min, etc.
  - Skill Preservation (5 practices): Explanation Requirement, no-AI debugging, etc.
  - Recovery & Attention (5 practices): 23-min transition ritual, sleep, movement
  - System & Sustainability (5 practices): Sunday recalibration, AI-free Fridays, quarterly audit
- 30-day tracker (4-week grid, print-ready)
- Weekly planner (no-AI hour + batch window + reflection section)
- Interactive checkboxes (clickable on screen, print-ready)
- Research citations: Gloria Mark (23-min recovery), Robert Bjork (desirable difficulty), Lisanne Bainbridge (Ironies of Automation 1983), Sophie Leroy (attention residue)
- Survey data: 71% ghost authorship stat from 2,147-engineer survey
- Open in browser: "Print / Save as PDF" button

**2. Email Course Sequence** (`email-course/`)
- `ai-fatigue-reset-email-1.html` — Day 1: The Sunday Night Reckoning
  - Naming the four dimensions of AI fatigue
  - Anonymous engineer survey quotes
  - Day 1 assignment: list 3 AI-dependent skills
- `ai-fatigue-reset-email-2.html` — Day 2: Why Resting Doesn't Fix It
  - Three misdiagnoses (burnout / boundaries / overwhelm)
  - Gloria Mark 23-min recovery finding
  - Day 2 assignment: track AI interruptions for one day
- `ai-fatigue-reset-email-3.html` — Day 3: The 23-Minute Rule
  - Sophie Leroy's attention residue research
  - Batching: 90-min work blocks + 15-min AI batch windows
  - Day 3 assignment: set 90-min no-AI timer
- `ai-fatigue-reset-email-4.html` — Day 4: The No-AI Hour
  - Robert Bjork's desirable difficulty
  - Bainbridge's Ironies of Automation (1983)
  - The No-AI Hour rules (30/45/60/90 min options)
  - Day 4 assignment: schedule no-AI hour on calendar
- `ai-fatigue-reset-email-5.html` — Day 5: The System, Not the Sprint
  - Four anchors: calendar protection / batch AI / Explanation Requirement / Sunday recalibration
  - The Dispatch weekly newsletter CTA
  - Full site CTA
- `SEQUENCE.md` — Setup manifest:
  - Send cadence: 1 email per day for 5 days
  - Formspree setup notes
  - Mailchimp/ConvertKit drip sequence setup
  - Metrics to track (open rate, CTR, unsubscribe)
  - Compliance notes (UNSUB, GDPR)

**3. Landing Page Update** (`email-course.html`)
- Added PDF lead magnet download section before testimonials
- "📄 Download Printable Checklist →" CTA linking to ai-fatigue-recovery-checklist.html
- Side panel: 20 Practices / 30-Day Tracker / Print-Ready PDF badges
- Email-course.html nav now includes "📋 Checklist" link

**4. Index Feature Card** (`index.html`)
- Added new "Printable PDF Checklist" feature card
- Highlights: 20 practices, 30-day tracker, weekly planner, research-backed

**5. Sitemap** (`sitemap.xml`)
- Added ai-fatigue-recovery-checklist.html (priority 0.8)
- Added email-course/ai-fatigue-reset-email-1.html (priority 0.3)

**6. TRACKER.json** — P4 windows: 69 → 70

## SEO Impact
- **Newsletter funnel:** Email landing page (email-course.html) now has actual content sequence + lead magnet to convert visitors
- **PDF lead magnet:** High-value downloadable resource = linkable from therapist directories, HR blogs, devrel newsletters
- **Email sequence:** 5 research-backed emails (Leroy, Mark, Bjork, Bainbridge) with clear conversion path to Dispatch
- **Print-optimized page:** Direct print/Download PDF = engagement signal + low bounce rate

## Site Stats
- Pages: 143 pages built
- Words: ~429k words
- Sitemap: 138 URLs
- P4 windows: 70/95 target

## Phase Status
- Phase 1 (Content): 115 windows ✅ (nearly complete)
- Phase 2 (Outreach): 123 windows ✅
- Phase 3 (SEO): 87 windows ✅
- Phase 4 (Community): 70 windows ⚠️ (under-indexed vs others)

## Outstanding Blocker
- **Formspree not set up** — all forms still use `YOUR_FORM_ID` placeholder
- Newsletter signup, testimonials form, checklist form all non-functional
- Priority: next P4 window should set up Formspree

## Next Window (P4)
1. Set up Formspree account + replace all `YOUR_FORM_ID` placeholders
2. Create Dispatch issue #30 (weekly email to existing subscribers)
3. Test email sequence HTML templates in actual email client
4. Or: engineer testimonials outreach campaign (testimonials-campaign.html already built)
