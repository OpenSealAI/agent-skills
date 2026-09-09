# SocialSeal MCP, CLI, and File-Mode Usage

The host selects directly discoverable SocialSeal actions from their typed schemas and composes the user's task. Basic reads, supplied-URL analysis, exports, and account evidence require no skill, semantic resolver, or prescribed workflow. This reference adds examples and evidence conventions; the currently available schema is authoritative.

## Discover access and scope

Use the host's available tool search/discovery facilities before concluding that a connector is missing. Tools can be loaded lazily. If discovery or connection status confirms missing access, use `references/onboarding-and-auth.md`; do not diagnose disconnection from an empty initial tool list or one failed action.

Use `socialseal_get_current_workspace` or `socialseal_list_workspaces` when workspace context is needed. Reuse the authorized, unambiguous context already available. Ask only when an operation requires context that remains ambiguous. An account read does not imply tracking setup; an absent brand does not block account metrics.

An unsupported platform, missing argument, missing evidence, authorization denial, and provider failure are different limitations. Preserve useful completed portions of compound requests. A stale skill or unavailable action does not authorize a search-only substitute or a resolver rephrase loop.

## Direct actions

Select the action matching the supplied target and requested deliverable from the live catalogue. Its description and schema state platforms, inputs, side effects, evidence/freshness limits, collection costs, and continuation. Use the actual schema rather than inventing parameters from a remembered name.

- Existing tracking groups: read the existing authorized group. Do not create groups or run collection to answer a read.
- Supplied video URL: use the URL-analysis action with that URL. Apply the operation's quote/approval boundary if new analysis is needed.
- Named creator: read the profile and recent account posts with the requested platform/count. Timeline ordering, pinned posts, mixed media, timestamp provenance, and pagination determine whether a latest-post claim is supported. Return the service's aggregates and denominators; missing values remain distinct from zero. Retrieve accessible brand context independently for fit evaluation.
- Ranked-search creator discovery: use the requested ranked-search population and retain its sampling caveats. It is not a substitute for account posts.
- Account tracking: only create the explicitly requested ongoing commitment, retaining required authorization.

A generic `socialseal_call_tool` remains for identified compatibility and rare-operation callers. `socialseal_list_available_tools` and `socialseal_get_tool_schema` can help those callers find a retained backend target. They are not mandatory steps before direct actions, and `socialseal_resolve_request` is not a prerequisite.

Named-account examples (Instagram currently):

```text
socialseal_get_creator_profile { "target": "<profile-url-or-handle>", "platform": "instagram" }
socialseal_get_creator_recent_posts { "target": "<profile-url-or-handle>", "platform": "instagram", "recentPostCount": 5, "freshness": "stored" }
```

```bash
npx -y @socialseal/cli creator profile '<profile-url-or-handle>' --platform instagram
npx -y @socialseal/cli creator recent-posts '<profile-url-or-handle>' --platform instagram --count 5
npx -y @socialseal/cli tools status '<returned-video-id>' --kind video_analysis --workspace-id '<workspace-id>' --include-results
```

Creator reads use stored snapshots. A fresh request returns `FRESH_COLLECTION_REQUIRED` with any usable evidence. For requested fresh collection, discover authorized workspace context and call `socialseal_collect_creator_account` with the target, platform `instagram`, explicit `workspaceId`, `idempotencyKey`, and `maxCredits: 1` under the existing one-account-refresh credit policy. This creates a one-off collection receipt, never a tracker. Reuse the key after timeouts. If running, call `socialseal_get_creator_collection` with its `id` and workspace; terminal failed receipts do not automatically retry. The provider does not support timeline pagination, so preserve partial coverage and `coverage.latestClaim`.

```sh
npx -y @socialseal/cli creator collect '<profile-url-or-handle>' --workspace-id '<id>' --idempotency-key '<key>' --max-credits 1 --wait --json
npx -y @socialseal/cli creator status '<collection-id>' --workspace-id '<id>' --json
npx -y @socialseal/cli actions list --json
npx -y @socialseal/cli actions schema socialseal_get_tracking_group --json
npx -y @socialseal/cli actions call socialseal_get_tracking_group --body '{"group_id":436}' --json
```

`actions` reads the deployed catalogue/schema and uses the same definitions as MCP. Generic `tools` remains compatibility access. A client package alone does not prove the new backend is deployed; report an unavailable operation precisely.

## Completed artifacts and async work

For enriched ranked search evidence, the existing export action accepts:

```text
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "body": { "reportType": "search_results_enriched", "format": "csv", "payload": { "groupIds": [<group-id>] } }
}
```

An export returns an artifact, not necessarily inline CSV. When its download cannot be read in-session, pass `read_token` as `t` to `socialseal_read_export_chunk` with `offset` and `limit`. Follow the returned next offset until `has_more` is false. Keep the source, row counts, and actual historical coverage; an artifact URL alone is not a completed analysis.

```text
socialseal_read_export_chunk { "t": "<read-token>", "offset": 0, "limit": 100 }
```

Poll async operations using the returned ID and their stated status kind. `socialseal_get_tool_status` takes `id`, `kind`, and workspace context where required. Do not guess whether an ID denotes a journey, video analysis, or another job. A queued response is not completed evidence. Resume the existing job on retry rather than paying for duplicate work.

New collection and external effects retain backend quote, approval, budget, idempotency, and settlement controls. Metadata never authorizes paid work; reuse authorization already given for the same scope. Stored-evidence reads remain separate from fresh collection.

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

Video analysis, blueprints, and brief exports (all function targets are also reachable via `tools call`):

```bash
npx -y @socialseal/cli video extract --search-result-id <search-result-id> --ensure-analysis --wait --out-dir ./video-assets --workspace-id <workspace-id>
npx -y @socialseal/cli tools call --function vnext-blueprints-generate --workspace-id <workspace-id> --body @blueprint.json --pretty
npx -y @socialseal/cli tools call --function vnext-briefs-export --workspace-id <workspace-id> --body '{"opportunityKey":"<opportunity-key>"}' --pretty
```

## Compatibility calls

Prefer a directly discovered action for routine work. Retained generic calls support existing scripts and rare operations; they do not require a resolver. The CLI equivalent of a compatibility `socialseal_call_tool` is:

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
