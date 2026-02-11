#!/usr/bin/env python3
"""Fix all internal links in docs: (ru/...) and yandex.ru/support/direct → relative."""

import re
import os
from pathlib import Path

DOCS_DIR = Path("/home/ubuntu/yandex-direct-docs/docs")


def fix_links_in_file(filepath: Path) -> tuple[bool, int]:
    text = filepath.read_text(encoding="utf-8")
    original = text
    count = 0

    rel_to_root = os.path.relpath(DOCS_DIR, filepath.parent)

    def rewrite(match):
        nonlocal count
        path = match.group(1).strip("/")
        anchor = ""
        if "#" in path:
            path, anchor = path.split("#", 1)
            anchor = "#" + anchor

        # Handle .html suffix
        path = re.sub(r'\.html$', '', path)

        # Check target exists
        target_md = DOCS_DIR / f"{path}.md"
        target_index = DOCS_DIR / path / "index.md"

        if target_md.exists():
            count += 1
            return f"({rel_to_root}/{path}.md{anchor})"
        elif target_index.exists():
            count += 1
            return f"({rel_to_root}/{path}/index.md{anchor})"
        elif (DOCS_DIR / path).is_dir():
            count += 1
            return f"({rel_to_root}/{path}/{anchor})"
        else:
            # Keep as-is if target doesn't exist in our docs
            return match.group(0)

    # Fix (ru/path) and (ru/path#anchor)
    text = re.sub(r'\(ru/([^)]+)\)', rewrite, text)

    # Fix https://yandex.ru/support/direct/ru/path
    def rewrite_full(match):
        nonlocal count
        path = match.group(1).strip("/")
        anchor = ""
        if "#" in path:
            path, anchor = path.split("#", 1)
            anchor = "#" + anchor
        path = re.sub(r'\.html$', '', path)

        target_md = DOCS_DIR / f"{path}.md"
        target_index = DOCS_DIR / path / "index.md"

        if target_md.exists():
            count += 1
            return f"({rel_to_root}/{path}.md{anchor})"
        elif target_index.exists():
            count += 1
            return f"({rel_to_root}/{path}/index.md{anchor})"
        else:
            return match.group(0)

    text = re.sub(r'\(https?://yandex\.ru/support/direct/ru/([^)]+)\)', rewrite_full, text)
    text = re.sub(r'\(https?://yandex\.ru/support/direct/en/([^)]+)\)', rewrite_full, text)

    if text != original:
        filepath.write_text(text, encoding="utf-8")
        return True, count
    return False, 0


def main():
    files = sorted(DOCS_DIR.rglob("*.md"))
    total = len(files)
    changed = 0
    total_links = 0

    print(f"Fixing links in {total} files...")
    for i, f in enumerate(files, 1):
        was_changed, link_count = fix_links_in_file(f)
        if was_changed:
            changed += 1
            total_links += link_count
        if i % 100 == 0:
            print(f"  [{i}/{total}] {changed} files, {total_links} links fixed")

    print(f"\nDone! {changed} files updated, {total_links} links rewritten")


if __name__ == "__main__":
    main()
