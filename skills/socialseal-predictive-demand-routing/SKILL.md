---
name: socialseal-predictive-demand-routing
description: >-
  Use this skill when sourcing early, forward-looking signals on shifting traveler
  (or category) interest to back campaign resource allocation and fast-track
  activity/tour onboarding. It runs periodic search journeys and Google AI runs,
  tracks rank and surfacing velocity for destination/route/activity keywords over
  time, and produces a routing recommendation with explicit selection-bias caveats.
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
    - socialseal
    - strategy
    - demand-routing
    - early-signals
    - travel
    - resource-allocation
---

# SocialSeal Predictive Demand Routing

## Overview

This skill sources **early market signals on shifting interest** so a team can route campaign budget, creator effort, and activity/tour onboarding toward demand that is rising before it peaks. It does not predict the future with a model. It detects direction of movement in the social-search surface earlier than a single snapshot would, and frames that as a routing hypothesis to act on and measure.

"Predictive" here means **leading indicators, not forecasts**: keywords newly appearing, climbing rank quickly, or newly attracting creator content are early demand signals. Treat them as direction with a confidence label, never as a guarantee. Everything SocialSeal sees is a biased sample (only high-ranking videos for tracked queries), so a signal is "interest rising in what surfaces for these queries," not proven total-market demand. See `references/evidence-and-confidence.md`.

## When to Use

- Spotting destinations/routes/activities where traveler interest is rising early.
- Backing campaign resource allocation (budget, creators, content) with movement evidence.
- Fast-tracking activity/tour onboarding when a destination shows an early surge.
- Setting up a repeatable cadence of signal refreshes for a market.

Pair with `socialseal-bilingual-demand-monitoring` to catch signals in either language, `socialseal-tracking-group-design` to operationalize new keywords, and `socialseal-opportunity-analysis` to turn a routed destination into content jobs.

## Inputs

Required:
- workspace id (or a configured default)
- the market (region) and language(s) in scope
- the candidate destinations/routes/activities (as topics or seed keywords)
- existing tracking group ids covering the space, if any

Good to have:
- a prior-period export or earlier journey/AI run for velocity comparison
- platform priority
- a decision context (what the routing recommendation will drive: budget, creators, onboarding)
- a refresh cadence (e.g. weekly, biweekly)

## Signal Sources (live tools)

Three complementary sources, all invoked through the standard MCP/CLI surface (`references/mcp-and-cli-usage.md`):

1. **Search journeys** expand and score keywords for a subject and return staged keywords with `score`, `stage` (e.g. awareness/consideration), `language`, `englishGloss`, `confidence`, and a `scoresByPlatform.snapshotDate`. Re-running over time turns the score and the surfacing into a velocity signal.

```text
socialseal_call_tool {
  "toolName": "search-journey-run",
  "workspaceId": "<workspace-id>",
  "body": { "subject": "<destination or activity>", "subjectType": "topic", "region": "<region>", "locale": "<locale>", "seedKeywords": ["<seed-1>", "<seed-2>"], "maxKeywords": 40, "executionMode": "async" }
}
```

Heavy journeys can time out synchronously; use `executionMode: "async"` and poll:

```text
socialseal_get_tool_status { "id": "<run-uuid>", "kind": "journey_run" }
```

2. **Google AI search runs** capture how AI answers/citations treat a destination's queries. They return a numeric `runId`.

```text
socialseal_call_tool {
  "toolName": "google-ai-search",
  "workspaceId": "<workspace-id>",
  "body": { "queries": ["<query-1>", "<query-2>"], "countryCode": "<cc>", "searchLanguage": "<lang>" }
}
```

Read status/results by numeric run id with the dedicated read function (the generic status route may 403 for numeric AI runs):

```text
socialseal_call_tool { "toolName": "get-google-ai-search-runs", "workspaceId": "<workspace-id>", "body": { "runId": <run-id> } }
socialseal_call_tool { "toolName": "get-google-ai-search-results", "workspaceId": "<workspace-id>", "body": { "runId": <run-id> } }
```

3. **Tracking exports** give rank and surfacing over time for established keywords. Compare windows to read velocity.

```bash
npx -y @socialseal/cli data export-tracking --group-id <group-id> --time-period 30d --workspace-id <workspace-id> --out ./exports/tracking-30d.csv
npx -y @socialseal/cli data export-search-results --group-ids <group-id> --workspace-id <workspace-id> --out ./exports/ranked.csv --timeout 120000
```

