# SocialSeal Onboarding and Auth

Choose the onboarding path by environment. Cowork and non-technical users use the hosted remote MCP connector first. Claude Code developers can use local stdio MCP as a developer fallback. File mode remains available when no live connector is present.

## Connector-first setup for Cowork

First use the host's available tool search/discovery facilities to look for SocialSeal actions. Use this setup path only when discovery or connection status confirms the connector is unavailable:

1. Tell the user the SocialSeal connector is not connected or enabled in this conversation.
2. Ask them to open **Customize** -> **Connectors**.
3. Ask them to click **+** -> **Add custom connector**.
4. Ask them to fill in **Name** `socialseal` and **Remote MCP server URL** `https://mcp.socialseal.co/mcp`.
5. Ask them to click **Add**/**Connect** and sign in to SocialSeal.
6. After they connect, retry `socialseal_list_workspaces`.

Do not ask Cowork users to install Node.js, run `npx`, or configure local MCP. The local stdio MCP server (`@socialseal/mcp-server`) is an npm-based developer fallback that needs Node.js/`npx`; the remote connector at `https://mcp.socialseal.co/mcp` needs none of that.

## Missing live tools

Treat these as live-tool setup triggers:

- Host discovery confirms no SocialSeal tools are available.
- Workspace discovery is unavailable after host tool discovery.
- The hosted connector reports disconnected or expired authentication. A forbidden operation can instead mean missing workspace permission; retain that specific error.
- Local stdio MCP reports a missing SocialSeal API key.
- Backend calls return `401` for the configured key. For `403`, inspect the permission error rather than assuming reconnecting will grant access.

When live tools are missing, give the right next step:

- Cowork / non-technical users: connect the hosted SocialSeal connector.
- Claude Code developers: install the local stdio MCP fallback.
- No connector or terminal access: switch to file mode with SocialSeal CSV/JSON exports.

## Local stdio MCP developer fallback

Use this only for Claude Code or developer environments that can run Node.js and `npx`:

```bash
claude mcp add --transport stdio socialseal -- npx -y @socialseal/mcp-server
```

Then use local device login if credentials are missing.

## Device login flow for local MCP

1. Call `socialseal_start_login`.
2. Give the user `verification_uri_complete` and ask them to confirm the short `user_code`.
3. Call `socialseal_poll_login` with the returned `device_code`.
4. After approval, the MCP server stores the key in `~/.config/socialseal/config.json` with local-only file permissions.

Never print a raw `ss_cli_...` key in full. Show only the final six characters when you need to identify a key.

## File mode fallback

If no connector is available, ask the user for SocialSeal exports such as tracking CSVs, enriched search-results CSVs, report JSON, or workspace setup notes. In file mode, inspect the supplied columns, date ranges, markets, platforms, and keywords before analysis. Be clear that file mode can analyze supplied exports but cannot start new SocialSeal jobs, poll live status, or create/update workspaces.

## Free-first billing

New users start on the free tier after browser signup or login. Do not ask for payment during first setup.

For hosted connector users in Cowork or Claude web, billing changes happen in the SocialSeal app. If a connector call reports exhausted credits, quota, plan, billing, or entitlement limits, ask the user to open SocialSeal billing from the app/account UI, upgrade or add credits, then retry the original action.

Local MCP users also manage billing in the SocialSeal app/account UI.
