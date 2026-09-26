---
name: socialseal-generation-prompts
description: >-
  Use this skill when real footage is missing and the user asks for generated B-roll,
  images, storyboard frames, cover explorations, voice guides, or prompts to fill a
  SocialSeal blueprint panel. Keep outputs social-native, non-deceptive, tied to a
  specific shot job, rights-safe, and clearly labeled as reference, draft, or
  production candidate.
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

This skill writes prompts for reference images, storyboard frames, draft B-roll, cover explorations, or voice guides tied to a blueprint shot panel. Actual media generation requires an available external generation tool. SocialSeal does not generate or assemble these assets. If no suitable tool is available, deliver the prompts and settings as a handoff.

See `references/production-pipeline.md`. Generated clips are reference or draft material; they do not replace lived creator footage when the shot needs authenticity.

Use the approved visual direction from `references/creative-production-gates.md`.
Do not fill an unspecified design gap with generic gradients, option/step pills,
arbitrary colors, fake social UI, or commercial stock aesthetics.

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
   Include the approved brand/reference visual mechanisms and explicitly excluded
   template treatments.
4. **Write the positive prompt.** Be concrete about scene, action, lens, lighting, social-native texture, and what the viewer should understand.
5. **Write the negative prompt.** Exclude over-polished commercial style, distorted hands/faces, fake logos, incorrect products, unreadable text, invented claims.
6. **Separate text rendering.** Unless the tool is reliable with text, generate no-text assets and add exact text later in editing/design tools.
7. **Document settings and hand off.** Record the intended external model/tool, aspect ratio, seed when supported, and prompt. If media was generated, record the actual result and usage rights. Give images, storyboards, and voice guides directly to the editor; only supported video files go through `socialseal-asset-planning` for rights verification and source-clip upload (`vnext-clips-create`, `rightsAttested: true`). Document the `panelId` association in the editor handoff coverage table, not a SocialSeal mapping API.

## Output

- prompt(s) by asset type and the target `panelId`
- negative prompt(s)
- technical settings
- usage note: reference only, draft asset, or production candidate
- revision instructions and an editor handoff; optional source-clip upload for a rights-cleared video produced externally

## Do / Don't

Do:
- tie every generated asset to a specific blueprint shot panel
- keep scenes grounded in the brief and blueprint
- use no-text generation when exact text matters
- label AI-generated assets clearly in handoff and clip metadata

Don't:
- invent product capabilities, places, people, or endorsements
- invent brand styling or present a generated destination image as documentary proof
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
- [ ] Prompts are handed off, or externally generated media is labeled with rights confirmed; any panel coverage is documented in the handoff.
