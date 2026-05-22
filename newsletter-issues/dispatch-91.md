# Dispatch #91 — The Proxy Productivity Trap

**Week of May 25, 2026**
**Theme: Why shipping faster is the industry's most expensive distraction**

---

## The Opening

A senior engineer I know — fifteen years in, solid reputation — told me last week that he'd started timing how long problems take him without AI assistance.

He called it his "unaided baseline."

Not because he was worried about skill atrophy (though he is). Not because he was building a case for a performance improvement plan. He started doing it because something had stopped feeling right, and he couldn't figure out what.

His unaided baseline was holding steady. His AI-assisted velocity was going up every quarter. The gap between the two numbers was widening, and he wanted to know if he should be alarmed.

The honest answer: nobody knows. Because almost no one is measuring what he's measuring.

---

## The Proxy Problem

The tech industry has a long history of optimizing for the wrong thing. We measured lines of code until that became a joke. We measured story points until everyone gamed them. We measured deployment frequency until we realized speed without quality was just faster breakage.

Now we're measuring shipping velocity with AI.

The proxy has changed. The problem hasn't.

When a developer's output goes from 2 tickets per week to 6 tickets per week, the velocity number looks unambiguous. It's right there in the dashboard. It's shareable in engineering all-hands. It shows up in performance reviews.

What's harder to measure: whether each of those 6 tickets represents the same depth of understanding as each of the 2 tickets used to.

The gap between those two numbers — between what you're shipping and what you understand — is the thing nobody's tracking. Until it shows up as an incident, an architecture decision nobody on the team can explain, or a senior engineer who can't solve a problem in an interview that they definitely would have solved three years ago.

---

## What "Shipping" Actually Means Now

Here's the thing about the word "shipping":

In 2019, shipping meant you wrote code, you understood it, you tested it, you shipped it. There was a continuous thread of understanding from problem to solution.

In 2026, shipping often means: you described the problem to an AI, you evaluated its output, you iterated on the prompt, you merged the suggestion, you moved on.

The output looks the same. The process isn't. And the process is where the learning — or the atrophy — happens.

This isn't an argument against AI tools. It's an observation that the word "shipping" now conceals a wide range of cognitive involvement, and treating all shipping as equivalent is how you end up with teams that produce a lot and understand very little.

---

## The Most Common Version of This

It usually starts like this:

A developer gets a problem. They open a chat window. They describe the problem. They get code back. They read the code, they understand it at the surface level — they could explain what it does — but the deeper understanding of why this approach was right, why this data structure makes sense here, what edge cases this solves — that understanding doesn't come.

So they move on to the next problem.

The next problem takes three exchanges instead of one. The code is more complex. They understand it even less. They start to feel like they're managing an AI rather than programming with one.

By month six, they're spending more time evaluating AI output than they would have spent just solving the problem. But the ticket count is higher, the velocity dashboard looks great, and nobody — including them — has made the connection between the growing fog and the growing output.

The velocity metric has become a proxy that hides the thing it's supposed to represent.

---

## What the Industry Got Wrong This Time

The framing was wrong from the start.

When AI coding tools became mainstream, the conversation was about productivity. The question everyone asked: "Will this make us faster?"

That's the wrong question.

The right question is: "Faster at what, exactly?"

Faster at producing code that looks right? Yes.

Faster at building understanding that compounds over time? No.

Faster at developing the judgment that tells you which approach is right before you try it? Definitely not.

The productivity gains from AI are real. They're also narrow. They apply to the output side of the equation, not the input side. And in a field where the input — the engineer's thinking, reasoning, judgment — is the actual product, optimizing for output while degrading input is not a productivity win. It's a trade.

The engineers who understand this most clearly are the ones who are now asking a different question before using any AI tool: "Will this make me better at this, or just faster at producing this?"

That question is harder to answer than "should I use AI here?" But it's the only one that leads somewhere useful.

---

## The One Metric Worth Tracking

Here's what I'd suggest if you're the kind of engineer who likes self-experimentation:

Once a month, spend an hour on a problem with zero AI assistance. Not because you're testing yourself. Not because you're proving a point. Because you're calibrating.

Note: Can you still do this? Can you still read this code a month later and understand what you wrote and why? Can you explain the architecture decision to a junior engineer without using the phrase "I asked ChatGPT"? Can you debug this in production at 2 AM without AI assistance?

These aren't moral questions. They're calibration questions. They're the difference between knowing how your system works and knowing that you used AI to build it.

The engineers who are going to be fine in five years aren't necessarily the ones using AI the least. They're the ones who are tracking the right numbers — including the numbers that don't show up in any dashboard.

---

## What I'm Working On

I've been spending more time in what's now called "deep debugging mode" — problems where AI gets disabled entirely for the first 45 minutes.

It's uncomfortable. It forces you to sit with not-knowing in a way that AI use doesn't. The friction is the point. The friction is where the understanding gets built.

I've also started keeping a "what I actually figured out this week" list alongside the "what I shipped this week" list. They're not the same list. They're rarely even correlated.

The shipping list gets shown in standups. The other list is the one that actually tells me whether I'm growing or just producing.

---

## The Question Worth Sitting With

What's your unaided baseline?

Not as a test. Not as proof of anything. Just as a calibration signal — a way to notice whether the gap between what you're shipping and what you understand is widening, narrowing, or holding steady.

If you don't know, the answer might be worth finding.

That's it for this week. See you next Sunday.

— The Clearing

P.S. If you're tracking your own unaided baseline, I'd genuinely love to hear what you're measuring. Reply to this email — I read everything.

---

**Share this dispatch:** Forwarded from a friend? [Subscribe to The Dispatch here](https://clearing-ai.com/newsletter.html). New readers every week.

**Continue reading:**
- [The Science of AI Fatigue](https://clearing-ai.com/the-science-of-ai-fatigue.html) — What's actually happening in your brain when AI tools slow you down
- [AI Fatigue Severity Index](https://clearing-ai.com/ai-fatigue-severity-index.html) — Take the 15-question quiz and get your score
- [The Explanation Requirement](https://clearing-ai.com/the-explanation-requirement.html) — The single practice that keeps learning from disappearing
- [Daily Practice](https://clearing-ai.com/daily-practice.html) — 30 days of small, concrete actions for AI fatigue recovery

---

*You're receiving this because you subscribed to The Dispatch, a weekly letter for software engineers navigating AI tools without losing themselves. Unsubscribe anytime — one click, no guilt, no follow-up emails.*