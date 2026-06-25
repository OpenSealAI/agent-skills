---
name: socialseal-orchestrator
description: >-
  Use this skill when starting, scoping, or unsure how to approach any SocialSeal
  task (strategy, setup, analysis, content production, or measurement). It is the
  lightweight entry point: it checks foundations first, routes to the right
  SocialSeal skill in the right order, and keeps the agent proactive instead of
  waiting for a perfectly specified request.
license: MIT
metadata:
  socialseal:
    phase: orchestration
  tags:
    - socialseal
    - orchestration
    - routing
    - workflow
    - getting-started
---

# SocialSeal Orchestrator

## Overview

This is the always-on router for SocialSeal work. Keep it light: its job is to figure out where the user is, check that foundations exist, and hand off to the right skill. It does not do the deep work itself.

SocialSeal concepts (personas, pillars, discoverability, share of voice, tracking groups, blueprints) are not widely understood. Be proactive: diagnose what is missing, explain it briefly, and offer to produce it with SocialSeal, rather than asking the user to supply perfect inputs.

## First move: choose access mode and check foundations

Before strategy or setup checks, confirm whether live SocialSeal tools are available:

- If `socialseal_list_workspaces`, `socialseal_list_available_tools`, and `socialseal_get_tool_schema` are available, use MCP mode. Start with workspace discovery and live registry/schema inspection.
- If no `socialseal_*` tools are available in Cowork or another non-technical environment, explain that the hosted SocialSeal connector is not connected or enabled. Tell the user to open **Customize** -> **Connectors**, click **+** -> **Add custom connector**, fill in **Name** `socialseal` and **Remote MCP server URL** `https://mcp.socialseal.co/mcp`, click **Add**/**Connect**, sign in, then retry.
- If the connector is unavailable, switch to file mode. Ask for SocialSeal CSV/JSON exports and continue with the skills that can work from files.
- If the user is in Claude Code or a developer environment, local stdio MCP and CLI are fallbacks. They require Node.js/`npx` and must be installed separately.

See `references/onboarding-and-auth.md` and `references/mcp-and-cli-usage.md`. Never print raw `ss_cli_...` keys in full; use only the final six characters.

Before any analysis or production, decide whether strategy and setup exist. If you are unsure, run `socialseal-strategy-readiness` first; it diagnoses strategy foundations (personas, pillars, brand voice, goals) and SocialSeal setup, and guides the user to define what is missing using SocialSeal research.

Do not stall on a missing input. Name it, explain it in a sentence, propose a SocialSeal-backed way to define it, then route.

## Routing map

- Missing `socialseal_*` tools in Cowork -> hosted connector setup from `references/onboarding-and-auth.md`, then retry workspace discovery
- Connector unavailable -> file mode with user-provided SocialSeal exports, then route to the best analysis skill
- Claude Code developer fallback -> local stdio MCP or CLI setup from `references/onboarding-and-auth.md`, then resume
- Invalid local MCP/CLI credentials -> device login from `references/onboarding-and-auth.md`, then resume
- Unclear request, or strategy/setup may be missing -> `socialseal-strategy-readiness`
- Need a workspace / tracking groups created or fixed -> `socialseal-workspace-setup`, `socialseal-tracking-group-design`
- "Where should we make content?" / gaps -> `socialseal-opportunity-analysis`
- "What are competitors/creators doing?" -> `socialseal-competitor-content-analysis`
- "Which creators should we partner with?" -> `socialseal-creator-discovery`
- "What's trending in local language vs English?" / catch micro-trends early -> `socialseal-bilingual-demand-monitoring`
- "Where is demand shifting?" / route budget and fast-track tour onboarding -> `socialseal-predictive-demand-routing`
- Turn opportunities into a plan -> `socialseal-social-plan-builder`
- Produce content (engine path): `socialseal-video-concepting` -> `socialseal-reference-video-analysis` -> `socialseal-blueprint-builder` -> `socialseal-creator-briefing` -> `socialseal-asset-planning` / `socialseal-generation-prompts` -> `socialseal-asset-studio-generation` -> `socialseal-capcut-export-prep`
- "How did it do?" / movement -> `socialseal-performance-readout`, `socialseal-discoverability-tracking`
- Decide next changes -> `socialseal-content-adjustment-recommendations`
- Brief leadership -> `socialseal-management-reporting`
- Turn a meeting/report into actions -> `socialseal-follow-up-planning`

## Workflow order (evidence-first)

Strategy & setup -> opportunity/competitor analysis -> plan -> production engine -> measurement -> recommendations/reporting -> follow-up. Production is grounded in real surfacing videos via the blueprint engine; do not jump to "write a content idea" when the engine exists. See `references/production-pipeline.md`.

## Hard rules to carry into every routed task

- Cite evidence in human-readable terms: `"keyword" [market, platform]`, video title/URL, `@handle`, group name. Keep `video_uid`/`search_result_id` as internal traceability only. See `references/socialseal-data-contract.md`.
- Be honest about evidence tiers: hard measurements are exact (not estimates), statistics carry selection bias (only high-ranking videos for tracked queries), and creative exemplars are anecdotal, not proof. See `references/evidence-and-confidence.md`.
- Reuse one `opportunityKey` across blueprint, brief, and asset.
- Never expose literal ids/tokens in shared artifacts; use placeholders.

## Do / Don't

Do:
- diagnose foundations before deep work and route accordingly
- stay proactive: teach the concept and offer to produce it
- hand off to one skill at a time and keep scope clear

Don't:
- do the deep analysis/production inside this skill
- wait for a perfect brief when you can guide the user to one
- proceed with analysis when strategy/setup is clearly missing
