import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def selected_cursor_skills(manifest):
    # Cursor's documented default is skills/*/SKILL.md. Explicit paths replace it.
    # https://cursor.com/docs/reference/plugins#cursor-plugin-component-discovery
    paths = manifest.get("skills", "skills")
    if isinstance(paths, str):
        paths = [paths]
    selected = set()
    for path in paths:
        directory = (ROOT / path).resolve()
        if not directory.is_relative_to(ROOT):
            raise ValueError(f"skill path leaves plugin: {path}")
        entry = directory / "SKILL.md"
        if entry.is_file():
            selected.add(entry)
        else:
            selected.update(directory.glob("*/SKILL.md"))
    return selected


class HostPluginManifestTests(unittest.TestCase):
    def test_cursor_selects_all_22_canonical_skills(self):
        manifest = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
        canonical = {path.resolve() for path in ROOT.glob("skills/*/SKILL.md")}
        self.assertEqual(len(canonical), 22)
        self.assertEqual(selected_cursor_skills(manifest), canonical)

    def test_selected_skills_have_complete_local_resources(self):
        manifest = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
        documents = set(ROOT.glob("references/**/*.md"))
        documents.update(ROOT.glob("templates/**/*.md"))
        for entry in selected_cursor_skills(manifest):
            documents.update(entry.parent.rglob("*.md"))
        resource_paths = re.compile(
            r"(?:references|templates)/[A-Za-z0-9_./-]+\.(?:md|json|csv|py)"
        )
        for document in documents:
            for resource in resource_paths.findall(document.read_text()):
                with self.subTest(document=document.relative_to(ROOT), resource=resource):
                    # Shared root resources and bundled skill-local resources are supported.
                    candidates = [document.parent / resource, ROOT / resource]
                    self.assertTrue(any(path.is_file() for path in candidates))

    def test_host_manifest_assets_are_inside_package(self):
        manifest = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
        for field in ("logo", "mcpServers"):
            with self.subTest(field=field):
                path = (ROOT / manifest[field]).resolve()
                self.assertTrue(path.is_relative_to(ROOT))
                self.assertTrue(path.is_file())

    def test_hosted_mcp_uses_explicit_http_transport(self):
        # https://claude.com/docs/plugins/pre-submission-checklist
        manifest = json.loads((ROOT / ".mcp.json").read_text())
        server = manifest["mcpServers"]["socialseal"]
        self.assertEqual(server.get("type"), "http")
        self.assertEqual(server["url"], "https://mcp.socialseal.co/mcp")
        self.assertEqual(set(server), {"type", "url"})


if __name__ == "__main__":
    unittest.main()
