from pathlib import Path
import re, sys, yaml
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
trigger_expectations = {
    "socialseal-orchestrator": ["content plan", "videos", "carousels", "search demand"],
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
    "socialseal-asset-studio-generation": ["make, assemble, or edit", "rough cut"],
    "socialseal-capcut-export-prep": ["finish, polish, caption, export", "post-ready"],
    "socialseal-carousel-production": ["create, design, redesign, or finish", "avoid generic ai design"],
    "socialseal-creator-discovery": ["which creators", "ugc partners"],
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
expected=24
found=len(list(root.glob('skills/*/SKILL.md')))
if found != expected:
    errors.append(f'expected {expected} skills, found {found}')
if set(trigger_expectations) != {p.parent.name for p in root.glob('skills/*/SKILL.md')}:
    errors.append('trigger expectation map must cover every skill exactly once')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('ok')
