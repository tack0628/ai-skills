# Review format

Adapt the depth to the request. Keep labels and evidence fields stable so later audits and user feedback can be compared.

## 1. Audit scope and limitations

State:

- articles and date ranges covered;
- sources actually used;
- match failures, duplicates, filters, and incomplete fields;
- conclusions the evidence cannot support.

Do not bury material data limitations after the recommendations.

## 2. Portfolio action table

For multiple articles, use:

| Priority | Article | Primary action | Secondary action / gate | Confidence | Evidence summary | Missing evidence | Next step |
|---|---|---|---|---|---|---|---|

Use `—` rather than inventing a secondary action. Keep the evidence summary specific enough to trace back to an article passage, metric comparison, or supplied policy.

## 3. Article decision card

Include decision cards for high-priority items, disputed items, and any MERGE, SPLIT, PRUNE, or HUMAN result. Include all items when the audit is small.

```markdown
### [Article title or supplied ID]

- URL/ID:
- Primary action:
- Secondary action or decision gate:
- Confidence:
- Priority rationale: impact / urgency / effort
- Current promise and intent:

**Evidence**
- Observed:
- Derived:
- Interpretation:
- Counterevidence / alternatives checked:
- Unknown or missing:

**Recommended scope**
- Change:
- Preserve:
- Do not change without human approval:
- Concrete next step:
- Reassess when / success signal:
```

For KEEP, provide a monitoring trigger. For TUNE and REFRESH, bound the edit. For MERGE and SPLIT, identify all examined pages or purposes. For PRUNE, list pre-action checks. For HUMAN, pose the exact decision question.

## 4. Cross-portfolio findings

Include only supported patterns, such as:

- query ownership or overlap candidates;
- recurring freshness risks;
- inventory or measurement gaps;
- workflow handoffs to related skills;
- recommended order of operations and dependencies.

Do not turn a single page observation into a sitewide conclusion.

## 5. Feedback record

When the user accepts, rejects, or changes decisions, append a separate feedback record in the response or user-approved storage:

```yaml
article_id: "supplied stable ID or URL"
audit_date: "YYYY-MM-DD"
recommended_action: "KEEP|TUNE|REFRESH|MERGE|SPLIT|PRUNE|HUMAN"
user_decision: "accepted|rejected|modified|deferred"
final_action: "action or null"
reason: "user's reason, faithfully summarized"
scope: "article|section|query cluster|site"
principle_candidate: "narrow reusable lesson or null"
exceptions: "known limits or null"
provenance: "conversation, ticket, editor, or other supplied source"
```

Never infer acceptance from silence. Do not overwrite the original recommendation or evidence; feedback is a later decision layer.

## Language discipline

Prefer:

- “The supplied export shows…”
- “This suggests…, but … remains an alternative.”
- “Cannot determine from the available data.”
- “Candidate for human review before…”

Avoid:

- “Google penalized this page” without direct evidence.
- “Search intent changed” based only on lower traffic.
- “These pages cannibalize each other” based only on similar titles.
- “No value” when conversion, link, or strategic data was not supplied.
