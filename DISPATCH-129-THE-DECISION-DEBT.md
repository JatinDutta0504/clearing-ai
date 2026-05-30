# DISPATCH-129-THE-DECISION-DEBT.md

## Newsletter Issue #129 · June 2026

**Word count:** ~1,800 words  
**Theme:** AI tools absorb the small decisions that engineers used to make — and the cumulative cost of that missing decision load is quietly restructuring how judgment forms  
**Tone:** Direct, slightly wry, genuinely empathetic  
**CTA:** Take the AI Fatigue Quiz →

---

## The Decision Debt

There is a category of cognitive work that nobody tracks.

It is not the big architectural decisions — those still get made, debated, documented. It is not the sprint planning decisions or the roadmap prioritization. Those are visible. They show up in tickets, in architecture documents, in the meeting notes your team actually keeps.

It is the small decisions. The micro-decisions. The ones that happen every few minutes while you are building something: this variable name versus that one, this approach versus that one, the dozens of tiny tradeoffs that add up to a piece of software having a particular character.

AI tools absorb most of those decisions automatically. And the absorption is mostly invisible — until you notice that your judgment has quietly atrophied in exactly the places where you stopped making the calls.

This is decision debt. And it is one of the least-discussed mechanisms of AI fatigue.

---

### What decision debt looks like

Decision debt accumulates when you stop making the small decisions that used to build up into judgment.

It shows up in unexpected places:

**Naming.** When you ask AI to generate a function, it names the function. When you generate a class, it names the class. The naming decisions — which carry more meaning than most engineers realize — get made by the tool. Over months, you have a codebase full of names that do not quite reflect how you think about the problem. The naming judgment, the thing that says "this name captures the intent better than that one," does not get practiced.

**Structure.** Where does this logic live? Should this be a separate module or part of the existing one? Should this be a utility function or a method on the class? These structural micro-decisions are a major part of what software design intuition feels like. When AI generates the structure, you stop making them. The intuition does not get updated.

**Tradeoffs.** This approach is faster to implement but harder to maintain. That approach is more generic but adds complexity. The hundreds of small tradeoff decisions that happen in a day of coding are, in many ways, the substance of engineering judgment. When AI chooses the tradeoff for you — usually optimizing for implementation speed — those decisions do not get made. And the judgment about tradeoffs does not get updated.

**Error handling.** How should this function behave when the input is unexpected? What edge cases should be considered? The error handling decisions are where engineering experience lives in the most concrete form. When AI generates the happy path and you only add error handling when prompted, the error-handling judgment stays where it was.

Each of these is small. None of them feels consequential in isolation. But they compound — and after months of AI-assisted development, the compound is a specific gap: you can evaluate the outputs AI produces, but you are less able to produce the inputs that AI would have needed.

The judgment that used to be automatic is now effortful. And effortful judgment is slower, which means you reach for AI more, which means you make fewer decisions, which means the judgment atrophies further.

---

### Why the small decisions matter more than they seem

Here is the thing about micro-decisions: they are not just about the specific choice in the specific moment.

They are about the trained perception that forms when you make them consistently over time.

A senior engineer does not have better memory or better logic. They have a trained perception for software structure — a sense of where things should live, how modules should interact, what makes a system legible versus clever. That trained perception formed through thousands of small decisions: this approach versus that one, this name versus that one, this structure versus that one.

When you stop making those decisions, the trained perception stops updating. Not because you are lazy or because the tool is bad — because the tool is doing the thing that used to do the updating.

This is why AI fatigue is different from normal skill decay. In normal skill decay, you stop practicing and the skill fades. In decision debt, you are still practicing — you are still writing code, still shipping features, still doing the work. But the practice is in the wrong mode: you are evaluating AI outputs rather than making original decisions. The skill that forms is the skill of evaluation, not the skill of creation.

And the problem is that the evaluation skill does not substitute for the creation skill. You can become very good at judging whether AI's code is right. That does not mean you can write the code yourself — or at least, not as fluently, not as confidently, not with the same sense of whether it is right.

---

### The debt compound

Decision debt compounds in a specific direction: it makes you more dependent on AI for decisions, which means you make fewer decisions yourself, which means the judgment atrophies further, which means you need AI more.

