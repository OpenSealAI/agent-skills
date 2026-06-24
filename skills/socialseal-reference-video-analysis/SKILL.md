---
name: socialseal-reference-video-analysis
description: >-
  Use this skill when identifying and analyzing the reference videos that already
  surface for tracked searches: finding exemplars by scope or semantic prompt,
  previewing promoted candidates, and extracting Video DNA (hook, structure, shots,
  production qualities) to ground a blueprint. This is the evidence stage before
  blueprints and briefs.
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
    - asset-studio
---

# SocialSeal Reference Video Analysis

## Overview

SocialSeal does not start content from a blank prompt. It lifts patterns from real videos that already surface for the brand's tracked searches. This skill is the evidence stage: identify the right reference videos for an opportunity, and analyze them into Video DNA you can ground a blueprint on.

Do not hand-invent "what good looks like." Pull exemplars from SocialSeal and read their actual analysis. See `references/production-pipeline.md` for the full pipeline and `references/mcp-and-cli-usage.md` for the call patterns.

## When to Use

- Selecting exemplar videos for a blueprint scope (topic, competitor, tracking group, list, or manual).
- Exploring candidates with a semantic `retrievalPrompt` before committing.
- Extracting Video DNA for one or more specific videos or public URLs.
- Clustering reference videos to see repeated mechanisms.

Hand off the selected, analyzed exemplars to `socialseal-blueprint-builder`.

## Inputs

Required:
- workspace id (or a configured default)
- an opportunity definition and its `opportunityKey`
- a scope: `topic` + `pillarId`, `competitor` + `competitorBrandIds`, `tracking_group` + `trackingGroupId`, `list` + `listId`, or `manual` + `videoUids`

Good to have:
- a `retrievalPrompt` describing the content you want exemplars of (topic/competitor/tracking_group scopes only)
- `platformIds`, `region`, `language`, `timePeriod` (e.g. `30d`)
- `pinnedVideoUids`, `excludedVideoUids`, `promotedCandidateTarget`

## Workflow

1. **Confirm scope and workspace.** Identify the opportunity and reuse its `opportunityKey`.
2. **Preview candidates.** Call `vnext-blueprints-generate` with `previewOnly: true`. Inspect the candidate and promoted-exemplar lists: each carries a score, matched keywords, sources, and metrics. Do not generate yet.
3. **Refine selection.** Pin must-include exemplars (`pinnedVideoUids`), drop off-scope or off-market ones (`excludedVideoUids`), and set `promotedCandidateTarget` for how many exemplars to promote. For semantic exploration, set `retrievalPrompt`.
4. **Analyze Video DNA.** For promoted exemplars that need detail, call `tracked-video-extract` with `ensureAnalysis: true` to resolve hook, content style, video structure, specific attributes, production qualities, transcript/audio/visual analysis, and signed frame/asset URLs. For a one-off public video, use `extract-url` with `allowUntracked: true`.
5. **Cluster if needed.** Use `vnext-cluster-videos` to group exemplars into repeated mechanisms when the set is large.
6. **Record evidence.** For every exemplar capture the human-readable citation (video title/URL, `@author_handle`, and the `"keyword" [market, platform]` it surfaced for) plus the analyzed DNA. Keep `video_uid` (and `search_result_id` where it came from a ranked row) as an internal traceability note for tool calls and blueprint joins. Remember exemplars are anecdotal creative evidence, not proof a mechanism will perform; see `references/evidence-and-confidence.md`.

## Tool Calls (MCP-first)

Preview exemplars for a tracking-group scope:

```text
socialseal_call_tool {
  "function": "vnext-blueprints-generate",
  "workspaceId": "<workspace-id>",
  "body": {
    "workspaceId": "<workspace-id>",
    "opportunityKey": "<opportunity-key>",
    "scopeType": "tracking_group",
    "trackingGroupId": <group-id>,
    "timePeriod": "30d",
    "promotedCandidateTarget": 12,
    "previewOnly": true
  }
}
```

Semantic exploration with a prompt (topic scope):

```text
socialseal_call_tool {
  "function": "vnext-blueprints-generate",
  "workspaceId": "<workspace-id>",
  "body": {
    "workspaceId": "<workspace-id>",
    "opportunityKey": "<opportunity-key>",
    "scopeType": "topic",
    "pillarId": "<pillar-id>",
    "retrievalPrompt": "first-timer walkthroughs that answer cost and timing",
    "previewOnly": true
  }
}
```

Extract Video DNA for promoted exemplars:

```text
socialseal_call_tool {
  "function": "tracked-video-extract",
  "workspaceId": "<workspace-id>",
  "body": {
    "ensureAnalysis": true,
    "includeAssets": true,
    "items": [{ "videoUid": "<video-uid>" }]
  }
}
```

Poll analysis status:

```text
socialseal_get_tool_status { "id": "<video-uid>", "kind": "video_analysis", "includeResults": true }
```

CLI equivalents:

```bash
npx -y @socialseal/cli tools call --function vnext-blueprints-generate --workspace-id <workspace-id> --body @preview.json --pretty
npx -y @socialseal/cli video extract --video-uid <video-uid> --ensure-analysis --wait --out-dir ./video-assets --workspace-id <workspace-id>
npx -y @socialseal/cli video extract --url <public-video-url> --allow-untracked --wait --workspace-id <workspace-id>
```

## Output

- a list of selected exemplars cited by video title/URL, `@handle`, and the `"keyword" [market, platform]` (with `video_uid`/`search_result_id` kept as a traceability note), plus score and source
- Video DNA per exemplar: hook, first frame, structure, hero/supporting shots, useful details or mood cues, production qualities, caption/CTA style, account type
- format and lens labels (aspirational vs utility/practical) with the evidence behind each
- a note on which exemplars are analyzed vs metadata-only

## Do / Don't

Do:
- preview before generating; refine with pins and exclusions
- inspect actual analysis/frames before claiming a visual or format pattern
- cite exemplars by title/URL and `@handle`; keep `video_uid`/`search_result_id` as a traceability note for the blueprint
- separate owned, creator, media, affiliate, and competitor exemplars

Don't:
- hand-pick "good examples" from outside SocialSeal when scoped exemplars exist
- infer a pattern from a single example, or present an exemplar as proof a hook will work
- make platform-age claims when `published_at` is blank (see `references/socialseal-data-contract.md`)
- copy hooks verbatim; capture the mechanism

## Troubleshooting

- Preview returns `missing_data`: the scope has no qualifying evidence. Widen the keyword/scope, change `timePeriod`, or pick a different scope before generating.
- Exemplars lack analysis: `tracked-video-extract` with `ensureAnalysis: true`, then poll `video_analysis` status.
- `retrievalPrompt` rejected: it is not allowed for `manual` or `list` scope; use a topic/competitor/tracking_group scope.
- Too many viral outliers: lower `promotedCandidateTarget` and pin representative exemplars instead.

## Verification Checklist

- [ ] Scope and `opportunityKey` are confirmed and reused.
- [ ] Exemplars were previewed and refined, not blindly generated.
- [ ] Each exemplar has a `video_uid` and source recorded.
- [ ] Video DNA is from real analysis or labeled metadata-only.
- [ ] Output is ready to ground `socialseal-blueprint-builder`.
