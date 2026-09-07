# Output template

Adapt detail to the number of pages and quality of evidence, but preserve the evidence boundaries and labels below.

## 1. Scope and data limitations

State:

- Pages, properties, query scope, and date ranges analyzed
- Sources, dimensions, metrics, filters, and content coverage actually used
- URL normalization or canonical assumptions
- Unmatched records, duplicates, row limits, missing fields, incomplete periods, and non-comparable data
- Whether this is a query-by-URL diagnosis or a content-only `competition candidate` screening
- Conclusions the available evidence cannot support

## 2. Candidate summary

For multiple pairs or clusters, use:

| Priority | Candidate pages / cluster | Finding | Primary action | Secondary action / gate | Confidence | Evidence for | Counterevidence / alternative | Missing evidence | Next step |
|---|---|---|---|---|---|---|---|---|---|

Use only these finding labels: `Likely competition`, `Possible competition`, `Competition candidate`, `Useful coexistence`, or `Indeterminate`.

Use only these actions: `KEEP`, `DIFFERENTIATE`, `MERGE`, `REDIRECT`, `INTERNAL-LINK`, or `HUMAN`. Use `REDIRECT` as primary only when the user's task is implementing an already approved retirement or migration; in an audit it is normally secondary to an approved MERGE/HUMAN gate.

## 3. Candidate decision card

Include a card for high-priority candidates, every MERGE or REDIRECT proposal, disputed findings, and small audits where each candidate can be shown.

```markdown
### [Query cluster or candidate label]

- Pages / stable IDs:
- Finding:
- Primary action:
- Secondary action or human gate:
- Confidence:
- Priority rationale: likely impact / evidence strength / urgency
- Query scope and periods:

**Page roles and intent**
- Page A:
- Page B (and others):
- Intended relationship:

**Evidence**
- Observed:
- Derived calculation:
- Interpretation:
- Evidence for competition:
- Counterevidence / alternatives checked:
- Unknown or missing:

**Recommendation**
- Change or decision:
- Preserve:
- Do not do without approval:
- Concrete next step:
- Success signal / reassess when:
```

When no Search Console or equivalent query-by-URL data is available, include this sentence or an equally explicit statement:

> This is a content-overlap competition candidate, not a finding of measured search-performance cannibalization.

## 4. Query ownership view

Include when query-by-URL data supports it:

| Query / justified cluster | Period | URL | Clicks | Impressions | CTR | Average position | Click share | Impression share | Ownership note |
|---|---|---|---:|---:|---:|---:|---:|---:|---|

Use `not provided` or `cannot derive` for missing values. Explain cluster rules and formulas. Do not fill gaps with estimates. For long exports, summarize material clusters and attach or describe a complete machine-readable output only when the user requests it.

## 5. Approved handoff record

After the user decides, preserve the decision separately from the diagnostic evidence:

```yaml
candidate_id: "supplied or locally assigned stable label"
pages:
  - "verified URL or ID"
finding: "Likely competition|Possible competition|Competition candidate|Useful coexistence|Indeterminate"
recommended_action: "KEEP|DIFFERENTIATE|MERGE|REDIRECT|INTERNAL-LINK|HUMAN"
confidence: "High|Medium|Low"
user_decision: "accepted|rejected|modified|deferred"
approved_action: "action or null"
intent_ownership: "approved role for each page or null"
preserve: "unique material, value, or constraints"
evidence_limits: "material unknowns"
next_skill: "content-refresh-auditor|article-quality-editor|internal-link-architect|none"
```

Never infer approval from silence. Pass only approved roles/actions to downstream implementation; retain unresolved hypotheses as hypotheses.

## Language discipline

Prefer:

- “The supplied query-by-URL export shows…”
- “These pages are a competition candidate because…, but measured harm cannot be determined without…”
- “The role distinction supports useful coexistence.”
- “The switching pattern is consistent with competition, while … remains an alternative explanation.”

Avoid:

- “Google is confused.”
- “These pages definitely cannibalize each other” from similarity or one period.
- “Delete/redirect the weaker page” without value and implementation checks.
- “CTR/rank improved because of the change” when only correlation is available.
