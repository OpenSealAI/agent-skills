---
name: socialseal-orchestrator
description: >-
  Use this skill when starting, scoping, or unsure how to approach any SocialSeal
  task (strategy, setup, analysis, content production, or measurement). It is the
  lightweight entry point: it checks foundations first, routes to the right
  SocialSeal skill in the right order, and keeps the agent proactive instead of
  waiting for a perfectly specified request.
license: MIT
metadata:
  socialseal:
    phase: orchestration
  tags:
    - socialseal
    - orchestration
    - routing
    - workflow
    - getting-started
---

# SocialSeal Orchestrator

## Overview

This is the always-on router for SocialSeal work. Keep it light: its job is to figure out where the user is, check that foundations exist, and hand off to the right skill. It does not do the deep work itself.

SocialSeal concepts (personas, pillars, discoverability, share of voice, tracking groups, blueprints) are not widely understood. Be proactive: diagnose what is missing, explain it briefly, and offer to produce it with SocialSeal, rather than asking the user to supply perfect inputs.

## First move: check foundations, do not assume them

Before any analysis or production, decide whether strategy and setup exist. If you are unsure, run `socialseal-strategy-readiness` first; it diagnoses strategy foundations (personas, pillars, brand voice, goals) and SocialSeal setup, and guides the user to define what is missing using SocialSeal research.

Do not stall on a missing input. Name it, explain it in a sentence, propose a SocialSeal-backed way to define it, then route.

## Routing map

- Unclear request, or strategy/setup may be missing -> `socialseal-strategy-readiness`
- Need a workspace / tracking groups created or fixed -> `socialseal-workspace-setup`, `socialseal-tracking-group-design`
- "Where should we make content?" / gaps -> `socialseal-opportunity-analysis`
- "What are competitors/creators doing?" -> `socialseal-competitor-content-analysis`
- Turn opportunities into a plan -> `socialseal-social-plan-builder`
- Produce content (engine path): `socialseal-video-concepting` -> `socialseal-reference-video-analysis` -> `socialseal-blueprint-builder` -> `socialseal-creator-briefing` -> `socialseal-asset-planning` / `socialseal-generation-prompts` -> `socialseal-asset-studio-generation` -> `socialseal-capcut-export-prep`
- "How did it do?" / movement -> `socialseal-performance-readout`, `socialseal-discoverability-tracking`
- Decide next changes -> `socialseal-content-adjustment-recommendations`
- Brief leadership -> `socialseal-management-reporting`
- Turn a meeting/report into actions -> `socialseal-follow-up-planning`

## Workflow order (evidence-first)

Strategy & setup -> opportunity/competitor analysis -> plan -> production engine -> measurement -> recommendations/reporting -> follow-up. Production is grounded in real surfacing videos via the blueprint engine; do not jump to "write a content idea" when the engine exists. See `references/production-pipeline.md`.

## Hard rules to carry into every routed task

- Cite evidence in human-readable terms: `"keyword" [market, platform]`, video title/URL, `@handle`, group name. Keep `video_uid`/`search_result_id` as internal traceability only. See `references/socialseal-data-contract.md`.
- Be honest about evidence tiers: hard measurements are exact (not estimates), statistics carry selection bias (only high-ranking videos for tracked queries), and creative exemplars are anecdotal, not proof. See `references/evidence-and-confidence.md`.
- Reuse one `opportunityKey` across blueprint, brief, and asset.
- Never expose literal ids/tokens in shared artifacts; use placeholders.

## Do / Don't

Do:
- diagnose foundations before deep work and route accordingly
- stay proactive: teach the concept and offer to produce it
- hand off to one skill at a time and keep scope clear

Don't:
- do the deep analysis/production inside this skill
- wait for a perfect brief when you can guide the user to one
- proceed with analysis when strategy/setup is clearly missing
