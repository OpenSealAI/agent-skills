---
name: socialseal-blueprint-builder
description: >-
  Use this skill when compiling a SocialSeal best-practices blueprint from grounded
  reference-video evidence: generating or reading a blueprint version, handling the
  missing_data outcome, inspecting best practices and shot-lift, and preparing the
  blueprint as the source of truth for briefs and Asset Studio rough cuts.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - blueprint
    - best-practices
    - shot-lift
    - asset-studio
---

# SocialSeal Blueprint Builder

## Overview

A SocialSeal blueprint is the compiled, evidence-grounded answer to "what makes content win for this opportunity." It is generated from real exemplar videos, not authored from intuition. It carries `best_practices[]`, `evidence[]`, the selected exemplars, and a set of shot panels that downstream briefs and Asset Studio rough cuts follow.

This skill drives `vnext-blueprints-*`. See `references/production-pipeline.md` for the end-to-end flow and `references/mcp-and-cli-usage.md` for call patterns. Use `socialseal-reference-video-analysis` first to select and analyze exemplars.

## When to Use

- Generating a blueprint version for an opportunity scope.
- Reading blueprint history/versions and the latest `best_practices`/`evidence`.
- Reading shot-lift rows and pinned shot assets (the panels used for clip mapping).
- Diagnosing and fixing a `missing_data` blueprint.

## Inputs

Required:
- workspace id and the opportunity `opportunityKey`
- a scope: `topic` + `pillarId`, `competitor` + `competitorBrandIds`, `tracking_group` + `trackingGroupId`, `list` + `listId` + `readinessRunId`, or `manual` + `videoUids`

Good to have:
- refinement: `pinnedVideoUids`, `excludedVideoUids`, `promotedCandidateTarget`, `retrievalPrompt` (not for manual/list)
- `platformIds`, `region`, `language`, `timePeriod`
- a `title` for the blueprint

## Workflow

1. **Confirm grounded exemplars.** Run the preview path in `socialseal-reference-video-analysis` until the promoted exemplar set is right.
2. **Generate the blueprint.** Call `vnext-blueprints-generate` (without `previewOnly`). The engine queues analysis for any promoted exemplar missing it and writes a version.
3. **Interpret status.**
   - `draft`: analysis pending. Poll until ready.
   - `generated`: ready to use.
   - `missing_data`: no qualifying evidence. The engine writes an explicit version with a reason (e.g. "no tracking group keywords found for this scope"). Do not invent practices. Fix the scope/keywords/time window and regenerate.
4. **Read the blueprint.** Use `vnext-blueprints-read` for the version's `best_practices`, `evidence`, and selected exemplars.
5. **Read shot-lift.** Use `vnext-blueprints-shots-read` to get shot panels and pinned shot assets (signed URLs). Each panel has a `panelId` used by clip mapping and the Asset Studio editSpec.
6. **Refresh shots if stale.** Use `vnext-blueprints-shots-refresh` to requeue shot assets.
7. **Hand off.** Pass `blueprintId` (+ version) to `socialseal-creator-briefing` and the panels to `socialseal-asset-studio-generation`.

## Tool Calls (MCP-first)

Generate (tracking-group scope):

```text
socialseal_call_tool {
  "function": "vnext-blueprints-generate",
  "workspaceId": "<workspace-id>",
  "body": {
    "workspaceId": "<workspace-id>",
    "opportunityKey": "<opportunity-key>",
    "scopeType": "tracking_group",
    "trackingGroupId": <group-id>,
    "timePeriod": "30d",
    "promotedCandidateTarget": 12,
    "title": "<blueprint-title>"
  }
}
```

Read the latest version and shot-lift:

```text
socialseal_call_tool { "function": "vnext-blueprints-read", "workspaceId": "<workspace-id>", "body": { "opportunityKey": "<opportunity-key>" } }
socialseal_call_tool { "function": "vnext-blueprints-shots-read", "workspaceId": "<workspace-id>", "body": { "blueprintId": "<blueprint-id>", "signedUrlSeconds": 3600 } }
```

CLI equivalents:

```bash
npx -y @socialseal/cli tools call --function vnext-blueprints-generate --workspace-id <workspace-id> --body @blueprint.json --pretty
npx -y @socialseal/cli tools call --function vnext-blueprints-read --workspace-id <workspace-id> --body '{"opportunityKey":"<opportunity-key>"}' --pretty
npx -y @socialseal/cli tools call --function vnext-blueprints-shots-read --workspace-id <workspace-id> --body '{"blueprintId":"<blueprint-id>"}' --pretty
```

## Output

- `blueprintId` and `version`, with `status`
- `best_practices[]` each tied to `evidence[]` (exemplar `video_uid`s)
- selected exemplars with scores and matched keywords
- shot panels (`panelId`, shot label, kind) and pinned shot assets
- a clear `missing_data` note and remediation when applicable

## Do / Don't

Do:
- ground every best practice in cited exemplar evidence
- reuse one `opportunityKey` across blueprint, brief, and asset
- treat `panelId`s as the contract for clip mapping and editSpec
- record the `blueprintId` and version for downstream skills

Don't:
- author best practices when the engine returns `missing_data`
- mix scopes in one blueprint to force a result
- edit shot panels by hand outside the engine
- expose literal workspace/blueprint IDs in shared artifacts

## Troubleshooting

- `missing_data`: widen keywords/scope, adjust `timePeriod`, or switch scope type; for competitor scope ensure `competitorBrandIds` resolve to active aliases.
- Stuck in `draft`: promoted exemplars are still analyzing; poll `vnext-blueprints-read` and `video_analysis` status.
- List scope errors (`READINESS_STALE`/`READINESS_BLOCKED`/`READINESS_WARNING_REQUIRES_OVERRIDE`): re-run list readiness; pass `allowWarningOverride` only when intentional.
- Empty shot-lift: run `vnext-blueprints-shots-refresh`, then re-read.

## Verification Checklist

- [ ] Blueprint reached `generated` (or `missing_data` was surfaced and addressed).
- [ ] Best practices are grounded in cited exemplar evidence.
- [ ] Shot panels and `panelId`s are recorded.
- [ ] `blueprintId`, version, and `opportunityKey` are handed to brief/asset skills.
