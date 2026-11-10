---
name: socialseal-growth-audit
description: >-
  Use this skill when a founder, growth lead or operator asks for a growth strategy
  audit, has just connected SocialSeal and wants to know where to grow next, or needs
  audience niches, jobs, worries, demand size and trends mapped for a start-up's
  markets before deciding on product, partnerships or marketing. Run the audit with
  SocialSeal tools, save the audience map to the workspace, and propose a Brand
  Strategy for the user to approve. Do not use it for a single keyword check, a
  one-off video analysis, or reading existing tracking groups.
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
    - socialseal
    - growth
    - audit
    - audience
    - strategy
    - onboarding
---

# SocialSeal Growth Audit

## Overview

The growth audit is the first piece of work after connecting SocialSeal. It answers one question for a start-up: **where should we grow next, and what is the evidence?**

It ends with three things saved in the workspace, so the next session starts from them and not from a blank page:

1. An **audience map**: niches, the demand behind each, the jobs and worries people bring, and who wins those searches today.
2. A **Brand Strategy** the user has approved and published.
3. A **baseline**: the searches that matter, tracked weekly, so change can be measured later.

Then hand over to `socialseal-growth-planning`.

Read `references/evidence-and-confidence.md` before making claims from the data, and `references/mcp-and-cli-usage.md` for access, schemas, quotes and polling.

## When to use

- A new workspace, or one with no published Brand Strategy, where the user wants direction and not one answer.
- A decision is coming: a market or segment to enter, growth that has stalled, organic against paid, a creator programme, agency against in-house.
- The user asks what their audience searches for, worries about or wants, across one or more markets.

Use the direct tools instead, without this skill, for a single keyword check, a supplied video, a named creator or a read of existing tracking.

## Start: read before you ask

1. `socialseal_get_current_workspace` for the workspace, credits and what is already set up. With several workspaces, confirm which one by name before any paid or saved work.
2. `socialseal_get_brand_strategy`. `state=missing` or `state=no_brand` is normal here.
3. `socialseal_get_core_workspace_notes`. If a note with key `growth/audience-map` exists, the audit has been started: read it, say what is done, and continue from the first unfinished step. Do not start again.

Then ask the user only for what the tools cannot know. Five things, in one message:

- **The decision** they face in the next 90 days.
- **What they sell**, how they earn, and what a good lead or sale looks like.
- **Markets and languages**, in priority order.
- **Three to five competitors**, and their own social accounts.
- **Who must not be attracted**, even if they search a lot.

Do not ask for personas, pillars or keywords. Finding those is the audit.

## Budget and approval

- State the plan and its estimated credits before the first paid step, and get one go-ahead for that scope. Read each tool's returned price; do not quote prices from memory.
- Free first: `socialseal_check_keyword_demand` and `socialseal_explore_preview_start` cost nothing and narrow what is worth paying for.
- Approve a returned price with the field that tool names, and send one `idempotencyKey` per intended request. Reuse the key on a retry; a new key starts new billable work.
- If a tool refuses a cost cap or quote, relay its exact reason and next step. Do not retry with invented parameters.
- Instagram collection costs several times more than TikTok or YouTube. Say so when the user's buyers are on Instagram, and track a tighter set there.

## The audit

Work through the steps in order. Each step names what to save, so a stopped audit can resume.

### 1. Set up the brand and competitors

Create the primary Brand and the competitors (`socialseal_create_brand`, `socialseal_create_brand_group`, `socialseal_add_brand_group_member`), and register owned handles as aliases. Skip what `socialseal_get_current_workspace` shows already exists.

### 2. Size demand

For two or three anchors per market and language (the category, the problem, a competitor):

- Check candidate wordings with `socialseal_check_keyword_demand`.
- Preview a demand map with `socialseal_explore_preview_start`, then run it with `socialseal_explore_start` and read it with `socialseal_explore_get`.

Rank wordings as Strong, Indicative or Untested. Missing search volume is not missing demand.

### 3. Find niches

Group the demand into candidate niches: a segment with its own searches. For the most promising, use `socialseal_search_videos` to see who ranks today: brands, creators or nobody in particular. Flag niches where results are thin or off-topic.

Agree three to five niches with the user before going deeper.

### 4. Jobs and worries

For each chosen niche:

- `socialseal_start_search_journey` for the stages people search through on the way to a decision.
- `socialseal_start_google_ai_search` for the questions AI answers get asked and which sources they cite.
- `socialseal_start_study` on the top videos, to see what the winning content answers. Creative analysis is priced per new video: show the price and run it only on approval.