CLI equivalents for the journey and AI runs:

```bash
npx -y @socialseal/cli tools call --function search-journey-run --async --body @journey.json --workspace-id <workspace-id>
npx -y @socialseal/cli tools status <run-uuid> --kind journey_run --workspace-id <workspace-id>
npx -y @socialseal/cli tools call --function google-ai-search --body @ai.json --workspace-id <workspace-id>
npx -y @socialseal/cli tools call --function get-google-ai-search-runs --body '{"runId":<run-id>}' --workspace-id <workspace-id>
```

## Workflow

1. **Frame the decision.** State what the routing output drives (budget split, creator allocation, which tours to onboard first) and the candidate destinations/activities.
2. **Establish a baseline.** Run a journey per candidate and/or export current tracking. Record the journey `score`/`stage` and `snapshotDate`, and the current rank distribution per keyword. This is signal time T0.
3. **Refresh on a cadence.** Re-run the same journeys and exports later (T1, T2). Keep subjects, seeds, region, and platform constant so the comparison is valid.
4. **Compute velocity (leading indicators).** For each destination/activity:
   - **new-keyword velocity**: keywords newly scored/surfacing since the last run.
   - **rank velocity**: keywords climbing toward top ranks across windows.
   - **creator-entry velocity**: new creators producing content for the queries (cross-check with `socialseal-creator-discovery`).
   - **journey score/stage shift**: rising scores or movement toward earlier funnel stages.
   - **AI-surface shift**: changes in Google AI citations/answers for the queries.
   Always anchor each to its capture/snapshot dates.
5. **Rank destinations by signal strength.** Combine the velocities into a directional ranking. Require corroboration: a signal backed by two sources (e.g. rank velocity + creator entry) is stronger than one source alone.
6. **Produce the routing recommendation.** For each top destination/activity: the signal, the evidence (queries, ranks, dates, AI/creator corroboration), the recommended resource action, and an explicit confidence label and selection-bias caveat.
7. **Set the measurement checkpoint.** Define what to re-measure next cycle to confirm the bet, and route operational follow-through (new keywords to track, onboarding to start) to the relevant skills.

## Output

A demand-routing readout:

- a ranked list of destinations/routes/activities by early-signal strength
- per item: the leading indicator(s), evidence (`"keyword" [market, platform]`, ranks, snapshot/capture dates, AI or creator corroboration), and the recommended resource action (budget / creators / onboarding)
- a confidence label per recommendation (measured movement vs indicative pattern) and the selection-bias scope
- a refresh cadence and the next-cycle measurement checkpoint
- explicit do-not-route items: candidates with weak or single-source signal

## Do / Don't

Do:
- treat signals as leading indicators and direction, framed as bets to measure
- hold subjects/seeds/region/platform constant across refreshes so velocity is real
- anchor every signal to its snapshot/capture dates
- require corroboration across sources before a high-confidence route
- state the selection-bias scope on every demand claim

Don't:
- call any signal a forecast or a guarantee of future demand
- infer total-market or whole-platform demand from surfaced/tracked queries
- compare runs whose subject, seeds, region, or platform changed without flagging it directional
- route significant budget on a single-source, single-window signal
- make platform-age claims when `published_at` is blank (see `references/socialseal-data-contract.md`)

## Troubleshooting

- Synchronous `search-journey-run` returns 504: re-run with `executionMode: "async"` and poll `journey_run`.
- Numeric Google AI run status 403 via the generic status route: read with `get-google-ai-search-runs` / `get-google-ai-search-results` by `runId` instead.
- Google AI run stays queued: poll `get-google-ai-search-runs` until `succeeded`/`partial`/`failed` before reading results.
- No prior run to compare: this cycle is the baseline; state that velocity needs at least one more refresh and avoid movement claims.
- Signals disagree across sources: report the disagreement; do not force a single ranking, lower confidence instead.

## Verification Checklist

- [ ] The decision the routing drives is stated.
- [ ] At least two snapshots (or a clear baseline-only caveat) anchor every velocity claim.
- [ ] Subjects/seeds/region/platform were held constant across refreshes.
- [ ] Each recommendation carries evidence, capture dates, a confidence label, and the selection-bias scope.
- [ ] Signals are framed as bets to measure, with a next-cycle checkpoint.
- [ ] Weak/single-source candidates are explicitly marked do-not-route.
