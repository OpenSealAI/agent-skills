---
name: socialseal-creator-briefing
description: >-
  Use this skill when producing creator, influencer, or UGC briefs from SocialSeal
  evidence. Prefer generating the brief from a best-practices blueprint with the
  vNext briefs engine; fall back to structured manual authoring (hooks, hero shot,
  shot priorities, caption rules, evidence) when no engine access or the blueprint
  is missing_data.
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

A SocialSeal creator brief turns grounded evidence into creator-ready direction. The strongest brief is generated from a best-practices blueprint so it carries the blueprint's evidence and shot structure. Manual authoring is the fallback when there is no SocialSeal access or the blueprint returned `missing_data`.

See `references/production-pipeline.md` for the pipeline, `references/mcp-and-cli-usage.md` for call patterns, and `references/content-lenses.md` for lenses. Run `socialseal-blueprint-builder` first when possible.

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
- creator type/persona, required assets/locations, compliance constraints
- deliverable count, length, aspect ratio, deadline

## Engine Path (preferred)

1. **Generate the brief.** Call `vnext-briefs-generate` from the blueprint:

```text
socialseal_call_tool {
  "function": "vnext-briefs-generate",
  "workspaceId": "<workspace-id>",
  "body": { "opportunityKey": "<opportunity-key>", "blueprintId": "<blueprint-id>", "brandContext": { "brandName": "<brand>", "platform": "tiktok" } }
}
```

   You can instead pass a scope (`scopeType` + scope fields) or a `retrievalPrompt` (not combinable with `blueprintId`/`blueprintVersion`) and the engine resolves the blueprint.
2. **Read and export.** `vnext-briefs-read` for versions; `vnext-briefs-export` for markdown:

```text
socialseal_call_tool { "function": "vnext-briefs-export", "workspaceId": "<workspace-id>", "body": { "opportunityKey": "<opportunity-key>" } }
```

3. **Review against the blueprint.** Confirm hooks, hero shot, and shot priorities trace to blueprint best practices and exemplar evidence. Tighten brand context; never add unsupported claims.
4. **Creative pack (optional).** Use `creative-pack-generate` / `creative-pack-export` when more than one brief is needed.

CLI equivalents:

```bash
npx -y @socialseal/cli tools call --function vnext-briefs-generate --workspace-id <workspace-id> --body @brief.json --pretty
npx -y @socialseal/cli tools call --function vnext-briefs-export --workspace-id <workspace-id> --body '{"opportunityKey":"<opportunity-key>"}' --pretty
```

## Manual Path (fallback)

Use only when there is no SocialSeal access or the blueprint is `missing_data`. Label it as a hypothesis and request more evidence. Even with a blueprint, hooks and hero shots drawn from exemplars are indicative creative bets to test, not proof; see `references/evidence-and-confidence.md`.

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
- cite blueprint and exemplar evidence

Don't:
- say proof, prove, persuasion, reasons to buy, or ad script
- hand-author when a generated blueprint is available
- include unsupported product or performance claims
- copy a competitor hook verbatim

## Troubleshooting

- `vnext-briefs-generate` returns `missing_data`: the underlying blueprint lacks evidence; fix scope in `socialseal-blueprint-builder` first.
- Brief feels like an ad: rewrite around a viewer question or practical-use moment.
- Shot list is abstract: pull concrete validators from blueprint shots and exemplar Video DNA.
- No engine access: use the manual path and label evidence gaps.

## Verification Checklist

- [ ] Brief is generated from a blueprint, or the manual fallback is justified.
- [ ] Hooks, hero shot, and shots trace to evidence/blueprint panels.
- [ ] `opportunityKey` and `blueprintId` are recorded.
- [ ] Caption creates curiosity; no ad framing or unsupported claims.
- [ ] Measurement note maps to a tracking group/keyword.