The mechanism is self-reinforcing, and it is not a character flaw. It is a structural property of the tool.

AI tools are designed to produce. They are optimized to give you a good answer fast. They are not designed to help you think through a tradeoff — they are designed to resolve the tradeoff for you. And when a tool resolves your tradeoff for you, the resolution does not deposit the judgment in you. It deposits the judgment in the tool.

This is the specific cognitive transaction that is happening, hundreds of times a day, in every AI-assisted engineering session: you are outsourcing the micro-decisions, and in exchange you are getting speed. The speed is real. The judgment debt is also real.

The question is not whether the trade is worth it. The question is whether you are accounting for both sides of the ledger.

---

### The three registers of decision debt

**You do not notice the decisions you stopped making.** This is the most insidious part. The decisions that AI absorbed are not visible to you — they are the ones that did not happen. You do not have a moment where you thought "I should make this tradeoff and I am not going to." You just... prompted. And the decision got made. By someone. Something.

**The outputs look like yours.** The code in your codebase is code you shipped. Your name is on the commit. Your team lead reviewed it. It looks like your work. But the small decisions that give software its character — the naming, the structure, the tradeoff choices — were made by AI. The outputs look like your judgment. The judgment inside you did not update.

**The gap only shows up when you need it.** Decision debt is invisible until you need the judgment it failed to build. Until you are in a situation where AI is unavailable, or where AI is producing wrong output, or where you need to make a decision fast without AI. Then the gap is suddenly very present. And by then, the debt has been accumulating for months.

---

### What the debt costs you

Decision debt has a specific cost that most people do not talk about: it makes you less useful in proportion to how productive you appear.

This sounds counterintuitive but it is not. The most valuable thing a senior engineer provides is not code — it is judgment. The ability to look at a problem and know which approach is right, which tradeoff is worth making, which direction will cause problems at scale. That judgment forms through the micro-decisions. When the micro-decisions stop, the judgment stops forming.

After18 months of heavy AI-assisted development, many engineers report this specific experience: they can work faster, ship more, produce better-looking code. And they are less confident in their ability to make architectural decisions without AI. Less confident in their design intuition. Less confident in the thing that used to be their core professional identity.

The productivity went up. The judgment stayed flat or declined. And the gap between them is the decision debt.

---

### The decision re-deposit protocol

Here is what actually helps:

**The 20-decisions-a-day practice.** Designate 20 micro-decisions per day that you will make without AI — not because AI would do them worse, but because the making of them is the point. Naming, structure, tradeoff choices, error handling. Write them down: this name because, this structure because, this tradeoff because. The writing is not the point — the articulating is. Articulating why you chose one thing over another is the practice that builds the judgment.

**The explain-the-alternative protocol.** When you ask AI to generate something, before you accept it, write down what you rejected and why. Not for the AI — for you. This is the highest-leverage decision practice you can do while still using AI. The decision debt accumulates in the rejections you did not consider. Write them down.

**The weekly judgment audit.** Once a week, pick one decision you made that week — one real architectural or design decision, not a micro one — and write out: the decision, the alternatives you considered, why you chose what you chose, what you would do differently. This is the maintenance practice for the judgment muscle. Without it, the debt accumulates silently.

**The no-AI design session.** Once a month, design something — a feature, a module, an interface — without AI. Not to produce production code. To practice the decision-making that design requires. The goal is not the output. The goal is the decisions.

---

### The thing nobody says

Here is the thing nobody says about decision debt: it is not the price of using AI. It is the price of using AI without accounting for what you are giving up.

The tool is not the problem. The output is real. The productivity is real.

But if you are not deliberately making the decisions that the tool is not making for you, the judgment is quietly not building. And the gap between what you can produce and what you understand is the debt.

Pay attention to the decisions you are not making. That is where the judgment lives — and that is where the debt is accumulating.

— The Clearing 🌿

---

*Previously in The Dispatch: ["The Handoff Gap" — AI creates a handoff gap where engineers lose the traceable lineage of their own decisions](https://clearing-ai.com/dispatch-128.html)*

*Forwarded this? [Subscribe for The Dispatch every Thursday](https://clearing-ai.com/newsletter.html)*
