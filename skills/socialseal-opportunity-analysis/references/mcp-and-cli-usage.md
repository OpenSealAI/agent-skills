# SocialSeal MCP and File-Mode Usage

MCP is the supported agent interface. Use the connected hosted server in Cowork
and Claude Code. Do not direct users to install or use the
retired standalone SocialSeal CLI. The historical filename of this reference is
retained for existing skill links.

## Discover access and direct actions

Use the host's available tool search/discovery facilities before concluding that a connector is missing. Tools can be loaded lazily. If discovery or connection status confirms missing access, use `onboarding-and-auth.md`; do not diagnose disconnection from an empty initial tool list or one failed action.

Use `socialseal_get_current_workspace` or `socialseal_list_workspaces` when workspace context is needed. Reuse the authorized, unambiguous context already available. Ask only when an operation requires context that remains ambiguous. An account read does not imply tracking setup; an absent brand does not block account metrics.

An unsupported platform, missing argument, missing evidence, authorization denial, and provider failure are different limitations. Preserve useful completed portions of compound requests. A stale skill or unavailable action does not authorize a search-only substitute or a resolver rephrase loop.

## Direct actions

Select the action matching the supplied target and requested deliverable from the live catalogue. Its description and schema state platforms, inputs, side effects, evidence/freshness limits, collection costs, and continuation. Use the actual schema rather than inventing parameters from a remembered name.

- Existing tracking groups: read the existing authorized group. Do not create groups or run collection to answer a read.
- Supplied video URL: start a one-video Study with that URL (`socialseal_start_study`, subject `{ "kind": "videos", "urls": ["<video-url>"] }`), then read it with `socialseal_get_study`. Apply the Study's price/approval boundary if new Video DNA is needed.
- Named creator: read the profile and recent account posts with the requested platform/count. Timeline ordering, pinned posts, mixed media, timestamp provenance, and pagination determine whether a latest-post claim is supported. Return the service's aggregates and denominators; missing values remain distinct from zero. Retrieve accessible brand context independently for fit evaluation.
- Ranked-search creator discovery: use the requested ranked-search population and retain its sampling caveats. It is not a substitute for account posts.
- Account tracking: only create the explicitly requested ongoing commitment, retaining required authorization.

Load individually named operations through host tool search. An unavailable action
is a specific capability limitation; it does not authorise a backend-selector fallback.

Named-account examples (Instagram currently):

```text
socialseal_get_creator_profile { "target": "<profile-url-or-handle>", "platform": "instagram" }
socialseal_get_creator_recent_posts { "target": "<profile-url-or-handle>", "platform": "instagram", "recentPostCount": 5, "freshness": "stored" }
```

Creator reads use stored snapshots. A fresh request returns `FRESH_COLLECTION_REQUIRED` with any usable evidence. For requested fresh collection, confirm which workspace pays, then call `socialseal_collect_account` with the target, `platform` (`instagram` or `tiktok`), explicit `workspaceId` and `idempotencyKey`. Instagram takes an optional `recentPostCount`; TikTok requires a publication window (`startAt`, `endAt`) and `maxProviderRequests`. Send `quoteOnly: true` first to show the price and the paying workspace (`paidBy`). This creates a one-off collection receipt, never a tracker. Reuse the key after timeouts. Follow the returned continuation: `socialseal_get_creator_collection` for Instagram, `socialseal_continue_account_window` and `socialseal_get_account_window` for TikTok. Terminal failed receipts do not automatically retry. Preserve partial coverage and `coverage.latestClaim`.

## Discover the action for the job

Use a named action directly when its schema is already available. Otherwise use
the host's tool search to load the matching operation and its live input schema.
Discovery and skills are references, not mandatory gates for every read or edit.

