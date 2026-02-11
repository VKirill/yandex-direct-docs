---
name: yandex-direct
version: 1.0.0
description: >-
  Complete Yandex Direct documentation reference (509 articles, Russian).
  Use when the user asks about Yandex Direct advertising: campaign types,
  bidding strategies, targeting, retargeting, keywords, ad moderation,
  feeds, Telegram Ads, CPM display, payments, analytics, or any aspect
  of Yandex contextual and display advertising. Provides navigation map,
  search instructions, and key concepts for answering questions accurately.
user-invocable: false
allowed-tools: Read Grep Glob
metadata:
  author: pomogay-marketing
  category: advertising
  language: ru
  articles: "509"
  source: https://yandex.ru/support/direct/ru/
  telegram: https://t.me/pomogay_marketing
---

# Yandex Direct — Documentation Reference

> 509 articles. Language: Russian. Updated: February 2026.
> Source: [yandex.ru/support/direct/ru/](https://yandex.ru/support/direct/ru/)

## Quick Search

```bash
# Find articles by keyword
grep -r "ретаргетинг" docs/ --include="*.md" -l

# List all files in a section
ls docs/strategies/

# Read a specific article
cat docs/strategies/select-strategy.md
```

## Campaign Types

| Type | Path | Description |
|------|------|-------------|
| Unified Performance (UPC) | `docs/unified-performance-campaign/` | Main type — search + display + maps |
| Campaign Master | `docs/campaign-master/` | Simplified creation wizard |
| Product Campaign | `docs/product-campaign/` | Feed-based product promotions |
| CPM Display | `docs/products-cpm-campaign/` | Display ads, CPM billing |
| Video Ads | `docs/products-cpm-campaign-video/` | Video ad formats |
| Video Banners | `docs/products-cpm-campaign-videobanner/` | Banners with video |
| Frontpage Ads | `docs/products-cpm-campaign-frontpage/` | Ads on ya.ru homepage |
| Connected TV | `docs/products-cpm-campaign-connected-tv/` | Smart TV advertising |
| Mobile Apps | `docs/products-mobile-apps-ads/` | iOS / Android app promotion |
| Company Ads | `docs/company-ads/` | Business cards in Maps & Search |
| Telegram Ads | `docs/telegram-ads/` | Ads in Telegram channels (YAN) |
| DOOH | `docs/dooh/` | Digital out-of-home |
| Search Banner | `docs/products-media-context-banner/` | Banner on search results |
| Fixed CPM | `docs/fixed-cpm-campaigns/` | Premium fixed-price placements |

## Bidding Strategies

Path: `docs/strategies/`

| Strategy | File | Use Case |
|----------|------|----------|
| Overview | `select-strategy.md` | How to choose a strategy |
| Max Conversions | `average-cpa.md` | Optimize for CPA |
| Max Clicks | `average-cpc.md` | Maximize traffic |
| Max Profit | `maximum-profit.md` | Optimize ROAS |
| Manual Bidding | `manual-strategy.md` | Full bid control |
| Portfolio | `portfolio-strategy.md` | Multi-campaign management |
| Priority Goals | `priority-goals.md` | Goal-based optimization |
| Budgets | `budgets-in-strategies.md` | Budget configuration |

## Targeting

| Type | File |
|------|------|
| Keywords | `docs/keywords/keywords.md` |
| Negative Keywords | `docs/keywords/negative-keywords.md` |
| Operators | `docs/keywords/symbols-and-operators.md` |
| Wordstat | `docs/keywords/wordstat.md` |
| Auto-targeting | `docs/impression-criteria/autotargeting.md` |
| Retargeting | `docs/impression-criteria/retargeting-lists.md` |
| Offer Retargeting | `docs/impression-criteria/offer-retargeting.md` |
| Geo-targeting | `docs/efficiency/geotargeting.md` |
| Time Targeting | `docs/efficiency/timetargeting.md` |

## Ad Creatives

Path: `docs/efficiency/`

Files: `improve-your-ads.md`, `text-and-title.md`, `images.md`, `video.md`, `quick-links.md`, `carousel.md`, `turbo-pages.md`

## Feeds

Path: `docs/feeds/`

Files: `about.md`, `types.md`, `requirements.md`, `requirements-yml.md`, `validate.md`

## Analytics & Reports

Path: `docs/statistics/`

Files: `overview.md`, `report-wizard.md`, `search-queries.md`, `conversions.md`, `url-tags.md`, `attribution-model.md`

## Moderation

Path: `docs/moderation/`

- Rules: `adv-rules.md`
- Technical limits: `technical-restrictions.md`
- Age restrictions: `age-alerts.md`
- **60+ special categories**: `categories/` directory

## Payments

Path: `docs/payments/`

Files: `payment-methods.md`, `promocode.md`, `refund.md`, `deferred-payment.md`, `shared-account.md`

## Technology & Services

Path: `docs/technologies-and-services/`

Files: `vcg-auction.md`, `antifraud.md`, `crypta.md`, `metrika-in-direct.md`, `ai-assistant.md`, `ad-labelingl.md`

## Ad Placements

| Placement | File |
|-----------|------|
| Search | `docs/general/positions.md` |
| YAN (Ad Network) | `docs/general/yan.md` |
| Dynamic | `docs/general/dynamic-places.md` |
| Product Gallery | `docs/product-gallery/about.md` |

## Research & Lift Studies

`docs/brand-lift/`, `docs/search-lift/`, `docs/visit-lift/`, `docs/target-lift/`

## Other Sections

| Section | Path |
|---------|------|
| Getting Started | `docs/quick-start/` |
| API & Interfaces | `docs/alternative-interfaces/` |
| New Interface | `docs/new-interface/` |
| For Agencies | `docs/agencies/` |
| Troubleshooting | `docs/troubleshooting/` |
| Glossary | `docs/glossary.md` |

## Key Concepts

- **CPC** — Cost Per Click
- **CPA** — Cost Per Action (conversion)
- **CPM** — Cost Per Mille (1000 impressions)
- **YAN** — Yandex Ad Network (partner sites)
- **UPC** — Unified Performance Campaign (main type)
- **Retargeting** — re-engaging past site visitors
- **Auto-targeting** — automatic audience matching by Yandex

## How to Answer Questions

1. Identify the topic from the tables above
2. Read the relevant file with `Read` tool
3. If unsure, search with `grep -r "keyword" docs/`
4. Always cite the file path in your answer
5. Provide the `source:` URL from front matter as reference
6. Answer in Russian unless user writes in another language
