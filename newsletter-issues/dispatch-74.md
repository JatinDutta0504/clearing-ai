# The Dispatch #74 — The Judgment Tax
# For: Engineers who use AI tools daily
# Date: June 22, 2026 (Sunday night send)
# Theme: Every time you let AI decide instead of you deciding, something expensive happens that doesn't show up on the invoice.
---

## Hero
**The Judgment Tax: What's Actually Being Charged When You Offload Decisions to AI**

There's a cost to AI-assisted decisions that nobody prices out.

When you ask an AI what architecture to use, what test to write first, how to structure a PR description, or which of three approaches is cleanest — the AI gives you an answer. The answer is usually fine. The transaction feels free.

It isn't.

Every time you let a model decide instead of you deciding, you pay a small tax: the judgment that could have formed in that moment doesn't form. The decision gets made. The reasoning doesn't develop.

This week's Dispatch is about that tax — what it looks like in practice, how it compounds, and what it costs you over months and years that velocity metrics will never show.

---

## Section 1: What the Judgment Tax Actually Is

The judgment tax is the gap between decisions you make and decisions you let AI make.

It shows up in three ways:

**The decision that didn't teach you anything:**

You asked AI which error handling pattern to use. It gave you a good answer. You implemented it. You didn't weigh options, consider tradeoffs, or develop a feel for why one pattern fits better in one context and not another. The decision happened. Your judgment around error handling didn't advance.

One instance of this is invisible. Do it two hundred times and you've paid the judgment tax two hundred times. The code is correct. Your ability to think about error handling hasn't grown.

**The tradeoff that never got considered:**

You asked AI how to structure a migration. It gave you a plan. The plan was reasonable. But in the process of thinking about how to structure a migration — the risks, the rollback options, the testing strategy, the edge cases — you'd have exercised a kind of judgment that architecture planning requires.

The AI's plan was better than what you would have come up with on your own, probably. But the judgment you would have exercised in producing your own plan was worth more, over time, than having the better plan.

**The pattern you recognized without realizing you recognized it:**

You saw the AI's solution and immediately knew it was right. That flash of recognition — the feeling that clicks when you see something that fits — is your judgment working. But if you didn't generate the alternatives, if you didn't hold multiple options in mind before the right one emerged, the recognition was faster but thinner.

Pattern recognition deepens through effort. When AI pre-loads the answer, the recognition happens without the search. The result is the same. The formation is incomplete.

---

## Section 2: The Compounding

The judgment tax doesn't show up in any individual decision. It shows up in the aggregate.

After enough months of AI-assisted decisions, you have: a codebase you can navigate, code you can modify, and an increasingly distant relationship with the reasoning that produced it.

The pattern looks like this:

**Month 1-3:** AI handles decisions. Output is good. You feel productive.

**Month 4-6:** You notice AI suggestions becoming more familiar. You're recognizing patterns you didn't develop. The recognition feels like understanding.

**Month 7-12:** You can maintain and extend code you didn't design. You have less feel for why the design decisions were made. When something goes wrong in an unexpected way, it takes longer to diagnose because you don't have the mental model the design was built on.

**Year 2:** You're effective with AI assistance. Without it, the gap between what you can do and what you understand is significant. You know how to prompt. You don't always know how to think.

The judgment tax compounds quietly because the output — the code, the feature, the system — still looks fine. It's only over time that the accumulation of decisions made without you reveals itself as a thinner foundation than it appeared.

---

## Section 3: Where It Shows Up Most

The judgment tax is highest in the decisions that feel lowest-stakes.

**"Which test should I write first?"**

This seems like a tactical question. But deciding what to test first — and why — is a form of risk prioritization. It's about understanding what matters in a system, what would hurt most if it broke, where the actual complexity lives.

When AI tells you what to test first, you get the test. You don't get the risk-calibration thinking that deciding the question was supposed to develop.

**"Is this clear enough or should I add a comment?"**

This is a judgment about what will be legible to the next human who reads this code — probably you, two years from now, debugging at 11pm. It's a form of empathy and prediction.

