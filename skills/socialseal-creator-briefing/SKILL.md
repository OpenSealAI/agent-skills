---
name: socialseal-creator-briefing
description: >-
  Use this skill when the user asks to create, rewrite, or improve a short-form video,
  creator, influencer, UGC or video-editor brief, including hooks, social-first language, shots,
  captions, and CTAs. Prefer a brief generated from a SocialSeal blueprint and real
  exemplars; use a clearly labeled manual hypothesis only when engine evidence is
  unavailable or missing_data.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - creator-brief
    - ugc
    - briefs-engine
    - hooks
---

# SocialSeal Creator Briefing

## Overview

A SocialSeal creator brief turns grounded evidence into creator-ready direction. Use the generation tools to retain blueprint evidence and version identity, then review the result. Tool use is not a guarantee of factual support, useful audience advice or better creative quality. Loading this skill does not itself generate a brief. A request for a Word document, editor framework or usual brief template is a delivery-format request, not a reason to bypass the engine.

See `references/production-pipeline.md` for the pipeline, `references/mcp-and-cli-usage.md` for call patterns, and `references/content-lenses.md` for lenses. Use `socialseal-blueprint-builder` when reference selection needs work; an existing usable blueprint or supported scope can go directly to brief generation.

Read `references/creative-production-gates.md` when the brief will feed immediate
production. Confirm the chosen concept, brand utility facts, benchmark direction,
and non-negotiable exclusions before generating.

## When to Use

- Generating a brief from an existing blueprint (`blueprintId`/version) or scope.
- Exporting a generated brief as markdown.
- Authoring a structured brief by hand when the engine is unavailable.

## Inputs

Required:
- platform and market
- target keyword/topic or content job, and the `opportunityKey`
- a blueprint (`blueprintId`) when using the engine, or exemplar evidence when authoring

Good to have:
- brand context (brandName, productName, campaignGoal, notes, locale, platform)
- approved brand utility/proof and facts needing confirmation
- creator type/persona, required assets/locations, compliance constraints
- deliverable count, length, aspect ratio, deadline

## Tool discovery and generation

1. **Resolve the requested work and workspace.** For an existing brief, read it and preserve its identity; do not regenerate for a caption tweak, formatting request or ordinary edit. For new briefs, look for the named `socialseal_generate_brief` action. If absent, list available tools without a category filter and look for `vnext-briefs-generate`; inspect its schema. Briefing spans `vnext` and `video-production`. Do not infer missing capability from one failed category lookup.
2. **Choose supported inputs.** Reuse an existing `opportunityKey` and blueprint/version. Otherwise supply the supported topic, competitor or tracking-group scope; use `retrievalPrompt` to focus that scope, not with `blueprintId`/`blueprintVersion`. For manually selected video IDs, build a blueprint first. Do not ask the user for internal IDs that can be discovered. Respect the tool's actual access, funding and approval result.
3. **Carry the creative agreement.** Use the supported `brandContext` fields for concise approved audience needs, product/service facts with source references, voice/CTA, exclusions, length and asset constraints. Project documents are not automatically inputs to the engine: read the relevant material and pass the supported summary. Distinguish unknown facts from approved claims; do not promise automatic document retrieval or verification.
4. **Generate or update.** Prefer the named actions below. If only the compatibility dispatcher is exposed, use the exact `toolName`/`body` shape, not `function`. Read returned status: pending/draft is not success, and `missing_data` requires the stated evidence gap to be resolved or a labelled fallback. Use returned identities for subsequent reads; do not repeatedly generate while waiting or bypass an access/funding rejection.
5. **Review and hand off.** Check the actual result against the audience job, source-supported claims, title/hook/payoff, scripts, duration/slide count and asset availability. Keep limitations explicit. Export the saved version, then use document tools for the requested presentation. Record any local edits not saved back to the canonical brief.

| Job | Named action, when available | Compatibility target |
| --- | --- | --- |
| Generate a new brief | `socialseal_generate_brief` | `vnext-briefs-generate` |
| Read a saved version | `socialseal_get_brief` | `vnext-briefs-read` |
| Revise a saved brief | `socialseal_update_brief` | `vnext-briefs-update` |
| Export for handoff | `socialseal_export_brief` | `vnext-briefs-export` |

Example for an existing blueprint (inspect the live schema first):

```text
socialseal_call_tool {
  "toolName": "vnext-briefs-generate",
  "workspaceId": "<workspace-id>",
  "body": {
    "opportunityKey": "<opportunity-key>",
    "blueprintId": "<blueprint-id>",
    "brandContext": { "brandName": "<brand>", "platform": "tiktok", "notes": "<approved facts, audience job and production constraints>" }
  }
}
```

## Manual Path (fallback)

Use when the user explicitly wants manual writing, generation is unavailable, or evidence remains `missing_data`. State the specific reason and what evidence is available; do not silently present a locally authored document as an engine-generated brief. A missing material fact needs a targeted question or omission, not invented specificity. Routine edits to an approved brief need no new generation run. Even with a blueprint, hooks and hero shots drawn from exemplars are indicative creative bets to test, not proof; see `references/evidence-and-confidence.md`.

1. Restate the viewer job.
2. Choose the content lens (aspirational vs utility/practical). Do not frame as an ad.
3. Write 3 platform-native hooks tied to the search intent.
4. Define the hero shot.
5. Add shot priorities (must / should / optional).
6. Add concrete validators (location, object, screen, step, price range, timing, before/after).
7. Write caption direction that builds curiosity; hashtags last.
8. Add an evidence note: which keyword/topic or exemplar informed the brief.

## Output Format

- Brief title
- Platform / market / target keyword / `opportunityKey`
- Viewer job and content lens
- 3 hook options
- Hero shot and shot list with priorities (aligned to blueprint shot panels when available)
- Useful details / validators
- Brand utility/proof sources and unresolved confirmations
- Caption direction and CTA
- What to avoid
- Evidence references: cite exemplars by video title/URL and `@handle` and the `"keyword" [market, platform]`; keep `blueprintId`/`video_uid` as a traceability note
- Measurement note (tracking group / keyword)

Use `templates/creator-brief-template.md` for the manual path.

## Do / Don't

Do:
- prefer engine briefs grounded in a blueprint
- align shot direction to blueprint shot panels
- keep direction creator-led and social-native
- use language depth and mechanisms anchored in selected references, not generic
  "pause/stop scrolling" filler
- cite blueprint and exemplar evidence

Don't:
- say proof, prove, persuasion, reasons to buy, or ad script
- silently bypass available generation for a new brief; preserve an explicit manual choice or documented fallback
- include unsupported product or performance claims
- call the brief a finished video or carousel
- copy a competitor hook verbatim

## Troubleshooting

- `vnext-briefs-generate` returns `missing_data`: the underlying blueprint lacks evidence; fix scope in `socialseal-blueprint-builder` first.
- Brief feels like an ad: rewrite around a viewer question or practical-use moment.
- Shot list is abstract: pull concrete validators from blueprint shots and exemplar Video DNA.
- No engine access: use the manual path and label evidence gaps.

## Verification Checklist

- [ ] Brief is generated from a blueprint, or the manual fallback is justified.
- [ ] Hooks, hero shot, and shots trace to evidence/blueprint panels.
- [ ] Engine identities and versions are retained when returned; a manual fallback has no invented IDs.
- [ ] Audience/product constraints reached the actual script and shots, not only metadata.
- [ ] Generated status and successful rendering are not reported as factual or creative validation.
- [ ] Caption creates curiosity; no ad framing or unsupported claims.
- [ ] Measurement note maps to a tracking group/keyword.
