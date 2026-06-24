# SocialSeal Data Contract

Skills can work from MCP responses, CLI exports, or CSV/JSON files. Before analysis, inspect available fields and identify:

- workspace or project scope
- tracking group or keyword set
- platform
- market/language
- date range
- keyword/topic
- result URL or media identifier
- account/creator/entity name
- owned vs creator vs competitor classification when available
- views or surfaced attention metric when available
- rank or position when available

If a required field is missing, either ask for the missing export or downgrade the claim.

## Enriched ranked search export columns

`export-search-results` (CLI) and `search_results_enriched` (report export) return enriched ranked rows. Cite these fields directly for attribution rather than vague "row references":

- `search_result_id`: stable id of the ranked search row. Use it to cite a specific surfaced result.
- `video_uid`: canonical SocialSeal video id. Use it to tie evidence to a video and to `tracked-video-extract` / blueprint exemplars.
- `platform_video_id`: platform-native video id.
- `keyword`, `region`, `language`, `platform_id`: scope of the surfaced result.
- `rank` / position: where the result surfaced for that keyword. Use for share-of-voice and discoverability, not raw counts.
- latest metrics (`views_count`, `likes_count`, `comments_count`, `shares_count`, `saves_count`): the most recent engagement snapshot.

## Timestamp semantics (avoid misattribution)

- `search_timestamp`: when SocialSeal captured that ranked search row.
- `latest_metrics_ts`: when the latest exported engagement metrics snapshot was captured.
- `published_at`: platform publish/upload time when available; blank if unavailable.
- `observed_at`: when SocialSeal first observed/ingested the video record when available; blank if unavailable.
- `first_seen_at` / `last_seen_at`: earliest/latest `search_timestamp` for the video within the exported scope.

Attribution rule: when `published_at` is blank, do NOT make platform-age or recency claims about the video. Use `first_seen_at` / `last_seen_at` only for "resurfacing in tracked search" language. Never infer how old a video is from when SocialSeal first saw it.

## Group evidence export

`export-group-evidence` routes social groups and Google AI groups to the correct CSV shape automatically. Prefer it when you need a single safe evidence export across mixed group types, or when enriched search rows are missing identifiers.

## Citing evidence

- Prefer `search_result_id` or `video_uid` plus the `keyword` and `rank` when citing a surfaced result.
- State the denominator and scope (platform, market, language, keyword set, date range) alongside any percentage.
- Label evidence as metadata-only when you have titles/captions but no viewed analysis.
