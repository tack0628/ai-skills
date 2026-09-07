# Routing rules

Use these rules after consulting `skill-catalog.md`. They resolve overlaps and multi-step requests; they do not replace the catalog.

## Outcome-to-skill map

| User's intended result | Route | Distinguishing evidence |
|---|---|---|
| Choose a skill, see available capabilities, or plan a cross-skill workflow | `$skill-router` | The desired result is a route or execution plan, not the domain artifact itself |
| Assess whether an existing article is ready to publish | `$article-quality-editor` | A completed draft exists; the user wants editorial diagnosis, verification needs, or concrete fixes |
| Decide what to do with an already-published article or portfolio | `$content-refresh-auditor` | The desired result is KEEP/TUNE/REFRESH/MERGE/SPLIT/PRUNE/HUMAN prioritization |
| Turn uploaded photos into the defined premium split-layout poster | `$gallery-poster-maker` | At least one source image exists and the requested deliverable is a poster image |
| Convert a vague product idea into a buildable MVP definition | `$idea-to-spec` | The product shape is still unclear and the deliverable is a specification, not implementation |
| Choose internal links for a target article | `$internal-link-architect` | Both target content and a real site inventory are available or retrievable |
| Draft a manga chapter recap, spoiler article, review, or analysis | `$manga-article-architect` | Source-grounded chapter notes or facts exist and the deliverable is manga-specific article copy |

## Important boundaries

- **Review vs refresh audit:** Use `$article-quality-editor` for the quality of a current draft. Use `$content-refresh-auditor` for the lifecycle decision and priority of an existing article. If both are requested, audit first; only send approved revision work to editorial review after revision.
- **Drafting vs reviewing:** Use `$manga-article-architect` to create or restructure a manga article from notes. Use `$article-quality-editor` to judge a completed draft. Do not route general drafting to the editor.
- **Specification vs implementation:** `$idea-to-spec` is appropriate while the MVP is vague. An implementation request against an already-defined spec has no matching build skill in this repository.
- **Visual specificity:** `$gallery-poster-maker` is for its defined 3:4 split poster treatment. General retouching, logos, illustrations, slide design, or unrelated image generation are not matches.
- **Inventory dependency:** `$internal-link-architect` needs both target content and a real inventory. A missing inventory is a blocking input, not a reason to invent candidate URLs.

## Common multi-skill sequences

Choose only the stages the user actually requests.

### New manga article through link planning

1. `$manga-article-architect` — turns grounded notes into the draft.
2. `$article-quality-editor` — reviews the stable draft and preserves source uncertainties.
3. Human revision or approval — resolves blockers and applies chosen edits.
4. `$internal-link-architect` — designs links against the verified site inventory after structure is stable.
5. Optional light `$article-quality-editor` pass — checks inserted anchors and final readability.

### Existing-content refresh

1. `$content-refresh-auditor` — recommends the smallest justified action.
2. Human decision — approves REFRESH, MERGE, SPLIT, or PRUNE scope.
3. `$manga-article-architect` — only when approved work is a manga article and source notes support drafting.
4. `$article-quality-editor` — checks the revised draft.
5. `$internal-link-architect` — runs after the article structure is stable.

### Product idea

1. `$idea-to-spec` — defines and validates the MVP boundary.
2. Stop or propose a new implementation skill — no repository skill currently builds the resulting product.

## Ordering logic

Order by artifact dependency, not a fixed master sequence:

- Decide scope before producing work that depends on the decision.
- Produce or revise content before reviewing it.
- Resolve major editorial findings before designing links against article structure.
- Require a human gate before deletion, publication, external side effects, or work marked HUMAN.
- Pass forward the smallest useful artifact: source notes and uncertainties, audit evidence and approved scope, stable draft, or verified inventory.

## Ambiguity handling

Do not ask the user to classify their request in skill terminology. Explain the concrete fork instead.

- “記事を直したい” may mean lifecycle prioritization or line/structure review. If an article is already selected and the user wants edits, prefer `$article-quality-editor`; if they want to decide whether and how much to update across articles, prefer `$content-refresh-auditor`.
- “記事を書いて” matches `$manga-article-architect` only for manga chapter material. General blog drafting has no current match.
- “画像を作って” matches `$gallery-poster-maker` only when source photos and its poster treatment are intended.
- “ツールを作って” matches `$idea-to-spec` only when the user wants the idea specified. Building the tool is a separate missing capability.

Ask one concise question only when the answer changes the selected skill or required sequence. Otherwise state the assumption and route.

## No-match behavior

A no-match result is correct when available skills cannot produce the requested outcome. State the gap before mentioning nearby skills.

Propose a new skill only when the capability is coherent and likely reusable. Use a lowercase hyphenated name, a discriminating one-sentence description, essential inputs, and the primary output. Examples of current gaps include:

- general article drafting outside manga;
- implementing an application from a completed specification;
- general-purpose image editing outside the gallery-poster treatment;
- publishing content to a CMS;
- collecting analytics when the user has not supplied an export or authorized a source.

Do not imply that a proposed skill exists. Do not create it unless the user asks.
