---
name: socialseal-discoverability-tracking
description: >-
  Use this skill when the user asks whether a brand or competitor appears in social
  search, who leads, how ranks/keyword coverage/share of voice compare, or whether
  visibility changed over time. Compute scoped discoverability metrics from ranked
  SocialSeal exports, produce tables/charts, and verify completeness and denominator
  consistency before reporting movement.
license: MIT
metadata:
  socialseal:
    phase: measurement
  tags:
  - socialseal
  - measurement
  - discoverability
  - share-of-voice
  - keyword-coverage
  - tracking
  - refresh
  - anomaly-check
---

# SocialSeal Discoverability Tracking

## Overview

This skill has two jobs:

1. **Measure now (snapshot).** Turn a ranked export into discoverability, keyword coverage, and share of voice for named entities (owned brand vs competitor), reported as metric tables and a chart — this is the answer to "how do we compare with <competitor> on discoverability / share of voice?".
2. **Track over time.** Refresh exports, compare like with like, detect tracking/data problems, and keep a change log so movement stays interpretable.

Always compute the metrics before discussing strategy. A brand-vs-competitor visibility question is a measurement question even when it names a competitor; do not stop at a narrative of which videos appeared.

## Inputs

- workspace ID and group IDs
- entity definition: owned brand and competitor handles to tag (if owned handles are unknown, ask or tag conservatively and mark review-needed)
- platform, market, language, keyword/topic scope, and date range
- current export and previous export (for movement)
- tracking-group change log and expected keyword/group manifest
- optional: the exact keyword list the user named (map to tracked items, see Workflow)

## Data Access

Lead with **ranked rows** — they carry `keyword`, `region`, `author_handle`, `rank`/`best_rank`/`latest_rank`, and latest engagement snapshots (`views_count`, `likes_count`, ...), which are the inputs to discoverability and share of voice. See `references/socialseal-data-contract.md` for column semantics.

MCP-first:

```text
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "body": { "reportType": "search_results_enriched", "format": "csv", "payload": { "groupIds": [<group-id>] } }
}
```

Legacy fallback (same data family, time-window CSV):

```text
socialseal_export_tracking_data {
  "workspaceId": "<workspace-id>",
  "body": { "groupId": <group-id>, "timePeriod": "30d" }
}
```

Completeness check before movement claims:

```text
socialseal_get_tracking_group_completeness {
  "workspaceId": "<workspace-id>",
  "group_id": <group-id>
}
```

CLI equivalents:

```bash
npx -y @socialseal/cli data export-search-results --group-ids <group-id> --workspace-id <workspace-id> --out ./exports/search.csv
npx -y @socialseal/cli data export-group-evidence --group-id <group-id> --workspace-id <workspace-id> --out ./exports/evidence.csv
npx -y @socialseal/cli data export-tracking --group-id <group-id> --time-period 30d --workspace-id <workspace-id> --out ./exports/tracking.csv
npx -y @socialseal/cli data group-completeness --help
```

If an export is too large for context, save it to a file and analyze it in chunks (or use the paginated export-artifact read), never silently drop rows. See `references/mcp-and-cli-usage.md`.

## Workflow

### Part A — Measure a snapshot (brand vs competitor)

1. **Confirm scope.** Workspace, platform, market, language, keyword set, date range. If the user did not give a group ID, locate the tracking group first: list groups (`group-management` action `list`), pick the one matching platform + market + keyword topic, and confirm it covers the user's keywords before exporting.
2. **Export ranked rows.** Use `search_results_enriched` (MCP) or `export-search-results` (CLI) for the group. If the user named exact keywords that are not tracked as items, map each to the nearest tracked item and say so explicitly; offer to add the literal terms and refresh as a follow-up.
3. **Qualify rows.** Drop wrong market/language/topic, non-comparable account types, and duplicate rows before any percentage.
4. **Tag entities.** Owned brand, competitor, creator/affiliate/partner, irrelevant/noise. Use the owned-handle list; when in doubt tag conservatively.
5. **Compute metrics.** Keyword coverage, discoverability, share of voice (rank-weighted and/or views-weighted), best rank. See "Metrics & last-mile computation".
6. **Report with tables and a chart.** See Output.

### Part B — Track over time (movement)

1. **Run exports** for current and previous periods with identical scope.
2. **Check completeness.** Compare expected groups/items with actual outputs (`group-management` `completeness` action or `data group-completeness`).
3. **Compare denominators.** Do not compare percentages if keyword sets changed without noting the break.
4. **Flag anomalies.** Sudden zeros, missing platforms, duplicate rows, missing media IDs, impossible spikes, or date gaps.
5. **Log changes.** Group membership edits, keyword additions/removals, platform changes, and export failures.
6. **Prepare tracker update.** Status, movement, anomalies, and next refresh date.

**Real change vs measurement:** a genuine measurement is exact, so true movement reflects a changing search reality, not noise; do not dismiss it. A data failure (empty export, missing identifiers, keyword-set change) is different and must be ruled out first. See `references/evidence-and-confidence.md`.

## Metrics & last-mile computation

Definitions (see `references/metrics-glossary.md`):

