# SocialSeal MCP and CLI Usage

SocialSeal exposes the same function surface through a public MCP server (`@socialseal/mcp-server`) and a public CLI (`@socialseal/cli`). Both are thin wrappers over the same backend tool registry. Always inspect the live registry/schema before calling a mutating tool; do not rely on stale tool memory.

## MCP mode (preferred when available)

The MCP server registers a small set of stable meta-tools. You do not call backend functions directly by name as separate MCP tools; you call them through `socialseal_call_tool`.

Meta-tools:
- `socialseal_list_workspaces` / `socialseal_get_current_workspace`: workspace discovery and default.
- `socialseal_list_available_tools` (optional `category`): list backend function targets in the registry.
- `socialseal_get_tool_schema` (`name`): required/optional fields and an example body for a function target.
- `socialseal_call_tool` (`function`, `body`, optional `workspaceId`): invoke a backend function target.
- `socialseal_get_tool_status` (`id`, `kind`): poll async runs. `kind` is one of `agent_job`, `google_ai_run`, `journey_run`, `video_analysis`.
- `socialseal_export_tracking_data`: stream a tracking CSV for a group or item.
- `socialseal_export_report`: report exports; `reportType` includes `keyword_universe`, `cluster_insights`, `creator_signatures`, `post_publish`, `quick_audit`, `search_results_enriched` (csv-only).

Canonical MCP loop:

1. `socialseal_list_workspaces` -> confirm scope.
2. `socialseal_list_available_tools` (optionally by `category`, e.g. `vnext`, `asset-studio`, `tracking`, `export`).
3. `socialseal_get_tool_schema` with the target function name before any mutating call.
4. `socialseal_call_tool` with `{ "function": "<target>", "body": { ... }, "workspaceId": "<workspace-id>" }`.
5. For async work, `socialseal_get_tool_status` with the returned id and the right `kind`.

Notes:
- There is no `export-group-evidence` or `export-search-results` MCP tool. In MCP mode reach enriched ranked rows via `socialseal_export_report` with `reportType: "search_results_enriched"` and `payload: { "groupIds": [<group-id>] }`, or use `socialseal_export_tracking_data` for a group/item CSV.
- All `vnext-*` and `tracked-video-extract` function targets are invoked through `socialseal_call_tool` with the same body shapes shown in `references/production-pipeline.md`.

## CLI mode

Install: `npm install -g @socialseal/cli` (or `npx -y @socialseal/cli ...`). Configure `SOCIALSEAL_API_KEY` and optionally `SOCIALSEAL_WORKSPACE_ID`; `socialseal workspace use <id|slug|exact-name>` writes a local default.

Discovery and schema:

```bash
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
MCP : socialseal_call_tool { function: "<target>", body: { ... }, workspaceId: "<workspace-id>" }
CLI : npx -y @socialseal/cli tools call --function <target> --workspace-id <workspace-id> --body '{ ... }'
```

and the CLI equivalent of `socialseal_get_tool_status` is `npx -y @socialseal/cli tools status <id> --kind <kind>`.

## Workspace and id discipline

- Effective workspace precedence (CLI): `--workspace-id` -> `SOCIALSEAL_WORKSPACE_ID` -> local config default.
- `group_id` for exports and group-management is a numeric tracking group id, not a brand-group UUID.
- Use placeholders (`<workspace-id>`, `<group-id>`, `<blueprint-id>`, `<clip-id>`, `<asset-id>`, `<opportunity-key>`) in any shared artifact; never literal IDs, tokens, or keys.
