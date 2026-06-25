---
name: socialseal-creator-discovery
description: >-
  Use this skill when shortlisting creator-shop or UGC partners for a market using
  SocialSeal search evidence: ranking creators by how often and how prominently they
  surface for the destination, category, and language searches that matter, not by
  follower or vanity metrics. Produces an evidence-backed partner shortlist with
  market, language, destination/topic authority, and the queries each creator wins.
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

# SocialSeal Creator Discovery

## Overview

SocialSeal creator discovery answers: which creators should we partner with for this market and topic, because they already surface for the searches our customers run? The signal is **search authority** (how often and how prominently a creator's content ranks for the tracked queries), not follower count or total likes.

Vanity metrics describe a creator's general reach. SocialSeal measures something more useful for a creator-shop partnership: does this creator's content actually surface when someone searches the destination, route, or category you care about, in the right market and language? This skill ranks candidates on that evidence.

Do not invent a creator list from outside knowledge or follower counts. Pull candidates from creators who already rank for the brand's tracked searches. See `references/mcp-and-cli-usage.md` for call patterns and `references/socialseal-data-contract.md` for attribution.

## When to Use

- Shortlisting creator-shop / affiliate / UGC partners for a destination, route, or category.
- Ranking creators by destination or topic authority in a specific market and language.
- Comparing candidate creators against current partners on the searches that matter.
- Producing a partner brief input (which queries a creator already wins) before outreach.

This is a strategy-phase skill. Hand the shortlist to `socialseal-creator-briefing` for the actual brief, and to `socialseal-social-plan-builder` when partners feed a plan.

## Inputs

Required:
- workspace id (or a configured default)
- the destination/route/category to staff, expressed as the tracked keyword set or group(s)
- target market (region) and target language(s)
- one or more tracking group ids that cover the relevant searches (one platform each)

Good to have:
- current/known partner handles to benchmark against
- platform priority (TikTok, Instagram, YouTube)
- a definition of "owned" handles so brand accounts are excluded from the partner shortlist
- a previous-period export to show momentum

If no tracking group covers the destination yet, route to `socialseal-tracking-group-design` to create a clean group first, or seed candidate searches with `socialseal-predictive-demand-routing` / `search-journey-run`.

## Data Access

The proven, primary source is enriched ranked search rows. Each row already carries the creator handle, the query it surfaced for, the rank, and the latest engagement snapshot.

CLI:

```bash
npx -y @socialseal/cli data export-search-results \
  --group-ids <group-id-1>,<group-id-2> \
  --workspace-id <workspace-id> \
  --out ./exports/creator-discovery.csv \
  --timeout 120000
```

MCP-first (there is no `export-search-results` MCP tool):

```text
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "body": { "reportType": "search_results_enriched", "format": "csv", "payload": { "groupIds": [<group-id>] } }
}
```

Use these enriched columns (see `references/socialseal-data-contract.md`):
- `author_handle`: the creator (render with a leading `@`).
- `keyword`, `region`, `language`, `platform_id`: the query and its scope.
- `rank` / `best_rank` / `latest_rank`: where the creator surfaced (prominence).
- `appearance_count`, `distinct_keywords_seen`: breadth of surfacing across the set.
- `views_count`, `likes_count`, ... : the latest engagement snapshot (context, not the ranking driver).
- `title`, `video_url`: human-readable evidence links.

Optional enrichment (only when cluster insights already exist for the scope): the `creator_signatures` report can summarize recurring creators per cluster. It requires a precomputed `clusterRequest`, not raw `groupIds`, and returns an error when no clustering exists. Treat it as an add-on; ground the shortlist on enriched search rows.

```text
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "body": { "reportType": "creator_signatures", "format": "json", "payload": { "clusterRequest": { "groupIds": [<group-id>], "region": "<region>", "platformId": <platform-id> } } }
}
```

## Workflow

1. **Confirm scope.** Lock the destination/category, market (region), language(s), platform(s), and which group ids cover the searches. State the date range of the export.
2. **Export enriched rows** for those groups and inspect columns and grain.
3. **Filter to qualified, in-scope rows.** Keep rows whose `keyword`, `region`, and `language` match the partnership scope. Drop off-market, off-language, and irrelevant rows before ranking. When `language` is blank at row level, derive language from the keyword (script/terms) or the group's configured language; say which you used.
4. **Exclude owned and non-creator accounts.** Remove brand-owned handles and obvious media/official accounts so the shortlist is genuine creator-shop candidates. Tag conservatively and flag ambiguous ones for review.
5. **Aggregate per creator.** For each `author_handle` compute, within the stated scope and denominator:
   - **keyword coverage**: distinct in-scope keywords the creator surfaces for / total in-scope keywords.
   - **prominence**: rank-weighted surfacing (higher rank = more weight); summarize as best/median rank and count of top-3 placements.
   - **destination/topic authority**: coverage and prominence concentrated on the destination/route/category keywords specifically, not generic terms.
   - **breadth vs depth**: `distinct_keywords_seen` and `appearance_count`.
   - engagement snapshot as supporting context only.
6. **Rank by search authority, not vanity.** Order candidates by destination authority + prominence + coverage in scope. Do not let raw views/followers reorder the list; report them as context.
7. **Attach evidence.** For each shortlisted creator, cite 1-3 concrete examples: the `"keyword" [market, platform]` they win, the video title/URL, and the rank. Keep `video_uid`/`search_result_id` as an internal traceability note only.
8. **Label confidence.** Coverage/prominence are hard observations (measured); but they describe only what surfaces for the tracked queries, a biased sample, so frame "authority" as scoped, never as total reach or guaranteed fit. See `references/evidence-and-confidence.md`.

## Output

A creator shortlist table:

- creator (`@handle`)
- market / language / platform
- destination/topic authority (scoped: coverage % + prominence)
- keyword coverage in scope (with denominator)
- prominence (best/median rank, # top-3)
- breadth (`distinct_keywords_seen`)
- engagement snapshot (context only)
- queries they win (`"keyword" [market, platform]`)
- evidence examples (video title/URL, rank)
- fit note + confidence basis (measured / scoped statistic)
- internal traceability column (e.g. `ref (video_uid)`), kept secondary

Plus a short recommendation: who to approach first and why, who to benchmark, and which destinations still have no strong creator surfacing (a staffing gap).

## Do / Don't

Do:
- rank on scoped search authority (coverage + prominence) for the destination
- state the platform, market, language, keyword set, date range, and denominator
- cite creators by `@handle` and back each with `"keyword" [market, platform]`, title/URL, and rank
- exclude owned and official/media accounts from the partner shortlist
- treat engagement and followers as context, not the ranking driver

Don't:
- shortlist by follower count, total likes, or general virality
- claim a creator's "total reach" or "audience size" from surfaced rows (selection bias)
- present a creator as a proven fit; surfacing is evidence, partnership performance is a test
- make the user read internal IDs as the deliverable
- make platform-age/recency claims when `published_at` is blank

## Troubleshooting

- Export lacks `author_handle` for some rows: those are likely unresolved videos; exclude or re-export with `export-group-evidence` before ranking.
- `language` column blank: derive language from the keyword text or the group config and state the method; or split the analysis by group when groups are language-clean.
- `creator_signatures` returns 400/500: it needs a precomputed `clusterRequest`; skip it and rank from enriched rows, or compute clustering first.
- No creators surface for the destination: that is a staffing gap, not a data error. Widen the keyword set, change `timePeriod`, or seed new searches via `socialseal-predictive-demand-routing`.
- One creator dominates a single viral video: weight by coverage/prominence across keywords, not one outlier row.

## Verification Checklist

- [ ] Scope (platform, market, language, keyword set, date range) and denominator are stated.
- [ ] Owned and non-creator accounts are excluded.
- [ ] Ranking is by scoped search authority, not follower/vanity metrics.
- [ ] Each shortlisted creator has evidence (queries won, title/URL, rank).
- [ ] Confidence basis is labeled and selection bias is acknowledged.
- [ ] Staffing gaps (destinations with no strong creator) are surfaced.
