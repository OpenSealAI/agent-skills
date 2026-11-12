---
name: socialseal-creator-briefing
description: >-
  Use this skill when the user asks to create, rewrite, or improve a short-form video,
  creator, influencer, UGC or video-editor brief, including hooks, social-first language, shots,
  captions, and CTAs. Route the request to the SocialSeal brief engine (free quote,
  then run) from a Study of real exemplars; write a hand-written brief only when the
  engine can't run, and say why at the top of the answer.
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

A SocialSeal creator brief turns grounded evidence into creator-ready direction. Use the generation tools to retain Study evidence and version identity, then review the result. Tool use is not a guarantee of factual support, useful audience advice or better creative quality. Loading this skill does not itself generate a brief. A request for a Word document, editor framework or usual brief template is a delivery-format request: run the engine, then format its export.

See `references/production-pipeline.md` for the pipeline, `references/mcp-and-cli-usage.md` for call patterns, and `references/content-lenses.md` for lenses. Every brief is generated from a Study revision. Use `socialseal-reference-video-analysis` when the Study subject needs choosing or its Video DNA needs approving; an existing usable Study can go directly to brief generation.

Read `references/creative-production-gates.md` when the brief will feed immediate
production. Confirm the chosen concept, brand utility facts, benchmark direction,
and non-negotiable exclusions before generating.

## When to Use

- Generating a brief from a Study revision (`studyContext`).
- Offering Study subjects when the brief tool returns `study_needed`, then retrying.
- Exporting a generated brief as markdown.
- Authoring a structured brief by hand under the declared fallback (see Manual Path).

## Inputs

Required:
- platform and market
- target keyword/topic or content job, and the `opportunityKey`
- a Study revision (`studyContext`) when using the engine, or exemplar evidence when authoring

Good to have:
- brand context (brandName, productName, campaignGoal, notes, locale, platform)
- approved brand utility/proof and facts needing confirmation
- creator type/persona, required assets/locations, compliance constraints
- deliverable count, length, aspect ratio, deadline

## Tool discovery and generation

1. **Resolve the requested work and workspace.** For an existing brief, read it and preserve its identity; do not regenerate for a caption tweak, formatting request or ordinary edit. For new briefs, load `socialseal_generate_brief` through host tool search and inspect its live schema. If discovery confirms it is unavailable, report the missing operation and preserve completed work. Do not infer missing capability from one failed lookup.
2. **Choose a Study.** Reuse an existing `opportunityKey` and pass the Study revision as `studyContext` (`briefContext` from `socialseal_get_study`). For the next brief in a series, use `socialseal_start_brief_run` with `continuesBriefId` and a new `continuationId`. Without a usable Study, call the brief tool with the topic, competitor or creator the brief is about: it starts and charges nothing, and returns `study_needed`. Then:
   - offer a fitting `reuse` Study first, since reusing it is free;
   - otherwise offer the ranked `candidates` (a topic, competitor, creator or specific videos) with each `reason`, `preview` and `estimatedPrice`, and let the user choose;
   - start only the chosen subject with its `startStudyArguments` through `socialseal_start_study`; on `approval_required`, show the price and resend with `maxCostUsd` or `approvedCredits` and an `idempotencyKey` only after the user approves it;
   - on `price_changed`, follow the recovery in `references/production-pipeline.md` (a wallet response needs a fresh quote and a new key);
   - poll `socialseal_get_study` while it is `enriching`; when the completed Study returns `briefContext`, retry the brief with it, and when it has none, explain the evidence gap (no briefable finding) instead of briefing.
   For manually selected videos, study them as `{ "kind": "videos", "urls": [...] }` (or `videoUids`). Do not ask the user for internal IDs that can be discovered. Respect the tool's actual access, funding and approval result.
3. **Carry the creative agreement.** Use the supported `brandContext` fields for concise approved audience needs, product/service facts with source references, voice/CTA, exclusions, length and asset constraints. Project documents are not automatically inputs to the engine: read the relevant material and pass the supported summary. Distinguish unknown facts from approved claims; do not promise automatic document retrieval or verification.
4. **Quote, then run.** Generate one `idempotencyKey` per brief. Check the workspace balance (`socialseal_get_workspace_balance`) and scope the brief count to the credits available. Call `socialseal_generate_brief` (or `socialseal_start_brief_run`) with `studyContext` and `quoteOnly: true` for the free quote, then resend it with the same key and without `quoteOnly` to run it; omit `maxCostUsd` on brief calls. On `upgrade_required`, nothing ran: relay the message and `upgradeUrl`, offer the briefs that fit the current credits, and resend with the same key after an upgrade. Poll `socialseal_get_brief_run` with the returned `runId` (or `jobId`), and retry a failed run with `socialseal_retry_brief_run`.
5. **Generate or update.** Use the named actions below with their typed arguments. If a required action is unavailable after host discovery, take the Manual Path with that reason; preserve actual pending, funding and missing-data states. Read returned status: pending/draft is not success, `study_needed` means no brief was made, and `missing_data` requires the stated evidence gap to be resolved or a labelled fallback. Use returned identities for subsequent reads; do not repeatedly generate while waiting or bypass an access/funding rejection.
6. **Review and hand off.** Check the actual result against the audience job, source-supported claims, title/hook/payoff, scripts, duration/slide count and asset availability. Keep limitations explicit. Export the saved version, then use document tools for the requested presentation. Record any local edits not saved back to the canonical brief.

