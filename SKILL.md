---
name: yandex-direct
description: >-
  Complete Yandex Direct documentation in Russian (509 articles). Use when
  the user asks about Yandex Direct advertising campaigns, ad targeting,
  keywords strategy, bid management, ad moderation, retargeting, strategies,
  CPM campaigns, feeds, Telegram Ads, or any aspect of Yandex contextual
  and display advertising platform. Covers all campaign types, bidding
  strategies, targeting options, moderation rules, payment methods, and
  performance analytics.
license: Content belongs to Yandex. Repository for reference purposes.
allowed-tools: Read Grep Glob
metadata:
  version: "1.0.0"
  author: pomogay-marketing
  category: advertising
  language: ru
  articles: "509"
  source: https://yandex.ru/support/direct/ru/
  telegram: https://t.me/pomogay_marketing
---

# Yandex Direct Documentation

> 509 articles covering all aspects of Yandex Direct advertising platform.
> Language: Russian. Updated: February 2026.

## How to Use This Skill

Search and read documentation files in the `docs/` directory:

```bash
# Search by keyword
grep -r "ретаргетинг" docs/ --include="*.md" -l

# List section contents
ls docs/strategies/

# Read specific article
cat docs/strategies/select-strategy.md
```

Each file has YAML front matter with `source:` — the original page URL on yandex.ru.

## Documentation Map

### Campaign Types

| Type | Path | Description |
|------|------|-------------|
| Unified Performance (UPC) | `docs/unified-performance-campaign/` | Main campaign type for search + display |
| Campaign Master | `docs/campaign-master/` | Simplified campaign creation wizard |
| Product Campaign | `docs/product-campaign/` | Product feed-based promotions |
| CPM Display | `docs/products-cpm-campaign/` | Display ads with CPM billing |
| Video Ads | `docs/products-cpm-campaign-video/` | Video ad formats |
| Video Banners | `docs/products-cpm-campaign-videobanner/` | Banner with video |
| Frontpage Ads | `docs/products-cpm-campaign-frontpage/` | Ads on Yandex homepage |
| Connected TV | `docs/products-cpm-campaign-connected-tv/` | Smart TV advertising |
| Mobile Apps | `docs/products-mobile-apps-ads/` | iOS/Android app promotion |
| Company Ads | `docs/company-ads/` | Business cards in Maps & Search |
| Telegram Ads | `docs/telegram-ads/` | Ads in Telegram channels (YAN partners) |
| DOOH | `docs/dooh/` | Digital out-of-home advertising |
| Search Banner | `docs/products-media-context-banner/` | Banners on search results page |
| Fixed CPM | `docs/fixed-cpm-campaigns/` | Premium fixed-price placements |

### Bidding Strategies (`docs/strategies/`)

| Strategy | File | When to Use |
|----------|------|-------------|
| Strategy Overview | `select-strategy.md` | Choosing the right strategy |
| Max Conversions | `average-cpa.md` | Optimize for CPA target |
| Max Clicks | `average-cpc.md` | Maximize traffic volume |
| Max Profit | `maximum-profit.md` | Optimize ROAS / profitability |
| Manual Bidding | `manual-strategy.md` | Full control over bids |
| Portfolio Strategy | `portfolio-strategy.md` | Manage group of campaigns |
| Priority Goals | `priority-goals.md` | Goal-based optimization |
| Budgets | `budgets-in-strategies.md` | Budget configuration |

### Targeting (`docs/impression-criteria/`, `docs/keywords/`)

| Targeting | File | Description |
|-----------|------|-------------|
| Keywords | `docs/keywords/keywords.md` | Keyword selection basics |
| Negative Keywords | `docs/keywords/negative-keywords.md` | Excluding irrelevant queries |
| Operators | `docs/keywords/symbols-and-operators.md` | Match type operators |
| Wordstat | `docs/keywords/wordstat.md` | Keyword research tool |
| Auto-targeting | `docs/impression-criteria/autotargeting.md` | Automatic audience matching |
| Retargeting | `docs/impression-criteria/retargeting-lists.md` | Returning site visitors |
| Offer Retargeting | `docs/impression-criteria/offer-retargeting.md` | Product-level retargeting |
| Geo-targeting | `docs/efficiency/geotargeting.md` | Geographic targeting |
| Time Targeting | `docs/efficiency/timetargeting.md` | Schedule-based targeting |