- **Discoverability:** how often a brand, competitor, creator type, or content pattern appears across the selected keyword set and platform scope.
- **Keyword coverage:** share of tracked keywords where the entity appears (entity keywords ÷ total tracked keywords). This is the primary "did we show up" metric and is always computable.
- **Share of voice (SOV):** qualified surfaced attention for an entity ÷ total qualified surfaced attention in the same scope.
- **Best rank:** the highest position (lowest rank number) the entity reaches across the set.

Deriving surfaced attention for SOV (from real export fields, never invented):

- **Rank-weighted:** sum over the entity's qualified rows of `1 / rank` (or position buckets), divided by the same sum over all qualified rows. Higher rank = more surfaced attention.
- **Views-weighted:** sum of the entity's surfaced `views_count` snapshots ÷ total surfaced `views_count` in the scope.
- State the weighting rule and the denominator with every SOV number.
- When rank or views are missing, fall back to keyword coverage and say so — never present a share-of-voice number you cannot ground.

Always state platform, market, language, keyword set, date range, and denominator alongside any percentage. Cite evidence in human-readable terms: `"keyword" [market, platform]`, video title/URL, `@author_handle`, group name; keep `video_uid`/`search_result_id` as an internal traceability note only.

### Worked example (illustrative numbers)

A snapshot export for 15 tracked keywords returns 209 qualified ranked rows. Tagging finds the owned brand in 9 rows and one competitor in 12 rows; the rest are creators/others.

- Raw rows are not the metric: report coverage and SOV, not just "12 vs 9 appearances".
- **Keyword coverage:** owned appears in 6 of 15 keywords = 40%; competitor in 8 of 15 = 53%.
- **Rank-weighted SOV:** `sum(1/rank)` = owned 1.84, competitor 2.10, all qualified rows 7.5 → owned 24.5%, competitor 28.0%, creators/others 47.5%.
- **Views-weighted SOV:** owned surfaced views 0.41M ÷ 2.1M total = 19.5%; competitor 0.63M ÷ 2.1M = 30.0%.
- **Best rank:** owned #1, competitor #5.

Four numbers tell the story: coverage (did we show up), rank-weighted SOV (how prominently), views-weighted SOV (how much attention surfaced rows carry), best rank (single best placement). Report all four; lead with percentages, not row counts.

## Output

A discoverability / share-of-voice readout:

1. **Scope and data note.** Platform, market, language, keyword set, date range, denominator, export freshness, and the keyword-mapping caveat if the user's exact terms were not tracked.
2. **Metric table (required).** Per entity (owned, each competitor): appearances, keywords covered (x of y), keyword coverage %, rank-weighted SOV %, views-weighted SOV %, best rank.
3. **Per-keyword presence table (required).** Keyword (`"keyword" [market, platform]`), which entities appear, and best rank per entity.
4. **Chart (required).** Render the SOV and coverage numbers graphically — use the `dataviz` skill (or Python/matplotlib, altair, or a supported chart tool) to produce e.g. a grouped bar chart of SOV by entity (rank-weighted vs views-weighted) and/or a keyword × entity presence heatmap. Attach the chart image when the client supports attachments; if a chart is impossible, say why.
5. **Findings.** What the numbers mean (who leads coverage, who leads prominence, affiliate/creator patterns if relevant), with 1-3 example videos cited by title/URL, `@handle`, and `"keyword" [market, platform]`.
6. **Caveats.** Selection bias: figures describe "what surfaces for these tracked queries in this scope," not total market demand. Movement claims need completeness checks and comparable denominators.
7. **Next actions (optional).** Keep measurement distinct from content recommendations; offer to refresh, add missing exact keywords, or trend over time.

## Do / Don't

Do:

- always compute and report keyword coverage and share of voice with denominators; lead with percentages, not raw row counts
- state the weighting rule (rank and/or views) with every SOV number
- produce the metric table and a chart; invoke the `dataviz` skill
- cite evidence as `"keyword" [market, platform]`, video title/URL, `@handle`, group name
- save raw exports by date and keep a manifest of expected groups/items
- flag comparison breaks and distinguish data failure from real visibility movement
- when the user names exact keywords not tracked, map to the nearest tracked items and say so, or offer to add and refresh

Don't:

- answer a discoverability/SOV question with only a narrative of which videos appeared
- treat empty files as real zeros, or compare periods after keyword edits without a caveat
- overwrite raw exports or report movement before checking completeness
- present a share-of-voice number without a denominator or weighting rule
- extrapolate scoped statistics to whole-market demand

## Troubleshooting

- Header-only export: check group completeness and refresh status.
- Missing identifiers: refresh enriched results (`search_results_enriched`) or use group evidence.
- Unexpected zero: compare against the previous raw export and check date filters.
- Duplicate rows: dedupe at the correct grain before calculating percentages.
- Export too large for context: save to a file and analyze in chunks; do not drop rows silently.
- User's exact keywords are not tracked items: map to nearest tracked items with a caveat, then offer to add the literal terms and refresh.

## Verification Checklist

- [ ] Scope and denominators stated (platform, market, language, keyword set, date range).
- [ ] Keyword coverage computed per entity (x of y keywords).
- [ ] Share of voice computed with an explicit weighting rule (rank and/or views) or an explicit fallback to coverage.
- [ ] Metric table and per-keyword presence table present.
- [ ] A chart was produced (dataviz / python) or a clear reason was given why not.
- [ ] Completeness and anomaly checks were run for any movement claim.
- [ ] Change log updated and next refresh date set.
