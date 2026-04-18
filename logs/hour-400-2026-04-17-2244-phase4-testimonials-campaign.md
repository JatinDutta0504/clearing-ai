# Hour 400 — 2026-04-17 22:44 PDT (Sat Apr 18 05:44 UTC)

## Phase 4 — Community Building

### What was built
**`testimonials-campaign.html`** — The Clearing's engineer testimonials campaign hub page.

- **40.5KB**, fully live at `https://clearing-ai.com/testimonials-campaign.html`
- **10 engineer testimonials** with tier badges + share buttons (Twitter/LinkedIn per story)
- **4 email outreach templates** (A=Colleague, B=Manager, C=AI tool discussion, D=Public/Slack) with copy-to-clipboard buttons
- **Share row** with Twitter, LinkedIn, HN, and Copy Link buttons
- **Pre-written share text** for Twitter, LinkedIn, and HN
- **Story submission form** with mailto:hello@clearing-ai.com fallback (Formspree unconfigured)
- **"How This Campaign Works"** guide (4 steps)
- Dark+light mode toggle
- Reading progress bar, skip link, ARIA landmarks
- WebPage + BreadcrumbList schema

### Technical notes
- Build approach: 4-part Python generator scripts (_gen1.py through _gen4.py) to avoid heredoc/quote escaping issues
- The testimonials-campaign.html was assembled by running each generator in sequence (Part 1: head/nav/hero, Part 2: share+how+stories 1-10+outreach, Part 3: submit section, Part 4: JS+footer)
- Nav updated on index.html (added Campaign link near Testimonials)
- sitemap.xml updated with testimonials-campaign.html entry

### Git commit
```
3601acc — Hour 400: Phase 4 — testimonials-campaign.html — engineer testimonials hub page (40KB, 10 stories, 4 email templates, share buttons, campaign guide, story submission form with mailto fallback, dark+light mode, full schema)
13 files changed, 1383 insertions(+), 5 deletions(-)
```

## Phase windows after this window
- P1 (Content): 115
- P2 (Outreach): 122
- P3 (SEO): 87
- P4 (Community): **67** (severely under-indexed vs ~95 target)

## Site stats
- **Pages:** 143
- **Words:** ~429k
- **Interactive features:** 11
- **Sitemap URLs:** 136

## HN context
- HN launch was Fri Apr 17 9AM PDT (~13h ago)
- Cassidoo follow-up #4 was sent at 8AM PDT
- Twitter Thread #19 (Middleman Problem) deployed 12-2PM PDT
- Twitter Thread #20 (Debugger Drift) deployed 10:30AM PDT
- Reddit Weekend 2 package ready for Sat-Sun Apr 19-20

## Open items (Sunny actions needed)
1. **Formspree setup** — configure at formspree.io, replace `YOUR_FORM_ID` in 7 files to enable automated newsletter capture
2. **Mailto newsletter signups** — manually process email signups arriving at hello@clearing-ai.com from HN week
3. **LinkedIn company page** — create at linkedin.com/pages/create to enable LinkedIn Post #1 deployment

## Next window (Hour 401)
- P4 is severely under-indexed (67 vs ~95 target)
- Next high-priority: newsletter growth (lead magnet PDF, Dispatch growth, partnership follow-ups)
- Phase 2 outreach (Reddit/HN follow-up engagement from launch)
- Phase 1 remaining pillars: more Pillar 3 tool overwhelm content