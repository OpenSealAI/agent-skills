# SocialSeal Production Pipeline (vNext)

SocialSeal can study reference videos, compile what they show into a Study revision and generate a brief with retained source lineage. The source links help review; they do not establish factual accuracy, practical usefulness or future performance. Inspect the live released tools for the requested deliverable before following any later production stage.

For a multi-stage production request, pair this engine with
`creative-production-gates.md`: confirm brand utility, let the user choose demand and
benchmark directions, approve material asset substitutions and a representative
prototype, then run final QA. Engine completion is not the same as post-ready.

Use this reference whenever a task touches reference videos, Studies, briefs, or source-clip handoffs. Do not fall back to generic "write a content idea" behavior when these tools exist.

Every brief is generated from a Study. Blueprints and topic-only brief requests have
retired: a brief request without a usable Study returns `study_needed` (or
`study_required`) instead of a brief. Understanding one video is a one-video Study.

## Brief requests can enter directly

For an approved concept with a usable Study revision, go directly to
`socialseal_generate_brief` with its `studyContext`, then `socialseal_get_brief` /
`socialseal_export_brief`. Use `socialseal_update_brief` for ordinary revisions. When
no Study fits yet, call `socialseal_generate_brief` anyway: it starts nothing and
returns `study_needed` with Study subjects to offer the user (see Stage 4). A
calendar-only or document-formatting request does not require the full pipeline. If a
named action is absent, use host tool search to load its live schema. If it remains
unavailable, report the missing operation and preserve completed work. Preserve
actual funding, pending and missing-data states rather than silently switching to
manual authoring.

## The opportunity spine

Every production artifact is tied together by a stable `opportunityKey` (8-128 chars). The same key flows:

```
journey / opportunity  ->  Study  ->  brief  ->  editor handoff
        (opportunityKey joins the brief and handoff; the Study is cited by studyRef + revision)
```

A brief records the Study revision it was generated from. Preserve the `opportunityKey` and that Study reference in the editor handoff; do not mint a new key per stage.

## Stage 1: Choose what to study (evidence)

A Study works from real videos. You rarely hand-pick from scratch. Start one with
`socialseal_start_study` and a `subject`:

- `{ "kind": "topic", "topicId": "<topic-id>" }` or `{ "kind": "topic", "keywords": [...], "question": "..." }`
- `{ "kind": "competitor", "brandId": "<brand-id>" }` or `{ "kind": "competitor", "handle": "<handle>" }`
- `{ "kind": "creator", "handle": "<handle>", "platformId": 1 }`
- `{ "kind": "monitor_finding", "monitor": { ... } }` for a Monitor finding
- `{ "kind": "saved_set", "videoListId": "<video-list-id>" }`
- `{ "kind": "videos", "urls": [...], "videoUids": [...] }` for specific videos; one video is `{ "kind": "videos", "urls": ["<video-url>"] }`

Narrow with `platformIds` (1 TikTok, 2 Instagram, 3 YouTube), `regions` (country
codes) and `windowDays`. A brief tool's `study_needed` candidates carry ready-made
`startStudyArguments`; use them as given.

A matching Study is reused for free. Photo and carousel posts are studied too; a post
that cannot be studied is skipped with a reason and the rest continue.

Named tools:
- `socialseal_start_study` (start or reuse a Study; prices missing Video DNA)
- `socialseal_get_study` (read a Study revision and its per-video evidence)
- `socialseal_extract_video_assets` (frames and source assets for stored video identifiers; not the route for understanding a video)

## Stage 2: Approve and run Video DNA

Starting or reusing a Study is free. Video DNA for videos that lack it is priced first:

- `ready`: the Study exists from existing evidence; nothing to approve.
- `approval_required`: nothing has run or been charged. Show the user the returned `price` (USD for a wallet workspace, credits for a subscription) and wait for approval.
- After approval, resend the same request with `maxCostUsd` (wallet) or `approvedCredits` (subscription) set to that price, plus an `idempotencyKey` you keep. After a timeout or an uncertain outcome, retry the unchanged request with the same key: it returns the same Study and never charges twice.
- `price_changed`: the price rose above the approved amount; nothing ran or was charged. Recovery depends on the workspace:
  - Wallet (USD): the response carries no `price`. Send the request again without approval fields (no `maxCostUsd` or `idempotencyKey`) to get a fresh quote, show the user the returned `price`, and once they approve it resend with that `maxCostUsd` and a new `idempotencyKey`, as the response's `nextStep` directs. The original key stays bound to the old maximum, so raising it under that key is rejected.
  - Subscription (credits): the response carries the new `price`. Show it, get approval again, then resend with that `approvedCredits` as its `nextStep` directs.
- `funding_required`: nothing ran. Share the returned funding link (never invent one) and keep its `operationId`; after a top-up, resend with the same idempotency key.
- `enriching`: Video DNA is running and is charged once, only for videos that succeed. Poll `socialseal_get_study` with the `studyRef`.

Do not assert visual/format claims you have not seen. Label evidence as metadata-only when Video DNA is not available.

## Stage 3: Read the Study (findings + evidence)

`socialseal_get_study` returns a Study revision with:
- findings: the grounded, reusable mechanisms, including the action finding a brief is made from
- coverage: how many videos have Video DNA and what is missing
- per-video evidence: hooks, CTAs, shots, beats, style and metrics (photo evidence by one-based slide)
- `briefContext`: the `studyContext` for a brief, present only when the revision can support one

Status semantics (never fabricate):
- `enriching`: Video DNA is still running; read again for the next revision
- `ready` with `briefContext`: usable for a brief
- `ready` without `briefContext`: this revision has no briefable action finding. Surface that to the user and study more videos or a broader subject instead of inventing content.

