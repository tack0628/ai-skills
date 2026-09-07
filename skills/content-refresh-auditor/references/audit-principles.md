# Audit principles and feedback memory

This file is a schema for user-approved, reusable audit judgment. It is intentionally empty of site-specific preferences at release.

## Applying feedback

1. Preserve the original evidence and recommendation.
2. Record the user's later decision and stated reason as a separate feedback event.
3. Apply a correction to the current audit immediately.
4. Propose a reusable principle only when the feedback appears broader than one article.
5. Persist, revise, or retire a principle only with explicit user authorization.

Do not interpret acceptance as proof of the diagnosis, silence as acceptance, or one exception as a universal rule.

## Principle record

Use one block per authorized principle:

```yaml
id: "stable-short-id"
status: "candidate|active|retired"
principle: "Narrow instruction that changes an audit decision"
applies_when:
  site_or_property: "specific scope or all"
  content_type: "specific type or all"
  conditions:
    - "observable condition"
does_not_apply_when:
  - "exception or boundary"
rationale: "why the user wants this rule"
examples:
  - article_id: "URL or stable ID"
    decision: "the relevant user decision"
provenance:
  source: "conversation, ticket, editor, or other supplied source"
  recorded_on: "YYYY-MM-DD"
  authorized_by: "name/role when supplied, otherwise user"
last_reviewed: "YYYY-MM-DD or null"
```

## Maintenance rules

- Prefer a narrow contextual rule over a broad preference.
- Keep decision thresholds only when the user explicitly provides them; include metric definitions and scope.
- Preserve contradictory feedback as separate evidence until the user resolves its scope.
- When a principle conflicts with current direct evidence or a higher-priority user instruction, surface the conflict.
- Retire rather than delete superseded principles so prior audits remain explainable.
- Never store private or sensitive context unless the user explicitly wants it retained and the chosen storage is appropriate.

## Authorized principles

None yet.
