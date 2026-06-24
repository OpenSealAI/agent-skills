---
name: socialseal-workspace-setup
description: >-
  Use this skill when configuring a SocialSeal workspace for a brand, market, or campaign: selecting or creating the workspace, creating tracking groups, adding tracking items, running a baseline search journey, and confirming exports work. The deliverable is a working SocialSeal workspace, not a setup brief.
license: MIT
metadata:
  socialseal:
    phase: setup
  tags:
  - socialseal
  - setup
  - workspace
  - tracking-groups
  - cli
  - mcp
---

# SocialSeal Workspace Setup

## Overview

SocialSeal is a social-search intelligence platform. It helps teams understand what appears when people search on social and AI-search surfaces, and whether a brand, competitor, creator, or content pattern is discoverable for the right keywords.

A setup task is complete only when the workspace can produce usable data. A document is not the deliverable. The deliverable is a configured workspace with the right tracking groups, tracking items, baseline runs, and exports verified.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Workspace | Top-level SocialSeal container for one brand, client, or project. Tracking groups and exports are scoped to a workspace. |
| Tracking group | A measurement container for one platform and one coherent keyword/topic scope. Example: `TikTok / US / category searches`. |
| Tracking item | A single item inside a group, usually a search keyword with region/platform metadata. |
| Search journey | A keyword-expansion or evidence run for a subject, subject type, and region. Useful for generating or validating keyword coverage before/after group creation. |
| Export | CSV/JSON output used by downstream analysis skills. Key export types include enriched search results and group evidence. |

## When to Use

Use this skill for:

- New workspace onboarding.
- Selecting and validating an existing workspace.
- Creating tracking groups.
- Adding keyword tracking items to groups.
- Running baseline search journeys.
- Confirming that group evidence and enriched search-result exports work.

Do not use this skill for opportunity analysis, creator briefs, social plans, or measurement readouts. Those are downstream tasks that depend on a correctly configured workspace.

## Inputs

### Required

- SocialSeal CLI access or SocialSeal MCP server access.
- Workspace target: existing workspace ID/name, or enough context to identify the intended workspace.
- Brand or subject name.
- Target platform(s): use platform values supported by SocialSeal, commonly `tiktok`, `instagram`, `youtube`, `ig_reels`, `yt_shorts`, `douyin`, `xhs`, or `google_ai`.
- Target market/region code, such as `US`, `GB`, `JP`, `SG`, `MY`.
- At least one keyword/topic set to track.

### Good to have

- Owned social handles.
- Competitor handles or competitor brand names.
- Local-language keyword variants.
- Whether each group is branded, category, competitor, creator, or campaign tracking.
- Reporting cadence and expected downstream deliverable.

### If the user is terse

If the user only says something like “set up SocialSeal for this brand,” ask for the minimum missing setup inputs:

1. workspace or workspace name
2. market/region
3. platform(s)
4. brand/subject
5. seed keyword/topic list

If the workspace already exists and you can list workspaces, do that before asking.

## Tooling

Both MCP and CLI work. Prefer MCP when available: discover with `socialseal_list_workspaces` and `socialseal_list_available_tools`, read `socialseal_get_tool_schema` before mutating calls, then `socialseal_call_tool`. The CLI mirrors this with `tools list` / `tools schema` / `tools call`. See `references/mcp-and-cli-usage.md`.

## CLI Setup Workflow

Use `npx -y @socialseal/cli` unless the `socialseal` binary is already installed. Prefer machine-readable flags when available.

### 1. Discover the current CLI surface

Run these first. Do not rely on stale command memory.

```bash
npx -y @socialseal/cli --help
npx -y @socialseal/cli workspace --help
npx -y @socialseal/cli tools --help
npx -y @socialseal/cli data --help
```

Then inspect the relevant tool schemas:

```bash
npx -y @socialseal/cli tools list
npx -y @socialseal/cli tools schema --function group-management
npx -y @socialseal/cli tools schema --function search-journey-run
npx -y @socialseal/cli data export-options
```

