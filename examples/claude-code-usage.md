# Claude Code Usage

This repo is also a Claude Code plugin. The `.claude-plugin/` manifest lives at the repo root, so point `--plugin-dir` at the repo root. Test locally with:

```bash
claude --plugin-dir .
```

Skills will be namespaced under the plugin name, for example:

```text
/socialseal-agent-skills:socialseal-creator-briefing
```

For a large content request, start with the orchestrator so Claude checks brand
utility, demand evidence, benchmarks, asset choices, prototypes, and delivery state
before producing files:

```text
/socialseal-agent-skills:socialseal-orchestrator
Create a search-grounded content plan and production package with videos and
carousels from our existing asset bank.
```

Invoke a downstream skill directly only when its prerequisites already exist, for
example `/socialseal-agent-skills:socialseal-carousel-production` after the topic,
benchmarks, utility facts, visual direction, and assets are approved.

Run `claude plugin validate` before marketplace submission.
