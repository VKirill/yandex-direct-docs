#!/usr/bin/env python3
"""Aggressive cleanup pass 2: remove ALL boilerplate regardless of position."""

import re
import os
from pathlib import Path

DOCS_DIR = Path("/home/ubuntu/yandex-direct-docs/docs")

# These regex patterns will remove everything from their first match to end of file
# (applied in order, greedily)
CUT_FROM_PATTERNS = [
    # "Остались вопросы?" section — always boilerplate
    r'\n+#{1,5}\s*Остались вопросы\?.*',
    # Contact block without heading
    r'\n+Внимание\s*\n+Специалисты отдела клиентского сервиса.*',
    # QR code reference
    r'\n+Сканируйте QR-код.*',
    # Viber/WhatsApp/Chat links
    r'\n+При выборе Telegram, WhatsApp.*',
    r'\n+Написать в Viber.*',
    r'\n+Написать в чат.*',
    r'\n+\[Написать в чат\].*',
    # Phone block
    r'\n+Позвонить\s*\n+Клиентам и представителям.*',
    r'\n+Клиентам и представителям агентств можно связаться.*',
    # Phone numbers as standalone blocks
    r'\n+\*\*Регионы России\*\*.*\n+\*\*Москва\*\*.*',
    # PIN code reference
    r'\n+Для доступа к кампаниям специалисту потребуется.*',
    # "Написать письмо" block
    r'\n+Написать письмо\s*\n+Клиентам\s*\n+Агентствам.*',
    # "Формы обратной связи"
    r'\n+\[?Формы обратной связи\]?.*',
    # "Полезные ссылки" section
    r'\n+#{1,5}\s*Полезные ссылки.*',
    # "Правовые документы" section
    r'\n+#{1,5}\s*Правовые документы.*',
    # "Онлайн-обучение" section
    r'\n+#{1,5}\s*Онлайн-обучение.*',
    # "Узнайте больше" section
    r'\n+#{1,5}\s*Узнайте больше.*',
]

# Navigation: "Предыдущая" / "Следующая" — remove regardless of position
# These typically appear at the very end
NAV_CLEANUP = [
    r'\n+Предыдущая\s*\n+\[.*?\]\(.*?\)\s*\n+Следующая\s*\n+\[.*?\]\(.*?\)\s*$',
    r'\n+Предыдущая\s*\n+\[.*?\]\(.*?\)\s*$',
    r'\n+Следующая\s*\n+\[.*?\]\(.*?\)\s*$',
    r'\n+Предыдущая\s*\n+[^\[#\n].*\s*\n+Следующая\s*\n+[^\[#\n].*\s*$',
    r'\n+Предыдущая\s*\n+[^\[#\n].*\s*$',
    r'\n+Следующая\s*\n+[^\[#\n].*\s*$',
]

# Inline junk to remove (not trailing — can appear mid-content)
INLINE_REMOVE = [
    # Phone numbers as standalone lines
    r'\n\*\*Казахстан\*\*:.*\n',
    r'\n\*\*Узбекистан\*\*:.*\n',
    r'\n\*\*Беларусь\*\*:.*\+375.*\n',
    # Belarus contact block
    r'\n\|[^|]*\|\s*\n\|\s*---.*\|\s*\n\|[^|]*Для обращений из Республики Беларусь[^|]*\|\s*\n',
]


def cleanup_file(filepath: Path) -> tuple[bool, str]:
    try:
        text = filepath.read_text(encoding="utf-8")
        original = text

        # Pass 1: Cut from boilerplate markers (greedy — remove everything after)
        for pattern in CUT_FROM_PATTERNS:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                text = text[:match.start()]

        # Pass 2: Remove nav blocks
        for pattern in NAV_CLEANUP:
            text = re.sub(pattern, '', text, flags=re.DOTALL)

        # Pass 3: Remove inline junk
        for pattern in INLINE_REMOVE:
            text = re.sub(pattern, '\n', text)

        # Pass 4: Remove duplicate title (plain text before # heading)
        lines = text.split("\n")
        if lines[0] == "---":
            fm_end = -1
            for i in range(1, len(lines)):
                if lines[i] == "---":
                    fm_end = i
                    break
            if fm_end > 0:
                cs = fm_end + 1
                while cs < len(lines) and not lines[cs].strip():
                    cs += 1
                if cs < len(lines):
                    plain = lines[cs].strip()
                    for j in range(cs + 1, min(cs + 4, len(lines))):
                        h = lines[j].strip()
                        if h.startswith("# ") and h[2:].strip() == plain:
                            lines[cs] = ""
                            break
            text = "\n".join(lines)

        # Pass 5: Clean excessive whitespace
        text = re.sub(r'\n{4,}', '\n\n\n', text)
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

    print(f"Cleanup pass 2: {total} files...")
    for i, f in enumerate(files, 1):
        was_changed, msg = cleanup_file(f)
        if was_changed:
            changed += 1
        if i % 100 == 0:
            print(f"  [{i}/{total}] {changed} changed")

    print(f"\nDone! {changed}/{total} files updated")


if __name__ == "__main__":
    main()