A Study is the evidence behind the brief and editor handoff. Cite its `studyRef` and revision, not a reconstructed summary.

## Stage 4: Generate the brief

`socialseal_generate_brief` (or `socialseal_start_brief_run` for a polled run) produces a brief grounded in a Study:
- from a Study: pass `studyContext` (`{ "studyRef", "revision", "findingId": "action" }`, as `briefContext` returns it)
- as the next member of a series: `socialseal_start_brief_run` with `continuesBriefId` + `continuationId`; the saved brief supplies its Study revision

Without a usable Study the brief tools start and charge nothing. They return:

```text
{ "status": "study_needed", "message", "nextStep", "reuse", "perVideoCredits",
  "candidates": [{ "kind", "label", "reason", "preview", "startStudyArguments", "estimatedPrice" }] }
```

1. If `reuse` carries a recent Study's `studyContext` that fits the request, offer it first; it costs nothing to reuse.
2. Otherwise offer the ranked candidates as plain choices: a topic, a competitor, a creator, or specific videos. Show each `label`, `reason`, `preview` (video and account counts, platforms, markets, freshness) and `estimatedPrice` (an upper bound).
3. Start only the subject the user picks, with its `startStudyArguments`, and apply Stage 2: run paid Video DNA only after the user approves the returned price.
4. When `socialseal_get_study` returns `briefContext`, retry the brief with it as `studyContext`.

Optional `brandContext` (brandName, productName, campaignGoal, notes, locale, platform) carries a concise summary of approved audience needs, product/service facts with source references and creative constraints. Read relevant documents first and pass supported context; do not assume the engine retrieves those documents or verifies every supplied claim.

Read and export:
- `socialseal_get_brief`: generated briefs and version history
- `socialseal_export_brief`: export a brief as markdown by `opportunityKey` (+ optional `version`)

For multiple concepts, generate and export the individual briefs. Creative packs have retired.

Use the engine path for new briefs to retain evidence and version lineage, then check the result. Manual authoring is appropriate for an explicit user choice, unavailable generation, a declined Study or unresolved `missing_data`; document the reason. Engine-generated does not mean better than manual or ready for production.

## Stage 5: Prepare source clips and an editor handoff

SocialSeal retains the source-clip library, Study evidence, and brief exports.
Asset Studio generation, clip-to-shot mapping APIs, generated-asset sharing, and
FCPXML export have retired. Do not promise a rendered video or timeline from these
retired tools; use the user's editor for assembly and finishing.

1. Inspect available clips with `socialseal_list_source_clips`, signing source URLs as needed.
2. Call `socialseal_prepare_source_clip_upload` for missing rights-cleared footage,
   then upload the bytes to its signed storage target. Call
   `socialseal_finalize_source_clip_upload` with the returned `clipId`, `fileName`,
   `storagePath`, `mimeType`, `sizeBytes`, and `rightsAttested: true`.
3. Use `socialseal-asset-planning` to prepare a coverage table of the brief's shot-list
   steps, approved clips, trim suggestions, rights, and missing-footage decisions. Do
   not claim the table creates backend mappings.
4. Hand off the exported brief, approved coverage table, source files or signed
   download links, and delivery specs to the user's editor. Confirm source access;
   signed URLs may expire. Preserve hook order and evidence-backed claims.
5. Label the output an editor handoff. Assembly, captions, audio, rendering, and
   mobile playback QA happen in the editor; a handoff is not a finished video.

Do not upload footage the workspace does not have rights to.

## End-to-end (happy path)

1. Pick or define the opportunity, its `opportunityKey` and the Study subject.
2. `socialseal_start_study` with that subject and a new `idempotencyKey`; on `approval_required`, show the price and get the user's approval, then resend with the approved amount and the same key.
3. Resend with `maxCostUsd` or `approvedCredits` and an `idempotencyKey` -> poll `socialseal_get_study` while it is `enriching`. If the completed Study has no `briefContext`, explain the evidence gap (no briefable finding) instead of briefing.
4. `socialseal_generate_brief` with that `studyContext`; `socialseal_export_brief` for the markdown brief.
5. Fill the source-clip library using `socialseal_prepare_source_clip_upload` and `socialseal_finalize_source_clip_upload`, and document approved shot coverage.
6. Export the brief and hand off source clips, coverage, and delivery specs to the editor.

## Carousel branch

For a carousel, reuse the same evidence stages through opportunity and benchmark
selection, then route to `socialseal-carousel-production` instead of pretending the
brief and clip tools render slides. The carousel skill applies the approved brand
utility, benchmark mechanisms, visual direction, rights/location-aware asset map,
prototype approval, slide rendering, and phone-size QA.

## Hard rules

- Reuse one `opportunityKey` across the brief and editor handoff, and cite the Study revision behind them.
- Never start paid Video DNA without the user's approval of the returned price. Keep the original idempotency key for timeouts, uncertain outcomes, funding retries and any retry of an unchanged accepted request; use a new key only for a newly approved price after a confirmed `price_changed`, as the response directs.
- Treat `missing_data` and a Study without `briefContext` as real outcomes. Fix the subject or evidence; never paper over them with invented best practices.
- Use the brief's shot-list steps to identify shots in the coverage table.
- Only finalize clips with `rightsAttested: true`.
- Call the exported brief and source-clip package an editor handoff; only call a video post-ready after editor finishing and final QA pass.
- Never call a brief, Study, shot list, outline, placeholder set, or unverified
  asset treatment finished content.
- Never put literal workspace IDs, Study refs, clip IDs, or share tokens in shared/public artifacts; use placeholders.
