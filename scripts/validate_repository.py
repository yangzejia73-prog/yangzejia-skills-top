#!/usr/bin/env python3
"""Validate repository structure and flag high-risk instructions in Skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REGISTRY = ROOT / "registry" / "skills.json"
REQUIRED_FILES = [
    "README.md", "README.en.md", "LICENSE", "CONTRIBUTING.md",
    "SECURITY.md", "CHANGELOG.md", "registry/skills.json",
]
HIGH_RISK = {
    "download-and-execute": re.compile(r"(?:curl|wget).{0,100}(?:\||&&).{0,40}(?:sh|bash|powershell)", re.I),
    "secret-harvesting": re.compile(r"(?:read|collect|upload|send).{0,80}(?:api[_ -]?key|secret|ssh key|credential)", re.I),
    "destructive-command": re.compile(r"(?:rm\s+-rf|Remove-Item\s+.*-Recurse|format\s+[a-z]:)", re.I),
    "instruction-bypass": re.compile(r"ignore (?:all )?(?:previous|system|developer) instructions", re.I),
}


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}
    block = text.split("\n---\n", 1)[0][4:]
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"')
    return result


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid registry: {exc}")
        registry = {"skills": []}

    registered = {item.get("name"): item for item in registry.get("skills", [])}
    folders = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if folders != set(registered):
        errors.append(f"registry/folder mismatch: folders={sorted(folders)}, registered={sorted(registered)}")

    for name in sorted(folders):
        path = SKILLS / name / "SKILL.md"
        if not path.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("name") != name:
            errors.append(f"{name}: frontmatter name does not match folder")
        if len(meta.get("description", "")) < 40:
            errors.append(f"{name}: description is missing or not discriminating")
        if "TODO" in text or "[TODO" in text:
            errors.append(f"{name}: unfinished scaffold marker")
        if not (SKILLS / name / "tests" / "cases.md").is_file():
            errors.append(f"{name}: missing tests/cases.md")
        for label, pattern in HIGH_RISK.items():
            if pattern.search(text):
                warnings.append(f"{name}: review possible {label}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Validated {len(folders)} skills: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
