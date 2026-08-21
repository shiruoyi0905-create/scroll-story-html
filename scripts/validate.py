#!/usr/bin/env python3
"""Validate the repository's self-contained HTML entry points."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [
    ROOT / "index.html",
    ROOT / "narrative-longform-html/assets/template.html",
    ROOT / "examples/vibe-coding-wechat-miniprogram-SOP.html",
]


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.has_title = False
        self.has_viewport = False
        self.local_refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "title":
            self.has_title = True
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = True
        for key in ("href", "src"):
            value = values.get(key)
            if value:
                parsed = urlparse(value)
                if not parsed.scheme and not parsed.netloc and not value.startswith(("#", "data:")):
                    self.local_refs.append(parsed.path)


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing required file: {path.relative_to(ROOT)}"]

    text = path.read_text(encoding="utf-8")
    if not text.lstrip().lower().startswith("<!doctype html>"):
        errors.append("missing HTML5 doctype")

    parser = DocumentParser()
    parser.feed(text)
    if not parser.has_title:
        errors.append("missing <title>")
    if not parser.has_viewport:
        errors.append("missing viewport meta tag")

    for ref in parser.local_refs:
        target = (path.parent / ref).resolve()
        if ROOT not in target.parents and target != ROOT:
            errors.append(f"local reference leaves repository: {ref}")
        elif not target.exists():
            errors.append(f"broken local reference: {ref}")
    return errors


def main() -> int:
    failures = 0
    for html_file in HTML_FILES:
        errors = validate(html_file)
        name = html_file.relative_to(ROOT)
        if errors:
            failures += len(errors)
            for error in errors:
                print(f"FAIL {name}: {error}")
        else:
            print(f"PASS {name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