### 2. Select the workspace

List accessible workspaces:

```bash
npx -y @socialseal/cli workspace list --pretty
```

Show the current default:

```bash
npx -y @socialseal/cli workspace current --pretty
```

Set the default workspace by ID, slug, or exact name:

```bash
npx -y @socialseal/cli workspace use <workspace-id-or-slug-or-exact-name>
```

If using scoped keys or automation, still pass `--workspace-id <workspace-id>` explicitly to later commands. This avoids accidental fallback to a personal/default workspace.

### 3. Design the group structure before creating groups

Use one group per platform and coherent measurement scope. A good group name encodes platform, market, and type.

Recommended group split:

- `TikTok / US / category searches`
- `TikTok / US / branded searches`
- `Instagram / US / category searches`
- `YouTube / US / category searches`
- `Google AI / US / category questions`

Rules:

- Do not mix platforms in one group.
- Do not mix branded and category keywords in one group.
- Do not mix markets/languages unless the reporting question explicitly needs a combined view.
- Use local-language search phrases for non-English markets.

### 4. Create a tracking group

Supported platform values include `tiktok`, `instagram`, `youtube`, `ig_reels`, `yt_shorts`, `douyin`, `xhs`, and `google_ai`.

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"create","name":"TikTok / US / category searches","platform":"tiktok","description":"Category search tracking for US TikTok keywords"}' \
  --pretty
```

Save the returned numeric tracking group ID as `<group-id>`. Downstream export commands use numeric group IDs, not brand-group UUIDs.

### 5. Add tracking items to the group

For keyword payloads, use `group_id` and item objects. Omit item platform to inherit the group platform, or pass it explicitly if needed.

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"add_items","group_id":<group-id>,"items":[{"name":"<keyword one>","type":"keyword","value":"<keyword one>","region":"US"},{"name":"<keyword two>","type":"keyword","value":"<keyword two>","region":"US"}]}' \
  --pretty
```

Use real user search language, not internal marketing phrasing. For travel/hospitality and many consumer categories, useful keywords often express planning help, comparisons, timing, location, first-timer questions, or practical detail.

### 6. Check setup completeness

Use completeness to confirm expected memberships and optionally refresh visibility.

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"completeness","group_id":<group-id>,"expected_items":[{"track_type":"search","track_value":"<keyword one>","region":"US"},{"track_type":"search","track_value":"<keyword two>","region":"US"}],"include_refresh_status":true}' \
  --pretty
```

Do not declare setup complete until the group has the expected items.

### 7. Run or inspect a baseline search journey

A search journey helps validate subject, region, and keyword direction before or after group creation.

Start a run:

```bash
npx -y @socialseal/cli tools call \
  --function search-journey-run \
  --workspace-id <workspace-id> \
  --body '{"subject":"<brand-or-topic>","subjectType":"brand","region":"US","executionMode":"async"}' \
  --pretty
```

Poll an async journey run:

```bash
npx -y @socialseal/cli tools status <run-uuid> \
  --kind journey_run \
  --workspace-id <workspace-id>
```

Use `subjectType: "brand"` for a brand, `"topic"` for a category/topic. If the CLI schema shows additional fields such as `locale`, `platformKeys`, `seedKeywords`, `contentPillars`, or `maxKeywords`, use them when relevant.

### 8. Verify export data flow

List export options:

```bash
npx -y @socialseal/cli data export-options
```

For enriched ranked search rows:

```bash
npx -y @socialseal/cli data export-search-results \
  --group-ids <group-id> \
  --workspace-id <workspace-id> \
  --out ./exports/search-results-<group-id>.csv \
  --timeout 120000
```

For group evidence that automatically routes social and Google AI groups to the correct export shape:

```bash
npx -y @socialseal/cli data export-group-evidence \
  --group-id <group-id> \
  --workspace-id <workspace-id> \
  --out ./exports/group-evidence-<group-id>.csv \
  --timeout 120000
