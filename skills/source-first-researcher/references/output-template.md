# Research package output template

Use these stable headings and IDs. Scale detail to the request, but do not omit provenance, uncertainty, or unresolved gaps merely to shorten the result.

```markdown
# Research package: <topic>

## 1. Research metadata

- Package version: 1.0
- Topic:
- Research purpose / downstream use:
- Scope and exclusions:
- Geography / jurisdiction:
- Time range and freshness requirement:
- Languages searched:
- Access date: YYYY-MM-DD
- Coverage limitations:

## 2. Executive findings

- <finding with claim IDs, e.g. C1, C4>
- Primary-source availability: <adequate / partial / none located, with a short reason>
- Most important uncertainty:

## 3. Question map

| ID | Research question | Priority | Status | Answer / disposition |
|---|---|---|---|---|
| Q1 | ... | Core | Answered / Partial / Unresolved | ... |

## 4. Claim ledger

| ID | Question | Claim | Label | Confidence | Source IDs | Caveat / reasoning |
|---|---|---|---|---|---|---|
| C1 | Q1 | ... | Verified fact | High | S1, S2 | ... |

Allowed labels: `verified fact`, `reported claim`, `inference`, `opinion`, `unresolved`.

## 5. Source ledger

### S1 — <source title>

- Source class: Primary / Authoritative synthesis / Secondary
- Author / issuing body:
- Document type:
- Published / updated / effective / data period:
- URL or persistent identifier:
- Accessed: YYYY-MM-DD
- Supports: C1, C3
- Important points:
- Relevant location: <section/page/table/timestamp when available>
- Authority and independence:
- Limitations:

## 6. Conflicts and competing accounts

| Issue | Source IDs | Nature of conflict | Assessment / unresolved point |
|---|---|---|---|

## 7. Evidence gaps and search limits

| Gap | Searches or repositories checked | Why it matters | Best next check |
|---|---|---|---|

State `No suitable primary source located` where applicable. Do not imply that the source does not exist.

## 8. Downstream handoff notes

- Claims safe to use as established facts:
- Claims requiring attribution:
- Inferences or opinions that must stay labeled:
- Claims to avoid or verify before publication:
- Useful angles, comparisons, tables, or visuals:
- Freshness triggers: <dates/events/versions that should prompt re-checking>
- Suggested next workflow or recipient:
```

## Formatting notes

- Cite source IDs beside every executive finding and downstream factual note.
- Put URLs in the source ledger rather than scattering untracked links through prose.
- Use one source entry per underlying document, not per website mention.
- Use `not stated`, `not accessible`, `not applicable`, or `cannot determine` instead of guessing.
- Keep facts compact. Do not draft the article, fabricate transitions, or optimize keyword density.
- When the user requests structured data, preserve the same fields and IDs in JSON, YAML, or a table. Do not change the meaning of labels.

## Machine-handoff invariants

A future source library can safely ingest the package when:

- `Package version`, topic, scope, access date, and freshness triggers are present;
- every claim has a unique `C` ID, status label, confidence, and source relationship;
- every question has a unique `Q` ID and disposition;
- every source has a unique `S` ID, source class, locator, dates, supported claims, and limitations;
- unresolved gaps and conflicts are explicit rather than embedded only in narrative prose.
