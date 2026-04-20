# AI Tool Overload Page Expansion — Hour 450 Plan

## Strategy
`imposter-syndrome-ai.html` is very well-written but uses classes (.feature-card, .feature-grid, .page-hero, .page-content, .continue-reading) that aren't defined in its own inline styles and may not be in css/style.css either. Fix by using standard classes from css/style.css.

`ai-tool-overload.html` also uses its own inline `<style>` block. Merge into imposter-syndrome-ai.html using the same class-free layout approach as signs-ai-fatigue.html.

## Page to expand: imposter-syndrome-ai.html
**Current:** 556 lines
**Target:** ~900 lines (3.5-4k words)
**Gap:** ~340 additional lines

## Sections to add
1. **The 5 Specific Ways AI Amplifies Imposter Syndrome** (expand existing content)
2. **The "Why Not Me" Problem** — social comparison accelerated by AI
3. **The Competence Ambiguity Test** — interactive self-diagnostic
4. **Real Engineer Stories** — 2-3 anonymous narratives
5. **Recovery Roadmap** — structured 30-day plan for imposter syndrome + AI
6. **Manager's Guide** — how to prevent imposter syndrome in teams using AI
7. **Expanded FAQ** — 8 Q&As total (existing 6 + 2 new)
8. **Internal Links Grid** — 6-card explore grid

## CSS classes available in css/style.css
- .feature-grid / .feature-card ✓
- .continue-reading / .continue-grid / .continue-card ✓  
- .faq-section ✓
- .callout / .callout-warning / .callout-info ✓

## HTML issues to fix
- Unclosed tags in footer/nav (multiple </li> issues)
- Duplicate main id attribute
