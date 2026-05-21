# The Dispatch #75 — The Visibility Trap
# For: Engineers who use AI tools daily
# Date: June 29, 2026 (Sunday night send)
# Theme: When AI writes half your code, your manager can't see your judgment — even when it was the most important part of what you did.
---

## Hero
**The Visibility Trap: Why the Best Engineers Are Getting Hardest to Evaluate**

There's a problem emerging in performance reviews, promotion decisions, and hiring conversations that nobody has named clearly yet.

It's not that AI is making engineers less capable.

It's that AI is making individual engineers less *legible* — the judgment, context, and decisions that constitute real expertise are increasingly invisible in the artifacts that get reviewed.

The engineers who are navigating this best aren't necessarily the ones doing the best work. They're the ones who've figured out how to make their thinking visible when the code itself is ambiguous.

---

## Section 1: What the Visibility Trap Is

The visibility trap is the gap between what an engineer knows and what their work shows.

When you write code from scratch, your thinking is embedded in the artifact. The design decisions, the edge cases you anticipated, the tradeoff you resolved in favor of maintainability over speed — all of it is legible in the result. Your manager can read your judgment through your code.

When AI writes 40% of your code, that 40% is the model's judgment, not yours. The artifact is correct. The thinking is invisible.

Over time, this creates an evaluation problem: your output looks like it includes work that isn't yours. Your manager sees code you shipped but can't tell which parts reflect your thinking and which parts reflect the model's. Your actual expertise becomes undetectable from the outside.

The trap is this: the better AI you use, the less visible your contribution becomes — even when your contribution (the decisions, the judgment, the direction) was more valuable than the code itself.

---

## Section 2: How It Shows Up in Practice

The visibility trap manifests in specific, recognizable ways.

**The code review that tells you nothing:**

You get feedback on a PR. The reviewer comments on the AI-generated portions — things that were reasonable defaults, not decisions you made. Your actual decision — the tradeoff you resolved, the architecture you chose, the constraint you worked within — goes unmentioned. Not because it was unremarkable. Because it didn't appear as code.

Your evaluation is based on the surface of your work, not the thinking underneath it.

**The promotion packet with no story:**

You're up for senior. Your manager needs to write a promotion case. She has your output — features shipped, metrics improved, code merged. What she doesn't have is the narrative of your thinking. The problems you solved before they became visible. The calls you made that the AI didn't make for you. The judgment you exercised in the AI-assisted work.

She can write about what you shipped. She can't fully write about what you decided.

**The reference check that can't go deep:**

A reference calls to discuss you. They say you shipped a lot of code. They ask what problems you solved that AI couldn't have solved. The honest answer requires explaining which judgments were yours and which were the model's — and that distinction is genuinely hard to articulate from the outside.

**The hiring signal that misfires:**

A company is evaluating you for a senior role. They can see you shipped extensively with AI tools. They can't see the decisions that shaped what shipped. Are you someone whose judgment scaled the output? Or are you someone whose output replaced their judgment? The code looks identical.

---

## Section 3: Why This Falls on Individual Engineers

The visibility trap is not a systemic failure — it's a structural feature of AI-assisted work that falls hardest on the individual.

Companies haven't built frameworks for evaluating the judgment underneath AI-assisted code. Performance processes are still organized around output: features shipped, PRs merged, bugs resolved. AI assistance increases output and decreases the legibility of the judgment behind it.

This means the burden of visibility falls on you.

The engineers who navigate this well do a specific thing: they make their thinking legible even when the code isn't fully theirs.

This shows up as: explaining their decisions in code review comments, writing architecture decision records, verbally walking through tradeoffs they resolved, documenting the "why" in PR descriptions, pairing on the design before the AI writes the implementation.

They're not showing their work. They're showing their thinking — and their thinking is what distinguishes them from the AI.

---

## Section 4: Specific Tactics for Making Your Judgment Visible

**Write the decision before you write the code:**

Before any significant implementation, write 3-5 sentences on what you're about to build, why you chose this approach, and what you decided against. Paste that into the PR description or a comment in the code. This is your thinking becoming legible — it shows the judgment that preceded the AI's output.

**Name what AI did in code review:**

When a reviewer asks about a specific piece of code, a useful answer is "I made this decision; the AI implemented it." Or: "This was a default from the AI; I reviewed and accepted it." Neither is better or worse. Both are honest. Both make your role clear.

**Use architecture decision records:**

For any significant system design, write a short ADR (Architecture Decision Record): what you decided, why, what alternatives you considered, and what you decided against. This is pure judgment documentation — exactly the thing AI doesn't produce.

**Narrate your tradeoffs in 1:1s:**

Don't assume your manager sees the judgment in your work. Tell them. "In this sprint I made the call to optimize for maintainability over velocity — the AI would have gone the other way. Here's why I overrode it." This is not bragging. This is making your expertise legible.

**Document the AI's contribution honestly:**

In code comments or PR descriptions, note what was AI-generated and what you directed. "AI-generated implementation of the approach we discussed in the design doc" is more useful than it sounds — it shows the human direction that shaped the output.

---

## Section 5: The Longer View

The visibility trap is a real problem that will get more pronounced, not less.

As AI coding tools become more capable, the output gap between AI-assisted and non-AI-assisted engineers will widen. The code will be better. The thinking will be harder to see. The engineers whose judgment is most valuable will be the least legible if they don't actively work to make it visible.

This isn't about protecting yourself. It's about the problem nobody is solving:

Companies don't know how to evaluate AI-era engineers. Performance frameworks are built for a world where output maps to individual contribution. That mapping is broken — and it won't be fixed by HR processes in the next 12-24 months.

The engineers who navigate this well will be the ones who made their thinking visible before they needed it to be visible.

The engineers who don't will find themselves in promotion conversations, hiring processes, and performance reviews where the work looks good and the story is hard to tell.

---

## CTA Block

If you're noticing the visibility problem in your own practice — the gap between what you know and what your work shows — the AI Fatigue Quiz surfaces where else this dynamic shows up in your daily experience.

→ [Take the AI Fatigue Quiz](https://clearing-ai.com/quiz.html)

The [manifesto on intentional AI use](https://clearing-ai.com/manifesto.html) goes deeper on staying visible while using AI tools — including the specific practices that make your judgment legible even when the code isn't fully yours.

→ [Read: An Engineer's Manifesto for Intentional AI Use](https://clearing-ai.com/manifesto.html)

---

## Closing

The visibility trap is not a failure of AI, and it's not a failure of you. It's a structural feature of a new way of working that nobody has fully figured out yet.

The good news: the engineers who figure this out — who learn to make their thinking legible, who narrate their tradeoffs, who write the decision before they write the code — will be the ones who stay visible even as the tools get more capable.

The engineers who don't will have done excellent work that tells an incomplete story.

Make your story complete.

— The Clearing

*P.S. If you've found ways to make your thinking more visible in AI-heavy work — specific practices, specific tools, specific moments where you deliberately chose legibility over speed — hit reply. This is a problem that engineers are solving in private and the solutions are worth sharing.*

---

*Not subscribed yet? [Join 2,400+ engineers](https://clearing-ai.com/newsletter.html) getting The Dispatch weekly.*

*Missed an issue? [Browse the archive →](https://clearing-ai.com/newsletter-archive.html)*