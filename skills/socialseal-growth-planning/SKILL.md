---
name: socialseal-growth-planning
description: >-
  Use this skill when the user wants a growth plan after a growth audit: turning a
  saved audience map and published Brand Strategy into cheap organic experiments
  (exploration) and then scaling what works through more accounts, creators and
  paid boosting (exploitation), with a weekly routine to run it. Also use it when a
  returning user asks what to do next, what is working, or how to split effort
  between testing and scaling. If no audience map or Strategy exists yet, run
  socialseal-growth-audit first.
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
    - socialseal
    - growth
    - planning
    - experiments
    - content-plan
    - routine
---

# SocialSeal Growth Planning

## The approach

Organic social is the cheapest place to experiment. A post costs little to make, reaches a real audience within days, and the results are measurable. So the plan has two modes, run side by side:

- **Exploration:** use organic posts to test, cheaply, which audience, account, message and format work.
- **Exploitation:** repeat what works and scale it with more accounts, creators and partnerships, and paid boosting.

The split between the two changes with the stage. A brand with nothing proven is almost all exploration. A brand with proven winners moves most of its effort to exploitation. **Always keep at least 10% in exploration**, so the next winner is being found while the current ones are scaled.

Planning ends with two notes saved in the workspace: the **plan** (experiments, winners, the split) and a **weekly routine** the user's agent can run.

Read `references/evidence-and-confidence.md` before interpreting results, `references/mcp-and-cli-usage.md` for schemas and polling, and use `templates/social-plan-template.md` for a posting calendar's layout.

## Start: read saved state

1. `socialseal_get_current_workspace`, then `socialseal_get_brand_strategy`.
2. `socialseal_get_core_workspace_notes`, looking for the notes with keys `growth/audience-map`, `growth/plan` and `growth/routine`. If one is missing from the core notes, look it up by key with `socialseal_search_workspace_notes` before concluding it doesn't exist.

The plan needs three facts from the audit: the growth objective as a number and a date, how many videos a week the team can make, and where each own account posts from. If the audience map doesn't hold them, ask the user for them before designing experiments.

Then:

- **No published Strategy or no audience map:** offer `socialseal-growth-audit`.
- **A plan already exists:** this is a return visit. Go to "Each week".
- **Map and Strategy, no plan:** continue below.

## Credits

Some of the tools require credits. Check the available credits before starting, and scope the plan's research and tracking appropriately. If available credits are insufficient for a quality plan, inform the user about the upgrade or overage options. Do not silently degrade the quality or fall back to assumptions.

## Exploration

Each experiment is a small bet: one audience, one account, one message, one format, a handful of posts. Design the first set from the audit's ranked opportunities.

### Decide platforms and accounts

- **Platform:** go where the niche's searches and winning videos are. The audience map shows this per niche.
- **One account, one audience.** Each account should serve a specific audience, in its language, on its topics. An account that speaks to everyone is recommended to no one. Where the opportunities point to different audiences or markets, plan separate accounts.
- **TikTok accounts should sit where the audience is.** A TikTok account is ideally located in the same market as the audience it targets.
- Start with the fewest accounts that cover the top opportunities. More come in exploitation.

Check existing accounts against this. Recommend keeping, refocusing or splitting each, and say why.

### Decide content

Two inputs, kept separate:

- **Message: what to say.** From the audit: the gap in today's answers, and the brand's edge that fills it (a USP, a point of view, data or access only they have). Each experiment should give a better answer than the audience gets now.
- **Format and mechanism: how to say it.** From a Study of what already wins the target search: hooks, opening move, duration, structure, on-screen text, call to action. Start one with `socialseal_start_study`, or reuse a Study from the audit.

Vary one thing at a time where possible, so a result can be read: the same message in two formats, or two messages in the same format.

### Brief the experiments

Generate briefs from the Study with `socialseal_generate_brief` (or `socialseal_start_brief_run`), read them with `socialseal_get_brief`, share them with `socialseal_export_brief`. On `study_needed`, offer the Study or subjects it returns. A brief follows one worked example from the Study; tell the user which video.

Generate the first brief, read it with the user, and adjust before generating the rest, so one correction doesn't have to be made in every brief. Brief two weeks ahead. Results should shape what comes after.

### Make each experiment measurable

Every experiment targets searches that are tracked (`socialseal_track_search_or_hashtag`, `socialseal_add_tracking_group_items`), and names what "worked" would look like before it runs.

## Exploitation

### What "works" means

Judge each experiment on three sources together:

1. **Search and tracking data in SocialSeal:** does the post, or the account, appear for the target searches; did discoverability and Share of Voice on those searches move. Attach published posts to their briefs with `socialseal_attach_brief_publication` and read `socialseal_get_brief_outcomes`; read the tracked groups for the wider picture.
2. **Engagement:** views, saves, shares, comments, and what the comments say.
3. **The account's own metrics and insights:** follower growth, audience location and demographics, retention, profile visits, link clicks, and the sign-ups, leads or sales behind them. SocialSeal does not see these. The user does: read them through whatever access the user's agent has, or ask the user for them.

