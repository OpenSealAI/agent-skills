# Changelog

## 0.3.0

- Added a lightweight always-on `socialseal-orchestrator` entry-point skill that checks foundations first and routes to the right skill in the right order, plus a `socialseal-strategy-readiness` skill that diagnoses strategy foundations (personas, pillars, brand voice, goals) and SocialSeal setup and guides the user to define what is missing using SocialSeal research (20 skills total).
- Made attribution human-readable across skills: cite `"keyword" [market, platform]`, video title/URL, and `@author_handle`; `video_uid`/`search_result_id` are demoted to an internal traceability note.
- Added `references/evidence-and-confidence.md` defining three evidence tiers (hard measurements that are exact not estimates, scoped statistics with selection bias, and anecdotal creative exemplars), threaded through the analysis and creative skills to prevent over/underconfidence.
- Added `references/strategy-foundations.md` (plain-language concept glossary and SocialSeal-backed derivation methods); updated `references/socialseal-data-contract.md` and `references/metrics-glossary.md`.

## 0.2.0

- Added the SocialSeal vNext production engine across skills: new `socialseal-reference-video-analysis`, `socialseal-blueprint-builder`, and `socialseal-asset-studio-generation` skills (18 total).
- Rewired `socialseal-creator-briefing` to the vNext briefs engine, and re-anchored `socialseal-video-concepting`, `socialseal-asset-planning`, `socialseal-generation-prompts`, and `socialseal-capcut-export-prep` around blueprints, shot panels, the clip library, and FCPXML finishing.
- Documented MCP meta-tool usage (`socialseal_call_tool` etc.) and exact export-column attribution; added `references/production-pipeline.md` and `references/mcp-and-cli-usage.md`.
- Made skills self-contained by bundling cited references/templates per skill.
- Trimmed frontmatter to spec-recognized keys and fixed Claude Code `--plugin-dir` usage.

## 0.1.0

- Initial public SocialSeal Agent Skills scaffold.
