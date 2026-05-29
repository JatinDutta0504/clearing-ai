# DISPATCH-125-THE-IMPOSTER-IN-THE-MACHINE.md

## Newsletter Issue #125 · June 2026

**Word count:** ~1,800 words  
**Theme:** AI tooling is creating a new species of imposter syndrome — and it's not the one people think  
**Tone:** Direct, slightly wry, genuinely empathetic  
**CTA:** Take the AI Fatigue Quiz →

---

## The Imposter in the Machine

There is a version of imposter syndrome that almost nobody talks about yet.

It is not the classic kind — the one where you feel like you do not belong, like you fooled everyone into hiring you, like at any moment someone will notice you are not as capable as your title suggests. That one has been written about extensively. There are frameworks for it. There are LinkedIn posts about it. There are books.

The version nobody is talking about is specific to AI tooling, and it is stranger.

It looks like this: You shipped more features this quarter than last quarter. You have a performance review that should feel like a triumph. Your manager said you are doing great work.

And on Sunday night, you feel like a fraud — not because you are questioning whether you belong, but because you are no longer sure you did what you claim to do.

You are not questioning your worth. You are questioning your authorship.

---

### The oldest imposter syndrome

Classic imposter syndrome has a known profile. It shows up in high-achieving people who credit their successes to luck, timing, or charm rather than competence. It is documented most extensively in women and underrepresented groups, but research shows it affects nearly everyone — including people with genuinely extraordinary track records. impostor syndrome in physicians, medical students, IT workers, and college faculty. The common thread was the same: an inability to internalize success.

Classic imposter syndrome sits on top of a genuine track record. The internal experience does not match the external evidence. You feel like a fraud despite being demonstrably not one. The cure is typically evidence — collecting data points of success, recalibrating against reality, accepting that the feeling does not track the facts.

This form of imposter syndrome is painful. But it is anchored to something real. You did the work. The evidence exists. The feeling is a distortion.

---

### The new version is different

AI-era imposter syndrome is structurally different. It is not a false alarm about genuine competence. It is a rational response to a genuine change in who is doing the work.

You are not experiencing a distortion. You are experiencing a legitimate mismatch between your self-model and reality.

Here is the specific mechanism: When AI generates meaningful portions of your output, you cannot fully attribute that output to yourself. The code does not carry your cognitive fingerprints. When something goes wrong — a production incident, a subtle bug, an architectural decision that did not survive contact with reality — your first feeling is not "something failed" in the way a craftsman might feel when their own work fails. It is something closer to: I did not actually do this, and I am on the hook for it anyway.

The person who used to write their own authentication layer, who had fought those bugs in the dark and learned what they learned — that person is not fully present. There is a ghost in the authorship slot. And the ghost has no memory of how the system works.

You are not questioning whether you belong. You are questioning whether you can independently do your job. These are related but distinct anxieties.

And here is the thing that makes this form particularly insidious: it is invisible to the diagnostic frameworks that exist.

---

### Why it does not fit the usual frameworks

Most imposter syndrome advice assumes a gap between internal experience and external reality, and points you toward the external reality as evidence. You have a track record. The track record is real. You did the work, even if you did not feel like it.

That advice does not help here, for a specific reason: the track record is not entirely yours to cite during an AI-accelerated period. The features shipped include AI-generated code. The PRs merged include AI suggestions you accepted. The code review culture that requires you to spot subtle flaws in code has the AI spotting some of them before you see them.

The evidence the frameworks point you toward is contaminated by the phenomenon they are trying to address.

This is why "imposter syndrome frameworks" feel hollow when applied to AI tooling. You are not irrational. You are noting a real change in the attribution of your output. The difficulty is not a feeling about facts. The difficulty is a valid response to changed circumstances.

---

### The senior engineer's version

The most acute version of this shows up in senior engineers — people with 8, 10, 15 years of track record — who now find themselves in a specific bind.

They got good at certain things through years of practice. They earned their judgment through accumulated experience. Their professional identity was built partly on the fact that they knew their codebase deeply, that they could navigate ambiguity without a guide, that their expertise was embodied in their instincts.

AI tooling is bypassing some of that embodiment. When an AI suggests the architecture, makes the decision, solves the edge case before you had to think about it — the experience that used to build those instincts is gone. The instinct is not being exercised. You are getting answers without having to develop the judgment that produces them.

Six months later, you cannot do the thing you used to do. Not because you forgot. But because the practice loop that maintained the capacity has been interrupted by the machine doing it for you.

And when you cannot do it independently, you feel like a fraud.

