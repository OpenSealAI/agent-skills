---
name: socialseal-creator-evaluation
description: >-
  Use this skill when evaluating a supplied creator for a brand partnership using recent-post metrics and brand evidence. Basic profile and post retrieval works without this skill.
license: MIT
---

# Named-creator Evaluation

Preserve the supplied URL/handle, platform, requested post count, engagement/views, and brand-fit question. Use directly discovered account-profile and recent-account-post actions. Search-ranked rows cannot substitute for the account timeline; no tracking group or strategy setup is required for routine retrieval.

Retrieve accessible brand context before asking for missing information. Complete account metrics even if brand evidence is absent. Stored reads and bounded fresh collection are separate: explain stale/incomplete evidence and respect the collection action's quote, approval, budget, and idempotency boundary. One evaluation does not authorize ongoing tracking.

Report:

- Requested and returned counts, eligibility rule (all supported post types versus videos), publication ordering, source URLs, post type, collection time, and coverage. Pinned placement is not publication order. Unknown or historically substituted dates cannot establish recency. One provider page does not prove completeness.
- Average views over available view values only, with denominator and coverage. Zero is available; missing is unknown.
- The returned engagement formula, available components, denominator, and aggregation method. Distinguish mean per-post rates from a ratio of totals; do not silently substitute one for the other.
- Brand-fit observations grounded in creator/content and brand evidence, then clearly labelled inference and missing context. Public views do not establish private audience demographics or unique reach.

Keep useful partial results for private/unavailable accounts, provider errors, fewer posts, or missing dates/metrics. State the specific limitation. If a stale skill suggests a resolver or search setup first, follow the available direct-action schema and preserve this account-based task.

Use `references/mcp-and-cli-usage.md` only for call examples, artifact reading, or polling. A compound or multilingual request can combine independent direct actions; no fixed tool sequence is required.
