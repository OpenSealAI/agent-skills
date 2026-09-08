# Integration Guide

## MCP mode

Use MCP mode when the agent can access the SocialSeal MCP server. The server exposes stable meta-tools; backend functions are invoked through `socialseal_call_tool`. The loop is: `socialseal_list_workspaces` -> `socialseal_list_available_tools` -> `socialseal_get_tool_schema` (before any mutating call) -> `socialseal_call_tool` -> `socialseal_get_tool_status` for async runs. There is no group-evidence/search-results MCP tool; reach enriched rows via `socialseal_export_report` (`search_results_enriched`) or `socialseal_export_tracking_data`. See `../references/mcp-and-cli-usage.md`.

### ChatGPT and Codex

The native plugin manifest at `../.codex-plugin/plugin.json` bundles the hosted
streamable HTTP server through `../.mcp.json`. Install the plugin, follow the
SocialSeal connection/authentication prompt, and start a new task or session. Public
directory releases must be submitted as **With MCP** using
`https://mcp.socialseal.co/mcp`; a repository update alone does not refresh the
reviewed public MCP snapshot.

For local ChatGPT developer testing, enable Developer mode and register the hosted
endpoint in the Plugins page. ChatGPT generates a `plugin_asdk_app...` connection ID
for any local `.app.json` mapping; do not invent or commit a placeholder ID.

### Claude

Claude Cowork uses the hosted endpoint as a custom connector. Claude Code may use
the local stdio `@socialseal/mcp-server` developer fallback documented in the README.

## CLI mode

Use CLI mode when the agent has terminal access and the SocialSeal CLI is installed. The agent should run the CLI help command first, export data to local CSV/JSON, and save raw exports before analysis.

## Export-file mode

Use export-file mode when the user provides CSV/JSON. The agent should inspect columns, data grain, date range, markets, platforms, and keywords before calculating metrics.

## Recommended workflow order

1. Workspace setup
2. Tracking group design
3. Opportunity analysis
4. Competitor/content analysis
4a. Creator discovery (shortlist partners by search authority)
4b. Bilingual demand monitoring (local-vs-English split, micro-trends)
4c. Predictive demand routing (early signals for resource allocation and tour onboarding)
5. Social plan builder
6. Video concepting (define scope / retrievalPrompt)
7. Reference video analysis (identify + analyze exemplars)
8. Blueprint builder (compile best-practices blueprint)
9. Creator briefing (generate brief from blueprint)
10. Asset planning (plan clips for blueprint shots)
11. Generation prompts (write prompts for external tools to fill shot gaps)
12. Source-clip preparation and editor handoff (brief, approved panel coverage, footage, and delivery specs)
13. Performance readout
14. Discoverability tracking
15. Content adjustment, management reporting, and follow-up planning

The production stages (6-12) are joined by a single `opportunityKey`. See `../references/production-pipeline.md`.
For an approved carousel concept, branch after evidence/benchmark selection into
`socialseal-carousel-production`: visual direction -> asset choices -> prototype ->
rendered/verified slides.
Use `../references/creative-production-gates.md` for large production requests and
delivery-state/QA rules.
