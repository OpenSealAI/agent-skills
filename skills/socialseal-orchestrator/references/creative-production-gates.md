# Creative Production Gates and Delivery States

Use this reference for multi-stage creative work: content plans with downstream
briefs, videos or carousels; production from an asset bank; or any request that
depends on SocialSeal research before making files.

## Start with a delivery contract

Before research or production, restate:

- final deliverables and file types
- platform, market, language, aspect ratio, duration or slide count
- deadline and production capacity
- whether credit-consuming journeys or Video DNA are allowed
- what the user means by final (brief, prototype, rough cut, editor-ready, or
  post-ready)

For work spanning three or more stages, show the stage plan and current stage. Do
not call a brief or shot list a finished video/carousel. SocialSeal supplies evidence,
briefs, and source clips. Media generation, assembled video prototypes/timelines,
and finishing require an external generation tool or editor. When none is
available, deliver the brief, storyboard, and editor handoff and state what remains.

## Use six decision gates

Move autonomously inside a confirmed gate. Present 2-3 options at each material
creative decision instead of making the user approve every minor action.

1. **Foundation gate.** Confirm persona, brand voice/constraints, measurement goal,
   and the brand utility bank: products, exclusions, real tips, itineraries, prices,
   timing, locations, proof, and facts needing confirmation.
2. **Demand gate.** Present candidate queries/topics and the audience job behind
   each. Ground them in a journey or ranked evidence. Let the user choose the
   production priority.
3. **Benchmark gate.** Present representative surfacing posts and 2-3 creative
   directions. Distinguish metadata-only review from focused or full Video DNA and
   state likely time/credit trade-offs before paid analysis.
4. **Asset gate.** Show which owned, rights-cleared stock, generated-reference, or
   new-capture assets can fill each content job. Label location/factual confidence as
   verified, likely, or unknown. Never silently use an unknown asset as a real place.
5. **Prototype gate.** Produce the first frame plus one representative body slide,
   or the opening 3-5 seconds/storyboard, before completing a large batch. Confirm
   hierarchy, language, visual direction, and asset treatment.
6. **Final QA gate.** Check evidence, facts, rights, location, brand voice, visual
   craft, safe areas, mobile readability, file integrity, and export specs.

If evidence or an essential asset is missing, present choices: change the concept,
source rights-cleared material, capture/reshoot, generate a clearly labeled draft
reference, or pause that deliverable. Do not paper over the gap.

## Save and reuse target segments

A segment found in one conversation (an under-served buyer, a niche rivals overlook,
a persona confirmed from search behaviour) should steer the next conversation's
briefs, concepts and plans. The workspace holds it between conversations.

**Save.** Finish the desk research first, then name the segment in one line: who
they are, the job or worry behind their searches, and the evidence it rests on. Offer
to save it with a single confirmation.

- Steers all of the brand's content: add it to `targetAudiences` in the Strategy.
  Read `socialseal_get_brand_strategy`, copy the published Strategy, add the segment,
  and save the complete result as a draft with `socialseal_propose_brand_strategy`
  (`expectedBaseRevisionId` is the revision you read, or `null` when none exists).
  Publish with `socialseal_publish_brand_strategy` once the user approves.
- Steers one campaign or is still a hypothesis: save a workspace note with
  `socialseal_create_workspace_note` (`type: "fact"` or `"decision"`, `key:
  "segments/<segment-slug>"`, `pinnedToCore: true`). Keep it to the segment, the job,
  the evidence and the date. Revise it with `socialseal_update_workspace_note`.

**Read before choosing who to write for.** Before a brief, concept set, creator brief
or plan slot picks its audience, read `socialseal_get_brand_strategy`
(`targetAudiences`, `excludedAudiences`), `socialseal_get_core_workspace_notes`, and
`socialseal_search_workspace_notes` for the topic's audience terms. Choose in this
order: the segment the user named, a saved segment that fits the topic, then the
Strategy's primary audience. With several saved segments, use the best fit and list
the others as alternatives.

**Say which segment.** Open the output with `Writing for: <segment> (source: user
request, workspace note, or Strategy)`, and carry the same line into the brief's
`brandContext.notes`. When the segment matches an excluded audience or contradicts a
Strategy rule, flag it and propose a version that passes. With none saved, state the
audience assumption in the same line.

## Use precise delivery states

- **Plan:** priorities and intended work; no production artifact.
- **Brief:** instructions for a creator/editor; not the content itself.
- **Prototype:** representative partial execution for direction approval.
- **Draft:** complete enough to review, with known gaps.
- **Rough cut:** video assembled in an external editor and requiring finishing.
- **Editor handoff:** brief, sources, shot coverage, copy, and notes packaged for
  the editor; no assembled timeline is promised.
- **Editor-ready:** the editor handoff plus any externally produced timeline
  required by the agreed delivery contract.
- **Production candidate:** complete output awaiting final factual/rights/brand QA.
- **Post-ready:** exported artifact passed final QA and has no unresolved blockers.

Use "done", "finished", or "ready-to-post" only for the state the user requested
and only after its checks pass. State unresolved blockers next to the status.

## Avoid generic AI creative defaults

Do not default to gradients, floating pills labeled "option"/"step", excessive empty
space, generic sans-serif templates, stock-marketing language, or arbitrary brand
colors. A treatment is valid only when it comes from the brand system, selected
social references, or an explicit user choice.

Anchor writing and design to real examples without copying them:

- hook and first-frame mechanism
- text density and hierarchy
- creator/local vocabulary and useful-detail depth
- image crop, sequence, pace, and proof objects
- platform conventions and safe areas

## Keep an audit trail

For large work, maintain a compact workflow manifest in the working artifact or
handoff:

- skills/stages used
- SocialSeal runs/exports and evidence scope
- approved topics, creative direction, and assets
- credit-consuming actions approved
- artifact state and remaining blockers

This makes resuming or auditing a long session possible without treating prior drafts
as approved evidence.
