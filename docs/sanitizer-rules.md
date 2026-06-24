# Sanitizer Rules

Before publishing any skill, reference, template, script, or example, remove or replace:

- Client, partner, employee, creator, or stakeholder names.
- Workspace IDs, tracking group IDs, tracking item IDs, Google object IDs, video IDs, and chat IDs.
- Google Docs/Sheets/Slides/Drive links.
- Internal chat, email, or ticket references.
- Private task folders, local profile names, or private skill-library paths.
- Private metrics, unpublished campaign results, contract details, and relationship-history notes.
- Internal postmortem, blame, escalation, or recovery language.
- API keys, tokens, cookies, OAuth file paths, or credential instructions not intended for public docs.

Use placeholders such as `{{BRAND}}`, `{{MARKET}}`, `{{PLATFORM}}`, `{{WORKSPACE_ID}}`, `{{TRACKING_GROUP_ID}}`, `{{KEYWORD_SET}}`, and `{{CAMPAIGN_PERIOD}}`.

Public skills may reference the public SocialSeal MCP server, the public SocialSeal CLI, or files the user provides. They must not reference private local skills or private internal paths.