| Job | Named action |
| --- | --- |
| Start or reuse the Study a brief needs | `socialseal_start_study` |
| Read the Study and its `briefContext` | `socialseal_get_study` |
| Quote, then generate a new brief | `socialseal_generate_brief` (`quoteOnly: true`, then run) |
| Start a polled run, or the next brief in a series | `socialseal_start_brief_run` (`quoteOnly: true`, then run), then `socialseal_get_brief_run` |
| Retry a failed run | `socialseal_retry_brief_run` |
| Read a saved version | `socialseal_get_brief` |
| Revise a saved brief | `socialseal_update_brief` |
| Export for handoff | `socialseal_export_brief` |

Example for an existing Study revision (inspect the live schema first):

```text
socialseal_generate_brief {
  "workspaceId": "<workspace-id>",
  "opportunityKey": "<opportunity-key>",
  "studyContext": { "studyRef": "<study-ref>", "revision": 2, "findingId": "action" },
  "idempotencyKey": "<stable-request-key>",
  "quoteOnly": true,
  "brandContext": {
    "brandName": "<brand>",
    "platform": "tiktok",
    "notes": "<approved facts, audience job and production constraints>"
  }
}
```

Resend with the same `idempotencyKey` and no `quoteOnly` to run it.

## Manual Path (declared fallback)

Use when the engine can't run: the brief tools are unavailable after host discovery, the quote or run fails again after one retry with the same key, credits stay short and the user declines an upgrade, the Study has no `briefContext` or returns `missing_data`, or the user asks for a hand-written brief. Open the answer with one line naming the reason, for example "Hand-written brief: the brief engine's quote failed twice", then state what evidence is available. Label the document hand-written, leave out engine identities and versions, and offer to regenerate it through the engine once the blocker clears. A missing material fact needs a targeted question or omission, not invented specificity. Routine edits to an approved brief need no new generation run. Even with a Study, hooks and hero shots drawn from exemplars are indicative creative bets to test, not proof; see `references/evidence-and-confidence.md`.

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
- Hero shot and shot list with priorities (aligned to the Study's observed shots and beats when available)
- Useful details / validators
- Brand utility/proof sources and unresolved confirmations
- Caption direction and CTA
- What to avoid
- Evidence references: cite exemplars by video title/URL and `@handle` and the `"keyword" [market, platform]`; keep the `studyRef`/revision and `video_uid` as a traceability note
- Measurement note (tracking group / keyword)

Use `templates/creator-brief-template.md` for the manual path.

## Do / Don't

Do:
- prefer engine briefs grounded in a Study
- align shot direction to the Study's observed shots and beats
- keep direction creator-led and social-native
- use language depth and mechanisms anchored in selected references, not generic
  "pause/stop scrolling" filler
- cite Study and exemplar evidence

Don't:
- say proof, prove, persuasion, reasons to buy, or ad script
- write a new brief by hand while the engine can run; a hand-written brief carries its declared reason
- include unsupported product or performance claims
- start paid Video DNA for a Study before the user approves its price
- call the brief a finished video or carousel
- copy a competitor hook verbatim

## Troubleshooting

- `socialseal_generate_brief` returns `study_needed`: no usable Study fits; offer the returned reuse Study or candidates, start the one the user chooses, then retry.
- `socialseal_generate_brief` returns `missing_data`: the Study revision lacks evidence (for example fewer than three observed beats); study more videos or a broader subject first.
- Brief feels like an ad: rewrite around a viewer question or practical-use moment.
- Shot list is abstract: pull concrete validators from the Study's per-video shots, beats and Video DNA.
- Quote or run fails: retry once with the same `idempotencyKey`; if it fails again, take the manual path, name the failure at the top of the answer and label evidence gaps.
- `upgrade_required`: relay the returned message and `upgradeUrl`; resend with the same key after the upgrade.

## Verification Checklist

- [ ] Brief is generated from a Study revision after a quote, or the answer opens with the reason for the manual fallback.
- [ ] Any paid Video DNA ran only after the user approved its price.
- [ ] Hooks, hero shot, and shots trace to Study evidence.
- [ ] Engine identities and versions are retained when returned; a manual fallback has no invented IDs.
- [ ] Audience/product constraints reached the actual script and shots, not only metadata.
- [ ] Generated status and successful rendering are not reported as factual or creative validation.
- [ ] Caption creates curiosity; no ad framing or unsupported claims.
- [ ] Measurement note maps to a tracking group/keyword.
