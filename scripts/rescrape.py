#!/usr/bin/env python3
"""Re-scrape pages that got SmartCaptcha instead of content."""

import os
import sys
import time
import random
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path("/home/ubuntu/yandex-direct-docs/docs")
PREFIX = "/support/direct/ru/"

CAPTCHA_URLS = [
    "https://yandex.ru/support/direct/ru/unified-performance-campaign/about",
    "https://yandex.ru/support/direct/ru/troubleshooting/why-this-ad",
    "https://yandex.ru/support/direct/ru/thematic-section/insurance",
    "https://yandex.ru/support/direct/ru/thematic-section/finance",
    "https://yandex.ru/support/direct/ru/thematic-section/credits/responce-codes",
    "https://yandex.ru/support/direct/ru/technologies-and-services/antifraud",
    "https://yandex.ru/support/direct/ru/strategies/manual-strategy-mobile-apps",
    "https://yandex.ru/support/direct/ru/search-lift/about",
    "https://yandex.ru/support/direct/ru/search-lift",
    "https://yandex.ru/support/direct/ru/research",
    "https://yandex.ru/support/direct/ru/reach-campaigns",
    "https://yandex.ru/support/direct/ru/quick-start/quick-start",
    "https://yandex.ru/support/direct/ru/quick-start/get-help",
    "https://yandex.ru/support/direct/ru/quick-start/create-campaign",
    "https://yandex.ru/support/direct/ru/products-media-context-banner/create",
    "https://yandex.ru/support/direct/ru/products-media-context-banner/about",
    "https://yandex.ru/support/direct/ru/products-cpm-campaign-frontpage/create",
    "https://yandex.ru/support/direct/ru/payments/promocode",
    "https://yandex.ru/support/direct/ru/payments/payment-methods",
]

# Realistic browser headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}


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

    article = (
        soup.find("article")
        or soup.find("div", class_="doc-c-main")
        or soup.find("div", class_="b-page-content")
        or soup.find("main")
        or soup.find("div", {"role": "main"})
    )

    if not article:
        candidates = soup.find_all("div")
        article = max(candidates, key=lambda d: len(d.get_text()), default=None)

    if not article:
        return ""

    for tag in article.find_all(["nav", "footer", "aside", "script", "style", "noscript"]):
        tag.decompose()

    for cls in ["breadcrumbs", "b-nav", "doc-c-nav", "doc-c-sidebar", "feedback", "b-foot"]:
        for el in article.find_all(class_=lambda c: c and cls in c):
            el.decompose()

    content = md(str(article), heading_style="ATX", bullets="-", strip=["img"])

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
    return f"---\nsource: {url}\n---\n\n{result}\n"


def main():
    total = len(CAPTCHA_URLS)
    print(f"Re-scraping {total} captcha-affected pages...")
    print(f"Using 5-8s delays between requests to avoid captcha\n")

    session = requests.Session()
    success = 0
    failed = 0
    still_captcha = 0

    for i, url in enumerate(CAPTCHA_URLS, 1):
        # Random delay 5-8 seconds
        if i > 1:
            delay = random.uniform(5, 8)
            print(f"  waiting {delay:.1f}s...", flush=True)
            time.sleep(delay)

        try:
            resp = session.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()

            # Check if we got captcha again
            if "SmartCaptcha" in resp.text or "captcha" in resp.text.lower():
                print(f"[{i}/{total}] CAPTCHA AGAIN - {url}")
                still_captcha += 1
                failed += 1
                continue

            content = extract_content(resp.text, url)
            if not content or len(content) < 100:
                print(f"[{i}/{total}] EMPTY - {url}")
                failed += 1
                continue

            filepath = url_to_filepath(url)
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding="utf-8")
            success += 1
            # Show first 80 chars of content after front matter
            preview = content.split("---\n\n", 1)[-1][:80].replace("\n", " ")
            print(f"[{i}/{total}] OK - {url}")
            print(f"  preview: {preview}...")

        except Exception as e:
            print(f"[{i}/{total}] ERROR - {url}: {e}")
            failed += 1

    print(f"\nDone! Success: {success}/{total}, Failed: {failed}, Still captcha: {still_captcha}")

    if still_captcha > 0:
        print(f"\n{still_captcha} pages still blocked by captcha.")
        print("Try running again after a longer wait, or use a different IP/VPN.")


if __name__ == "__main__":
    main()
