# Changelog

## Unreleased

- Aligned with SOC-349 retirement: removed Asset Studio generation and CapCut/FCPXML skills from active distribution.
- Retained blueprint/brief generation and source-clip upload/read; updated routing and bundled references to deliver an editor handoff without retired mapping, creative-pack, or generated-asset calls.

## 0.7.0

- Added a native ChatGPT/Codex plugin manifest and bundled hosted SocialSeal MCP configuration.
- Expanded marketplace discovery metadata for social video, short-form video, TikTok, Instagram, Xiaohongshu/XiaoHongShu/RedNote, Douyin, creator/UGC, content strategy, competitor analysis, and discoverability jobs.
- Split installation guidance by ChatGPT/Codex, Claude Cowork, Claude Code, and skills-only use.
- Documented the OpenAI **With MCP** submission requirement and local ChatGPT developer-mode connection flow.
- Added a discovery regression fixture and public submission checklist.

## 0.6.0

- Rewrote all 23 existing skill descriptions around concrete user-language triggers
  so SocialSeal routing activates for content plans, videos/carousels, benchmark
  requests, asset-bank production, search-demand questions, creator discovery, and
  measurement work even when the user does not name the internal skill.
- Added shared creative-production gates: delivery contracts, brand utility,
  demand/topic choices, benchmark and tiered Video DNA choices, rights/location-aware
  asset selection, representative prototypes, final QA, precise delivery states, and
  a workflow audit manifest.
- Added `socialseal-carousel-production` (24 skills total) for evidence-grounded
  carousel creative direction, asset mapping, prototype approval, rendered slide
  production, mobile-view verification, and post-ready QA. It explicitly rejects
  ungrounded AI-template defaults and unverified location imagery.
- Strengthened strategy readiness with a brand utility bank and hard exclusions;
  added a focused one-off versus reusable setup branch when no tracking group exists;
  and prevented briefs, shot lists, blueprints, or Asset Studio rough cuts from being
  mislabeled as finished content.

## 0.5.0

- Made discoverability / share-of-voice measurement a first-class, findable workflow: rewrote `socialseal-discoverability-tracking` so it measures a brand-vs-competitor snapshot (keyword coverage, rank-weighted and views-weighted share of voice, best rank) as well as tracking over time. It now bundles `references/metrics-glossary.md`, defines the last-mile computation with a worked example, requires metric tables and a chart (via the `dataviz` skill), and leads ranked data access with `search_results_enriched`.
- Fixed routing so visibility-measurement questions reach the right skill: `socialseal-orchestrator` now routes "how do we compare with <competitor> on discoverability / share of voice?" to `socialseal-discoverability-tracking`, instructs the agent to load the routed skill's instructions, and `socialseal-competitor-content-analysis` now guards against answering measurement questions with a content-pattern matrix.
- Added "share of voice" to the `socialseal-opportunity-analysis` description so the skill is discoverable for visibility-gap work.

## 0.4.1

- Fixed the Claude marketplace manifest so `OpenSealAI/agent-skills` syncs: the plugin `source` now uses the required `./` prefix (Claude rejected the previous `"."` at sync time with "Marketplace sync failed"), and the non-standard `displayName` field was removed for compatibility with older Claude clients. The plugin now appears in the marketplace as `socialseal-agent-skills`.

## 0.4.0


- Added three strategy skills that close gaps in creator sourcing and demand sensing (23 skills total): `socialseal-creator-discovery` (shortlist creator-shop partners by market, language, and destination/topic authority using enriched ranked search rows and rank-weighted surfacing instead of follower/vanity metrics), `socialseal-bilingual-demand-monitoring` (map the explicit local-language vs English search-demand split across language-clean tracking groups, bridge terms via search-journey `englishGloss`/`canonicalKeyword`, and catch micro-trends early), and `socialseal-predictive-demand-routing` (source early leading-indicator signals via periodic `search-journey-run` and `google-ai-search` runs plus rank/surfacing velocity to back campaign resource allocation and fast-track activity/tour onboarding).
- Grounded the new skills in live-validated tool behavior: `search_results_enriched` exports for creator authority, async `search-journey-run` (poll `journey_run`) for keyword expansion with per-keyword language/gloss/score, and `get-google-ai-search-runs`/`get-google-ai-search-results` for numeric Google AI runs. Documented gotchas (row-level `language` can be blank; `creator_signatures`/`cluster_insights` require a precomputed `clusterRequest`; synchronous journeys can 504; numeric AI-run status uses the dedicated read function).
- Bundled the cited references into each new skill directory so single-skill installs remain self-contained.

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
