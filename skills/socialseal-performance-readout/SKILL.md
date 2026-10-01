---
name: socialseal-performance-readout
description: Use this skill when the user asks how posted content, a campaign, a
  creator programme, or a content period performed in SocialSeal; what changed after
  publishing; or what the latest results mean. Produce a scoped readout with metrics,
  examples, interpretation, caveats, and next actions without claiming unsupported
  causality.
license: MIT
metadata:
  socialseal:
    phase: measurement
  tags:
  - socialseal
  - measurement
  - performance-readout
  - reporting
  - metrics
---

# SocialSeal Performance Readout

## Overview

A SocialSeal performance readout explains what changed in discoverability and what to do next. It should connect posted content and tracked keywords without pretending SocialSeal data is a complete view of every platform interaction.

## Inputs

- current and comparison SocialSeal exports
- list of posted content during the period
- tracking group IDs and keyword/topic scope
- previous objectives or content plan
- optional platform-native metrics

## Data Access

```text
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "reportType": "search_results_enriched", "format": "csv",
  "payload": { "groupIds": [<group-id>] }
}
```

Use `socialseal_export_tracking_data` for a group/item time-window export. For Google AI evidence, use the named results read and retain its actual coverage. See `references/mcp-and-cli-usage.md`.

Attribution: cite movement in human-readable terms, the `"keyword" [market, platform]`, the video title/URL, `@author_handle`, and where it ranked; keep `video_uid`/`search_result_id` as an internal traceability note. Use `first_seen_at`/`last_seen_at` for resurfacing language and never infer platform age when `published_at` is blank. See `references/socialseal-data-contract.md`.

Evidence tiers: movement in discoverability/coverage/SOV is a hard observation, not a noisy estimate; attribute day-to-day change to a shifting search reality, not measurement error. But the figures are scoped to high-ranking videos for the tracked queries, so do not generalize past that scope. See `references/evidence-and-confidence.md`.

## Workflow

1. **State scope.** Platform, market, language, tracking group, keyword set, date range, and comparison period.
2. **Validate data.** Check rows, columns, date range, missing identifiers, and whether the export is social or Google AI evidence.
3. **Calculate metrics.** Keyword coverage, discoverability by topic, SOV where qualified attention exists, owned/creator split, competitor/entity changes.
4. **Connect to content.** Map posted content to tracked topics carefully. Use “consistent with” unless causality is established.
5. **Explain examples.** Include examples that show why a metric moved or why a gap remains.
6. **Write next actions.** Continue, adjust, add, pause, or investigate.

## Output

- scope and data note
- metric snapshot
- changes vs previous period
- examples and interpretation
- caveats
- next actions

Use `templates/measurement-readout-template.md` when a simple report format is needed.

## Do / Don't

Do:

- show denominators and comparison periods
- separate owned and creator content
- call out missing data clearly
- make recommendations specific enough to brief

Don't:

- lead with raw row counts or internal IDs
- claim causality from timing alone
- treat a hard measurement's day-to-day variation as noise
- generalize a scoped statistic to the whole platform/market
- hide export freshness or scope
- overload management audiences with every table

## Troubleshooting

- If IDs are missing, use group evidence or refresh enriched search results.
- If current and previous groups differ, state that comparison is directional only.
- If platform-native metrics conflict with SocialSeal signals, explain that they measure different surfaces.

## Verification Checklist

- [ ] Scope and data freshness are stated.
- [ ] Metrics use percentages/denominators where relevant.
- [ ] Examples support interpretation.
- [ ] Recommendations are concrete.
- [ ] Caveats are visible.
