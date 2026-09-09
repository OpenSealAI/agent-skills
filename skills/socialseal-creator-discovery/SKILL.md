---
name: socialseal-creator-discovery
description: >-
  Use this skill when the user asks which creators or UGC partners rank for specified search terms, or requests a shortlist based on ranked search evidence. Evaluate a supplied creator with named-account evidence instead.

license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
    - socialseal
    - strategy
    - creator-discovery
    - partner-shortlisting
    - share-of-voice
    - exports
---

# Search-evidence Creator Discovery

Shortlist partners from creators appearing in the requested ranked search population. This skill applies to search-authority shortlisting, not a supplied account's latest posts or general partnership evaluation.

Read existing authorized groups or supplied exports before requesting identifiers. Preserve the requested terms, market, language, platform, date window, and ranking criteria. Missing groups do not authorize creating a tracker or purchasing collection. Use available evidence and state the missing scope.

Read `references/mcp-and-cli-usage.md` for current direct-action schemas and complete export-artifact reading. The `search_results_enriched` report is CSV-only and takes `payload.groupIds`; `creator_signatures` is optional and requires existing `clusterRequest` evidence.

Within the requested population:

- Filter wrong markets, languages, unrelated queries, duplicate rows, and brand-owned/non-creator accounts. Flag uncertain account classification. If language is derived from the query or group, say so.
- Calculate keyword coverage with its denominator, best/median rank, top-three placements, and breadth across queries. Attach concrete post URLs and the queries/markets where each creator surfaced.
- Rank by scoped search authority when that is the requested criterion. Preserve other requested criteria and report available engagement/views separately; search rows do not represent an account's latest posts.
- Distinguish measured ranks from partnership-fit inference. State selection bias, coverage gaps, and the evidence window. Public views do not establish private audience demographics, unique reach, or guaranteed performance.

Return a useful shortlist with evidence and limitations. If no creators appear, report that none appeared in this sample; do not infer that the creator or partnership opportunity does not exist. A named creator absent from this sample remains eligible for account-based evaluation.
