# Editing Principles

Use this file to distinguish durable editorial judgment from one-off preferences. The default principles apply unless the user supplies stronger constraints. The user-specific section is intentionally conservative: explicit feedback should improve future reviews without turning a single reaction into a universal rule.

## Precedence

Apply instructions in this order:

1. The user's instructions for the current article.
2. Confirmed, context-matching user-specific principles in this file.
3. The publication's supplied style guide or editorial policy.
4. The default principles below.

Factual integrity and safety are not overridden by stylistic preference. If two principles conflict, follow the more specific one and mention the conflict only when it affects the result.

## Default principles

### Preserve purpose and voice

Edit toward the article's promise and reader outcome. Retain intentional personality, cadence, humor, and domain terminology. Prefer the smallest change that solves the identified problem.

### Prefer information-bearing prose

Every paragraph should advance fact, reasoning, context, evidence, emotion, or transition. A sentence that only announces that something is important, interesting, or surprising should explain why or be removed.

### Make uncertainty legible

Distinguish confirmed fact, sourced interpretation, personal judgment, and prediction. Calibrate certainty to the available evidence instead of using either false confidence or blanket hedging.

### Explain at the reader's point of need

Define unfamiliar terms and supply necessary context before the reader must use them. Do not repeat background the intended audience can reasonably be expected to know.

### Earn the analysis

Strong analysis connects an observation to an interpretation, explains why it matters, and addresses a plausible alternative when relevant. Plot summary, paraphrase, and generic reaction do not become analysis merely by appearing under an analysis heading.

### Keep SEO subordinate to meaning

Use search terms where they naturally clarify topic or intent. Remove repetitive exact-match phrases, search-query fragments, and headings written for crawlers rather than readers.

## Recognizing AI-like expression

Treat “AI-like” as a pattern diagnosis, not an accusation about authorship. Common signals include:

- generic openings or conclusions that could fit almost any article;
- repeated restatement with little new information;
- mechanical transitions and overly symmetrical section shapes;
- inflated abstraction where a concrete detail is available;
- empty praise, excitement, or importance claims;
- excessive signposting about what the article “will explain” or “has shown”;
- uniform sentence rhythm that suppresses the author's natural voice.

Recommend an edit only when the pattern harms specificity, credibility, pace, or voice.

## User-specific editorial profile

No user-specific principles are recorded yet.

When the user explicitly authorizes an update, record one atomic principle per entry with this structure:

```markdown
### UEP-001: Short descriptive title

- Status: active
- Scope: article types or contexts where this applies
- Principle: a testable editorial rule
- Rationale: why the user prefers it
- Evidence: brief paraphrase of the user's feedback; do not store unnecessary personal data
- Added: YYYY-MM-DD
- Last refined: YYYY-MM-DD
- Exceptions: known cases where it should not apply
```

Use sequential IDs. Revise an existing entry when new feedback narrows or clarifies the same preference. Mark an entry `deprecated` with a short reason instead of deleting its history when the user reverses a preference.

## Turning feedback into a principle

1. Apply the correction to the current task.
2. Decide whether it is article-specific, contextual, or plausibly durable.
3. If durability is uncertain, present it as a candidate rather than persisting it.
4. Ask for or rely on explicit authorization before editing this file.
5. Record the narrowest rule supported by the feedback, including scope and exceptions.
6. On later reviews, cite the principle ID only when it materially explains a recommendation.

Do not record secrets, private source material, or personal data that is unnecessary for editorial behavior.
