---
name: idea-to-spec
description: Turn rough product ideas, short notes, or “wouldn't it be useful if…” concepts into implementation-ready MVP specifications. Use for web tools, local utilities, AI tools, and small apps when the product shape is still vague; not for implementing an already-defined specification.
---

# Idea to Spec

Convert the user's idea into the smallest specification that a builder can implement and a stakeholder can verify. Preserve the idea's intent, distinguish facts from assumptions, and scale the document to the product's actual complexity.

## Reference routing

- Read [references/spec-template.md](references/spec-template.md) when producing the specification. Select only sections that improve implementation or review; do not emit empty or ceremonial sections.
- Read [references/design-principles.md](references/design-principles.md) when making product or scope decisions, and whenever the user supplies feedback or established preferences.
- Before delivery, apply [references/quality-checklist.md](references/quality-checklist.md).

## Workflow

1. Restate the idea in one or two sentences and identify the intended outcome rather than merely repeating the proposed feature.
2. Separate supplied facts, constraints, and decisions from assumptions. Note consequential unknowns.
3. Ask a question only when different answers would materially change the MVP's users, core workflow, architecture, risk, or acceptance criteria and no safe default is available. Ask the fewest questions needed. Otherwise proceed and label the assumption.
4. Choose the lightest useful specification depth: compact for a single-purpose utility, standard for a small product, and expanded only for multi-user, sensitive, integrated, or operationally complex products.
5. Define one coherent primary user journey and the smallest end-to-end slice that delivers value. Resolve contradictions by preserving explicit user constraints and surfacing the tradeoff.
6. Describe behavior, inputs, outputs, state, failure handling, and acceptance criteria precisely enough to implement and test. Use IDs for requirements or criteria only when traceability would help.
7. Recommend technologies only when the user requests a recommendation or when a constraint makes a choice consequential. Express unconfirmed choices as options or decision criteria, not settled facts.
8. Break implementation into ordered, outcome-based tasks that map back to the MVP. Keep research spikes or decisions separate from build tasks.
9. Run the quality checklist and return the specification with assumptions, open questions, and exclusions visible.

## Non-negotiable guardrails

- Do not overdesign a simple tool. Omit architecture layers, roles, integrations, persistence, analytics, deployment machinery, or formal requirement catalogs unless they serve a demonstrated need.
- Do not silently expand the idea into a platform. Prefer one user, one main job, and one complete workflow for the MVP when that satisfies the request.
- Do not invent research findings, user demand, business metrics, legal obligations, APIs, budgets, deadlines, or existing infrastructure.
- Do not fix an unspecified language, framework, database, model, hosting provider, or cloud platform without evidence. If implementation can remain stack-neutral, keep it stack-neutral.
- Do not disguise ambiguity as certainty. Label assumptions and unresolved decisions, and describe their impact when material.
- Do not confuse “possible later” with MVP scope. Put optional extensions outside the MVP and do not include their groundwork unless it is cheap and clearly justified.
- Do not omit privacy, security, accessibility, or failure behavior when the product handles sensitive data, accounts, external actions, AI output, payments, or essential user workflows. Keep these sections proportional elsewhere.
- AI behavior must specify what the model receives, what it returns, how uncertainty or malformed output is handled, and where human review is required. Do not promise deterministic accuracy from a probabilistic system.
- Treat destructive operations and external side effects as explicit, confirmable actions. Define preview, confirmation, idempotency, recovery, or audit behavior in proportion to risk.

## Feedback and evolving preferences

Apply feedback immediately to the current specification. Treat a correction as context-specific unless the user explicitly identifies it as a reusable preference or asks to record it.

When maintaining preferences, use the record format in `references/design-principles.md`: capture the principle, scope, rationale, provenance, examples, exceptions, and status. Keep stable preferences separate from project facts and one-off decisions. Never overwrite a prior preference silently when new feedback conflicts with it; surface the conflict and narrow or supersede the record.

## Output

Lead with a concise product summary and the proposed MVP boundary. Then use the relevant sections from the specification template. For a very small tool, a short specification with assumptions, core flow, requirements, acceptance criteria, and tasks is sufficient. For a consequential unresolved decision, end with a small decision block explaining what must be chosen and why.