```

A valid setup should produce a file with usable rows or a clear, explainable reason for no rows, such as a new group with no completed refresh yet.

## MCP Setup Workflow

Use the same logical workflow through MCP. Do not invent MCP tool names.

1. List available MCP tools from the SocialSeal server.
2. Identify tools corresponding to:
   - workspace list/current/select
   - tool/function schema or help
   - tracking group creation
   - tracking item add/bulk add
   - group completeness/status
   - search journey start/status
   - search results or group evidence export
3. Read tool schema before calling mutating actions.
4. Create one group first, add a small keyword set, and verify completeness before bulk creation.
5. Export evidence after setup to confirm the workspace produces downstream data.

If MCP lacks a setup operation that the CLI supports, use the CLI for that operation and continue with MCP for reads/exports.

## Done Means

Workspace setup is done only when all of these are true:

- Correct workspace selected and confirmed.
- Planned tracking groups created with the correct platform values.
- Tracking items added to each group.
- Completeness check confirms expected items.
- At least one baseline search journey or status check has run for the workspace.
- At least one export command works for each important group type, or the reason for no rows is documented.
- Workspace ID, group IDs, group names, platform, market, and keyword set are recorded for downstream skills.

## Do / Don't

### Do

- Use `workspace list` before setup if the workspace is not explicitly provided.
- Use `tools schema --function group-management` before creating or adding items.
- Use `group_id`, not `groupId`, in `group-management` bodies unless the live schema says otherwise.
- Use `--group-ids` for `export-search-results` and `--group-id` for `export-group-evidence`.
- Keep a raw setup log with commands run, returned IDs, and export file paths.
- Create and validate one group first, then scale the pattern.

### Don't

- Don't call the output a brief when the user asked for setup.
- Don't mix platforms or keyword types inside one group.
- Don't add English-only keywords for non-English markets unless the user's scope is English-language search.
- Don't use brand-group UUIDs where the CLI expects numeric tracking group IDs.
- Don't treat a header-only export as success without explaining why no rows exist.
- Don't expose real workspace IDs, tracking IDs, API keys, or private exports in public examples.

## Troubleshooting

### Workspace not found

- Run `npx -y @socialseal/cli workspace list --pretty`.
- Confirm the key has access to the intended workspace.
- Use `workspace use <identifier>` with ID, slug, or exact name.
- Pass `--workspace-id <workspace-id>` explicitly on scoped commands.

### `add_items` succeeds but completeness fails

- Re-check the live schema for `group-management`.
- Confirm the body uses `group_id` and item objects.
- Confirm the region value is valid and consistent.
- Try adding a single item first to isolate malformed payloads.

### Export returns only headers or no rows

- Confirm items were added with completeness.
- New or modified groups may need refresh time before ranked results exist.
- Try `export-group-evidence` to route the group to the correct export type.
- Check date filters; too narrow a date range can hide valid results.

### Search journey does not start

- Confirm required fields: `subject`, `subjectType`, `region`, and workspace context.
- Use `subjectType: "topic"` for category searches, not `brand`.
- Add `executionMode: "async"` for long runs and poll with `tools status`.

### MCP and CLI disagree

- Prefer the live schema from the surface you are using.
- Record which surface created each group/item.
- If a mutating MCP call is missing or unstable, use the CLI for setup and MCP for inspection/exports.

## Verification Checklist

- [ ] Correct workspace selected or identified.
- [ ] Group structure matches platform × market × keyword type plan.
- [ ] Groups created with valid platform values.
- [ ] Items added using schema-valid payloads.
- [ ] Completeness confirms expected tracking items.
- [ ] Baseline journey/status was run or intentionally skipped with reason.
- [ ] Exports tested and saved for downstream use.
- [ ] Setup log includes workspace ID, group IDs, group names, platforms, markets, and export paths.
- [ ] No private IDs or credentials appear in public/shared docs.
