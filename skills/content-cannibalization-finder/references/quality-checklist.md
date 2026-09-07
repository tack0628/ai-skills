# Quality checklist

Run this before delivering the analysis. Fix failures rather than listing them.

## Source and data integrity

- [ ] Every page and metric maps to a supplied stable URL/ID or the mapping limitation is explicit.
- [ ] Original URLs are retained and normalization/canonical assumptions are documented.
- [ ] Search property, dimensions, filters, date ranges, aggregation, row limits, and content coverage are named when available.
- [ ] Duplicate/unmatched records, zero denominators, missing values, partial periods, migrations, seasonality, and non-comparable filters are handled or flagged.
- [ ] No URL, query, content, metric, trend, page role, canonical, link, cause, or business value was invented.
- [ ] Observed data, derived calculations, interpretations, user statements, and unknowns remain distinct.

## Diagnosis

- [ ] Candidate generation considers query-by-URL evidence when available; title, slug, keyword, entity, or text similarity alone was not treated as proof.
- [ ] Each page's intent, audience, specificity, and role were examined from available evidence.
- [ ] Legitimate hub/detail, parent/child, episode/series, person/topic, overview/deep-dive, FAQ/article, brand/navigation, and funnel relationships were considered when applicable.
- [ ] Multiple URLs appearing for one query was not automatically called harmful.
- [ ] Query ownership, switching, click/impression distribution, position context, content overlap, and unique value were evaluated independently where supported.
- [ ] A single rank decline, CTR movement, or URL switch was not treated as proof.
- [ ] Average position and CTR were treated as aggregates; cluster CTR uses total clicks divided by total impressions when derived.
- [ ] Time-series claims use complete comparable periods or state the limitation.
- [ ] Alternative explanations such as demand, seasonality, query mix, device/country filters, migration, indexation, publication age, and export truncation were checked when relevant.
- [ ] Content-only analysis is labeled `Competition candidate`, never measured or confirmed cannibalization.

## Findings and actions

- [ ] Every candidate uses one allowed finding label and reports confidence separately.
- [ ] Every candidate has evidence for, counterevidence/alternatives, missing evidence, and a concrete next step.
- [ ] Every candidate has one primary action, with a secondary action only for a genuine gate or sequence.
- [ ] KEEP states the distinct value and a monitoring trigger.
- [ ] DIFFERENTIATE assigns a distinct intent/role and bounds title, structure, and content changes.
- [ ] MERGE names all examined pages and the retained purpose, inventories unique value, and does not invent a destination.
- [ ] REDIRECT follows an approved merge/retirement/migration decision and includes destination, chain, canonical, internal-link, value, and monitoring checks.
- [ ] INTERNAL-LINK represents a defensible hierarchy and does not substitute for unresolved duplicate intent.
- [ ] HUMAN asks a precise question and names the evidence or decision owner needed.
- [ ] No change, deletion, redirect, canonical edit, publication, or other external action is implied without separate authorization.

## Handoff quality

- [ ] Broader lifecycle questions go to `$content-refresh-auditor` with overlap evidence kept as one diagnostic dimension.
- [ ] Approved revisions or merges go to `$article-quality-editor` with intent assignments, facts to preserve, and unresolved risks.
- [ ] Stable page relationships go to `$internal-link-architect` with verified inventory and no unresolved hypothesis presented as fact.
- [ ] The final report follows `references/output-template.md` and keeps the user's later decision separate from the original evidence and recommendation.
