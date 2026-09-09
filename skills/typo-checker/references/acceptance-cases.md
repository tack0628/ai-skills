# Standard acceptance cases

Use these cases when changing or release-testing the standard skill. They preserve the boundary demonstrated by the long-form 八尺様 test without storing the full source text.

## Mixed regression passage

```text
垣根の切れ目まで来ると、一人女性が見えた。
二人の動きが止った。
何を話しているのかは良く分からなかった。
今日は帰すわけには行かなくなった。
何にも心配しなくていいから。
何かおきたら仏様の前でお願いしなさい。
お菓子も食べる気が全くおこらなかった。
風のせいでそんな音がでているのか判断がつかなかった。
自分の時計を見たところはぼ同じ時刻だった。
やがて車は道の広い所で止り、親父の車に移された。
七人もの男が今の今、というわけにはいかなく、一晩待つことになった。
前文では成人前の若い人間が狙われやすいと述べた。まだ子供や若年の人間が不安なとき、つい心を許してしまうのだろう。
```

Expected classification:

### 明確な修正

- `一人女性` → `一人の女性`
- `はぼ同じ` → `ほぼ同じ`
- `道の広い所で止り` → `道の広い所で止まり`

### 表記の候補

- `止った` → `止まった`
- `良く分からなかった` → `よく分からなかった`
- `帰すわけには行かなくなった` → `帰すわけにはいかなくなった`
- `何かおきたら` → `何か起きたら`
- `全くおこらなかった` → `全く起こらなかった`
- `音がでている` → `音が出ている`

### 要確認

- `何にも心配しなくていい` → `何も心配しなくていい`; the reason must state that the colloquial original may be intentional and needs no correction if so.
- `今の今、というわけにはいかなく` → `—`; flag the connection as contextually suspicious, but do not invent `今すぐ`, `集まる`, or any other missing content.
- `まだ子供や若年の人間が` → `また、子供や若年の人間が`; state that both readings are possible and the original needs no correction if intentional.

Exact wording may vary. The classification, caution, and no-rewrite boundary must not.

## Excluded improvements

These must not be reported unless they contain a separate qualifying error:

- a long but grammatical sentence;
- a more elegant synonym or less repetitive phrase;
- word-order, rhythm, readability, politeness, or tone preferences;
- deliberate half-width kana, slang, dialogue, sound effects, or punctuation;
- factual, logical, structural, or SEO concerns.

When a phrase is unclear but no localized correction is supported, `要確認` may identify the uncertainty but must not complete, paraphrase, or rewrite it.

## Lite/standard split

Use the mixed regression passage to check the product boundary:

- `typo-checker-lite` remains the existing minimal localized-error pass; these standard cases do not add requirements to or modify that skill.
- `typo-checker` must systematically return the notation candidates and useful contextual suspicions above, separated by certainty.
- Neither skill may return a rewritten passage.

## Long-document invariant

Place the mixed regression passage near the end of a document of at least 100 paragraphs. All qualifying candidates must remain detectable, no text after the first finding may be skipped, and no corrected copy of the document may be produced.
