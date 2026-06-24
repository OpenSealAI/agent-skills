# Changelog

## 0.2.0

- Added the SocialSeal vNext production engine across skills: new `socialseal-reference-video-analysis`, `socialseal-blueprint-builder`, and `socialseal-asset-studio-generation` skills (18 total).
- Rewired `socialseal-creator-briefing` to the vNext briefs engine, and re-anchored `socialseal-video-concepting`, `socialseal-asset-planning`, `socialseal-generation-prompts`, and `socialseal-capcut-export-prep` around blueprints, shot panels, the clip library, and FCPXML finishing.
- Documented MCP meta-tool usage (`socialseal_call_tool` etc.) and exact export-column attribution; added `references/production-pipeline.md` and `references/mcp-and-cli-usage.md`.
- Made skills self-contained by bundling cited references/templates per skill.
- Trimmed frontmatter to spec-recognized keys and fixed Claude Code `--plugin-dir` usage.

## 0.1.0

- Initial public SocialSeal Agent Skills scaffold.
