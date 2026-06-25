# Integration Guide

## MCP mode

Use MCP mode when the agent can access the SocialSeal MCP server. The server exposes stable meta-tools; backend functions are invoked through `socialseal_call_tool`. The loop is: `socialseal_list_workspaces` -> `socialseal_list_available_tools` -> `socialseal_get_tool_schema` (before any mutating call) -> `socialseal_call_tool` -> `socialseal_get_tool_status` for async runs. There is no group-evidence/search-results MCP tool; reach enriched rows via `socialseal_export_report` (`search_results_enriched`) or `socialseal_export_tracking_data`. See `../references/mcp-and-cli-usage.md`.

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
11. Generation prompts (fill shot gaps with reference clips)
12. Asset Studio generation (assemble rough cut, export FCPXML)
13. CapCut export prep (finish the exported cut)
14. Performance readout
15. Discoverability tracking
16. Content adjustment, management reporting, and follow-up planning

The production stages (6-13) are joined by a single `opportunityKey`. See `../references/production-pipeline.md`.
