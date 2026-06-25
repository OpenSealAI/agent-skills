---
name: socialseal-bilingual-demand-monitoring
description: >-
  Use this skill when monitoring search demand across a local language and English
  for the same market, so micro-trends are caught early in whichever language they
  start. Maps the explicit local-vs-English split using language-clean tracking
  groups and per-keyword English glosses, compares discoverability movement across
  the split over time, and flags emerging queries to track or brief.
license: MIT
metadata:
  socialseal:
    phase: measurement
  tags:
    - socialseal
    - measurement
    - bilingual
    - demand-monitoring
    - micro-trends
    - localization
---

# SocialSeal Bilingual Trend and Demand Monitoring

## Overview

In many markets a trend starts in the local language before it appears in English (or vice versa). If you only watch one language you see the trend late. This skill maps the **explicit split between local-language and English search demand** for the same market and platform, then compares movement across that split over time so an emerging micro-trend is caught in whichever language it begins.

The unit of comparison is two (or more) language-clean tracking surfaces for the same market and intent: one local-language group and one English group. SocialSeal keeps discoverability trustworthy only when each group is one platform, one market/language context, and one coherent intent (see `references/strategy-foundations.md`). This skill compares across those clean surfaces; it does not mix languages inside one group.

## When to Use

- Standing up or maintaining paired local-language and English monitoring for a market.
- Detecting emerging keywords/queries early in either language.
- Comparing discoverability or surfaced attention between the local-language and English split.
- Bridging local queries to English (and back) so a trend spotted in one language can be briefed in the other.

Route group creation to `socialseal-tracking-group-design`, opportunity sizing to `socialseal-opportunity-analysis`, and ongoing tracking hygiene to `socialseal-discoverability-tracking`.

## The bilingual split, concretely

A single market group can contain a real language mix. For example, one Malaysia route group held both Chinese queries (`直飞福冈`, `深圳机票`) and Malay/English queries (`penerbangan kl fukuoka`, `direct flight kl fukuoka`). Monitoring is only trustworthy when the two languages are separated into clean groups and compared, not averaged inside one group.

Two ways to establish the split:

1. **Language-clean groups (preferred).** One group per language for the same market/intent, e.g. `TikTok / MY / routes / local-language` and `TikTok / MY / routes / english`. Discoverability and share of voice are then comparable across the split.
2. **Language tagging within an export.** When existing rows mix languages, derive language per keyword. The enriched `language` column is sometimes blank at row level; fall back to detecting script/terms in the `keyword` field, or to per-keyword English glosses from a search journey (`englishGloss`, `canonicalKeyword`, `language`), and say which method you used.

## Inputs

Required:
- workspace id (or a configured default)
- target market (region) and the local language(s) plus English
- the shared intent (e.g. a route, destination, or category)
- tracking group ids per language, or an export covering the market

Good to have:
- seed keywords in each language
- a previous-period export per language for comparison
- platform priority

## Data Access

Compare language-clean groups by exporting each and reading discoverability movement.

CLI:

```bash
# enriched ranked rows per language-clean group
npx -y @socialseal/cli data export-search-results --group-ids <local-lang-group-id> --workspace-id <workspace-id> --out ./exports/local.csv --timeout 120000
npx -y @socialseal/cli data export-search-results --group-ids <english-group-id> --workspace-id <workspace-id> --out ./exports/english.csv --timeout 120000

# tracking movement over a window per group
npx -y @socialseal/cli data export-tracking --group-id <local-lang-group-id> --time-period 30d --workspace-id <workspace-id> --out ./exports/local-30d.csv
npx -y @socialseal/cli data export-tracking --group-id <english-group-id> --time-period 30d --workspace-id <workspace-id> --out ./exports/english-30d.csv
```

MCP-first:

```text
socialseal_export_report { "workspaceId": "<workspace-id>", "body": { "reportType": "search_results_enriched", "format": "csv", "payload": { "groupIds": [<group-id>] } } }
socialseal_export_tracking_data { "workspaceId": "<workspace-id>", "body": { "groupId": <group-id>, "timePeriod": "30d" } }
```

