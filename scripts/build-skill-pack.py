#!/usr/bin/env python3
"""Build downloadable skill pack for Claude Chat web."""

import os
import shutil
import zipfile
from pathlib import Path

ROOT = Path("/home/ubuntu/yandex-direct-docs")
DOCS = ROOT / "docs"
DIST = ROOT / "dist"

# Key articles from each section — curated for maximum value
KEY_ARTICLES = [
    # Campaign types
    "unified-performance-campaign/about.md",
    "unified-performance-campaign/create-text-image.md",
    "unified-performance-campaign/create-product.md",
    "unified-performance-campaign/create-comb-ad.md",
    "unified-performance-campaign/create-catalogs.md",
    "unified-performance-campaign/upgrade-to-UPC.md",
    "campaign-master/about.md",
    "product-campaign/create.md",
    "telegram-ads/create.md",
    "company-ads/create.md",
    "products-mobile-apps-ads/about.md",
    # Strategies
    "strategies/select-strategy.md",
    "strategies/average-cpa.md",
    "strategies/average-cpc.md",
    "strategies/maximum-profit.md",
    "strategies/manual-strategy.md",
    "strategies/portfolio-strategy.md",
    "strategies/priority-goals.md",
    "strategies/budgets-in-strategies.md",
    # Keywords & targeting
    "keywords/keywords.md",
    "keywords/negative-keywords.md",
    "keywords/symbols-and-operators.md",
    "keywords/wordstat.md",
    "impression-criteria/autotargeting.md",
    "impression-criteria/retargeting-lists.md",
    "impression-criteria/offer-retargeting.md",
    # Efficiency
    "efficiency/geotargeting.md",
    "efficiency/timetargeting.md",
    "efficiency/text-and-title.md",
    "efficiency/images.md",
    "efficiency/video.md",
    "efficiency/quick-links.md",
    "efficiency/improve-your-ads.md",
    # Feeds
    "feeds/about.md",
    "feeds/types.md",
    "feeds/requirements.md",
    "feeds/requirements-yml.md",
    # Statistics
    "statistics/overview.md",
    "statistics/report-wizard.md",
    "statistics/conversions.md",
    "statistics/attribution-model.md",
    "statistics/url-tags.md",
    # Moderation
    "moderation/adv-rules.md",
    "moderation/technical-restrictions.md",
    "moderation/age-alerts.md",
    # Payments
    "payments/payment-methods.md",
    "payments/promocode.md",
    # Technology
    "technologies-and-services/vcg-auction.md",
    "technologies-and-services/antifraud.md",
    "technologies-and-services/metrika-in-direct.md",
    # Placements
    "general/positions.md",
    "general/yan.md",
    # CPM
    "products-cpm-campaign/about.md",
    "reach-campaigns.md",
    # Other
    "glossary.md",
    "quick-start/quick-start.md",
    "quick-start/create-campaign.md",
]


def build_zip():
    """Build ZIP with structured skill files."""
    DIST.mkdir(exist_ok=True)
    zip_path = DIST / "yandex-direct-skill.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Official format: skill-name/ as root folder inside ZIP
        prefix = "yandex-direct"

        # SKILL.md at skill root
        skill_src = ROOT / ".claude" / "skills" / "yandex-direct" / "SKILL.md"
        zf.write(skill_src, f"{prefix}/SKILL.md")

        # Resources (official name per Anthropic spec)
        refs_dir = ROOT / ".claude" / "skills" / "yandex-direct" / "references"
        for ref in refs_dir.glob("*.md"):
            zf.write(ref, f"{prefix}/resources/{ref.name}")

        # Key docs
        added = 0
        for rel_path in KEY_ARTICLES:
            full_path = DOCS / rel_path
            if full_path.exists():
                zf.write(full_path, f"{prefix}/resources/docs/{rel_path}")
                added += 1
            else:
                print(f"  SKIP (not found): {rel_path}")

        print(f"ZIP: {added} docs + SKILL.md + {len(list(refs_dir.glob('*.md')))} references")

    size_kb = zip_path.stat().st_size / 1024
    print(f"Created: {zip_path} ({size_kb:.0f} KB)")
    return zip_path


def build_single_file():
    """Build single consolidated markdown file."""
    DIST.mkdir(exist_ok=True)
    out_path = DIST / "yandex-direct-skill.md"

    parts = []

    # Header
    parts.append("# Яндекс Директ — Полный справочник для AI-агентов\n")
    parts.append("> 509 статей документации Яндекс Директа. Февраль 2026.\n")
    parts.append("> Telegram: https://t.me/pomogay_marketing\n")
    parts.append("> GitHub: https://github.com/VKirill/yandex-direct-docs\n\n")
    parts.append("---\n\n")

    # SKILL.md (navigation map)
    skill_src = ROOT / ".claude" / "skills" / "yandex-direct" / "SKILL.md"
    content = skill_src.read_text()
    # Remove frontmatter
    if content.startswith("---"):
        end = content.index("---", 3)
        content = content[end + 3:].strip()
    parts.append(content)
    parts.append("\n\n---\n\n")

    # References
    refs_dir = ROOT / ".claude" / "skills" / "yandex-direct" / "references"
    for ref in sorted(refs_dir.glob("*.md")):
        ref_content = ref.read_text().strip()
        parts.append(ref_content)
        parts.append("\n\n---\n\n")

    # Key articles
    parts.append("# Документация по разделам\n\n")
    added = 0
    total_chars = sum(len(p) for p in parts)

    for rel_path in KEY_ARTICLES:
        full_path = DOCS / rel_path
        if not full_path.exists():
            continue

        doc_content = full_path.read_text()
        # Remove source frontmatter
        if doc_content.startswith("---"):
            try:
                end = doc_content.index("---", 3)
                doc_content = doc_content[end + 3:].strip()
            except ValueError:
                pass

        # Truncate very large files to ~4KB
        if len(doc_content) > 4000:
            doc_content = doc_content[:4000] + "\n\n*[Статья сокращена. Полная версия: docs/" + rel_path + "]*\n"

        parts.append(f"<!-- docs/{rel_path} -->\n\n")
        parts.append(doc_content)
        parts.append("\n\n---\n\n")
        added += 1
        total_chars += len(doc_content)

    result = "".join(parts)
    out_path.write_text(result, encoding="utf-8")

    size_kb = out_path.stat().st_size / 1024
    print(f"Single file: {added} articles included")
    print(f"Created: {out_path} ({size_kb:.0f} KB)")
    return out_path


if __name__ == "__main__":
    print("Building skill pack...\n")
    build_zip()
    print()
    build_single_file()
    print("\nDone!")
