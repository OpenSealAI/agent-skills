---
name: socialseal-social-plan-builder
description: 'Use this skill when the user asks for a SocialSeal-informed content
  plan, content calendar, editorial calendar, posting schedule, social plan, campaign plan, content pillars, posting/production queue, or a
  set of videos and carousels tied to search demand. Convert opportunity and benchmark
  evidence into prioritized content slots, briefs, asset needs, owners, and
  measurement mapping; do not generate a generic calendar.'
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
  - socialseal
  - strategy
  - social-plan
  - content-calendar
  - measurement-mapping
---

# SocialSeal Social Plan Builder

## Overview

A SocialSeal social plan is an evidence-backed production and measurement plan. It should say what to create, why that content is needed, which keywords/topics it supports, and how SocialSeal will measure whether visibility improves.

The plan is not a generic calendar. Each slot should identify its intended audience, viewer job, useful takeaway and evidence. Link tracking where available; mark untracked topics as measurement gaps rather than excluding a user-prioritised topic or inventing validation. A calendar request belongs here even when the user never says "social plan". Calendar composition is guidance-led; do not assume a calendar-generation tool exists.

Read `references/creative-production-gates.md` when the plan will lead directly to
videos or carousels. Require confirmed foundations, a brand utility bank, demand
evidence, and benchmark patterns before calling the plan production-ready.

## Inputs

- opportunity analysis
- competitor/content pattern matrix
- confirmed brand utility bank and exclusions
- tracking group IDs and keyword/topic scope
- platform and market priorities
- production capacity and available creators/assets
- reporting cadence

## Workflow

1. **Recover the current agreement.** Read the user's existing calendar and approved context first. Retain the date range/time zone, weekly cadence, audience priorities, voice/CTA, exclusions, owner, available assets and latest brief versions. A scheduled date does not establish that a post is published. Ask only about conflicts that prevent a useful plan; label assumptions.
2. **Assess relevant evidence.** Combine scoped SocialSeal observations with supplied audience questions, verified brand/product facts and insider knowledge. Separate a topic's popularity from evidence supporting a particular audience recommendation. Views on surfaced videos are not search volume. Reuse adequate evidence instead of rerunning research merely to fill a column.
3. **Choose content jobs and treatments.** For each candidate state who it helps, the decision/question it addresses, the hook promise, useful payoff and why this treatment fits the audience. A keyword citation alone does not make a generic idea useful. Reference formats are hypotheses to adapt, not proven recipes. Preserve the requested mix of utility, mood and other content jobs.
4. **Set the mix before expanding.** Use the user's chosen direction and capacity. Offer alternatives only when a consequential choice remains open. Do not invent audience percentages or make every researched topic a commitment. Check a representative concept against the user's request before expanding a large batch.
5. **Schedule the selected slots.** Preserve the user's table layout; add missing information without repeatedly changing the format. Respect priority/front-loading instructions. Distinguish available footage from proposed capture or unverified sources. Keep candidates separate from scheduled posts.
6. **Hand selected slots to briefing.** Load `socialseal-creator-briefing` for video/editor briefs and discover the current generation actions. Carry the audience, promise, evidence, constraints and stable opportunity identity into the brief. Spreadsheet/Word packaging does not replace brief generation. A calendar-only request does not authorise generating every brief.
7. **Validate the complete revised calendar.** Check dates, agreed weekly boundaries, counts, gaps, duplicate concepts, owner/asset feasibility and title-hook-payoff agreement. Moving one post requires checking both affected weeks. Only claim a rolling-window check if that was the requested rule and every such window was checked.
8. **Deliver one current version.** Record which calendar/brief versions were updated and any copies that remain stale or inaccessible. Carry changed audience/CTA/format decisions into hooks, scripts, assets and linked briefs within scope, not just labels. Report unresolved conflicts and what was actually checked. Retain the agreed measurement/review cadence without inventing dates.

## Output

A plan that can be pasted into a sheet or project tracker:

- date and scheduling status (candidate / scheduled / published only with evidence)
- pillar
- audience/search job
- target keywords/topics
- platform/market
- hook promise and useful payoff
- format and duration or slide count
- content lens
- owner and asset availability / capture needs
- linked brief and current version, when present
- measurement/tracking group
- evidence reference (video title/URL, `@handle`, `"keyword" [market, platform]`)
- brand utility/proof and approval status

Use `templates/social-plan-template.md` if available. Evidence describes the observed search surface and scoped coverage gaps; it does not measure total search demand. The creative direction is an indicative bet to test. See `references/evidence-and-confidence.md`.

## Do / Don't

Do:

- make every slot traceable to SocialSeal evidence
- preserve user decisions; do not turn every candidate opportunity into a committed slot
- balance utility/practical and aspirational content
- keep cadence realistic for available creators/assets
- include a measurement column from the start

Don't:

- produce “3 posts per week” without saying what they answer
- call a plan, brief queue, or asset list finished content
- describe untracked content as measured; identify its measurement gap
- overfit to one competitor example
- use the plan as a posting automation spec

## Troubleshooting

- If the plan feels generic, check whether the hook and payoff help this audience make a specific decision. Find the missing supported detail or revise the treatment; adding another keyword citation is insufficient.
- If a planned pillar lacks tracking, record the gap and propose relevant tracking within the user's scope; do not silently start collection.
- If production capacity is unknown, create a low/medium/high capacity version rather than one unrealistic plan.

## Verification Checklist

- [ ] Each row has an audience, viewer job, hook/payoff, evidence basis and tracking scope or explicit gap.
- [ ] Each row has a content job and format.
- [ ] Evidence references are included.
- [ ] Cadence, date range, priorities, duplicates and available assets were checked across the revised calendar.
- [ ] Audience/CTA/format changes reached affected hooks, scripts and linked briefs; stale copies are identified.
- [ ] Plan retains the agreed measurement/review point or identifies it as undecided.
