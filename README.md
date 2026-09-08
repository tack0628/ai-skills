# ai-skills

実務で繰り返し使うAIワークフローを、再利用可能なSkillとして管理するリポジトリです。

## Skill Catalog

呼び出し名は `$skill-name` に統一しています。どのSkillを使うべきか分からない場合は、`$skill-router` に自然な言葉でやりたいことを伝えてください。

| Skill名 | 用途 | 呼び出し例 | 必要入力 | 主な出力 |
|---|---|---|---|---|
| `skill-router` | 依頼に合うSkillの選定、入力案内、実行順の提案 | `$skill-router ブログ記事を見直して内部リンクも整えたい` | やりたいこと。目的、素材、制約があれば併記 | 推奨Skill、選定理由、不足入力、実行順。該当Skillがなければ新規Skill候補 |
| `article-quality-editor` | 完成記事を編集長視点で査読し、公開可否と修正優先度を判断 | `$article-quality-editor この記事を公開前に査読して` | 記事本文（必須）。任意で読者、目的、出典、キーワード、文体ルール | 公開判定、品質評価、優先度付き指摘、要確認事項、修正順 |
| `content-cannibalization-finder` | 記事同士の検索意図競合を複数の根拠から検出し、共存・差別化・統合等を判断 | `$content-cannibalization-finder 記事一覧とSearch Consoleデータから競合候補を調べて` | URL等の安定した識別子。任意でタイトル、本文/要約、クエリ×URLの検索データ、時系列、内部リンク等 | 競合候補/共存判定、クエリ所有状況、KEEP/DIFFERENTIATE/MERGE/REDIRECT/INTERNAL-LINK/HUMAN、根拠・反証・確信度 |
| `content-refresh-auditor` | 既存記事を監査し、維持・調整・刷新・統合等を判断 | `$content-refresh-auditor 既存記事の更新優先度を監査して` | 記事本文または内容表現。複数記事ではURL等の識別子。任意で公開日・検索データ等 | KEEP/TUNE/REFRESH/MERGE/SPLIT/PRUNE/HUMAN判定、根拠、確信度、優先度、次の行動 |
| `gallery-poster-maker` | 写真を上半分が写真、下半分が抽象表現の3:4ポスターに変換 | `$gallery-poster-maker この写真をギャラリーポスターにして` | 画像1枚以上（必須）。任意でタイトル、年、ムード、背景色、文字の有無 | 入力画像ごとの独立した3:4ミニマルポスター画像 |
| `idea-to-spec` | 曖昧なプロダクト案を実装・検証可能なMVP仕様に整理 | `$idea-to-spec このツール案をMVP仕様にして` | ラフなアイデアやメモ。任意で利用者、制約、既決事項 | MVP境界、前提、ユーザーフロー、要件、受入基準、実装タスク |
| `internal-link-architect` | 対象記事とサイト内記事一覧から自然な内部リンク候補を設計 | `$internal-link-architect この記事の内部リンク候補を出して` | 対象記事本文またはアクセス可能な内容と、サイトマップ・CSV・URL一覧等の記事在庫（ともに必須） | 優先度付きリンク候補、挿入位置、アンカーテキスト、除外候補、構造上の所見 |
| `manga-article-architect` | 漫画の章メモからネタバレ・感想・考察記事を構成・執筆 | `$manga-article-architect 第○話のメモから記事を書いて` | 作品名、話数、章メモ・要約・根拠のある事実 | タイトル案、導入、見出し付き本文、感想・考察、結論、必要に応じてメタ説明 |
| `story-to-manga` | 怪談・体験談・一次資料・説明文などを、原文の確度を保った漫画ネームへ変換 | `$story-to-manga この怪談を8ページの漫画ネームにして` | 原文・メモ・根拠のある要約。任意でページ数、形式、画風方向、人物資料 | 適応方針、出典整理、キャラ/場所設定、ビート、ページ/コマ割り、画像生成指示 |\n| `source-first-researcher` | 一次情報を優先し、事実・推測・意見を分けた再利用可能な調査資料を作成 | `$source-first-researcher Googleの現在のSEO公式見解を調べて` | テーマまたは調査質問と調査目的。任意で対象読者、地域、期間、言語、深度 | 論点、主張台帳、出典台帳、URL、確認日、重要ポイント、矛盾・未確認事項、後工程への引継ぎ |

詳細なdescription、任意入力、出力仕様、使い分けは [`skills/skill-router/references/skill-catalog.md`](skills/skill-router/references/skill-catalog.md) を参照してください。

## Skillを追加・変更するとき

1. `skills/<skill-name>/SKILL.md` のfrontmatterと本文を正本として更新する。
2. `agents/openai.yaml` の表示名・説明・`$skill-name` を使う既定プロンプトを整合させる。
3. `skills/skill-router/references/skill-catalog.md` に入力・出力・適用範囲を反映する。
4. 上のSkill Catalogを更新し、`skill-router` のrouting rulesで新しい分岐が必要か確認する。
5. Skill validatorとYAML・参照パスの検査を実行する。
