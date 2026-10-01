"""Detect retired caller instructions, including prose without wrapper names."""

import re

PATTERNS = {
    "retired MCP wrapper": r"\bsocialseal_(?:list_available_tools|get_tool_schema|call_tool)\b",
    "compatibility dispatcher or target": r"\bcompatibility\s+(?:dispatcher|targets?)\b",
    "backend selector and payload": r"\btoolName\s*[/,]\s*body\b",
    "retired CLI package": r"@socialseal/cli\b",
    "retired CLI tool command": r"\btools\s+(?:call|schema|list|status)\b",
    "retired journey execution selector": r"\bexecutionMode\b",
}


def retired_guidance(content):
    # Markdown backticks may separate the selector from its payload in prose.
    plain = content.replace("`", "")
    return [label for label, pattern in PATTERNS.items() if re.search(pattern, plain, re.I)]
