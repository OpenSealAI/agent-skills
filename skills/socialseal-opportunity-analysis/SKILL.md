---
name: socialseal-opportunity-analysis
description: 'Use this skill when turning SocialSeal tracking exports, search journey
  results, or group evidence into opportunity analysis: discoverability gaps, keyword
  priorities, content jobs, and recommended next actions grounded in SocialSeal data.'
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
  - socialseal
  - strategy
  - opportunity-analysis
  - discoverability
  - exports
---

# SocialSeal Opportunity Analysis

## Overview

SocialSeal opportunity analysis answers: where should the brand create or improve content because people are searching and the current surfaced content leaves a gap?

This skill replaces a vague prompt like “analyze this SocialSeal data.” It tells the agent what to inspect, how to define an opportunity, what metrics are safe to use, and what a good deliverable looks like.

## Inputs

Required:

- SocialSeal export files or SocialSeal MCP/CLI access
- workspace ID and group ID(s), or exported CSV/JSON files
- brand/entity definition and owned handles
- platform, market, language, keyword/topic scope, and date range

Good to have:

- competitor list
- current content pillars
- business priority or target audience
- previous-period export for comparison

## Data Access

Use enriched ranked search rows for keyword-level analysis:

```bash
npx -y @socialseal/cli data export-search-results \
  --group-ids <group-id-1>,<group-id-2> \
  --workspace-id <workspace-id> \
  --out ./exports/search-results.csv \
  --timeout 120000
```

Use group evidence when you need a safer unified export across social and Google AI groups:

```bash
npx -y @socialseal/cli data export-group-evidence \
  --group-id <group-id> \
  --workspace-id <workspace-id> \
  --out ./exports/group-evidence.csv \
  --timeout 120000
```

MCP-first: there is no `export-group-evidence`/`export-search-results` MCP tool. Reach enriched ranked rows via `socialseal_export_report` (`reportType: "search_results_enriched"`, `payload: { "groupIds": [<group-id>] }`) or `socialseal_export_tracking_data`. See `references/mcp-and-cli-usage.md`.

Attribution: cite surfaced results in human-readable terms, the `"keyword" [market, platform]`, the video title or `video_url`, and `@author_handle`, with where it ranked. Keep `video_uid`/`search_result_id` only as an internal traceability note, and respect the timestamp rules (no platform-age claims when `published_at` is blank). See `references/socialseal-data-contract.md`.

Evidence tiers: discoverability, coverage, and share of voice are hard observations, not estimates; report them plainly. But every figure is computed over a biased sample (only high-ranking videos for the tracked queries), so it describes "what surfaces for these queries," not total market demand. See `references/evidence-and-confidence.md`.

## Workflow

1. **Inspect the export.** Identify columns, grain, platform, market, date range, keyword field, URL/media ID, account/entity fields, metrics, and analysis fields.
2. **Define the denominator.** For each group, count qualified keywords/searches and qualified surfaced results. Exclude irrelevant rows before calculating.
3. **Separate entities.** Tag owned brand, competitors, creators/media/partners, and irrelevant/noise. If owned handles are unknown, ask or create a conservative placeholder column.
4. **Calculate safe metrics.** Use keyword coverage, discoverability by topic, surfaced attention/share where qualified metrics exist, and owned-vs-creator split. Do not lead with raw row counts.
5. **Find gaps.** A strong opportunity usually has search intent, relevant surfaced content, weak/absent owned presence, and a content job the brand can answer.
6. **Classify content jobs.** Use practical tags such as teach, walkthrough, compare, plan, reassure, show mood, show detail, or answer first-timer questions.
7. **Prioritize.** Rank by relevance, search intent strength, competitive/creator activity, expected business usefulness, and production feasibility.
8. **Select evidence.** For each recommendation, include metrics plus 1-3 examples that show what currently surfaces, cited by video title/URL and `@handle`. Label each recommendation's confidence basis (measured / scoped statistic / indicative pattern).

## Output

Create an opportunity table with:

- priority
- platform / market / keyword or topic
- current brand presence
- who/what surfaces now
- content job
- why this matters
- recommended content direction
- evidence examples (video title/URL, `@handle`, `"keyword" [market, platform]`)
- caveat/confidence (measured / scoped statistic / indicative pattern)

Also include a short action summary: what to brief, what to track, what to inspect further, and what not to pursue.

## Do / Don't

Do:

- use percentages and denominators
- distinguish “no brand presence” from “no meaningful search demand”
- cite examples by video title/URL, `@handle`, and `"keyword" [market, platform]`
- keep recommendations shootable or operationally actionable

Don't:

- call every zero a whitespace opportunity
- recommend topics outside the brand’s plausible scope
- claim total market demand from sampled social-search results (selection bias)
- make the user read internal IDs or raw exports as the deliverable

## Troubleshooting

- If exports lack video/source identifiers, run `export-group-evidence` or refresh the export before video-level analysis.
- If brand tagging is ambiguous, tag conservatively and add a review-needed column.
- If keyword language is mixed, split analysis by language/market before ranking opportunities.
- If the export is stale, refresh before making recommendations.

## Verification Checklist

- [ ] Export grain and scope are stated.
- [ ] Denominators are visible.
- [ ] Owned, competitor, creator, and irrelevant rows are separated.
- [ ] Opportunities include evidence and a content job.
- [ ] Recommendations are actionable and within brand scope.

