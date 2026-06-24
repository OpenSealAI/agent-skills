---
name: socialseal-strategy-readiness
description: >-
  Use this skill when checking whether a brand has the strategy foundations (target
  personas, content pillars, brand voice, measurable goals) and a correct SocialSeal
  setup before analysis or production, and to guide the user through defining what is
  missing using SocialSeal research. It explains each concept in plain language and
  proposes concrete, SocialSeal-backed ways to produce it rather than asking the user
  to supply perfect inputs.
license: MIT
metadata:
  socialseal:
    phase: orchestration
  tags:
    - socialseal
    - orchestration
    - readiness
    - strategy
    - personas
    - pillars
---

# SocialSeal Strategy Readiness

## Overview

Most SocialSeal skills assume a strategy and a working setup already exist. Often they do not, and the concepts are unfamiliar. This skill diagnoses readiness and guides the user to fill gaps. Guiding means teaching the concept and proposing a concrete, SocialSeal-backed way to define it, not asking "please input your personas."

`socialseal-orchestrator` routes here when strategy or setup may be missing. See `references/strategy-foundations.md` for the concept definitions and derivation methods, and `references/evidence-and-confidence.md` for how to talk about what the data can and cannot prove.

## When to Use

- A request assumes personas, pillars, brand voice, or goals that may not exist.
- A new brand/workspace with no clear strategy.
- Before opportunity analysis or production, to confirm the inputs are real.
- The user seems unsure what SocialSeal concepts mean.

## Readiness diagnosis

Assess two halves and report each as ready / partial / missing.

### Strategy foundations
- **Target personas:** named viewers with a job-to-be-done and hesitations, not just demographics.
- **Content pillars:** 3-5 durable themes, each tied to real tracked search demand.
- **Brand voice:** tone, point of view, and hard constraints (claims to avoid).
- **Goal / measurement intent:** which pillars/keywords, market, and platform to improve, with a baseline.

### SocialSeal setup
- correct workspace selected
- clean tracking groups (one platform, one market/language, one intent) covering the priority pillars
- groups have items, a baseline run, and exports that produce rows (or a known empty reason)

## Guided workflow

1. **Diagnose.** State what exists, what is partial, and what is missing across both halves. Use what the user said plus any SocialSeal access (list workspaces/groups, inspect exports).
2. **Explain the gap.** For each missing foundation, give a one or two sentence plain-language explanation of what it is and why it matters. Do not assume the term is understood.
3. **Propose a SocialSeal-backed way to define it.** Concretely:
   - **Personas:** run a search journey on the category, read which questions/jobs surface, cluster keywords, and propose 2-4 personas grounded in real search behavior for the user to confirm.
   - **Pillars:** cluster the tracked keyword set and surfaced content into 3-5 candidate pillars relevant to the user's brand and product USPs, each validated for search demand and a presence gap.
   - **Brand voice:** ask for existing guidelines; if none, draft a short voice note from how the brand talks on their website and in existing social videos, or from high-surfacing creator tone in the category, then confirm.
   - **Goals:** pick priority pillars/keywords and capture the current measured discoverability/SOV baseline so movement is checkable.
4. **Offer, do not demand.** Present the proposal and ask the user to confirm or adjust. If they already have a foundation, capture it and move on.
5. **Route.** Hand off to the right skill: `socialseal-workspace-setup` and `socialseal-tracking-group-design` for setup gaps; `socialseal-opportunity-analysis` to turn readiness into opportunities; the production chain once foundations hold.

## Output

- a short readiness report: each foundation and setup item marked ready / partial / missing
- for each gap: a one-line explanation and a proposed SocialSeal-backed way to define it
- a confirmed or draft set of personas, pillars, voice note, and goal where the user engaged
- the recommended next skill and why

## Do / Don't

Do:
- explain every unfamiliar concept in plain language before asking about it
- propose to produce missing foundations with SocialSeal research, then confirm with the user
- ground proposed personas/pillars in real surfaced search behavior, not invention
- be honest that proposed personas/pillars are hypotheses to validate (see `references/evidence-and-confidence.md`)

Don't:
- ask the user to "input personas/pillars" with no explanation or help
- invent personas or pillars with no search evidence and present them as fact
- block all progress on one missing input when you can guide the user to it
- skip the setup half; a strategy with no clean tracking groups cannot be measured

## Verification Checklist

- [ ] Both halves (strategy foundations + SocialSeal setup) were diagnosed.
- [ ] Every missing foundation got a plain-language explanation.
- [ ] Each gap has a concrete, SocialSeal-backed proposal, not just a request for input.
- [ ] Proposed foundations are labeled as hypotheses to confirm.
- [ ] A specific next skill was recommended.
