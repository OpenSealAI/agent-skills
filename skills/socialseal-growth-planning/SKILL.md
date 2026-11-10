---
name: socialseal-growth-planning
description: >-
  Use this skill when the user wants a growth plan after a growth audit: turning a
  saved audience map and published Brand Strategy into recorded decisions, a
  six-week content plan, a tracked set of searches, first briefs, and a weekly
  routine they can run with their agent. Also use it when a returning user asks
  what to do next or what changed since the plan was made. If no audience map or
  Strategy exists yet, run socialseal-growth-audit first.
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
    - socialseal
    - growth
    - planning
    - decisions
    - content-plan
    - routine
---

# SocialSeal Growth Planning

## Overview

Planning turns the audit into action the user can keep running: **decide, plan, brief, then measure every week.**

It ends with four things saved in the workspace:

1. The **decisions**, each as its own note, and reflected in the Brand Strategy's angle ledger.
2. A **plan**: six weeks of content against the chosen niches.
3. The **first briefs**, each generated from a Study.
4. A **weekly routine** the user's agent can run without help.

Read `references/evidence-and-confidence.md` before interpreting results, `references/mcp-and-cli-usage.md` for schemas, quotes and polling, and use `templates/social-plan-template.md` for the plan's layout.

## Start: read saved state

1. `socialseal_get_current_workspace`, then `socialseal_get_brand_strategy`.
2. `socialseal_get_core_workspace_notes`, looking for the notes with keys `growth/audience-map`, `growth/plan` and `growth/routine`.

Then:

- **No published Strategy or no audience map:** say so and offer `socialseal-growth-audit`. Do not plan from assumptions.
- **A plan already exists:** this is a return visit. Go to "Each week".
- **Map and Strategy, no plan:** continue below.

## 1. Decide

For each decision the audit was meant to serve, prepare one short page: the options, the evidence for each from the audience map, and what we would expect to see if the choice is right.

Typical decisions: which market or segment first; which niche to own; organic against paid; whether to start a creator programme; agency against in-house; a product, pricing or partnership change the worries point to.

The user decides. Then record it:

- One note per decision with `socialseal_create_workspace_note`: `type: "decision"`, `key: "growth/decision/<short-name>"`, stating the choice, the date, the evidence and what would change it.
- Update the Strategy's `angles`: chosen angles `live`, turned-down ones `rejected` with the reason. Save with `socialseal_propose_brand_strategy`, passing the published revision as `expectedBaseRevisionId`, and publish only after the user approves the draft.

Check every recommendation against the Strategy's decision tests. If one fails, say which test and offer a version that passes.

## 2. Check the tracked set

Read what is tracked (`socialseal_list_tracking_groups`, `socialseal_get_tracking_group`). The decisions may have changed what matters:

- Add searches the chosen niches need (`socialseal_track_search_or_hashtag`, `socialseal_add_tracking_group_items`).
- Pause what the decisions dropped, with the user's agreement.
- Tell the user what the set costs to refresh each week, from the tools' own prices.

## 3. Plan six weeks

Draft the plan against the chosen niches: the searches each post targets, the format, who makes it and the cadence. Cut anything the user cannot produce; the Strategy's `production` limits are binding.

Save it as one note: `type: "workflow"`, `key: "growth/plan"`, `pinnedToCore: true`.

```markdown
# Growth plan · <brand> · <start date> to <end date>

Decisions this plan carries out: <links to the decision notes>
Measured by: <tracked groups; Share of Voice and discoverability on those searches>

| Week | Post | Niche | Target search | Format | Maker | Brief | Published link |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | <brief ref or "to do"> | |

## Not doing, and why
- <what was cut>

## Review dates
- <weekly check day>; <six-week review date>
```

## 4. Brief the first two weeks

Briefs come from a Study of what already wins the target search.

- Reuse an existing Study where one covers the niche; otherwise start one with `socialseal_start_study` and run creative analysis only after the user approves its price.
- Generate each brief with `socialseal_generate_brief` (or `socialseal_start_brief_run`), read it with `socialseal_get_brief`, and share it with `socialseal_export_brief`.
- On `study_needed`, offer the returned Study or candidate subjects; do not work around it.
- Put each brief's reference into the plan note.

A brief is one worked example from the Study, not a summary of every video. Tell the user which video it follows.

## 5. Write the weekly routine

Save the routine as a note the user's agent can follow: `type: "workflow"`, `key: "growth/routine"`, `pinnedToCore: true`. Keep it to what they will do:

```markdown
# Weekly routine · <brand>

Every <day>, about 30 minutes. Ask your agent: "Run my SocialSeal weekly routine."

1. Read the plan and decisions (core notes) and the Brand Strategy.
2. What moved on the tracked searches and competitors since last week?
3. Link any post published this week to its brief.
4. Read outcomes for linked posts.
5. Brief next week's posts from the latest Study.
6. Update the plan note: published links, what changed, what is next.

Monthly: a one-page readout for whoever needs it.
Every quarter, or when a new decision comes up: run the growth audit again for that question.
```

## Each week

When the user returns, run the routine:

1. Read `growth/plan`, the decision notes and the Strategy.
2. Read the tracked groups for what moved. Use the tracking reads and exports available in the live catalogue; if a Monitor report read is offered, prefer it.
3. For posts published since last time, attach each to its brief with `socialseal_attach_brief_publication`, then read `socialseal_get_brief_outcomes`.
4. Say what moved, what did not, and what cannot be told yet. Outcomes are observations, not proof that the post caused the change.
5. Recommend the next week's work and update the plan note in place with `socialseal_update_workspace_note`.

The user's own numbers (sign-ups, leads, sales) are theirs to add. Do not claim them.

## Finish

Report: the decisions recorded; the plan's first two weeks; the briefs ready and the video each follows; what is tracked and its weekly cost; the routine and the next review date.

## Do / Don't

Do:
- keep one plan note and update it; a returning agent reads it first
- tie every planned post to a tracked search, so it can be measured
- record what was cut and why
- state weekly tracking cost before adding to the set

Don't:
- plan without a published Strategy and a saved audience map
- record a decision the user has not made
- promise results, or read a cause into a before-and-after
- generate every brief up front; brief two weeks ahead
- add platforms or markets the decisions did not choose

## Verification checklist

- [ ] The Strategy and core notes were read first; a missing map or Strategy was routed to the audit.
- [ ] Each decision is a note with its evidence and date, and the Strategy's angle ledger matches.
- [ ] One pinned note with key `growth/plan` holds the six weeks, each post tied to a tracked search.
- [ ] The first two weeks have briefs generated from a Study, and the plan names them.
- [ ] One pinned note with key `growth/routine` tells the user's agent what to do each week.
- [ ] Tracking cost and the next review date were stated.
