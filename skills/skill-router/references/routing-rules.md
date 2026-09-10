# Routing rules

Use these rules after consulting `skill-catalog.md`. They resolve overlaps and multi-step requests; they do not replace the catalog.

## Outcome-to-skill map

| User's intended result | Route | Distinguishing evidence |
|---|---|---|
| Choose a skill, see available capabilities, or plan a cross-skill workflow | `$skill-router` | The desired result is a route or execution plan, not the domain artifact itself |
| Strongly compress supplied text into only essential bullets | `$compact-summarizer-lite` | The user wants quick confirmation of facts, decisions, or chronology rather than explanation, rewriting, analysis, or a new content format |
| Find only clear typos and localized language errors without rewriting | `$typo-checker-lite` | The user wants minimal error detection, not editorial evaluation or prose improvement |
| Proofread Japanese for errors and notation without rewriting | `$typo-checker` | The user wants ordinary proofreading that includes okurigana, kanji/hiragana, auxiliary verbs, consistency, or cautious context-dependent checks |
| Assess whether an existing article is ready to publish | `$article-quality-editor` | A completed draft exists; the user wants editorial diagnosis, verification needs, or concrete fixes |
| Detect whether multiple pages compete for the same search intent | `$content-cannibalization-finder` | The user wants page-pair/cluster, query-ownership, overlap, or cannibalization diagnosis rather than a general content lifecycle decision |
| Decide what to do with an already-published article or portfolio | `$content-refresh-auditor` | The desired result is KEEP/TUNE/REFRESH/MERGE/SPLIT/PRUNE/HUMAN prioritization |
| Turn uploaded photos into the defined premium split-layout poster | `$gallery-poster-maker` | At least one source image exists and the requested deliverable is a poster image |
| Convert a vague product idea into a buildable MVP definition | `$idea-to-spec` | The product shape is still unclear and the deliverable is a specification, not implementation |
| Choose internal links for a target article | `$internal-link-architect` | Both target content and a real site inventory are available or retrievable |
| Draft a manga chapter recap, spoiler article, review, or analysis | `$manga-article-architect` | Source-grounded chapter notes or facts exist and the deliverable is manga-specific article copy |
| Adapt supplied prose, testimony, primary-source material, or explanatory text into a manga or manga-production package | `$story-to-manga` | The source material already exists and the deliverable is a production script, manga name/storyboard, continuity plan, generated art, speech-balloon layout, or fully lettered page images |
| Build an evidence package before writing, analysis, or fact-checking | `$source-first-researcher` | The user needs questions decomposed, primary sources gathered, claims classified, citations traced, or evidence gaps made explicit |

## Important boundaries

- **Compression vs rewriting or analysis:** Use `$compact-summarizer-lite` when the deliverable is a short bullet-only extraction from supplied text. Do not use it for smoother prose, detailed explanations, critique, interpretation, fact-checking, multi-document comparison, or conversion into email, article, or social copy.
- **Minimal check vs ordinary proofreading vs editorial review:** Use `$typo-checker-lite` when only clear localized errors should be reported. Use `$typo-checker` when notation and cautious context-dependent errors should also be checked, without expression improvement or rewriting. Use `$article-quality-editor` for readability, expression, publication readiness, structure, depth, factual risk, or whole-article quality.
- **Review vs refresh audit:** Use `$article-quality-editor` for the quality of a current draft. Use `$content-refresh-auditor` for the lifecycle decision and priority of an existing article. If both are requested, audit first; only send approved revision work to editorial review after revision.
- **Cannibalization diagnosis vs refresh audit:** Use `$content-cannibalization-finder` when the core question is whether pages compete for the same intent, how query ownership is distributed, or whether overlap is useful. Use `$content-refresh-auditor` when overlap is only one factor in a broader KEEP/TUNE/REFRESH/MERGE/SPLIT/PRUNE decision. For a combined portfolio audit, diagnose material overlap candidates first and pass the evidence into the refresh audit.
- **Drafting vs reviewing:** Use `$manga-article-architect` to create or restructure a manga article from notes. Use `$article-quality-editor` to judge a completed draft. Do not route general drafting to the editor.
- **Specification vs implementation:** `$idea-to-spec` is appropriate while the MVP is vague. An implementation request against an already-defined spec has no matching build skill in this repository.
- **Visual specificity:** `$gallery-poster-maker` is for its defined 3:4 split poster treatment. General retouching, logos, illustrations, slide design, or unrelated image generation are not matches.
- **Inventory dependency:** `$internal-link-architect` needs both target content and a real inventory. A missing inventory is a blocking input, not a reason to invent candidate URLs.
- **Manga article vs manga adaptation:** Use `$manga-article-architect` when the output is a prose article about a manga chapter. Use `$story-to-manga` when supplied prose or source material itself should become a manga name, production package, or generated manga images.
- **Blueprint vs full manga production:** `$story-to-manga` handles both. Route to the same skill and preserve the user's requested stopping point; otherwise its default is production script, pre-lettering art generation, deterministic balloon and text composition, and final QA when the required tools are available.
- **Research before documentary manga:** Use `$source-first-researcher` first when primary-source facts still need to be gathered or verified; pass the approved evidence package to `$story-to-manga` for adaptation and image production.
- **Research vs drafting:** Use `$source-first-researcher` when the deliverable is evidence organized for later use. Use `$manga-article-architect` only when the deliverable is manga article copy. A request for general finished article drafting remains unmatched after research unless another suitable drafting skill is added.