Tie the judgement to the growth objective in the audience map. A post that ranks but brings the wrong audience has not worked.

### Repeat

Make more of what worked: the same message and mechanism on new searches in the niche, as a series, and adapted to the next platform. Record the winning combination in the Strategy's angle ledger (`socialseal_propose_brand_strategy`, then publish once the user confirms), and mark what failed as `rejected` with the reason, so it is not retried by accident.

### Scale

- **More accounts:** a new account per additional audience or market that the winners justify, following the one-account-one-audience rule.
- **Creators and partnerships:** find creators who already rank for the niche's searches, nano included (`socialseal_search_videos`, `socialseal_get_creator_profile`, `socialseal_get_creator_recent_posts`, `socialseal_collect_account`). Brief them with the winning message and mechanism. See `socialseal-creator-discovery`, `socialseal-creator-evaluation` and `socialseal-creator-briefing`.
- **Ads and boosting:** put paid budget behind posts that have already won organically. Organic results choose the creative; paid extends its reach.

## Set the split

Recommend a split of effort between exploration and exploitation for the next six weeks, from where the brand is:

| Stage | Signs | Exploration | Exploitation |
|---|---|---|---|
| Nothing proven | New accounts, or no post has moved the objective | Most of the effort | Little or none |
| First winners | One or two combinations work repeatably | About half | About half |
| Proven engine | Several winners, a steady cadence, results tied to the objective | At least 10% | The rest |

State the reasoning, and what would move the brand to the next stage.

## Write it down

Save the plan as one note: `type: "workflow"`, `key: "growth/plan"`, `pinnedToCore: true`. Update it in place. Keep it under about 6,000 characters so it fits in the core notes; move finished experiments to "Stopped, and why" in one line each.

```markdown
# Growth plan · <brand> · <start date> to <end date>

Growth objective: <from the audience map>
Stage and split: <stage> — <x>% exploration, <y>% exploitation. Next stage when: <condition>

## Accounts
| Platform | Account | Audience it serves | Market / location | Status |
|---|---|---|---|---|

## Exploration: experiments
| # | Audience / niche | Account | Message (gap + edge) | Format / mechanism (Study ref) | Target searches | "Worked" means | Posts | Result |
|---|---|---|---|---|---|---|---|---|

## Exploitation: what works
| Winner (message + mechanism) | Evidence (search, engagement, account insights) | Repeating as | Scaling through (accounts / creators / paid) |
|---|---|---|---|

## Stopped, and why
- <experiments that failed or were cut>

## Review dates
- <weekly check day>; <six-week review date>
```

Save the routine as a second note: `type: "workflow"`, `key: "growth/routine"`, `pinnedToCore: true`.

```markdown
# Weekly routine · <brand>

Every <day>, about 30 minutes. Ask your agent: "Run my SocialSeal weekly routine."

1. Read the plan, the audience map and the Brand Strategy.
2. Link posts published this week to their briefs; read their outcomes.
3. Read what moved on the tracked searches and competitors.
4. Bring in the accounts' own insights for the week.
5. Judge each running experiment: worked, did not, or too early.
6. Update the plan: results, new winners, what stops, next week's posts.
7. Brief next week's posts.

Every six weeks: review the stage and the split.
When the objective changes or a new market opens: run the growth audit for it.
```

## Each week

When the user returns, run the routine:

1. Read `growth/plan`, `growth/audience-map` and the Strategy.
2. Attach new posts to their briefs and read `socialseal_get_brief_outcomes`.
3. Read the tracked groups for what moved, using the tracking reads and exports in the live catalogue; prefer a Monitor report read where one is offered.
4. Get the accounts' own insights, through the agent's access or from the user.
5. Say what worked, what did not and what is too early to call. Outcomes are observations; a before-and-after alone does not show cause.
6. Move winners to exploitation, stop what failed, propose the next experiments, and update the plan note with `socialseal_update_workspace_note`.

## Finish

Report: the stage and the recommended split; the accounts and who each serves; the first experiments and what would count as working; the briefs ready; what is tracked; the routine and the next review date.

## Do / Don't

Do:
- keep one plan note and update it; a returning agent reads it first
- tie every experiment to an audience, an account, tracked searches and a stated test of "worked"
- keep the message (gap and edge) separate from the format (Study)
- judge on search data, engagement and the account's own insights together
- keep at least 10% of effort in exploration at every stage

Don't:
- plan without a published Strategy and a saved audience map
- run one account for several audiences
- scale a post with paid budget before it has worked organically
- call a result from a single post, or read a cause into a before-and-after
- brief more than two weeks ahead

## Verification checklist

- [ ] The Strategy and core notes were read first; a missing map or Strategy was routed to the audit.
- [ ] Platforms and accounts are decided, each account serving one named audience.
- [ ] Each experiment names its message (gap and edge), its format (Study), its target searches and what "worked" means.
- [ ] The stage and the exploration and exploitation split are stated, with at least 10% exploration.
- [ ] One pinned note with key `growth/plan` and one with key `growth/routine` are saved.
- [ ] Return visits judge results on search data, engagement and the accounts' own insights.
