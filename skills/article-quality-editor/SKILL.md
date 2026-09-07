---
name: article-quality-editor
description: Review completed article drafts from an editor-in-chief perspective and produce a prioritized, actionable publication-readiness report. Use when the user asks to proofread, critique, audit, or improve an article for factual risk, AI-like phrasing, redundancy, missing explanation, heading structure, reader clarity, depth of analysis, unnatural SEO language, deletion candidates, or human verification needs.
---

# Article Quality Editor

Review a completed article without flattening its intended voice. Diagnose before rewriting, distinguish verified errors from items that merely need verification, and concentrate attention on changes that materially improve trust and readability.

## Inputs

The article draft is required. Use any supplied brief, intended reader, publication goal, source notes, target keyword, house style, or prior editorial feedback as constraints.

If optional context is absent, proceed with reasonable assumptions and state only assumptions that affect the verdict. Do not invent the article's intended audience, factual support, or SEO target.

## Reference routing

- For a full review, read [references/quality-checklist.md](references/quality-checklist.md) and inspect every applicable dimension.
- For the report shape, severity levels, and verdicts, read [references/review-format.md](references/review-format.md).
- Before applying house-style or user-specific judgment, and whenever the user gives feedback on the review, read [references/editing-principles.md](references/editing-principles.md).

## Review method

1. Identify the article's promise, intended reader, central claim, and desired reader outcome from the supplied material.
2. Separate statements that are presented as fact from opinion, inference, prediction, and promotional language.
3. Review the article in focused passes: factual risk; AI-like expression; redundancy and deletion candidates; missing explanation; headings and flow; reader clarity; analytical depth; SEO naturalness; and required human checks.
4. Evaluate each applicable dimension using the quality checklist. Do not manufacture findings to fill every category.
5. Consolidate overlapping symptoms into the underlying editorial issue. Rank findings by publication risk and reader impact, not by their position in the draft.
6. For each actionable finding, identify the location, quote only the shortest necessary fragment, explain the impact, and recommend a concrete edit. Provide replacement wording when it resolves the issue efficiently.
7. Return the report using the review format. Rewrite the whole article only when the user asks for a rewrite; otherwise preserve a clear boundary between diagnosis and proposed edits.

## Factual integrity

Treat absence of support as a verification need, not proof that a claim is false.

- Label a statement as incorrect only when reliable supplied or retrieved evidence contradicts it.
- Flag names, dates, numbers, quotations, attributions, causal claims, superlatives, and time-sensitive claims when their support is unclear.
- When sources are available, cite the source that supports the finding and explain the conflict precisely.
- When verification cannot be completed, say what a human should check and what evidence would resolve it.
- Keep fact, interpretation, and speculation visibly distinct.

## Editorial boundaries

- Preserve deliberate style, dialect, humor, and emphasis unless they obstruct the stated goal or conflict with confirmed editorial principles.
- Do not call text “AI-like” merely because it is polished. Name the observable pattern and its reader impact.
- Do not force brevity where context, safety, accessibility, or persuasion requires explanation.
- Do not force target keywords, exact-match anchors, or generic search phrases into prose.
- Do not silently change technical meaning, quotations, proper nouns, or the author's position.
- Escalate potentially material factual, legal, medical, financial, attribution, privacy, or copyright concerns for human review.

## Feedback and learning

Apply explicit user corrections to the current review immediately. Convert recurring preferences into small, testable candidate principles using the process in `references/editing-principles.md`.

Do not modify the persistent principles file merely because the user accepted one edit or disliked one sentence. Add, revise, or retire a user-specific principle only when the user explicitly asks to record it or clearly authorizes that update. Preserve the context and provenance of every recorded principle so later feedback can refine it without turning one example into a universal rule.

## Related skills

- After `$manga-article-architect`, use its source notes and factual/interpretive separation as review context. Return structural, unsupported, or shallow-analysis findings without inventing canon details.
- Before `$internal-link-architect`, resolve major content and structure issues so link recommendations target a stable draft. If links have already been inserted, review anchor naturalness and reader value, but do not infer the contents of linked pages from URLs alone.
- A useful sequence is draft creation → quality review → internal-link design → a light final quality pass. Follow the user's requested order when it differs.