- Content calendars and posting schedules: `socialseal-social-plan-builder` guides composition and revision; do not assume a calendar-generation tool.
- New video/editor/UGC briefs: `socialseal_generate_brief` with a Study revision's `studyContext`. Without a usable Study it returns `study_needed` with Study subjects to offer the user; start the chosen one with `socialseal_start_study`, then retry.
- Existing brief: `socialseal_get_brief`, `socialseal_update_brief`, `socialseal_export_brief`. A formatting or copy edit does not need new evidence collection.
- Tracking setup: `socialseal_create_tracking_group`, `socialseal_add_tracking_group_items`, then `socialseal_get_tracking_group_completeness`. Read existing groups before proposing setup.
- Demand signals: read what the workspace already holds before collecting more: `socialseal_list_keywords` (`demandSignals`, `seoMetrics`, autocomplete `sources`), Explore snapshots via `socialseal_explore_get` (`relativeDemand`), and tracked-query results. Compare candidate wordings, hooks or titles with `socialseal_check_keyword_demand` (free autocomplete check plus stored volume). Expand or validate keyword candidates with `socialseal_start_search_journey` and `socialseal_get_search_journey_run`. Google AI uses `socialseal_start_google_ai_search`, `socialseal_list_google_ai_search_runs`, and `socialseal_get_google_ai_search_results`. Rank candidates with whatever signals exist; see "Relative demand" in `evidence-and-confidence.md`.
- Understanding videos (one or many), a topic, competitor or creator: `socialseal_start_study`, then `socialseal_get_study`. Source-video frames and assets: `socialseal_extract_video_assets` with stored identifiers.

Inspect the exact live input schema before an unfamiliar mutation. Arguments go
directly on the named action, without a backend-function selector or body envelope:

```text
socialseal_generate_brief {
  "workspaceId": "<workspace-id>",
  "opportunityKey": "<opportunity-key>",
  "studyContext": { "studyRef": "<study-ref>", "revision": 2, "findingId": "action" }
}
```

If host discovery confirms an action is unavailable, report that precise limitation
and preserve completed work. Preserve backend authorisation, admission and funding
controls; tool discovery is not approval for additional paid work.

## Studies and paid Video DNA

`socialseal_start_study` starts or reuses a Study free. Every call carries an
`idempotencyKey`: generate one per intended request and keep it from the price
request through approval, top-ups, timeouts and retries; a new key starts new
billable work. Video DNA for videos that lack it is priced first and returns
`approval_required` with the price; nothing runs. After the user approves, resend
with the approved amount and the same key:

```text
socialseal_start_study {
  "workspaceId": "<workspace-id>",
  "subject": { "kind": "videos", "urls": ["<video-url>"] },
  "maxCostUsd": "<approved-usd-price>",
  "idempotencyKey": "<stable-request-key>"
}
```

A subscription workspace sends `approvedCredits` instead of `maxCostUsd`. Other
statuses: `ready` (nothing to approve), `price_changed` (nothing ran; see below),
`funding_required` (share the returned funding link and keep its `operationId`),
`enriching` (poll `socialseal_get_study`). Keep the key for timeouts, uncertain
outcomes and retries of the unchanged request. A wallet `price_changed` carries no
price: request a fresh quote without approval fields, get approval for the returned
price, then resend with it and a new `idempotencyKey`. A subscription
`price_changed` carries the new credit price to approve; follow its `nextStep`.
When the completed Study returns `briefContext`, pass it as `studyContext` to the
brief tools; without one it has no briefable finding.

## Explore acquisition preview and start

When Explore is released for the authorized workspace, load
`socialseal_explore_preview_start` and `socialseal_explore_start` through host tool
search. Call the preview with the same workspace, canonical anchor, market,
language and provider basket that will be used for start:

```text
socialseal_explore_preview_start {
  "workspaceId": "<workspace-id>",
  "anchor": { "anchorKind": "search_term", "subjectId": "<subject-id>" },
  "marketCode": "US", "languageTag": "en", "providerBasket": []
}
socialseal_explore_start {
  "workspaceId": "<workspace-id>",
  "anchor": { "anchorKind": "search_term", "subjectId": "<subject-id>" },
  "marketCode": "US", "languageTag": "en", "providerBasket": [],
  "previewFingerprint": "<returned-planFingerprint>",
  "idempotencyKey": "<stable-request-key>"
}
```

