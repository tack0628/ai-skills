---
name: source-first-researcher
description: Research a topic for articles, analysis, or fact-checking by decomposing the question, prioritizing primary and authoritative sources, separating verified facts from inference and opinion, and returning a traceable research package with claims, citations, URLs, access dates, gaps, and handoff-ready notes. Use for SEO, public-policy, folklore or occult history, products and services, technical topics, and general research; not for writing the finished article.
---

# Source First Researcher

Turn a topic and research purpose into a reusable evidence package. Optimize for traceability and honest uncertainty, not for a persuasive narrative or a large link count.

## Inputs

Require a topic or research question and a research purpose. Use supplied constraints when available: intended reader or downstream task, geography, time range, language, freshness deadline, desired depth, and known sources.

If the purpose is broad, infer a reasonable scope and state it. Ask only when an unresolved choice would materially change the research target, such as jurisdiction, product version, or historical period.

## Research depth

Default to **Standard** unless the user asks otherwise.

- **Quick** — answer a narrow question with the minimum strong evidence; use 1–2 authoritative/primary sources per core question and no broad context search.
- **Standard** — cover core questions with the strongest reasonably available evidence; use at most 3 strong sources per core question by default, adding secondary context only when needed to resolve a gap, conflict, or interpretation.
- **Deep** — use for contested, high-stakes, historical, or explicitly comprehensive research; broaden cross-checking and source diversity deliberately.

Do not equate depth with link count. In every mode, stop when additional searches mostly repeat established evidence, the core questions are adequately supported, and remaining gaps are explicit.

## Reference routing

- Before searching, read [references/source-priority.md](references/source-priority.md) to choose and classify sources. Revisit it when source authority is ambiguous or primary evidence is unavailable.
- For planning, searching, verification, and stopping rules, read [references/research-workflow.md](references/research-workflow.md).
- Before assembling the deliverable, read [references/output-template.md](references/output-template.md) and keep its stable section names and identifiers.
- Before delivery, run [references/quality-checklist.md](references/quality-checklist.md).

## Workflow

1. Define the research decision: restate the topic, purpose, scope, exclusions, freshness needs, and what the package should enable downstream.
2. Decompose the topic into answerable research questions. Distinguish core questions from useful context and identify claims likely to need strong evidence.
3. Build a source plan for each question using the domain-specific priority rules. Search primary and authoritative sources first; add secondary sources only to discover, contextualize, compare, or explain primary evidence.
4. Inspect the actual source, not only a search snippet or third-party summary. Record the source owner, title, publication or update date when available, canonical URL or identifier, access date, source class, and the exact point it supports.
5. Cross-check consequential or disputed claims. Note scope, definitions, version, jurisdiction, sample, date range, conflicts, and limitations that affect interpretation.
6. Maintain a claim ledger. Label every substantive conclusion as `verified fact`, `reported claim`, `inference`, `opinion`, or `unresolved`; link it to source IDs and state confidence without laundering repetition into corroboration.
7. Stop when the core questions are covered by the strongest reasonably available evidence, remaining searches repeat known material, and gaps are explicit. Do not pad the package with weak sources.
8. Return the structured research package, including source and claim ledgers, conflicts, gaps, downstream notes, and recommended next checks. Do not turn it into a finished article unless the user separately requests drafting.

## Evidence rules

- Prefer Google or vendor documentation, public bodies, standards organizations, original research, company filings and first-party releases, archives, interviews or records closest to the event, and other direct evidence appropriate to the question.
- Treat a source as primary only for claims it is positioned to establish. A company page is primary for its stated policy or specification, not automatically for market-wide superiority or independent safety.
- Treat press coverage, encyclopedias, trade publications, reviews, aggregators, and expert commentary as secondary. They may provide context or leads but must not silently replace an available primary source.
- Separate publication date, last-updated date, event or data period, and access date. Fresh retrieval does not make old evidence current.
- Use precise citations and concise paraphrase. Preserve source meaning, qualification, and uncertainty; never invent quotations, page numbers, URLs, dates, authors, study findings, or archival provenance.
- When primary evidence cannot be found, say where and how it was sought, use the best available secondary evidence with a lower confidence label, and leave the claim unresolved when warranted.
- When sources disagree, present the conflict and the likely reason if supported. Do not choose the most convenient account.

## Boundaries

- The primary output is research structure, not publishable prose, SEO copy, a literature review masquerading as exhaustive, or a verdict unsupported by evidence.
- Do not cite search-result snippets as evidence when the underlying page can be inspected.
- Do not assume a high-ranking, frequently repeated, official-looking, or recently accessed source is accurate or independent.
- Do not overstate completeness. State search limitations, inaccessible material, language constraints, paywalls, missing archives, and tool or date cutoffs.
- Preserve copyright boundaries: extract only the minimum quotation needed for verification and otherwise paraphrase.

## Handoff

Use stable IDs such as `Q1`, `C1`, and `S1` and retain the output-template headings. This lets a writer, analyst, fact-checker, or future `$source-library-builder` ingest the package without reconstructing provenance. Downstream work must preserve claim labels, source IDs, caveats, and unresolved gaps.
