# SocialSeal Production Pipeline (vNext)

SocialSeal can select reference evidence, synthesise a blueprint and generate a brief with retained source lineage. The source links help review; they do not establish factual accuracy, practical usefulness or future performance. Inspect the live released tools for the requested deliverable before following any later production stage.

For a multi-stage production request, pair this engine with
`creative-production-gates.md`: confirm brand utility, let the user choose demand and
benchmark directions, approve material asset substitutions and a representative
prototype, then run final QA. Engine completion is not the same as post-ready.

Use this reference whenever a task touches reference videos, blueprints, briefs, or source-clip handoffs. Do not fall back to generic "write a content idea" behavior when these tools exist.

## Brief requests can enter directly

For an approved concept with a usable blueprint or supported scope, go directly to
`socialseal_generate_brief`, then `socialseal_get_brief` / `socialseal_export_brief`.
Use `socialseal_update_brief` for ordinary revisions. A new research pass is needed
only when the evidence or scope requires it; a calendar-only or document-formatting
request does not require the full pipeline. If a named action is absent, inspect
the compatibility target using `socialseal_get_tool_schema` and invoke it with
`socialseal_call_tool` (`toolName`, `body`, `workspaceId`). Preserve actual funding,
pending and missing-data states rather than silently switching to manual authoring.

## The opportunity spine

Every production artifact is tied together by a stable `opportunityKey` (8-128 chars). The same key flows:

```
journey / opportunity  ->  blueprint  ->  brief  ->  editor handoff
        (opportunityKey is the join across all of them)
```

A blueprint and brief for the same opportunity share one `opportunityKey`. Preserve it in the editor handoff; do not mint a new key per stage.

## Stage 1: Identify reference videos (evidence)

The engine selects exemplar videos from real tracked data. You rarely hand-pick from scratch.

Scope a blueprint generation by one of:

