# Codex Usage

## Install the plugin

The native Codex package combines the repository's skills with the hosted SocialSeal
MCP server:

```bash
codex plugin marketplace add OpenSealAI/agent-skills
codex plugin add socialseal-agent-skills@socialseal-skills
```

Start a new Codex session after installation. If prompted, connect and sign in to
SocialSeal. The bundled MCP endpoint is `https://mcp.socialseal.co/mcp`; no local
Node.js or `npx` MCP process is required.

Example requests:

- Find what travellers search for on TikTok, Instagram, RedNote, and Douyin and show the content gaps.
- Turn this social-search demand into a short-form video and carousel plan.
- Benchmark competitor videos and draft a creator or UGC brief.
- Track our social-search discoverability and share of voice.

## Skills-only use

Use this repo as project context or copy selected `SKILL.md` files into the agent's
configured skills directory when live SocialSeal tools are not required. For terminal
workflows, let Codex inspect SocialSeal CLI help before running exports.

Skills-only installation does not connect the SocialSeal MCP server. Use SocialSeal
CSV/JSON exports in file mode if no live connection is available.
