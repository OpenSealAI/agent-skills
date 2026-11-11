---
name: socialseal-growth-audit
description: >-
  Use this skill when a founder, growth lead or operator asks for a growth strategy
  audit, has just connected SocialSeal and wants to know where to grow next, or needs
  audience niches, jobs, worries, demand size, content gaps and the brand's edge
  mapped for a start-up's markets. Research the brand first, run the audit with
  SocialSeal tools, save the audience map to the workspace, and propose a Brand
  Strategy for the user to confirm. Do not use it for a single keyword check, a
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

The growth audit is the first piece of work after connecting SocialSeal. It answers one question for a start-up: **where is the audience we can win, and what can we say to them that nobody else is saying?**

It ends with three things saved in the workspace, so the next session starts from them:

1. An **audience map**: niches, the demand behind each, the jobs and worries people bring, who answers them today, the gaps in those answers, and the brand's edge for each gap.
2. A **Brand Strategy** the user has confirmed and published.
3. A **baseline**: the searches that matter, tracked weekly, so change can be measured.

Then hand over to `socialseal-growth-planning`.

Read `references/evidence-and-confidence.md` before making claims from the data, and `references/mcp-and-cli-usage.md` for access, schemas and polling.

## When to use

- A new workspace, or one with no published Brand Strategy, where the user wants direction.
- Growth has stalled, a new market or segment is on the table, or the team is choosing where to put its effort.
- The user asks what their audience searches for, worries about or wants, across one or more markets.

For a single keyword check, a supplied video, a named creator or a read of existing tracking, use the direct tools.

## 1. Read what is already saved

1. `socialseal_get_current_workspace` for the workspace, credits and what is set up. With several workspaces, confirm which one by name.
2. `socialseal_get_brand_strategy`. `state=missing` or `state=no_brand` is normal here.
3. `socialseal_get_core_workspace_notes`. If a note with key `growth/audience-map` exists, compare its scope and growth objective with what the user is asking for. If they match, the audit has been started: read it, say what is done, and continue from the first unfinished step. If the user asks about a new market, segment or objective, run the audit for that scope and add it to the same map. If the core notes don't show it, look it up by key with `socialseal_search_workspace_notes` before starting afresh.

Pinned notes that contradict a published Strategy, or that a newer note replaces, mislead every later session. List them in the diagnostic and propose updating or unpinning each.

## 2. Research the brand yourself

Do the desk research before asking the user anything. Sources, in order of weight:

1. What the user has said or shared in this conversation.
2. What the workspace already holds: notes, the existing Strategy, earlier research.
3. Public sources: the brand's website, pricing and product pages, help centre, announcements and social accounts.

Public pages often lag behind the business. Where they disagree with the user or the workspace, keep the more recent source and list the difference in the diagnostic for the user to settle.

From these, draft a **diagnostic**:

- **What they sell and how they earn:** products, prices, the customer, what a good lead or sale looks like.
- **Markets and languages:** where they operate and sell today, in the order the evidence suggests.
- **Competitors:** three to five, with why each is one.
- **Own accounts:** each social account found, by platform, with who it seems to speak to.
- **The brand's edge:** stated USPs, a distinct point of view, and any data, access or experience only they have.
- **Who the content should not attract:** a proposal, with the reasoning. For example people the product cannot serve, a price band it does not cover, or a market it does not ship to.

Mark each line as found (with its source) or inferred.

## 3. Confirm with the user

Show the diagnostic and ask the user to correct it. Then ask only what research cannot answer:

- **Their north star metric or growth objectives:** what they are trying to move, by how much, and by when. Ask for a number; a target without one can't be judged later.
- **What they can produce:** how many videos a week, and who posts them.
- **Where their accounts post from:** the handle or URL of each own account, and the country the TikTok account and the person posting are in. TikTok shows posts to people near where they are posted from.
- **Anything the diagnostic got wrong or missed,** especially the edge and the excluded audiences.
- **What they have already tried** on social, and what they concluded.

Do not ask for personas, pillars or keywords. Finding those is the audit.

**End your turn here and wait for the user's reply.** The audience and the objective decide what the audit researches, so the research in step 4 starts once they have answered.

## Credits

Some of the tools require credits. Check the available credits before starting, and scope your audit research appropriately. If available credits are insufficient for a quality audit, inform the user about the upgrade or overage options. Do not silently degrade the quality or fall back to assumptions.

## 4. The audit

