from pathlib import Path
import json, re, sys, yaml
root = Path(__file__).resolve().parents[1]
blocked = [
    r"@socialseal\.co",
    r"https://docs\.google\.com/",
    r"https://drive\.google\.com/",
    r"/\.hermes/",
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
]
errors=[]

codex_manifest_path = root / ".codex-plugin" / "plugin.json"
mcp_manifest_path = root / ".mcp.json"
discovery_prompts_path = root / "tests" / "plugin-discovery-prompts.json"

for required_path in (codex_manifest_path, mcp_manifest_path, discovery_prompts_path):
    if not required_path.is_file():
        errors.append(f"missing required plugin file: {required_path.relative_to(root)}")

if codex_manifest_path.is_file() and mcp_manifest_path.is_file() and discovery_prompts_path.is_file():
    codex_manifest = json.loads(codex_manifest_path.read_text())
    mcp_manifest = json.loads(mcp_manifest_path.read_text())
    discovery_prompts = json.loads(discovery_prompts_path.read_text())
    searchable_parts = [
        codex_manifest.get("name", ""),
        codex_manifest.get("description", ""),
        *codex_manifest.get("keywords", []),
        codex_manifest.get("interface", {}).get("displayName", ""),
        codex_manifest.get("interface", {}).get("shortDescription", ""),
        codex_manifest.get("interface", {}).get("longDescription", ""),
        *codex_manifest.get("interface", {}).get("defaultPrompt", []),
    ]
    searchable_copy = "\n".join(str(part) for part in searchable_parts).casefold()
    for phrase in discovery_prompts.get("positive", []):
        if str(phrase).casefold() not in searchable_copy:
            errors.append(f".codex-plugin/plugin.json: missing discovery phrase {phrase!r}")
    socialseal_mcp = mcp_manifest.get("mcpServers", {}).get("socialseal", {})
    if socialseal_mcp.get("url") != "https://mcp.socialseal.co/mcp":
        errors.append(".mcp.json: SocialSeal MCP URL is missing or incorrect")
    if codex_manifest.get("mcpServers") != "./.mcp.json":
        errors.append(".codex-plugin/plugin.json: mcpServers must reference ./.mcp.json")

trigger_expectations = {
    "socialseal-orchestrator": ["multi-stage", "production"],
    "socialseal-strategy-readiness": ["content plan", "product truths", "exclusions"],
    "socialseal-workspace-setup": ["there is no tracking group", "baseline/search journey"],
    "socialseal-tracking-group-design": ["what keywords or queries to track", "no group"],
    "socialseal-opportunity-analysis": ["what are people searching for", "content gaps"],
    "socialseal-competitor-content-analysis": ["what good social content looks like", "benchmarks"],
    "socialseal-social-plan-builder": ["content plan", "videos and carousels"],
    "socialseal-video-concepting": ["video ideas", "hooks", "first frames"],
    "socialseal-reference-video-analysis": ["real social examples", "benchmark videos", "video dna"],
    "socialseal-blueprint-builder": ["creative best practices", "socialseal blueprint"],
    "socialseal-creator-briefing": ["create, rewrite, or improve", "social-first language"],
    "socialseal-asset-planning": ["footage/image bank", "which assets to use"],
    "socialseal-generation-prompts": ["generated b-roll", "storyboard frames"],
    "socialseal-carousel-production": ["create, design, redesign, or finish", "avoid generic ai design"],
    "socialseal-creator-discovery": ["ranked search evidence"],
    "socialseal-creator-evaluation": ["supplied creator", "brand partnership"],
    "socialseal-bilingual-demand-monitoring": ["local language versus", "multilingual demand"],
    "socialseal-predictive-demand-routing": ["what is trending", "demand is shifting"],
    "socialseal-discoverability-tracking": ["whether a brand or competitor appears", "share of voice"],
    "socialseal-performance-readout": ["how posted content", "performed in socialseal"],
    "socialseal-content-adjustment-recommendations": ["what to change next", "not surfacing"],
    "socialseal-management-reporting": ["executive", "senior-stakeholder summary"],
    "socialseal-follow-up-planning": ["turn a socialseal meeting", "owners/due dates"],
}
for p in root.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.yaml','.yml','.csv','.txt'}:
        txt=p.read_text(errors='ignore')
        rel=str(p.relative_to(root))
        for pat in blocked:
            if re.search(pat, txt, flags=re.I):
                errors.append(f'{rel}: blocked pattern {pat}')
for p in root.glob('skills/*/SKILL.md'):
    txt=p.read_text()
    if not txt.startswith('---'):
        errors.append(f'{p}: missing frontmatter'); continue
    m=re.search(r'\n---\s*\n', txt[3:])
    if not m:
        errors.append(f'{p}: missing closing frontmatter'); continue
    fm=yaml.safe_load(txt[3:m.start()+3]) or {}
    name=fm.get('name')
    if name != p.parent.name:
        errors.append(f'{p}: name must match parent directory')
    if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name or ''):
        errors.append(f'{p}: invalid skill name')
    desc=fm.get('description','')
    if not desc or len(desc)>1024:
        errors.append(f'{p}: missing/long description')
    if not str(desc).startswith('Use this skill when'):
        errors.append(f'{p}: description should start with Use this skill when')
    desc_lower = str(desc).lower()
    for phrase in trigger_expectations.get(name, []):
        if phrase not in desc_lower:
            errors.append(f'{p}: missing trigger phrase {phrase!r}')
# SOC-349 removed persisted shot mappings and the generated-video editSpec.
# Guard the concrete stale instructions; external editor work remains supported.
retired_instruction_patterns = {
    "skills/socialseal-blueprint-builder/SKILL.md": [r"\beditSpec\b", r"panels used for clip mapping", r"blueprint, brief, and asset"],
    "skills/socialseal-generation-prompts/SKILL.md": [r"upload/map", r"upload and mapping"],
    "references/mcp-and-cli-usage.md": [r"Video and asset studio"],
    "skills/socialseal-orchestrator/SKILL.md": [r"blueprint, brief, and asset"],
}
for relative_path, patterns in retired_instruction_patterns.items():
    content = (root / relative_path).read_text()
    for pattern in patterns:
        if re.search(pattern, content, re.I):
            errors.append(f"{relative_path}: retired workflow instruction {pattern!r}")

# Single-skill installs must receive the same contracts as the full plugin.
for resource_type in ("references", "templates"):
    for bundled in root.glob(f"skills/*/{resource_type}/**/*"):
        if not bundled.is_file():
            continue
        relative = bundled.relative_to(root / "skills")
        canonical = root / resource_type / Path(*relative.parts[2:])
        if not canonical.is_file() or bundled.read_bytes() != canonical.read_bytes():
            errors.append(f"{bundled.relative_to(root)}: differs from canonical {resource_type} resource")

expected=23
found=len(list(root.glob('skills/*/SKILL.md')))
if found != expected:
    errors.append(f'expected {expected} skills, found {found}')
if set(trigger_expectations) != {p.parent.name for p in root.glob('skills/*/SKILL.md')}:
    errors.append('trigger expectation map must cover every skill exactly once')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('ok')
