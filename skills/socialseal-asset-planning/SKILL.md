---
name: socialseal-asset-planning
description: >-
  Use this skill when planning what footage to capture or gather so a SocialSeal
  blueprint's shot panels can be filled in the Asset Studio clip library. Maps
  blueprint shots to required clips, identifies coverage gaps, batches capture,
  and prepares clips for upload and clip-to-shot mapping.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - asset-plan
    - clip-library
    - shot-coverage
---

# SocialSeal Asset Planning

## Overview

Asset planning converts a blueprint's shot panels into a concrete capture and clip-library plan. The goal is that every shot panel the rough cut needs has a rights-cleared clip ready to upload and map. This is the bridge between `socialseal-blueprint-builder` and `socialseal-asset-studio-generation`.

See `references/production-pipeline.md`. Work from the blueprint shot panels (`vnext-blueprints-shots-read`), not a generic shot list.

## When to Use

- Turning blueprint shot panels into a capture/clip plan.
- Auditing clip-library coverage against blueprint panels.
- Batching capture and preparing clips for upload.

## Inputs

- the `blueprintId` and its shot panels (`panelId`, shot label, kind)
- current clip library (`vnext-clips-read`) and existing mappings (`vnext-clip-shot-mappings-read`)
- platform specs and aspect ratio
- available footage, creator/talent/location constraints, deadline

## Workflow

1. **List the shot panels.** From `vnext-blueprints-shots-read`, enumerate every `panelId` and what it needs (hook, hero, supporting, detail).
2. **Audit coverage.** Compare panels against the clip library and existing mappings. Mark each panel: covered, needs capture, needs sourcing, or needs generation.
3. **Plan capture for gaps.** For panels needing footage, write required shots first, then useful, then optional B-roll.
4. **Batch capture.** Group shots by location, setup, product, screen recording, creator, or time of day.
5. **Add validators.** Capture practical details that make utility content useful: signs, screens, maps, prices, steps, timing, packing, setup, texture, before/after.
6. **Prepare clips for upload.** Define file names and confirm usage rights for each clip (required to finalize with `rightsAttested: true`).
7. **Hand off.** Pass the plan to `socialseal-asset-studio-generation` (upload + map), and to `socialseal-generation-prompts` for any panel that should be filled with a generated reference clip.

## Output

- panel coverage table: `panelId` -> status (covered / capture / source / generate) -> clip or plan
- capture batch plan
- missing-asset list
- file naming convention and rights notes
- editor/handoff notes for shots that still need real footage

## Do / Don't

Do:
- plan against blueprint `panelId`s, not an abstract list
- mark shots required / useful / optional
- confirm rights before planning a clip for upload
- plan reusable B-roll across multiple panels/concepts

Don't:
- plan footage that does not map to a blueprint shot
- assume a panel is covered without checking mappings
- over-polish UGC assets
- forget thumbnails, first frames, safe areas, captions, source audio

## Troubleshooting

- A panel has no candidate footage: route it to `socialseal-generation-prompts` (generate a reference clip) or flag for a reshoot.
- Too expensive: reduce locations and combine capture batches.
- No hero shot exists for the hook panel: the concept is not production-ready; revisit the blueprint.

## Verification Checklist

- [ ] Every blueprint shot panel has a coverage status.
- [ ] Capture is batched where possible.
- [ ] Missing assets are listed with a fill path (capture/source/generate).
- [ ] Rights are confirmed for clips planned for upload.
- [ ] Plan hands off cleanly to Asset Studio generation.