- `scopeType: "topic"` with `pillarId` (uses pillar seed terms)
- `scopeType: "competitor"` with `competitorBrandIds[]` (uses brand aliases, mentions, handles)
- `scopeType: "tracking_group"` with `trackingGroupId` (uses the group's search keywords)
- `scopeType: "manual"` with `videoUids[]` (hand-picked)
- `scopeType: "list"` with `listId` + `readinessRunId`

Or use query-native semantic retrieval: pass a `retrievalPrompt` (2-2000 chars) on a topic/competitor/tracking_group scope. This routes through broad video retrieval and clusters candidates. `retrievalPrompt` is not allowed with manual or list scope.

Refinement controls: `pinnedVideoUids[]`, `excludedVideoUids[]`, `promotedCandidateTarget` (<=24), `platformIds[]`, `region`, `language`, `timePeriod` (e.g. `30d`).

Preview before committing: pass `previewOnly: true` to inspect candidate and promoted-exemplar lists (with scores, matched keywords, sources) without creating a blueprint version.

For ad hoc or deeper analysis of a single video, use `tracked-video-extract` (`ensureAnalysis: true`) to resolve Video DNA, shots, and frames for a tracked identifier or an allowed public URL.

Engine tools:
- `vnext-blueprints-generate` (candidate selection + analysis queueing live here)
- `tracked-video-extract` (Video DNA for one video or URL)
- `vnext-cluster-videos` (cluster reference videos)

## Stage 2: Analyze reference videos (Video DNA)

When `vnext-blueprints-generate` selects promoted exemplars that lack completed analysis, it queues analysis automatically and returns `status: "draft"` with a summary like "Analysis queued. Blueprint will generate once promoted exemplar analysis completes." Poll the blueprint until analysis lands.

For explicit analysis, `tracked-video-extract` returns structured analysis: hook, content style, video structure, specific attributes, production qualities, transcript/audio/visual analysis, plus signed frame and asset URLs.

Do not assert visual/format claims you have not seen. Label evidence as metadata-only when analysis is not available.

## Stage 3: Compile a blueprint (best practices + evidence)

`vnext-blueprints-generate` compiles selected exemplars into a blueprint version with:
- `best_practices[]`: the grounded, reusable mechanisms
- `evidence[]`: the exemplar references behind each practice
- `selected_video_uids` / `selected_candidates` with scores and matched keywords

Status semantics (never fabricate):
- `draft`: queued / analysis pending
- `generated`: ready
- `missing_data`: no qualifying evidence for the scope. The engine writes an explicit `missing_data` version with a summary (e.g. "no tracking group keywords found for this scope") instead of inventing content. Surface that to the user and fix the scope.

Read and shots:
- `vnext-blueprints-read`: history and a specific version
- `vnext-blueprints-shots-read`: shot-lift rows and pinned shot assets (signed URLs); these define the blueprint's panels/shots
- `vnext-blueprints-shots-refresh`: queue a refresh of shot assets

A blueprint is the source of truth for the brief and editor handoff. Use each shot panel's `panelId` in a coverage table linking approved source clips to shots. This table is a handoff document, not a persisted SocialSeal mapping.

## Stage 4: Generate the brief

`vnext-briefs-generate` produces a brief grounded in a blueprint:
- from an existing blueprint: pass `blueprintId` (+ optional `blueprintVersion`)
- from scope: pass `scopeType` + scope fields and the engine resolves/creates the blueprint
- from a prompt: pass `retrievalPrompt` (cannot be combined with `blueprintId`/`blueprintVersion`)

Optional `brandContext` (brandName, productName, campaignGoal, notes, locale, platform) carries a concise summary of approved audience needs, product/service facts with source references and creative constraints. Read relevant documents first and pass supported context; do not assume the engine retrieves those documents or verifies every supplied claim.

Read and export:
- `vnext-briefs-read`: generated briefs and version history
- `vnext-briefs-export`: export a brief as markdown by `opportunityKey` (+ optional `version`)

For multiple concepts, generate and export the individual briefs. Creative packs have retired.

Use the engine path for new briefs to retain evidence and version lineage, then check the result. Manual authoring is appropriate for an explicit user choice, unavailable generation or unresolved `missing_data`; document the reason. Engine-generated does not mean better than manual or ready for production.

## Stage 5: Prepare source clips and an editor handoff

SocialSeal retains the source-clip library, blueprint evidence, and brief exports.
Asset Studio generation, clip-to-shot mapping APIs, generated-asset sharing, and
FCPXML export have retired. Do not promise a rendered video or timeline from these
retired tools; use the user's editor for assembly and finishing.

1. Inspect available clips with `vnext-clips-read`, signing source URLs as needed.
2. Upload missing rights-cleared footage with `vnext-clips-create`:
   - `action: "create"` returns a signed upload target; upload bytes to storage.
   - `action: "finalize"` requires `clipId`, `fileName`, `storagePath`, `mimeType`,
     `sizeBytes`, and `rightsAttested: true`.
3. Use `socialseal-asset-planning` to prepare a coverage table of real `panelId`s,
   approved clips, trim suggestions, rights, and missing-footage decisions. Do not
   claim the table creates backend mappings.
4. Hand off the exported brief, approved coverage table, source files or signed
   download links, and delivery specs to the user's editor. Confirm source access;
   signed URLs may expire. Preserve hook order and evidence-backed claims.
5. Label the output an editor handoff. Assembly, captions, audio, rendering, and
   mobile playback QA happen in the editor; a handoff is not a finished video.

Do not upload footage the workspace does not have rights to.

## End-to-end (happy path)

1. Pick or define the opportunity and `opportunityKey` and scope.
2. `vnext-blueprints-generate` with `previewOnly: true` to inspect candidate exemplars; refine with pins/exclusions/prompt.
3. `vnext-blueprints-generate` (commit) -> poll `vnext-blueprints-read` until `generated`.
4. `vnext-blueprints-shots-read` to get panels/shots.
5. `vnext-briefs-generate` from the `blueprintId`; `vnext-briefs-export` for the markdown brief.
6. Fill the source-clip library (`vnext-clips-create`) and document approved panel coverage.
7. Export the brief and hand off source clips, coverage, and delivery specs to the editor.

## Carousel branch

For a carousel, reuse the same evidence stages through opportunity and benchmark
selection, then route to `socialseal-carousel-production` instead of pretending the
brief and clip tools render slides. The carousel skill applies the approved brand
utility, benchmark mechanisms, visual direction, rights/location-aware asset map,
prototype approval, slide rendering, and phone-size QA.

## Hard rules

- Reuse one `opportunityKey` across the blueprint, brief, and editor handoff.
- Treat `missing_data` as a real outcome. Fix scope or evidence; never paper over it with invented best practices.
- Use real blueprint `panelId`s to identify shots in the coverage table.
- Only finalize clips with `rightsAttested: true`.
- Call the exported brief and source-clip package an editor handoff; only call a video post-ready after editor finishing and final QA pass.
- Never call a brief, blueprint, shot list, outline, placeholder set, or unverified
  asset treatment finished content.
- Never put literal workspace IDs, blueprint IDs, clip IDs, or share tokens in shared/public artifacts; use placeholders.
