# Detection framework

Use this framework to investigate page competition without turning weak correlations into a verdict.

## 1. Evidence ledger and normalization

For every source, retain enough context to reproduce the interpretation:

| Source | Context to retain |
|---|---|
| URL/content inventory | original URL or ID, canonical if supplied, title, content coverage, captured version/date |
| Search Console export | property, search type, dimensions, filters, timezone, date range, row/export limits, freshness caveats |
| Historical comparison | both complete periods, period length, site migrations/releases, seasonality caveats |
| Internal-link/index data | capture date, crawl scope, status/canonical source |
| Business/editor input | stated role, priority, conversion purpose, decision owner, date when known |

Separate these evidence states:

- **Observed:** directly supplied or retrieved.
- **Derived:** calculated from observed fields with the calculation stated.
- **Interpreted:** a plausible explanation supported by evidence but open to alternatives.
- **Unknown:** not supplied or not determinable.

Normalize URLs conservatively. Safe mechanical comparisons may standardize protocol/host case, fragments, or an explicitly documented trailing-slash rule, but do not collapse parameters, paths, language versions, mobile pages, canonicals, or redirects without evidence. Retain the original identifier beside any normalized key.

## 2. Establish page roles and intent

For each page, describe only what the available title, headings, content, summary, query set, and supplied editorial context support:

- Primary user need or question
- Likely search-intent type and level of specificity
- Audience or stage in the journey
- Content role: hub/category, detail, episode/chapter, person/entity, definition, how-to, comparison, review, analysis, FAQ, news, location, product/service, or another evidenced role
- Unique material or value
- Expected parent, child, sibling, or standalone relationship when supported

Do not force a single intent label when the page is mixed. A hub and a detail page, a series overview and an episode article, a person profile and a work analysis, or a guide and its FAQ can legitimately share vocabulary and even queries.

## 3. Generate candidates

Prefer candidate generation in this order when data permits:

1. Shared query or query-cluster exposure across multiple URLs
2. Material URL ownership switching for the same query cluster over time
3. Similar primary intent and overlapping content among indexed pages
4. Title, slug, entity, heading, or keyword similarity as a screening clue only

Analyze both pairs and clusters. Pairwise review can miss three or more pages distributing one intent; a broad cluster can also hide one legitimate hub/detail relationship, so retain page-level evidence.

Group queries only when the grouping rule is explicit and meaningfully reflects intent. Do not merge queries merely because they share a token. Preserve important branded, navigational, local, freshness, product-model, episode/chapter, and question modifiers.

## 4. Diagnostic dimensions

### Intent equivalence

Ask whether the pages promise substantially the same outcome to the same searcher at the same stage. Strong lexical similarity with different purposes is counterevidence. Weak lexical similarity can still mask equivalent intent, but that conclusion requires content or query evidence.

### Same-query exposure

For each query or justified cluster, examine:

- Number and identity of URLs receiving impressions
- Impressions and clicks by URL
- Position context and exposure period
- Whether the pages appear concurrently, alternate across dates, or represent a stable primary page plus a minor secondary page
- Whether branded or navigational queries make multiple results useful

Multiple URLs receiving impressions is necessary performance evidence for a same-query competition hypothesis, but is not sufficient proof of harm.

### Query ownership and switching

When time-granular data exists, derive a transparent ownership view, such as each URL's share of cluster impressions or clicks per complete period. Investigate repeated switching of the leading URL together with performance or intent evidence. Do not label isolated switching at low volume, after publication, during migrations, or within normal position noise as cannibalization.

### Click, impression, CTR, and position distribution

Inspect concentration and dispersion instead of demanding that one URL always receive all activity.

- Cluster CTR, when raw data exists: `sum(clicks) / sum(impressions)`
- URL share of cluster clicks: `URL clicks / cluster clicks`
- URL share of cluster impressions: `URL impressions / cluster impressions`

Handle zero denominators explicitly. Do not sum average positions, and do not compute an unweighted mean of row CTRs or average positions. If a derived weighted position is useful, state the weighting and retain the original aggregates.

Distribution alone does not show harm. Check whether combined visibility, clicks, conversions, or user pathways are healthy; whether one page is clearly primary; and whether distinct pages satisfy different variants of the intent.

### Time-series behavior

Use complete and comparable periods. Look for persistent patterns such as:

- URL A rises as URL B falls for the same query cluster
- The leading URL repeatedly changes while combined results weaken
- A newly published or revised overlapping page coincides with displaced ownership
- Consolidation or differentiation is followed by clearer ownership and improved or stable combined outcomes

These are associations, not causal proof. Consider seasonality, demand shifts, algorithm changes, indexing changes, migrations, title edits, new content age, device/country mix, SERP features, and export truncation.

### Content duplication and distinctive value

Compare page promise, covered questions, entities, headings, conclusions, examples, media, firsthand material, and audience. Mechanical similarity measures may prioritize review, but copied boilerplate and shared series metadata can inflate similarity. Conversely, different wording does not make equivalent intent distinct.

Record what only each page contributes. A merge that discards unique evidence or purposeful specialization can be worse than coexistence.

### Architecture and internal signals

When supplied, inspect canonicals, indexation, redirects, breadcrumbs, hubs, anchor text, navigation, and internal-link concentration. Conflicting internal signals may blur page roles, but they do not alone prove search-performance cannibalization.

## 5. Counterevidence and alternative explanations

Check at least the applicable alternatives:

- Legitimate hub/detail, parent/child, series/episode, person/topic, review/specification, article/FAQ, regional, language, or funnel-stage separation
- One stable primary URL and incidental low-volume secondary exposure
- Brand or navigational SERPs where multiple owned results help users
- Seasonality, demand change, publication age, recrawl/indexing delay, migration, canonical error, measurement/filter changes, or incomplete recent data
- Different device, country, search appearance, or query mixes
- Normal rank volatility, especially for low-impression rows
- A general visibility problem affecting all pages rather than competition between them

## 6. Finding and confidence labels

Use one finding label per candidate:

- **Likely competition:** comparable query-by-URL evidence and examined content support substantially equivalent intent, a plausible harmful ownership/distribution pattern exists, and material alternatives were checked.
- **Possible competition:** multiple signals support concern, but harm, intent equivalence, or an important alternative remains unresolved.
- **Competition candidate:** content, title, URL, or limited query evidence merits investigation, but query-by-URL performance evidence is absent or insufficient. This is the maximum claim for content-only analysis.
- **Useful coexistence:** overlap exists, but distinct roles, intent, or user value support keeping the pages separate.
- **Indeterminate:** data quality, mapping, conflicts, or missing content prevents a defensible direction.

Report confidence separately:

- **High:** direct, comparable query-by-URL evidence and examined page content align; alternatives and data limitations were materially addressed.
- **Medium:** the direction is supported, but one important signal or alternative remains unresolved.
- **Low:** the result is screening-level, sparse, unstable, or depends on substantial assumptions.

Never call a finding “confirmed” solely because it has high confidence. Search data is observational, and the most defensible outcome may still be a monitored hypothesis or controlled change.
