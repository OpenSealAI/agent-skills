# ChatGPT and Codex Plugin Submission

Use this checklist when publishing a new SocialSeal version to the universal
Plugins Directory shared by ChatGPT and Codex.

## Package

- Use `.codex-plugin/plugin.json` as the native plugin manifest.
- Include `skills/` and the root `.mcp.json` in the submitted package.
- Keep `.claude-plugin/` for Claude and legacy-compatible marketplace installs.
- Run `python scripts/validate_public_repo.py` and the Codex plugin validator
  before packaging.

## Submission type

Choose **With MCP**, not **Skills only**. Enter the universal production MCP URL:

```text
https://mcp.socialseal.co/mcp
```

Do not submit a pre-existing integration ID or a placeholder `plugin_asdk_app...`
value. ChatGPT creates that identifier only for local developer-mode connections;
the public submission scans the MCP server URL directly.

Complete OAuth configuration, domain verification, tool scanning, tool annotations,
review credentials, privacy and terms fields, regional availability, and release
notes in the OpenAI submission portal.

## Listing copy

Copy the customer-facing name, descriptions, keywords, category, website, legal
links, and starter prompts from `.codex-plugin/plugin.json` into the submission.
The public directory uses a reviewed metadata snapshot, so committing new repository
copy does not update an already-published listing.

## Discovery evaluation

Use `tests/plugin-discovery-prompts.json` as the baseline. Before submission and
again after publication:

1. Search the directory with every positive phrase and record whether SocialSeal is
   returned and its position.
2. Install the plugin, start a new task, and test representative indirect requests
   without naming SocialSeal.
3. Confirm the negative prompts do not route into unsupported posting, inbox, or
   paid-media operations.
4. Record the tested plugin version, date, product surface, locale, and result so
   changes can be compared across releases.

The submission itself must also include at least five positive and three negative
test cases with expected behaviour and reproducible inputs.
