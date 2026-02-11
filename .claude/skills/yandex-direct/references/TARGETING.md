# Targeting Quick Reference

## Targeting Types

| Type | How It Works | File |
|------|-------------|------|
| Keywords | Manual keyword selection, match types | `docs/keywords/keywords.md` |
| Negative Keywords | Exclude irrelevant queries | `docs/keywords/negative-keywords.md` |
| Auto-targeting | Yandex ML matches audience automatically | `docs/impression-criteria/autotargeting.md` |
| Retargeting | Re-engage site visitors via Metrika segments | `docs/impression-criteria/retargeting-lists.md` |
| Offer Retargeting | Product-level retargeting from feeds | `docs/impression-criteria/offer-retargeting.md` |
| Geo-targeting | Show ads in specific regions | `docs/efficiency/geotargeting.md` |
| Time Targeting | Schedule ads by day/hour | `docs/efficiency/timetargeting.md` |

## Keyword Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `""` | Exact word order | `"купить квартиру"` |
| excl. mark | Fixed word form | excl.купить (exact form) |
| `+` | Required word | `+в Москве` |
| `-` | Exclude word | `-бесплатно` |
| `[]` | Fixed word order | `[купить квартиру]` |

Full reference: `docs/keywords/symbols-and-operators.md`

## Retargeting Setup

1. Install Yandex Metrika on site
2. Create audience segments in Metrika or Audiences
3. Add retargeting conditions in ad group settings
4. Set bid adjustments for retargeting audiences

Details: `docs/impression-criteria/retargeting-lists.md`
