# Social Badges — Shareable AI Fatigue Score Badges

## Concept
Engineers who complete the AI Fatigue Quiz and land on Tier 2+ are presented with a shareable badge. The badge is a PNG downloadable image — post it on LinkedIn, Twitter, or share anywhere. Each badge links back to clearing-ai.com/quiz for discovery.

## Viral Loop
```
Quiz completion → Tier 2/3/4 result → "Download your badge" CTA → PNG download → Share on LinkedIn/Twitter → Viral discovery → New visitors → Quiz completions
```

## Badge Designs

### Style 1: Forest (🌿 Tier 1-2)
- Background: #0f2419 (dark forest green)
- Accent: #3dd68c (mint green)
- White text
- Leaf SVG accent top-right
- Tier name in large caps
- Quote in italic

### Style 2: Slate (🌤 Tier 2-3)
- Background: #1a1d29 (dark blue-grey)
- Accent: #f0b429 (warm amber)
- White text
- Subtle geometric pattern
- Tier name in large caps
- Quote in italic

### Style 3: Midnight (🌧 Tier 3-4)
- Background: #0a0a14 (deep navy-black)
- Accent: #6366f1 (indigo)
- White text
- Storm-cloud pattern
- Tier name in large caps
- Quote in italic

### Style 4: Dawn (🌑 Tier 4 — crisis)
- Background: #1a1214 (dark burgundy)
- Accent: #e879f9 (magenta)
- White text
- Soft glow
- More sensitive/warm messaging
- "Your body is asking for rest." messaging
- Links to recovery resources

## Elements per badge
- The Clearing wordmark (SVG text)
- Tier badge (icon + name)
- AI Fatigue Score line ("AI Fatigue Score: Tier 3 — Real Fatigue")
- Short quote (2-3 sentences, tier-specific)
- "clearing-ai.com" URL
- Optional: name (user-entered)
- Optional: score date

## Technical
- Single HTML page: `social-badges.html`
- Canvas API for rendering
- Download as PNG (600×400)
- Twitter Web Intent share
- LinkedIn share URL
- Tier selector (1-4)
- Style selector (4 styles)
- Name input (optional)
- Dark mode always

## Share Copy

### Twitter
```
I took the AI Fatigue Quiz from @TheClearingHQ.

Tier 3: Real Fatigue Is Setting In.

If this sounds like you → clearing-ai.com/quiz

#AIFatigue #SoftwareEngineering
```

### LinkedIn
```
I recently took the AI Fatigue Quiz from The Clearing — a free resource for engineers experiencing the cumulative cost of AI-assisted work.

Result: Tier 3 — Real Fatigue Is Setting In

The quiz helped me name something I'd been feeling for months. Worth taking if you're a software engineer: clearing-ai.com/quiz
```

## Status
- Badge canvas generator: READY to build (social-badges.html)
- 4 styles designed
- Share copy drafted
- Viral loop documented
