# Moderation Quick Reference

## General Rules

All ads in Yandex Direct must pass moderation. Key requirements:

- Ads must comply with Russian advertising law (Federal Law No. 38-FZ)
- Content must be truthful and not misleading
- Landing page must match the ad content
- Required disclaimers for regulated industries

Full rules: `docs/moderation/adv-rules.md`

## Technical Limits

| Element | Limit |
|---------|-------|
| Title 1 | 56 characters |
| Title 2 | 30 characters |
| Ad text | 81 characters |
| Display URL | 20 characters |
| Quick links | 8 per ad, 30 chars each |
| Clarifications | 25 chars each, 4 per ad |
| Image | 450x450 min, 5MB max |

Full limits: `docs/moderation/technical-restrictions.md`

## Special Categories (60+)

Located in `docs/moderation/categories/`. Key categories:

| Category | File | Required Documents |
|----------|------|--------------------|
| Finance / Banking | `finance.md` | Banking license |
| Insurance | `insurance.md` | Insurance license |
| Medical services | `medicine.md` | Medical license |
| Pharma / Drugs | `drugs.md` | Registration certificate |
| Alcohol | `alcohol.md` | Restricted, special rules |
| Real estate | `realty.md` | Developer declaration |
| Education | `education.md` | Education license |
| Gambling | `gambling.md` | Mostly prohibited |
| Crypto | `crypto.md` | Restricted |

## Common Rejection Reasons

1. Missing required disclaimers
2. Landing page doesn't match ad
3. Prohibited product/service
4. Missing license/certificate documentation
5. Age restriction marker not set
6. Comparative/superlative claims without proof

## Age Restrictions

- 0+ — general audience
- 6+ — mild scary content
- 12+ — moderate violence references
- 16+ — tobacco, military topics
- 18+ — adult content, alcohol, gambling

Details: `docs/moderation/age-alerts.md`
