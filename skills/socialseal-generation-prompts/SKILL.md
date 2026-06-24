---
name: socialseal-generation-prompts
description: >-
  Use this skill when writing image, video, storyboard, or voice prompts to produce
  reference or B-roll clips that fill a SocialSeal blueprint shot panel in the Asset
  Studio clip library. Keeps generated assets social-native and rights-safe, and
  routes finished clips to upload and clip-to-shot mapping.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - generation-prompts
    - clip-library
    - storyboard
---

# SocialSeal Generation Prompts

## Overview

Generated assets support production by filling shot panels that lack real footage. Use this skill to create reference images, storyboard frames, draft B-roll, cover explorations, or voice guides for a specific blueprint shot panel, then route the finished clip into the Asset Studio clip library.

See `references/production-pipeline.md`. Generated clips are reference or draft material; they do not replace lived creator footage when the shot needs authenticity.

## When to Use

- Filling a blueprint shot panel that has no captured footage.
- Producing storyboard frames or B-roll drafts to align a team before a shoot.
- Generating cover/thumbnail explorations or a voice guide.

## Inputs

- the blueprint shot panel this asset fills (`panelId`, shot label, kind) and the brief
- platform/aspect ratio
- desired output type: image, video, storyboard, voice, thumbnail, or mood reference
- brand constraints and what must not be invented
- whether text should be included now or added later

## Workflow

1. **Tie to a panel.** State which `panelId` the asset fills and the shot's job (hook, hero, detail, B-roll).
2. **Define the asset job.** Reference, storyboard, B-roll, thumbnail idea, voice guide, or editor aid.
3. **Extract non-negotiables.** Subject, setting, action, mood, camera style, aspect ratio, realism level.
4. **Write the positive prompt.** Be concrete about scene, action, lens, lighting, social-native texture, and what the viewer should understand.
5. **Write the negative prompt.** Exclude over-polished commercial style, distorted hands/faces, fake logos, incorrect products, unreadable text, invented claims.
6. **Separate text rendering.** Unless the tool is reliable with text, generate no-text assets and add exact text later in editing/design tools.
7. **Document settings and route to library.** Record model/tool, aspect ratio, seed, prompt, and result notes. Hand the finished clip to `socialseal-asset-studio-generation` for upload (`vnext-clips-create`, `rightsAttested: true`) and mapping to the `panelId`.

## Output

- prompt(s) by asset type and the target `panelId`
- negative prompt(s)
- technical settings
- usage note: reference only, draft asset, or production candidate
- revision instructions and a route to upload/map the clip

## Do / Don't

Do:
- tie every generated asset to a specific blueprint shot panel
- keep scenes grounded in the brief and blueprint
- use no-text generation when exact text matters
- label AI-generated assets clearly in handoff and clip metadata

Don't:
- invent product capabilities, places, people, or endorsements
- generate fake real creators or impersonations
- use generated assets as final UGC when the shot requires lived experience
- finalize generated clips without confirming rights

## Troubleshooting

- Output too polished: add "handheld", "natural light", "phone footage", "unedited", or category-specific realism cues.
- Output invents details: reduce scene complexity and specify allowed elements.
- Text is wrong: remove text from generation and add it in finishing tools.
- Panel still feels inauthentic: prefer captured footage via `socialseal-asset-planning`.

## Verification Checklist

- [ ] Each prompt names the blueprint `panelId` it fills.
- [ ] Prompt includes subject, action, setting, mood, and format.
- [ ] Negative prompt prevents common failure modes.
- [ ] Exact text is handled outside generation when needed.
- [ ] Finished clip is routed to upload and mapping with rights confirmed.
