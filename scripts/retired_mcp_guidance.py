"""Detect retired caller instructions, including prose without wrapper names."""

import re

PATTERNS = {
    "retired MCP wrapper": r"\bsocialseal_(?:list_available_tools|get_tool_schema|call_tool)\b",
    "compatibility dispatcher or target": r"\bcompatibility\s+(?:dispatcher|targets?)\b",
    "backend selector and payload": r"\btoolName\s*[/,]\s*body\b",
    "retired CLI package": r"@socialseal/cli\b",
    "retired CLI tool command": r"\btools\s+(?:call|schema|list|status)\b",
    "retired journey execution selector": r"\bexecutionMode\b",
    # SOC-1024 deleted Blueprints and the blueprint-backed brief save.
    "removed Blueprint tool": r"\bsocialseal_(?:generate_blueprint|get_blueprint|save_blueprint|get_blueprint_shots|refresh_blueprint_shots|save_brief)\b",
    "removed Blueprint argument": r"\b(?:blueprintId|blueprintVersion|panelId)\b",
    "retired Blueprint skill": r"\bsocialseal-blueprint-builder\b",
    # SOC-1025: one video is a one-video Study (socialseal_start_study).
    "removed single-video analysis tool": r"\bsocialseal_(?:analyse_public_video|get_video_evidence)\b",
}


def retired_guidance(content):
    # Markdown backticks may separate the selector from its payload in prose.
    plain = content.replace("`", "")
    return [label for label, pattern in PATTERNS.items() if re.search(pattern, plain, re.I)]
