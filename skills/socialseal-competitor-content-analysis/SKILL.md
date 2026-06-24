---
name: socialseal-competitor-content-analysis
description: Use this skill when extracting competitor, creator, and category content
  patterns from SocialSeal search results or tracked-video extracts. Produces reusable
  video/content DNA for strategy, briefs, and concepting without copying posts.
license: MIT
metadata:
  socialseal:
    phase: strategy
  tags:
  - socialseal
  - strategy
  - competitor-analysis
  - video-dna
  - content-patterns
---

# SocialSeal Competitor Content Analysis

## Overview

SocialSeal can show which competitor, creator, or category videos surface for tracked searches. This skill turns those surfaced examples into reusable content DNA: hooks, first frames, shots, useful details, formats, and viewer jobs.

The deliverable is not “competitor posts are doing well.” The deliverable is a pattern library the brand can adapt.

When the goal is to produce content (not just analysis), route into the production engine instead of stopping at a pattern matrix: use `socialseal-reference-video-analysis` to select and analyze exemplars and `socialseal-blueprint-builder` to compile a grounded blueprint. This skill is for the strategy-side pattern read; the engine turns those patterns into briefs and rough cuts. See `references/production-pipeline.md`.

## Inputs

- enriched search-result export or group evidence export
- target competitor/entity list or category scope
- keywords/topics to inspect
- optional tracked video IDs, search result IDs, or source URLs

## Data Access

Export ranked rows:

```bash
npx -y @socialseal/cli data export-search-results \
  --group-ids <group-id> \
  --workspace-id <workspace-id> \
  --out ./exports/search-results.csv
```

Extract individual video analysis/assets when row identifiers are available:

```bash
npx -y @socialseal/cli video extract \
  --search-result-id <search-result-id> \
  --workspace-id <workspace-id> \
  --ensure-analysis \
  --wait \
  --out-dir ./video-assets/<search-result-id>
```

Alternative identifiers include `--video-id`, `--video-uid`, or `--platform-video-id`. Use the CLI help to choose the correct one.

MCP equivalent: `socialseal_call_tool` with `function: "tracked-video-extract"` and a body of `{ "ensureAnalysis": true, "includeAssets": true, "items": [{ "videoUid": "<video-uid>" }] }`. Attribution: cite every example by video title/URL, `@author_handle`, and `"keyword" [market, platform]`; keep `video_uid`/`search_result_id` as an internal traceability note only, and avoid platform-age claims when `published_at` is blank (see `references/socialseal-data-contract.md` and `references/mcp-and-cli-usage.md`).

Evidence note: surfaced exemplars are anecdotal evidence for creative direction, not proof a pattern will perform. A pattern needs multiple exemplars or an explicit reason; frame adaptations as hypotheses to test. See `references/evidence-and-confidence.md`.

## Workflow

1. **Sample deliberately.** Select examples from top keywords, repeated competitors/creators, and high-opportunity gaps. Avoid only picking viral outliers.
2. **Qualify scope.** Remove irrelevant rows, wrong market/language, wrong topic, or non-comparable account types.
3. **Extract video DNA.** For each example, capture hook, first frame, hero shot, shot sequence, on-screen text, useful details, mood cues, caption style, CTA, and creator/account type.
4. **Classify format.** Use labels such as walkthrough, comparison, first-timer guide, map/pin, list, day-in-life, itinerary, review, before-after, FAQ, or myth-vs-reality.
5. **Separate lenses.** Aspirational patterns create mood/desire. Utility patterns teach, plan, compare, or reduce hesitation.
6. **Find repeated mechanisms.** A pattern needs multiple examples or a clear reason it matters for a priority keyword.
7. **Translate into adaptation.** State how the brand should adapt the mechanism, not copy the post.

## Output

Create a content-pattern matrix:

- keyword/topic (as `"keyword" [market, platform]`)
- example (video title/URL, `@handle`)
- account/entity type
- format
- hook/first-frame pattern
- shot/structure pattern
- useful detail or mood cue
- why it surfaces
- how the brand can adapt it
- caveat

Then write a short “briefing implications” section for downstream creator briefs or concepts.

## Do / Don't

Do:

- inspect visuals/captions where possible before making format claims
- identify account type: owned, creator, media, affiliate/partner, competitor
- adapt the mechanism, not the wording
- cite examples by title/URL and `@handle`; keep `video_uid` as a traceability note

Don't:

- copy hooks verbatim unless the user explicitly asks for close variants
- infer a pattern from one example, or present an exemplar as proof it will work
- confuse account size with format quality
- use ad-style labels; describe social-native content jobs

## Troubleshooting

- If `video extract` cannot resolve an ID, try the other supported identifiers from CLI help.
- If analysis is missing, use `--ensure-analysis --wait`.
- If assets are unavailable, use titles/captions/metadata and label the evidence as metadata-only.
- If examples are off-topic, resample from stricter keyword or market filters.

## Verification Checklist

- [ ] Examples are relevant to the stated keyword/topic scope.
- [ ] Patterns are based on multiple examples or clearly justified single examples.
- [ ] Visual/caption evidence status is labeled.
- [ ] Recommendations are adaptations, not copies.
- [ ] Output can feed creator briefing or video concepting directly.

