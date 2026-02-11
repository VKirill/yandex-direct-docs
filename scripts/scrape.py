#!/usr/bin/env python3
"""Scraper for Yandex Direct documentation → Markdown files."""

import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path("/home/ubuntu/yandex-direct-docs/docs")
URL_FILE = Path("/home/ubuntu/yandex-direct-docs/urls.txt")
LOG_FILE = Path("/home/ubuntu/yandex-direct-docs/scrape.log")
ERRORS_FILE = Path("/home/ubuntu/yandex-direct-docs/errors.log")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9",
}

PREFIX = "/support/direct/ru/"


def url_to_filepath(url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith(PREFIX):
        path = path[len(PREFIX):]
    path = path.strip("/")
    if not path:
        path = "index"
    return BASE_DIR / f"{path}.md"


def extract_content(html: str, url: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Try to find main article content
    article = (
        soup.find("article")
        or soup.find("div", class_="doc-c-main")
        or soup.find("div", class_="b-page-content")
        or soup.find("main")
        or soup.find("div", {"role": "main"})
    )

    if not article:
        # Fallback: find the largest div with text
        candidates = soup.find_all("div")
        article = max(candidates, key=lambda d: len(d.get_text()), default=None)

    if not article:
        return ""

    # Remove navigation, sidebars, footers
    for tag in article.find_all(["nav", "footer", "aside", "script", "style", "noscript"]):
        tag.decompose()

    # Remove breadcrumbs and navigation blocks
    for cls in ["breadcrumbs", "b-nav", "doc-c-nav", "doc-c-sidebar", "feedback", "b-foot"]:
        for el in article.find_all(class_=lambda c: c and cls in c):
            el.decompose()

    # Convert to markdown
    content = md(str(article), heading_style="ATX", bullets="-", strip=["img"])

    # Clean up excessive whitespace
    lines = content.split("\n")
    cleaned = []
    blank_count = 0
    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            blank_count += 1
            if blank_count <= 2:
                cleaned.append("")
        else:
            blank_count = 0
            cleaned.append(stripped)

    result = "\n".join(cleaned).strip()

    # Add source URL header
    return f"---\nsource: {url}\n---\n\n{result}\n"


def scrape_url(url: str, session: requests.Session) -> tuple[bool, str]:
    try:
        resp = session.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        content = extract_content(resp.text, url)
        if not content or len(content) < 100:
            return False, f"Empty/too short content"
        filepath = url_to_filepath(url)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content, encoding="utf-8")
        return True, str(filepath)
    except Exception as e:
        return False, str(e)


def main():
    urls = [u.strip() for u in URL_FILE.read_text().splitlines() if u.strip()]
    total = len(urls)
    print(f"Starting scrape of {total} URLs...")

    session = requests.Session()
    success = 0
    failed = 0
    errors = []

    for i, url in enumerate(urls, 1):
        ok, msg = scrape_url(url, session)
        if ok:
            success += 1
            status = "OK"
        else:
            failed += 1
            status = f"FAIL: {msg}"
            errors.append(f"{url} → {msg}")

        log_line = f"[{i}/{total}] {status} — {url}"
        print(log_line, flush=True)

        with open(LOG_FILE, "a") as f:
            f.write(log_line + "\n")

        # Polite delay to not overload Yandex servers
        if i % 10 == 0:
            time.sleep(1)
        else:
            time.sleep(0.3)

    # Save errors
    if errors:
        ERRORS_FILE.write_text("\n".join(errors), encoding="utf-8")

    summary = f"\nDone! Success: {success}/{total}, Failed: {failed}"
    print(summary)
    with open(LOG_FILE, "a") as f:
        f.write(summary + "\n")


if __name__ == "__main__":
    main()
