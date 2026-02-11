#!/usr/bin/env python3
"""Cleanup scraped Yandex Direct docs: remove boilerplate, fix links."""

import re
import os
from pathlib import Path

DOCS_DIR = Path("/home/ubuntu/yandex-direct-docs/docs")

# Markers that indicate the start of boilerplate footer
FOOTER_MARKERS = [
    "Остались вопросы?",
    "### Полезные ссылки",
    "### Правовые документы",
    "### Онлайн-обучение",
    "### Узнайте больше",
    "Сканируйте QR-код",
    "Написать в Viber",
    "Написать в чат",
    "Позвонить\n",
    "Клиентам и представителям агентств можно связаться",
    "Для доступа к кампаниям специалисту потребуется",
    "Написать письмо\n",
    "Формы обратной связи",
    "Специалисты отдела клиентского сервиса",
]

# Patterns for Prev/Next navigation at the end of files
NAV_PATTERNS = [
    r'\nПредыдущая\n.*$',
    r'\nСледующая\n.*$',
]

# Internal link patterns to rewrite
# (ru/path/to/page) → (docs/path/to/page.md) or relative
INTERNAL_LINK_REWRITES = [
    # (ru/strategies/average-cpa) → (strategies/average-cpa.md)
    (r'\(ru/([^)#]+?)(?:#[^)]+)?\)', _rewrite_internal_link := None),  # placeholder
    # https://yandex.ru/support/direct/ru/strategies/... → relative
    (r'\(https?://yandex\.ru/support/direct/ru/([^)#]+?)(?:#[^)]+)?\)', None),
    # https://yandex.ru/support/direct/en/... → relative (same content)
    (r'\(https?://yandex\.ru/support/direct/en/([^)#]+?)(?:#[^)]+)?\)', None),
]


def find_footer_start(lines: list[str]) -> int:
    """Find the line index where boilerplate footer begins."""
    # Search from the end backwards for the earliest footer marker
    earliest = len(lines)

    full_text = "\n".join(lines)

    for marker in FOOTER_MARKERS:
        idx = full_text.find(marker)
        if idx != -1:
            # Convert char position to line number
            line_num = full_text[:idx].count("\n")
            # Go back a few lines to catch section headers before marker
            start = max(0, line_num - 2)
            # Only consider if it's in the last 40% of the file
            if start > len(lines) * 0.4:
                earliest = min(earliest, start)

    return earliest


def remove_prev_next_nav(text: str) -> str:
    """Remove 'Предыдущая' and 'Следующая' navigation blocks at the end."""
    # These appear as the last lines in most files
    # Pattern: \nПредыдущая\n\n[Link text](url)\n\nСледующая\n\n[Link text](url)\n
    text = re.sub(
        r'\n+Предыдущая\s*\n+\[.*?\]\(.*?\)\s*\n+Следующая\s*\n+\[.*?\]\(.*?\)\s*$',
        '', text, flags=re.DOTALL
    )
    # Sometimes only one of them
    text = re.sub(
        r'\n+Предыдущая\s*\n+\[.*?\]\(.*?\)\s*$',
        '', text, flags=re.DOTALL
    )
    text = re.sub(
        r'\n+Следующая\s*\n+\[.*?\]\(.*?\)\s*$',
        '', text, flags=re.DOTALL
    )
    # Plain text version (no link)
    text = re.sub(
        r'\n+Предыдущая\s*\n+[^\[#\n].*\n+Следующая\s*\n+[^\[#\n].*\s*$',
        '', text, flags=re.DOTALL
    )
    return text


