#!/usr/bin/env python3
"""Run dependency-free structural checks for the Meta Skill package.

This validates package files and local Markdown links only. It does not test
Agent loading, automatic routing, runtime behavior, or output quality.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "references/observability.md",
    "tests/README.md",
    "tests/REPORT_TEMPLATE.md",
)
REQUIRED_SECTIONS = (
    "When to use this Skill",
    "Interaction contract",
    "Lifecycle workflow",
    "Observability and evaluation rules",
    "Safety and authority boundaries",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> int:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, re.DOTALL)
    if not frontmatter:
        fail("could not parse YAML frontmatter boundaries")

    metadata = frontmatter.group(1)
    if not re.search(r"^name:\s*meta-skill\s*$", metadata, re.MULTILINE):
        fail("frontmatter name must be meta-skill")
    if not re.search(r"^description:\s*.+$", metadata, re.MULTILINE):
        fail("frontmatter description is missing")

    for heading in REQUIRED_SECTIONS:
        if f"## {heading}" not in skill:
            fail(f"missing required section: {heading}")

    agent_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if 'display_name: "Meta Skill"' not in agent_yaml:
        fail("OpenAI agent metadata display_name is missing")

    markdown_files = (
        ROOT / "README.md",
        ROOT / "SKILL.md",
        ROOT / "references/observability.md",
        ROOT / "tests/README.md",
        ROOT / "tests/REPORT_TEMPLATE.md",
    )
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown_file in markdown_files:
        source = markdown_file.read_text(encoding="utf-8")
        for target in link_pattern.findall(source):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("https://", "http://", "mailto:")):
                continue
            if not (markdown_file.parent / target).resolve().is_file():
                fail(f"broken local link in {markdown_file.relative_to(ROOT)}: {target}")

    test_plan = (ROOT / "tests/README.md").read_text(encoding="utf-8")
    for case_id in (f"T{i:02d}" for i in range(1, 17)):
        if f"### {case_id}" not in test_plan:
            fail(f"missing manual test case: {case_id}")

    print("PASS: package structure, frontmatter, required sections, and local links")
    print("LIMIT: no Agent loading, routing, behavior, or quality tests were run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
