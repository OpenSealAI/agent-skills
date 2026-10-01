---
name: socialseal-workspace-setup
description: >-
  Use this skill when configuring or repairing SocialSeal for a brand, destination,
  market, or campaign, including "set up/onboard SocialSeal", "there is no tracking
  group", "create a workspace/group", "run a baseline/search journey", or when production is blocked
  because the requested topic has no usable SocialSeal evidence. Select or create the
  workspace, add groups/items, run a baseline journey, and verify exports; deliver a
  working setup, not merely a setup brief.
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

Use the host's tool search to load each named operation and inspect its live
schema. Resolve the workspace with `socialseal_get_current_workspace` or
`socialseal_list_workspaces`; pass that exact workspace ID throughout. Read existing
groups before proposing new setup. See `references/mcp-and-cli-usage.md`.

## MCP Setup Workflow

Design one group per platform, market and coherent measurement scope. Keep branded
and category queries separate, use local-language terms, and record the keyword
source. Confirm the proposed setup and any required collection approval before
starting paid work. Create one group and verify a small set before bulk setup.

```text
socialseal_create_tracking_group {
  "workspaceId": "<workspace-id>",
  "name": "TikTok / US / category searches",
  "platform": "tiktok",
  "description": "Category search tracking for US TikTok"
}
socialseal_add_tracking_group_items {
  "workspaceId": "<workspace-id>",
  "group_id": <group-id>,
  "items": [{ "name": "<keyword>", "type": "keyword", "value": "<keyword>", "region": "US" }]
}
socialseal_get_tracking_group_completeness {
  "workspaceId": "<workspace-id>",
  "group_id": <group-id>,
  "expected_items": [{ "track_type": "search", "track_value": "<keyword>", "region": "US" }],
  "include_refresh_status": true
}
```

Search adds use canonical Topic resolution; preserve returned conflicts and
approval/idempotency requirements. Completeness reads stored memberships and
refresh status; it does not collect evidence or prove freshness. Do not declare
setup complete until expected items are present.

For a baseline search journey, inspect the live `socialseal_start_search_journey`
schema and available preflight/credit information. Show subject, region, seeds and
platform scope; obtain the user's focused/full choice before consuming credits.
Use a focused one-off journey for an immediate brief, or reusable group setup when
future measurement is requested. Preserve the journey output for opportunity
analysis rather than reducing it to hashtags.

```text
socialseal_start_search_journey {
  "workspaceId": "<workspace-id>", "subject": "<brand-or-topic>",
  "subjectType": "brand", "region": "US"
}
socialseal_get_search_journey_run {
  "workspaceId": "<workspace-id>", "runId": "<run-uuid>"
}
socialseal_export_report {
  "workspaceId": "<workspace-id>",
  "reportType": "search_results_enriched", "format": "csv",
  "payload": { "groupIds": [<group-id>] }
}
```

Use `subjectType: "topic"` for a category. Poll the returned run, preserving pending,
funding and missing-data states; do not restart it to poll. Read the complete export,
including chunks when needed, and report actual coverage. A new group may have no
completed evidence yet; do not claim setup produced fresh collection.

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
- [ ] If the topic initially lacked a group, the one-off versus reusable choice and any credit approval are recorded.
- [ ] Exports tested and saved for downstream use.
- [ ] Setup log includes workspace ID, group IDs, group names, platforms, markets, and export paths.
- [ ] No private IDs or credentials appear in public/shared docs.
