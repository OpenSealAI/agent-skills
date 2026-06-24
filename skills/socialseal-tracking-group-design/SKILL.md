---
name: socialseal-tracking-group-design
description: Use this skill when designing or implementing SocialSeal tracking groups,
  keyword sets, market/platform splits, or competitor scopes. It teaches the agent
  how SocialSeal tracking groups and tracking items should be structured, then creates
  or specifies groups using the CLI or MCP.
license: MIT
metadata:
  socialseal:
    phase: setup
  tags:
  - socialseal
  - setup
  - tracking-groups
  - keywords
  - measurement-architecture
---

# SocialSeal Tracking Group Design

## Overview

A SocialSeal tracking group is not a folder for random keywords. It is a measurement surface: one platform, one market/language context, and one coherent search intent. Downstream SOV, discoverability, and creator/content insights only work if the group structure is clean.

The deliverable depends on access:

- With SocialSeal CLI/MCP access: tracking groups are created, populated, and checked for completeness.
- Without access: a tracking-group specification is produced for someone else to implement.

## What SocialSeal Needs

SocialSeal measures what surfaces for tracked social-search keywords. A useful setup separates:

- branded search: the brand/name itself
- category search: generic demand the brand wants to appear for
- competitor search: named competitor/entity terms
- planning/help search: practical questions and comparisons
- campaign/topic search: temporary or seasonal themes

Do not combine these just because they belong to the same brand.

## Inputs

Required:

- workspace ID or workspace name
- platform(s), using SocialSeal platform values such as `tiktok`, `instagram`, `youtube`, `ig_reels`, `yt_shorts`, `douyin`, `xhs`, `google_ai`
- market/region code and language
- group objective: branded, category, competitor, planning/help, campaign, or Google AI questions
- seed keywords or topics

Good to have:

- owned handles and competitor handles
- audience segments/personas
- previous keyword exports or search journey results
- reporting cadence and expected output

## Tooling

Prefer MCP when available (`socialseal_get_tool_schema` then `socialseal_call_tool` with `function: "group-management"`); the CLI `tools call` mirrors it. See `references/mcp-and-cli-usage.md`.

## CLI Workflow

First inspect the live surface:

```bash
npx -y @socialseal/cli tools schema --function group-management
npx -y @socialseal/cli data export-options
```

Create each group:

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"create","name":"TikTok / US / category searches","platform":"tiktok","description":"Category search tracking for US TikTok"}' \
  --pretty
```

Add keyword tracking items:

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"add_items","group_id":<group-id>,"items":[{"name":"<keyword>","type":"keyword","value":"<keyword>","region":"US"}]}' \
  --pretty
```

Check completeness:

```bash
npx -y @socialseal/cli tools call \
  --function group-management \
  --workspace-id <workspace-id> \
  --body '{"action":"completeness","group_id":<group-id>,"expected_items":[{"track_type":"search","track_value":"<keyword>","region":"US"}],"include_refresh_status":true}' \
  --pretty
```

For MCP, use the same sequence through the live MCP tools: schema/help → create group → add items → completeness. Do not guess MCP tool names.

## Keyword Design Rules

- Use 2-5 word phrases people would type into social search.
- Use local-language terms for non-English markets.
- Include practical intent: `how to`, `where to`, `best`, `vs`, `first time`, `itinerary`, `cost`, `near`, `what to expect`, category-specific equivalents.
- Keep brand names out of category groups.
- Keep competitor names out of category groups unless the group is explicitly competitor-search tracking.
- Avoid one-word generic keywords unless the category is narrow enough to make them meaningful.

## Recommended Group Naming

Use a consistent naming pattern:

`<Platform> / <Market> / <Type> / <Optional topic>`

Examples with placeholders:

- `TikTok / US / category / family travel`
- `Instagram / GB / branded`
- `YouTube / JP / planning-help`
- `Google AI / SG / category questions`

## Output

If implementing:

- created tracking groups
- added tracking items
- completeness check result for each group
- exported setup manifest with workspace ID, group IDs, group names, platform, market, type, keyword count

If specifying only:

- tracking-group architecture
- keyword list by group
- group naming convention
- implementation checklist

## Do / Don't

Do:

- create one group first and validate before bulk work
- use numeric tracking group IDs in export commands
- record keyword source: user-provided, search journey, manual research, or translated/localized
- separate stable evergreen groups from temporary campaign groups

Don't:

- mix TikTok/Instagram/YouTube in one group
- put branded and non-branded keywords in one group
- add keywords that are too broad to classify later
- change group membership in the middle of a reporting period without noting the break

## Troubleshooting

- If `add_items` fails, inspect schema and try one item object before bulk payloads.
- If completeness is missing expected items, compare `track_value`, region, and platform inheritance.
- If exports are empty, confirm the group has items and has had time or a run to produce results.
- If the user gave a long keyword dump, cluster first, then create groups. Do not create one giant group.

## Verification Checklist

- [ ] Every group has one platform, one market/language context, and one tracking type.
- [ ] Group names encode platform, market, and type.
- [ ] Branded/category/competitor/campaign terms are separated.
- [ ] Keywords are local-language where relevant.
- [ ] Completeness confirms expected tracking items.
- [ ] Setup manifest is saved for downstream analysis.

