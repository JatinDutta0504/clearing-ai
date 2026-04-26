---
title: "The Attribution Problem"
number: 42
date: 2026-04-26
description: "When AI does the work, how do you show your manager what you actually contributed? A practical guide to being seen."
---

# The Attribution Problem

*A letter about something nobody talks about clearly.*

---

Here's a question that comes up constantly in the engineers who write to us:

*"How do I show my manager that I'm still doing real work?"*

The engineers asking this aren't slacking off. They're not hiding behind AI. They are working hard — thinking through problems, reviewing AI-generated code, making architectural decisions, asking the right questions. But something feels invisible. The output looks like it came from AI. The thinking feels like it didn't count.

This is the attribution problem. And if you're feeling it, you're not imagining it.

---

## Why It Feels So Strange

Before AI, work had a visible texture. Your manager could see you wrestling with something for hours. They could see the code you wrote. They could see the PR you reviewed. They could see the problem you understood deeply enough to explain it in a meeting.

AI has made the texture invisible. The wrestling happens in the gap between what AI produces and what you actually understand. The code appears on the screen. The explanation sounds fluent. The decision about what to build and why — that happened in your head, but nobody saw it happen.

The result: you feel like you're not contributing. Your manager may feel like you're coasting. The work is still real. The contribution is still real. But the story you can tell about it has changed.

This is the part of AI fatigue that nobody writes about.

---

## The Three Layers of What's Being Lost

**Layer 1: The visible wrestling.**

In the old workflow, you wrestling with a problem was evidence of work. Your manager could watch you struggle for an afternoon and know: this engineer is figuring something out.

With AI, the wrestling moves. Sometimes you're wrestling with the problem before you know what to ask AI. Sometimes you're wrestling with whether the AI output is right. Sometimes you're wrestling with how to explain it to your team. But all of that happens in your head, in the gaps — and the gaps aren't visible from the outside.

**Layer 2: The legible decision.**

Senior engineers make invisible decisions constantly. You chose the approach, not the other approach. You understood why the requirement was wrong. You anticipated the edge case. You named the risk that nobody else had thought to name.

None of that shows up in the code AI wrote. But it all still happened.

**Layer 3: The explained understanding.**

This is the subtlest one. When you understand something deeply and explain it, the explanation is legible. People can hear your thinking. With AI-generated explanations, the thinking looks like it belongs to the tool.

When you explain AI's output to your team, you are demonstrating understanding. But the demo sounds like you're describing what the tool did, not what you know.

---

## The Four Failed Responses

Engineers usually respond to this invisibility in ways that make it worse:

**1. Working longer hours.**
The instinct: prove you're doing real work by doing more of it. The problem: AI generates more in an hour than you could write in a day. More output means more AI, which means less visible human contribution. The treadmill accelerates.

**2. Hiding AI use.**
The instinct: if AI is what's making me invisible, I'll stop using it. The problem: this tanks your productivity, creates friction with teammates who are using AI, and doesn't actually solve the attribution problem — it just makes you slower and less effective.

**3. Over-narrating your contributions.**
The instinct: make sure everyone knows what you did. The problem: constantly framing everything as "I decided to..." comes across as defensive and self-justifying. It makes you look insecure rather than accomplished. Nobody wants to work with someone who narrates their own achievements.

**4. Waiting for someone to notice.**
The instinct: the work speaks for itself. The problem: in an AI-assisted workflow, the work doesn't always speak for itself. The gap between what you know and what you can show has widened. If you don't actively close it, it stays open.

---

## What Actually Works

The solution is not doing less with AI. The solution is learning to narrate your judgment in a way that AI can't generate.

**1. Name the constraints you held.**
AI generates options. You chose constraints. When you review AI output, the thing that matters isn't what the model produced — it's what you rejected, and why.

"The approach AI suggested would have scaled poorly under write-heavy load, so I redirected it. Here's what I changed and why."

That's not self-narration. That's thinking. And thinking is what AI cannot do.

**2. Surface the decision before the implementation.**

Instead of: "AI generated this implementation"

Try: "We needed to handle three failure modes here. I asked AI for options for each, then picked approach A because of X, and built a hybrid for approach B."

The before-and-after structure shows that your judgment shaped the outcome, not just your cursor.

**3. Explain the why at the architecture level.**

Architectural decisions are the one thing AI genuinely cannot make without you. You know the context. You know the tradeoffs. You know the history of the system and why one approach would cause problems three months from now.

When you walk your team through the "why" of an implementation, you're not narrating your work — you're demonstrating expertise. This is legible. This is valuable. This is what AI can't replace.

**4. Add the part AI can't write.**

After every AI-assisted task, write down: what did you know that the AI didn't? What context did you provide that changed the output? What did you reject and why?

This is a calibration practice. It keeps you honest about your actual contribution. And it gives you concrete answers when your manager asks what you've been working on.

**5. Make the invisible work visible, but concise.**

The single most effective thing you can do: write a brief weekly summary that includes your reasoning, not just your outputs.

Not: "Shipped feature X, reviewed 4 PRs, fixed bug Y."

Instead: "Shipped feature X — made the call to defer auth until v2 after seeing the complexity cost. Reviewed 4 PRs, pushed back on one architecture that would have created a hard-to-debug dependency cycle. Fixed bug Y by identifying that it was a symptom of the caching layer, not a standalone code issue."

That second version is 3x more informative. It shows judgment, context, and initiative. AI cannot write that. You can.

---

## The Honest Framing

The attribution problem is real. It is structural. It comes from the fact that AI separates the visible output from the invisible thinking that shaped it.

The engineers who navigate this well are not the ones who do more with AI, or less with AI. They're the ones who have learned to show their reasoning — not their outputs — as their primary contribution.

Your actual job, in an AI-assisted workflow, is increasingly this: not to write the code, but to know what the code needs to do, why it needs to do it that way, and what would go wrong if it were done differently. That knowledge is invisible by default. Learning to make it visible is the skill.

Until next Thursday.

— *Sunny*
*The Clearing*

---

**P.S.** If you're heading into a performance review cycle: our [manifesto on the Explanation Requirement](https://clearing-ai.com/the-explanation-requirement.html) was built exactly for this moment. 5 minutes of reading. Take it with you.

**P.P.S.** This is Dispatch #42. If you're just joining us, you can read the full archive at [clearing-ai.com/newsletter-archive.html](https://clearing-ai.com/newsletter-archive.html).
