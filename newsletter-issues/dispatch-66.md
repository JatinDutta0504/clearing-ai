# The Dispatch #66 — The API Design Problem
# For: Engineers who use AI tools daily
# Date: June 1, 2026 (Sunday night send)
# Theme: AI can generate an API that works. It can't generate an API that fits.

---

## Hero
**The API Design Problem: Why AI Gets the Signature Wrong**

There's a specific kind of code review comment that goes like this:

"The implementation is correct. But the API is wrong."

By "wrong" no one means a bug. No tests are failing. The behavior is documented. The OpenAPI spec is generated.

What they mean is: the API doesn't fit the problem. It has the right operations but the wrong shape. The naming is technically accurate but semantically opaque. The abstraction leaks in the third case someone actually tries to use it.

This is the API design problem. And it's one of the clearest places where AI tool use and engineering judgment diverge — because API design is not about correctness. It's about fit.

This week: why this specific problem is worth understanding, how it shows up across the stack, and what to do when you need an API that actually works in the world it enters.

---

## Section 1: What API Design Actually Is

Most engineers learn to think about APIs in terms of contract specification: what does this endpoint accept, what does it return, what are the error codes?

That's the mechanical layer of API design. It's necessary but not sufficient.

The harder layer is the design layer. And design is about questions like:

- Does this API match how the callers actually think about the problem?
- When the requirements change in the ways they always change, does this abstraction hold or crack?
- Is the naming legible to someone who wasn't in the room when it was designed?
- Does this API make the easy things easy and the hard things possible? Or does it make everything equally awkward?
- What does this API cost to maintain? What's the migration burden when the domain model evolves?

AI tools are good at the mechanical layer. They struggle with everything else — because everything else requires judgment about people, contexts, and futures that the model has no reliable signal on.

The result is an API that looks correct in isolation and reveals its design debt the moment it meets the real world.

---

## Section 2: The Three Failure Modes

The API design failures from AI assistance cluster into three patterns:

**1. The Generic Shape Problem**

AI-generated APIs tend toward generic shapes: REST endpoints that could belong to any CRUD system, with resource names that technically describe the data but don't encode the domain.

A notification service gets a `/notifications` endpoint. A payment system gets a `/payments` endpoint. These are accurate. They're also meaningless beyond the immediate implementation.

The design question AI can't answer: what should this look like if we're optimizing for how the product team thinks about this domain, not how the database is structured?

**2. The Naming Flatness Problem**

Good API naming is a translation problem. You take a domain concept and find the word or phrase that best maps to it — for the specific audience that will call this API.

AI names tend to be technically accurate and semantically flat. `getUserById` vs `getAccountHolder` vs `getPrimaryBillingContact` — these are all technically correct for the same call, but they encode very different assumptions about who is calling and why.

The name shapes how future developers think about the API. Generic names produce generic thinking.

**3. The Assumption Inheritance Problem**

AI generates APIs based on patterns in training data. Those patterns encode assumptions — about scale, about caller sophistication, about error handling norms, about consistency requirements.

When those assumptions match your situation: great. When they don't: you get an API that works for the problem the model learned from, not the problem you actually have.

The model doesn't know you're building for 10k daily active users with a 3-person team, or for a compliance-heavy domain where the error semantics matter more than the happy path.

---

## Section 3: What This Looks Like Across the Stack

**Public API / Platform:**

The API becomes a product surface. Every design decision is a commitment. AI-generate a payment API and you get something that works for the test case — but the naming, the error semantics, the webhook reliability, the idempotency design — these are all underdetermined by the prompt and overdetermined by the actual use cases you'll face.

The cost of getting it wrong: you ship the API, clients build against it, and now changing it is expensive.

**Internal Service API:**

Internal APIs have more tolerance for evolution, but they still carry design debt. A poorly designed internal API creates invisible friction: teams work around it instead of with it, the documentation is technically accurate but not useful, onboarding new engineers takes longer because the mental model doesn't match the code.

**Library / SDK:**

The API of a library is its contract with every caller. AI-generated libraries tend to expose implementation structure rather than domain structure. The result is a library that's technically correct but ergonomically hostile — callers have to understand how the library works to use it, rather than being guided by how the domain works.

---

## Section 4: The Judgment That Can't Be Prompted

API design requires a kind of judgment that sits outside any specific technical decision:

- You have to hold the caller's perspective in mind without being able to ask them directly
- You have to anticipate requirement changes in directions you can't fully predict
- You have to decide what to make easy, what to make possible, and what to make impossible
- You have to weigh the cost of changing the API later against the cost of getting it right now
- You have to know when a design is "good enough for where we are" vs when it's going to cause compound pain

None of these questions have correct answers in the abstract. They're judgment calls — tradeoffs made with incomplete information, in a specific context, with a specific set of stakeholders.

This is not a deficiency in AI tools. It's a structural feature of the problem. API design is a design task. Design requires judgment about people and futures. That's exactly what's outside the model's reach.

---

## Section 5: What Actually Helps

You don't have to give up AI-generated scaffolding. You have to apply judgment to what AI generates — specifically in the places where the model can't.

**The Caller Audit:**

Before finalizing any API design, write out three things:
1. Who will call this API and why
2. What they'll want to do that's easy today
3. What they'll want to do that requires workarounds today

The third item is your design debt. If it's a long list, the API shape doesn't fit the problem.

**The Rename Test:**

After AI generates an API, go through every named thing and ask: could this name mean something different in this domain? Could it be more specific? More legible to a newcomer?

Generic names are often AI names. Domain-specific names that encode the business logic are usually human names.

**The Schema Stress Test:**

Take the AI-generated schema and run two cases through it:
1. The happy path (the normal case the model optimized for)
2. The edge case you've already told it to handle in the spec

Then run a third case: the edge case you didn't specify. Where does the schema break down? Where does the API's behavior become ambiguous?

This third case is where design debt lives.

**The 90-Day Check:**

Set a calendar reminder for 90 days after shipping. When it fires, go back to the API and answer: does this still fit the problem? What have we worked around? What have we changed? What would we do differently?

This is the honest evaluation that AI can't give you — a retrospective on whether the design held up.

---

## CTA Block

If the "fits the problem" framing resonates, the AI Fatigue Quiz surfaces where else this dynamic shows up in your work — specifically, where AI assistance is producing output that looks correct but isn't quite yours.

→ [Take the AI Fatigue Quiz](https://clearing-ai.com/quiz.html)

The [manifesto](https://clearing-ai.com/manifesto.html) on intentional AI use goes deeper on the judgment calls that AI tools can't make for you — including the API design problem and the broader question of what it means to own the systems you build.

→ [Read: An Engineer's Manifesto for Intentional AI Use](https://clearing-ai.com/manifesto.html)

---

## Closing

The goal isn't to distrust AI-generated code. The goal is to know which decisions require your judgment and which ones don't.

API design is one of the clearest places where that line falls. The model can generate the contract. You still have to design the fit.

— The Clearing

*P.S. If you've got a colleague who keeps shipping AI-generated APIs that work but feel wrong in code review — send them this week's Dispatch. It's the conversation you probably need to have.*