## Common multi-skill sequences

Choose only the stages the user actually requests.

### New manga article through link planning

1. Optional `$source-first-researcher` — builds a source-grounded package when supplied notes are insufficient, contested, or need provenance work.
2. `$manga-article-architect` — turns grounded notes or the approved research package into the draft.
3. `$article-quality-editor` — reviews the stable draft and preserves source uncertainties.
4. Human revision or approval — resolves blockers and applies chosen edits.
5. `$internal-link-architect` — designs links against the verified site inventory after structure is stable.
6. Optional light `$article-quality-editor` pass — checks inserted anchors and final readability.

### Research before downstream work

1. `$source-first-researcher` — decomposes the question and produces a traceable research package.
2. Human or subject-matter review — resolves consequential disputed or unresolved claims when necessary.
3. Pass the package, including claim labels, source IDs, and gaps, to the requested drafting, analysis, specification, or future source-library workflow. Select another repository skill only when it actually matches that deliverable.

### Existing-content refresh

1. Optional `$content-cannibalization-finder` — diagnoses material page-overlap or query-ownership questions when they are central to the audit.
2. `$content-refresh-auditor` — recommends the smallest justified lifecycle action using overlap as one evidence dimension.
3. Human decision — approves REFRESH, MERGE, SPLIT, or PRUNE scope.
4. `$manga-article-architect` — only when approved work is a manga article and source notes support drafting.
5. `$article-quality-editor` — checks the revised draft.
6. `$internal-link-architect` — runs after the article structure and page roles are stable.

### Product idea

1. `$idea-to-spec` — defines and validates the MVP boundary.
2. Stop or propose a new implementation skill — no repository skill currently builds the resulting product.

## Ordering logic

Order by artifact dependency, not a fixed master sequence:

- Decide scope before producing work that depends on the decision.
- Produce or revise content before reviewing it.
- Resolve major editorial findings before designing links against article structure.
- Require a human gate before deletion, publication, external side effects, or work marked HUMAN.
- Pass forward the smallest useful artifact: a research package with claim/source IDs and uncertainties, audit evidence and approved scope, stable draft, or verified inventory.

## Ambiguity handling

Do not ask the user to classify their request in skill terminology. Explain the concrete fork instead.

- “記事を直したい” may mean lifecycle prioritization or line/structure review. If an article is already selected and the user wants edits, prefer `$article-quality-editor`; if they want to decide whether and how much to update across articles, prefer `$content-refresh-auditor`.
- “記事を書いて” matches `$manga-article-architect` only for manga chapter material. General blog drafting has no current match.
- “画像を作って” matches `$gallery-poster-maker` only when source photos and its poster treatment are intended. It matches `$story-to-manga` when supplied prose should be adapted into manga reference art or page/panel images.
- “ツールを作って” matches `$idea-to-spec` only when the user wants the idea specified. Building the tool is a separate missing capability.
- “調べて記事にして” contains two outcomes. Use `$source-first-researcher` for the evidence package, then route drafting separately; do not imply that research alone produces publishable copy.

Ask one concise question only when the answer changes the selected skill or required sequence. Otherwise state the assumption and route.

## No-match behavior

A no-match result is correct when available skills cannot produce the requested outcome. State the gap before mentioning nearby skills.

Propose a new skill only when the capability is coherent and likely reusable. Use a lowercase hyphenated name, a discriminating one-sentence description, essential inputs, and the primary output. Examples of current gaps include:

- general article drafting outside manga (research for it is covered by `$source-first-researcher`);
- implementing an application from a completed specification;
- general-purpose image editing outside the gallery-poster treatment and story-to-manga production workflow;
- publishing content to a CMS;
- collecting analytics when the user has not supplied an export or authorized a source.

Do not imply that a proposed skill exists. Do not create it unless the user asks.
