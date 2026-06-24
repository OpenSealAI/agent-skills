# Skill Authoring Notes

This repo follows the Agent Skills open specification:

- Every skill is `skills/<skill-name>/SKILL.md`.
- `name` must match the parent directory.
- `description` starts with “Use this skill when...” and stays below 1024 characters.
- Frontmatter is trimmed to spec-recognized keys: `name`, `description`, `license`, and `metadata` (we keep `metadata.socialseal.phase` and `metadata.tags`). Do not add non-spec top-level keys such as `version`, `author`, or `compatibility`.
- Skills are concise and rely on progressive disclosure.
- Detailed examples and schemas live in `references/` or `templates/`.
- Never put literal IDs/UUIDs, tokens, or emails in any file; the validator blocks them. Use placeholders like `<workspace-id>`, `<blueprint-id>`, `<opportunity-key>`.

Resource packaging (self-contained skills):

- The root `references/` and `templates/` directories are canonical.
- Each skill that cites a reference/template by relative path also carries a copy under `skills/<skill-name>/references/` or `skills/<skill-name>/templates/`, so single-skill installs remain self-contained.
- When you edit a canonical reference/template, re-copy it into the skill dirs that cite it (see the copy map in the repo history) to avoid drift.

Claude Code plugin compatibility:

- `.claude-plugin/plugin.json` is at repository root.
- Skills are direct children of `skills/`, not nested by category.
- Plugin invocation will be namespaced by the plugin name.

skills.sh compatibility:

- Public GitHub repo with standard skill directories.
- README includes `npx skills add owner/repo` and a badge placeholder.
- Validation rejects private IDs, private paths, and likely secrets.
