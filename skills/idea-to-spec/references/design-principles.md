# Product design principles and preference records

Use these defaults when the user has not supplied a conflicting preference. They guide judgment; they are not mandatory sections in the output.

## Default principles

### Start with the job, not the feature

Identify the result the user wants and the situation in which they want it. A suggested feature may be one solution, not the requirement itself. Preserve an explicitly requested feature while noting a simpler route when it materially changes cost or scope.

### Build the smallest complete loop

An MVP must let the primary user reach a useful outcome end to end. Prefer a narrow complete flow over many partial features. “Smallest” does not mean omitting the validation, recovery, privacy, or accessibility needed to make that flow responsibly usable.

### Make scope proportional

Use compact depth for deterministic, single-user, single-purpose tools with little persistent state. Expand the specification when it includes multiple roles, sensitive data, destructive or financial actions, regulated use, unreliable integrations, collaboration, substantial persistent state, or AI decisions with meaningful consequences.

### Prefer reversible decisions

Delay choices that are cheap to change and resolve choices that would reshape the core flow or data model. Do not introduce abstraction merely to preserve hypothetical options.

### Keep technology subordinate to constraints

Translate the need into capabilities before selecting products or frameworks. Relevant criteria may include the user's existing skills, runtime environment, offline operation, distribution, integration support, privacy, cost, latency, and maintainability. If these are unknown, remain stack-neutral or label a recommendation as provisional.

### Design the failure path with the happy path

For each consequential step, decide how failure is detected, communicated, retried, canceled, or recovered. The severity and likelihood of harm determine how much detail is needed.

### Separate evidence, assumptions, and preferences

Facts about this project, temporary assumptions, and reusable product preferences have different lifetimes. Never promote one into another without user confirmation.

## Preference record format

Use this structure when the user explicitly asks to retain a reusable product-design preference. A repository may keep these records in this file under `Recorded preferences`, or in another user-approved durable store. Do not persist them without authorization.

```markdown
### PREF-<stable-id>: <short principle>

- **Principle:** <the decision rule>
- **Scope:** <products or situations where it applies>
- **Rationale:** <why the user prefers it>
- **Provenance:** <user feedback or decision, with date/project if known>
- **Positive example:** <what following it looks like>
- **Exception / boundary:** <when it does not apply>
- **Status:** proposed | confirmed | superseded
- **Supersedes / conflicts with:** <record IDs or none>
```

Record the narrowest rule supported by the feedback. For example, “prefer local-only storage for personal text utilities” is safer than “never use cloud storage.” When feedback conflicts with a record, retain provenance, explain the conflict, and ask whether to narrow, supersede, or keep both context-dependent rules if that decision affects future work.

## Recorded preferences

No user-specific preferences have been recorded yet.
