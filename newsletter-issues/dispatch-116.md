# The Invisible Carries
### Issue #116 — July 10, 2026

---

Something happened before you shipped that feature last Tuesday.

You asked AI to generate the authentication module. It did. You reviewed it, found it reasonable, and shipped it. The feature worked. Nobody pushed back. The ticket closed.

But something was working while you were working that day.

You were managing a hidden load: the cognitive overhead of operating as a supervisor rather than an author, the responsibility for decisions you didn't author but now own, the justification load for architectural choices you didn't evaluate before accepting, the context debt accumulating as AI-generated code fills gaps you'd normally have to understand.

This is "invisible carrying" — the quiet cognitive work of overseeing AI output that doesn't show up in any metric but depletes you just the same.

---

## What's Being Carried Without Your Notice

The metaphor of carrying is precise. When you oversee AI-generated work, you are transporting something that would otherwise have a weight — except the weight is invisible and the transportation is constant and the path is uphill.

Three invisible carries show up repeatedly in high-AI-use engineers:

### The Responsibility Gap

AI made the decision. You own it anyway.

Every architectural choice embedded in AI-generated code is on your head when it fails in production at 2am. You accepted the output without evaluating the alternatives, because evaluating the alternatives would have required the same work AI was supposed to save you from.

The responsibility gap creates a specific kind of acute stress: accountable for decisions you didn't consciously make. This is different from normal engineering responsibility — normally you evaluate, decide, implement, and own the trade-offs. With AI, the decision step happens without your judgment engaged, but the outcome lands in your lap regardless.

### The Context Debt

When you build something yourself, you hold the full context in working memory during the build. The trade-offs you rejected, the constraints you navigated, the "why" of the approach — this context is loaded into your understanding as you go. It survives in your mental model.

When AI generates the code, the context doesn't transfer. You have the output. You may understand the output. But the working memory of why this approach was chosen over the alternatives you didn't evaluate — that context is absent better by the efficiency of the generation.

Over a full day of AI-assisted work, the context debt compounds. By the end of the day, you're overseeing a system whose full context is distributed between AI logs, generated code, and your partial understanding of both. Managing that distribution is real cognitive work.

### The Justification Load

When you build something yourself, you can explain why it works because you built it. The explanation emerges from understanding.

When AI builds it, you're downstream of an explanation someone else generated — AI. To explain the code to a colleague, you have to go back and understand it first, or reproduce AI's explanation, or deflect. The engineer who asks "why did you choose this approach?" expects your engineering judgment, not your ability to narrate what AI told you.

This creates a continuous justification load: the ambient awareness that you may not be able to explain what you're responsible for, and the ongoing effort to maintain enough understanding to be credible.

---

## Why It Doesn't Show Up in Metrics

Standard engineering metrics measure flow: tasks completed, PRs merged, stories closed. Invisible carrying doesn't appear in any of these.

If anything, it looks like productivity improvement. You're shipping faster. The task board is cleaner. Your velocity is up.

The invisible carrying depletes your cognitive resources while improving the visible metrics that measure whether you're doing work. This is the perverse property that makes AI fatigue so hard to identify from the outside.

Your team's velocity dashboard shows improvement. Your internal experience shows something quieter and harder to name: the growing difficulty of caring about the work in the way you used to. The mild resistance to owning decisions. The vague sense that you should be able to explain more than you can.

---

## What Actually Helps

The interventions aren't complex, but they require commitment and they have to be repeated:

**The Explanation Requirement**: After every significant AI-assisted implementation, write three sentences in your own words about why the approach works. Not what the code does — why this approach was chosen. If you can't write three sentences, read the code until you can. This sounds tedious. It's less tedious than the compounding context debt.

**The Supervision Boundary**: Treat AI output as a first draft, not a finished product. Every significant implementation deserves a human review that engages the design question — is this approach right, not just functional? This is the work that used to happen during building. You have to do it after.

**The Weekly Context Audit**: Every Friday, before you close the week, ask yourself: could I explain the three biggest architectural decisions I accepted this week, unprompted? If not, that's your weekend reading.

---

## The Asymmetry Nobody Talks About

There's an asymmetry at the heart of AI-assisted work that's worth sitting with:

AI generates the output. You generate the accountability.

This isn't a reason to reject AI tooling. It's a reason to be precise about what you're taking on when you accept AI output. You're not just getting a productivity boost. You're taking on a supervision load that your workflow probably doesn't account for, and distributing it across every task you move through AI-assisted.

The engineers who are navigating this well aren't the ones using less AI. They're the ones who've found systematic ways to manage the invisible carries — by auditing their own understanding, by writing explanations they otherwise wouldn't have to write, by treating AI output as something they have to understand rather than something they can approve.

The clearing is in the explicitness. Making the invisible visible is the first step to managing it.

---

*This week, pay attention to what you're carrying that isn't showing up anywhere. The invisible carries add up.*

<div class="dispatch-cta">
<p><strong>The AI Fatigue Quiz</strong> identifies where you are with invisible cognitive loads and gives you a specific tier-based recovery path. Takes 90 seconds.</p>
<a href="../#quiz" class="cta-btn">Take the AI Fatigue Quiz →</a>
</div>