Each step names what to save, so a stopped audit can resume. Every step below is part of the audit: run all of them for the chosen niches. If the work has to pause, save the map with its progress and tell the user which steps are left.

### When the brand sells to businesses

Buyers who are marketers, founders or operators research differently from consumers, so adjust the audit:

- **Anchor on the buyer's problem** and on the category and comparison searches they make when choosing a tool or a supplier.
- **Expect small, specific demand.** Rank niches by intent and fit with the growth objective, ahead of volume. A thin demand map points to a small, specific audience; use keyword demand checks, video searches and AI answers to fill in the picture.
- **Weight AI answers and YouTube heavily.** Professional buyers ask AI assistants and watch longer explainers. Which brands and sources each engine names is central evidence here.
- **Look for gaps in proof:** comparisons nobody has run, how-to content with real numbers, and data only this brand holds.
- **Keep the baseline tight:** a handful of high-intent searches, plus the buyer questions asked of the AI engines.

### Set up the brand and competitors

Create the primary Brand and the confirmed competitors (`socialseal_create_brand`, `socialseal_create_brand_group`, `socialseal_add_brand_group_member`), and register owned handles as aliases. Skip what already exists.

### Size demand

For two or three anchors per market and language (the category, the problem, a competitor):

- Check candidate wordings with `socialseal_check_keyword_demand`.
- Preview a demand map with `socialseal_explore_preview_start`, run it with `socialseal_explore_start` and read it with `socialseal_explore_get`.

Rank wordings as Strong, Indicative or Untested. Missing search volume is not missing demand.

### Find niches

Group the demand into candidate niches: a segment with its own searches. For the most promising, use `socialseal_search_videos` to see who ranks today: brands, creators or nobody in particular.

Propose three to five niches that fit the growth objective, and say why each.

### Jobs and worries

For each chosen niche:

- `socialseal_start_search_journey` for the stages people search through on the way to a decision.
- AI answers across **Google AI, ChatGPT, Gemini and Claude** with `socialseal_start_google_ai_search`, one call per engine through its `engine` argument (`google_ai`, `chatgpt`, `gemini`, `claude`). Ask three to five buyer questions per niche, worded as the buyer would ask them. Read what each engine answers and which sources it cites. Read the results with `socialseal_get_google_ai_search_results`, filtered by `engine`.
- `socialseal_start_study` on the top videos for the niche's searches, to see what the winning content answers and how. A Study needs at least 6 videos; choose videos that match the niche, and drop off-topic ones before starting.

Searches show what people ask. The answers they currently get, in the videos that rank and in AI answers, give strong clues to why they ask and what would reassure them. Read both sides. Customer conversations the user has had can confirm the picture.

### Find the gaps and the brand's edge

This step turns research into strategy. For each niche, compare what people ask with what they are told today:

- **Answer gaps:** questions the ranking videos and AI answers leave unanswered, answer vaguely, answer for another market or language, answer with out-of-date facts, or get wrong.
- **Content gaps:** searches where results are thin, off-topic, held by one creator, or missing a format the audience uses elsewhere.
- **Presence gaps:** searches where competitors appear and the brand does not, and the reverse.

Then match each gap to the brand's edge from the diagnostic:

- a **USP** that answers the worry directly,
- a **point of view** that disagrees usefully with the common answer,
- **data, access or experience** nobody else can show.

A gap the brand can answer better than anyone is an opportunity. A gap with no edge behind it is a note for later, and a strong edge with no gap needs a different niche. Rank the opportunities by demand, how weak the current answers are, and how strong the edge is.

Where the edge is thin, say so and propose what would build it: data the brand could publish, a comparison it could run, a stance it could take.

### Competitors

Track competitor accounts where ongoing comparison is useful (`socialseal_track_account`), or collect once (`socialseal_collect_account`). Note what they post, which of their videos rank for the niches, and which gaps they leave open.

### Set the baseline

Track the searches that define each chosen niche, weekly, on the platforms that matter: select them in Explore and use `socialseal_explore_preview_activation` then `socialseal_explore_activate_searches`, or `socialseal_track_search_or_hashtag` for searches found outside Explore.

The first refresh of these searches is the "before" picture. Tracking a search schedules it; to take the first capture now, refresh each new search once with `socialseal_refresh_tracking_item` (quote first). Record the date, and the next refresh date each search reports.

## 5. Write it down

### The audience map

