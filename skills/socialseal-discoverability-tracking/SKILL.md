---
name: socialseal-discoverability-tracking
description: Use this skill when refreshing, comparing, or maintaining SocialSeal
  discoverability tracking over time. It checks export completeness, anomaly patterns,
  denominator consistency, and tracking changes before reporting movement.
license: MIT
metadata:
  socialseal:
    phase: measurement
  tags:
  - socialseal
  - measurement
  - tracking
  - refresh
  - anomaly-check
---

# SocialSeal Discoverability Tracking

## Overview

Discoverability tracking is the operating rhythm after setup: refresh exports, compare like with like, detect tracking/data problems, and keep a change log so trends remain interpretable.

## Inputs

- workspace ID and group IDs
- refresh cadence
- current export and previous export
- tracking-group change log
- expected keyword/group manifest

## Workflow

1. **Confirm scope.** Same workspace, group IDs, platform, market, keyword set, and date range.
2. **Run exports.** Use `export-group-evidence` for group-level evidence and `export-search-results` for ranked rows.
3. **Check completeness.** Compare expected groups and items with actual outputs. Use `data group-completeness` or `group-management` completeness if available.
4. **Compare denominators.** Do not compare percentages if keyword sets changed without noting the break.
5. **Flag anomalies.** Sudden zeros, missing platforms, duplicate rows, missing media IDs, impossible spikes, or date gaps.
6. **Log changes.** Record group membership edits, keyword additions/removals, platform changes, and export failures.
7. **Prepare tracker update.** Status, movement, anomalies, and next refresh date.

## Useful CLI Commands

```bash
npx -y @socialseal/cli data export-options
npx -y @socialseal/cli data export-group-evidence --group-id <group-id> --workspace-id <workspace-id> --out ./exports/evidence.csv
npx -y @socialseal/cli data export-search-results --group-ids <group-id> --workspace-id <workspace-id> --out ./exports/search.csv
npx -y @socialseal/cli data group-completeness --help
```

MCP-first: the same exports run via `socialseal_export_report` (`reportType: "search_results_enriched"`) and `socialseal_export_tracking_data`; check completeness with the `group-management` `completeness` action through `socialseal_call_tool`. See `references/mcp-and-cli-usage.md`. Compare like with like using `search_timestamp` and the timestamp rules in `references/socialseal-data-contract.md`. Cite anomalies and movement by group name and `"keyword" [market, platform]`, not numeric ids.

Real change vs measurement: a genuine measurement is exact, so true movement reflects a changing search reality, not noise; do not dismiss it. A data failure (empty export, missing identifiers, keyword-set change) is different and must be ruled out first. See `references/evidence-and-confidence.md`.

## Output

- tracker status update
- anomaly log
- denominator/comparability note
- change log entry
- next refresh plan

## Do / Don't

Do:

- save raw exports by date
- keep a manifest of expected groups/items
- flag comparison breaks
- distinguish data failure from real visibility movement

Don't:

- treat empty files as real zeros
- compare periods after keyword edits without a caveat
- overwrite raw exports
- report movement before checking completeness

## Troubleshooting

- Header-only export: check group completeness and refresh status.
- Missing identifiers: switch export type or refresh enriched results.
- Unexpected zero: compare against previous raw export and check date filters.
- Duplicate rows: dedupe at the correct grain before calculating percentages.

## Verification Checklist

- [ ] Current and previous scope are comparable or caveated.
- [ ] Raw exports are saved.
- [ ] Completeness and anomaly checks were run.
- [ ] Change log was updated.
- [ ] Next refresh date is set.

