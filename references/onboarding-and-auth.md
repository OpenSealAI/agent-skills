# SocialSeal Onboarding and Auth

Choose the onboarding path by environment. Cowork and non-technical users use the hosted remote MCP connector first. Claude Code developers can use local stdio MCP or CLI as fallbacks. File mode remains available when no live connector is present.

## Connector-first setup for Cowork

Use this path when SocialSeal `socialseal_*` tools are missing in Cowork, Claude web, or a non-technical setup:

1. Tell the user the SocialSeal connector is not connected or enabled in this conversation.
2. Ask them to open **Customize** -> **Connectors**.
3. Ask them to click **+** -> **Add custom connector**.
4. Ask them to fill in **Name** `socialseal` and **Remote MCP server URL** `https://mcp.socialseal.co/mcp`.
5. Ask them to click **Add**/**Connect** and sign in to SocialSeal.
6. After they connect, retry `socialseal_list_workspaces`.

Do not ask Cowork users to install Node.js, run `npx`, or configure local MCP. The local stdio MCP server (`@socialseal/mcp-server`) is an npm-based developer fallback that needs Node.js/`npx`; the remote connector at `https://mcp.socialseal.co/mcp` needs none of that.

## Missing live tools

Treat these as live-tool setup triggers:

- No `socialseal_*` tools are available.
- `socialseal_list_workspaces` is unavailable.
- The hosted connector reports disconnected, unauthorized, or forbidden.
- Local stdio MCP reports a missing SocialSeal API key.
- CLI exits with auth code `3`, or says to run `socialseal login`.
- Backend calls return `401` or `403` for the configured key.

When live tools are missing, give the right next step:

- Cowork / non-technical users: connect the hosted SocialSeal connector.
- Claude Code developers: install the local stdio MCP fallback or use CLI.
- No connector or terminal access: switch to file mode with SocialSeal CSV/JSON exports.

## Local stdio MCP developer fallback

Use this only for Claude Code or developer environments that can run Node.js and `npx`:

```bash
claude mcp add --transport stdio socialseal -- npx -y @socialseal/mcp-server
```

Then use local device login if credentials are missing.

## Device login flow for local MCP and CLI

CLI:

```bash
npx -y @socialseal/cli login
npx -y @socialseal/cli whoami
```

MCP:

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

For Claude Code developers using the local CLI fallback, the CLI can open billing:

```bash
npx -y @socialseal/cli billing
```

Do not give the `npx` billing command as the primary path for hosted connector users.
