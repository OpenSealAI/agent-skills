import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from retired_mcp_guidance import retired_guidance


class RetiredGuidanceTests(unittest.TestCase):
    def test_rejects_dispatcher_instructions_without_retired_tool_names(self):
        for instruction in (
            "If only the compatibility dispatcher is exposed, use its arguments.",
            "Use the exact `toolName`/`body` shape, not `function`.",
            "Prefer the named action; vnext is a compatibility target.",
            "Use `tools schema --function group-management` before creating items.",
            "Call npx -y @socialseal/cli workspace list.",
            'Re-run with `executionMode: "async"` and poll.',
        ):
            with self.subTest(instruction=instruction):
                self.assertTrue(retired_guidance(instruction))

    def test_rejects_each_retired_public_wrapper(self):
        for suffix in ("list_available_tools", "get_tool_schema", "call_tool"):
            self.assertTrue(retired_guidance(f"Call socialseal_{suffix}."))

    def test_rejects_removed_blueprint_and_single_video_tools(self):
        for suffix in (
            "generate_blueprint",
            "get_blueprint",
            "save_blueprint",
            "get_blueprint_shots",
            "refresh_blueprint_shots",
            "save_brief",
            "analyse_public_video",
            "get_video_evidence",
        ):
            with self.subTest(tool=suffix):
                self.assertTrue(retired_guidance(f"Call socialseal_{suffix}."))

    def test_rejects_blueprint_inputs_and_retired_blueprint_skill(self):
        for instruction in (
            'Pass "blueprintId": "<blueprint-id>" to the brief tool.',
            "Pin `blueprintVersion` when regenerating.",
            "Map each clip to its `panelId`.",
            "Use socialseal-blueprint-builder to compile best practices.",
        ):
            with self.subTest(instruction=instruction):
                self.assertTrue(retired_guidance(instruction))

    def test_preserves_supported_discovery_and_explicit_fallbacks(self):
        for instruction in (
            "Use host tool search to load the named operation and its live schema.",
            "The local stdio MCP server is a developer fallback.",
            "Use a manual brief only for an explicit choice or documented missing evidence.",
            "Call socialseal_generate_brief with typed arguments.",
            "Call socialseal_start_brief_run with studyContext.",
            "Start a one-video Study with socialseal_start_study, then read socialseal_get_study.",
            "Blueprints and topic-only brief requests have retired.",
            "Read the brief with socialseal_get_brief and export it with socialseal_export_brief.",
            "The standalone CLI is retired; use MCP or supplied files.",
        ):
            self.assertEqual(retired_guidance(instruction), [])


if __name__ == "__main__":
    unittest.main()
