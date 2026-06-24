---
name: socialseal-asset-studio-generation
description: >-
  Use this skill when assembling a SocialSeal Asset Studio rough cut from a workspace
  clip library that follows a blueprint's shots: uploading and finalizing clips,
  mapping clips to blueprint shot panels, creating a generated asset from an edit
  spec, optimizing revisions, and exporting FCPXML or a share link.
license: MIT
metadata:
  socialseal:
    phase: production
  tags:
    - socialseal
    - production
    - asset-studio
    - clips
    - rough-cut
    - fcpxml
---

# SocialSeal Asset Studio Generation

## Overview

Asset Studio assembles a rough cut by mapping workspace clip-library footage onto a blueprint's shot panels and rendering an edit spec. The blueprint defines the shots; clips fill them; the engine produces a generated asset you can optimize, export as FCPXML, and share.

This skill drives `vnext-clips-*`, `vnext-clip-shot-mappings-*`, and `vnext-generated-asset-*`. See `references/production-pipeline.md` for the pipeline and `references/mcp-and-cli-usage.md` for call patterns. Run `socialseal-blueprint-builder` first to get the `blueprintId` and shot panels.

## When to Use

- Building a rough cut for a generated blueprint.
- Uploading clips into the workspace clip library.
- Mapping clips to blueprint shot panels.
- Optimizing, revising, exporting (FCPXML), or sharing a generated asset.

## Inputs

Required:
- workspace id, the `blueprintId`, and its shot panels (`panelId`s) from `vnext-blueprints-shots-read`
- clips for the shots, with confirmed usage rights

Good to have:
- the brief and `opportunityKey` for titles and context
- target spec: aspect ratio (commonly 9:16, 1080x1920), fps, durations per shot

## Workflow

1. **Read shot panels.** From `vnext-blueprints-shots-read`, list the `panelId`s and what each shot needs.
2. **Inventory the clip library.** `vnext-clips-read` to see existing clips and sign source URLs.
3. **Upload missing clips.** `vnext-clips-create` `action: "create"` returns a signed upload target; upload bytes to storage; then `action: "finalize"` with `clipId`, `fileName`, `storagePath`, `mimeType`, `sizeBytes`, and `rightsAttested: true`. Only finalize footage the workspace has rights to.
4. **Map clips to panels.** `vnext-clip-shot-mappings-write` `action: "upsert"` for each `panelId` + `clipId` (`source: "override"` for manual picks). Use `vnext-clip-shot-mappings-read` to confirm coverage; `action: "delete"` to clear a panel.
5. **Create the rough cut.** `vnext-generated-asset-create` with `blueprintId`, `title`, and an `editSpec` (`version`, `fps`, `width`, `height`, `totalDurationSeconds`, and `shots[]`). Each shot maps a `panelId` to a `clipId` with `sourceStartSeconds`, `durationSeconds`, `kind`, `shotLabel`, and `evidenceIds[]`.
6. **Review and optimize.** `vnext-generated-assets-read` (`detail`) to inspect; `vnext-generated-asset-optimize` to optimize or `create-revision`.
7. **Export and share.** `vnext-generated-asset-export` for FCPXML to finish in an editor; `vnext-generated-asset-share` to create a review link.

## Tool Calls (MCP-first)

Map a clip to a shot panel:

```text
socialseal_call_tool {
  "function": "vnext-clip-shot-mappings-write",
  "workspaceId": "<workspace-id>",
  "body": { "action": "upsert", "blueprintId": "<blueprint-id>", "panelId": "panel-1", "clipId": "<clip-id>", "source": "override" }
}
```

Create the rough cut from an edit spec:

```text
socialseal_call_tool {
  "function": "vnext-generated-asset-create",
  "workspaceId": "<workspace-id>",
  "body": {
    "blueprintId": "<blueprint-id>",
    "title": "<rough-cut-title>",
    "editSpec": {
      "version": 1, "fps": 30, "width": 1080, "height": 1920, "totalDurationSeconds": 18,
      "shots": [
        { "panelId": "panel-1", "clipId": "<clip-id>", "title": "Opening hook", "kind": "hook", "shotLabel": "Hero exterior", "sourceStartSeconds": 0, "durationSeconds": 3, "evidenceIds": [] }
      ]
    }
  }
}
```

Export FCPXML:

```text
socialseal_call_tool { "function": "vnext-generated-asset-export", "workspaceId": "<workspace-id>", "body": { "assetId": "<asset-id>", "format": "fcpxml" } }
```

CLI equivalents:

```bash
npx -y @socialseal/cli tools call --function vnext-clips-read --workspace-id <workspace-id> --body '{}' --pretty
npx -y @socialseal/cli tools call --function vnext-clips-create --workspace-id <workspace-id> --body '{"action":"create","fileName":"hero-shot.mp4","mimeType":"video/mp4"}' --pretty
npx -y @socialseal/cli tools call --function vnext-generated-asset-create --workspace-id <workspace-id> --body @edit-spec.json --pretty
npx -y @socialseal/cli tools call --function vnext-generated-asset-export --workspace-id <workspace-id> --body '{"assetId":"<asset-id>","format":"fcpxml"}' --pretty
```

## Output

- finalized clips in the library (with `clipId`s)
- clip-to-panel mappings covering the blueprint shots
- a generated asset (`assetId`) with status
- an FCPXML export and/or a share link

## Do / Don't

Do:
- cover every required shot panel before generating
- keep `panelId`s consistent across mappings and the editSpec
- attest rights (`rightsAttested: true`) on every finalized clip
- export FCPXML for finishing rather than treating the rough cut as final

Don't:
- finalize or assemble footage the workspace lacks rights to
- invent `panelId`s that are not in the blueprint
- skip the blueprint and assemble arbitrary clips
- put share tokens or literal asset/clip IDs in public artifacts

## Troubleshooting

- Finalize rejected: confirm `storagePath`, `sizeBytes`, `mimeType`, and `rightsAttested: true`; upload bytes before finalize.
- A panel has no clip: upload or map a clip, or hand it to `socialseal-asset-planning` (capture) or `socialseal-generation-prompts` (generate a reference clip).
- Asset create fails: validate the editSpec shape (fps/width/height/totalDurationSeconds and each shot's `panelId`/`clipId`/durations).
- Share link issues: `read` is unscoped via `shareToken`; `create`/`revoke` require `workspaceId`.

## Verification Checklist

- [ ] Blueprint shot panels are covered by mapped clips.
- [ ] All finalized clips have `rightsAttested: true`.
- [ ] The editSpec uses real `panelId`/`clipId` values and valid dimensions.
- [ ] A generated asset exists and was reviewed/optimized.
- [ ] FCPXML export or share link produced as needed.