def rewrite_links(text: str, file_path: Path) -> str:
    """Rewrite Yandex internal links to relative paths within the repo."""

    # Calculate relative path from current file to docs root
    rel_to_root = os.path.relpath(DOCS_DIR, file_path.parent)

    def make_relative_link(match):
        path = match.group(1).strip("/")
        anchor = ""
        # Check if there's an anchor in the original match
        full = match.group(0)
        anchor_match = re.search(r'#([^)]+)', full)
        if anchor_match:
            anchor = "#" + anchor_match.group(1)

        # Check if the target file exists
        target = DOCS_DIR / f"{path}.md"
        target_dir = DOCS_DIR / path

        if target.exists():
            return f"({rel_to_root}/{path}.md{anchor})"
        elif (target_dir / "index.md").exists():
            return f"({rel_to_root}/{path}/index.md{anchor})"
        elif target_dir.is_dir():
            # Directory exists but no index — link to dir
            return f"({rel_to_root}/{path}/{anchor})"
        else:
            # File doesn't exist in our docs — keep original URL
            return match.group(0)

    # Rewrite (ru/path/to/page) links
    text = re.sub(r'\(ru/([^)]*)\)', make_relative_link, text)

    # Rewrite https://yandex.ru/support/direct/ru/... links
    text = re.sub(
        r'\(https?://yandex\.ru/support/direct/ru/([^)]*)\)',
        make_relative_link, text
    )

    # Rewrite https://yandex.ru/support/direct/en/... links
    text = re.sub(
        r'\(https?://yandex\.ru/support/direct/en/([^)]*)\)',
        make_relative_link, text
    )

    # Rewrite old tech.yandex.ru links to best-guess internal links
    def rewrite_tech_link(match):
        path = match.group(1).strip("/")
        # Try to map old API doc paths
        # e.g., dg/concepts/use-cases → alternative-interfaces/api
        return match.group(0)  # Keep as-is if can't map

    text = re.sub(
        r'\(https?://tech\.yandex\.ru/direct/([^)]*)\)',
        rewrite_tech_link, text
    )

    return text


def remove_duplicate_title(text: str) -> str:
    """Remove duplicate title that appears before the # heading."""
    # Pattern: after front matter, there's often a plain text title
    # followed by the same title as # heading
    lines = text.split("\n")
    # Find front matter end
    if lines[0] == "---":
        fm_end = -1
        for i in range(1, len(lines)):
            if lines[i] == "---":
                fm_end = i
                break
        if fm_end > 0:
            # Check if line after front matter + blank is same as next # heading
            content_start = fm_end + 1
            # Skip blank lines
            while content_start < len(lines) and not lines[content_start].strip():
                content_start += 1

            if content_start < len(lines):
                plain_title = lines[content_start].strip()
                # Look for matching # heading in next few lines
                for j in range(content_start + 1, min(content_start + 4, len(lines))):
                    heading = lines[j].strip()
                    if heading.startswith("# ") and heading[2:].strip() == plain_title:
                        # Remove the plain title line
                        lines[content_start] = ""
                        break

    return "\n".join(lines)


def clean_excessive_whitespace(text: str) -> str:
    """Remove excessive blank lines (max 2 consecutive)."""
    return re.sub(r'\n{4,}', '\n\n\n', text)


def cleanup_file(filepath: Path) -> tuple[bool, str]:
    """Clean up a single markdown file. Returns (changed, message)."""
    try:
        text = filepath.read_text(encoding="utf-8")
        original = text

        # 1. Remove footer boilerplate
        lines = text.split("\n")
        footer_start = find_footer_start(lines)
        if footer_start < len(lines):
            text = "\n".join(lines[:footer_start])

        # 2. Remove prev/next navigation
        text = remove_prev_next_nav(text)

        # 3. Remove duplicate title
        text = remove_duplicate_title(text)

        # 4. Rewrite internal links
        text = rewrite_links(text, filepath)

        # 5. Clean whitespace
        text = clean_excessive_whitespace(text)
        text = text.rstrip() + "\n"

        if text != original:
            filepath.write_text(text, encoding="utf-8")
            return True, "cleaned"
        return False, "no changes"

    except Exception as e:
        return False, f"ERROR: {e}"


def main():
    files = sorted(DOCS_DIR.rglob("*.md"))
    total = len(files)
    changed = 0
    errors = 0

    print(f"Cleaning {total} files...")

    for i, f in enumerate(files, 1):
        was_changed, msg = cleanup_file(f)
        if was_changed:
            changed += 1
        if msg.startswith("ERROR"):
            errors += 1
            print(f"  [{i}/{total}] ERROR: {f.relative_to(DOCS_DIR)} — {msg}")

        if i % 50 == 0:
            print(f"  [{i}/{total}] processed ({changed} changed so far)")

    print(f"\nDone! {changed}/{total} files cleaned, {errors} errors")


if __name__ == "__main__":
    main()
