# SocialSeal Onboarding and Auth

Every Claude surface uses the hosted SocialSeal connector at `https://mcp.socialseal.co/mcp`, which the SocialSeal plugin bundles. Users sign in through SocialSeal's OAuth page; no API key is copied, stored, or pasted. File mode remains available when no live connector is present.

## Connector-first setup for Cowork

First use the host's available tool search/discovery facilities to look for SocialSeal actions. Use this setup path only when discovery or connection status confirms the connector is unavailable:

1. Tell the user the SocialSeal connector is not connected or enabled in this conversation.
2. Ask them to open **Customize** -> **Connectors**.
3. Ask them to click **+** -> **Add custom connector**.
4. Ask them to fill in **Name** `socialseal` and **Remote MCP server URL** `https://mcp.socialseal.co/mcp`.
5. Ask them to click **Add**/**Connect** and sign in to SocialSeal.
6. After they connect, retry `socialseal_list_workspaces`.

Do not ask Cowork users to install Node.js, run `npx`, or configure local MCP. The hosted connector needs none of that.

## Missing live tools

Treat these as live-tool setup triggers:

- Host discovery confirms no SocialSeal tools are available.
- Workspace discovery is unavailable after host tool discovery.
- The hosted connector reports disconnected or expired authentication. A forbidden operation can instead mean missing workspace permission; retain that specific error.
- A call asks the user to connect or sign in to SocialSeal. For a forbidden (`403`) result, inspect the permission error rather than assuming reconnecting will grant access.

When live tools are missing, give the right next step:

- Cowork / non-technical users: connect the hosted SocialSeal connector.
- Claude Code users: run `/mcp`, select `socialseal`, and sign in.
- No connector or terminal access: switch to file mode with SocialSeal CSV/JSON exports.

## Claude Code

The SocialSeal plugin adds the hosted connector to Claude Code. Without the plugin, the user can add it with:

```bash
claude mcp add --transport http socialseal https://mcp.socialseal.co/mcp
```

Ask the user to run `/mcp`, select `socialseal`, and sign in in the browser window that opens, then retry the original action.

## File mode fallback

If no connector is available, ask the user for SocialSeal exports such as tracking CSVs, enriched search-results CSVs, report JSON, or workspace setup notes. In file mode, inspect the supplied columns, date ranges, markets, platforms, and keywords before analysis. Be clear that file mode can analyze supplied exports but cannot start new SocialSeal jobs, poll live status, or create/update workspaces.

## Free-first billing

New users start on the free tier after browser signup or login. Do not ask for payment during first setup.

For hosted connector users in Cowork or Claude web, billing changes happen in the SocialSeal app. If a connector call reports exhausted credits, quota, plan, billing, or entitlement limits, ask the user to open SocialSeal billing from the app/account UI, upgrade or add credits, then retry the original action.
