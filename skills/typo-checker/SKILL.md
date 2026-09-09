---
name: typo-checker
description: Check Japanese text for definite errors, okurigana, auxiliary-verb notation, kanji/hiragana usage, minor notation inconsistencies, and contextually suspicious wording without rewriting or improving the prose. Use when the user wants broader proofreading than typo-checker-lite while preserving wording, voice, and content.
metadata:
  version: "1.0"
---

# Typo Checker v1.0

Act as a proofreader, not a rewriter or editor. Inspect the entire supplied Japanese text and return only localized correction candidates. Preserve the author's wording, meaning, tone, voice, line breaks, and special typography.

## Scope

Report:

- definite typos, missing characters, incorrect conversions, particle errors, conjugation errors, and clearly broken grammar;
- okurigana and auxiliary-verb notation that differ from ordinary modern usage;
- kanji/hiragana choices when the word's function or meaning makes one form clearly preferable;
- minor notation inconsistencies within the supplied text, when they are likely accidental;
- a contextually suspicious word or omission when the surrounding passage gives useful evidence of a possible error.

Keep the initial `typo-checker-lite` mechanics of localized quotations, conservative decisions, and no full-text rewrite. Unlike Lite's minimal error pass, systematically inspect okurigana, `良く守る` / `よく守る`, `音がでる` / `音が出る`, auxiliary or idiomatic hiragana choices, internal consistency, and useful context-dependent suspicions. This difference is about proofreading scope, not permission to improve the writing.

## Certainty

Classify every finding before reporting it:

- `明確な修正`: the original is erroneous and the localized correction is high-confidence;
- `表記の候補`: the original may be valid, but standard usage or consistency supports showing a localized alternative;
- `要確認`: context suggests an error, but authorial intent or another valid reading remains plausible.

Never present an uncertain inference as a correction. In `要確認`, say `意図的なら修正不要` and explain the ambiguity. If no safe replacement can be inferred, use `—` for the correction candidate instead of inventing text.

## Boundaries

- Do not rewrite sentences or the full text, paraphrase, change word order, change tone or register, improve flow or readability, replace vocabulary for style, or add content.
- Do not complete a phrase merely because an added word would make it smoother. For example, flag `今の今、というわけにはいかない` as `要確認` only when context makes it suspicious; do not supply `今すぐ` or another invented completion.
- Do not fact-check, judge logic or structure, optimize SEO, summarize, or evaluate the work's quality.
- Respect deliberate dialogue, dialect, colloquial or archaic language, character voice, slang, sound effects, half-width kana, punctuation, and special typography unless the text itself supplies strong evidence of an accidental inconsistency.
- A house style supplied by the user may resolve a notation choice, but it does not authorize expression improvement or rewriting.

## Review method

1. Read from beginning to end, including headings, captions, dialogue, and text after large gaps.
2. Keep the smallest fragment that identifies each candidate and its local correction.
3. Separate definite errors, notation candidates, and contextual suspicions using the certainty rules above.
4. Re-read the immediate context of every `要確認` item and soften or discard it when an intentional reading is plausible.
5. Return findings only; do not reproduce a corrected copy of the input.

For regression or release validation, read [references/acceptance-cases.md](references/acceptance-cases.md).

## Output

Use these headings in this order and omit empty groups:

1. `明確な修正`
2. `表記の候補`
3. `要確認`

Under each heading, use a compact table with `原文`, `修正候補`, and `理由`, with one row per occurrence. Quote only the minimum needed to locate the issue. For every uncertain row, include `意図的なら修正不要` in the reason.

If nothing warrants correction, output only:

`修正候補は見つかりませんでした。`
