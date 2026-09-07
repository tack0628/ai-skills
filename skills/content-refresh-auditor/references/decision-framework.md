# Decision framework

Use this framework to explain a recommendation, not to manufacture certainty. Evaluate only dimensions supported by the available inputs.

## Evidence ledger

For each source, record:

| Source | Minimum context to retain |
|---|---|
| Article content | URL or ID, captured version/date, completeness |
| Inventory | URL/ID field, title, status, canonical handling, coverage |
| Search Console | property, search type, dimensions, filters, timezone, date ranges, fresh-data caveats |
| Analytics/conversions | metric definition, attribution scope, date ranges, filters |
| Publish/update metadata | source and whether the date reflects a meaningful editorial change |
| User/editor judgment | decision, reason, scope, date, and who supplied it when known |

Keep `observed`, `derived`, `interpreted`, and `unknown` separate:

- **Observed:** directly present in a supplied or retrieved source.
- **Derived:** transparently calculated from observed values; state the formula or comparison.
- **Interpreted:** a supported explanation that could still have alternatives.
- **Unknown:** not available or not determinable from the evidence.

## Diagnostic dimensions

### Demand

Look for changes in impressions across comparable page/query segments, seasonality, and query mix. Lower clicks alone do not establish lower demand. A demand-decline hypothesis should remain tentative when the available export is truncated, filtered differently, or lacks comparable query/page detail.

### Visibility

Use impressions, average position, and query/page distribution together when available. Average position is an aggregate and can shift because query mix changed. Distinguish a broad loss from a few high-volume queries and from changes caused by newly appearing queries.

### CTR

Use clicks divided by impressions when raw values are available; do not average row-level CTRs unless weighting is justified. Compare like position ranges, queries, devices, countries, and search appearances when possible. A CTR issue may justify a title, description, or snippet-alignment TUNE, but only after checking visibility and intent. Do not apply an external “good CTR” benchmark unless the user supplies or authorizes one.

### Freshness and obsolescence

Inspect the actual article for stale facts, dates, product behavior, screenshots, broken promises, expired events, or unsupported “latest” language. An old update date is a review signal, not proof that content is obsolete; a recent date is not proof that it is current.

### Intent alignment

Compare the article's promise and structure with supplied query evidence and, if available, authorized current search evidence. Label intent change as a hypothesis unless there is direct comparative evidence. Distinguish mismatch in title/snippet from mismatch in the article itself.

### Content quality and unique value

Assess whether the article fulfills its promise, explains important points, avoids redundant padding, and contributes something not duplicated elsewhere. Preserve supported first-hand experience and authorial analysis even when surrounding factual sections need updating.

### Overlap and cannibalization

Content similarity can reveal an overlap candidate, not performance cannibalization by itself. Stronger evidence includes multiple site URLs receiving impressions for the same query cluster across comparable periods, unstable URL/query ownership, or two examined pages serving the same intent without distinct value. Also consider legitimate multi-page journeys and branded/navigation queries as counterevidence.

### Strategic value and risk

Where available, consider conversions, qualified traffic, backlinks, topical role, contractual needs, legal/compliance obligations, and editorial priorities. Absence of reported value is not evidence of no value.

## Action definitions

Choose one primary action. A secondary action may express sequencing, such as `HUMAN → REFRESH`, without hiding the current decision gate.

### KEEP — leave unchanged

Use when the article remains useful and supported; observed movement is adequately explained by demand, seasonality, measurement, or normal variation; expected benefit does not justify intervention; or evidence does not show a defect. State what should trigger reassessment.

### TUNE — make a bounded adjustment

Use when the underlying article and intent remain sound and the issue is localized: title/snippet alignment, a small stale passage, weak introduction, limited structural cleanup, or a few verified link/metadata fixes. Define the exact boundary so TUNE does not silently become a rewrite.

### REFRESH — materially revise

Use when important sections are obsolete, incomplete, misaligned with supported current intent, or unable to fulfill the article's promise. Identify what must be preserved and what must change. A performance decline without article-level diagnosis is insufficient.

### MERGE — evaluate consolidation

Use when two or more examined articles substantially duplicate intent or value and consolidation appears better for readers and site structure. Name all verified candidates, the likely retained purpose, unique material to preserve, and redirect/canonical questions. If destination and consequences are unresolved, pair with HUMAN.

### SPLIT — evaluate separation

Use when one examined article serves meaningfully distinct intents or audiences that make it unwieldy, confusing, or poorly focused. Name the proposed child purposes, not invented URLs, and explain why headings alone cannot solve the problem.

### PRUNE — consider removal, noindex, or retirement

Use only when the examined page has little unique or strategic value, is obsolete or harmful, and a safer update/merge option is not justified. Before execution require human review of traffic, conversions, backlinks, legal/compliance needs, internal links, replacement page, and redirect/noindex behavior. Lack of traffic data is not proof of no traffic.

### HUMAN — require human judgment

Use when the decision depends on first-hand experience, personal opinion, interviews, sensitive or regulated claims, brand intent, rights, unpublished business context, destructive changes, unresolved evidence conflicts, or data too weak for the requested consequence. Specify the exact question and evidence the reviewer needs. HUMAN is not a generic label for every missing optional metric.

## Confidence and priority

Use qualitative confidence:

- **High:** direct article evidence and relevant, comparable data support the diagnosis; material alternatives were checked.
- **Medium:** the evidence supports the direction but an important alternative or input remains unresolved.
- **Low:** the action is a hypothesis or screening candidate; do not present it as ready to execute.

Priority combines likely reader/business impact, urgency, confidence, and effort. Keep these components visible; do not assign precise ROI or arbitrary composite scores without user-provided assumptions.

## Common signal patterns

These are hypotheses to test, not automatic rules.

| Observed pattern | Likely next diagnosis | Do not conclude yet |
|---|---|---|
| Clicks down, impressions down, position stable | Demand, seasonality, query mix | Rewrite needed |
| Impressions stable, position stable, CTR down | Snippet/title, SERP mix, device/query mix | Article body is poor |
| Position and impressions down for relevant queries | Visibility and intent/content fit | Exact cause or required scope |
| Stable performance, verified stale facts | Freshness risk | KEEP because traffic is stable |
| Several pages share query clusters | Ownership and overlap | Cannibalization without page review |
| Old date but current, useful content | Monitor or KEEP | Obsolete content |
| Low traffic plus no supplied value data | Gather value evidence | PRUNE |

## Portfolio consistency

Normalize URLs conservatively and retain the original values. Report canonical ambiguity, duplicate rows, and unmatched items. Use a common comparison window only when appropriate, but allow exceptions for new, seasonal, migrated, or event-driven pages. Avoid forcing every article into an action distribution; it is valid for most pages to be KEEP.