### Ad Creatives (`docs/efficiency/`)

| Element | File |
|---------|------|
| Improve Ads Guide | `improve-your-ads.md` |
| Text & Headlines | `text-and-title.md` |
| Images | `images.md` |
| Video | `video.md` |
| Quick Links (Sitelinks) | `quick-links.md` |
| Carousel | `carousel.md` |
| Turbo Pages | `turbo-pages.md` |

### Feeds (`docs/feeds/`)

| Topic | File |
|-------|------|
| About Feeds | `about.md` |
| Feed Types | `types.md` |
| Requirements | `requirements.md` |
| YML Format | `requirements-yml.md` |
| Validation | `validate.md` |

### Analytics (`docs/statistics/`)

| Report | File |
|--------|------|
| Overview | `overview.md` |
| Report Wizard | `report-wizard.md` |
| Search Queries | `search-queries.md` |
| Conversions | `conversions.md` |
| UTM Tags | `url-tags.md` |
| Attribution Models | `attribution-model.md` |

### Moderation (`docs/moderation/`)

| Topic | File |
|-------|------|
| Ad Rules | `adv-rules.md` |
| Technical Limits | `technical-restrictions.md` |
| Age Restrictions | `age-alerts.md` |
| Special Categories (60+) | `categories/` directory |

### Payments (`docs/payments/`)

| Topic | File |
|-------|------|
| Payment Methods | `payment-methods.md` |
| Promo Codes | `promocode.md` |
| Refunds | `refund.md` |
| Deferred Payment | `deferred-payment.md` |
| Shared Account | `shared-account.md` |

### Technology (`docs/technologies-and-services/`)

| Topic | File |
|-------|------|
| VCG Auction | `vcg-auction.md` |
| Anti-fraud | `antifraud.md` |
| Crypta (Interest Detection) | `crypta.md` |
| Metrika Integration | `metrika-in-direct.md` |
| AI Assistant | `ai-assistant.md` |
| Ad Labeling | `ad-labelingl.md` |

### Ad Placements (`docs/general/`)

| Placement | File |
|-----------|------|
| Search Positions | `positions.md` |
| YAN (Yandex Ad Network) | `yan.md` |
| Dynamic Placements | `dynamic-places.md` |
| Product Gallery | `docs/product-gallery/about.md` |

### Effectiveness Research

| Study | Path |
|-------|------|
| Brand Lift | `docs/brand-lift/` |
| Search Lift | `docs/search-lift/` |
| Visit Lift | `docs/visit-lift/` |
| Target Lift | `docs/target-lift/` |

### Other Sections

| Section | Path |
|---------|------|
| Getting Started | `docs/quick-start/` |
| Interfaces & API | `docs/alternative-interfaces/` |
| New Interface | `docs/new-interface/` |
| For Agencies | `docs/agencies/` |
| Troubleshooting | `docs/troubleshooting/` |
| Glossary | `docs/glossary.md` |
| Reach Campaigns | `docs/reach-campaigns.md` |

## Key Concepts

### Billing Models
- **CPC** (Cost Per Click) — pay per click
- **CPA** (Cost Per Action) — pay per conversion
- **CPM** (Cost Per Mille) — pay per 1000 impressions

### Main Placements
- **Search** — Yandex search results
- **YAN** (Yandex Ad Network) — partner websites and apps
- **Retargeting** — re-engagement of past visitors

### Ad Formats
- Text & Image ads
- Graphic banners
- Video ads
- Smart banners (dynamic)
- Product ads (from feeds)

## Answering Questions

When answering user questions about Yandex Direct:

1. **Identify the topic** — match to a section above
2. **Read the relevant file** using `Read` or `cat`
3. **Search for specifics** using `grep -r "keyword" docs/`
4. **Cite the source** — each file has a `source:` URL in front matter
5. **Answer in Russian** unless the user writes in another language
