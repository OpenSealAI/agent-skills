# SocialSeal MCP and File-Mode Usage

MCP is the supported agent interface. Use the connected hosted server in Cowork;
local stdio MCP is a developer fallback. Do not direct users to install or use the
retired standalone SocialSeal CLI. The historical filename of this reference is
retained for existing skill links.

## Discover the action for the job

Use a named action directly when its schema is already available. Otherwise use
`socialseal_list_available_tools` and `socialseal_get_tool_schema`. Discovery and
skills are references, not mandatory gates for every read or edit.

- Content calendars and posting schedules: `socialseal-social-plan-builder` guides composition and revision; do not assume a calendar-generation tool.
- New video/editor/UGC briefs: `socialseal_generate_brief` (compatibility target `vnext-briefs-generate`). Existing blueprint/version or supported scope is sufficient to begin; reference selection can use `socialseal_generate_blueprint` when needed.
- Existing brief: `socialseal_get_brief`, `socialseal_update_brief`, `socialseal_export_brief`. A formatting or copy edit does not need new evidence collection.
- Brief discovery spans `vnext` and `video-production`; omit category if a filtered listing misses it. A missing named action does not prove the compatibility target is unavailable.

Inspect the exact live input schema before an unfamiliar mutation. The compatibility
dispatcher accepts **`toolName`**, not `function`:

```text
socialseal_get_tool_schema { "toolName": "vnext-briefs-generate" }
socialseal_call_tool {
  "toolName": "vnext-briefs-generate",
  "workspaceId": "<workspace-id>",
  "body": { "opportunityKey": "<opportunity-key>", "blueprintId": "<blueprint-id>" }
}
```

Prefer named actions when exposed. Preserve backend authorisation, admission and
funding controls; tool discovery is not approval for additional paid work.

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

If no SocialSeal tools are available in Cowork, explain the missing connection:
**Customize → Connectors → + → Add custom connector**, name `socialseal`, URL
`https://mcp.socialseal.co/mcp`, then connect/sign in. Do not ask a non-technical
Cowork user to install Node.js or run shell commands.

Developers can use the local `@socialseal/mcp-server` stdio server. Its
`socialseal_start_login` / `socialseal_poll_login` actions handle device login.

If live access is unavailable, use supplied exports and approved documents. State
their dates and limitations; file mode cannot start live collection or run the
brief engine. A manual brief is a labelled fallback with its evidence gaps, not a
claim that SocialSeal generated it.
