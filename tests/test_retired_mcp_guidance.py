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

    def test_preserves_supported_discovery_and_explicit_fallbacks(self):
        for instruction in (
            "Use host tool search to load the named operation and its live schema.",
            "The local stdio MCP server is a developer fallback.",
            "Use a manual brief only for an explicit choice or documented missing evidence.",
            "Call socialseal_generate_brief with typed arguments.",
            "The standalone CLI is retired; use MCP or supplied files.",
        ):
            self.assertEqual(retired_guidance(instruction), [])


if __name__ == "__main__":
    unittest.main()