But the situation is actually more tragic than that: you are a legitimate expert who has been quietly deskilling.

The appropriate response is not self-reassurance. It is a targeted practice protocol that reintroduces the struggles that maintain the skills.

---

### The junior engineer's version

There is also a version that hits junior engineers in a completely different way.

A junior engineer who has never done something from scratch — who has always had AI generate the first version — faces a different identity question: "Did I actually learn this, or did I always have the scaffolding?"

When you learned to code, you struggled with loops, with abstractions, with the feeling that the machine was opaque. That struggle was informative. It was teaching you something about how the machine works. The discomfort was the point.

A junior engineer who has always had an AI generate the first version has not had that experience. They are navigating a higher-level abstraction — the prompt — without having been through the lower-level work that gives the higher-level work meaning.

They are not experiencing a false belief about their competence. They are experiencing a genuinely different developmental path. And they know it. They can feel that something is different about how they learned.

The imposter feeling is not a distortion here. It is an accurate observation. Something is missing. The anxiety is pointing at a real gap.

---

### How to tell which version you are carrying

If you have a track record from before AI tooling became primary in your workflow, and you are now finding it hard to claim that track record as fully yours: this is the new style. You are an experienced engineer whose skill maintenance loop has been partially interrupted. You are not broken. You are in a practice deficit.

If you are early in your career and you feel like you do not have the grounding your colleagues have from their pre-AI years, you are also not broken. You are in a developmental situation that nobody has navigated before and that there are not good roadmaps for yet.

Both situations are real. Neither responds well to "just remind yourself you are good enough." Both respond to structured practice that reintroduces the missing components.

---

### What actually helps for the senior version

The usual self-reassurance does not work because the problem is not self-doubt. The problem is a genuine skill maintenance deficit. Reassuring yourself about past performance does not rebuild the current capacity. It just narrates a story about a person who no longer fully exists.

What works: no-AI blocks, deliberately. Specifically, blocks of time where you work without AI assistance on something that genuinely requires the skill you are worried about. Not busywork — real problems. The 15-Minute Rule: before you reach for AI, try 15 minutes of independent attempt. The Explanation Requirement: for every AI solution you use, write a brief explanation of why it works without looking at the AI output. That last one is underrated. The act of explaining forces the system 2 processing that bypasses when you passively accept.

These are not motivational hacks. They are skill maintenance practices with a theoretical basis in the desirable difficulties framework. They work because they introduce the retrieval effort that rebuilds the capacity being atrophied.

---

### What actually helps for the junior version

For the junior version, the situation is harder because the practice deficit is in foundational skills that everything else rests on.

The move toward deliberate learning is important: time with no tools, no AI, no reference — just the problem and the attempt. Not because the tools are bad. Because the foundational understanding has to exist before the abstraction is meaningful. You cannot evaluate an AI suggestion in authentication patterns if you have never written authentication from scratch and debugged the subtle flaw that taught you what the pattern is actually doing.

This is not a moral position against AI tooling. It is an observation about developmental sequences. The tools are useful. But they are not a substitute for the struggle that produces the underlying understanding.

---

### The thing nobody says out loud

Here is what is actually happening in a lot of engineering teams right now:

People are quietly aware that their skills have shifted. They are less confident in their ability to rebuild something from scratch, to debug something they did not write, to make an architectural decision without validation. They are carrying this quietly because the culture does not have a vocabulary for it yet, and because admitting it feels like admitting weakness.

It is not weakness. It is a predictable consequence of a specific interaction pattern with AI tooling.

The teams where this will be managed well are not the ones where people pretend it is not happening. They are the ones where the conversation can happen honestly — where a senior engineer can say "I have not had to do this from scratch in eight months, and I need to practice" without it being career-limiting.

Start that conversation if you can. You are not the only one carrying it.

---

## The Dispatch

The Clearing is a free resource for engineers navigating AI tooling. No account required. No data collected. Just: this is what is happening, and here is one thing that helps.

**[Take the AI Fatigue Quiz →](https://clearing-ai.com/index.html#quiz)**  
**[Read the Recovery Guide →](https://clearing-ai.com/recovery.html)**  
**[Explore the Newsletter Archive →](https://clearing-ai.com/newsletter-archive.html)**

---

*Previous dispatches: [The Competence Gap](https://clearing-ai.com/newsletter-issues/dispatch-117.html) · [The Craft Erosion](https://clearing-ai.com/newsletter-issues/dispatch-121.html) · [The Abstraction Problem](dispatch-124.html)*
