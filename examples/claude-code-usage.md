# Claude Code Usage

This repo is also a Claude Code plugin. The `.claude-plugin/` manifest lives at the repo root, so point `--plugin-dir` at the repo root. Test locally with:

```bash
claude --plugin-dir .
```

Skills will be namespaced under the plugin name, for example:

```text
/socialseal-agent-skills:socialseal-creator-briefing
```

Run `claude plugin validate` before marketplace submission.
