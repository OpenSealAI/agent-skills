# Integration Guide

## MCP mode

Use MCP mode when the agent can access the SocialSeal MCP server. Load named
operations through the host's tool search and inspect their live schemas. Resolve
the authorised workspace with `socialseal_get_current_workspace` or
`socialseal_list_workspaces`, then call the operation with typed top-level arguments.
Use `socialseal_get_tool_status` or the operation's named read for async runs;
polling does not authorise restarting paid work. Reach enriched evidence rows via
`socialseal_export_report` (`search_results_enriched`) or
`socialseal_export_tracking_data`. See `../references/mcp-and-cli-usage.md`.

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

Claude Cowork uses the hosted endpoint as a custom connector. Claude Code uses the
same endpoint through the plugin's `.mcp.json` and signs in with `/mcp`.

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
6. Video concepting (define the Study subject)
7. Reference video analysis (start a Study, approve any Video DNA price, read its evidence)
8. Creator briefing (generate the brief from the Study)
9. Asset planning (plan clips for the brief's shots)
10. Generation prompts (write prompts for external tools to fill shot gaps)
11. Source-clip preparation and editor handoff (brief, approved shot coverage, footage, and delivery specs)
12. Performance readout
13. Discoverability tracking
14. Content adjustment, management reporting, and follow-up planning

The production stages (6-11) are joined by a single `opportunityKey`. See `../references/production-pipeline.md`.
For an approved carousel concept, branch after evidence/benchmark selection into
`socialseal-carousel-production`: visual direction -> asset choices -> prototype ->
rendered/verified slides.
Use `../references/creative-production-gates.md` for large production requests and
delivery-state/QA rules.