Bridge languages with a search journey. It returns staged keywords each carrying `language`, `englishGloss`, and `canonicalKeyword`, which is the explicit local-to-English map you can use to find the English equivalent of a local trend (and discover gaps):

```text
socialseal_call_tool {
  "toolName": "search-journey-run",
  "workspaceId": "<workspace-id>",
  "body": { "subject": "<route or topic>", "subjectType": "topic", "region": "<region>", "locale": "<locale>", "seedKeywords": ["<local-language seed>", "<english seed>"], "maxKeywords": 30, "executionMode": "async" }
}
```

Heavy journeys can time out synchronously; start with `executionMode: "async"` and poll:

```text
socialseal_get_tool_status { "id": "<run-uuid>", "kind": "journey_run" }
```

CLI equivalent: `npx -y @socialseal/cli tools call --function search-journey-run --async --body @journey.json --workspace-id <workspace-id>` then `tools status <run-uuid> --kind journey_run`.

## Workflow

1. **Confirm the split.** Identify the market, the local language(s), English, and the shared intent. Confirm there is a clean group per language, or plan them via `socialseal-tracking-group-design`.
2. **Export each language surface** (enriched rows + tracking window) and inspect columns, grain, and date range.
3. **Establish language per keyword.** Use the group's language when groups are clean; otherwise tag each `keyword` by script/terms or by journey `language`/`englishGloss`. State the method.
4. **Compute discoverability per language** within each surface's own denominator: keyword coverage, owned-vs-creator split, and rank-weighted surfaced attention. Never average across languages into one number; keep them side by side.
5. **Compare movement over time.** For each language surface compare the current window to the prior one using consistent denominators. Note any keyword-set changes (those make comparisons directional only).
6. **Detect micro-trends early.** Flag keywords that are newly surfacing, climbing rank fast, or newly drawing creator content in either language. A query rising in the local language with no English equivalent tracked yet is an early signal; map it via `englishGloss` and propose tracking the English form (and vice versa).
7. **Bridge and recommend.** For each early signal, give the local term, its English gloss, where it is moving, and the recommended action: add to tracking, brief content, or watch. Keep the two languages explicitly labeled throughout.

## Output

A bilingual monitoring readout:

- a side-by-side panel: local-language vs English, each with its own discoverability/coverage and denominator
- movement per language vs the prior window (with capture dates)
- an early-signal list: emerging/climbing keywords per language, with the cross-language gloss and whether the other language tracks it yet
- recommended actions per signal: track, brief, or watch
- explicit scope and caveats (platform, market, languages, keyword sets, date ranges)

## Do / Don't

Do:
- keep the two languages as separate, clearly labeled surfaces with their own denominators
- state which method established the language of each keyword
- use `englishGloss`/`canonicalKeyword` to bridge a local trend to its English equivalent and vice versa
- treat discoverability movement as a hard observation of a changing search reality, with capture dates

Don't:
- mix languages inside one tracking group or average them into one figure
- infer total market demand in a language from surfaced results (selection bias; scoped only)
- claim a micro-trend is real off a single row; require multiple surfacing keywords or a clear rank climb
- compare across periods when the keyword set changed without flagging it as directional

## Troubleshooting

- `language` column blank: derive from the `keyword` text or journey `language`; if a group mixes languages, split it via `socialseal-tracking-group-design` before trusting comparisons.
- Synchronous `search-journey-run` returns 504: re-run with `executionMode: "async"` and poll `journey_run`.
- No English equivalent surfaces for a local trend: that is the early-signal case; propose tracking the `englishGloss` form, do not assume absence of demand.
- Denominators differ a lot between languages: report each language in its own scope; do not normalize away a real size difference.

## Verification Checklist

- [ ] Each language is a clean, separately labeled surface with its own denominator.
- [ ] The language-tagging method is stated.
- [ ] Movement is compared per language with capture dates and keyword-set notes.
- [ ] Early signals include the cross-language gloss and whether the other language tracks it.
- [ ] Selection-bias scope is stated; no whole-market demand claims.
