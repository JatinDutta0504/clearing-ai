---
title: "The Attribution Problem"
number: 47
date: 2026-05-11
description: "When code you shipped that you didn't write becomes the thing you're most known for — the quiet identity crisis behind AI-assisted engineering."
---

# The Attribution Problem

*A letter about what happens to your sense of authorship when the machine starts taking credit.*

---

There's a moment every engineer working with AI eventually hits.

You're in a meeting. Someone asks how a feature got built. You have the answer — you know it was you, the architecture, the decision to build it this way versus that way — but the person asking isn't asking about that. They're asking about the code. And the code, the actual implementation, you didn't write.

You approved. You guided. You reviewed. You made the calls when the AI got stuck. But the artifact they want to see? That came from a tab.

This is the attribution problem. And it's more corrosive than it sounds.

---

## The Version of You That Shows Up

When you ship a feature the traditional way, the story of who you are as an engineer is legible. The commits tell it. The PRs tell it. The code review comments, the tests you wrote, the edge cases you caught — these are all artifacts of a specific mind at work.

When you ship with heavy AI assistance, those artifacts become ambiguous. The commits show your name. But they also show code you didn't conceive, решения you didn't evaluate from scratch, implementations you accepted on first read.

Your sense of "I built this" has a gap in it. Not a gap in the work — a gap in the felt experience of the work.

And over time, that gap gets lonely.

---

## Why It's Harder for Senior Engineers

Junior engineers navigating this are dealing with skill development. Senior engineers are dealing with something older: identity.

You've spent years building a professional self around the ability to understand systems deeply. When that understanding gets outsourced — not because you're lazy, but because the tool is right there and the pressure to ship is real — something erodes that isn't about competence.

It's about whether you feel like you.

One engineer told us: "I used to be able to look at a pull request I wrote two years ago and immediately feel where the pain points were. I could remember what I was thinking. Now when I look back at AI-assisted PRs, there's just... nothing. I don't recognize myself in the work."

That's the sentence worth sitting with.

---

## The Quiet Compounding

The attribution problem compounds silently.

You start to feel a slight distance from your own work. You stop talking about features in the first person — "we shipped X" becomes safer than "I built X." You become less confident in your own code judgment, not because your judgment has actually declined, but because you've stopped practicing it out loud.

Eventually, you notice that when someone asks a deep question about the system, you feel a flicker of anxiety. Not because you don't know the answer, but because you're not sure the answer you know is actually yours.

The erosion isn't dramatic. It's gradual. And you don't notice it until you realize you've stopped saying "I built this" altogether.

---

## What Most Advice Gets Wrong

The standard responses to this are all slightly off-target:

"Use AI as a pair programmer, not an author." — This assumes the problem is how much you use AI. But the attribution problem exists at low usage levels too.

"Make sure you understand every line AI generates." — Correct in principle, exhausting in practice. You can understand every line and still not feel authorship.

"Attribution doesn't matter as long as the work gets done." — This is true economically and false psychologically. Engineers are not pure economic actors. The felt experience of making things is part of why most of us chose this work.

---

## What Actually Helps

**Name it first.** The attribution problem is not imaginary. It's real. Calling it by name — to yourself and to your team — removes the shame layer. You didn't stop being an engineer. You're navigating a genuinely new situation.

**Keep a decision log.** Not a journal, not a diary. Just a plain text file where you capture the calls you made each week: "Chose to use a B-tree here instead of a hash map because X." "Rejected AI's suggestion because it would have introduced a circular dependency." These are the traces of your judgment that AI didn't make. They add up.

**Build one small thing without AI once a month.** Not for any reason except to remember what it's like to solve something that was hard for you. The felt experience of difficulty, when it ends in solution, is where ownership lives.

**Separate "shipping" from "understanding."** You can ship more and understand less. That can be fine economically. It doesn't have to be fine psychologically. Acknowledge both realities without forcing them into the same conversation.

---

## One Question to Sit With

Before your next AI-assisted review, ask yourself: do I know why this decision was made?

Not "do I agree with it" — you can agree with AI output without understanding why it's right. Ask: do I know the reasoning? If the answer is no, that's not a failure. It's a gap. And gaps can be closed.

The engineers who stay sharp aren't the ones who refuse AI. They're the ones who notice when they've outsourced their understanding — and who have a way back.

---

## From the Community

*"My biggest fear isn't that AI will replace my job. It's that I'll forget what I actually know how to do. And one day someone will ask me a question and I'll have to answer from memory instead of understanding."*

— Staff engineer, 9 years, fintech

If this landed, [take the 5-minute fatigue quiz](https://clearing-ai.com/quiz.html). You'll get a real read on where you stand — not a performance assessment, a calibration.

---

## This Week's Recommended Read

[developer-identity.html](https://clearing-ai.com/developer-identity.html) — Who Am I Without My Code? The Identity Crisis at the Heart of Senior Engineer AI Fatigue. For anyone who's been in the game long enough to notice when something shifts.

---

## One Thing You Can Do Today

Open a text file. Write down three decisions you made this week that weren't obvious — why you chose one approach over another, what tradeoffs you weighed. You don't have to share it. You just have to have the trace of your own thinking.

See you next week.

— Sunny
*clearing-ai.com*
