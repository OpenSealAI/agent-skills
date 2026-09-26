# SocialSeal Production Pipeline (vNext)

SocialSeal can select reference evidence, synthesise a blueprint and generate a brief with retained source lineage. The source links help review; they do not establish factual accuracy, practical usefulness or future performance. Inspect the live released tools for the requested deliverable before following any later production stage.

For a multi-stage production request, pair this engine with
`creative-production-gates.md`: confirm brand utility, let the user choose demand and
benchmark directions, approve material asset substitutions and a representative
prototype, then run final QA. Engine completion is not the same as post-ready.

Use this reference whenever a task touches reference videos, blueprints, briefs, or generated rough cuts. Do not fall back to generic "write a content idea" behavior when these tools exist.

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
journey / opportunity  ->  blueprint  ->  brief  ->  generated asset (rough cut)
        (opportunityKey is the join across all of them)
```

A blueprint, a brief, and an asset for the same opportunity share one `opportunityKey`. Reuse it; do not mint a new key per stage.

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

A blueprint is the source of truth for the brief and for the Asset Studio edit spec. Each shot panel has a `panelId` used downstream for clip mapping.

## Stage 4: Generate the brief

`vnext-briefs-generate` produces a brief grounded in a blueprint:
- from an existing blueprint: pass `blueprintId` (+ optional `blueprintVersion`)
- from scope: pass `scopeType` + scope fields and the engine resolves/creates the blueprint
- from a prompt: pass `retrievalPrompt` (cannot be combined with `blueprintId`/`blueprintVersion`)

Optional `brandContext` (brandName, productName, campaignGoal, notes, locale, platform) carries a concise summary of approved audience needs, product/service facts with source references and creative constraints. Read relevant documents first and pass supported context; do not assume the engine retrieves those documents or verifies every supplied claim.

Read and export:
- `vnext-briefs-read`: generated briefs and version history
- `vnext-briefs-export`: export a brief as markdown by `opportunityKey` (+ optional `version`)

`creative-pack-generate` / `creative-pack-export` produce a broader creative pack when more than a single brief is needed.

Use the engine path for new briefs to retain evidence and version lineage, then check the result. Manual authoring is appropriate for an explicit user choice, unavailable generation or unresolved `missing_data`; document the reason. Engine-generated does not mean better than manual or ready for production.

## Stage 5: Generate the video from library clips (Asset Studio)

Asset Studio assembles a rough cut from a workspace clip library that follows the blueprint's shots.

1. Put clips in the library:
   - `vnext-clips-read`: list clips, optionally sign source URLs
   - `vnext-clips-create` (`action: "create"`): get a signed upload target; upload bytes to storage; then `action: "finalize"` with `clipId`, `fileName`, `storagePath`, `mimeType`, `sizeBytes`, and `rightsAttested: true`
2. Map clips to blueprint shots:
   - `vnext-clip-shot-mappings-read`: read current clip-to-panel mappings for a `blueprintId`
   - `vnext-clip-shot-mappings-write`: `action: "upsert"` with `blueprintId`, `panelId`, `clipId`, optional `source` (`suggested`|`override`); `action: "delete"` to clear a panel
3. Create and refine the rough cut:
   - `vnext-generated-asset-create`: pass `blueprintId`, `title`, and an `editSpec` (`version`, `fps`, `width`, `height`, `totalDurationSeconds`, `shots[]` where each shot has `panelId`, `clipId`, `title`, `kind`, `shotLabel`, `sourceStartSeconds`, `durationSeconds`, `evidenceIds[]`)
   - `vnext-generated-assets-read`: `action: "list"` by `blueprintId` or `action: "detail"` by `assetId`
   - `vnext-generated-asset-optimize`: `action: "optimize"` or `action: "create-revision"` on an `assetId`
   - `vnext-generated-asset-export`: export FCPXML by `assetId` (`format: "fcpxml"`) for finishing in an editor
   - `vnext-generated-asset-share`: create/read/revoke a share link (read is unscoped via `shareToken`)

`rightsAttested: true` is required to finalize a clip. Do not upload or assemble footage the workspace does not have rights to.

## End-to-end (happy path)

1. Pick or define the opportunity and `opportunityKey` and scope.
2. `vnext-blueprints-generate` with `previewOnly: true` to inspect candidate exemplars; refine with pins/exclusions/prompt.
3. `vnext-blueprints-generate` (commit) -> poll `vnext-blueprints-read` until `generated`.
4. `vnext-blueprints-shots-read` to get panels/shots.
5. `vnext-briefs-generate` from the `blueprintId`; `vnext-briefs-export` for the markdown brief.
6. Fill the clip library (`vnext-clips-create`), map clips to panels (`vnext-clip-shot-mappings-write`).
7. `vnext-generated-asset-create` from an editSpec; `optimize`; `export` FCPXML; `share`.

## Carousel branch

For a carousel, reuse the same evidence stages through opportunity and benchmark
selection, then route to `socialseal-carousel-production` instead of pretending the
video rough-cut engine renders slides. The carousel skill applies the approved brand
utility, benchmark mechanisms, visual direction, rights/location-aware asset map,
prototype approval, slide rendering, and phone-size QA.

## Hard rules

- Reuse one `opportunityKey` across the blueprint, brief, and asset.
- Treat `missing_data` as a real outcome. Fix scope or evidence; never paper over it with invented best practices.
- Use blueprint `panelId`s as the contract between shots, clip mappings, and the editSpec.
- Only finalize clips with `rightsAttested: true`.
- Call Asset Studio output a rough cut until editor finishing and final QA pass.
- Never call a brief, blueprint, shot list, outline, placeholder set, or unverified
  asset treatment finished content.
- Never put literal workspace IDs, blueprint IDs, clip IDs, or share tokens in shared/public artifacts; use placeholders.