Save one note with `socialseal_create_workspace_note`: `type: "fact"`, `key: "growth/audience-map"`, `pinnedToCore: true`. Update the same note as the audit progresses.

Keep the map under about 6,000 characters, so it fits in the core notes every session reads first. Put long evidence (video lists, AI answer excerpts, full demand tables) in a second, unpinned note with key `growth/audience-map-evidence`, and link to it from the map.

```markdown
# Audience map · <brand> · <date>

Growth objective: <north star metric or objectives, and by when>
Scope: <markets, languages, platforms, window>
Progress: <steps done / steps left>

## The brand
- Sells: <offer, customer, what a good lead is>
- Edge: <USPs, point of view, unique data or access>
- Not for: <excluded audiences, confirmed by the user>
- Accounts: <platform, handle, posting location, who it speaks to>
- Production: <videos a week, who posts>

## <Market · language>

### Niche: <name>
- Demand: <wordings, level (Strong / Indicative / Untested), source and window>
- Trend: <direction and evidence, or "one capture: baseline">
- Jobs: <what people are trying to get done>
- Worries: <hesitations and questions, with where each was seen>
- Answered today by: <who ranks; what AI answers say and cite>
- Gaps: <answer, content and presence gaps>
- Our edge here: <the USP, point of view or data that gives a better answer>
- Evidence: <Explore run, journey, AI search, Study ref, tracked group>

## Opportunities, ranked
1. <niche · gap · edge> — why it ranks here, and what would prove it wrong

## Open questions
- <what to confirm with customers or with the user's own account data>
```

### The Brand Strategy

The Strategy rests on observed gaps. Draft it once each chosen niche has its AI answers read across the four engines and at least one Study, and the gaps-and-edge step is written from that evidence. Until then, keep building the map.

Draft the Strategy from the confirmed diagnostic and the map, then save it with `socialseal_propose_brand_strategy` (`expectedBaseRevisionId: null` when none exists).

| Strategy field | Fill it from |
|---|---|
| `summary` | One positioning paragraph: who it is for, the problem, why this brand |
| `offer` | What they sell, how they earn, what a good lead is |
| `targetAudiences` | The chosen niches, one line each |
| `excludedAudiences` | The confirmed "not for" list |
| `frictions` | The worries the brand removes, each with its `source` and `confidence` |
| `messaging` | The edge as rules (the claims, the point of view, the data to cite), wordings the audience uses, wordings to avoid |
| `production` | Real limits: people, time, footage |
| `angles` | Each ranked opportunity as a `live` angle; ideas the user turned down as `rejected` with the reason |
| `decisionTests` | Three to six yes/no tests every idea must pass, derived from the growth objective, the edge and the exclusions |

Show the draft in plain language. Publish with `socialseal_publish_brand_strategy` once the user confirms it.

## Finish

Report in this order: the growth objective; the three to five opportunities, ranked, each as niche, gap and edge with its evidence level; what was saved (the map note, the Strategy, the tracked searches and when the first refresh lands); and the open questions.

Then offer `socialseal-growth-planning` to turn the opportunities into experiments.

## Do / Don't

Do:
- research first; ask the user to confirm and to fill what research cannot reach
- resume from saved state and update the one audience-map note
- give every number its source, scope and window, and label findings Strong, Indicative or Untested
- tie every opportunity to both a gap and an edge
- keep the confirmed exclusions above demand: a large audience the brand cannot serve is not an opportunity

Don't:
- ask the user for facts a website, a document or a tool can supply
- invent audiences, worries, gaps or an edge that no source showed
- present a trend from one capture, or a cause from a correlation
- track every wording found; track what the chosen niches need

## Verification checklist

- [ ] The workspace, existing Strategy and core notes were read first.
- [ ] A researched diagnostic was shown, and the user confirmed or corrected it before the audit research began.
- [ ] Differences between public pages and what the user or workspace says were listed and settled.
- [ ] Each chosen niche has a Study, and its gaps come from evidence.
- [ ] The user's north star metric or growth objectives are recorded, with a number and a date.
- [ ] Own accounts, their posting location and weekly production capacity are recorded.
- [ ] AI answers were read across Google AI, ChatGPT, Gemini and Claude for the chosen niches.
- [ ] Each chosen niche has its gaps and the brand's edge written down.
- [ ] One pinned note with key `growth/audience-map` holds the map.
- [ ] A Brand Strategy was proposed, confirmed by the user, then published.
- [ ] Baseline searches are tracked, each has a first capture, and the date is recorded.