Search data shows what people ask, not why. Say this, and recommend the user holds three to five short customer calls to test the worries. There is no comment-mining tool; do not imply one.

### 5. Competitors

Track competitor accounts where the user wants ongoing comparison (`socialseal_track_account`), or collect once (`socialseal_collect_account`, quote first). Note what they post and which of their videos rank for the niches.

### 6. Set the baseline

Track the searches that define each chosen niche, weekly, on the platforms that matter: select them in Explore and use `socialseal_explore_preview_activation` then `socialseal_explore_activate_searches`, or `socialseal_track_search_or_hashtag` for searches found outside Explore. Keep the set big enough to see change and small enough to afford.

The first refresh of these searches is the "before" picture. Record the date.

## Write it down

### The audience map

Save one note with `socialseal_create_workspace_note`: `type: "fact"`, `key: "growth/audience-map"`, `pinnedToCore: true`. Update the same note as the audit progresses; do not create a second one.

```markdown
# Audience map · <brand> · <date>

Decision this audit serves: <the user's decision>
Scope: <markets, languages, platforms, window>
Progress: <steps done / steps left>

## <Market · language>

### Niche: <name>
- Demand: <wordings, level (Strong / Indicative / Untested), source and window>
- Trend: <direction and evidence, or "one capture only: baseline">
- Jobs: <what people are trying to get done>
- Worries: <hesitations and questions, with where each was seen>
- Who wins today: <brands, creators, competitors; or "nobody in particular">
- Evidence: <Explore run, journey, Study ref, tracked group>

## Opportunities, ranked
1. <niche or angle> — why, and what would prove it wrong

## What this audit could not tell
- <limits: platforms not covered, thin samples, things only customer calls can answer>
```

### The Brand Strategy

Draft the Strategy from the map and the user's five answers, then save it with `socialseal_propose_brand_strategy` (`expectedBaseRevisionId: null` when none exists).

| Strategy field | Fill it from |
|---|---|
| `summary` | One positioning paragraph: who it is for, the problem, why this brand |
| `offer` | What they sell, how they earn, what a good lead is (the user's words) |
| `targetAudiences` | The chosen niches, one line each |
| `excludedAudiences` | Who must not be attracted, even where demand is large |
| `frictions` | The worries the brand removes, each with its `source` and `confidence` |
| `messaging` | Wordings people use (`use`), wordings to avoid, and hard rules |
| `production` | Real limits: people, time, footage |
| `angles` | Each ranked opportunity as a `live` angle; ideas the user turned down as `rejected` with the reason |
| `decisionTests` | Three to six yes/no tests every idea must pass, derived from the decision and the exclusions |

Show the draft in plain language and ask the user to approve or change it. Publish with `socialseal_publish_brand_strategy` only after they approve that exact draft in the conversation.

## Finish

Report in this order: the decision the audit served; the three to five opportunities, ranked, each with its evidence level; what was saved (the map note, the Strategy revision, the tracked searches and when the first refresh lands); credits used; and what the audit could not tell.

Then offer `socialseal-growth-planning` to turn the map into decisions, a content plan and briefs.

## Do / Don't

Do:
- resume from saved state; update the one audience-map note
- give every number its source, scope and window
- label findings Strong, Indicative or Untested, and say when a sample is small
- keep the user's exclusions above demand: a large audience they cannot serve is not an opportunity
- stop and report at any step the user wants; the map is useful half-finished

Don't:
- open with a Visibility Check or any report the user did not ask for; this audit's baseline is the tracked searches
- invent audiences, worries or demand that no search, journey, answer or video showed
- publish a Strategy the user has not approved, or start paid collection outside the agreed scope
- claim a trend from one capture, or a cause from a correlation
- create tracking for every wording found; track what the chosen niches need

## Verification checklist

- [ ] The workspace, existing Strategy and core notes were read before anything was asked or created.
- [ ] The five inputs came from the user; nothing else was demanded up front.
- [ ] Paid steps ran inside a scope and price the user approved.
- [ ] One pinned note with key `growth/audience-map` holds the map, with scope, evidence levels and limits.
- [ ] A Brand Strategy was proposed, approved by the user in the conversation, then published.
- [ ] Baseline searches are tracked and the date of the first refresh is recorded.
- [ ] The final report names what the audit could not tell.
