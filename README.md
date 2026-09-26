# SocialSeal Agent Skills

[![skills.sh](https://skills.sh/b/OpenSealAI/agent-skills)](https://skills.sh/OpenSealAI/agent-skills)

Open-source Agent Skills for SocialSeal workflows: social-search strategy across
TikTok, Instagram, Xiaohongshu/RedNote, Douyin, YouTube Shorts, and other social
platforms; evidence-grounded video/carousel production; creator/UGC planning; and
discoverability measurement.

## Install

### ChatGPT and Codex (recommended)

Install **SocialSeal — Social Search & Video** from the Plugins Directory, connect
to SocialSeal when prompted, and start a new task. The plugin bundles the SocialSeal
skills and its hosted remote MCP server at `https://mcp.socialseal.co/mcp`, so users
do not need to add a separate custom connector or install Node.js.

Search for SocialSeal by name, or through jobs such as social search, social video,
short-form video, TikTok SEO, Instagram Reels, Xiaohongshu/RedNote, Douyin, creator
content, UGC, content strategy, competitor analysis, or discoverability tracking.

The public ChatGPT/Codex listing must be submitted and published as a **With MCP**
plugin in the OpenAI plugin submission portal. Updating this repository does not by
itself replace the reviewed public listing or its MCP metadata snapshot. See the
[ChatGPT and Codex submission checklist](docs/openai-plugin-submission.md).

### Codex local and repository development

This repository includes the native `.codex-plugin/plugin.json` manifest and a
bundled `.mcp.json` connection to the hosted SocialSeal MCP server. Add the repository
as a marketplace source, install `socialseal-agent-skills`, then start a new Codex
session so the new skills and tools are loaded:

```bash
codex plugin marketplace add OpenSealAI/agent-skills
codex plugin add socialseal-agent-skills@socialseal-skills
```

If authentication is required, follow the connection prompt and sign in to
SocialSeal. For local testing in ChatGPT Chat or Work, enable Developer mode, register
`https://mcp.socialseal.co/mcp` in the Plugins page, and use the generated registered
connection when packaging a local `.app.json` mapping.

### Claude Cowork and non-technical users

Use the hosted SocialSeal remote MCP connector for live tools, then install this plugin for skills. This is the default path for Cowork because it does not require local Node.js, `npx`, terminal commands, or local config files.

1. Open **Customize** -> **Connectors**.
2. Click **+** -> **Add custom connector**.
3. Fill in **Name**: `socialseal` and **Remote MCP server URL**: `https://mcp.socialseal.co/mcp`.
4. Click **Add**/**Connect** and sign in to SocialSeal.
5. Open the **Cowork** tab, then open **Customize** in the left sidebar.
6. Go to the **Plugins** tab. Under **Personal plugins**, click **+** -> **Add marketplace** -> **Add from a repository**.
7. Enter `OpenSealAI/agent-skills` and confirm.
8. Click **Install** on **socialseal-agent-skills**.

Skills then appear via `/` or the **+** button. If tools are not initially visible, use the host's available tool search/discovery facilities first. A missing initial tool list does not establish that the connector is disconnected. Return to **Customize** -> **Connectors**, confirm `socialseal` (`https://mcp.socialseal.co/mcp`) is connected, and retry. If the connector is not available, use file mode with SocialSeal CSV/JSON exports.

For a large content plan or production request, explicitly start with
`socialseal-orchestrator` if Claude does not select it automatically. The orchestrator
will check brand utility, demand evidence, benchmarks, asset choices, prototypes, and
delivery state before routing into downstream skills.

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

### Cursor and Grok Bot

The Cursor-format package at `.cursor-plugin/plugin.json` connects to the hosted
SocialSeal MCP server and includes the focused `socialseal-creator-evaluation`
skill. Routine social-search, profile, and post requests use the live tools directly;
they do not require a tracking group or the broader production skills in this repo.
Follow the tools' current schemas, account permissions, collection quotes, and
approval requirements. A SocialSeal account is required; available operations depend
on that account's entitlements.

For local Cursor development, load this checkout with
`agent --plugin-dir /absolute/path/to/agent-skills`, then complete the SocialSeal
browser sign-in when prompted. The package references `.mcp.json`; it does not
require Node.js, an API key, or a separate local MCP server.

Example requests:

- "Research social-search results for my brand and market, with source links."
- "Get this creator's recent posts and explain which engagement metrics are available."
- "Evaluate this creator for a brand partnership using recent posts and the brand evidence I provide."

Marketplace review and Grok Bot compatibility are pending. This repository is not
proof of a published Grok listing. Once SocialSeal is available in Grok Bot's
**Plugins** catalogue, add it, complete the SocialSeal browser authorization, and
confirm it appears under **Installed**. See the official
[Grok plugin connection guide](https://cursor.com/help/grok-bot/connect-plugins).
A custom MCP connection is an assisted setup and does not travel with a shared
Grok bot template; recipients must connect their own SocialSeal account.

### skills.sh (skills only)

```bash
npx skills add OpenSealAI/agent-skills
```

The Claude plugin manifest lives at `.claude-plugin/plugin.json` and remains
skills-only for Claude plugin compatibility. Live tools should use the hosted
connector for Cowork or the local stdio MCP developer fallback for Claude Code. The
native ChatGPT/Codex package instead lives at `.codex-plugin/plugin.json` and bundles
the hosted MCP connection through `.mcp.json`.

## What this helps agents do

- Set up SocialSeal workspace scope and measurement surfaces.
- Design tracking groups, keyword sets, markets, platforms, and competitor scopes.
- Analyze discoverability gaps and competitor/content patterns.
- Shortlist creator-shop partners by search authority, monitor bilingual (local-vs-English) demand, and route resources to early demand signals.
- Run the SocialSeal production engine: identify and analyze reference videos (Video DNA), compile best-practices blueprints, generate briefs from blueprints, and prepare source clips and editor handoffs.
- Build social plans, creator briefs, video concepts, asset plans, and editor handoffs.
- Read out posted content and campaign performance, track discoverability, and plan next actions.

## What this does not do

Asset Studio video generation and CapCut/FCPXML export skills have retired. Use
brief exports and rights-cleared source clips for an editor handoff; SocialSeal
does not assemble or render that video.

This repo does not automate posting, scheduling, inbox/comment/DM management, account growth tactics, paid media buying, or day-to-day social account operations.

## Integration modes

- **MCP mode (preferred):** the hosted SocialSeal connector, or the local developer fallback `@socialseal/mcp-server`, exposes stable meta-tools (`socialseal_list_available_tools`, `socialseal_get_tool_schema`, `socialseal_call_tool`, `socialseal_get_tool_status`, `socialseal_export_report`, `socialseal_export_tracking_data`). Backend function targets are invoked through `socialseal_call_tool`.
- **CLI mode:** the public `@socialseal/cli` mirrors the same surface via `tools list` / `tools schema` / `tools call` plus first-class `data export-*` commands.
- **File mode:** use user-provided SocialSeal exports.

Always inspect the live registry/schema before mutating calls. See [references/mcp-and-cli-usage.md](references/mcp-and-cli-usage.md) and [references/production-pipeline.md](references/production-pipeline.md). For how to cite evidence in human-readable terms and how confident to be about it, see [references/socialseal-data-contract.md](references/socialseal-data-contract.md) and [references/evidence-and-confidence.md](references/evidence-and-confidence.md); for the strategy concepts the skills assume, see [references/strategy-foundations.md](references/strategy-foundations.md).

## Skill taxonomy

### Orchestration
- `socialseal-orchestrator` (coordinates explicitly requested multi-stage creative production)
- `socialseal-strategy-readiness` (diagnoses strategy + setup readiness and guides the user to define what is missing)

### Strategy
- `socialseal-workspace-setup`
- `socialseal-tracking-group-design`
- `socialseal-opportunity-analysis`
- `socialseal-competitor-content-analysis`
- `socialseal-creator-evaluation` (supplied creator, recent-post metrics, and grounded brand fit)
- `socialseal-creator-discovery` (shortlist creator-shop partners by market, language, and destination/topic authority from search evidence)
- `socialseal-bilingual-demand-monitoring` (map the local-language vs English search-demand split and catch micro-trends early)
- `socialseal-predictive-demand-routing` (source early demand signals to back resource allocation and fast-track activity/tour onboarding)
- `socialseal-social-plan-builder`

### Production

These follow the SocialSeal vNext engine: opportunity -> reference videos -> blueprint -> brief -> source-clip/editor handoff, joined by a single `opportunityKey`. See [references/production-pipeline.md](references/production-pipeline.md).

- `socialseal-video-concepting`
- `socialseal-reference-video-analysis`
- `socialseal-blueprint-builder`
- `socialseal-creator-briefing`
- `socialseal-asset-planning`
- `socialseal-generation-prompts`
- `socialseal-carousel-production` (evidence, visual direction, asset selection,
  prototype approval, rendered slides, and post-ready QA for carousels)

For multi-stage creative work, the skills use explicit foundation, demand,
benchmark, asset, prototype, and final-QA gates. See
[references/creative-production-gates.md](references/creative-production-gates.md).

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
- ChatGPT/Codex plugin: `.codex-plugin/plugin.json`, `.mcp.json`, and `skills/`
- Cursor-format package: `.cursor-plugin/plugin.json`, `.mcp.json`, and the creator-evaluation skill; marketplace review and Grok compatibility pending
- Claude Code plugin marketplace: `.claude-plugin/plugin.json` plus direct `skills/` children
- Hermes project usage through the same `SKILL.md` files

## License

MIT
