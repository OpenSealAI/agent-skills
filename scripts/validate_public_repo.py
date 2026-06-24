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
expected=18
found=len(list(root.glob('skills/*/SKILL.md')))
if found != expected:
    errors.append(f'expected {expected} skills, found {found}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('ok')
