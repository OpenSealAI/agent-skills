---
name: socialseal-asset-planning
description: >-
  Use this skill when the user provides a footage/image bank, asks which assets to
  use, wants a shot list or capture plan, or needs to know what is missing before a
  video or carousel can be produced. Map verified, rights-cleared assets to the
  grounded brief's shots, present meaningful source/substitute/reshoot choices, identify
  gaps, and prepare source clips and an editor handoff rather than guessing from filenames.
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

Asset planning converts a brief's shot list into a concrete capture and clip-library plan. The goal is that every planned video shot has a rights-cleared clip ready for the editor. This is the bridge between `socialseal-creator-briefing` and an editor handoff. Record shot coverage in the handoff document; SocialSeal's clip-to-shot mapping and generated-video tools have retired.

See `references/production-pipeline.md`. Work from the saved brief's shot list (`socialseal_get_brief`), grounded in its Study's observed shots, not a generic shot list.

Read `references/creative-production-gates.md` for production-bound work. The asset
gate must present meaningful choices and evidence, not silently assign approximate
images because they are visually convenient.

## When to Use

- Turning a brief's shot list into a capture/clip plan.
- Auditing clip-library coverage against the brief's shots.
- Batching capture and preparing clips for upload.

## Inputs

- the saved brief (`opportunityKey`, version) and its shot list (`step`, beat, overlay)
- current clip library (`socialseal_list_source_clips`) and any user-provided shot coverage table
- platform specs and aspect ratio
- available footage, creator/talent/location constraints, deadline

## Workflow

1. **List the shots.** From the brief's shot list (`socialseal_get_brief`), enumerate every `step` and what it needs (hook, hero, supporting, detail).
2. **Audit coverage.** Compare shots against the clip library and documented shot coverage. Mark each shot: covered, needs capture, needs sourcing, or needs generation.
   Inspect the actual media (or a contact sheet), not only filenames/descriptions.
   Record rights and subject/location confidence as `verified`, `likely`, or
   `unknown`.
3. **Plan capture for gaps.** For shots needing footage, write required shots first, then useful, then optional B-roll.
4. **Batch capture.** Group shots by location, setup, product, screen recording, creator, or time of day.
5. **Add validators.** Capture practical details that make utility content useful: signs, screens, maps, prices, steps, timing, packing, setup, texture, before/after.
6. **Prepare clips for upload.** Define file names and confirm usage rights for each clip. `socialseal_prepare_source_clip_upload` returns a signed upload target; upload bytes, then call `socialseal_finalize_source_clip_upload` with `clipId`, `fileName`, `storagePath`, `mimeType`, `sizeBytes`, and `rightsAttested: true`.
7. **Run the asset decision gate.** For material gaps, present 2-3 viable choices:
   verified owned material, rights-cleared stock, new capture/reshoot, generated
   reference, or a concept change. Get approval before using substitutes.
8. **Hand off.** Package the approved plan, exported brief, source clips, trim suggestions, and delivery specs for the user's editor. Route gaps to `socialseal-generation-prompts` only for approved generated references. SocialSeal does not assemble the video or export FCPXML.

## Output

- shot coverage table: brief shot `step` -> status (covered / capture / source / generate) -> clip or plan
- capture batch plan
- missing-asset list
- reviewed asset options with rights and location/factual confidence
- file naming convention and rights notes
- editor/handoff notes for shots that still need real footage

## Do / Don't

Do:
- plan against the brief's shot-list steps, not an abstract list
- mark shots required / useful / optional
- confirm rights before planning a clip for upload
- show the user the material asset choices for a major creative deliverable
- plan reusable B-roll across multiple shots/concepts

Don't:
- plan footage that does not map to a brief shot
- assume a shot is covered without inspecting the source clip and coverage table
- label or depict an unknown location/person/product as verified
- over-polish UGC assets
- forget thumbnails, first frames, safe areas, captions, source audio

## Troubleshooting

- A shot has no candidate footage: route it to `socialseal-generation-prompts` (write a prompt for an external generation tool) or flag for a reshoot.
- Too expensive: reduce locations and combine capture batches.
- No hero shot exists for the hook: the concept is not production-ready; revisit the brief or its Study.

## Verification Checklist

- [ ] Every brief shot has a coverage status.
- [ ] Capture is batched where possible.
- [ ] Missing assets are listed with a fill path (capture/source/generate).
- [ ] Rights are confirmed for clips planned for upload.
- [ ] Editor handoff includes the brief, approved coverage table, accessible source clips, and unresolved blockers.
