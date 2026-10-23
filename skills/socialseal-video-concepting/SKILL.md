---
name: socialseal-video-concepting
description: >-
  Use this skill when the user asks for video ideas, creative routes, hooks, first
  frames, or ways to turn a search query/audience problem into short-form content.
  Generate multiple SocialSeal-groundable concept options before briefing or
  production, each with a viewer job, lens, arc, Study subject,
  production difficulty, and measurement intent.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - video-concepts
    - short-form
    - study-input
---

# SocialSeal Video Concepting

## Overview

Video concepting is the ideation step that frames an opportunity into shootable routes and, crucially, into the Study subject that grounds the brief. A good concept names the search gap, picks a lens, and specifies the exemplar direction so a SocialSeal Study can ground it in real videos.

See `references/production-pipeline.md` and `references/content-lenses.md`. Concepting precedes the Study and brief generation; it does not replace them. Concepts are hypotheses to ground in real surfacing videos and then test, not proven winners; see `references/evidence-and-confidence.md`.

For work that will proceed into production, read
`references/creative-production-gates.md`. Concepts are a decision gate, not an
excuse to select one route silently and build a large batch.

## When to Use

- Translating an opportunity/gap into 3+ distinct concept families.
- Defining the Study subject (topic, competitor, creator, saved set or specific videos) per concept.
- Preparing concepts for grounding before any brief or externally edited rough cut.

## Inputs

- target platform, market, and keyword/topic, with the `opportunityKey`
- opportunity analysis or competitor/content evidence
- brand context and constraints
- brand utility bank: real facts, tips, proof, exclusions, and facts needing confirmation
- available assets, creator type, or shoot context

## Workflow

1. **Name the search gap.** One sentence: "People search for X, but current surfaced content lacks Y."
2. **Select lens.** Aspirational (mood/emotion) or utility/practical (teach/plan/compare).
3. **Generate concept families.** At least three distinct: tutorial/walkthrough, comparison, first-timer guide, POV/day-in-life, list/map/pin, mistake/avoidance, or mood montage.
4. **For each concept, specify:** hook, first frame, arc, hero shot, supporting shots, useful detail or mood cue, CTA, and target keyword/topic.
5. **Attach an engine handle.** For each concept, define the Study subject that would cover matching exemplars: a topic (`topicId` or `keywords`, with a `question`), a competitor, a creator, a saved set, or specific videos. This is what makes the concept groundable.
6. **Rank concepts.** Score by evidence fit, usefulness/emotional pull, production ease, and measurement clarity.
7. **Present the concept decision.** Show the top 2-3 routes with trade-offs and ask
   the user to select, combine, or adjust them. Record the approved route and facts;
   do not produce every route unless requested.
8. **Hand off.** Send approved concepts to `socialseal-reference-video-analysis` (start the Study and approve any Video DNA) and then `socialseal-creator-briefing` (generate the brief from it).

## Output

For each concept:
- name, viewer job, lens
- hook options and first 3 seconds
- arc / beats, hero shot, supporting shots
- caption direction and measurement keyword/topic
- Study subject (or an existing Study to reuse)
- production difficulty
- brand utility/proof used and approval status

## Do / Don't

Do:
- produce multiple directions, not one early "best" idea
- give every concept a concrete Study subject
- connect every concept to a measurement signal
- keep concepts shootable with available assets

Don't:
- generate generic viral ideas detached from the keyword gap
- treat a concept as final content; it must be grounded by a Study first
- copy competitor hooks directly
- use scripted ad language

## Troubleshooting

- Concepts feel generic: add the exact keyword and viewer hesitation, and a sharper Study `question` or narrower subject.
- The Study returns too few videos or no `briefContext`: widen the subject/keywords or revise the question before briefing.
- Concept does not map to a tracking group: add tracking coverage (`socialseal-tracking-group-design`) so it is measurable.

## Verification Checklist

- [ ] Each concept has a viewer job and lens.
- [ ] Each concept has hook, first frame, arc, and hero shot.
- [ ] Each concept carries a Study subject.
- [ ] Each concept maps to a measurement keyword/topic.
- [ ] Top concepts are ranked and ready for grounding.
