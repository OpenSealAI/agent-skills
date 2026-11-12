# SocialSeal Data Contract

Skills can work from MCP responses or supplied CSV/JSON exports. Before analysis, inspect available fields and identify:

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

## Human-readable attribution (default for anything a person reads)

When you cite evidence in a deliverable, a quote, or a recommendation, use concepts the user already understands. Never make the user decode an internal id.

Cite the **query** as the keyword plus its market and platform:

- `"best hotel in NYC" [US, TikTok]` — not "search row 23" or "tracking_item_id 5417".

Cite the **video** by its title, linked to its public URL, and the creator handle:

- `["3 mistakes first-timers make in Tokyo"](<video_url>) by @creator` — not `video_uid abc...` or `search_result_id 8842`.

Cite the **group/scope** by its name:

- `TikTok / US / category searches` — not the numeric group id.

These map directly to enriched export columns:

| Display this | From column | Notes |
| --- | --- | --- |
| the query | `keyword` + `region` + platform | platform from the group/scope; in raw rows `platform_id` 1=TikTok, 2=Instagram, 3=YouTube |
| the video | `title` linked to `video_url` | use the URL as the text when there is no title |
| the creator | `author_handle` linked to the creator's profile URL | render with a leading `@` |
| watch link | `video_url` | constructed when not stored directly |
| the group | `tracking_group_names` / `tracking_item_name` | human names, not numeric ids |
| where it ranked | `rank` / `best_rank` / `latest_rank` | "ranked #3 for ..." |

## Machine ids (internal / traceability only)

`search_result_id`, `video_uid`, `platform_video_id`, numeric `group_id`/`tracking_item_id`, `studyRef`, `clipId`, `assetId`, and share tokens are needed for tool calls, joins, dedupe, and follow-up extraction. Keep them, but treat them as an **optional internal traceability note**, not the user-facing citation. Do not lead a sentence a human reads with an id. If a traceability column is useful in a table, label it clearly (e.g. a final `ref (video_uid)` column) and keep the human-readable citation primary. Never put literal ids/tokens in shared or public artifacts; use placeholders.

## Enriched ranked search export columns

`socialseal_export_report` with `reportType: "search_results_enriched"` return enriched ranked rows. Human-readable fields for citation:

- `keyword`, `region`, `language`, `platform_id`: the query and its scope.
- `title`, `description`: the video's human title and caption.
- `author_handle`: the creator handle.
- `video_url`, `thumbnail_url`: links for the human.
- `tracking_group_names`, `tracking_item_name`: human group/item names.
- `rank` / `best_rank` / `latest_rank`: where it surfaced. Use for share-of-voice and discoverability, not raw counts.
- latest metrics (`views_count`, `likes_count`, `comments_count`, `shares_count`, `saves_count`): the most recent engagement snapshot.

Traceability fields (keep, do not display as the citation): `search_result_id`, `video_uid`, `platform_video_id`, `tracking_item_id`, `tracking_group_ids`, `user_id`, `deepdive_id`.

## Timestamp semantics (avoid misattribution)

- `search_timestamp`: when SocialSeal captured that ranked search row.
- `latest_metrics_ts`: when the latest exported engagement metrics snapshot was captured.
- `published_at`: platform publish/upload time when available; blank if unavailable.
- `observed_at`: when SocialSeal first observed/ingested the video record when available; blank if unavailable.
- `first_seen_at` / `last_seen_at`: earliest/latest `search_timestamp` for the video within the exported scope.

Attribution rule: when `published_at` is blank, do NOT make platform-age or recency claims about the video. Use `first_seen_at` / `last_seen_at` only for "resurfacing in tracked search" language. Never infer how old a video is from when SocialSeal first saw it.

## Group evidence export

`export-group-evidence` routes social groups and Google AI groups to the correct CSV shape automatically. Prefer it when you need a single safe evidence export across mixed group types, or when enriched search rows are missing identifiers.

## Public links for every example

Every claim about a specific video, creator or competitor account carries the public URL the tool returns for it (`video_url`, the profile or account URL, the Study's source URL). A reader opens the link and sees the same video or account.

- Put the link beside the claim: inline in a sentence, one link per row in a table or matrix. Each video, creator or account named in an example table has a link in that row.
- Use the URL exactly as the tool returned it.
- When the data for an item carries no URL, write the source in that spot, for example `source: workspace data, no public link`, and keep the claim at the level the data supports. A named item with neither a link nor a source note is incomplete.
- Link each video or account where its claim is made; a summary line that restates a claim already cited needs no second link.

## Citing evidence

- Default display: the human-readable citation (`"keyword" [market, platform]`, video title linked to its URL, `@handle` linked to the profile, group name, rank).
- State the denominator and scope (platform, market, language, keyword set, date range) alongside any percentage.
- Keep `video_uid`/`search_result_id` as an internal traceability note for follow-up tool calls, not as the quote.
- Label evidence as metadata-only when you have titles/captions but no viewed analysis.
- Be explicit about which tier of evidence a claim rests on; see `evidence-and-confidence.md`.
