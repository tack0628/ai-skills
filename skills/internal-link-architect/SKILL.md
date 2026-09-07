---
name: internal-link-architect
description: Analyze a target article against a supplied site inventory and recommend useful, natural internal links with ranked candidates, insertion points, anchor text, exclusions, and structural observations. Use when the user asks to find internal-link opportunities, improve internal linking, connect an article to related pages, analyze a sitemap or article inventory for links, or invokes $internal-link-architect.
---

# Internal Link Architect

Analyze a target article together with a supplied inventory of existing site content and propose useful internal links grounded only in the material available.

## Required inputs

Obtain:
- Target article text, draft, or accessible URL content.
- Existing article inventory such as a sitemap, CSV, URL list, or article list.

Accept optional constraints such as:
- Priority pages.
- Excluded pages.
- Preferred anchor-text style.
- Site category rules.
- Maximum recommendation count.

If the user supplies only one article and no inventory, ask for a sitemap or article list unless the environment can directly access the site's content.

## Workflow

1. Identify the target article's main topic, subtopics, search intent, entities, and likely reader follow-up questions.
2. Review the supplied inventory and infer relevance only from information actually available.
3. Exclude:
   - the target page itself;
   - clearly unrelated pages;
   - duplicate or near-duplicate recommendations;
   - pages explicitly excluded by the user.
4. Score remaining candidates for semantic relevance and reader usefulness.
5. Prefer links that:
   - answer a natural next question;
   - explain a term or concept mentioned in the target article;
   - connect detail pages to useful hub or summary pages;
   - connect hub pages to useful detail pages.
6. Identify a natural insertion point in the target article.
7. Suggest concise anchor text that fits the surrounding sentence naturally.
8. Never invent articles, URLs, facts, or page contents.
9. If the supplied inventory is insufficient to make reliable recommendations, say so explicitly.

## Scoring

Use this scale:
- 90–100: Directly useful and highly natural.
- 75–89: Strong supporting link.
- 60–74: Context-dependent.
- Below 60: Normally do not recommend.

Do not score candidates purely from keyword overlap.

## Output

Return a Markdown table using exactly these columns:

| Priority | Internal link candidate | Relevance | Suggested insertion point | Anchor text | Reason |
|---|---|---:|---|---|---|

Then include `### Avoid linking` and list candidates that may appear related but should not be linked, with a brief reason.

Include `### Structural observations` only when useful. Consider:
- missing hub pages;
- orphan-like content;
- excessive overlap;
- category inconsistencies;
- reciprocal-link opportunities.

## Guardrails

- Prioritize reader usefulness over SEO theory.
- Do not force exact-match anchor text.
- Do not recommend excessive links.
- Do not claim ranking or traffic benefits without evidence.
- Keep every recommendation grounded in the supplied material.
- If using a CSV or sitemap, do not pretend to know article content that is not exposed by titles, URLs, metadata, or accessible page text.

## Examples

For reusable test cases and QA checks, read `references/examples.md` when examples are needed.

## Related skills

- After `$content-cannibalization-finder`, accept only approved page roles and stable destinations as architecture constraints. Keep unresolved competition candidates labeled as hypotheses; do not use internal links as a substitute for a pending DIFFERENTIATE or MERGE decision.
