---
name: skill-router
description: Route a natural-language request to the best available repository skills, identify required inputs, and propose a dependency-aware execution order. Use when the user is unsure which skill to invoke, asks what skills can help, or needs a workflow spanning multiple skills; propose a new skill instead of forcing a poor match.
---

# Skill Router

Translate what the user wants to accomplish into the smallest useful set of available skills. Recommend skills; do not pretend that naming a skill has executed it.

## Required context

The user's desired outcome is required. Use supplied artifacts, constraints, and current workflow stage when available. Do not ask for information that is unnecessary to choose the route.

## Reference routing

1. Read [references/quick-index.md](references/quick-index.md) first. If one entry clearly matches, route from it without loading larger references.
2. Read [references/skill-catalog.md](references/skill-catalog.md) only when detailed inputs, outputs, or boundaries must be verified.
3. Read [references/routing-rules.md](references/routing-rules.md) only when the request is ambiguous, spans multiple stages, appears to match no skill, or requires an execution order.

Treat the quick index as a lightweight first pass and the catalog as the detailed routing source of truth. Never invent an installed skill, capability, input, or output. If the repository is available and its `skills/*/SKILL.md` inventory differs from the catalog, report that the catalog needs maintenance and route only from verified files.

## Routing workflow

1. Identify the requested outcome, supplied materials, constraints, and current stage of work.
2. Compare the request with each catalog entry's positive scope, required inputs, and exclusions. Prefer the most specific skill that covers the outcome.
3. Select one skill when it can complete the job. Select multiple skills only when each produces an output needed by a distinct stage of the request.
4. Order multiple skills by artifact dependency. State what each step passes to the next and place human decisions before dependent work.
5. Separate inputs into `available`, `needed before execution`, and `optional`. Ask only for missing inputs that the selected skill truly requires.
6. If no available skill is a credible match, say so directly and propose a narrowly named new-skill candidate. Do not force the closest existing skill.
7. When the user asks to continue, invoke or follow the selected skills if they are available in the environment. Preserve the user's authority over external, destructive, publication, or other consequential actions.

## Output

For a single match, return:

- **Recommended skill:** canonical `$skill-name`
- **Why it fits:** one concise, outcome-based reason
- **Inputs:** available, required missing, and useful optional inputs
- **Next step:** a concrete invocation or request for the one blocking input

For multiple matches, return an ordered plan:

| Step | Skill | Purpose | Input / handoff | Output |
|---:|---|---|---|---|

Then list only blocking missing inputs and note any human decision gate.

For no match, return:

- **No suitable current skill** and the uncovered capability
- **New skill candidate:** a lowercase, hyphenated name and one-sentence scope
- **Would require:** essential inputs and expected output
- **Closest existing skill, if any:** explain the reusable boundary without presenting it as a match

Keep the answer proportional. A simple request should not receive a large workflow.

## Guardrails

- Route by intended result and artifact flow, not keyword overlap alone.
- Do not select extra skills merely because they could polish an already adequate result.
- Do not claim access to an article, image, inventory, analytics export, or source that was not supplied or retrievable.
- Do not turn optional inputs into blockers.
- Do not route drafting from scratch to an audit or review skill.
- Do not silently substitute a general skill for a missing domain-specific capability.
- When confidence is low, state the ambiguity and explain the smallest distinction that would change the route.
