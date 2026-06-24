---
name: socialseal-video-concepting
description: >-
  Use this skill when turning a SocialSeal opportunity or keyword gap into short-form
  video concept routes that feed the blueprint engine. Produces concepts with viewer
  job, lens, hook and first-frame ideas, arcs, and the scope or retrievalPrompt to
  drive socialseal-blueprint-builder, plus a measurement intent.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - video-concepts
    - short-form
    - blueprint-input
---

# SocialSeal Video Concepting

## Overview

Video concepting is the ideation step that frames an opportunity into shootable routes and, crucially, into the scope or `retrievalPrompt` that drives the blueprint engine. A good concept names the search gap, picks a lens, and specifies the exemplar direction so `socialseal-blueprint-builder` can ground it in real videos.

See `references/production-pipeline.md` and `references/content-lenses.md`. Concepting precedes reference-video analysis and blueprint generation; it does not replace them.

## When to Use

- Translating an opportunity/gap into 3+ distinct concept families.
- Defining the blueprint scope (topic/competitor/tracking_group) or a `retrievalPrompt` per concept.
- Preparing concepts for grounding before any brief or rough cut.

## Inputs

- target platform, market, and keyword/topic, with the `opportunityKey`
- opportunity analysis or competitor/content evidence
- brand context and constraints
- available assets, creator type, or shoot context

## Workflow

1. **Name the search gap.** One sentence: "People search for X, but current surfaced content lacks Y."
2. **Select lens.** Aspirational (mood/emotion) or utility/practical (teach/plan/compare).
3. **Generate concept families.** At least three distinct: tutorial/walkthrough, comparison, first-timer guide, POV/day-in-life, list/map/pin, mistake/avoidance, or mood montage.
4. **For each concept, specify:** hook, first frame, arc, hero shot, supporting shots, useful detail or mood cue, CTA, and target keyword/topic.
5. **Attach an engine handle.** For each concept, define the blueprint input: a `scopeType` (+ scope fields) or a `retrievalPrompt` that would retrieve matching exemplars. This is what makes the concept groundable.
6. **Rank concepts.** Score by evidence fit, usefulness/emotional pull, production ease, and measurement clarity.
7. **Hand off.** Send the top concepts to `socialseal-reference-video-analysis` (preview exemplars) and `socialseal-blueprint-builder` (generate).

## Output

For each concept:
- name, viewer job, lens
- hook options and first 3 seconds
- arc / beats, hero shot, supporting shots
- caption direction and measurement keyword/topic
- blueprint input: scope or `retrievalPrompt`
- production difficulty

## Do / Don't

Do:
- produce multiple directions, not one early "best" idea
- give every concept a concrete blueprint scope or `retrievalPrompt`
- connect every concept to a measurement signal
- keep concepts shootable with available assets

Don't:
- generate generic viral ideas detached from the keyword gap
- treat a concept as final content; it must be grounded by a blueprint first
- copy competitor hooks directly
- use scripted ad language

## Troubleshooting

- Concepts feel generic: add the exact keyword and viewer hesitation, and a sharper `retrievalPrompt`.
- No exemplars surface in preview: widen the scope/keywords or revise the prompt before briefing.
- Concept does not map to a tracking group: add tracking coverage (`socialseal-tracking-group-design`) so it is measurable.

## Verification Checklist

- [ ] Each concept has a viewer job and lens.
- [ ] Each concept has hook, first frame, arc, and hero shot.
- [ ] Each concept carries a blueprint scope or `retrievalPrompt`.
- [ ] Each concept maps to a measurement keyword/topic.
- [ ] Top concepts are ranked and ready for grounding.
