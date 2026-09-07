# MVP specification template

Use this as a menu, not a mandatory form. Include a section only when it changes implementation, validation, risk, or scope. Merge sections for compact specifications. Replace instructional prompts with actual content.

## Specification header

- **Working title:** A descriptive temporary name; do not imply branding is settled.
- **Status:** Draft, decision needed, or ready for implementation.
- **Source idea:** The user's original idea, faithfully condensed.
- **Specification depth:** Compact, standard, or expanded, with a short reason when useful.

## Product summary

State what will be built, for whom, the result it produces, and the proposed MVP boundary in a short paragraph.

## Problem and objective

Describe the user problem or opportunity, the desired outcome, and why the proposed tool helps. Do not invent market evidence. If success is measurable, define a practical signal; otherwise describe observable success qualitatively.

## Target users

Identify primary users and the relevant context, capability, or constraint. Add secondary users, administrators, or roles only when their needs affect the MVP.

## Assumptions, constraints, and open questions

Keep these distinct:

- **Known:** Explicit facts and decisions supplied by the user or verified sources.
- **Assumed:** Defaults used to keep the specification moving, each with its impact if wrong.
- **Open:** Unresolved decisions. Mark as `blocking` only when implementation cannot responsibly start without an answer; otherwise give a recommended default.

## Primary use cases and flow

Describe the few end-to-end jobs the MVP must support. For each, state the trigger, main steps, and successful outcome. Include alternate or failure paths only when useful.

## MVP scope

Define the smallest coherent release:

- In scope
- MVP completion boundary
- Dependencies or prerequisites

Avoid listing implementation conveniences as user-facing scope.

## Functional requirements

State observable system behavior. Use identifiers such as `FR-1` only if they help trace acceptance criteria or implementation tasks. For each requirement, include the trigger, behavior, and result; add permissions, validation, or side effects where relevant.

Prefer “When X, the system does Y and shows Z” over vague labels such as “support uploads.”

## Screens and UI

Describe only the interfaces the product needs. For each screen, view, command, or surface, include its purpose, key elements, main actions, and important states: initial, loading, empty, success, validation error, and failure as applicable. A local command-line tool may need interaction text rather than screens.

## Inputs and outputs

Specify accepted inputs, required and optional fields, limits, validation, and representative formats. Specify outputs, destination, structure, and what constitutes a valid result. Include examples when they remove ambiguity, not as invented data.

For AI features, also define:

- Context and instructions sent to the model
- Expected output shape
- Validation or parsing
- Handling of uncertainty, refusal, malformed output, and retries
- Human review or confirmation before consequential use

## Data and persistence

Include only when state must survive a session. Define the minimum entities or records, ownership, lifecycle, retention, deletion, export, and source of truth. State “no persistent storage” when that is a meaningful privacy or architecture decision.

## Technical requirements and decisions

Record user-supplied constraints first: target environment, integrations, offline needs, supported platforms, deployment, or compatibility. Then state capability needs and decision criteria.

If no stack is selected, use one of these forms:

- **Stack-neutral:** Describe required capabilities and interfaces only.
- **Options:** Compare a small number of viable choices against actual constraints.
- **Recommendation:** Choose one with a stated rationale and label it as proposed, not mandated.

Do not add a database, backend, authentication, queue, vector store, or cloud service without a requirement that calls for it.

## Non-functional requirements

Include testable targets only where justified: responsiveness, throughput, reliability, availability, offline behavior, compatibility, observability, maintainability, cost ceiling, localization, or supportability. Use `to be measured` rather than invented thresholds when a target needs evidence.

## Errors and edge cases

Prioritize likely or damaging cases: missing or invalid input, duplicates, partial completion, timeouts, network loss, external-service failure, concurrency, cancellation, retries, oversized data, unsupported formats, and recovery. Define what the user sees and whether work can be retried or restored.

## Privacy and security

Match controls to the data and actions involved. Cover data minimization, access, secrets, sensitive-content handling, external transmission, retention, deletion, logging, consent, confirmation for side effects, and abuse prevention as applicable. Flag legal or policy questions for qualified review instead of inventing requirements.

## Accessibility

For user interfaces, cover keyboard operation, focus, labels, contrast, non-color cues, error identification, text scaling, reduced motion, and screen-reader semantics as applicable. For audio, image, or document output, identify equivalent alternatives. Do not claim compliance without verification.

## Explicitly out of scope

List attractive but unnecessary capabilities that are intentionally excluded from the MVP. Include the reason when exclusion prevents likely scope creep or clarifies a tradeoff.

## Future extensions

List plausible follow-ons only when useful. Keep them independent of MVP acceptance and do not pre-build speculative architecture solely for them.

## Acceptance criteria

Write testable, user-observable conditions. Cover the happy path and the few failure or safety paths needed for release confidence. When requirement IDs are used, map each criterion to them. Avoid criteria that merely assert “works,” “is intuitive,” or name an internal implementation.

Example form:

> Given a valid input file, when the user starts conversion, then the tool produces the documented output format and reports the saved location.

## Implementation tasks

Order thin, verifiable slices rather than isolated technical layers. A useful sequence is:

1. Resolve blocking decisions or validate risky assumptions.
2. Build the narrow happy path end to end.
3. Add validation and important failure handling.
4. Add persistence, integrations, or safety controls that are in scope.
5. Verify acceptance criteria and package the MVP for its intended environment.

For each task, name the outcome and the acceptance criteria or requirement it advances. Avoid estimates unless the user asks and enough delivery context exists.

## Decision log

Use for material choices only:

| Decision | Status | Rationale | Consequence / revisit trigger |
|---|---|---|---|
| Example choice | Proposed | Constraint it satisfies | Evidence or event that would change it |

## Compact specification shape

For a single-purpose utility, prefer this reduced shape:

1. Summary and assumptions
2. Core user flow
3. In scope / out of scope
4. Functional behavior, inputs, and outputs
5. Essential errors, safety, and accessibility considerations
6. Acceptance criteria
7. Implementation tasks
