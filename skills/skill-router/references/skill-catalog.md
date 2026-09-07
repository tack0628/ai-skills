# Skill catalog

This is the routing source of truth for the skills in this repository. Each `Description` below mirrors the corresponding `SKILL.md` frontmatter. The skill's own files remain authoritative if a mismatch is found.

Use the canonical invocation form `$skill-name`. Do not infer availability from examples in old conversations or documentation.

## skill-router

- **Source:** `skills/skill-router/SKILL.md`
- **Invocation:** `$skill-router`
- **Description:** Route a natural-language request to the best available repository skills, identify required inputs, and propose a dependency-aware execution order. Use when the user is unsure which skill to invoke, asks what skills can help, or needs a workflow spanning multiple skills; propose a new skill instead of forcing a poor match.
- **Required input:** The user's desired outcome.
- **Optional input:** Available artifacts, constraints, current workflow stage, preferred deliverable.
- **Primary output:** One recommended skill or an ordered multi-skill plan, required and optional inputs, handoffs, and the next step. When nothing fits, a bounded new-skill proposal.
- **Boundary:** It selects and sequences work; selection alone does not execute another skill.

## article-quality-editor

- **Source:** `skills/article-quality-editor/SKILL.md`
- **Invocation:** `$article-quality-editor`
- **Description:** Review completed article drafts from an editor-in-chief perspective and produce a prioritized, actionable publication-readiness report. Use when the user asks to proofread, critique, audit, or improve an article for factual risk, AI-like phrasing, redundancy, missing explanation, heading structure, reader clarity, depth of analysis, unnatural SEO language, deletion candidates, or human verification needs.
- **Required input:** Completed article draft.
- **Optional input:** Brief, intended reader, publication goal, source notes, target keyword, house style, prior feedback.
- **Primary output:** Publication verdict; quality overview; prioritized findings with concrete edits; deletion/compression candidates; human verification checks; strengths to preserve; revision order. A full rewrite only when requested.
- **Boundary:** Reviews an existing draft. It does not create a topic-specific article from raw notes by default.

## content-refresh-auditor

- **Source:** `skills/content-refresh-auditor/SKILL.md`
- **Invocation:** `$content-refresh-auditor`
- **Description:** Audit existing articles with available content, inventory, publication metadata, and search-performance data to recommend KEEP, TUNE, REFRESH, MERGE, SPLIT, PRUNE, or HUMAN actions with evidence and uncertainty. Use for content refresh audits, decay diagnosis, content pruning, consolidation, or refresh prioritization; not for drafting an article from scratch.
- **Required input:** An existing article or useful content representation for content-quality, freshness, intent, MERGE, or SPLIT decisions. For a portfolio, stable IDs or URLs are needed to match records safely.
- **Optional input:** Article inventory, publish/update dates, comparable-period Search Console data, analytics, conversions, backlinks, business priorities, editorial constraints, prior decisions.
- **Primary output:** Scope and limitations; article or portfolio actions; evidence, counterevidence, confidence and missing data; priority and bounded next step; detailed decision cards and cross-portfolio findings when applicable.
- **Boundary:** Can run a content-only audit without performance data but must limit performance conclusions. It does not draft from scratch or automatically delete content.

## gallery-poster-maker

- **Source:** `skills/gallery-poster-maker/SKILL.md`
- **Invocation:** `$gallery-poster-maker`
- **Description:** Transform uploaded photos into premium minimalist 3:4 editorial posters with a photographic upper half and an abstract geometric lower half. Use when the user asks to turn one or more uploaded photos into luxury, gallery-style, architectural, editorial, or minimalist posters, or invokes $gallery-poster-maker.
- **Required input:** At least one user-provided image.
- **Optional input:** Title, year, mood, typography direction, background tone, whether to omit text.
- **Primary output:** One independent 3:4 poster image per source image, with an undistorted photographic upper half and a recognizable geometric abstraction below.
- **Boundary:** Does not combine images into a collage unless explicitly requested and is not a general-purpose image editor.

## idea-to-spec

- **Source:** `skills/idea-to-spec/SKILL.md`
- **Invocation:** `$idea-to-spec`
- **Description:** Turn rough product ideas, short notes, or “wouldn't it be useful if…” concepts into implementation-ready MVP specifications. Use for web tools, local utilities, AI tools, and small apps when the product shape is still vague; not for implementing an already-defined specification.
- **Required input:** A rough product idea, short note, or desired product outcome.
- **Optional input:** Intended users, known constraints, decided requirements, environment, integrations, delivery preferences.
- **Primary output:** Proportional MVP specification with product boundary, facts and assumptions, primary flow, requirements, inputs/outputs, essential risks, acceptance criteria, and ordered implementation tasks.
- **Boundary:** Produces a specification. It does not implement an already-defined specification.

## internal-link-architect

- **Source:** `skills/internal-link-architect/SKILL.md`
- **Invocation:** `$internal-link-architect`
- **Description:** Analyze a target article against a supplied site inventory and recommend useful, natural internal links with ranked candidates, insertion points, anchor text, exclusions, and structural observations. Use when the user asks to find internal-link opportunities, improve internal linking, connect an article to related pages, analyze a sitemap or article inventory for links, or invokes $internal-link-architect.
- **Required input:** Target article text, draft, or accessible URL content; and an existing article inventory such as a sitemap, CSV, URL list, or article list.
- **Optional input:** Priority pages, excluded pages, preferred anchor style, category rules, maximum recommendation count.
- **Primary output:** Ranked Markdown table of link candidates, relevance, insertion points, anchor text and reasons; avoid-link list; structural observations when useful.
- **Boundary:** Cannot reliably recommend links from a target article alone. It never invents pages or claims knowledge beyond exposed inventory metadata or accessible content.

## manga-article-architect

- **Source:** `skills/manga-article-architect/SKILL.md`
- **Invocation:** `$manga-article-architect`
- **Description:** Turn manga chapter notes, summaries, or source-grounded details into a structured spoiler article with title ideas, lead, headings, body, impressions, analysis, conclusion, and meta description. Use when the user asks to write or structure a manga chapter article, spoiler recap, review, analysis, or invokes $manga-article-architect.
- **Required input:** Manga title, chapter number or episode label, and user notes, summary, or source-grounded facts. Sparse material results in a correspondingly bounded article.
- **Optional input:** Preferred title, target keyword, existing URL, tone, site style, spoiler label preference, meta-description preference.
- **Primary output:** Title candidates, lead, structured recap body, separately labeled impressions/analysis, conclusion, and a meta description when requested or useful.
- **Boundary:** It is manga-specific and must not invent plot facts, dialogue, or canon. It is not a general article-review skill.

## Maintenance contract

When a skill is added, renamed, removed, or materially changes scope:

1. Inspect its actual `SKILL.md` and relevant output-format references.
2. Add or update one section here; copy the frontmatter description exactly.
3. Use `$skill-name` as the canonical invocation and align `agents/openai.yaml`.
4. Update the root README's human-facing table.
5. Update `routing-rules.md` only when the new capability changes a decision boundary, composition pattern, or no-match example.
6. Validate every skill and check local Markdown links and YAML parsing.
