---
name: socialseal-orchestrator
description: >-
  Use this skill when the user requests a multi-stage content plan or production programme combining research, videos, carousels, and editor handoff. Coordinate only the requested creative deliverables.

license: MIT
metadata:
  socialseal:
    phase: orchestration
  tags:
    - socialseal
    - orchestration
    - routing
    - workflow
    - getting-started
---

# SocialSeal Multi-stage Production

Use this guidance for an explicitly requested production programme. Routine group reads, named-account metrics, supplied-video analysis, exports, and compound analytical requests work through the host's direct tools without this skill.

Agree the requested delivery state: plan, brief, draft, externally edited rough cut, editor-ready, or post-ready export. Read `references/creative-production-gates.md` for the stages that apply to those deliverables. Reuse approved inputs and decisions.

- Retrieve available brand facts and evidence. Use strategy-readiness only when missing foundations affect the creative work; missing strategy does not prevent reading existing evidence.
- For demand research, preserve the requested markets, languages, platforms, and sample. Use opportunity or competitor analysis guidance only when that analysis is requested or needed for the production.
- For creative production, use the relevant concept, reference-video, blueprint, brief, asset, or carousel skill when its guidance improves the deliverable. Load only the current task's instructions.
- Keep one `opportunityKey` across blueprint, brief, and handoff. SocialSeal does not assemble generated videos or export FCPXML; deliver source clips and briefs to the user's editor.
- Apply demand, benchmark, asset, prototype, and final-QA gates only to the creative artifacts they protect. Present material creative choices, not routine execution questions.
- New collection and external effects retain the operation's quote, approval, budget, and idempotency requirements. Reuse authorization already given for the same scope.
- Cite source URLs and scoped evidence; distinguish observations, sampled statistics, and creative inference. Do not substitute unverified location imagery without the user's choice and a caveat.

For access, actual schemas, artifact reading, and polling, read `references/mcp-and-cli-usage.md`. The host discovers and composes tools directly; a semantic resolver or prescribed workflow is never a prerequisite. Keep a compact artifact/decision manifest only for a large production task.
