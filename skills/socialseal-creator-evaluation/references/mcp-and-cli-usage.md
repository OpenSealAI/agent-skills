# SocialSeal MCP and File-Mode Usage

MCP is the supported agent interface. Use the connected hosted server in Cowork;
local stdio MCP is a developer fallback. Do not direct users to install or use the
retired standalone SocialSeal CLI. The historical filename of this reference is
retained for existing skill links.

## Discover access and direct actions

Use the host's available tool search/discovery facilities before concluding that a connector is missing. Tools can be loaded lazily. If discovery or connection status confirms missing access, use `onboarding-and-auth.md`; do not diagnose disconnection from an empty initial tool list or one failed action.

Use `socialseal_get_current_workspace` or `socialseal_list_workspaces` when workspace context is needed. Reuse the authorized, unambiguous context already available. Ask only when an operation requires context that remains ambiguous. An account read does not imply tracking setup; an absent brand does not block account metrics.

An unsupported platform, missing argument, missing evidence, authorization denial, and provider failure are different limitations. Preserve useful completed portions of compound requests. A stale skill or unavailable action does not authorize a search-only substitute or a resolver rephrase loop.

## Direct actions

Select the action matching the supplied target and requested deliverable from the live catalogue. Its description and schema state platforms, inputs, side effects, evidence/freshness limits, collection costs, and continuation. Use the actual schema rather than inventing parameters from a remembered name.

- Existing tracking groups: read the existing authorized group. Do not create groups or run collection to answer a read.
- Supplied video URL: use the URL-analysis action with that URL. Apply the operation's quote/approval boundary if new analysis is needed.
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

Creator reads use stored snapshots. A fresh request returns `FRESH_COLLECTION_REQUIRED` with any usable evidence. For requested fresh collection, discover authorized workspace context and call `socialseal_collect_creator_account` with the target, platform `instagram`, explicit `workspaceId`, `idempotencyKey`, and `maxCredits: 1` under the existing one-account-refresh credit policy. This creates a one-off collection receipt, never a tracker. Reuse the key after timeouts. If running, call `socialseal_get_creator_collection` with its `id` and workspace; terminal failed receipts do not automatically retry. The provider does not support timeline pagination, so preserve partial coverage and `coverage.latestClaim`.

## Discover the action for the job

Use a named action directly when its schema is already available. Otherwise use
the host's tool search to load the matching operation and its live input schema.
Discovery and skills are references, not mandatory gates for every read or edit.

- Content calendars and posting schedules: `socialseal-social-plan-builder` guides composition and revision; do not assume a calendar-generation tool.
- New video/editor/UGC briefs: `socialseal_generate_brief`. Existing blueprint/version or supported scope is sufficient to begin; reference selection can use `socialseal_generate_blueprint` when needed.
- Existing brief: `socialseal_get_brief`, `socialseal_update_brief`, `socialseal_export_brief`. A formatting or copy edit does not need new evidence collection.
- Tracking setup: `socialseal_create_tracking_group`, `socialseal_add_tracking_group_items`, then `socialseal_get_tracking_group_completeness`. Read existing groups before proposing setup.
- Search demand: `socialseal_start_search_journey` and `socialseal_get_search_journey_run`; Google AI uses `socialseal_start_google_ai_search`, `socialseal_list_google_ai_search_runs`, and `socialseal_get_google_ai_search_results`.
- Source-video assets: `socialseal_extract_video_assets` with stored identifiers. For a supplied public URL, use `socialseal_analyse_public_video`.

Inspect the exact live input schema before an unfamiliar mutation. Arguments go
directly on the named action, without a backend-function selector or body envelope:

```text
socialseal_generate_brief {
  "workspaceId": "<workspace-id>",
  "opportunityKey": "<opportunity-key>",
  "blueprintId": "<blueprint-id>"
}
```

If host discovery confirms an action is unavailable, report that precise limitation
and preserve completed work. Preserve backend authorisation, admission and funding
controls; tool discovery is not approval for additional paid work.

## Workspace and identity

Use the workspace the user named. For an unnamed workspace, resolve
`socialseal_get_current_workspace`; never infer the default from list order or
ownership. Use `socialseal_list_workspaces` to find a named workspace or resolve
ambiguity. Reuse the workspace from the lookup that returned a group/item ID.

- A numeric tracking-group ID is not a brand-group UUID.
- Reuse the opportunity identity and returned blueprint/brief versions across stages.
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
verified local audience demand. Region describes collection context. Preserve
capture dates, denominator, duplicate-video treatment and missing values. See
`evidence-and-confidence.md` before deriving audience/creative recommendations.

## Pending work and failures

Use the returned job identity and the action's documented read/status tool.
Video search uses `socialseal_get_video_search`; video analysis can use
`socialseal_get_tool_status` with `kind: "video_analysis"` and the returned stored
identifier. Blueprint/brief versions use their corresponding read actions.
Pending/draft is not completed; `missing_data` is an evidence gap, not a generated
deliverable. Inspect typed errors and correct the indicated input once evidence
supports it. Do not cycle arbitrary parameters, replace pending paid operations,
or mislabel an MCP-host approval failure as SocialSeal billing or job failure.

## Connector setup and file mode

If tool discovery and connection status confirm no SocialSeal access in Cowork, explain the missing connection:
**Customize → Connectors → + → Add custom connector**, name `socialseal`, URL
`https://mcp.socialseal.co/mcp`, then connect/sign in. Do not ask a non-technical
Cowork user to install Node.js or run shell commands.

Developers can use the local `@socialseal/mcp-server` stdio server. Its
`socialseal_start_login` / `socialseal_poll_login` actions handle device login.

If live access is unavailable, use supplied exports and approved documents. State
their dates and limitations; file mode cannot start live collection or run the
brief engine. A manual brief is a labelled fallback with its evidence gaps, not a
claim that SocialSeal generated it.
