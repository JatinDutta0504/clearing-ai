---
title: "The Disowning"
number: 49
date: 2026-05-23
description: "The moment you open your own code and can't explain how it works. Why AI makes engineers strangers to their own work."
---

# The Disowning

*A letter about the growing gap between what you ship and what you know.*

---

There's a specific feeling worth naming.

You open a file. Your name is in the commit history. You wrote this. And you have no idea how it works.

Not the surface level — you can read it. You can trace the logic if you concentrate. But if someone asked you to explain why it was designed this way, or what would break if you changed that condition, or whether this approach still makes sense given how the system evolved — you'd be guessing.

This is not imposter syndrome. This is not normal forgetting. This is a specific phenomenon: the work you produced without the understanding that usually comes with it.

---

## What the Disowning Actually Is

The disowning happens when your brain records output without recording the reasoning that produced it.

Normally, when you build something yourself — when you struggle with a design problem, argue with yourself about trade-offs, get something wrong and debug your way back — that reasoning process gets etched into memory. The effort is the encoding mechanism. The struggle is the teacher.

When AI handles the difficult part, the struggle disappears. The output arrives. Your brain records: "this got solved." It does not record the reasoning that would have happened if you'd done the solving.

Over time, the gap between what you've produced and what you understand grows. You have more output than ever. You have less understanding than ever, relative to what you've built.

And at some point — often triggered by something small — you open your own work and feel like a stranger reading someone else's code.

---

## Why It Creeps Up Slowly

The disowning is invisible because it doesn't feel wrong while it's happening.

The work gets done. The code ships. The feature launches. There's no immediate consequence that makes you aware something was missing from the process. The missing understanding is invisible — it only shows up later, when you need it.

And the thing is, you can coast on accumulated understanding for longer than you think. The knowledge you built before AI became central carries you through a lot. You have enough context from the years of doing things yourself that AI-generated code often fits into mental models you already have.

Until it doesn't.

Until you open a file you wrote six months ago and realize the architecture decision that felt obvious then now feels arbitrary. Until you need to extend something and can't remember why the original approach was chosen. Until someone asks a question in a retro and you realize you're describing what the code does while avoiding the question of whether you know why it does it that way.

The moment of reckoning only arrives after the gap has been growing for a while. That's what makes it so disorienting when it arrives.

---

## The Specific Mechanism

There's a cognitive phenomenon that explains this:

When you understand something deeply, you hold multiple models of it — the mental model, the code model, the execution model. These are connected. When you need to reason about the system, you move between them fluidly. That's what makes you effective at debugging, extending, and explaining your own work.

When AI generates code you don't fully understand, those models don't get built. You have the code model — you can read it — but you don't have the underlying reasoning that would connect it to your mental model of the system. The abstraction layer is missing.

This is why engineers often feel competent reading AI-generated code but not confident extending it. Reading is pattern matching. Extending requires the deeper models that only get built through genuine struggle.

---

## The Compound Effect

Here's what makes this particularly insidious:

The less you understand your own code, the less satisfying the work feels. This creates a subtle motivation to stay in surface-level interaction — reading what AI produced, modifying it slightly, shipping it — and avoid the deeper engagement that would build real understanding.

You might notice yourself getting more passive. Less curious about why something works. More focused on getting to "done" and less interested in whether you'd actually be able to rebuild it from scratch.

The passivity compounds. The understanding gap grows. The work becomes more purely transactional — input in, output out — and less like something you're actually building mastery through.

This is also why the disowning often shows up first as a motivation problem rather than a skill problem. You feel less ownership over the work before you notice the skill gap. The loss of satisfaction is the first signal.

---

## What It Looks Like Day to Day

A few common forms:

**The "it works, I guess" feeling.** Code ships and you feel nothing. Not pride, not satisfaction, just relief that it's done. The work used to feel like yours in a way that mattered.

**The "I'd have to re-read this" default.** When asked about code you wrote, your first response is "let me look at it again" — even though you were the one who wrote it.

**The explain-by-paraphrasing problem.** Someone asks a question about a system you own and you find yourself paraphrasing what the code does rather than explaining the reasoning behind it. You describe the implementation without touching the design intent.

**The documentation gap.** You can't write meaningful documentation because the documentation would require explaining why decisions were made — and you don't remember making them.

**The meeting avoidance.** You start quietly hoping no one asks you about the parts of the system you're least certain about, because you're not sure what you'd say.

---

## The Practice That Starts to Close It

The Explanation Requirement is the practice we've found most effective for this:

After any significant AI-generated contribution — a feature, a refactor, a fix — write a three-sentence explanation: what the problem was, why this approach was chosen, and what edge cases this handles.

Three sentences. No code snippets. Just your reasoning.

The act of writing those three sentences forces the connection between the output and the reasoning. It won't fully rebuild the understanding you missed — nothing fully replaces the struggle — but it creates a bridge. The next time you open that file, those three sentences will be there. They'll anchor the code to the reasoning that produced it.

Over time, a file of these explanations becomes a map of what you actually understand versus what you've just had AI produce. It's the most honest record you can keep.

---

## One Question to Sit With

Think about the last piece of code you shipped that you couldn't explain in detail — the why behind the design, not just the what.

What was it? And do you wish you understood it better — or have you already stopped thinking about it?

The disowning becomes complete when you stop wishing you understood. If that wish is still alive, there's something to recover.

---

## From the Community

*"I spent two weeks building a feature with heavy AI help. At the end, my manager asked me to walk through the architecture in a 1:1. I could describe what it did. I could not explain why the decisions were made the way they were. I told him I'd need to review it and he looked at me like 'didn't you write this?' I had. But I didn't feel like I had."*

— Mid-level engineer, 4 years, backend team

If this resonated, [take the 5-minute AI Fatigue Quiz](https://clearing-ai.com/quiz.html). Fourteen thousand engineers have taken it. The quiz gives you a tier and a language for what's happening — with or without AI in the room.

---

## This Week's Recommended Read

[developer-identity.html](https://clearing-ai.com/developer-identity.html) — Who Am I Without My Code? Developer Identity in the AI Era. For anyone who has noticed the gap between what they ship and what they feel ownership over.

---

## One Thing You Can Do Today

Find one file in your current project that AI helped generate significantly. Open it. Try to answer three questions: Why was this approach chosen? What would break if you changed the core logic? What does this interact with?

If you can't answer those three, that's the gap. That's where the work is.

See you next week.

— Sunny
*clearing-ai.com*