Read the preview's source availability, estimated credits, capacity and blocking
reasons. It does not collect provider evidence or create a lineage. Pass the
returned `startLineagePreview.planFingerprint` as `previewFingerprint` without
inventing a fingerprint or probing start for an error. Ordinary approved plans
need no additional user confirmation. Only when `confirmationRequired` is true,
obtain the user's scope confirmation and echo that plan fingerprint as
`confirmedScopeFingerprint`, retaining the same retry key. If the plan is stale,
read a fresh preview for the intended scope; if blocked, preserve the blocker.
Retain the returned lineage/run identity and poll with `socialseal_explore_get`
(`resource: "run"`, `runId`, workspace); do not restart collection to poll. If
preview or start is unavailable after host discovery, report that exact capability
limitation and preserve completed work.

When a snapshot exists, read `diagnostics.relativeDemand.terms[]`. `index` (0-100)
ranks terms within that snapshot. A null `index`, a term state of
`insufficient_evidence` or `partial`, or a snapshot `indexState` of `thin` means the
calibrated composite was gated, not that demand is unknown. Use the snapshot's
`signalRanking`, which orders terms by their observed components (`googleDemand`,
`recommendationSalience`, `searchResultResponse`, `searchResultEngagement`) and
labels each `evidenceLevel`. `socialseal_explore_list` returns a summary view; read
one snapshot with `socialseal_explore_get` for the full components and evidence.

## Workspace and identity

Use the workspace the user named. For an unnamed workspace, resolve
`socialseal_get_current_workspace`; never infer the default from list order or
ownership. Use `socialseal_list_workspaces` to find a named workspace or resolve
ambiguity. Reuse the workspace from the lookup that returned a group/item ID.

- A numeric tracking-group ID is not a brand-group UUID.
- Reuse the opportunity identity, the Study `studyRef`/revision and returned brief versions across stages.
- Keep real internal IDs for tool calls; use human-readable citations in deliverables. Never expose credentials or signed read tokens in shared artifacts.

## Research exports and interpretation

For ranked search results use `socialseal_export_report` with `reportType:
"search_results_enriched"`, `format: "csv"` and `payload.groupIds`, keeping the
selected group's workspace. `socialseal_export_tracking_data` is the separate
legacy group/item time-window export. Inspect actual columns and scope before
choosing or interpreting either.

Poll a pending export with `socialseal_get_tool_status`, `kind: "export"`, and its
returned ID. Do not repeatedly submit it. Once ready, fetch `download_url`; if that
is inaccessible, use `socialseal_read_export_chunk` with the returned `read_token`,
then each `next_offset` until `has_more` is false. Report partial coverage if reading
stops early; do not assume omitted rows are unimportant or expose the token.

Views on surfaced videos are not search volume, query-attributed engagement or
verified local audience demand. Within one platform, market and capture window,
result counts, rank and views remain valid relative demand signals for comparing
queries. Region describes collection context. Preserve
capture dates, denominator, duplicate-video treatment and missing values. See
`evidence-and-confidence.md` before deriving audience/creative recommendations.

## Pending work and failures

Use the returned job identity and the action's documented read/status tool.
Video search uses `socialseal_get_video_search`; video analysis can use
`socialseal_get_tool_status` with `kind: "video_analysis"` and the returned stored
identifier. A Study uses `socialseal_get_study` with its `studyRef`; brief versions
use their corresponding read actions. Pending/draft/`enriching` is not completed;
`missing_data` and `study_needed` are evidence gaps, not a generated deliverable. Inspect typed errors and correct the indicated input once evidence
supports it. Do not cycle arbitrary parameters, replace pending paid operations,
or mislabel an MCP-host approval failure as SocialSeal billing or job failure.

## Connector setup and file mode

If tool discovery and connection status confirm no SocialSeal access in Cowork, explain the missing connection:
**Customize → Connectors → + → Add custom connector**, name `socialseal`, URL
`https://mcp.socialseal.co/mcp`, then connect/sign in. Do not ask a non-technical
Cowork user to install Node.js or run shell commands.

In Claude Code, the plugin bundles the same hosted connector; ask the user to run
`/mcp`, select `socialseal`, and sign in.

If live access is unavailable, use supplied exports and approved documents. State
their dates and limitations; file mode cannot start live collection or run the
brief engine. A manual brief is a labelled fallback with its evidence gaps, not a
claim that SocialSeal generated it.
