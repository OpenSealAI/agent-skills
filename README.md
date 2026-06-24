# SocialSeal Agent Skills

[![skills.sh](https://skills.sh/b/socialseal/agent-skills)](https://skills.sh/socialseal/agent-skills)

Open-source Agent Skills for SocialSeal workflows: social-search strategy, creator/UGC production planning, and discoverability measurement.

## Install

```bash
npx skills add socialseal/agent-skills
```

For Claude Code plugin usage, add this repository or marketplace and install the `socialseal-agent-skills` plugin. The plugin manifest lives at `.claude-plugin/plugin.json`, and skills are direct children of `skills/` for Claude plugin compatibility.

## What this helps agents do

- Set up SocialSeal workspace scope and measurement surfaces.
- Design tracking groups, keyword sets, markets, platforms, and competitor scopes.
- Analyze discoverability gaps and competitor/content patterns.
- Run the SocialSeal production engine: identify and analyze reference videos (Video DNA), compile best-practices blueprints, generate briefs from blueprints, and assemble Asset Studio rough cuts from a clip library.
- Build social plans, creator briefs, video concepts, asset plans, and editor handoffs.
- Read out posted content and campaign performance, track discoverability, and plan next actions.

## What this does not do

This repo does not automate posting, scheduling, inbox/comment/DM management, account growth tactics, paid media buying, or day-to-day social account operations.

## Integration modes

- **MCP mode (preferred):** the public `@socialseal/mcp-server` exposes stable meta-tools (`socialseal_list_available_tools`, `socialseal_get_tool_schema`, `socialseal_call_tool`, `socialseal_get_tool_status`, `socialseal_export_report`, `socialseal_export_tracking_data`). Backend function targets are invoked through `socialseal_call_tool`.
- **CLI mode:** the public `@socialseal/cli` mirrors the same surface via `tools list` / `tools schema` / `tools call` plus first-class `data export-*` commands.
- **File mode:** use user-provided SocialSeal exports.

Always inspect the live registry/schema before mutating calls. See [references/mcp-and-cli-usage.md](references/mcp-and-cli-usage.md) and [references/production-pipeline.md](references/production-pipeline.md).

## Skill taxonomy

### Strategy
- `socialseal-workspace-setup`
- `socialseal-tracking-group-design`
- `socialseal-opportunity-analysis`
- `socialseal-competitor-content-analysis`
- `socialseal-social-plan-builder`

### Production

These follow the SocialSeal vNext engine: opportunity -> reference videos -> blueprint -> brief -> Asset Studio rough cut, joined by a single `opportunityKey`. See [references/production-pipeline.md](references/production-pipeline.md).

- `socialseal-video-concepting`
- `socialseal-reference-video-analysis`
- `socialseal-blueprint-builder`
- `socialseal-creator-briefing`
- `socialseal-asset-planning`
- `socialseal-generation-prompts`
- `socialseal-asset-studio-generation`
- `socialseal-capcut-export-prep`

### Measurement
- `socialseal-performance-readout`
- `socialseal-discoverability-tracking`
- `socialseal-content-adjustment-recommendations`
- `socialseal-management-reporting`
- `socialseal-follow-up-planning`

## Content principle

SocialSeal primarily supports UGC and creator content, not advertising. These skills use two content lenses:

- **Aspirational:** creates emotion or mood.
- **Utility/practical:** teaches useful information and gives the viewer an unlock, relief, accomplishment, or confidence.

## Distribution

This repository is structured for:

- Agent Skills / skills.sh: `skills/<skill-name>/SKILL.md`
- Claude Code plugin marketplace: `.claude-plugin/plugin.json` plus direct `skills/` children
- Hermes/Codex project usage through the same SKILL.md files

## License

MIT
