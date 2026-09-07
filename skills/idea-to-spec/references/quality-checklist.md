# MVP specification quality checklist

Apply this checklist before delivery. Report unresolved material gaps; do not paste the checklist into the specification unless the user asks for an audit trail.

## Intent and evidence

- The summary preserves the user's actual idea and desired outcome.
- Supplied facts, explicit decisions, assumptions, and open questions are distinguishable.
- No users, demand, metrics, deadlines, integrations, policies, or constraints were invented.
- Questions are limited to ambiguities that materially affect implementation; safe defaults are labeled.

## Scope and proportionality

- The MVP is the smallest coherent end-to-end value loop.
- Every in-scope feature is necessary for that loop or for a justified safety or operational need.
- Attractive extras are excluded or moved to future extensions.
- The document's depth matches the product's complexity and risk; unused sections are omitted.
- The specification does not silently turn a utility into a platform or multi-role system.

## Implementability

- The primary journey, inputs, outputs, state, and observable behavior are clear.
- Important validation, empty, failure, retry, cancellation, and recovery behavior is defined.
- Persistent data has an owner, lifecycle, source of truth, and deletion approach where relevant.
- External integrations and side effects identify permissions, confirmation, failure handling, and retry/idempotency needs where relevant.
- AI features define context, output shape, validation, uncertainty or malformed-output handling, and human review where warranted.

## Technology and quality

- No unspecified stack choice is presented as settled.
- Any proposed technology follows from stated constraints and includes its rationale.
- Non-functional targets are testable and evidence-based, or explicitly left to measurement.
- Privacy and security controls are proportional to the data and harm involved.
- Accessibility covers the relevant interaction and output modes without unsupported compliance claims.

## Verification and delivery

- Acceptance criteria are observable, specific, and cover the core happy path.
- High-impact failure or safety paths have acceptance criteria.
- Implementation tasks form ordered, verifiable slices and map to the MVP.
- Out-of-scope items, blocking decisions, and material risks are visible.
- A builder could begin without guessing about the core flow; any remaining guess is explicitly documented.

## Preference hygiene

- Current feedback is reflected in the specification.
- Reusable preferences are recorded only with user authorization.
- Preference records are narrow, contextual, traceable, and include exceptions.
- Conflicting feedback does not silently erase earlier provenance.
