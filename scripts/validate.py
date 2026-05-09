#!/usr/bin/env python3
"""Lightweight checks for the awesome-social-media-zh README."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_HEADINGS = [
    "# awesome-social-media-zh",
    "## 内容范围",
    "## 目录",
    "## 资源区",
    "## 收录标准",
    "## 条目格式",
    "## 当前阶段",
    "## 本地维护",
    "## 贡献",
    "## 许可",
]

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DATE_RE = re.compile(r"观察日期：(\d{4}-\d{2}-\d{2})")
RESOURCE_LINE_RE = re.compile(r"^\s*-\s+\[[^\]]+\]\((https?://[^)]+)\)\s+-\s+")


def section_for_line(lines: list[str], line_number: int) -> str:
    section = ""
    for index, line in enumerate(lines[:line_number], start=1):
        if line.startswith("## "):
            section = line.strip()
    return section


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not README.exists():
        print("README.md is missing", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")

    urls: dict[str, int] = {}
    today = dt.date.today()

    in_code_block = False

    for line_number, line in enumerate(lines, start=1):
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        if "awosome" in line.lower():
            errors.append(f"line {line_number}: possible typo 'awosome'")

        for _label, target in LINK_RE.findall(line):
            if target.startswith("#") or target.startswith(("README", "CONTRIBUTING", "LICENSE")):
                continue

            if target.startswith(("http://", "https://")):
                if not is_valid_url(target):
                    errors.append(f"line {line_number}: invalid URL: {target}")
                if target in urls:
                    warnings.append(
                        f"line {line_number}: duplicate URL also appears on line {urls[target]}: {target}"
                    )
                urls.setdefault(target, line_number)
                continue

            if not (ROOT / target).exists():
                errors.append(f"line {line_number}: relative link target not found: {target}")

        if RESOURCE_LINE_RE.match(line):
            section = section_for_line(lines, line_number)
            if section not in {"## 相关"}:
                date_match = DATE_RE.search(line)
                if not date_match:
                    warnings.append(f"line {line_number}: resource entry has no observation date")
                    continue
                try:
                    observed = dt.date.fromisoformat(date_match.group(1))
                except ValueError:
                    errors.append(f"line {line_number}: invalid observation date")
                    continue
                if observed > today:
                    errors.append(f"line {line_number}: observation date is in the future")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Errors:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("README validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
