---
name: content-refresh-auditor
description: Audit existing articles with available content, inventory, publication metadata, and search-performance data to recommend KEEP, TUNE, REFRESH, MERGE, SPLIT, PRUNE, or HUMAN actions with evidence and uncertainty. Use for content refresh audits, decay diagnosis, content pruning, consolidation, or refresh prioritization; not for drafting an article from scratch.
---

# Content Refresh Auditor

Decide what each existing article needs without treating every ranking or traffic decline as a rewrite request. Separate observed evidence from interpretation, identify missing evidence, and make the smallest justified recommendation.

## Inputs

Accept one article or a portfolio. Use only what the user supplies or what authorized tools can actually retrieve.

- Article content or accessible page text
- Article inventory with stable identifiers or URLs
- Publish and update dates
- Comparable-period search data, such as Google Search Console page/query clicks, impressions, CTR, and average position
- Optional analytics, conversions, backlinks, business priorities, editorial constraints, and prior audit decisions

An article or useful content representation is required for content-quality, intent, freshness, MERGE, or SPLIT conclusions. Performance data is optional. When it is absent, perform a content-only audit and explicitly limit performance conclusions. Ask for missing material only when it is essential to the requested decision; otherwise proceed with a clearly bounded result.

## Portfolio efficiency

For a portfolio, do not send every full article through deep analysis by default.

Use a staged funnel:
1. **Screen** inventory/metadata/performance data to identify plausible candidates.
2. **Triage** the highest-value or highest-uncertainty candidates using titles, summaries, relevant sections, and query evidence.
3. **Deep audit** full article text only for candidates where the lifecycle decision depends on content-level evidence.

Prefer deterministic filtering or supplied audit outputs before model-heavy review when available. State the shortlist logic and do not interpret an unexamined article as audited.

## Reference routing

- For evidence requirements, diagnosis, action definitions, and confidence rules, read [references/decision-framework.md](references/decision-framework.md).
- For the audit table, article detail cards, portfolio summary, and feedback record, read [references/review-format.md](references/review-format.md).
- Before delivering any audit, run [references/quality-checklist.md](references/quality-checklist.md).
- When the user supplies prior decisions, corrects a recommendation, or asks to retain audit preferences, read and apply [references/audit-principles.md](references/audit-principles.md).

## Workflow

1. Inventory the supplied sources. Record field definitions, date ranges, filters, aggregation level, missing values, and whether periods are actually comparable.
2. Match records by canonical URL or another supplied stable identifier. Report unmatched and duplicate records; do not silently join on a guessed title or partial URL.
3. Establish the article's current promise, audience, search intent, unique value, and any passages based on first-hand experience, opinion, interviews, or author voice.
4. Compare performance only across defensible baselines. Check period length, seasonality, publication age, site changes, query mix, device/country filters, and incomplete recent data before interpreting movement.
5. Diagnose dimensions separately: demand, visibility, CTR, freshness, intent alignment, content quality, overlap/cannibalization, strategic value, and human-review risk.
6. Assign one primary action and, only when useful, a secondary action. Use the minimum intervention supported by evidence. Do not use a score or threshold as a substitute for diagnosis.
7. Attach direct evidence, counterevidence, confidence, missing data, expected scope, and a concrete next step to every recommendation.
8. Rank work by expected value, urgency, confidence, and effort. Keep “priority” distinct from “severity”; a weak article may still be low priority.
9. Return the result in the review format and record user feedback separately from observed evidence.

## Non-negotiable guardrails

- Never fabricate article text, page contents, metrics, trends, dates, queries, competitors, intent shifts, conversions, or causes.
- Use `not provided`, `not observed`, or `cannot determine` instead of filling gaps with plausible values.
- Do not infer demand decline from clicks alone. Do not infer CTR failure from rank decline alone. Do not infer cannibalization from topic similarity alone.
- Treat average position and aggregate CTR as diagnostic clues, not precise rankings or universal quality scores.
- Do not compare non-equivalent periods without labeling the limitation. Never treat a partial recent period as a completed period.
- A ranking decline may lead to KEEP when demand, seasonality, measurement, or insufficient evidence better explains the change.
- PRUNE means “consider removal, redirect, or noindex after checks,” never automatic deletion. Require human approval and assess traffic, conversions, links, uniqueness, compliance, and redirect consequences.
- MERGE and SPLIT are candidates until the involved articles and likely reader intents have been examined. Never invent a destination URL.
- Preserve first-hand experience, personal judgments, interviews, sensitive claims, and distinctive author voice. Recommend HUMAN when deciding or rewriting them requires the author's intent, subject expertise, legal judgment, or unpublished context.
- When retrieved data conflicts with supplied data, surface the conflict rather than selecting whichever supports the recommendation.

## Feedback and learning

Treat user decisions as labeled feedback, not retroactive proof that the original evidence meant something else. Apply feedback immediately to the current audit. Persist it only when the user explicitly asks to record it or clearly authorizes the update.

Store reusable preferences as narrow, contextual principles with provenance, examples, exceptions, and status using `references/audit-principles.md`. Keep site policy separate from observations and per-article decisions so future audits can distinguish stable rules from one-off judgment.

## Related skills

- Use `$content-cannibalization-finder` when overlap or unstable query ownership needs dedicated pair/cluster diagnosis. Pass its finding, query scope, counterevidence, confidence, and unresolved data into this audit without treating the hypothesis as settled.
- Send approved REFRESH work that needs manga-specific drafting or restructuring to `$manga-article-architect`, together with the audit evidence, preserved facts, and sections marked HUMAN.
- Send a revised draft to `$article-quality-editor` for publication-readiness review. Preserve this audit's factual uncertainties and required human checks.
- Use `$internal-link-architect` after article structure is stable. Pass the verified inventory and any overlap findings, but do not convert a cannibalization hypothesis into a link recommendation without evidence.
- A typical loop is audit → human decision → revise → quality review → internal-link design → publish → later audit. Follow the user's requested order when it differs.
