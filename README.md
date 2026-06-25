# SocialSeal Agent Skills

[![skills.sh](https://skills.sh/b/OpenSealAI/agent-skills)](https://skills.sh/OpenSealAI/agent-skills)

Open-source Agent Skills for SocialSeal workflows: social-search strategy, creator/UGC production planning, and discoverability measurement.

## Install

### Claude Cowork and non-technical users

Use the hosted SocialSeal remote MCP connector for live tools, then install this plugin for skills. This is the default path for Cowork because it does not require local Node.js, `npx`, terminal commands, or local config files.

1. Open **Customize** -> **Connectors**.
2. Click **+** -> **Add custom connector**.
3. Fill in **Name**: `socialseal` and **Remote MCP server URL**: `https://mcp.socialseal.co/mcp`.
4. Click **Add**/**Connect** and sign in to SocialSeal.
5. Open the **Cowork** tab, then open **Customize** in the left sidebar.
6. Go to the **Plugins** tab. Under **Personal plugins**, click **+** -> **Add marketplace** -> **Add from a repository**.
7. Enter `OpenSealAI/agent-skills` and confirm.
8. Click **Install** on **SocialSeal Agent Skills**.

Skills then appear via `/` or the **+** button. If Claude says SocialSeal tools are unavailable, the connector is not connected or enabled for that conversation. Return to **Customize** -> **Connectors**, confirm `socialseal` (`https://mcp.socialseal.co/mcp`) is connected, and retry. If the connector is not available, use file mode with SocialSeal CSV/JSON exports.

### Claude Code

Install the skills plugin:

```bash
/plugin marketplace add OpenSealAI/agent-skills
/plugin install socialseal-agent-skills@socialseal-skills
```

For local developer MCP usage, install the local stdio server separately. This is a developer fallback, not the default Cowork setup, and it requires Node.js and `npx`:

```bash
claude mcp add --transport stdio socialseal -- npx -y @socialseal/mcp-server
```

### skills.sh (skills only)

```bash
npx skills add OpenSealAI/agent-skills
```

The plugin manifest lives at `.claude-plugin/plugin.json` and is skills-only by default for Claude plugin compatibility. Live tools should use the hosted connector for Cowork or the local stdio MCP developer fallback for Claude Code.

## What this helps agents do

- Set up SocialSeal workspace scope and measurement surfaces.
- Design tracking groups, keyword sets, markets, platforms, and competitor scopes.
- Analyze discoverability gaps and competitor/content patterns.
- Shortlist creator-shop partners by search authority, monitor bilingual (local-vs-English) demand, and route resources to early demand signals.
- Run the SocialSeal production engine: identify and analyze reference videos (Video DNA), compile best-practices blueprints, generate briefs from blueprints, and assemble Asset Studio rough cuts from a clip library.
- Build social plans, creator briefs, video concepts, asset plans, and editor handoffs.
- Read out posted content and campaign performance, track discoverability, and plan next actions.

## What this does not do

This repo does not automate posting, scheduling, inbox/comment/DM management, account growth tactics, paid media buying, or day-to-day social account operations.

## Integration modes

- **MCP mode (preferred):** the hosted SocialSeal connector, or the local developer fallback `@socialseal/mcp-server`, exposes stable meta-tools (`socialseal_list_available_tools`, `socialseal_get_tool_schema`, `socialseal_call_tool`, `socialseal_get_tool_status`, `socialseal_export_report`, `socialseal_export_tracking_data`). Backend function targets are invoked through `socialseal_call_tool`.
- **CLI mode:** the public `@socialseal/cli` mirrors the same surface via `tools list` / `tools schema` / `tools call` plus first-class `data export-*` commands.
- **File mode:** use user-provided SocialSeal exports.

Always inspect the live registry/schema before mutating calls. See [references/mcp-and-cli-usage.md](references/mcp-and-cli-usage.md) and [references/production-pipeline.md](references/production-pipeline.md). For how to cite evidence in human-readable terms and how confident to be about it, see [references/socialseal-data-contract.md](references/socialseal-data-contract.md) and [references/evidence-and-confidence.md](references/evidence-and-confidence.md); for the strategy concepts the skills assume, see [references/strategy-foundations.md](references/strategy-foundations.md).

## Skill taxonomy

### Orchestration
- `socialseal-orchestrator` (lightweight entry point: checks foundations, routes to the right skill)
- `socialseal-strategy-readiness` (diagnoses strategy + setup readiness and guides the user to define what is missing)

### Strategy
- `socialseal-workspace-setup`
- `socialseal-tracking-group-design`
- `socialseal-opportunity-analysis`
- `socialseal-competitor-content-analysis`
- `socialseal-creator-discovery` (shortlist creator-shop partners by market, language, and destination/topic authority from search evidence)
- `socialseal-bilingual-demand-monitoring` (map the local-language vs English search-demand split and catch micro-trends early)
- `socialseal-predictive-demand-routing` (source early demand signals to back resource allocation and fast-track activity/tour onboarding)
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