When AI decides to add a comment or not based on what it thinks is clear, you bypass the exercise of predicting what will actually be confusing to a future reader.

**"What's the priority here?"**

Deciding what matters most — in a backlog, in a design, in a debugging session — is a form of judgment that develops through practice. It requires holding multiple values in mind simultaneously and weighing them against each other.

When AI prioritizes for you, you get the right priority. You don't get the experience of weighing the values that produced it.

---

## Section 4: How to Recover the Judgment

The judgment tax is recoverable. Unlike skill debt, which requires deliberate rebuild, judgment can be recovered through a different practice: generate-before-receive.

**The 5-minute generation rule:**

Before you look at any AI suggestion, spend five minutes — even rough, even imperfect — generating your own answer. Not a complete solution. A direction. A guess about what approach is likely right and why. Then look at what the AI produced.

This is not about being right. It's about exercising the judgment muscle before the AI's answer loads. Your answer doesn't have to be better. The exercise of producing it is the point.

**The explanation requirement:**

When you receive an AI decision — this pattern, this test, this approach — write one sentence explaining why it makes sense in this context. Not what it does. Why it fits here.

If you can't write that sentence, the judgment didn't transfer. Read the code again. Ask yourself what the AI was responding to. Generate the explanation.

**The alternative rejection log:**

When AI suggests approach A and you implement A, note what alternatives you considered and why A was better. Not in the commit message — in a personal log. The act of articulating why A > B/C is the judgment exercise.

Over time, this log becomes a record of your own decision-making patterns. It shows you how you think, which is more important than what you know.

**The question before the question:**

Before asking AI a decision-question ("should I use X or Y?", "what's the best way to structure this?") — ask yourself the question first, for two minutes, out loud or on paper. State the problem. Note what you think matters. Guess the answer.

Then ask the AI. Compare. The delta between your guess and the AI's answer is where judgment develops.

---

## Section 5: The Longer View

The judgment tax is paid in small installments that feel like nothing in the moment and reveal themselves as significant over time.

The solution isn't to stop using AI for decisions. It's to stay in the loop — to make sure that when AI decides, you still decided first. Not because your answer is better. Because the exercise of producing an answer is the thing that develops the capacity to produce good answers.

The engineers who will have the most durable careers in the AI era are not the ones who use AI most effectively. They are the ones whose judgment keeps pace with their output — where every artifact produced reflects their thinking, not just their prompting.

The goal isn't to do it the hard way. It's to make sure the hard way's benefit — the judgment formation — isn't being waived in the transaction.

---

## CTA Block

If you're noticing the judgment tax in your own practice — the gap between what you can produce with AI and what you understand about why it works — the AI Fatigue Quiz surfaces where else this dynamic shows up in your daily experience.

→ [Take the AI Fatigue Quiz](https://clearing-ai.com/quiz.html)

The [manifesto on intentional AI use](https://clearing-ai.com/manifesto.html) goes deeper on staying in the loop — including the specific decisions where you need to stay in the chair, not just sign off on the output.

→ [Read: An Engineer's Manifesto for Intentional AI Use](https://clearing-ai.com/manifesto.html)

---

## Closing

The judgment tax is small in any individual decision. It's significant in aggregate. The practice of recovering it — generating before receiving, explaining before accepting, logging the alternatives — isn't about resisting AI. It's about making sure the judgment you're developing keeps pace with the output you're producing.

The code can be right while your judgment is still catching up. That's fine for now. The question is whether you're doing the work that closes the gap.

— The Clearing

*P.S. If you've noticed the judgment tax in your own practice — or if you have a method for staying in the decision loop that isn't just "try harder" — hit reply. This Dispatch goes to a lot of engineers and some of them have figured out practical approaches. I'd like to hear what's working.*

---

*Not subscribed yet? [Join 2,400+ engineers](https://clearing-ai.com/newsletter.html) getting The Dispatch weekly.*

*Missed an issue? [Browse the archive →](https://clearing-ai.com/newsletter-archive.html)*