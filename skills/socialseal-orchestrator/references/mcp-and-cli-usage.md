# SocialSeal MCP, CLI, and File-Mode Usage

SocialSeal exposes the same function surface through the hosted SocialSeal connector, the local developer MCP fallback (`@socialseal/mcp-server`), and the public CLI (`@socialseal/cli`). These paths are thin wrappers over the same backend tool registry. Always inspect the live registry/schema before calling a mutating tool; do not rely on stale tool memory.

## Hosted connector mode (preferred for Cowork)

For Cowork and non-technical users, use the hosted SocialSeal remote MCP connector. It should expose `socialseal_*` tools after the user connects SocialSeal under **Customize** -> **Connectors**. If those tools are missing, give setup guidance instead of continuing as if live tools exist:

1. Say that the SocialSeal connector is not connected or enabled in this conversation.
2. Ask the user to open **Customize** -> **Connectors**, click **+** -> **Add custom connector**, and fill in **Name** `socialseal` and **Remote MCP server URL** `https://mcp.socialseal.co/mcp`, then click **Add**/**Connect** and sign in.
3. After they connect, retry workspace discovery with `socialseal_list_workspaces`.
4. If the connector is unavailable, switch to file mode and ask for SocialSeal CSV/JSON exports.

Do not ask Cowork users to install Node.js, run `npx`, or configure a local MCP server. The local stdio MCP server (`@socialseal/mcp-server`) is an npm-based developer fallback that requires Node.js/`npx`; the remote connector at `https://mcp.socialseal.co/mcp` needs none of that.

## MCP mode

The MCP connector/server registers a small set of stable meta-tools. You do not call backend functions directly by name as separate MCP tools; you call them through `socialseal_call_tool`.

Meta-tools:

- `socialseal_list_workspaces` / `socialseal_get_current_workspace`: workspace discovery and default.
- `socialseal_list_available_tools` (optional `category`): list backend function targets in the registry.
- `socialseal_get_tool_schema` (`toolName`): required/optional fields and an example body for a function target.
- `socialseal_call_tool` (`toolName`, `body`, optional `workspaceId`): invoke a backend function target.
- `socialseal_get_tool_status` (`id`, `kind`): poll async runs. `kind` is one of `agent_job`, `google_ai_run`, `journey_run`, `video_analysis`.
- `socialseal_export_tracking_data` (`body`, optional `workspaceId`): stream a tracking CSV for a group or item.
- `socialseal_export_report` (`body`, optional `workspaceId`): report exports. Inside `body`, `reportType` includes `keyword_universe`, `cluster_insights`, `creator_signatures`, `post_publish`, `quick_audit`, `search_results_enriched` (csv-only).

Local stdio MCP only:

- `socialseal_start_login` / `socialseal_poll_login`: browser-based device login when local developer credentials are missing.

Canonical MCP loop:

1. `socialseal_list_workspaces` -> confirm scope.
2. `socialseal_list_available_tools` (optionally by `category`, e.g. `vnext`, `asset-studio`, `tracking`, `export`).
3. `socialseal_get_tool_schema` with `{ "toolName": "<target>" }` before any mutating call.
4. `socialseal_call_tool` with `{ "toolName": "<target>", "body": { ... }, "workspaceId": "<workspace-id>" }`.
5. For async work, `socialseal_get_tool_status` with the returned id and the right `kind`.

Notes:

- There is no `export-group-evidence` or `export-search-results` MCP tool. In MCP mode reach enriched ranked rows via `socialseal_export_report` with `{ "body": { "reportType": "search_results_enriched", "format": "csv", "payload": { "groupIds": [<group-id>] } } }`, or use `socialseal_export_tracking_data` with `{ "body": { "groupId": <group-id>, "timePeriod": "30d" } }` for a group/item CSV.
- All `vnext-*` and `tracked-video-extract` function targets are invoked through `socialseal_call_tool` with the same body shapes shown in `references/production-pipeline.md`.

## Local stdio MCP developer fallback

Claude Code developers can install the local stdio MCP server separately when they need local development or debugging. This fallback requires Node.js and `npx`; it is not the default Cowork setup.

```bash
claude mcp add --transport stdio socialseal -- npx -y @socialseal/mcp-server
```

If local MCP credentials are missing, call `socialseal_start_login`, send the approval URL/code to the user, then call `socialseal_poll_login`. The local server stores the resulting key in `~/.config/socialseal/config.json` with local-only file permissions.

## CLI mode

Install: `npm install -g @socialseal/cli` (or `npx -y @socialseal/cli ...`). Run `socialseal login` first when credentials are missing. It stores a local key in `~/.config/socialseal/config.json`; `socialseal workspace use <id|slug|exact-name>` writes a local default.

Discovery and schema:

```bash
npx -y @socialseal/cli login
npx -y @socialseal/cli whoami
npx -y @socialseal/cli tools list
npx -y @socialseal/cli tools schema --function <function-name>
npx -y @socialseal/cli data export-options
```

Direct function calls (inline JSON or `@file.json`):

```bash
npx -y @socialseal/cli tools call \
  --function <function-name> \
  --workspace-id <workspace-id> \
  --body '{"action":"..."}' \
  --pretty
```

Async start + poll:

```bash
npx -y @socialseal/cli tools call --function search-journey-run --body @journey.json --async --workspace-id <workspace-id>
npx -y @socialseal/cli tools status <run-id> --kind journey_run --workspace-id <workspace-id>
```

First-class data exports:

```bash
npx -y @socialseal/cli data export-search-results --group-ids <group-id> --workspace-id <workspace-id> --out ./exports/search.csv
npx -y @socialseal/cli data export-group-evidence --group-id <group-id> --workspace-id <workspace-id> --out ./exports/evidence.csv
npx -y @socialseal/cli data export-tracking --group-id <group-id> --time-period 30d --workspace-id <workspace-id> --out ./exports/tracking.csv
npx -y @socialseal/cli data export-report --report-type search_results_enriched --format csv --payload '{"groupIds":[<group-id>]}' --workspace-id <workspace-id> --out ./exports/ranked.csv
```

Video and asset studio (all function targets are also reachable via `tools call`):

```bash
npx -y @socialseal/cli video extract --search-result-id <search-result-id> --ensure-analysis --wait --out-dir ./video-assets --workspace-id <workspace-id>
npx -y @socialseal/cli tools call --function vnext-blueprints-generate --workspace-id <workspace-id> --body @blueprint.json --pretty
npx -y @socialseal/cli tools call --function vnext-briefs-export --workspace-id <workspace-id> --body '{"opportunityKey":"<opportunity-key>"}' --pretty
```

## Equivalence note for skills

Skills document the MCP path first. The CLI equivalent of any `socialseal_call_tool` is:

```text
MCP : socialseal_call_tool { toolName: "<target>", body: { ... }, workspaceId: "<workspace-id>" }
CLI : npx -y @socialseal/cli tools call --function <target> --workspace-id <workspace-id> --body '{ ... }'
```

and the CLI equivalent of `socialseal_get_tool_status` is `npx -y @socialseal/cli tools status <id> --kind <kind>`.

## File mode

Use file mode when no hosted connector, local MCP server, or CLI is available. Ask the user for SocialSeal CSV/JSON exports, inspect the columns and date ranges, then run the relevant skill from the provided files. Be explicit that file mode can analyze supplied exports but cannot create workspaces, start live jobs, poll async runs, or export new reports.

## Workspace and id discipline

- Effective workspace precedence (CLI): `--workspace-id` -> `SOCIALSEAL_WORKSPACE_ID` -> local config default.
- `group_id` for exports and group-management is a numeric tracking group id, not a brand-group UUID.
- Use placeholders (`<workspace-id>`, `<group-id>`, `<blueprint-id>`, `<clip-id>`, `<asset-id>`, `<opportunity-key>`) in any shared artifact; never literal IDs, tokens, or keys.
- If auth fails, run `socialseal login` before continuing. If credits or quota are exhausted, run `socialseal billing`.
