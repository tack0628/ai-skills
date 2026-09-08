---
name: manga-article-architect
description: Turn manga chapter notes, summaries, or source-grounded details into a structured spoiler article with title ideas, lead, headings, body, impressions, analysis, conclusion, and meta description. Use when the user asks to write or structure a manga chapter article, spoiler recap, review, analysis, or invokes $manga-article-architect.
---

# Manga Article Architect

Create a publishable manga chapter article from user-provided notes, summaries, excerpts, or source-grounded facts.

## Required inputs

Obtain as much as available:
- Manga title
- Chapter number or episode label
- User notes, summary, or source-grounded facts

Optional inputs:
- Preferred article title
- Target keyword
- Existing article URL
- Desired tone
- Site-specific style rules
- Whether spoilers should be clearly marked
- Whether meta description is needed

If the supplied information is sparse, write only what is supported. Do not invent missing plot details.

## Core goals

Produce an article that:
- accurately reflects the supplied chapter information;
- is easy to scan;
- separates plot facts from opinion and analysis;
- avoids padding;
- preserves important narrative chronology;
- gives the reader useful interpretation after the recap.

## Efficiency defaults

- Use only the supplied notes/source-grounded material unless the user explicitly asks for research.
- Do not retrieve the same chapter/article again when sufficient notes are already present.
- Produce 3 title candidates by default, not an open-ended list.
- If the user asks to revise an existing article, change only the requested or diagnosed sections unless a full rewrite is explicitly requested.
- Stop when the supplied material is exhausted; do not pad missing detail with generic commentary.

## Workflow

1. Identify the chapter's central conflict, reveal, turning point, or thematic hook.
2. Organize the supplied facts into chronological or narratively coherent order.
3. Draft 3 SEO-conscious but natural title options.
4. Write a concise lead that tells the reader what makes the chapter notable.
5. Build the spoiler recap using a clear H2/H3 hierarchy.
6. Write impressions and analysis separately from factual recap.
7. Highlight especially notable scenes, mechanics, reveals, character decisions, or future implications.
8. Write a short conclusion.
9. When requested or clearly useful, write a meta description.
10. Run the quality checks in `references/quality-checklist.md`.

## Default article structure

Use `references/article-structure.md` unless the user's requested structure overrides it.

## Writing style

Follow `references/writing-style.md`.

## Factual integrity

Never:
- invent dialogue;
- fabricate scenes;
- create character motivations as fact;
- add plot events absent from the supplied material;
- present speculation as confirmed canon;
- infer exact wording from paraphrased notes.

When uncertain, use language such as:
- "〜と考えられます"
- "〜の可能性があります"
- "作中の描写を見る限り"
- "今回の情報だけでは断定できません"

## Copyright-aware handling

Do not reproduce long copyrighted passages or dialogue.

Prefer:
- concise paraphrase;
- summary;
- analysis;
- brief quoted fragments only when genuinely necessary.

## Output

Default output order:

1. Title candidates
2. Lead
3. Article body
4. Impressions / analysis
5. Conclusion
6. Meta description, when requested

If the user asks only for part of the article, return only that part.

## Guardrails

- Do not pad the article to hit an arbitrary word count.
- Do not repeat the same event across multiple headings unless analysis adds something new.
- Do not overuse generic reactions such as "衝撃的でした" without explaining why.
- Keep chronology readable.
- Distinguish fact, interpretation, and prediction.
- Do not force SEO keywords unnaturally.
- Prefer specific chapter details over generic manga commentary.
