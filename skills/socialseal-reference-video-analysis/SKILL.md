---
name: socialseal-reference-video-analysis
description: >-
  Use this skill when the user asks to find real social examples, benchmark videos,
  successful-looking references, "what good looks like", or Video DNA for a topic,
  brief, or planned video, including a single supplied video. Study exemplars that
  actually surface for tracked searches, approve any paid analysis, and read hooks,
  structure, shots, language, pacing, and production qualities before any brief or
  externally edited rough cut.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - reference-videos
    - video-dna
    - exemplars
    - study
    - editor-handoff
---

# SocialSeal Reference Video Analysis

## Overview

SocialSeal does not start content from a blank prompt. It lifts patterns from real videos that already surface for the brand's tracked searches. This skill is the evidence stage: choose what to study for an opportunity, run a SocialSeal Study, and read its Video DNA so a brief can be generated from it. Understanding one supplied video is a one-video Study.

Do not hand-invent "what good looks like." Study exemplars in SocialSeal and read their actual analysis. See `references/production-pipeline.md` for the full pipeline and `references/mcp-and-cli-usage.md` for the call patterns.

Read `references/creative-production-gates.md` for production-bound work. The
benchmark gate should let the user see representative candidates and choose the
creative direction before expensive analysis or large-scale production.

## When to Use

- Choosing a Study subject for an opportunity: topic, competitor, creator, Monitor finding, saved set, or specific videos.
- Offering the Study subjects a brief tool returned with `study_needed`.
- Getting Video DNA for one or more specific videos or public URLs.
- Comparing reference videos to see repeated mechanisms.

Hand off the Study's `briefContext` to `socialseal-creator-briefing`.

## Inputs

Required:
- workspace id (or a configured default)
- an opportunity definition and its `opportunityKey`
- a Study subject: `topic` (`topicId` or `keywords`), `competitor` (`brandId` or `handle`), `creator` (`handle`), `monitor_finding`, `saved_set` (`videoListId`), or `videos` (`urls` and/or `videoUids`)

Good to have:
- a `question` describing what you want to learn (topic subjects)
- `platformIds`, `regions`, `windowDays`
- the `study_needed` candidates and `reuse` Study from a brief tool

## Workflow

1. **Confirm subject and workspace.** Identify the opportunity and reuse its `opportunityKey`. If a brief tool returned `study_needed`, start from its `reuse` Study and ranked `candidates`.
2. **Start or reuse the Study.** Load `socialseal_start_study` through host tool search and call it with the chosen `subject`, without approval fields. If the named action remains unavailable, report that limitation and preserve completed work. A matching Study is reused for free; `ready` means no new analysis is needed.
3. **Offer analysis depth.** On `approval_required`, nothing has run. Present representative videos, the returned price and how many videos are new versus already analysed, and let the user choose:
   - metadata/existing evidence only (free; weakest visual claims)
   - focused DNA on a narrow subject or roughly 3-5 chosen videos (default for a single deliverable)
   - fuller DNA on a broader subject or roughly 8-12 videos (broader pattern confidence)
   State likely time/credit trade-offs before a paid run. If the user picks a different set than the one priced, build that subject (for example `{ "kind": "videos", "videoUids": [...] }` for the chosen videos, or a narrower topic) and call `socialseal_start_study` with it, without approval fields, to get its price. Seek approval for that price, not the original one.
