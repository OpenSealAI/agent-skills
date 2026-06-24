---
name: socialseal-capcut-export-prep
description: >-
  Use this skill when finishing a SocialSeal Asset Studio rough cut in CapCut or
  another editor after FCPXML export: importing the timeline, organizing source
  clips, applying captions/overlays, setting export specs, naming, and mobile-view
  QC. This is the post-engine finishing step, not posting.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - capcut
    - editor-handoff
    - fcpxml
---

# SocialSeal CapCut Export Prep

## Overview

This skill finishes an Asset Studio rough cut for delivery. It starts from the FCPXML export produced by `socialseal-asset-studio-generation` (`vnext-generated-asset-export`) and prepares an editor-ready handoff and export checklist. It is about finishing files and specs, not posting.

See `references/production-pipeline.md`. The rough cut and its shot order come from the blueprint; finishing should respect that structure.

## When to Use

- Importing an FCPXML rough cut into CapCut or another editor.
- Organizing source clips, captions, overlays, and export settings.
- QC and editor handoff before delivery.

## Inputs

- the FCPXML export and `assetId` from Asset Studio
- the brief and blueprint shot order for reference
- source clips/assets (from the clip library or local copies)
- platform(s) and aspect ratios, caption/overlay text rules
- target duration and version count

## Workflow

1. **Import the FCPXML.** Bring the Asset Studio timeline into the editor; relink source clips from the clip library or local copies.
2. **Verify against the blueprint.** Confirm shot order and durations match the rough cut and brief; do not silently reorder hero/hook shots.
3. **Inventory files.** Raw footage, selects, audio, generated assets, captions, brand assets.
4. **Set edit rules.** Pace, caption style, overlay safe areas, music/audio, transitions, and what not to over-edit.
5. **Define export settings.** Common vertical baseline: 9:16, 1080x1920, H.264 MP4, platform-appropriate bitrate, original frame rate unless there is a reason to change.
6. **Name files.** `<brand>_<platform>_<concept>_<market>_<version>_<date>.mp4` or the team convention.
7. **QC on mobile.** Readability, crop, audio, caption timing, first frame, final CTA.
8. **Prepare handoff note.** Source folder, FCPXML/`assetId` reference, edit notes, export settings, QC checklist.

## Output

- imported, relinked timeline
- file manifest and editor handoff note (with `assetId`/FCPXML reference)
- export settings
- caption/overlay instructions
- QC checklist

## Do / Don't

Do:
- preserve the blueprint shot order and hook timing
- preserve raw creator feel for UGC
- keep overlays readable on a phone
- separate source files and final exports

Don't:
- restructure the rough cut away from the blueprint without a reason
- add heavy transitions that change the content type
- flatten all videos to one platform spec without checking the target
- rely on desktop preview only

## Troubleshooting

- FCPXML will not relink: confirm clip filenames/paths match the library export; re-sign source URLs via `vnext-clips-read` if needed.
- Captions too small: test on phone-size preview; increase size/contrast.
- Crop cuts important action: reframe manually rather than auto-cropping.
- Export too large: lower bitrate before lowering resolution.

## Verification Checklist

- [ ] FCPXML imported and source clips relinked.
- [ ] Shot order/timing matches the blueprint and brief.
- [ ] Export settings match platform needs.
- [ ] Captions/overlays pass mobile readability.
- [ ] Handoff note references the `assetId`/FCPXML and final file naming.
