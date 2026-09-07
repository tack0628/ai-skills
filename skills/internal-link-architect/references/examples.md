# Examples

## Example 1: Simple article inventory

```text
$internal-link-architect

Target article:
[Paste article here]

Candidate articles:
1. ...
2. ...
3. ...
```

## Example 2: With constraints

```text
Analyze internal links for this article.

Target:
[article]

Inventory:
[CSV / sitemap / list]

Rules:
- Maximum 5 recommendations
- Prefer hub pages
- Exclude sponsored articles
- Avoid repeating the same anchor text
```

## Example 3: QA test

Check whether the skill:
- avoids invented URLs;
- rejects keyword-only matches;
- gives a concrete insertion location;
- explains why each link helps the reader;
- avoids recommending too many links.

## Example 4: Expected shape

Input:

```text
$internal-link-architect

Target:
Why does an air conditioner leak water on rainy days?

Existing pages:
- How to clean an AC drain hose
- Difference between cooling and dehumidifying
- How to choose an air conditioner
- Winter heating electricity costs
```

Expected high-level behavior:
- Rank drain-hose cleaning highest when drainage is discussed.
- Consider cooling vs. dehumidifying when operating modes are discussed.
- Reject unrelated pages even if they share the term "air conditioner".
- Suggest natural insertion points and non-forced anchor text.