4. **Approve and run.** After the user approves the price, resend the request that produced it with `maxCostUsd` (wallet workspace) or `approvedCredits` (subscription) set to it and an `idempotencyKey` you keep. After a timeout or uncertain outcome, retry the unchanged request with the same key; it is never charged twice. On `price_changed`, nothing ran: a wallet response carries no price, so request a fresh quote without approval fields, get approval for the returned price and resend with a new `idempotencyKey`; a subscription response carries the new credit price to approve, then follow its `nextStep`. On `funding_required`, share the returned funding link and keep its `operationId`.
5. **Read Video DNA.** Poll `socialseal_get_study` with the `studyRef` while it is `enriching`. Read the findings, coverage and per-video evidence: hooks, CTAs, shots, beats, style and metrics (photo evidence by slide). Use `socialseal_extract_video_assets` only when you need frames or source assets for stored videos.
6. **Group observed mechanisms if needed.** Compare the returned per-video evidence locally and label this as your synthesis, separately from the Study's own findings.
7. **Record evidence.** For every exemplar capture the human-readable citation (video title/URL, `@author_handle`, and the `"keyword" [market, platform]` it surfaced for) plus the analyzed DNA. Keep `video_uid` (and `search_result_id` where it came from a ranked row) and the Study's `studyRef`/revision as an internal traceability note. Separate observed features from `likelyReasonItRanks` and other model hypotheses; do not cite those interpretations as independent corroboration. Remember exemplars are anecdotal creative evidence, not proof a mechanism will perform; see `references/evidence-and-confidence.md`.

## Tool Calls (MCP-first)

Start (or reuse) a topic Study and get its price:

```text
socialseal_start_study {
  "workspaceId": "<workspace-id>",
  "subject": {
    "kind": "topic",
    "topicId": "<topic-id>",
    "question": "first-timer walkthroughs that answer cost and timing"
  },
  "windowDays": 30
}
```

Study one supplied video after the user approves the returned USD price:

```text
socialseal_start_study {
  "workspaceId": "<workspace-id>",
  "subject": { "kind": "videos", "urls": ["<video-url>"] },
  "maxCostUsd": "<approved-usd-price>",
  "idempotencyKey": "<stable-request-key>"
}
```

Read the Study and its per-video evidence:

```text
socialseal_get_study { "workspaceId": "<workspace-id>", "studyRef": "<study-ref>" }
```

## Output

- a list of studied exemplars cited by video title/URL, `@handle`, and the `"keyword" [market, platform]` (with `video_uid`/`search_result_id` kept as a traceability note), plus metrics
- Video DNA per exemplar: hook, first frame, structure, hero/supporting shots, useful details or mood cues, production qualities, caption/CTA style, account type
- format and lens labels (aspirational vs utility/practical) with the evidence behind each
- a note on which exemplars are analyzed vs metadata-only, from the Study's coverage
- approved benchmark direction, analysis-depth choice and price
- the Study's `studyRef`, revision and `briefContext` (or why it has none)

## Do / Don't

Do:
- reuse an existing Study before starting a new one
- get the user's benchmark/analysis-depth choice and price approval before paid DNA work
- inspect actual analysis/frames before claiming a visual or format pattern
- cite exemplars by title/URL and `@handle`; keep `video_uid`/`search_result_id` and the `studyRef` as a traceability note
- separate owned, creator, media, affiliate, and competitor exemplars

Don't:
- hand-pick "good examples" from outside SocialSeal when a Study can cover them
- resend a paid start with a new idempotency key after a timeout
- infer a pattern from a single example, or present an exemplar as proof a hook will work
- make platform-age claims when `published_at` is blank (see `references/socialseal-data-contract.md`)
- copy hooks verbatim; capture the mechanism

## Troubleshooting

- `socialseal_get_study` has no `briefContext`: the revision has no briefable action finding. Study more videos or a broader subject, or change `windowDays`, before briefing.
- Still `enriching`: Video DNA is running; read the Study again later rather than restarting it.
- A video was skipped: keep the returned reason and continue with the rest; it is not studied.
- Too many viral outliers: study a chosen set of representative videos instead.

## Verification Checklist

- [ ] Subject and `opportunityKey` are confirmed and reused.
- [ ] Paid Video DNA ran only after the user approved its price, with a kept idempotency key.
- [ ] Each exemplar has a `video_uid` and source recorded.
- [ ] Video DNA is from real analysis or labeled metadata-only.
- [ ] The Study's `briefContext` is ready for `socialseal-creator-briefing`, or its absence is explained.
