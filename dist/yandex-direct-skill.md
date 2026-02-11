# Яндекс Директ — Полный справочник для AI-агентов
> 509 статей документации Яндекс Директа. Февраль 2026.
> Telegram: https://t.me/pomogay_marketing
> GitHub: https://github.com/VKirill/yandex-direct-docs

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

---

# Campaign Types Quick Reference

## Decision Tree

```
Selling products from catalog/feed?
  ├── Simple setup needed → Product Campaign
  └── Advanced settings needed → UPC with product ads

Running performance ads (search + display)?
  → Unified Performance Campaign (UPC)

Quick campaign, no expertise?
  → Campaign Master

Display/awareness campaign (CPM)?
  ├── Standard display → CPM Campaign
  ├── Video → Video Ads / Video Banners
  ├── Homepage banner → Frontpage Ads
  └── Smart TV → Connected TV

Promoting mobile app?
  → Mobile Apps Campaign

Promoting local business?
  → Company Ads

Advertising in Telegram?
  → Telegram Ads

Outdoor digital screens?
  → DOOH
```

## Comparison

| Type | Billing | Placements | Complexity |
|------|---------|-----------|------------|
| UPC | CPC/CPA | Search + YAN + Maps | High |
| Campaign Master | CPC/CPA | Search + YAN | Low |
| Product Campaign | CPC/CPA | Search + YAN | Medium |
| CPM Campaign | CPM | YAN + partners | Medium |
| Video Ads | CPM | Video network | Medium |
| Telegram Ads | CPM | Telegram channels | Low |
| Mobile Apps | CPC/CPA/CPI | Search + YAN + apps | High |
| Company Ads | CPC | Maps + Search | Low |

## Key Paths

- UPC: `docs/unified-performance-campaign/`
- Campaign Master: `docs/campaign-master/`
- Product: `docs/product-campaign/`
- CPM: `docs/products-cpm-campaign/`
- Telegram: `docs/telegram-ads/`
- Mobile: `docs/products-mobile-apps-ads/`

---

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

---

# Strategies Quick Reference

## Decision Tree

```
Need conversions at target CPA?
  → Max Conversions (average-cpa.md)

Need maximum traffic?
  → Max Clicks (average-cpc.md)

Need to optimize ROAS / profitability?
  → Max Profit (maximum-profit.md)

Need full control over individual bids?
  → Manual Bidding (manual-strategy.md)

Managing multiple campaigns with shared budget?
  → Portfolio Strategy (portfolio-strategy.md)
```

## Strategy Comparison

| Strategy | Billing | Optimization | Best For |
|----------|---------|-------------|----------|
| Max Conversions | CPA/CPC | Target CPA | Lead gen, e-commerce |
| Max Clicks | CPC | Max traffic | Awareness, new sites |
| Max Profit | ROAS | Profitability | E-commerce with margins |
| Manual | CPC | Manual bids | Expert advertisers |
| Portfolio | Mixed | Cross-campaign | Agencies, multi-campaign |

## Key Files

- Overview: `docs/strategies/select-strategy.md`
- Budget rules: `docs/strategies/budgets-in-strategies.md`
- Goal priorities: `docs/strategies/priority-goals.md`

---

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

---

# Документация по разделам

<!-- docs/unified-performance-campaign/about.md -->

# Единая перфоманс-кампания

- [Преимущества](../unified-performance-campaign/about.md#benefits)
- [Типы объявлений в ЕПК](../unified-performance-campaign/about.md#zoo)
- [Ответы на распространенные вопросы](../unified-performance-campaign/about.md#q-a)
- [Кейсы и полезные материалы](../unified-performance-campaign/about.md#kejsy-i-poleznye-materialy)

Единая перфоманс-кампания (ЕПК) — это инструмент для специалистов по продвижению в Поиске, Картах и Рекламной сети Яндекса, который позволяет комплексно решать перфоманс-задачи в рамках одной кампании с помощью гибких настроек.

Объявления показываются в результатах поиска и в Рекламной сети Яндекса, на десктопах, планшетах и мобильных телефонах.

## Преимущества

Общая структура интерфейса:

- На уровне кампании задаются общие настройки: места показа (поиск, Рекламная сеть и Карты или только определенные площадки, телеграм-каналы), стратегия, сроки проведения кампании, расписание и дополнительные настройки, которые можно применить для всех групп.
- На уровне группы задаются таргетинги на целевую аудиторию: география показов, автотаргетинг, тематические слова, интересы и привычки, сегменты аудитории, сценарий группы, тип контента площадок, а также настройки, которые можно применить для всех объявлений в группе.
- На уровне объявлений есть все для работы с их внешним видом: выбор типа объявления, поля для загрузки текстов, изображений, видео, быстрых ссылок, уточнений, контактных данных и других дополнительных элементов. А для товарных объявлений и страниц каталога — загрузка фидов и настройка фильтров. Здесь же доступен их предпросмотр.

## Типы объявлений в ЕПК

В одной кампании могут быть разные объявления. Мы рекомендуем создавать как можно больше вариантов, чтобы показываться на всех доступных площадках.

|  |  |
| --- | --- |
| **Товарное** | |
|  | Автоматические объявления для товарных предложений — создаются под каждый товар или услугу, которые вы хотите продвигать, с сайта или из фида.  Показываются на [поиске](../general/positions.md) и в [сетях](../general/yan.md).  [Как создать товарное объявление](../unified-performance-campaign/create-product.md) |
| **Страницы каталога** | |
|  | Автоматические объявления для страниц каталога — создаются под раздел с товарами или услугами, которые вы хотите продвигать, с сайта или из фида.  Показываются на [поиске](../general/positions.md) и в [сетях](../general/yan.md).  [Как создать объявление для страниц каталога](../unified-performance-campaign/create-catalogs.md) |
| **Текстово-графическое** | |
|  | **Текстово-графическое с текстом**    Объявление будет состоять из заголовка, текста объявления и ссылки на продвигаемый сайт. Заголовки и тексты объявлений должны заинтересовать пользователя или предложить решение его задачи.  Показываются на [поиске](../general/positions.md) и в [сетях](../general/yan.md).  [Как создать текстово-графическое объявление](../unified-performance-campaign/create-text-image.md) |
|  |  |
|  | **Текстово-графическое с изображением или каруселью**    Правильно подобранные изображения привлекают к объявлению больше внимания и помогают быстрее понять суть предложения.  Объявления с изображениями показываются в [сетях](../general/yan.md).  [Как добавить изображения](../efficiency/images.md) или [слайды карусели](../efficiency/carousel.md) |
|  |  |
|  | **Текстово-графическое с видео**    Превратите ваши объявления в видеорекламу с оплатой за клик. Снимите свой видеоролик и загрузите его при создании объявления.  Объявления с видео размещаются в [видеосети](../general/yan.md#partner-video) и других подходящих площадках Рекламной сети Яндекса в блоках OutStream и InStream. Пропустить видео можно с 5-й секунды.  [Как добавить видео](../efficiency/video.md) |
| **Комбинаторное объявлениеβ** | |
|  | Вы указываете несколько заголовков, текстов, изображений и видео, а Директ составляет из них множество баннеров.  Комбинаторные объявления могут показываться на [поиске](../general/positions.md) и в [сетях](../ge

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/about.md]*


---

<!-- docs/unified-performance-campaign/create-text-image.md -->

# Создание текстово-графического объявления

- [Модерация объявлений и запуск кампании](../unified-performance-campaign/create-text-image.md#section_vf4_c1h_yz)
- [Особенности настройки объявлений для продвижения товаров на маркетплейсах](../unified-performance-campaign/create-text-image.md#sales-on-marketplaces)

1. В поле **Ссылка в объявлении** укажите адрес страницы сайта, на которую будет вести ваше объявление или выберите [лендинг](../efficiency/landing.md). Сайт должен соответствовать тексту объявления и отвечать [требованиям Яндекса](../moderation/ad-rules.md#corresponding).
2. Опишите свое предложение, его преимущества или особенности:

   - Сгенерируйте объявление с помощью нейросетей. На основе продвигаемой страницы Директ создаст до шести вариантов объявлений с помощью различных генеративных алгоритмов и моделей Яндекса, например, YandexGPT, которая формирует заголовок и текст объявления, и YandexArt — для создания изображений.

     Выберите подходящее объявление. Если надо, отредактируйте его:

     - Измените заголовок и текст объявления от нейросети или придумайте свой. Опишите свое предложение, его преимущества или особенности. Ознакомьтесь с нашими [рекомендациями по составлению объявления](../efficiency/text-and-title.md).
     - Откадрируйте изображение, предложенное нейросетью. Или [замените его](../efficiency/images.md) на свое. Анимация изображения будет добавлена автоматически. Для объявлений, которые будут показываться в товарной галерее, также укажите [цену](../efficiency/price.md).
   - Добавьте собственный текст, заголовок и [изображение](../efficiency/images.md). Анимация изображения будет добавлена автоматически.

     Используйте [ИИ-редактор креативов](../products-image-ads/editor.md), чтобы сгенерировать и отредактировать изображение по текстовому описанию.

   Ознакомьтесь с нашими [рекомендациями по составлению объявления](../efficiency/text-and-title.md).

   Для объявлений, которые будут показываться в товарной галерее, также укажите [цену](../efficiency/price.md).
3. Объявление можно сделать более заметным и информативным — в блоке **Видео** добавьте файл с видеороликом или используйте видеоролик из галереи. [Подробнее](../efficiency/video.md).

   [ИИ-редактор креативов](../products-image-ads/editor.md) поможет создать видео на основе изображения.
4. Включите [карусель](../efficiency/carousel.md) изображений — способ показать товар или услугу в объявлении с разных сторон, рассказать, как они создаются, подробнее показать их преимущества или особенности. К объявлению можно добавить от 2 до 10 изображений в заданном порядке.
5. Проверьте [контактные данные](../efficiency/vcards.md) компании.
6. Настройте [кнопку действия](../efficiency/button.md) — она привлекает внимание и побуждает пользователей взаимодействовать с вашим объявлением. Кнопка дополняет объявление с изображением или видео еще одной ссылкой.
7. Опишите преимущества и особенности с помощью [уточнений](../efficiency/callout.md).
8. Укажите короткий путь к важной информации на сайте с помощью [быстрых ссылок](../efficiency/quick-links.md).

Заполняйте все элементы объявления, в том числе дополнительный заголовок. Директ использует их для разных вариантов креативов, в том числе разных трафаретов в поиске.

Яндекс как оператор рекламных данных при создании кампании присваивает каждому креативу уникальный идентификатор — токен. Затем по этому токену агрегирует всю информацию по размещению и передает в Единый реестр интернет-рекламы (ЕРИР). Подробнее о [маркировке рекламы](https://yandex.ru/adv/ad-labeling).

## Модерация объявлений и запуск кампании

После создания ваше объявление будет проверено на соответствие [установленным требованиям](../moderation/adv-rules.md). Нажмите кнопку **Отправить на модерацию** и подтвердите свое согласие с условиями [оферты](https://yandex.ru/legal/oferta_direct/), на основании которой Яндекс размещает ваши объявления. Обычно модераторы проверяют объявление в течение нескольких часов. В выходные и п

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/create-text-image.md]*


---

<!-- docs/unified-performance-campaign/create-product.md -->

# Создание товарного объявления

- [Модерация объявлений и запуск кампании](../unified-performance-campaign/create-product.md#section_vf4_c1h_yz)
- [Особенности настройки объявлений для продвижения товаров на маркетплейсах](../unified-performance-campaign/create-product.md#sales-on-marketplaces)
- [Вопросы и ответы](../unified-performance-campaign/create-product.md#voprosy-i-otvety)
  - [Не формируются товарные объявления](../unified-performance-campaign/create-product.md#ne-formiruyutsya-tovarnye-obuyavleniya)

В группу можно добавить **только одно** активное товарное объявление. Чтобы разместить другое товарное объявление, остановите и архивируйте текущее, затем создайте новое.

Создавать объявления можно на основе данных сайта или фида. Если у вас сайт с товарами, то подойдут оба способа, если вы продвигаете услуги, курсы, билеты или другие нетоварные тематики — предпочтительнее [фид](../feeds/about.md). Использование фида позволяет получить больше информации о каждой позиции в предложении и точнее настроить правила отбора. Также можно добавить товары вручную.

Товарные объявления можно создать для любых категорий товаров, кроме указанных в [требованиях](../moderation/restricted-categories.md).

1. В блоке **Товары** выберите источник информации для объявлений:

   Новый фид по сайту

   Новый фид по ссылке или с компьютера

   Ручное управление товарами

   Яндекс автоматически найдет товары на вашем сайте и создаст объявление для каждого товара. Если товары не найдены, проверьте, что ваш сайт соответствует [требованиям](../unified-performance-campaign/structure-of-site.md).

   Если у вас уже есть фид с актуальными ценами и списком товаров, то используйте его. Это может быть один из ранее загруженных товарных фидов или новый фид, добавленный через ссылку или с помощью загрузки с устройства.

   1. Добавьте ссылку на фид или выберите файл с фидом.

      Формат файла зависит от выбранного типа фида. Также введите свой логин и пароль, если они требуются для доступа по ссылке.
   2. Нажмите **Загрузить фид**.

   Рекламно-информационные материалы, передаваемые вами, в том числе данные фида (название товара, изображение, цена, описание), могут быть использованы для размещения информации о ваших предложениях в различных сервисах Яндекса. Это бесплатно. Если хотите отказаться, напишите в [отдел клиентского сервиса](../unified-performance-campaign/create-product.md#questions).

   Вы можете добавить описание товаров вручную. Для каждого товара заполните карточку:

   - Укажите ссылку на товар, добавьте название и описание.
   - Добавьте до 5 изображений размером от 450 × 450 пикселей и объемом до 10 МБ.
   - Укажите цену и сведения: категорию, производителя, модель и наличие.

   Все добавленные товары будут собраны в один фид на логин. Всего можно добавить до 1000 товаров разных категорий.

   Все описания и изображения должны соответствовать [требованиям](../moderation/ad-rules.md).
2. В блоке **Фильтр** укажите какие товары использовать, а какие исключить при генерации объявлений. Условия объединяются оператором «И», для показа будут выбраны товары, которые соответствуют всем заданным условиям.

   Также можно использовать в фильтрах [кастомные элементы](../feeds/requirements-yml.md).

   При настройке параметров фильтра Директ в режиме реального времени проверяет, сколько предложений соответствует выбранным критериям. Подсказка поможет избежать ситуации, когда под условия фильтра не попадает ни один товар и показы объявлений не идут.

   Пример
3. Для товаров с сайта в блоке **Тексты** напишите текст по умолчанию — он будет общим для всех объявлений, а заголовок объявления будет сгенерирован автоматически.

   Если вы используете файл с фидом или загружаете информацию о товарах вручную, выберите, как использовать элементы фида :

   - **автоматические** — заголовок будет сгенерирован автоматически, а объявление будет составлено из текста, который указан в поле **Текст по умолчанию**.
   - **ручные** — укажите элементы из фид

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/create-product.md]*


---

<!-- docs/unified-performance-campaign/create-comb-ad.md -->

Комбинаторное объявление<sup>β</sup>

# Комбинаторное объявлениеβ

- [Как настроить](../unified-performance-campaign/create-comb-ad.md#kak-nastroit)
- [Как оценить результаты](../unified-performance-campaign/create-comb-ad.md#kak-ocenit-rezultaty)

Комбинаторные объявленияβ — тип объявлений, где вы указываете несколько заголовков, текстов, изображений и видео, а Директ составляет из них множество баннеров.

Комбинаторные объявления позволяют оптимизировать работу специалистов с объявлениями:

- Упрощают и ускоряют настройку текстово-графических объявлений.

  Вместо создания множества отдельных объявлений с разными сообщениями, достаточно добавить как можно больше вариантов элементов в одно объявление. Из них автоматически сформируются баннеры, а нейротехнологии Яндекс Рекламы определят наиболее эффективный для каждого показа.
- Позволяют расширить охват и повысить конверсионность продвижения.

  Большее количество вариантов текстов, заголовков, изображений и видео в одном объявлении позволяет системе находить эффективные варианты для разных аудиторий и площадок. Это помогает увеличить охват и повысить вероятность конверсии.
- Адаптируются к разным площадкам.

  Благодаря загрузке нескольких изображений и видео с разным соотношением сторон на каждой площадке будут показываться наиболее подходящие креативы в нужных пропорциях.

#### Как работает

1. **Добавление элементов**. Добавьте в объявление несколько вариантов заголовков, текстов, изображений и видео.
2. **Формирование комбинаций**. Система автоматически создает различные сочетания элементов и формирует из них готовые объявления.
3. **Оптимизация показов**. Нейротехнологии Яндекс Рекламы в реальном времени оценивают эффективность каждой комбинации и выбирают наиболее подходящий вариант для каждого показа.

## Как настроить

1. В Единой перфоманс-кампании выберите тип объявления — Комбинаторноеβ.

   В одну группу можно добавить до 3 неархивных комбинаторных объявленийβ и до 10 объявлений этого типа с учетом архивных.
2. Укажите ссылку на продвигаемую страницу.
3. Добавьте до 7 заголовков и до 3 текстов — вручную или с помощью опции **Сгенерировать заголовки и тексты**.

   Совет

   Добавьте максимальное количество заголовков и текстов и сделайте их разнообразными. Директ подберет подходящую аудиторию для каждого варианта объявления, а вы заинтересуете больше потенциальных клиентов. Чтобы повысить эффективность заголовков и текстов, используйте опцию **Оптимизировать текст объявлений под запрос**.
4. Загрузите до 5 изображений. В блоке предпросмотра можно увидеть, как они будут выглядеть с разным соотношением сторон, и при необходимости скорректировать [смарт-центры](../efficiency/carousel.md#smart-center) для каждого изображения.

   Используйте [ИИ-редактор креативов](../products-image-ads/editor.md), чтобы сгенерировать и отредактировать изображение по текстовому описанию.
5. Добавьте до 6 вариантов видео. [ИИ-редактор креативов](../products-image-ads/editor.md) поможет создать видео на основе изображения.

   Совет

   Загружайте как можно больше видео, чтобы лучше раскрыть предложение и повысить конверсионность продвижения. Согласно экспериментам, объявления с видео позволяют охватить в среднем 7% дополнительной целевой аудитории. Загружайте видеоролики с разным соотношением сторон (например, 16 : 9, 4 : 5, 1 : 1). Это поможет системе подобрать формат для показа на разных площадках и устройствах, увеличив охват.

   Чем больше заголовков, текстов, изображений и видео вы добавите, тем больше баннеров сформирует Директ и тем больше пользователей вы сможете охватить.
6. Заполните дополнительные поля: контакты, уточнения, быстрые ссылки, цену или промоакцию. Эти элементы могут быть показаны в составе объявления в зависимости от формата и площадки.

Примечание

Комбинаторные объявленияβ доступны в [Директ Коммандере](https://yandex.ru/support/direct-commander-new/ru/). Управлять их настройками также можно с помощью [файлов формата XLS и XLSX](../alternative-interfaces/xls

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/create-comb-ad.md]*


---

<!-- docs/unified-performance-campaign/create-catalogs.md -->

# Создание страниц каталога

- [Модерация объявлений и запуск кампании](../unified-performance-campaign/create-catalogs.md#section_vf4_c1h_yz)
- [Вопросы и ответы](../unified-performance-campaign/create-catalogs.md#voprosy-i-otvety)
  - [Не формируются объявления для страниц каталога](../unified-performance-campaign/create-catalogs.md#ne-formiruyutsya-obuyavleniya-dlya-stranic-kataloga)

В группу можно добавить **только одно** активное объявление для страниц каталога. Объявления для страниц каталога можно настроить на основе:

- Сайта — только для товаров.
- Фида — для товаров (YML-фид) и тематик «Авто» и «Недвижимость» (XML-фид).
- CSV-файла — для всех тематик, которые можно продвигать в Директе.

1. Укажите источник для создания объявлений:

   Страницы каталога, найденные на сайте

   Фид по ссылке или с компьютера

   Робот Яндекса обходит страницы каталога на сайте. Чтобы робот точно определил страницы каталога, они должны быть размечены специальной строгой микроразметкой.

   Объявления для страниц каталога, найденных на сайте, можно сгенерировать только для товаров.

   - **CSV-файл**

     CSV-файл можно использовать для генерации объявлений для страниц каталога с любыми товарами и услугами, которые можно продвигать в Директе. В одну группу можно загрузить только один файл.

     **Требования к файлу**

     - Формат CSV с кодировкой UTF-8.
     - Запятая «,» или точка с запятой «;» в качестве разделителя.
       Если вы используете запятую в качестве разделителя, проверьте, что в тексте одного поля не встречается запятая. Если она есть, то весь текст этого поля нужно передавать в кавычках. Например: `"Молочные, растительные напитки"`.
     - В шапке файла должен быть перечислен весь набор столбцов: Url, Title, Description, Offer minimal price, Currency, Image url 1, Image url 2, Image url 3, Image url 4, Image url 5.

       Название и описание полей

       |  |  |
       | --- | --- |
       | **Название** | **Описание** |
       | Url | Ссылка на страницу каталога на сайте. Каждая ссылка должна быть уникальна. Обязательное поле. |
       | Title | Название каталога. До **56 символов**, включая пробелы и знаки препинания. Обязательное поле. |
       | Description | Описание. **До 81 символа**, включая пробелы, и до 15 знаков препинания. Рекомендуем указать. |
       | Offer minimal price | Минимальная цена товара в категории. Целое число, без разделителя. Если число дробное, округлите до целого. Например: 150000. |
       | Currency | Валюта, в которой указывается цена товара. Буквенный код, например, RUB, USD, EUR. Обязательное поле, если заполнено поле Offer minimal price. |
       | Image url 1, Image url 2, Image url 3, Image url 4, Image url 5 | Ссылки на изображение на сайте. Ссылка должна вести на саму картинку, а не на страницу, где ее можно скачать. Например, ссылка на Яндекс Диск не подойдет. Рекомендуем указать. |
     - Ограничение по количеству строк — 1000.

     **Как создать CSV-файл**

     Заполните данные в любом редакторе таблиц, например, Excel или Numbers. Сохраните файл в формате CSV с разделителем - запятой.

     В Excel (Windows)

     1. В верхнем меню выберите **Файл** → **Сохранить как**.

     2. Введите название файла в поле **Сохранить как**.

     3. Выберите **Формат файла** «Текст с разделителем запятой (.CSV)»

     4. Нажмите **Сохранить**.

     В Numbers (iOS)

     1. В верхнем меню выберите **File** → **Export to** → **CSV...**

     2. В окне **Export Your Spreadsheet** на вкладке **CSV** раскройте **Advanced Options**.

     3. В поле **Text Encoding** выберите «Unicode (UTF-8)»

     4. Нажмите **Next...**

     **Возможные ошибки при загрузке файла**

     - Неверная кодировка — проверьте, что ваш файл в кодировке UTF-8.
     - Файл не может быть пустым — проверьте, что ваш файл содержит строки с каталогами.
     - Список не может быть больше 1000 строк — проверьте, что ваш файл содержит менее 1000 строк.
     - Поле не должно быть пустым — проверьте, что все обязательные

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/create-catalogs.md]*


---

<!-- docs/unified-performance-campaign/upgrade-to-UPC.md -->

# Обновление до Единой перфоманс-кампании

- [Как устаревшие типы кампаний обновляются до ЕПК](../unified-performance-campaign/upgrade-to-UPC.md#kak-ustarevshie-tipy-kampanij-obnovlyayutsya-do-epk)
- [Настройки кампаний, которые изменятся после обновления](../unified-performance-campaign/upgrade-to-UPC.md#whats-new)

## Как устаревшие типы кампаний обновляются до ЕПК

**Кампания «Текстово-графические объявления»**
:   После обновления кампания станет Единой перфоманс-кампанией с группами текстово-графических объявлений. Количество групп и все основные настройки сохранятся. Места показа будут такие же, как и в кампании до обновления.

**Кампания «Динамические объявления»**
:   После обновления кампания станет Единой перфоманс-кампанией с группами, в которых будет по [одному активному товарному объявлению](../unified-performance-campaign/upgrade-to-UPC.md#do-ads). Места показа — такие же, как и в кампании до обновления: поисковая выдача и/или Товарная галерея.

**Кампания «Смарт-баннеры»**
:   После обновления кампания станет Единой перфоманс-кампанией с группами, в которых будет по одному активному товарному объявлению. Места показа — только Рекламная сеть Яндекса.

Полный список изменений, связанных с устаревшим функционалом, размещен в разделе [Настройки кампаний, которые изменятся после обновления](../unified-performance-campaign/upgrade-to-UPC.md#whats-new).

## Настройки кампаний, которые изменятся после обновления

**Тип объявления «Мобильное» в кампании «Текстово-графические объявления»**
:   Объявления для мобильных как отдельный тип не поддерживается в ЕПК. При обновлении они станут текстово-графическими, в том числе и архивные объявления.

    Если необходимо, перенесите их в отдельную группу и настройте для нее [корректировку по устройствам](ru/impressions/bids-adjustment.dita#devices).

**Турбо-страницы/Турбо-сайты**
:   При создании или редактировании объявлений Турбо-сайт/Турбо-страницы можно было добавить к ссылке перехода на основной сайт или [быстрой ссылке](../efficiency/quick-links.md). В ЕПК данный функционал не поддерживается.

    При обновлении до ЕПК Турбо-сайт/Турбо-страницы будут заменены ссылкой на сайт, в том числе и в архивных объявлениях. Если сайт не указан, то они будут сконвертированы в ссылку. Эта ссылка будет добавлена в настройки объявления, где были указаны турбо-страницы (страница перехода или быстрые ссылки).

**Виртуальная визитка**
:   В ЕПК визитки не поддерживаются. Вместо них лучше использовать данные организации в Яндекс Бизнесе. После обновления данные визиток, которые указаны вместе с данными организации, удалятся автоматически, а контактная информация в объявлении будет подтягиваться из данных организации в Яндекс Бизнесе.

    Данные визитки будут изменены на данные организации и в случае, если изначально были указаны и визитка, и контакты организации, но в блоке **Контакты в объявлении** опция **Использовать контакты организации в объявлении** была выключена.

    Если в объявлении была указана только виртуальная визитка без указания страницы перехода и контактов организации, то из такого объявления виртуальная визитка будет удалена. Объявление будет обновлено: его можно будет разархивировать и запустить, но его показов не будет (будет указан соответствующий статус). Чтобы начались показы, в объявление необходимо добавить новую страницу перехода. Также нельзя что-то изменить в нем без указания страницы перехода.

**Стратегия «Рентабельность инвестиций»**
:   Если вы использовали стратегию «Рентабельности инвестиций», при обновлении она изменится на [Максимум конверсий](../strategies/average-cpa.md) с ограничением по доле рекламных расходов (ДРР) — настройки бюджета сохранятся, а ROI пересчитается в ДРР по формуле:

    ДРР = (1 / (ROI + 1)) × 100%

    Изменение стратегии не повлияет на текущую эффективность вашей кампании. Вы можете выбрать другие параметры стратегии в настройках — до или после обновления кампании.

####

**Объявления в группах кампаний «Динамические объявления

*[Статья сокращена. Полная версия: docs/unified-performance-campaign/upgrade-to-UPC.md]*


---

<!-- docs/campaign-master/about.md -->

# Мастер кампаний

- [Какие задачи решает](../campaign-master/about.md#kakie-zadachi-reshaet)
- [Преимущества](../campaign-master/about.md#preimushestva)
- [Виды размещений](../campaign-master/about.md#vidy-razmeshenij)
- [Рекомендации](../campaign-master/about.md#rekomendacii)
- [Вопросы и ответы](../campaign-master/about.md#voprosy-i-otvety)

Мастер кампаний — это простой и быстрый способ разместить объявления в Директе. Достаточно указать ссылку на продвигаемую страницу сайта или написать пару предложений о своем деле, если сайта нет. На каждом шаге создания объявления Мастер подсказывает настройки, тематические слова, тексты и картинки.

Мастер предлагает несколько вариантов бюджета для запуска кампании.

После запуска кампании Мастер предоставляет понятную статистику кликов и заявок, чтобы вы могли отслеживать, как расходуется ваш бюджет.

Создавать кампании и управлять ими можно как с компьютера, так и с мобильного устройства. Чтобы в мобильной версии перейти к меню навигации, в правом верхнем углу нажмите ваш аватар.

## Какие задачи решает

С помощью Мастера кампаний вы можете:

- Создать кампанию для продвижения сайта — [Конверсии и трафик](../campaign-master/site.md).
- Создать кампанию, если сайта нет, — [Продвижение без сайта](../campaign-master/without-site.md).
- Создать кампанию для продвижения товаров — [Товарная кампания](../campaign-master/product-campaign.md).
- Создать кампанию для [продвижения телеграм-канала](../campaign-master/telegram.md).
- Создать кампанию для продвижения товаров на маркетплейсе — [Продажи на маркетплейсах](../campaign-master/sales-on-marketplaces.md).

## Преимущества

На основе информации с сайта или описания вашего бизнеса, если сайта нет, Мастер кампаний автоматически:

- сгенерирует объявления;
- подберет целевую аудиторию;
- определит подходящее время и площадки для показа объявлений.

## Виды размещений

Мастер кампаний покажет объявления:

В поиске

В РСЯ

В Яндекс Картах

В результатах поиска Яндекса, когда пользователи ищут товары и услуги, похожие на ваши.

На сайтах-партнерах Рекламной сети Яндекса. Ваши объявления увидят те, кто уже интересовался похожими товарами и услугами. При клике по объявлению пользователи смогут легко перейти на ваш сайт и оформить заказ.

- В Яндекс Картах карточка организации будет показываться выше в результатах поиска.
- В карточке организации появится особая зеленая метка, а в Картах значок заведения вместо синего станет зеленым.
- Потенциальные клиенты, которые ищут товары или услуги рядом с вами, будут чаще видеть вашу организацию и с большей вероятностью обратятся к вам.

#### Продвижение постов в Яндекс Ритме

Если у вас есть посты в Яндекс Ритме, в которых ссылка совпадает со ссылкой в настройках кампании, то эти посты также будут продвигаться — они будут показываться в ленте Яндекс Ритма и на главной странице [ya.ru](http://ya.ru/) чаще и на более высоких позициях.

Подробнее о [продвижении постов](https://yandex.ru/support2/rythm/ru/buisness/promotion) в Справке Яндекс Ритма.

## Рекомендации

**Если вы знаете, сколько готовы платить за переходы по объявлению**

Для получения большего количества переходов по вашему объявлению на этапе создания кампании в разделе **Цель рекламы** выберите стратегию «Максимум переходов». Директ автоматически будет оптимизировать кампанию для увеличения кликов по вашему объявлению, удерживая заданные условия стоимости клика.

**Если вам важно достижение целевых действий посетителем**

Если вы хотите получить максимальное количество достижений целевых действий, например обращений в мессенджер, заполнения форм на сайте или добавления товара в корзину, в разделе **Цель рекламы** выберите стратегию «Максимум целевых действий».

## Вопросы и ответы

**Настройка**

Как в новых кампаниях с оплатой за конверсии убрать нежелательные запросы

На странице статистики вы можете отключить показы для неэффективных фраз. Также вы можете добавить фразы с [минус-словами](../keywords/negative-keywords.md) при создании или на

*[Статья сокращена. Полная версия: docs/campaign-master/about.md]*


---

<!-- docs/product-campaign/create.md -->

# Создание и настройка

- [Шаг 1. Создайте кампанию](../product-campaign/create.md#shag-1-sozdajte-kampaniyu)
- [Шаг 2. Настройте объявления для товаров](../product-campaign/create.md#shag-2-nastrojte-obuyavleniya-dlya-tovarov)
- [Шаг 3. Настройте объявления для страниц каталога](../product-campaign/create.md#catalog)
- [Шаг 4. Настройте объявление про ваш магазин](../product-campaign/create.md#shag-4-nastrojte-obuyavlenie-pro-vash-magazin)
- [Шаг 5. Объявления от нейросети](../product-campaign/create.md#ad-neuro)
- [Шаг 6. Определите аудиторию](../product-campaign/create.md#shag-6-opredelite-auditoriyu)
- [Шаг 7. Определите бюджет и цели кампании](../product-campaign/create.md#shag-7-opredelite-byudzhet-i-celi-kampanii)

Товарная кампания стремится принести максимум целевых действий. Перед созданием Товарной кампании [установите](https://yandex.ru/support/metrica/general/creating-counter.html) счетчик Яндекс Метрики на ваш сайт, настройте цели и убедитесь, что у аккаунта в Директе есть доступ к этому счетчику.

## Шаг 1. Создайте кампанию

1. Нажмите **Добавить** → **Кампанию**.
2. На вкладке **Мастер кампаний** выберите **Товарная кампания**.
3. Укажите ссылку на страницу интернет-магазина.
4. Директ подтянет информацию об организации в Яндекс Бизнесе. Если организации еще нет, вы можете добавить ее. Почему это важно, читайте в статье [Зачем добавлять организацию в Яндекс Бизнес](https://yandex.ru/adv/edu/materials/kak-rabotat-s-organizaciyami-iz-biznesa-v-direkte).
5. Если у вас есть офлайн-точка продаж, куда могут прийти клиенты, включите опцию **Продвижение организации из Яндекс Бизнеса**. Так вы сможете использовать форматы для продвижения в Картах. Подробнее читайте в [статье о продвижении в Яндекс Картах](https://yandex.ru/adv/news/reklama-v-kartah-v-direct).

## Шаг 2. Настройте объявления для товаров

1. Выберите способ добавления товаров в кампанию.

   Товары, найденные на сайте

   Новый фид

   Ручное управление товарами

   Самый простой способ генерации объявлений. Алгоритмы Директа найдут товары на указанном сайте. Информация в объявлениях будет обновляться автоматически. Если товары не найдены, проверьте, что ваш сайт соответствует [требованиям](../unified-performance-campaign/structure-of-site.md).

   Фид с компьютера или по ссылке. Подходит для магазинов с большим ассортиментом, который часто обновляется. Объявления для товаров Директ будет генерировать на основе данных в фиде.

   Товарный фид — файл с информацией о товарах. Для продвижения интернет-магазинов рекомендуется использовать [YML-фид](../feeds/requirements-yml.md).

   - **Новый фид с компьютера**: выберите файл и задайте название фида. Если загружать фид файлом, то обновлять его потребуется вручную.
   - **Новый фид по ссылке**: укажите ссылку на файл, данные для авторизации (если необходимо) и задайте название фида. Если фид обновляется по ссылке, то информация в объявлениях также будет меняться автоматически.

   Подходит для магазинов с небольшим ассортиментом, который редко обновляется.

   Для каждого товара заполните карточку:

   - Укажите ссылку на товар, добавьте название и описание.
   - Добавьте до 5 изображений размером от 450 × 450 пикселей и объемом до 10 МБ.
   - Укажите актуальную и старую цены, категорию, производителя, модель и наличие.

   Все описания и изображения должны соответствовать [требованиям](../moderation/ad-rules.md).

   Все добавленные товары будут собраны в один фид на логин. Всего можно добавить до 1000 товаров разных категорий.
2. Выберите товары, которые хотите продвигать с помощью фильтров.

   Для каждого источника данных будут доступны свои фильтры. Условия объединяются оператором «И». Для показа будут выбраны товары, которые соответствуют всем заданным условиям.

   Когда вы генерируете объявления на основе фида и настраиваете фильтр для товаров, система в режиме реального времени проверяет, сколько товаров подходит под условие. Обращайте внимание на эту подсказку — она поможет избежать ситуации, когда 

*[Статья сокращена. Полная версия: docs/product-campaign/create.md]*


---

<!-- docs/telegram-ads/create.md -->

# Создание и настройка

Для рекламы в телеграм-каналах нужно создавать новые кампании. В существующих кампаниях изменить место показа на телеграм-канал невозможно.

### Шаг 1. Перейдите к созданию кампании и настройте ее параметры

1. Нажмите **Добавить** → **Кампанию**.
2. На вкладке **Режим эксперта** создайте кампанию одним из способов:

   - Выберите **Реклама в телеграм-каналах** → **Автоподбор каналов**.
   - Выберите **Единая перфоманс-кампания**. В блоке **Места показа рекламы** выберите **Телеграм-каналы**.

     После сохранения настроек кампании изменить место показа невозможно.

     Единые перфоманс-кампании с показами в телеграм-каналах нельзя объединять в рамках пакетной стратегии с другими кампаниями, в которых выбраны иные места показа.
3. Для рекламы в телеграм-каналах доступна только стратегия [Максимум кликов](../strategies/average-cpc.md), изменить ее на другую нельзя. Заполните обязательные поля: укажите недельный бюджет (от 300 рублей) и максимальную ставку (от 30 рублей).

### Шаг 2. Создайте группу объявлений. Выберите географию и тематики каналов

География показов — Россия, [Узбекистан](../telegram-ads/features.md#uz-features), [Казахстан](../telegram-ads/features.md#kz-features) и [Турция](../telegram-ads/features.md#tr-features).

Запуск рекламы в телеграм-каналах Беларуси в настоящее время находится в бета-тестировании. Чтобы принять в нем участие, напишите в [отдел клиентского сервиса](../telegram-ads/create.md#questions) и запросите доступ.

1. В блоке **География телеграм-каналов** укажите, в каналах каких регионов России показывать ваши рекламные посты-объявления. Каналы для размещения будут подбираться на основе содержимого ваших объявлений с учетом указанных регионов.

   Для максимального охвата рекомендуем выбрать всю Россию — так ваша реклама появится в том числе в каналах, которые не связаны с конкретными регионами.

   Чтобы не показывать рекламу в каналах конкретных регионов, лучше выбрать всю Россию и добавить исключения.

   Каналы чаще всего не привязаны к регионам. Выбор конкретных регионов может значительно уменьшить количество показов рекламы, так как исключит большинство каналов.

   > Например, ваша реклама связана с автомобилями:
   >
   > - Выбор России и отключение Москвы: реклама покажется в канале «Все об автомобилях», но не в «Все об автомобилях Москвы».
   > - Выбор только Москвы: реклама покажется в «Все об автомобилях Москвы», но не в «Все об автомобилях».
   > - Выбор России: реклама покажется в обоих каналах, обеспечивая максимальное количество показов.

   В Рекламе в телеграм-каналах есть каналы без привязки к региону, например, про новости экономики или мира кино, а есть и каналы, заточенные под специфику конкретного региона. Рекламодателям иногда важно обратиться именно к локальной аудитории.

   Алгоритмы Директа на основе статистических данных из переходов пользователей проверяют, из каких регионов целевая аудитория в канале. Это помогает повысить эффективность рекламы, направленной на локальных пользователей.

   > Например, вы создали рекламную кампанию для своего автосалона в Москве и задали регион показа — Москва. Ваша реклама будет показана не только в каналах, которые связаны названием с Москвой, но и в тех, в которых большинство подписчиков из Москвы.
   >
   > Таким образом, объявления будут показаны только той аудитории, которая сможет воспользоваться вашим рекламным предложением, так как большая часть подписчиков канала будет связана с выбранной настройкой геотаргетинга, и рекламу увидит ваша целевая аудитория.

   Регулярное местоположение определяется с помощью технологии [Крипта](../technologies-and-services/crypta.md) на основании переходов подписчиков канала.
2. В блоке **Тематика телеграм-каналов** по умолчанию выбраны показы по всем тематикам. Это дает максимальный охват аудитории. Если необходимо, измените на «Настроить вручную» и исключите из списка тематики телеграм-каналов, в которых не надо показывать рекламные посты. Вы можете выбрать как

*[Статья сокращена. Полная версия: docs/telegram-ads/create.md]*


---

<!-- docs/company-ads/create.md -->

# Как настроить продвижение организаций

Настройте продвижение в [Картах](../company-ads/maps.md) и в [списке организаций в результатах поиска](../company-ads/company-card.md). Такое продвижение поднимет карточку организации выше в результатах поиска и сделает объявление более заметным и информативным.

- [Настроить с Простым стартом](../company-ads/create-pa.md)
- [Настроить в Мастере кампаний](../company-ads/create-cm.md)
- [Настроить в Единой перфоманс-кампании](../company-ads/create-upc.md)

---

<!-- docs/products-mobile-apps-ads/about.md -->

# Продвижение приложений

Продвижение приложений — инструмент Директа, который позволяет продвигать iOS и Android приложения. С его помощью бизнесы, разработчики и паблишеры могут привлечь новых пользователей или вернуть тех, кто давно не заходил в приложение.

Продвижение доступно:

- [На мобильных устройствах и планшетах](../products-mobile-apps-ads/about-mobile.md).
- [На Connected TV и десктопах](../products-mobile-apps-ads/cross-platform/about.md).

Объявления показываются:

- На мобильных устройствах и планшетах – в результатах поиска и в Рекламной сети Яндекса.
- На Connected TV – в приложениях и браузерах на телевизорах, а также на Яндекс ТВ.
- На десктопах – в [видеосети](../general/yan.md#yan-partners) и Рекламной сети Яндекса.

Поддерживаются мобильные приложения из App Store, Google Play и RuStore.

## Какие задачи решает

---

<!-- docs/strategies/select-strategy.md -->

# Стратегии показов

- [Как работают стратегии](../strategies/select-strategy.md#how-it-works)
- [Как эффективно использовать стратегии](../strategies/select-strategy.md#how-to-use)
- [Адаптация стратегии к сезонному спросу](../strategies/select-strategy.md#adaptation)
- [Перезапуск стратегии](../strategies/select-strategy.md#restart)

Стратегия — это набор настроек, которые позволяют решить задачу кампании, например привлечь трафик на сайт, получить максимум полезных действий, оптимизировать рентабельность или увеличить прибыль от продвижения.

Управлять ставками можно с помощью автоматических алгоритмов, указав нужные параметры, или самостоятельно — вручную:

- При автоматическом управлении вы определяете, на какой результат должна быть нацелена стратегия. Например, привлечение посетителей на сайт, совершение полезных действий на сайте, целевая доля рекламных расходов. Исходя из задачи вы выбираете параметр для оптимизации — клики, конверсии или долю рекламных расходов. Дополнительно можно задать условия для достижения цели, например указать бюджет или среднюю цену, которую вы готовы заплатить за результат.
- При ручном управлении вы самостоятельно назначаете ставку для каждого условия показа и при необходимости ограничиваете средний дневной бюджет.

Мы рекомендуем использовать автоматические стратегии, так как они вносят корректировки в кампанию гораздо чаще, чем это возможно делать вручную или с помощью сторонних инструментов управления продвижением.

Выбрать стратегию показов можно на странице параметров кампании. Для каждой кампании можно выбрать только одну стратегию, которая будет работать для всех ее объявлений.

Доступные стратегии в зависимости от типа кампании

|  |  |
| --- | --- |
| **Тип кампании** | **Доступные стратегии** |
| «Единая перфоманс-кампания» | [Максимум конверсий](../strategies/average-cpa.md)  [Максимум кликов](../strategies/average-cpc.md)  [Максимум кликов с ручными ставками](../strategies/manual-strategy.md)  [Максимум прибылиβ](../strategies/maximum-profit.md)  Подробнее о том, как выбрать [стратегию для оптимизации по целям](https://yandex.ru/adv/news/optimizatsiya-konversiy-i-optimizatsiya-rentabelnosti-kak-nastroit-avtostrategii-v-direkte#algorithm). |
| «Продвижение приложений» | [Оптимизация конверсий](../strategies/average-cpa-mobile-apps.md) (для приложений с трекинговой ссылкой)  [Оптимизация кликов](../strategies/optimize-clicks-mobile-apps.md) |
| «Баннер на поиске» | [Оптимизация кликов для баннера на поиске](../strategies/optimize-number-of-clicks-mcb.md)  [Максимум кликов с ручными ставками](../strategies/manual-strategy.md) |

## Как работают стратегии

Все стратегии Директа основаны на специальном математическом алгоритме, который прогнозирует вероятность перехода по объявлению и достижения целевого действия на сайте.

При построении прогноза система анализирует статистику по ключевым фразам, подобранным к объявлению. Для поисковых площадок она учитывает данные по показам на поиске Яндекса, а для тематических — данные по показам в сетях (РСЯ и внешние сети). Если статистики недостаточно, используется база аналогий и информация о переходах из поиска Яндекса. Также учитывается поведение пользователей, кликающих на объявления. Система отбирает наиболее эффективные фразы — те, по которым на сайт приходят будущие клиенты — и активнее показывает объявления именно по ним.

Прогноз строится по часам для каждого дня недели, чтобы учесть зависимость количества показов, кликов и целевых действий от времени суток и дня недели. В процессе размещения прогноз регулярно пересчитывается по свежим данным.

В стратегии по умолчанию встроена защита от перетрат. В стратегиях с оплатой за клики система не может потратить за день более 35% недельного бюджета. В любой стратегии ставка никогда не поднимается выше 10% от недельного бюджета, если не настроены корректировки ставок.

- При срабатывании повышающей корректировки ставка может быть более 10% от недельного бюджета.
- Если показы ограничены време

*[Статья сокращена. Полная версия: docs/strategies/select-strategy.md]*


---

<!-- docs/strategies/average-cpa.md -->

# Максимум конверсий

- [Принцип работы](../strategies/average-cpa.md#how-it-works)
- [Условия подключения](../strategies/average-cpa.md#conditions)
- [Модель оплаты](../strategies/average-cpa.md#payment)
- [Как вычислить оптимальную цену конверсии](../strategies/average-cpa.md#tips)
  - [Оценка статистической значимости результатов при оплате за клики](../strategies/average-cpa.md#ocenka-statisticheskoj-znachimosti-rezultatov-pri-oplate-za-kliki)
- [Отчет о конверсиях](../strategies/average-cpa.md#konv-report)

Стратегия позволяет получить максимум *целевых визитов* на сайт, удерживая заданную долю рекламных расходов, среднюю цену конверсии или недельный бюджет. Также вы можете настроить оплату только за целевые визиты пользователей. Стратегия подходит для пользователей, которые определили цель привлечения посетителей на сайт или знают, какое соотношение расхода на продвижение и дохода от него является для них оптимальным.

## Принцип работы

Стратегия «Максимум конверсий» стремится увеличить долю кликов по тем объявлениям и ключевым фразам, которые чаще других приводят к целевому действию на сайте. Ставки автоматически подбираются таким образом, чтобы достичь наилучшего результата и соблюсти заданные условия и ограничения.

Рекомендуем оценивать результат через 7–14 дней — на старте кампании стратегии может потребоваться время на первичный сбор статистики. Если за время обучения получено мало конверсий, проверьте настройки стратегии, опираясь на рекомендации в интерфейсе.

Если вы изменяете тип атрибуции или цель, стратегии вновь понадобится время на обучение.

[Подробнее о работе стратегий](../strategies/select-strategy.md)

## Условия подключения

Для подключения стратегии необходим [счетчик Метрики](../statistics/metrika.md#settings). Для Метрики проверьте, что:

1. [Код счетчика](https://yandex.ru/support/metrica/general/creating-counter.html) установлен на рекламируемом сайте. Мы рекомендуем установить код счетчика на все страницы сайта.
2. У счетчика [настроены цели](https://yandex.ru/support/metrica/general/goals.html).
3. Для ограничения по доле рекламных расходов должна быть настроена передача в Директ дохода от рекламы — значения и валюты ценности цели. Передавать его можно несколькими способами:

   - Добавить [целевые действия](../strategies/priority-goals.md) в настройках стратегии и задать для них ценность. Для оптимизации вы можете выбирать не только те действия, которые приносят непосредственный доход, но и любые другие, например регистрацию на сайте или согласие на участие в акции.
   - Указать [доход по цели](https://yandex.ru/support/metrica/general/price-goal.html#price-goal__interface) в интерфейсе Яндекс Метрики. Для этого не требуются навыки программирования и точные финансовые показатели — достаточно задать средний чек или примерную оценку дохода от одной заявки или отправленной формы.
   - Использовать [метод `reachGoal`](https://yandex.ru/support/metrica/objects/reachgoal.html) с идентификатором цели и заданной ценностью.
   - Включить [электронную коммерцию](https://yandex.ru/support/metrica/data/e-commerce.html#ecommerce-enable) и передавать цену товара или сумму заказа. Для цели «eCommerce: Покупка» идентификатор цели будет автоматически передаваться Метрикой. Для другой цели идентификатор нужно передавать в поле `goal_id`.

     Пример передачи цены товара и идентификатора цели

     ```
     dataLayer.push({
              "ecommerce": {
              "purchase": {
              "actionField": {
              "id" : "TRX987",
              "goal_id": "123456"
              },
              "products": [
              {
              "id": "25341",
              "name": "Толстовка Яндекс мужская",
              "price": 1345.26,
              "brand": "Яндекс / Яndex",
              "category": "Одежда/Мужская одежда/Толстовки и свитшоты",
              "variant": "Оранжевый цвет"
              },
              {
              "id": "25314",
              "name": "Толстовка Яндекс женская",
     

*[Статья сокращена. Полная версия: docs/strategies/average-cpa.md]*


---

<!-- docs/strategies/average-cpc.md -->

# Максимум кликов

Стратегия позволяет привлечь как можно больше посетителей на сайт, удерживая заданные условия. Определите, на какой результат должна быть нацелена стратегия: получить максимум кликов по указанной средней цене клика или максимум кликов за указанный бюджет.

## Настройки стратегии

1. Выберите условия и ограничение расходов, при котором вы хотите получить максимум целевых действий:

   Средняя цена клика

   Бюджет

   Вариант подходит пользователям, которые знают, сколько готовы платить за посетителя.

   Система будет автоматически назначать ставки по условиям показа так, чтобы привлечь как можно больше пользователей. Ставки по одним условиям могут быть выше назначенной средней цены, по другим — ниже. В течение дня возможно отклонение средней цены как в большую, так и в меньшую сторону. Однако средняя цена клика по итогам недели не будет превышать сумму, которую вы назначили. Чтобы ограничение было выдержано, стратегия должна работать без изменений и остановок в течение всей календарной недели.

   Стратегия эффективна для кампаний с количеством кликов за неделю более 100. Если в кампании используются низкочастотные ключевые фразы и количество кликов за неделю менее 100, по итогам недели возможно отклонение средней цены за клик от заданного значения в большую сторону, но не более чем в 2 раза.

   ##### **Бюджет**

   Укажите сумму и выберите ограничение: в неделю или на период. Недельный бюджет подойдет для длительных кампаний без точной даты окончания. Если нужно контролировать расходы по флайтовым кампаниям, используйте бюджет на период.

   Минимальный бюджет:

   - На неделю — 300 рублей (*значения для других валют*).
   - На период — 50 рублей в день (*значения для других валют*).

   Подробнее о [бюджете в стратегии](../strategies/budgets-in-strategies.md).

   ##### **Средняя цена клика**

   Средняя цена клика — отношение недельного расхода к недельному количеству кликов, то есть цена, которая в среднем списывается за переход посетителя по объявлению. На указанную величину влияют выбранные [корректировки](../impressions/bids-adjustment.md#how-it-works).

   Минимальная средняя цена клика — 0,9 руб. (*значения для других валют*). Для определения оптимальной средней цены за клик рекомендуется использовать [Прогноз бюджета](https://direct.yandex.ru/registered/main.pl?cmd=advancedForecast).

   #####

   Вариант подходит пользователям, первоочередная задача которых — привлечь на сайт как можно больше заинтересованных посетителей.

   Система распределяет средства так, чтобы получить как можно больше переходов на сайт за указанный бюджет. Ключевым фразам с высоким прогнозом CTR система обеспечивает больший объем трафика, для фраз с небольшим прогнозом кликабельности ставки понижаются.

   Чтобы ограничение было выдержано, стратегия должна работать без изменений и остановок в течение всей календарной недели или указанного периода.

   ##### **Как настроить**
2. Добавьте [счетчик Метрики](../strategies/average-cpa.md#conditions).

   Если у вас нет доступа к счетчику Метрики, то можно запросить доступ к целям, которые настроены на нем. Для этого укажите счетчик и нажмите **Запросить доступ**. Далее обратитесь к владельцу счетчика для включения [опции](../statistics/metrika.md#access-to-goals) **Разрешить в рекламных кампаниях оптимизацию по целям**.
3. Выберите целевые действия и задайте их ценность.

   Цель — это действие, к которому вы хотите привести пользователя с помощью продвижения. Можно выбрать получение визитов по целям, заданным в Метрике.

   По умолчанию выбраны вовлеченные сессии — алгоритм ориентируется на рассчитанные целевые действия и среднюю ценность конверсии на вашем сайте.

   Определиться с целью для оптимизации поможет цветная точка рядом с ней:

   - Зеленая — по цели достаточно целевых визитов по всем источникам трафика. Рекомендуем использовать эту цель.
   - Серая — по цели мало целевых визитов по всем источникам трафика. Есть риск, что цель будет плохо достигаться с помощью рек

*[Статья сокращена. Полная версия: docs/strategies/average-cpc.md]*


---

<!-- docs/strategies/maximum-profit.md -->

Максимум прибыли<sup>β</sup>

# Максимум прибылиβ

- [Принцип работы](../strategies/maximum-profit.md#how-it-works)
  - [Как рассчитать маржу с конверсии](../strategies/maximum-profit.md#margin)
- [Настройки стратегии](../strategies/maximum-profit.md#how-to-use)
- [Как оценить работу стратегии](../strategies/maximum-profit.md#how-to-rate)
  - [В Мастере отчетов](../strategies/maximum-profit.md#v-mastere-otchetov)
  - [С помощью А/В-эксперимента](../strategies/maximum-profit.md#s-pomoshyu-a/v-eksperimenta)
- [Вопросы и ответы](../strategies/maximum-profit.md#voprosy-i-otvety)

Стратегия позволяет получить максимальную *прибыль от продвижения*. На основе данных о *марже с конверсии* она подбирает оптимальную цену конверсии и постоянно ее актуализирует. Это позволяет:

- Определять тот уровень цены конверсии, при котором бизнес получает максимальную итоговую прибыль, даже если это означает отклонение от средних показателей цены конверсии.
- Масштабировать финансовые результаты бизнеса. Стратегия будет стремиться не достичь заданного показателя, а найти те объем и стоимость конверсий, которые позволят бизнесу заработать больше.

Стратегия подходит бизнесам, которые оптимизируются по цене конверсии и стремятся повысить финансовую эффективность кампаний с учетом юнит-экономики. В первую очередь стратегия будет полезна компаниям, для которых важен именно рост прибыли и экономика которых позволяет рассчитать и усреднить маржу для выбранной цели.

## Принцип работы

Стратегия «Максимум прибыли» подбирает ставки так, чтобы найти оптимальное соотношение между количеством конверсий и их стоимостью и получить больше прибыли от продвижения.

|  |  |
| --- | --- |
|  | Обучающее видео. Как стратегия находит максимальную прибыль и подбирает оптимальную стоимость конверсии Посмотреть видео |

Для работы стратегии нужно выбрать цель и указать среднюю маржу, которую приносит ее достижение, без учета расхода на продвижение (цены конверсии).

Динамическая передача маржи для каждой отдельной конверсии (например, для разных товаров в корзине) пока не поддерживается.

**Маржа с конверсии** — это средний доход с одной целевой конверсии за вычетом переменных затрат (например, себестоимости товара, оплаты исполнителю, комиссий платежных систем и т. д.), но без учета расходов на продвижение. Эту сумму нужно указать в настройках стратегии.

**Прибыль от продвижения** — это итоговый финансовый результат кампаний. Рассчитывается как суммарная маржа с конверсий, полученных в рамках кампании, за вычетом общих расходов на продвижение в ней за тот же период. Это то, что стратегия будет стремиться максимизировать.

### Как рассчитать маржу с конверсии

**Маржа с конверсии = Средний доход с продажи - Средняя себестоимость продажи**, где:

- **Средний доход с продажи** — это средняя выручка от одной продажи (например, цена товара или услуги);
- **Средняя себестоимость продажи** — это все переменные расходы, которые связаны с одной продажей. Например, себестоимость товара, оплата исполнителю, расходные материалы, комиссии платежных систем, доставка и т. д. Постоянные расходы не вычитаются на этом этапе (например, аренда офиса, зарплата бухгалтера, разработка ПО и т. д.). Также эти затраты не включают расходы на продвижение (цену конверсии).

Если не каждое достижение цели приводит к продаже, для маржи с одной конверсии нужно учесть коэффициент конверсии из цели в продажу CR:

**Конверсия из цели в продажу (CR) = Количество фактических продаж / Количество конверсий по цели**,

тогда

**Маржа с конверсии (для цели) = (Средний доход с продажи - Средняя себестоимость продажи) × CR**

Примеры расчета маржи

##### **Пример 1. Клининговая служба**

- Цель стратегии: заявка с сайта.
- Средний доход с одного оплаченного заказа: 5 000 рублей.
- Средняя себестоимость заказа (зарплата исполнителя, моющие средства и другие переменные расходы): 3 000 рублей.
- Маржа с одного заказа: 5 000 – 3 000 = 2 000 рублей.
- Средняя конверсия из заявки в оплаченный заказ: 50%.

Маржа с кон

*[Статья сокращена. Полная версия: docs/strategies/maximum-profit.md]*


---

<!-- docs/strategies/manual-strategy.md -->

# Максимум кликов с ручными ставками

- [Настройки стратегии](../strategies/manual-strategy.md#how-to-use)
- [Как выбрать оптимальную ставку](../strategies/manual-strategy.md#optimal-bid)
- [Как назначить ставку](../strategies/manual-strategy.md#how-to-bid)
- [Как отслеживать изменение объема трафика](../strategies/manual-strategy.md#traffic-volume-statistic)

Стратегия «Максимум кликов с ручными ставками» позволит вам самостоятельно назначать ставки для отдельных [условий показа](../impression-criteria/impression-criteria.md) в кампаниях только **на поиске**. Вы получите максимально возможное количество показов и кликов с учетом заданных ограничений (ставки, региона показа и т. д.) и конкуренции. В кампаниях с показами в РСЯ или на поиске и РСЯ действуют правила [GSP-аукциона](../technologies-and-services/vcg-auction.md#calc-gsp), ставка устанавливается автоматически, ручное управление недоступно.

Благодаря [прогнозатору конверсий](../impressions/automatic-bid-adjustment-in-yan.md#about), ставки могут автоматически снижаться для кликов с низкой вероятностью конверсии или повышаться для кликов с высокой вероятностью конверсии. Так вы сможете получить больше целевого трафика. Чтобы продвижение стало более выгодным для бизнеса, укажите [целевые действия](../strategies/priority-goals.md) и их ценности. Алгоритмы, корректирующие ставки, будут ориентироваться на указанные значения и прицельно работать на ваши задачи.

## Настройки стратегии

##### **Дневной бюджет**

Ежедневный расход на кампанию в среднем за календарную неделю.

В течение недели бюджет перераспределяется: остатки бюджета с менее активных дней будут потрачены в более активные. Таким образом, расход за день может быть больше или меньше указанного значения. Дополнительно может быть израсходовано не более 30% указанной суммы среднего дневного бюджета. При этом **ежедневный расход в среднем за неделю** останется в рамках заданного ограничения.

Минимальный размер дневного бюджета — 300 рублей (*значения для других валют*).

Подробнее о [бюджете в стратегии](../strategies/budgets-in-strategies.md#day-budget).

##### **Счетчик Метрики**

Добавьте [счетчик Метрики](../strategies/average-cpa.md#conditions).

Если у вас нет доступа к счетчику Метрики, то можно запросить доступ к целям, которые настроены на нем. Для этого укажите счетчик и нажмите **Запросить доступ**. Далее обратитесь к владельцу счетчика для включения [опции](../statistics/metrika.md#access-to-goals) **Разрешить в рекламных кампаниях оптимизацию по целям**.

##### **Целевые действия и их ценность**

Укажите [целевые действия](../strategies/priority-goals.md#priority-goals), чтобы система прицельно работала для решения ваших задач. По умолчанию выбраны *вовлеченные сессии*.

Если у текущего логина нет доступа к нужным счетчикам, вы можете запросить доступ к целям Яндекс Метрики на чужом счетчике и использовать их для настройки.

Количество целевых действий не ограничено.

##### **Модель атрибуции**

Если необходимо, в дополнительных настройках выберите модель атрибуции.

Модель атрибуции — это правило, какой переход на сайт считать источником визита. Модель помогает точнее определить вклад рекламы в развитие вашего бизнеса. При назначении ставок система использует статистику Яндекс Метрики по выбранной модели атрибуции и стремится достигать заданного вами результата.

Выбор модели зависит от типа бизнеса, способа привлечения трафика и ваших задач. По умолчанию установлена автоматическая модель атрибуции. При необходимости вы можете ее изменить.

Подробнее о [моделях атрибуции](../statistics/attribution-model.md).


Вы в любой момент можете изменить используемую стратегию в параметрах кампании.

## Как выбрать оптимальную ставку

**Оптимальная ставка** — это максимальная рентабельная цена клика, которую вы готовы заплатить, опираясь на показатели бизнеса, чтобы получить как можно больше трафика.

- В ручной стратегии нужно самостоятельно подбирать оптимальную ставку для каждой ключевой фразы. При этом лучше

*[Статья сокращена. Полная версия: docs/strategies/manual-strategy.md]*


---

<!-- docs/strategies/portfolio-strategy.md -->

# Пакетная стратегия

- [Как создать](../strategies/portfolio-strategy.md#create)
- [Как в настройках кампании выбрать пакетную стратегию](../strategies/portfolio-strategy.md#settings)
- [Как создать пакетную стратегию на базе обычной](../strategies/portfolio-strategy.md#use)
- [Статистика](../strategies/portfolio-strategy.md#statistics)
- [Вопросы и ответы](../strategies/portfolio-strategy.md#qa)

Пакетная стратегия позволяет объединить несколько кампаний одного типа с единой настройкой показателей стратегии. Она решает проблему нехватки конверсий для обучения. Конверсии, полученные в рамках пакетной стратегии, идут в обучение для всех добавленных в нее кампаний. Если добавить новую кампанию к уже работающей пакетной стратегии, кампания быстрее выйдет на заданные показатели оптимизации.

Также пакетные стратегии будут полезны тем, кому важно работать с одним бюджетом в рамках нескольких кампаний с разными задачами. Бюджет в пакетной стратегии будет распределяться между кампаниями в зависимости от их эффективности.

Пакетные стратегии доступны в [Единой перфоманс-кампании](../unified-performance-campaign/about.md), кроме кампаний с показами в телеграм-каналах и для продвижения приложений.

Для управления кампаниями можно создать один из типов пакетных стратегий:

- [Максимум кликов](../strategies/average-cpc.md) — объединяет кампании, цель которых привлечь как можно больше посетителей на сайт.
- [Максимум конверсий](../strategies/average-cpa.md) — подходит для кампаний с целью получить максимум *целевых визитов* на сайте, удерживая заданную долю рекламных расходов, среднюю цену конверсии или недельный бюджет.
- [Максимум прибыли](../strategies/maximum-profit.md) — объединяет кампании, цель которых получить максимальную *прибыль от продвижения*.

## Как создать

1. В меню слева выберите **Библиотека** → **Пакетные стратегии** или нажмите **Добавить**  → **Пакетную стратегию**.
2. Укажите название стратегии.
3. Настройте стратегию, используя доступные параметры. Они аналогичны обычным стратегиям [Максимум кликов](../strategies/average-cpc.md), [Максимум конверсий](../strategies/average-cpa.md) или [Максимум прибыли](../strategies/maximum-profit.md).
4. Добавьте кампании, в которых будет работать стратегия. В блоке **Кампании, к которым применяется пакетная стратегия** нажмите **Добавить** и выберите нужные. Объединить в рамках пакета можно только кампании одного типа.

   Если вы добавляете к пакетной стратегии уже работающую кампанию, в ней одна стратегия изменится на другую, поэтому результаты ее работы могут измениться. С другой стороны, данные обучения, ранее накопленные в кампании, сохранятся в системе и будут учитываться при управлении ставками в этой кампании.

   В одну пакетную стратегию можно добавить до 100 кампаний.

Можно создать до 500 активных пакетных стратегий.

## Как в настройках кампании выбрать пакетную стратегию

В настройках кампании в блоке **Стратегии**:

1. Перейдите на вкладку **Пакетные**.
2. В поле **Стратегия** выберите созданную пакетную стратегию.
3. Если необходимо, перейдите в настройки стратегии и проверьте их. Например, указанного недельного бюджета должно хватать **на все** кампании.

## Как создать пакетную стратегию на базе обычной

Пакетную стратегию можно не создавать с нуля, а использовать для настройки уже работающую в другой кампании. Для этого в настройках одной из кампаний в блоке **Стратегии**:

1. Перейдите на вкладку **Пакетные**.
2. В поле **Стратегия** выберите «Из другой кампании».
3. Укажите кампанию — источник для стратегии.
4. Если необходимо, перейдите в настройки стратегии и проверьте их. Например, указанного недельного бюджета должно хватать **на все** кампании.

После сохранения настроек кампании в библиотеке пакетных стратегий появится новая стратегия. К ней будут добавлены две кампании – исходная (на базе настроек которой вы создавали пакетную стратегию), и только что сохраненная.

#### Особенности статистики

Если вы создаете пакетную стратегию на базе настроек кампан

*[Статья сокращена. Полная версия: docs/strategies/portfolio-strategy.md]*


---

<!-- docs/strategies/priority-goals.md -->

# Целевые действия

- [Настройка целевых действий](../strategies/priority-goals.md#priority-goals)
- [Как рассчитать ценность конверсии](../strategies/priority-goals.md#conversion-value)
- [Статистика по целевым действиям (ЦД)](../strategies/priority-goals.md#statistics)

Целевые действия (бывшие Ключевые цели) — действия посетителей сайта, наиболее важные для бизнеса. Например, отправка заявки, регистрация на сайте, просмотр страниц с ценами и услугами, добавление товара в корзину, покупка. Используйте их в кампании, и система будет прицельно работать для решения ваших задач.

## Настройка целевых действий

Чтобы система корректировала ставки в зависимости от задач вашего сайта, настройте [цели в Яндекс Метрике](https://yandex.ru/support/metrica/general/goals.html) и укажите их в настройках стратегии.

1. При настройке кампании в блоке **Стратегии** в разделе **Целевые действия и их ценность** выберите необходимую цель из списка:

   - Если в местах показа выбраны **Поиск** или **РСЯ**, укажите счетчик Яндекс Метрики для сайта и выберите цели для сайта.
   - Если выбраны **Список организаций в результатах поиска** или **Карты**, в счетчики Яндекс Метрики автоматически добавится счетчик для профиля организации в Яндекс Бизнесе. Укажите цели для него.

   Если в рамках одной кампании продвигается и сайт, и профиль организации, лучше добавить как минимум одну цель для сайта и одну цель для профиля, чтобы кампания оптимизировалась на все места показа.

   В стратегиях «Максимум кликов» и «Максимум кликов с ручными ставками» по умолчанию выбраны вовлеченные сессии — алгоритм ориентируется на рассчитанные целевые действия и среднюю ценность конверсии на вашем сайте. Вы можете выбрать любые цели, в том числе составные или Ecommerce.
2. Задайте для каждой цели ценность конверсии — оптимальную для бизнеса экономическую выгоду от достижения цели. Чем выше ценность конверсии, тем более важную роль играет цель в работе кампании. В стратегии [Максимум конверсий](../strategies/average-cpa.md) для eCommerce-целей лучше указывать, что ценность — «*Динамическая*».

В стратегии можно указать не более 30 целевых действий. Если у текущего логина нет доступа к нужным счетчикам, вы можете запросить доступ к целям Яндекс Метрики на чужом счетчике и использовать их для настройки.

## Как рассчитать ценность конверсии

Если цели независимы друг от друга, можно указать номинальную ценность — сколько бизнес зарабатывает на каждой конверсии. Например, достижение цели «Заказал обратный звонок» приносит 50 руб., «Посмотрел товар» — 10 руб., а «Оформил заказ» — 180 руб.

Если рассчитать номинальную ценность невозможно, то укажите ценность конверсии главной цели кампании, а ценность других целей задайте в зависимости от приоритета относительно главной цели.

В расчетах ценности можно учесть влияние целей друг на друга, если для достижения каждой следующей цели требуется выполнить условия для завершения предыдущей.

> Например, туроператор разместил объявления в сетях и настроил в Яндекс Метрике цели «Просмотр каталога туров», «Тур добавлен в корзину», «Клиент купил тур».
>
> Достижение цели «Клиент купил тур» приносит бизнесу 10 000 руб. Это ценность одной конверсии для бизнеса. Каждый десятый клиент, который добавляет тур в корзину, затем покупает его. Ценность конверсии «Тур добавлен в корзину» = 10 000 / 10 = 1000 (руб.), количество конверсий = 10 000 / 1000 = 10. Каждый двадцатый клиент, который смотрит каталог, добавляет тур в корзину. Ценность конверсии «Просмотр каталога туров» = 1000 / 20 = 50 (руб.), количество конверсий = 10 000 / 50 = 200.
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> |  | **Просмотр каталога туров** | **Тур добавлен в корзину** | **Клиент купил тур** |
> | Конверсии | 200 | 10 | 1 |
> | Ценность конверсии | 50 руб. | 1000 руб. | 10 000 руб. |
>
> Для достижения каждой следующей цели требуется выполнить условия, указанные для завершения предыдущей, поэтому необходимо рассчитать доли каждой цели:
>
> При настройке ключевых целей

*[Статья сокращена. Полная версия: docs/strategies/priority-goals.md]*


---

<!-- docs/strategies/budgets-in-strategies.md -->

# Настройка бюджета в стратегиях

- [Типы бюджетов](../strategies/budgets-in-strategies.md#tipy-byudzhetov)
- [Вопросы и ответы](../strategies/budgets-in-strategies.md#voprosy-i-otvety)
- [Кейсы и полезные материалы](../strategies/budgets-in-strategies.md#kejsy-i-poleznye-materialy)

В стратегии [Максимум кликов с ручными ставками](../strategies/manual-strategy.md) можно задать только дневной бюджет.

В стратегиях [Максимум конверсий](../strategies/average-cpa.md), [Максимум кликов](../strategies/average-cpc.md) и [Максимум прибыли](../strategies/maximum-profit.md) можно установить ограничение бюджета:

- На неделю — подходит для длительных кампаний без точной даты окончания.
- На период — подходит для кампаний, которые имеют заранее определенный бюджет и даты начала и окончания.

Недельный и периодный бюджет можно настроить в обычных и [пакетных](../strategies/portfolio-strategy.md) стратегиях.

## Типы бюджетов

Дневной бюджет

Недельный бюджет

Периодный бюджет

Это ежедневный расход на кампанию в среднем за календарную неделю.

Дневной бюджет можно настроить только для стратегии [Максимум кликов с ручными ставками](../strategies/manual-strategy.md).

#### **Как работает**

Стратегия стремится выдержать заданный дневной бюджет, распределяя средства на весь день или на промежуток, который указан в настройках временного таргетинга.

Ориентируясь на дневной бюджет, система оптимизирует расходы в течение календарной недели. С одной стороны, она выдерживает ограничение, с другой — балансирует расходы и приток трафика.

Если бюджета не хватает для показов в течение всего дня, объявления будут реже принимать участие в аукционе. Если указанной суммы затрат достаточно на день показов, вы будете получать весь доступный трафик.

Если при небольшом дневном бюджете вы используете высокочастотные фразы или по фразам установлены высокие ставки, Директ не гарантирует равномерного распределения показов в течение дня. Доступный бюджет может быть израсходован в начале периода показов, и на остаток дня средств не останется.

В течение недели бюджет перераспределяется: остатки бюджета с менее активных дней будут потрачены в более активные. Таким образом, расход за день может быть больше или меньше указанного значения. Дополнительно может быть израсходовано не более 30% указанной суммы среднего дневного бюджета. При этом **ежедневный расход в среднем за неделю** останется в рамках заданного ограничения.

Дневной бюджет работает по московскому времени, независимо от выбранного часового пояса кампании.

#### **Максимальный расход в день**

Расход за день не может превышать заданный бюджет более чем на 30%.

#### **Ограничения по сумме**

Минимальный размер дневного бюджета — 300 рублей (*значения для других валют*).

#### **Изменение дневного бюджета**

Изменять сумму дневного бюджета можно не более трех раз в сутки:

- При установке лимита или уменьшении дневного бюджета настройка будет работать со **следующего дня**.
- При снятии лимита или увеличении дневного бюджета он применится **сразу после активизации**.

При этом средний расход с понедельника до дня изменения, включая его, может превышать ранее установленный лимит не более чем на 30%. За оставшиеся дни недели средний расход будет стремиться к новой сумме дневного бюджета.

#### **Как работает**

Стратегия стремится выдержать заданный недельный бюджет, распределяя средства на календарную неделю с понедельника по воскресенье. Бюджет может расходоваться неравномерно в течение недели, но недельное ограничение не будет превышено. В рамках недели может потратиться больше средств только в случае [рестарта бюджета](../strategies/budgets-in-strategies.md#restart).

Распределение бюджета зависит от настроек [временного таргетинга](../efficiency/timetargeting.md). Например, если вы ограничили показы объявлений до двух дней в неделю, бюджет будет распределен только на два дня.

Если бюджет не может быть потрачен, как правило, это говорит о неэффективном подборе [ключевых фраз](../keywords/building-ke

*[Статья сокращена. Полная версия: docs/strategies/budgets-in-strategies.md]*


---

<!-- docs/keywords/keywords.md -->

# Ключевые фразы

- [Принципы работы](../keywords/keywords.md#how-it-works)
- [Как добавить ключевые фразы](../keywords/keywords.md#add)

**Ключевые фразы** — это слова или словосочетания, которые определяют, кому будет показано ваше объявление.

На поиске Яндекса объявления показываются по запросам, которые:

- Содержат фразу целиком (пословное соответствие).
- Семантически уточняют фразу: содержат опечатки, синонимы, более конкретные слова, переформулировки (семантическое соответствие).

## Принципы работы

Ключевые фразы на поиске и в сетях работают по-разному.

На поиске

В сетях

|  |  |
| --- | --- |
|  | Обучающее видео. Как работают ключевые фразы на Поиске Посмотреть видео |

Ключевая фраза определяет, по каким запросам объявление из группы может показываться на поиске Яндекса и на поисковых площадках РСЯ.

Например, если вы задали фразу *туры на марс*, то ваши объявления могут быть показаны по запросам *туры на марс*, *горящие туры на марс*, *туры на марс недорого*, *купить туры на марс* и т. п., но не будут показаны по запросам *туры на луну* или *есть ли жизнь на марсе*.

Отследить, по каким запросам и типам соответствия было показано объявление, поможет [отчет «Поисковые запросы»](../statistics/search-queries.md). Проанализируйте статистику и дополните ключевые фразы запросами с высоким CTR, а нерелевантные запросы исключите, добавив их в минус-фразы.

Ключевая фраза определяет тематику площадок и интересы пользователя, в соответствии с которыми объявление может показываться в сетях. Например, объявление о продаже туров на Марс может быть показано на странице про путешествия или пользователю, который интересуется полетами на Марс.

## Как добавить ключевые фразы

Ключевые фразы можно добавить через боковое меню: нажмите **Добавить** → **Ключевые фразы**, выберите кампанию и группу объявлений и нажмите **Добавить ключевые фразы**. Воспользуйтесь подбором фраз или перейдите на вкладку **Ручной ввод**, чтобы ввести готовые запросы. Подробнее о [подборе фраз](../keywords/prompt-to-keyword-generator.md).

Добавление или изменение ключевой фразы происходит в течение 3 часов. Чтобы добавить ключевые фразы для отдельного объявления, создайте для него новую группу.

#### Требования и ограничения

В тексте ключевых фраз разрешается использовать только буквы английского, турецкого, казахского, русского, украинского или белорусского алфавита, кавычки, знаки «-», «+», «!», пробел и другие [операторы Директа](../keywords/symbols-and-operators.md). В десятичных дробях допустимо использовать точку. Регистр букв и порядок слов не важны.

Длина ключевой фразы не может быть больше 4096 символов (включая [минус-слова](../keywords/negative-keywords.md), пробелы и операторы Директа). Количество фраз на группу — не более 200. Количество слов для одной ключевой фразы — не более 7.

#### Пересечения и повторы

Если ключевые фразы пересекаются (одна содержит в себе другую), то к ним автоматически добавляются минус-слова. В этом случае ключевые фразы перестают конкурировать при выборе объявления для показа.

Повторяющиеся слова в ключевой фразе объединяются. Например, вместо фразы *Баден-Баден* останется только слово *Баден.* Показы объявления будут идти как по запросу *Баден-Баден*, так и просто по запросу *Баден*.

#### Стоп-слова

Стоп-слова — это служебные части речи и местоимения, которые автоматически исключаются из ключевой фразы при отборе объявлений для показа. Например, в запросе *как и когда путешествовать на марс* будут отобраны объявления с ключевой фразой *путешествовать марс*. Слова *как*, *и*, *когда*, *на* являются стоп-словами.

В некоторых случаях стоп-слова могут иметь важное значение, и без них смысл фразы меняется. Например, для сериала «Это по дружбе» ключевая фраза будет *это по дружбе*. Частица *это* и предлог *по* являются стоп-словами и важны для смысла ключевой фразы. Чтобы учитывать стоп-слова во фразе, можно зафиксировать их [операторами](../keywords/symbols-and-operators.md) «+» или «!», но это необязательно.


*[Статья сокращена. Полная версия: docs/keywords/keywords.md]*


---

<!-- docs/keywords/negative-keywords.md -->

# Минус-слова и минус-фразы

- [Принципы работы](../keywords/negative-keywords.md#how-it-works)
- [Как добавить минус-слова и минус-фразы](../keywords/negative-keywords.md#add)
- [Минус-слова и минус-фразы при показе в сетях](../keywords/negative-keywords.md#yan)
- [Совместная работа с операторами](../keywords/negative-keywords.md#operators)

Объявления в Директе показываются по запросам, полностью содержащим вашу ключевую фразу.

> Например, вы продаете путешествия на Луну. Объявление с ключевой фразой *путешествие на луну* будет показано не только по запросу *купить путешествие на луну*, но и по не самым подходящим запросам: *книги про путешествия на луну*, *первое путешествие на луну*.

Чтобы исключить показы по неподходящим запросам, добавьте минус-слова и минус-фразы.

## Принципы работы

**Минус-слова** и **минус-фразы** — это слова и словосочетания, по запросам с которыми объявление показываться не будет.

Минус-слова можно добавить только для ключевой фразы. Например, если к фразе *путешествие на луну* добавить минус-слово *книга*, объявление не будет показано по запросу *книги о путешествиях на луну*.

Чтобы исключить показ по словосочетанию целиком, добавьте **минус-фразы** для кампании или группы объявлений. По запросам, которые содержат все слова минус-фразы, объявление показываться не будет. При этом показы будут по запросам, в которых есть только часть минус-фразы.

> Например, у вас задана ключевая фраза *путешествие*, если для группы объявлений вы добавили минус-фразу *созвездие водолея*, то по запросу *путешествия в созвездие тельца* объявления будут показаны.

Если все слова из минус-фразы или минус-слова входят в ключевую фразу (полностью пересекаются с ней), минус-слово или минус-фраза игнорируются.

> Например, ключевая фраза *купить розового слона* и минус-фраза *купить слона* полностью пересекаются — все слова из минус-фразы входят в ключевую фразу. Минус-фраза игнорируется и показы по запросу *купить розового слона* будут идти.
>
> Ключевая фраза *купить розового слона* и минус-фраза *купить недорого* пересекаются частично, только по слову *купить*. По запросу *купить розового слона недорого* показов объявления не будет.

Если вы хотите исключить конкретную форму слова, добавьте ее с оператором `!`.

## Как добавить минус-слова и минус-фразы

Добавить минус-слова можно для ключевой фразы, а минус-фразы — для  группы объявлений или кампании.

#### Минус-слова для ключевой фразы

На вкладке **Фразы** укажите минус-слово после ключевой фразы с оператором `-`.

Также минус-слова можно задать и на странице редактирования группы в блоке **Тематические слова** в поле **Ключевые фразы**.

#### Минус-фраза для группы объявлений

На странице редактирования группы объявлений в блоке **Тематические слова** в поле **Минус-фразы** укажите минус-фразы через запятую или `-`. Количество слов для одной минус-фразы — не более 7. Максимально допустимое количество символов — 4096 без учета пробелов.

#### Минус-фраза в Мастере кампаний

- Продвижение приложений: количество фраз на группу — не более 200;
- Продвижение сайта: максимально допустимое количество символов — 20 000 без учета пробелов.

#### Минус-фраза для кампании

Укажите минус-фразы через запятую на странице параметров кампании в блоке **Минус-фразы**. Количество слов для одной минус-фразы — не более 7. Максимально допустимое количество символов — 20 000 без учета пробелов.

Минус-слова и минус-фразы в Директе дополняют друг друга, но не заменяют. Если указаны минус-слова для ключевой фразы, минус-фразы для группы объявлений и для кампании, то они применяются к ключевой фразе все вместе, и показов не будет по всем минус-словам и фразам.

Добавить минус-слова или минус-фразы сразу в несколько объявлений можно с помощью [XLS/XLSX-файлов](../alternative-interfaces/xls-interface.md), [массового действия с группами объявлений](../campaigns/groups-edit.md), Директ.Коммандера или [API Яндекс Директа](../alternative-interfaces/api.md).

## Минус-слова и минус-фразы при

*[Статья сокращена. Полная версия: docs/keywords/negative-keywords.md]*


---

<!-- docs/keywords/symbols-and-operators.md -->

# Символы и операторы

- [Как работают операторы](../keywords/symbols-and-operators.md#how-it-works)
- [Рекомендации по использованию](../keywords/symbols-and-operators.md#joint-use)

В Директе можно использовать специальные символы и операторы, которые помогут вам точнее сформулировать ключевую фразу, минус-фразу или запрос в [Вордстате](../keywords/wordstat.md). Операторы можно комбинировать между собой.

В тексте объявления вы можете использовать математические символы (+, -, =, /, \*, % и другие), знаки препинания, апостроф, хештеги. Употребление символов должно быть логически обосновано.

Некоторые символы в объявлении могут работать как операторы, например `#слово#` будет работать [шаблоном](../features/ad-templates.md) и в объявление будет подставляться ключевая фраза вместо слова, выделенного ##.

## Как работают операторы

В таблицах ниже перечислены все операторы, а также приведены примеры ключевых фраз и запросов, по которым будут или не будут показаны ваши объявления.

- Оператор `!` фиксирует форму слова (число, падеж, время).

  |  |  |
  | --- | --- |
  | **Пример ключевой фразы** | **Когда покажем** |
  | `купить билет в !москву` | *купить билет в москву*  *купить билет в москве* |
  | `купить !собаку` | *купить собаку*  *купить корм для собак*  *купить собак* |
  | `перевозка водного !транспорта` | *перевозка водного транспорта*  *перевозка водным транспортом* |
  | `купить !вазу` | *купить вазу*  *купить ваз* |
- Оператор `+` фиксирует стоп-слова (служебные части речи и местоимения, а также любые слова, не несущие дополнительного смысла).

  |  |  |
  | --- | --- |
  | **Пример ключевой фразы** | **Когда покажем** |
  | `работа +на дому` | *работа на дому*  *работа по дому*  *работа дома* |
  | `+если выключился компьютер` | *если выключился компьютер*  *чтобы выключился компьютер* |
  | `крем +для бритья` | *крем для бритья*  *крем после бритья* |
  | `сверло +по металлу` | *сверло по металлу*  *сверло из металла* |
- Оператор `" "` фиксирует количество слов. Показ по запросам, содержащим фразу без дополнительных слов.

  |  |  |
  | --- | --- |
  | **Пример ключевой фразы** | **Когда покажем** |
  | `"купить автомобиль"` | *купить автомобиль*  *автомобиль купить*  *купить красный автомобиль* |
  | `"купить автомобиль в кредит в Москве"` | *купить автомобиль в кредит в москве*  *купить автомобиль в кредит москва* |
  | `"номер в отеле на двоих"` | *номер в отеле на двоих*  *номер в отеле для двоих*  *номер в недорогом отеле на двоих* |
  | `"приложение с картами"` | *приложение с картами*  *приложение с дисконтными картами* |
- Оператор `[]` фиксирует порядок слов. При этом учитываются все словоформы и стоп-слова.

  |  |  |
  | --- | --- |
  | **Пример ключевой фразы** | **Когда покажем** |
  | `билеты [из москвы в париж]` | *билеты из москвы в париж*  *билеты на самолет из москвы в париж*  *билеты из парижа в москву*  *билеты москва париж*  *билеты из москвы недорого в париж* |
  | `билеты [москва париж]` | *билеты москва париж*  *билеты на самолет москва париж*  *билеты недорого москва париж*  *стоимость билетов москва париж*  *билеты из москвы в париж*  *билеты париж москва*  *билеты из москвы недорого в париж* |
  | `[лечение при осложнениях]` | *лечение при осложнениях*  *осложнения при лечении* |
  | `[школа живописи]` | *школа живописи*  *школа живописи маслом*  *живопись школы кано* |
- Операторы `()` и `|` группируют слова при сложных запросах.

  |  |  |
  | --- | --- |
  | **Пример ключевой фразы** | **Когда покажем** |
  | `купить машину (недорого|ваз)` | *купить машину недорого*  *купить машину ваз* |
  | `заказать еду (роллы|пицца)` | *заказать еду роллы*  *заказать еду пицца* |
  | `купить (пуховик|куртку)` | *купить пуховик*  *купить куртку* |

Если нужно учитывать стоп-слова во фразе, то можно их зафиксировать операторами «+» или «!», но это необязательно. Директ [учтет](../keywords/keywords.md#stopwords), как стоп-слова влияют на смысл ключевой фразы, и исключит показы по нерелевантным зап

*[Статья сокращена. Полная версия: docs/keywords/symbols-and-operators.md]*


---

<!-- docs/keywords/wordstat.md -->

# Сервис подбора слов

[Вордстат](https://wordstat-2.yandex.ru/) или **Подбор слов (wordstat)** — это сервис, который показывает статистику поисковых запросов к Яндексу. С его помощью можно посмотреть, как менялась популярность интересующих вас запросов и как она отличается в разных регионах России, а также построить топы запросов с нужными словами и узнать, что еще люди искали на ту же тему.

## Как пользоваться сервисом

Вы можете воспользоваться формой подбора слов из интерфейса Директа. Для этого нажмите **Подобрать слова** в блоке **Новые ключевые фразы** и введите ключевую фразу. Чтобы изучить более подробную статистику, перейдите в интерфейс сервиса Вордстат — в меню слева выберите **Инструменты**, затем **Подбор слов**.

Например, в Директе вы продвигаете бригаду по ремонту квартир и хотите добавить к вашему объявлению ключевую фразу *ремонт*. Введите эту фразу в сервисе [Вордстат](https://wordstat-2.yandex.ru/). Перейдите на вкладку **Топы запросов**. По данным на странице видно, что *ремонт* — популярный запрос (12 млн показов в месяц). Но он не отражает, чем интересовался покупатель: ремонтом квартир, машин или телефонов.

Чтобы объявления не показывались по популярным, но неподходящим для вас запросам, в Директе замените ключевую фразу *ремонт* на *ремонт квартир*. Уточнить фразу *ремонт* можно и с помощью минус-слов. Если добавить минус-слова *машин* и *телефонов*, объявление не будет показываться по популярным запросам *ремонт машин* и *ремонт телефонов*.

При работе с сервисом можно использовать [дополнительные операторы](../keywords/symbols-and-operators.md):

- Вордстат (новый интерфейс) — на вкладках **Топы запросов** и **Регионы** работают все операторы, на вкладке **Динамика** — только `+`.
- Подбор слов (старый интерфейс) — на вкладках **По словам** и **По регионам** работают все операторы, на вкладке **История запросов** — только `+`.

Переключитесь на **Похожие запросы**. Пользователей, искавших *ремонт квартир*, может заинтересовать *отделка квартир* и *натяжной потолок*. Добавьте в список ключевых фраз вашего объявления в Директе те, которые соответствуют целям продвижения.

Подробнее о работе сервиса в [Справке Вордстата](https://yandex.ru/support2/wordstat/ru/interface/new).

## Обновили мобильное приложение Директа

Настроить продвижение теперь проще и удобнее, даже если у вас нет опыта

[Скачать приложение](https://redirect.appmetrica.yandex.com/serve/1110145804347161038)

---

<!-- docs/impression-criteria/autotargeting.md -->

# Автотаргетинг

- [Принципы работы](../impression-criteria/autotargeting.md#how-it-works)
- [Настройки автотаргетинга на поиске и в Картах](../impression-criteria/autotargeting.md#at-for-search)
- [Как настроить автотаргетинг в кампании](../impression-criteria/autotargeting.md#autoy_on)
- [Управление ставками в ручной стратегии](../impression-criteria/autotargeting.md#auto-bids)
- [Как анализировать эффективность автотаргетинга](../impression-criteria/autotargeting.md#what-next)

Автотаргетинг — это технология показа объявлений, не использующая ключевые фразы. Она анализирует информацию в объявлении и на странице перехода и определяет, соответствует ли объявление поисковому запросу, интересам пользователя или тематике площадки. Автотаргетинг позволяет получить дополнительный целевой трафик благодаря показам аудитории, которую сложно охватить с помощью ключевых фраз.

## Принципы работы

На поиске

В сетях

Для показа на поиске автотаргетинг в режиме реального времени подбирает объявления, у которых заголовок (без дополнительного заголовка), текст и страница перехода более всего соответствуют запросу пользователя. При этом учитывается множество факторов: возможные синонимы, формы слов, родственные тематики, заданные для кампании и группы объявлений [минус-фразы](../keywords/negative-keywords.md) и т. д.

Например, объявление с текстом про путешествия в космос и продвигаемой страницей `в-космос.рф` может быть показано по запросу *туры на марс*.

Для подбора объявлений в сетях автотаргетинг анализирует в первую очередь известную информацию об интересах пользователя. Если этой информации недостаточно (например, пользователь выходит в интернет с нового компьютера или недавно удалил файлы cookie), технология ориентируется на тематику площадки.

Например, объявление о продаже туров на Марс может увидеть пользователь, который интересуется космосом. А пользователь, о котором ничего не известно, увидит такое объявление на странице с похожей тематикой.

#### Почему полезно включать автотаргетинг

Ключевые фразы в сетях позволяют нацелиться только на тех пользователей, которые явно проявляли интерес к тематике, заданной именно этими фразами. Автотаргетинг не опирается на конкретные формулировки и позволяет показывать ваши объявления пользователям, которые интересовались родственными тематиками или похожими товарами. Таким образом, с включенным автотаргетингом вы можете расширить аудиторию показа, не подбирая вручную большого количества ключевых фраз.

Автотаргетинг работает параллельно с ключевыми фразами в равном приоритете. Статистика показов по автотаргетингу будет учитываться отдельно.

Примечание

Автотаргетинг работает эффективнее, если использовать его вместе с конверсионными стратегиями. Для этого установите на сайт счетчик [Яндекс Метрики](../statistics/metrika.md) и настройте в нем цели.

## Настройки автотаргетинга на поиске и в Картах

#### Категории запросов

- **Целевые запросы** — объявление точно отвечает на запросы пользователя. Например, для организации `в-космос.рф` с объявлением «Путешествия в космос» целевым запросом будет *купить путешествие в космос*.
- **Узкие запросы** — объявление шире, чем запросы пользователя. Например, для организации `в-космос.рф` с объявлением «Путешествия в космос» узким запросом будет *купить романтическое путешествие в космос*.

  Ранее узкие запросы относились к целевым. Поэтому в текущих кампаниях с настроенными целевыми запросами будут включены две категории: узкие и целевые. При необходимости это можно изменить.
- **Широкие запросы** — пользователь пишет запрос, не указывая на конкретный продукт, и ваше предложение входит в эту категорию. Например, *выбрать тур*.
- **Альтернативные запросы** — пользователь ищет продукт, который можно заменить на тот, который вы продвигаете. При этом объявление также может удовлетворить запрос. Например, *купить подводный тур*.
- **Сопутствующие запросы** — запросы по продуктам, которые могут быть интересны вместе с продвигаемым товаром или услугой. Н

*[Статья сокращена. Полная версия: docs/impression-criteria/autotargeting.md]*


---

<!-- docs/impression-criteria/retargeting-lists.md -->

# Сегменты аудитории

- [Как работает](../impression-criteria/retargeting-lists.md#how-it-works)
- [Условия формирования сегментов аудитории](../impression-criteria/retargeting-lists.md#zoo)
- [Как создать сегмент аудитории](../impression-criteria/retargeting-lists.md#how-to)
- [Советы по настройке](../impression-criteria/retargeting-lists.md#tips)
- [Назначение ставок](../impression-criteria/retargeting-lists.md#bids)

Сегменты аудитории — это способ показывать объявления только интересующим вас пользователям. Например, с помощью сегментов аудитории вы можете настроить ретаргетинг и показывать объявления только тем пользователям, которые посетили сайт и положили товары в корзину. Выделить группу пользователей можно с помощью Яндекс Метрики и Яндекс Аудиторий.

Объявления по сегментам аудитории будут показываться на поиске и в сетях (РСЯ и внешние сети).

Внимание

Объявления, которые касаются деликатных тем (например, некоторые аспекты медицины, знакомства для взрослых), не показываются по сегментам аудитории в сетях.

## Как работает

##### На поиске

Ретаргетинг на поиске работает совместно с ключевыми фразами или автотаргетингом через логический оператор «И». То есть объявления показываются пользователям, которые соответствуют и условиям ретаргетинга, и условиям показа: ключевым фразам или критериям автотаргетинга. Например, по ключевой фразе *купить диван* и условию ретаргетинга *посетил сайт* объявление покажется пользователю, который напечатал в поиске «купить диван» и уже посещал сайт.

Между собой сегменты аудитории работают через «ИЛИ». Если в условиях показа заданы ключевая фраза и 2 сегмента аудитории, то объявление будет показано пользователю, который и указал в поиске фразу, и попадает в один из сегментов аудитории.

Сегменты аудитории на поиске работают в [Единой перфоманс-кампании](../unified-performance-campaign/create-group.md), а также для [рекламы мобильных приложений](../products-mobile-apps-ads/upc/create-group.md).

##### В сетях

Сегменты аудитории в сетях работают с другими условиями показа через оператор «ИЛИ». То есть объявление будет показываться пользователю, который подходит хотя бы под одно из выбранных условий показа или попадает в настроенный сегмент аудитории.

## Условия формирования сегментов аудитории

Условие формирования сегмента аудитории в Директе представляет собой комбинацию целей/сегментов Яндекс Метрики и сегментов Яндекс Аудиторий, с помощью которых можно описать интересующую вас аудиторию. В Директе можно использовать готовые сегменты Яндекс Метрики и Яндекс Аудиторий или настроить их самостоятельно.

#### Готовые сегменты

Готовые сегменты созданы на базе самых популярных пользовательских сценариев. В зависимости от того, подключен ли у вас счетчик Метрики и какие цели выбраны, можно выбрать одно или несколько условий формирования сегментов аудитории. В сегмент попадают пользователи, выполнившие выбранное условие за последние 540 дней.

- **Подключен счетчик Метрики:**

  - **Посетители** — в сегмент входят пользователи вашего сайта. Возвращайте пользователей, которые когда-то были на вашем сайте. Используйте это условие, чтобы напомнить им о ваших предложениях.
  - **Похожие на посетителей** — привлекайте пользователей, которые потенциально заинтересованы в ваших товарах и услугах или похожи на тех, кто уже посещал ваш сайт. Увеличивайте охват и получайте больше целевых действий, благодаря привлечению заинтересованной аудитории.
- **Указаны цели в настройках стратегии:**

  - **Достигли целей кампании** — показывайте объявления пользователям, которые уже совершали целевые действия на сайте. Например, в кампании выбрана цель — «Звонок». Предложите пользователям, которые уже звонили, скидку или особые условия.
  - **Похожие на достигнувших целей кампании** — расширьте свою аудиторию за счет потенциально заинтересованных в ваших товарах и услугах пользователей. Этот сегмент включает не просто похожих на посетителей сайта, а тех, которые с высокой вероятностью достигнут указанной ва

*[Статья сокращена. Полная версия: docs/impression-criteria/retargeting-lists.md]*


---

<!-- docs/impression-criteria/offer-retargeting.md -->

# Офферный ретаргетинг

- [Как работает](../impression-criteria/offer-retargeting.md#kak-rabotaet)
- [Настройте показы](../impression-criteria/offer-retargeting.md#nastrojte-pokazy)
- [Статистика](../impression-criteria/offer-retargeting.md#statistika)

Офферный ретаргетинг работает для товарных объявлений и страниц каталога в любой тематике. Это могут быть товары, автомобили, объекты недвижимости, услуги или их подборки. Пользователи, которые смотрели предложения или каталоги на сайте, повторно увидят эти предложения и каталоги, а также новые рекомендованные предложения и каталоги в ваших объявлениях в Рекламной сети Яндекса. Если пользователь смотрел на сайте каталоги, система добавит в объявление не только каталоги, но и отдельные предложения из этих каталогов.

Если пользователи взаимодействовали с предложениями или каталогами в [приложении](../web-app/campaign-settings.md#smart-banners), они увидят в Рекламной сети только товарные объявления.

## Как работает

Товарное объявление

Объявление для страниц каталога

- **На основе фида**

  Если в кампании настроена [электронная коммерция](https://yandex.ru/support/metrica/ecommerce/about.html), система сравнит `id` товаров из фида с теми, которые пользователь посмотрел на сайте, и добавит в объявление товары с этими `id` и рекомендованные. Подробнее об [ID товара](../feeds/requirements-yml.md#goods).

  Если электронная коммерция не настроена, по ссылке на товар система определит, какие товары пользователь просмотрел на сайте. Товары из фида с этими ссылками и рекомендованные товары будут добавлены в объявления.
- **С сайта или ручное управление**

  Система по ссылке на товар определит, какие товары пользователь посмотрел на сайте. Товары с этими ссылками и рекомендованные товары будут добавлены в объявления.

- **На основе фида**

  Система по ссылке определит, какие каталоги пользователь просмотрел на сайте. Каталоги из фида с этими ссылками будут добавлены в объявления.
- **С сайта или ручное управление**

  Система по ссылке определит, какие каталоги пользователь посмотрел на сайте. Каталоги с этими ссылками будут добавлены в объявления.

## Настройте показы

В Единой перфоманс-кампании при [создании группы](../unified-performance-campaign/create-group.md) в блоке **Сегменты аудитории** включите опцию офферного ретаргетинга.

В Товарной кампании, [созданной](../product-campaign/create.md) в Мастере кампаний, офферный ретаргетинг включен по умолчанию.

## Статистика

Статистику можно смотреть в Мастере отчетов. Чтобы проанализировать показы, клики, конверсии и другие показатели по офферному ретаргетингу, используйте срез «Условие показа». А в новом Мастере отчетов — группировку «Тип условия показа».

---

<!-- docs/efficiency/geotargeting.md -->

# География показов

- [Как работает геотаргетинг](../efficiency/geotargeting.md#how-it-works)
- [Расширенный географический таргетинг](../efficiency/geotargeting.md#search-and-web)
- [Массовое редактирование регионов показа](../efficiency/geotargeting.md#editing)
- [Геотаргетинг в вашей первой кампании](../efficiency/geotargeting.md#easy-settings)
- [Уточнение регионов и детальная проработка географии](../efficiency/geotargeting.md#hard-settings)
- [Ограничения расширенного геотаргетинга](../efficiency/geotargeting.md#rules)

Эффективность рекламы в Директе зависит не только от привлекательности вашего объявления, но и от возможности конкретного человека на него отреагировать. Как правило, люди интересуются товарами и услугами в тех регионах, где они живут или куда собираются поехать.

## Как работает геотаргетинг

Геотаргетинг — это технология, позволяющая управлять географией показов вашей рекламы. Объявления Директа будут показаны только той аудитории, которая сможет воспользоваться вашим рекламным предложением, так как находится в выбранном регионе показа или интересуется им. Так, если вы доставляете пиццу только в Курске, в настройках кампании или группы объявлений выберите регион показа — Курск. Или укажите более точно регион на карте, например, улицу рядом с вашим магазином и показывайте рекламу тем, кто живет, работает или находится рядом с ним прямо сейчас.

Настроить геотаргетинг можно на уровне группы объявлений в блоке **География показов**.

Страны, области и города

Указать регион на карте

В поле **Перечислить страны, области и города**:

1. Начните вводить название, перейдите к дереву выбора регионов и отметьте регионы для показа объявлений. Установив флажок рядом с регионом, вы выбираете его целиком, включая все входящие в него населенные пункты (даже если они не указаны отдельно в дереве регионов).
2. Если необходимо, добавьте регионы, которые надо **исключить** из показа — начните вводить название области или населенного пункта в поле рядом с регионами показа. Выберите в подсказках или в дереве нужные.

Для исключения из показов можно выбрать любой доступный в настройке регион. Он может и не входить в состав указанного региона показа. Например, можно выбрать для показов Липецкую область и исключить из показов Елец и Грязи.

Дерево выбора регионов

Для каждой новой группы в кампании будут автоматически применены указанные в первой группе настройки регионов.

Укажите регион на карте, если хотите показывать рекламу в конкретном месте, например, рядом с вашим кафе, либо вас интересуют клиенты в узкой области. Например, у вас маленький бизнес без доставки по всему городу. Также лучше выбирать **Указать регион на карте**, если вашего населенного пункта нет в дереве регионов. Стоит помнить, что выбирая регионы на карте, вы рискуете сильно сузить географию показов и потерять потенциальных клиентов.

1. Введите адреса в свободной форме или скопируйте список из другой группы — 100 штук максимум. Адреса также можно указать на карте. Определите радиус показа — от 0,5 км до 10 км около каждого адреса.
2. Укажите, кому именно вы бы хотели показывать рекламу: людям, которые бывают рядом в этом месте регулярно, живут, работают или находятся прямо сейчас. Если вы хотите охватить больше аудитории, выберите тех, кто бывает рядом регулярно, так как в эту группу входят люди, которые живут и работают рядом.

Заменить или удалить существующую точку можно только в группе объявлений:

- Если добавить новую точку, ранее указанные удалятся.
- Если вы указываете несколько точек одновременно и корректируете радиус, он меняется у всех точек.

## Расширенный географический таргетинг

|  |  |
| --- | --- |
|  | Обучающее видео. Как работает расширенный геотаргетинг Посмотреть видео |

В параметрах кампании в блоке **Дополнительные настройки** по умолчанию включена опция **Расширенный географический таргетинг**. Эта опция работает на поиске Яндекса и в сетях. Она не влияет на показы объявлений на поисковых площадках РСЯ (в том числе на стр

*[Статья сокращена. Полная версия: docs/efficiency/geotargeting.md]*


---

<!-- docs/efficiency/timetargeting.md -->

# Временной таргетинг

- [Как настроить временной таргетинг](../efficiency/timetargeting.md#timezone)
- [Показы в праздники и рабочие выходные](../efficiency/timetargeting.md#holidays)
- [Почасовая корректировка](../efficiency/timetargeting.md#hourly-adjustment)

По умолчанию объявления Директа показываются круглосуточно. Это позволяет привлечь внимание большинства потенциальных клиентов. Если вы хотите показывать разные объявления в разное время, используйте временной таргетинг — показ объявлений по расписанию.

> Например, вы рекламируете кафе и в нем действует скидка на доставку после 16 часов. Создайте отдельные рекламные кампании с разными предложениями и временем показа. В первой кампании настройте показы объявлений с утра до вечера для тех, кто хочет пообедать или ищет место пообщаться с друзьями. Во второй — предложение тем, кто хочет заказать еду на дом, и показы с 15 часов до полуночи.

Не ограничивайте рекламную кампанию только временем работы офиса или колл-центра. Потенциальные клиенты могут искать ваши товары и услуги ночью. Настройте показы в нерабочее время и предложите оставить заявку или заказать обратный звонок.

Временной таргетинг ограничивает время показов объявлений, а не кликов по ним. Клик может произойти значительно позже показа, если пользователь, например, оставил вкладку с объявлением на несколько часов, потом вернулся и перешел по нему.

|  |  |
| --- | --- |
|  | Обучающее видео. В какое время лучше показывать объявления Посмотреть видео |

## Как настроить временной таргетинг

В блоке **Расписание показов** на странице параметров кампании укажите, когда вы хотите показывать объявления. Это можно сделать:

- с помощью шаблонов — например, можно настроить показ ежедневно в рабочее время;
- вручную, отметив в таблице дни недели и часы.

Общее время показов должно составлять не менее 8 часов в неделю. Переход на летнее время осуществляется автоматически.

Выберите страну и часовой пояс. Выбранный часовой пояс не влияет на остальные параметры вашей кампании: дата начала кампании и данные отчетов статистики всегда показываются по московскому времени. Для одной кампании можно выбрать только один часовой пояс. Если вы рекламируете свои услуги в городах с разными часовыми поясами, создайте для каждого часового пояса отдельную кампанию.

Даже если вы отключили показ объявлений в определенное время, ставки по их фразам все равно учитываются при расчете прогнозируемой ставки.

## Показы в праздники и рабочие выходные

Вы можете управлять показами в нерабочие праздничные дни: задать отдельное время показов или полностью запретить их. Для этого в блоке **В праздничные дни** выберите подходящий вариант.

Даты праздников соответствуют стране, выбранной в настройках временного таргетинга. Для России, Украины, Казахстана, Беларуси и Турции используются официальные нерабочие праздничные дни и переносы выходных дней по законодательству этих стран, а для других стран — по законодательству России. Праздничным днем считается непосредственно праздничная дата, а также будний день, который стал официальным выходным.

Если в праздники рабочий день переносится на субботу или воскресенье, объявления будут автоматически показываться в рабочий выходной по расписанию соответствующего ему рабочего дня. Чтобы показывать объявления как обычно, в блоке **В рабочие выходные** выберите пункт **По расписанию выходного дня**, для других типов кампаний отключите опцию **Учитывать рабочие выходные**.

## Почасовая корректировка

С помощью почасовой корректировки вы можете настроить автоматическое повышение или понижение ставки, цены целевого действия и доли рекламных расходов в определенные часы. Понять, в какое время и какие корректировки лучше использовать, вам помогут [отчеты Яндекс Метрики](../statistics/metrika.md).

Чтобы добавить корректировку, включите в расписании показов опцию **Корректировка**. Установите размер корректировки, отметьте те часы, когда она должна применяться.

Размер почасовой корректировки вы можете задать в п

*[Статья сокращена. Полная версия: docs/efficiency/timetargeting.md]*


---

<!-- docs/efficiency/text-and-title.md -->

# Заголовок и текст

Правильно составленные заголовок и текст помогут вам привлечь пользователей и повысить *CTR* объявления. В заголовке дайте пользователю понять, что он нашел именно то, что искал. В тексте расскажите подробнее о товаре или услуге, чтобы пользователь смог сделать выбор в вашу пользу. Помните, что заголовок и текст должны соответствовать [требованиям модерации](../moderation/ad-rules.md#ad-grammar).

Заголовок и текст можно добавить в текстово-графические объявления в ЕПК и в Мастере кампаний. Либо сгенерировать их с помощью нейросети — на основе рекламируемой страницы и информации о вашем бизнесе Директ подберет уникальные тексты, которые можно отредактировать.

Текст в объявлении не должен превышать количественные ограничения:

- заголовок — 56 знаков (включая пробелы и знаки препинания), одно слово не более 22 символов;
- дополнительный заголовок — 30 символов и 15 знаков препинания, одно слово не более 22 знаков. Показ дополнительного заголовка не гарантирован;
- текст объявления — 81 символ и 15 знаков препинания, одно слово не более 23 знаков (текст объявления может быть обрезан в зависимости от места показа).

Подробнее об ограничениях для [рекламы мобильных приложений](../products-mobile-apps-ads/recommendations.md).

### Рекомендации по составлению эффективного заголовка и текста

#### Напишите о преимуществах

Расскажите пользователю, почему стоит выбрать именно ваше предложение. Укажите конкурентные преимущества: скидки, акции, условия доставки, гарантию и т. д. Стоимость товара или услуги обозначит ценовой сегмент и исключит нецелевые клики. Название фирмы привлечет внимание, если бренд известный и узнаваемый. Важно, чтобы информация в объявлении была достоверной и подтверждалась на сайте. Если пользователь не сможет сразу найти то, о чем шла речь в объявлении, он уйдет с сайта.

#### Добавьте призыв к действию

Старайтесь побудить пользователя к действию. Оно должно быть простым и ни к чему не обязывать. Сложный призыв, который требует от пользователя больших усилий, не сможет его заинтересовать. Используйте восклицательный или вопросительный знаки, но не злоупотребляйте. Например:

#### Используйте ключевые фразы

Добавьте в заголовок и текст [ключевые фразы](../keywords/keywords.md). В объявлении они будут выделены полужирным шрифтом. Это поможет привлечь внимание пользователей и увеличить отклик на ваше предложение. Выделение работает при показе на поиске и в сетях.

#### Расширьте заголовок

Используйте дополнительный заголовок, чтобы сообщить пользователю больше информации о вашем предложении. Дополнительный заголовок показывается не всегда, поэтому убедитесь, что объявление не теряет смысл и связность без него.

В заголовок объявлений могут быть подставлены и другие элементы объявления ([уточнения](../efficiency/callout.md), [регион](../efficiency/geotargeting.md)) в зависимости от платформы, настроек объявления и [трафарета](../general/positions.md#templates) для конкретного пользователя.

[Экспериментируйте с объявлениями](../efficiency/ad-groups.md) — только на практике можно узнать, какие из них работают лучше.

## Обновили мобильное приложение Директа

Настроить продвижение теперь проще и удобнее, даже если у вас нет опыта

[Скачать приложение](https://redirect.appmetrica.yandex.com/serve/1110145804347161038)

---

<!-- docs/efficiency/images.md -->

# Изображения в объявлении

- [Как добавить изображение](../efficiency/images.md#kak-dobavit-izobrazhenie)
  - [Единая перфоманс-кампания](../efficiency/images.md#upc)
  - [Мастер кампаний](../efficiency/images.md#campaign-master)
- [Смарт-центры](../efficiency/images.md#smart-centr)
- [Изменение пропорций изображения](../efficiency/images.md#ratio)

В Единой перфоманс-кампании, в том числе для продвижения мобильных приложений, в Мастере кампаний и с Простым стартом вы можете добавить к объявлениям изображение. Правильно подобранные изображения привлекают к объявлению больше внимания и помогают быстрее понять суть предложения.

Изображения показываются в сетях ([РСЯ](../general/yan.md) и внешние сети) и в [товарной галерее](../product-gallery/about.md) на поиске.


Иллюстрированные объявления могут выглядеть так:

Текстово-графические объявления

Продвижение мобильных приложений

Формат объявлений зависит от настроек площадки, где показывается реклама. Узнайте больше о различных [форматах рекламных блоков в РСЯ](https://yandex.ru/support/partner2/web/products-rtb/types.html).

## Как добавить изображение

### Единая перфоманс-кампания

В ЕПК изображение можно загрузить в процессе создания или редактирования объявления. В блоке **Изображение** нажмите **Добавить**. Используйте подходящее с сайта или добавьте новое:

- загрузите;
- укажите ссылку;
- выберите из ранее загруженных изображений.

**Технические требования к изображению**

- При соотношении сторон от 1 : 1 до 3 : 4 / 4 : 3 — размер от 450 до 5000 пикселей по каждой стороне.
- При соотношении сторон 16 : 9 — размер от 1080 × 607 до 5000 × 2812 пикселей.
- Максимальный объем файла — до 10 МБ.
- Формат — JPG, PNG или GIF (будет использован только первый кадр).

### Мастер кампаний

В Мастере кампаний изображения можно загрузить в процессе создания или редактирования кампании.

**Технические требования к изображению**

- При соотношении сторон от 1 : 1 до 3 : 4 / 4 : 3 — размер от 450 до 5000 пикселей по каждой стороне.
- При соотношении сторон 16 : 9 — размер от 1080 × 607 до 5000 × 2812 пикселей.
- Максимальный объем файла — до 4 МБ, кроме [Рекламы мобильных приложений](../products-mobile-apps-ads/create.md). Тут допустимый объем — до 10 МБ.
- Формат — JPG, PNG или GIF (будет использован только первый кадр), кроме Рекламы мобильных приложений. Тут только JPG или PNG.

Совет

Чтобы повысить эффективность объявлений, мы рекомендуем использовать изображения, размер которых составляет от 1080 до 5000 пикселей.

После загрузки изображения вам нужно будет выбрать формат. В зависимости от формата меняется соотношение сторон изображения: для стандартного изображения — от 1 : 1 до 4 : 3/3 : 4, для широкоформатного — 16 : 9. Проверьте видимую область изображения. Нажмите кнопку **Сохранить** на странице с выбранным форматом.

Мы рекомендуем создавать два варианта каждого объявления: со стандартным и с широкоформатным изображением. Так вы сможете охватить больше площадок показа. Если у вас только одно изображение, загрузите его в формате 4 : 3.

Для успешного прохождения модерации изображение должно соответствовать [требованиям к оформлению объявления](../moderation/ad-rules.md#pics).

При размещении в рекламном блоке на той или иной площадке изображение может быть уменьшено и обрезано. Если в каком-то из форматов ваше изображение обрезано не так, как вам хотелось бы, задайте [смарт-центры](../efficiency/images.md#smart-centr) вручную.

Добавить изображения сразу в несколько объявлений в ЕПК можно с помощью [XLS/XLSX-файлов](../alternative-interfaces/xls-interface.md) или [Директ Коммандера](../alternative-interfaces/direct-commander.md), через [массовые действия с объявлениями](../campaigns/multi-edit.md) или [API Яндекс Директа](../alternative-interfaces/api.md).

Статистика показов объявлений с изображением доступна в [Мастере отчетов](../statistics/report-wizard.md). Подробнее о том, [как оценить результат кампании](../statistics/performance-stat-guide.md).

Ограничение

При р

*[Статья сокращена. Полная версия: docs/efficiency/images.md]*


---

<!-- docs/efficiency/video.md -->

# Видео

- [Чем полезны видео](../efficiency/video.md#utility)
- [Как добавить видео](../efficiency/video.md#add)
- [Рекомендации при подготовке ролика](../efficiency/video.md#new-desing)
- [Статистика показов](../efficiency/video.md#statistics)
- [Корректировки ставок](../efficiency/video.md#bids-adjustment)

Видео в объявлениях — это короткие (от 5 до 60 секунд) рекламные видеоролики. Снимите свой видеоролик и загрузите его при создании объявления. Видео может быть показано в текстово-графическом объявлении вместо изображения на подходящих площадках и в Видеосети Яндекса. Как при показах любых текстово-графических объявлений Директа, вы платите только за клик.

Кроме Video in banner объявление может быть показано в других форматах:

- Потоковое видео (мультиролл, InStream) — рекламный ролик встраивается в видеопоток и может проигрываться перед основным видео, в середине или в конце.
- Видео в контенте (OutStream) — рекламный ролик встраивается на страницы сайтов.
- Видео в приложениях (Interstitial) — рекламный ролик проигрывается в мобильном приложении перед загрузкой или сменой контента.
- Видео с вознаграждением (Rewarded) — рекламный ролик проигрывается в игровых мобильных приложениях. За просмотр рекламы пользователь получает награду или внутриигровую валюту.

Подробнее о форматах перфоманс-видео можно прочитать в статье [Как сделать перфоманс-рекламу ярче и получать больше конверсий с помощью видео](https://yandex.ru/adv/edu/materials/kak-sdelat-kontekstnuyu-reklamu-yarche).

## Чем полезны видео

**Наглядность**

Используя видео, вы улучшаете восприятие рекламы и можете наглядно показать преимущества вашего товара или услуги. Красочное объявление с видео привлекает больше внимания, чем статичное текстовое объявление.

**Узнаваемость**

Объявления с собственными видеороликами позволят пользователям сформировать позитивное отношение к бренду и создать необходимые ассоциации с компанией или продуктом.

**Учет показов по стандарту IAB и MRC**

Яндекс использует строгие критерии учета видимости: показ видео засчитывается после двух секунд при условии, что не менее 50% площади видеоплеера*\** непрерывно находится в видимой зоне экрана.

## Как добавить видео

Добавить видео можно при создании или редактировании объявления в Единой перфоманс-кампании, в Мастере кампаний, а также с Простым стартом. Загрузите новый ролик или выберите из галереи добавленный ранее либо используйте видео, сгенерированное нейросетью.

Видео должно соответствовать [правилам модерации](../moderation/ad-rules.md#video) и техническим требованиям.

Технические требования к видеоролику

|  |  |
| --- | --- |
| Формат | MP4, WebM, MOV, QT, FLV, AVI |
| Размер | не более 100 Мб |
| Длительность | от 5 до 60 c |
| Рекомендованное соотношение сторон | 16 : 9; 1 : 1; 9 : 16 |
| Минимальное разрешение | 360 p |
| Рекомендованное разрешение | 1080 p |
| Частота кадров | от 20 кадров/с |
| Видеокодеки | H.264, VP6F, VP8, Theora |
| Количество видеодорожек | 1 |
| Минимальное качество | 44 кГц, 16 Кбит/c, стерео |
| Аудиокодеки | AAC, MP3, Vorbis |
| Количество аудиодорожек | не более 1 |
| Кодек файла | avc1, F4V, isom, M4A, M4V, mmp4, mp41, mp42, qt |
| Обложка | Нет |

В формате Video in banner видео будет вписано в отведенный размер автоматически. Если это невозможно, показывается картинка — добавьте ее в блок **Изображение** заранее. Чтобы обеспечить кампании максимальный охват, создавайте в группе объявлений несколько видеокреативов с разным соотношением сторон. Алгоритмы Яндекса выберут наиболее подходящий формат в зависимости от рекламного места

При показах на подходящих площадках Рекламной сети Яндекса заголовок, текст и ссылка объявления будут добавлены к ролику автоматически.

В Видеосети заголовок и текст объявления отображаются так:

- в формате InStream в интерфейсе плеера показываются заголовок объявления, иконка с вашим доменом и кнопка;
- в формате OutStream заголовок и текст могут быть размещены в шапке над роликом или в интерфейсе плеера.

Дл

*[Статья сокращена. Полная версия: docs/efficiency/video.md]*


---

<!-- docs/efficiency/quick-links.md -->

# Быстрые ссылки

- [Чем полезны быстрые ссылки](../efficiency/quick-links.md#about)
- [Как добавлять или редактировать быстрые ссылки](../efficiency/quick-links.md#how-to)
- [Показ быстрых ссылок на мобильных площадках](../efficiency/quick-links.md#mobile)
- [Эксклюзивное размещение](../efficiency/quick-links.md#extended)
- [Советы по использованию быстрых ссылок](../efficiency/quick-links.md#advice)

Быстрые ссылки — это короткий путь к важной информации на вашем сайте. Они дают возможность пользователям сразу попасть на нужную страницу сайта.

Вы можете добавить к объявлению до восьми быстрых ссылок, ведущих на страницы вашего сайта, страницу товара или услуги на Яндекс Маркете или в социальных сетях. Быстрые ссылки показываются как на поиске, так и в сетях (РСЯ и внешние сети). Количество отображаемых быстрых ссылок на разных площадках и устройствах может различаться. Максимальное количество быстрых ссылок показывается в [объявлениях в эксклюзивном формате](../efficiency/quick-links.md#extended) на поиске.

## Чем полезны быстрые ссылки

**Повышают кликабельность объявления без дополнительных затрат**

По нашим данным, объявления с быстрыми ссылками привлекают больше посетителей. При этом быстрые ссылки не требуют увеличения затрат на рекламу — переход по быстрой ссылке оплачивается так же, как и один клик по объявлению. Если пользователь при просмотре объявления кликнет на несколько ссылок, вы заплатите только за один клик.

**Делают навигацию проще**

После добавления быстрых ссылок у вашего объявления появятся дополнительные элементы, которые помогут пользователям сразу перейти в нужные разделы вашего сайта.

**Предлагают больше пространства для продающего текста**

В быстрых ссылках вы можете рассказать о ваших предложениях, описать выгодные условия доставки или добавить другую информацию, которая не уместилась в основной текст объявления.

## Как добавлять или редактировать быстрые ссылки

Единая перфоманс-кампания

Мастер кампаний

Быстрые ссылки можно добавить в настройках кампании, группы или объявления. Для этого в блоке **Дополнительные элементы объявлений** выберите **Быстрые ссылки** нажмите **Добавить** и заполните поля.

- **На уровне кампании** — задайте быстрые ссылки для всей кампании — они будут применяться ко всем группам и объявлениям.
- **На уровне группы объявлений** — при необходимости укажите быстрые ссылки для конкретной группы, и они будут использоваться во всех объявлениях в этой группе. Если отдельные настройки для группы не заданы, они будут наследоваться с уровня кампании по умолчанию.
- **На уровне объявления** — при необходимости задайте быстрые ссылки для конкретного объявления, и они будут применяться только к нему. Если отдельные настройки для объявлений не выбраны, они будут наследоваться с уровня группы или кампании по умолчанию.

Настройки на уровне группы объявлений приоритетнее настроек на уровне кампании, так же как настройки в объявлении приоритетнее настроек на уровне группы или кампании.

> Например, если в кампании пять групп объявлений, можно для четырех из них использовать настройки, которые заданы для кампании, а для одной группы задать другие.

К быстрым ссылкам можно добавить описания — они помогут вам уточнить, куда ведет быстрая ссылка. Обратите внимание, что описания быстрых ссылок показываются только в [объявлениях в расширенном формате](../efficiency/quick-links.md#extended) на десктопах и планшетах.

Текст быстрой ссылки и описания может состоять из букв, цифр и символов, кроме «!», «?», «[», «]». Текст не должен содержать эмодзи. Длина одной быстрой ссылки — до 30 символов. Длина описания — до 60 символов.

Добавить быстрые ссылки сразу в несколько объявлений можно с помощью [XLS/XLSX-файлов](../alternative-interfaces/xls-interface.md), [массовых изменений](../campaigns/multi-edit.md), Директ Коммандера или [API Яндекс Директа](../alternative-interfaces/api.md).

В Директ Коммандере настройка быстрых ссылок есть только **на уровне объявлений**. Поэтому если внести из

*[Статья сокращена. Полная версия: docs/efficiency/quick-links.md]*


---

<!-- docs/efficiency/improve-your-ads.md -->

# Работа с элементами объявления

Качественные объявления помогают не только привлекать целевую аудиторию, но и экономить рекламный бюджет. Такие объявления могут получить больший объем трафика по более низкой цене. Работайте с элементами объявления:

- напишите правильные [заголовок и текст](../efficiency/text-and-title.md);
- добавьте к объявлению [изображения](../efficiency/images.md) и [видео](../efficiency/video.md);
- включите [карусель](../efficiency/carousel.md) изображений;
- настройте [кнопку действия](../efficiency/button.md);
- также добавьте [цены](../efficiency/price.md);
- укажите короткий путь к важной информации на сайте с помощью [быстрых ссылок](../efficiency/quick-links.md);
- настройте [отображаемую ссылку](../efficiency/display-link.md);
- опишите преимущества и особенности с помощью [уточнений](../efficiency/callout.md);
- настройте показ [данных из внешних источников](../efficiency/enrich-ads-with-third-party-data.md).

В настройках кампании или группы добавьте [промоакцию](../efficiency/promotion.md) — она привлечет внимание яркой меткой и обогатит объявление еще одной ссылкой.

В настройках кампании добавьте информацию о [доставке](../efficiency/delivery.md) — она поможет рассказать больше о вашем предложении и привлечет внимание пользователей отдельной меткой в объявлениях в Рекламной сети Яндекса.

*Элементы объявления на изображении — ссылки на разделы Справки, в которых подробнее рассказывается о работе с ними.*

## Smart Design

В Рекламной сети Яндекса работает Smart Design — технология на основе машинного обучения, которая автоматически собирает объявления с разными дополнениями для каждого показа.

Когда посетитель заходит на сайт, алгоритм Smart Design мгновенно анализирует информацию о нем, площадке и данные от рекламодателя и создает наиболее подходящее объявление. Технология решает, нужно ли заменить картинку на видео, добавить больше быстрых ссылок или кнопку с текстом. В результате каждое объявление в форматах с Smart Design будет выглядеть по-разному.

Например:

Smart Design подбирает для показа только те элементы объявления, которые будут актуальны для конкретного пользователя на конкретном сайте в момент показа.

Чтобы сделать объявления более эффективными, мы рекомендуем при создании или редактирования объявления заполнять все доступные поля. Так система сможет составить больше вариантов, актуальных для разных пользователей и ситуаций. Например, добавить изображение, текст и быстрые ссылки одновременно для людей, которые любят изучать объявления, прежде чем перейти по ним.

---

<!-- docs/feeds/about.md -->

# Управление фидами

Фид — это файл с информацией о товарах и услугах. Используйте фид при создании:

- [товарных](../unified-performance-campaign/create-product.md) объявлений и объявлений для [страниц каталога](../unified-performance-campaign/create-catalogs.md) в Единой перфоманс-кампании;
- [товарных кампаний](../campaign-master/product-campaign.md).

Директ проанализирует содержание фида и автоматически сформирует объявления с товарными предложениями для показа на поиске, в РСЯ и товарной галерее.

Ознакомьтесь с информацией о фидах:

- [Типы фидов](../feeds/types.md) — выбрать тип фида.
- [Требования к фиду](../feeds/requirements.md) — как заполнять файл фида.
- [Добавление фида](../feeds/add.md) — как добавить фид в Директ с помощью файла или ссылки.
- [Валидация файла](../feeds/validate.md) — какие условия проверяются при чтении файла.

---

<!-- docs/feeds/types.md -->

# Типы фидов

#### Продажа товаров

|  |  |
| --- | --- |
| **Тип фида** | **Для чего** |
| [Фид Яндекс Маркета (YML)](../feeds/requirements-yml.md)  [Фид в формате Google Shopping (Спецификация RSS 2.0)](../feeds/requirements-other-product.md#google-shopping) | Продажа:   - электроники и аксессуаров; - бытовой техники; - промышленного оборудования; - одежды; - мебели; - товаров для сада и огорода; - спортивных товаров; - строительных материалов; - детских товаров; - шин и дисков; - косметики; - парфюмерии; - прочих товаров и услуг. |
| [Фид «Специальный» Google Рекламы (CSV)](../feeds/requirements-other-product.md#special_1)  [Универсальный фид (CSV)](../feeds/requirements-other-product.md#universal_1) | Любые товары и услуги, кроме:   - отелей; - автомобилей; - недвижимости; - авиабилетов. |

#### Другие категории

|  |  |
| --- | --- |
| **Тип фида** | **Для чего** |
| [Фид «Отели и аренда жилья» Google Рекламы (CSV)](../feeds/requirements-other-categories.md#hotels) | Бронирование отелей |
| [Фид Авто.ру (XML)](../feeds/requirements-other-categories.md#autos) | Продажа новых и подержанных автомобилей |
| [Фид Яндекс Недвижимости (XML)](../feeds/requirements-other-categories.md#real-estate) | Продажа жилой недвижимости |
| [Фид «Авиабилеты» Google Рекламы (CSV)](../feeds/requirements-other-categories.md#tickets) | Продажа авиабилетов |
| [Фид «Путешествия» Google Рекламы (CSV)](../feeds/requirements-other-categories.md#travel) | Продажа туров, билетов на поезда, паромы и т. д. |

---

<!-- docs/feeds/requirements.md -->

# Требования к фиду

- [Продажа товаров](../feeds/requirements.md#goods)
- [Другие категории](../feeds/requirements.md#other)

## Продажа товаров

Общие требования для товарных фидов:

- Каждый товар должен иметь уникальный идентификатор.
- Идентификаторы одного товара в разных фидах должны быть одинаковы, в том числе в и в фидах разных типов. Например, один и тот же товар в фиде Яндекс Маркета и в фиде Google Shopping должен иметь один и тот же идентификатор.

[Фид Яндекс Маркета](../feeds/requirements-yml.md)

[Фид в формате Google Shopping](../feeds/requirements-other-product.md#google-shopping)

[Универсальный фид](../feeds/requirements-other-product.md#universal_1)

[Фид «Специальный» Google Рекламы](../feeds/requirements-other-product.md#special_1)

## Другие категории

[Фид «Отели и аренда жилья» Google Рекламы](../feeds/requirements-other-categories.md#other)

[Фид Авто.ру](../feeds/requirements-other-categories.md#autos)

[Фид Яндекс Недвижимости](../feeds/requirements-other-categories.md#real-estate)

[Фид «Авиабилеты» Google Рекламы](../feeds/requirements-other-categories.md#tickets)

[Универсальный фид](../feeds/requirements-other-categories.md#universal)

[Фид «Специальный» Google Рекламы](../feeds/requirements-other-categories.md#special)

[Фид «Путешествия» Google Рекламы](../feeds/requirements-other-categories.md#travel)

---

<!-- docs/feeds/requirements-yml.md -->

- [Товары](../feeds/requirements-yml.md#goods)
- [Каталоги](../feeds/requirements-yml.md#collections)

# Требования к YML-фиду

## Товары

Общие требования для товарных фидов:

- Каждый товар должен иметь уникальный идентификатор.
- Идентификаторы одного товара в разных фидах должны быть одинаковы, в том числе в и в фидах разных типов. Например, один и тот же товар в фиде Яндекс Маркета и в фиде Google Shopping должен иметь один и тот же идентификатор.

Подробнее о формате YML для фида Яндекс Маркета в [Справке Яндекс Маркета](https://yandex.ru/support/marketplace/ru/assortment/auto/yml?lang=ru).

Любой XML-документ может содержать только один корневой элемент. Формат YML в качестве корневого использует элемент <yml\_catalog>. Атрибут date элемента <yml\_catalog> должен соответствовать дате и времени генерации YML-файла на стороне заказчика. Дата должна иметь формат YYYY-MM-DD hh:mm.

Список товарных предложений содержится в элементе `<offers>`. Каждое товарное предложение описывается отдельным элементом `<offer>`. Элементы `<currencies>` и `<categories>` в элементе `<shop>` нужно указать перед списком товарных предложений. Подробнее о входящих в `<shop>` элементах в [Справке Яндекс Маркета](https://yandex.ru/support/marketplace/ru/assortment/auto/yml).

**Типы описания офера**

Есть два типа описания офера — упрощенный и произвольный. Типы описания оферов отличаются только способом передачи названия товара:

- в оферах упрощенного типа название товара передается с помощью одного элемента `<name>`;
- в оферах произвольного типа название товара передается с помощью трех элементов: `<typePrefix>`, `<vendor>` и `<model>`.

Можно применить комбинированный тип описания, где одновременно используются элементы для упрощенного и произвольного типов. Преимущество: больше элементов для генерации релевантного объявления.

|  |  |  |
| --- | --- | --- |
| **Упрощенный тип** | **Произвольный тип** | **Комбинированный тип** |
| - `<name>`Смартфон Samsung Galaxy S22 Ultra 8/128 ГБ, синий`</name>` | - `<typePrefix>`Cмартфон`</typePrefix>` - `<vendor>`Samsung`</vendor>` - `<model>`Galaxy S22 Ultra 8/128 ГБ, синий`</model>` | - `<name>`Смартфон Samsung Galaxy S22 Ultra 8/128 ГБ, синий`</name>` - `<typePrefix>`Cмартфон`</typePrefix>` - `<vendor>`Samsung`</vendor>` - `<model>`Galaxy S22 Ultra 8/128 ГБ, синий`</model>` |

Внутри одного фида могут одновременно присутствовать оферы упрощенного и произвольного типа.

**Примеры оферов**

Упрощенный тип описания

Произвольный тип описания (vendor.model)

Базовый, более простой тип описания.

**Пример:**

```
  <offer id="0123456" available="true">
    <url>http://www.надежнаятехника.рф/catalog/element/index.php?from=ya_market&utm_source=ya_market&utm_medium=cpc</url>
    <price>1620.00</price>
    <oldprice>1800.00</oldprice>
    <currencyId>RUB</currencyId>
    <categoryId>19</categoryId>
    <picture>http://89.123.45.678/catalog/photo/19/6.JPG</picture>
    <picture>http://89.123.45.678/catalog/photo/19/7.JPG</picture>
    <store>false</store>
    <pickup>true</pickup>
    <delivery>false</delivery>
    <name>Антивирус ESET NOD32 Platinum Edition</name>
    <vendor>Eset</vendor>
    <vendorCode>NOD32-ENA-NS(BOX)-2-1</vendorCode>
    <description>Антивирус ESET NOD32 Platinum Edition - лицензия на 2 года NOD32-ENA-NS(BOX)-2-1</description>
    <video>http://89.123.45.678/catalog/video/19/6.MP4</video>
    <sales_notes>Оплата: Наличные, Б/Н, пластиковые карты, кредит</sales_notes>
    <manufacturer_warranty>true</manufacturer_warranty>
    <country_of_origin>Россия</country_of_origin>
    <age unit="year">18</age>
  </offer>
```

Этот тип описания является наиболее удобным и универсальным, он рекомендован для описания товаров из большинства категорий.

**Пример:**

```
  <offer id="1234567" type="vendor.model" available="true">
    <url>http://www.надежнаятехника.рф/catalog/element/index.php?from=ya_market&utm_source=ya_market&utm_medium=cpc</url>
    <price>889.00</price>
    <oldprice>17000.00</oldpr

*[Статья сокращена. Полная версия: docs/feeds/requirements-yml.md]*


---

<!-- docs/statistics/overview.md -->

# Обзор

- [Сквозная аналитика из Яндекс Метрики](../statistics/overview.md#end-to-end-analytics)
- [Аналитика по кампаниям](../statistics/overview.md#direct-analitics)
- [Аналитика по категориям товаров и услуг](../statistics/overview.md#analitika-po-kategoriyam-tovarov-i-uslug)
- [Настройка отображения данных](../statistics/overview.md#settings)

На странице **Обзор результатов продвижения в Директ** представлена аналитика размещения объявлений в Директе. Она разделена на несколько виджетов, которые помогают отслеживать ключевые показатели размещения и анализировать кампании в разных срезах. В виджеты собирается статистика только кампаний с оплатой за клики.

По умолчанию для аналитики используется модель атрибуции «Последний переход из Директа кросс-девайс». Ее можно изменить на любую другую из [списка](../statistics/attribution-model.md).

Обзор по основным показателям кампаний доступен в [мобильном приложении Директа](https://yandex.ru/support/mobile-app-direct/stat).

## Сквозная аналитика из Яндекс Метрики

В виджете отображаются данные из Метрики за последние 30 дней, если для вашего логина открыт доступ к счетчику. По умолчанию доступны три показателя, по которым можно сравнить результаты продвижения:

- **Клики** — визиты из различных источников.
- **Конверсии** — достижения всех или отдельных целей, настроенных в Метрике.
- **Доходы** — денежная оценка конверсий по всем или отдельным целям. Вкладка появляется, если по целевым действиям в Метрике передается доход.

Данные о доходах и количестве конверсий в Директе и в Метрике могут отличаться, так как используются разные методики расчета.

## Аналитика по кампаниям

В разделе **Аналитика по кампаниям** отображается статистика по данным Директа.

На панели с фильтрами задайте период для анализа показателей на всех виджетах в этом разделе и добавьте фильтры:

- **Цели** — составьте список целей, по которым нужна аналитика в виджетах. Выберите все или отметьте нужные в категориях:

  - **Любые цели** — цели по всем счетчикам Метрики, которые используются в кампаниях.
  - **Цели из кампаний** — цели, которые выбраны как цели стратегии во всех кампаниях, включая архивные.
  - **Цели с указанной ценностью** — цели, у которых задана ценность в Метрике или в Директе, в любой кампании, включая архивные. Например [ключевые цели](../strategies/priority-goals.md).

  Фильтр влияет только на значения показателей «Конверсии», «Цена цели», «Доход», «Прибыль», «ДРР», «Рентабельность».
- **Кампании** — выберите кампании по названию или номеру;
- **Статус кампаний**;
- **Стратегии** — для аналитики кампаний с указанными стратегиями;
- **Места показа** — для аналитики кампаний с выбранными местами показа (поиск, сети или все площадки).

После применения фильтров в виджетах отображаются только данные кампаний, по которым есть статистика за указанный период. Выбранные фильтры сохраняются до следующего посещения страницы.

**Ключевые показатели**

Виджет помогает отслеживать метрики кампаний в динамике. По умолчанию для сравнения на графике выбраны четыре показателя: клики, конверсии,расходы и доходы. Любой из четырех показателей можно изменить — нажать на него и в меню выбрать нужный. Или скрыть лишний. Уровень детализации зависит от выбранного на панели фильтров периода.

**Эффективность продвижения**

Виджет позволяет анализировать результаты продвижения в различных аналитических разрезах. Он состоит из графиков и подробной таблицы.

В виджете доступны 3 вкладки:

- **Кампании** — пузырьковая диаграмма с кликами по оси ординат и расходами по оси абсцисс. Выберите нужный срез справа. Можно анализировать конверсии, доходы, прибыль, рентабельность и другие показатели кампании. Размер круга зависит от значения показателя, выбранного в срезе.
- **Цели** — график для оценки достижения целей по интересующим показателям. На графике отображаются топ-10 целей по выбранной метрике. Доступна статистика по конверсиям, доходам, прибыли, ДРР и другим показателям.
- **Места показа** — график для сравн

*[Статья сокращена. Полная версия: docs/statistics/overview.md]*


---

<!-- docs/statistics/report-wizard.md -->

# Мастер отчетов

- [Как построить отчет](../statistics/report-wizard.md#about)
- [Как настроить графики в отчетах](../statistics/report-wizard.md#graph)
- [Сохранение отчетов](../statistics/report-wizard.md#save)
- [Аналитика по категориям товаров и услуг](../statistics/report-wizard.md#analitika-po-kategoriyam-tovarov-i-uslug)

Мастер отчетов — это удобный инструмент для просмотра статистики. С его помощью можно получить подробную статистику по всем кампаниям и оценить эффективность отдельных ключевых фраз и объявлений.

## Как построить отчет

Для этого перейдите по ссылке **Посмотреть статистику** на странице кампании. Чтобы посмотреть статистику по всем кампаниям, в меню слева выберите **Статистика** → **Статистика по всем кампаниям**.

Примечание

Для отчета нужно накопить статистику показов. Поэтому для объявлений, по которым не было показов, отчет построить нельзя.

#### Задайте период

Вы можете задать интервал дат вручную или выбрать один из предложенных периодов времени.

Кроме того, вы можете посмотреть данные по двум периодам одновременно. Для этого нажмите кнопку  и задайте периоды А и В. Дата окончания периода В должна быть раньше даты начала периода А. Периоды не должны пересекаться между собой.

Обратите внимание, данные статистики доступны за последние 3 года от текущего месяца.

#### Укажите цель и модель атрибуции

Если с вашими кампаниями связан [счетчик Яндекс Метрики](../statistics/metrika.md#settings) и [настроены цели](https://yandex.ru/support/metrica/general/goals.html), то в отчете доступны показатели, характеризующие конверсию кликов в реальные заказы. Выберите цель, по которой вы хотите получить данные о конверсиях. По умолчанию выводятся данные по всем целям.

[Подробнее о конверсиях в отчете](../statistics/performance-stat-guide.md)

Пользователи могут переходить на сайт несколько раз — например, по объявлению, по ссылке в результатах поиска или по закладке, сохраненной в браузере. Атрибуция — это правило, какой из переходов на сайт считать источником визита.

[Подробнее о моделях атрибуции](../statistics/attribution-model.md)

#### Выберите срезы и столбцы

В блоке **Срезы** выберите для каких срезов данных строить отчет. В блоке **Столбцы** выберите интересующие вас статистические показатели.

Например, вы хотите узнать, как распределяются показы и клики по вашим кампаниям среди пользователей разного пола и возраста. В блоке **Срезы** выберите **Кампании**, **Пол**, **Возраст**. В блоке **Столбцы** выберите **Показы**, **Клики**, **CTR**.

Вы можете изменить порядок срезов и столбцов — для этого перетащите их.

#### Добавьте фильтры

Вы можете отобрать данные для показа в отчете, для этого добавьте условия фильтрации.

Например, вы хотите узнать по каким кампаниям поступает больше всего кликов от мужчин старше 45 лет. Сначала в блоке **Срезы** выберите **Кампании**, а в блоке **Столбцы** выберите **Показы**, **Клики**. Затем добавьте условия фильтрации **Возраст** и **Пол**:

Вы можете сохранить фильтр для последующего использования.

Примечание

В одном условии фильтрации можно использовать несколько значений, например, подготовить отчет только для двух ключевых фраз. При вводе фраз разделите их с помощью клавиши «Enter».

## Как настроить графики в отчетах

Данные отчета можно отобразить на графике. Для этого нажмите кнопку **Показать график** над таблицей с отчетом.

#### Виды графиков

Вы можете выбрать линейный график или гистограмму.

Если вы изучаете статистику за длительный период времени, данные не всегда могут отобразиться на гистограммме. В этом случае система по умолчанию строит только линейный график.

#### Отображение данных

Для удобства отображения данные условно разделены по видам измерений на три группы:

- количественные показатели — Показы, Клики, Ср. позиция показа, Ср. позиция клика, Глубина (стр.), Конверсии;
- процентные показатели — CTR (%), Отказы (%), Конверсия (%);
- стоимостные показатели — Расход всего (руб.), Ср. цена клика (руб), Цена цели (руб.), Рентабельность

*[Статья сокращена. Полная версия: docs/statistics/report-wizard.md]*


---

<!-- docs/statistics/conversions.md -->

# Центр конверсий

- [Загрузка данных о конверсиях](../statistics/conversions.md#data-load)
- [Использование идентификаторов JavaScript-целей в качестве статуса заказа](../statistics/conversions.md#javascript-goal)
- [Окно атрибуции конверсии к визитам и окно на изменении информации о конверсии](../statistics/conversions.md#first-load)
- [Как проверить, что все работает?](../statistics/conversions.md#сheck-work)
- [Ошибки при загрузке](../statistics/conversions.md#mistake)
- [Ошибки в файле](../statistics/conversions.md#errors_file)
- [Статистика по конверсиям](../statistics/conversions.md#stat)

Загружайте данные о конверсиях и учитывайте их при настройке кампаний. Соберите все данные о конверсиях из всех источников и анализируйте картину целиком:

- какие конверсии из офлайна или по звонкам принесли объявления в Директе;
- сколько стоили конверсии из Директа.

Все это доступно в Центре конверсий — едином окне для работы с конверсиями из офлайна, по звонкам и из онлайна. В нем можно:

- загружать конверсии из офлайна и по звонкам альтернативными способами отправки данных. Это дополнит сведения Метрики о конверсиях. Подробнее о загрузке [офлайн-конверсии](../strategies/offline-conversions.md) и [конверсий по звонкам](../strategies/call-conversions.md).
- отслеживать статистику по конверсиям, которые загружены через альтернативные способы, по API или через коннекторы. Все данные из Метрики по конверсиям можно выгрузить в Директ.

Чтобы перейти в центр, в меню выберите **Конверсии**.

## Загрузка данных о конверсиях

Данные о конверсиях можно выгрузить из CRM-базы в CSV-файл и добавить через альтернативные способы загрузки в Центр конверсий: с FTP или SFTP-сервера, по ссылке на HTTP или HTTPS или через Google Sheets. Из Центра конверсий данные попадут в Метрику, где по ним будут сформированы конверсии и цели.

Статистика и оптимизация на цели будет доступна для всех логинов Директа, у которых есть доступ к счетчику Метрики, в который загружены данные.

Загрузка состоит из трех этапов:

1. [Сформируйте файл с данными по установленному формату](../statistics/conversions.md#step1).
2. [Загрузите файл в источник](../statistics/conversions.md#step2).
3. [Добавьте ссылку на источник](../statistics/conversions.md#step3).

#### Этап 1. Подготовка файла

Сформируйте файл в формате CSV. Используйте точку с запятой, чтобы разделить колонки в CSV-файле. Например:

id;create\_date\_time;client\_uniq\_id;client\_ids;emails;phones;order\_status;revenue

Название и описание полей:

**Дата и время совершения конверсии. Обязательное поле**

|  |  |  |
| --- | --- | --- |
| **Название** | **Описание** | **Примечание** |
| create\_date\_time | Дата и время создания заказа в часовом поясе счетчика. Значение нельзя менять. | Указывайте дату и время. Если вы не храните в CRM время конверсии, отправляйте только дату. Мы автоматически припишем конверсии время 23:59:59. Это значит, что все конверсии, которые случились за этот день до 23:59:59 мы сможем атрибутировать к визитам. Подробнее о [формате даты и времени](https://yandex.ru/dev/metrika/ru/data-import/date). |

**Идентификаторы пользователя. Обязательно хотя бы одно из полей**

|  |  |  |
| --- | --- | --- |
| **Название** | **Описание** | **Примечание** |
| client\_ids | Список ClientID. Подробно см. в разделе  [Передача подробных данных](https://yandex.ru/dev/metrika/doc/api2/practice/crm/contacts.html#full-data__data). | Если вы передаете заказы, созданные в онлайне, настройте сбор и передавайте ClientID. Это позволит атрибутировать к визитам все конверсии из онлайна. |
| emails | Список адресов электронной почты клиента. Строка латиницей, включающая символ @ и имя домена. Нельзя использовать прописные буквы. Пример: `mail@yandex.ru`.  Чтобы передать несколько значений, оберните их в кавычки и разделите запятой без пробелов. Пример: `"mail@example.com,mail2@example.com"` | Если адрес электронной почты будет указана в неправильном формате, мы не сможем определить, к какому визиту относится конве

*[Статья сокращена. Полная версия: docs/statistics/conversions.md]*


---

<!-- docs/statistics/attribution-model.md -->

# Модели атрибуции

- [Что такое модель атрибуции](../statistics/attribution-model.md#about-title)
- [Какую модель атрибуции выбрать](../statistics/attribution-model.md#select)
- [Модели атрибуции в стратегиях](../statistics/attribution-model.md#strategies)
- [Модели атрибуции в оплате за конверсии](../statistics/attribution-model.md#conversions)
- [Кросс-девайс](../statistics/attribution-model.md#cross-device)
- [Модели атрибуции в статистике](../statistics/attribution-model.md#statistics)
- [Модели атрибуции в статистике медийных объявлений](../statistics/attribution-model.md#brand-statistics)
- [Окно атрибуции для медийных моделей](../statistics/attribution-model.md#window)

Модель атрибуции помогает точнее определить вклад продвижения в развитие вашего бизнеса. Посетители могут переходить на ваш сайт несколько раз и разными путями: например, кликнув по объявлению, по ссылке в результатах поиска или по закладке, сохраненной в браузере. Важно правильно определить [источник перехода](https://yandex.ru/support/metrica/sources/sources-summary.html): только те визиты, источником которых является кампания, учитываются в [статистике](../statistics/campaign-report.md) Директа.

Выбрать модель атрибуции можно:

- в [настройках стратегии](../statistics/attribution-model.md#strategies) для [текстово-графических](../unified-performance-campaign/create-text-image.md), [товарных](../unified-performance-campaign/create-product.md) объявлений и объявлений для [страниц каталога](../unified-performance-campaign/create-catalogs.md) в Единой перфоманс-кампании (по умолчанию установлена автоматическая атрибуция);
- при формировании отчета в [Мастере отчетов](../statistics/report-wizard.md) и во всех стандартных отчетах, кроме «Общей статистики».

В кампаниях, созданных в Мастере кампаний, и в товарных кампаниях по умолчанию установлена автоматическая атрибуция. Изменить ее невозможно.

В [кампаниях с оплатой за конверсии](../strategies/average-cpa.md#conversions) выбор модели атрибуции существенно влияет на то, какие визиты пользователя будут оплачиваться. Смотрите [рекомендации по выбору](../statistics/attribution-model.md#conversions) модели атрибуции для таких кампаний.

## Что такое модель атрибуции

**Модель атрибуции** — это правило, какой переход на сайт считать источником визита:

- **Автоматическая атрибуция** — конверсии, к которым привела кампания, определяются с помощью алгоритмов машинного обучения. Алгоритмы учитывают различные факторы: время до и после конверсии, тип устройства (кросс-девайс), проявление интереса пользователя и членов его семьи ([домохозяйства](../technologies-and-services/crypta.md#household)) к товару или услуге и т. д. Например, утром один член семьи просмотрел товар на мобильном устройстве, позже подробнее почитал об этом товаре на компьютере, переслал ссылку своему партнеру и тот совершил покупку.

  Используйте автоматическую атрибуцию для обучения конверсионных стратегий: она точнее определяет конверсионные клики и портрет аудитории, поэтому может обеспечить больше сигналов для обучения.

  Чтобы решить, нужно ли вам переходить на автоматическую модель атрибуции в уже существующих кампаниях, оцените разницу и качество конверсий в Метрике по уже сформированным отчетам в разрезах отдельных моделей атрибуций. Статистика по автоматической атрибуции доступна по визитам, случившимся начиная с 8 апреля 2023 года.
- **Первый переход** — источником любых визитов посетителя считается его первый переход на сайт за последние 180 дней. Эта модель позволяет отследить источник, который впервые привел клиента и тем самым повлиял на все последующие взаимодействия с сайтом.
- **Последний переход** — источником визита считается переход, в результате которого посетитель в данный момент пришел на сайт, без учета истории визитов. Эта модель может использоваться при техническом анализе сайта. Для модели **Последний переход** окно атрибуции составляет 180 дней.
- **Последний значимый переход** — все источники переходов за последн

*[Статья сокращена. Полная версия: docs/statistics/attribution-model.md]*


---

<!-- docs/statistics/url-tags.md -->

# Параметры URL

- [Что такое параметры URL](../statistics/url-tags.md#about)
- [Как добавить параметры в ссылку](../statistics/url-tags.md#how-add)
- [Метки UTM](../statistics/url-tags.md#utm)
- [Динамические параметры Директа](../statistics/url-tags.md#dynamic)
- [Отчет по меткам в Метрике](../statistics/url-tags.md#reports)

В ссылке объявления Директа можно передавать различные параметры и метки, в том числе UTM-метки. С их помощью можно отслеживать различные статистические показатели (например, источники трафика) и оценивать эффективность кампаний.

## Что такое параметры URL

Параметры URL — это переменные (метки), которые могут быть добавлены в ссылку на продвигаемый сайт. Они позволяют системам веб-аналитики (Яндекс Метрика, Google Analytics и др.) получать дополнительную информацию о переходах по этим ссылкам.

Например, так с помощью параметра вы можете передать Яндекс Метрике информацию о том, что пользователь перешел по ключевой фразе:

Параметр URL — это пара «название = значение». Вы можете указать свои названия (`term`, `block`). Или использовать универсальные метки, например UTM, которые позволяют системам аналитики корректно воспринимать информацию.

В зависимости от задаваемого значения параметры могут быть:

- **статические** — передаваемое значение вы задаете сами, например, `utm_term=sony_playstation` (`utm_term` — название, `sony_playstation` — статическое значение);
- **динамические** — система автоматически подставит необходимые данные, например, `term={keyword}` или `utm_term={keyword}`, где вместо `{keyword}` передается ключевая фраза, по которой произошел показ. Список [динамических параметров Директа](../statistics/url-tags.md#dynamic).

## Как добавить параметры в ссылку

Добавьте нужные параметры к ссылке на сайт, используя операторы `?` и `&`, например:

```
http://www.site.ru/?source=yandex-direct&term={keyword}
```

Название и значение параметров задайте самостоятельно, например, `term=sony_playstation` или `keyword={keyword}`.

Убедитесь, что страницы, на которые ведут получившиеся ссылки, доступны.

Внимание

Кириллические символы, передаваемые в URL, автоматически кодируются в UTF-8. Важно, чтобы ваш сайт корректно принимал запросы в этой кодировке. Когда кириллические символы кодируются в UTF-8, URL увеличивается. Если он превысит 4096 байт, значения будут переданы только для меток [yclid](../statistics/metrika.md#settings) и openstat.

[Как добавить параметры URL в кампании](../statistics/url-tags-for-camping.md)

## Метки UTM

UTM — это стандарт меток для сбора статистики. Основные UTM-метки:

| Название | Описание | Примеры |
| --- | --- | --- |
| `utm_source` | Источник перехода или платформа продвижения, обязательный параметр | `utm_source=yandex`— объявления размещаются в Директе |
| `utm_medium` | Тип продвижения, обязательный параметр | *cpc*, *search*— контекстная реклама; *display*— медийная реклама |
| `utm_campaign` | Название кампании, обязательный параметр; | `utm_campaign=polet_v_kosmos` или `utm_campaign={campaign_id}` |
| `utm_content` | Дополнительная информация, которая помогает различать объявления, необязательный параметр; | Можно использовать несколько значений, разделяя их "|" или ".": `utm_content={position_type}.{position}` |
| `utm_term` | Ключевая фраза, необязательный параметр. | `utm_term={keyword}` |

Добавьте нужные параметры к ссылке на сайт, используя операторы `?` и `&`, например:

```
http://www.site.ru/?utm_source=yandex-direct&utm_medium=cpc&utm_campaign=polet_v_kosmos&utm_term={keyword}
```

#### Рекомендации

- Лучше размещать метки последовательно: первой указывать `utm_source`, затем `utm_medium`, далее `utm_campaign`, `utm_content`, `utm_term`.
- Информация по UTM будет собираться корректно, если заполнить обязательные параметры.
- В значениях используйте латиницу — пишите на английском или транслитерацией, при написании слов на кириллице данные могут искажаться. Не используйте заглавные буквы. Разделяйте слова подчеркиваниями ( \_ ) или дефисами ( 

*[Статья сокращена. Полная версия: docs/statistics/url-tags.md]*


---

<!-- docs/moderation/adv-rules.md -->

# Правила и требования

Все объявления в Директе проходят модерацию — проверку на соответствие требованиям к рекламно-информационным материалам. Ознакомьтесь с приведенными в этом разделе правилами, прежде чем размещать объявления.

**[Товары и услуги, продвижение которых ограничено или запрещено](../moderation/special-categories.md)**

Яндекс не принимает объявления определенных товаров и услуг, а также устанавливает дополнительные правила для некоторых тематик. Это связано с законодательными ограничениями и рекламной политикой Яндекса. Убедитесь, что ваши товары и услуги не попадают в список [запрещенных тематик](../moderation/restricted-categories.md) или узнайте о том, какие документы нужно предоставить, чтобы пройти модерацию.

**[Требования к сайту и оформлению объявления](../moderation/ad-rules.md)**

Изучите правила, касающиеся текстов и ключевых фраз, требования к изображениям и странице перехода, а также другим элементам объявления, чтобы оформить объявление правильно.

**[Предупреждения и возрастные ограничения в объявлениях](../moderation/age-alerts.md)**

Узнайте, к каким объявлениям добавляются предупреждения и возрастные ограничения.


**[Требования к размещению объявлений в формате медийного баннера на новой вкладке Яндекс Браузера](../products-cpm-campaign-frontpage/requirements.md)**

Яндекс не размещает объявления определенных товаров и услуг в формате медийного баннера на новой вкладке Яндекс Браузера, а также устанавливает дополнительные правила для размещения в этом формате.

Рекламно-информационные материалы — текст, ключевые фразы, ссылки — модерируются обычно в течение нескольких часов. Чем больше объявлений содержит кампания, тем больше времени требуется на их модерацию.

Результаты модерации вы получите по электронной почте и сможете увидеть в интерфейсе в статусе вашей кампании.

Если действия рекламодателя подвергают риску Яндекс, пользователей или партнеров, его аккаунт в Директе может быть заблокирован. Подробнее о [причинах блокировки](../moderation/block.md).

Внимание

Cписок правил и требований приведен в документах:

- [Общие положения. Требования к рекламно-информационным материалам](https://yandex.ru/legal/general_adv_rules/);
- [Правила размещения объявлений на Яндексе](https://yandex.ru/legal/adv_rules/);
- [Требования к рекламно-информационным материалам в Директе](https://yandex.ru/legal/direct_adv_rules/);
- [Правила показа объявлений в Директе](http://yandex.ru/legal/direct_display_rules/).

---

<!-- docs/moderation/technical-restrictions.md -->

# Технические ограничения

- [Ограничения для объявлений](../moderation/technical-restrictions.md#text-graph)
- [Ограничения для кампании и аккаунта](../moderation/technical-restrictions.md#company-account-limit)
- [Видео](../moderation/technical-restrictions.md#video)
  - [Видео в текстово-графических объявлениях в Единой перфоманс-кампании, Мастере кампаний, медийных кампаниях](../moderation/technical-restrictions.md#video-table)
  - [Видео про товар в Единой перфоманс-кампании и товарной кампании](../moderation/technical-restrictions.md#product-video)
- [Изображения](../moderation/technical-restrictions.md#images)
- [Баннеры](../moderation/technical-restrictions.md#banner-search)
  - [Баннеры в графических объявлениях](../moderation/technical-restrictions.md#banner-image)
  - [Баннеры в медийной кампании](../moderation/technical-restrictions.md#banner-media)
  - [Баннеры в медийной кампании с фиксированным СРМ](../moderation/technical-restrictions.md#banner-graph)
- [Технические требования к HTML5-баннерам](../moderation/technical-restrictions.md#html5)
- [Рекомендации к отображению HTML5-баннеров](../moderation/technical-restrictions.md#html5-recomended)

## Ограничения для объявлений

Максимальное количество знаков, включая пробелы:

**Текстово-графические объявления в Единой перфоманс-кампании**

- заголовок — 56 знаков (включая пробелы и знаки препинания), одно слово не более 22 символов;
- дополнительный заголовок — 30 символов и 15 знаков препинания, одно слово не более 22 знаков;
- текст объявления — 81 символ и 15 знаков препинания, одно слово не более 23 знаков (текст объявления может быть обрезан в зависимости от места показа);
- ссылка — 1024 знака (включая протокол);
- отображаемая ссылка — 20 знаков (не включая домен);
- уточнения —  25 знаков с учетом пробелов, общая длина уточнения для одного объявления должна быть не более 132 символов для показов на десктопах и не более 66 — на мобильных устройствах;
- быстрая ссылка —   30 знаков (заголовок), описание — не более 60 знаков.

**Продвижение приложений**

- заголовок — 56 знаков (включая пробелы и знаки препинания), одно слово не более 22 символов;
- текст объявления — 75 знаков, одно слово не более 23 знаков;
- ссылка — 1024 знака (включая протокол);
- трекинговая ссылка — 1024 знака (включая протокол).

## Ограничения для кампании и аккаунта

**Ключевые фразы**

Длина ключевой фразы не может быть больше 4096 символов (включая [минус-слова](../keywords/negative-keywords.md), пробелы и операторы Директа). Количество фраз на группу — не более 200. Количество слов для одной ключевой фразы — не более 7.

**Минус-фразы на группу**

В списке минус-фраз можно использовать не более 4096 символов без учета пробелов. Количество слов для одной минус-фразы — не более 7.

**Минус-фразы в Мастере кампаний**

- Продвижение приложений: количество фраз на группу — не более 200;
- Продвижение сайта: максимально допустимое количество символов — 20 000 без учета пробелов.

**Минус-фразы на кампанию**

В списке минус-фраз можно использовать не более 20 000 символов без учета пробелов. Количество слов для одной минус-фразы — не более 7.

**Группа объявлений**

В каждой кампании может быть до 1000 групп.

**Количество объявлений**

В каждой группе может быть до 50 объявлений.

**Кампании**

На одном аккаунте может размещаться до 3000 кампаний, из них — не более 1000 активных (активными считаются все кампании, за исключением находящихся в архиве).

## Видео

### Видео в текстово-графических объявлениях в Единой перфоманс-кампании, Мастере кампаний, медийных кампаниях

Для размещения текстово-графических объявлений в Единой перфоманс-кампании, продвижения приложений с видео, видео про магазин в товарной кампании, видеорекламы в медийных кампаниях подходят видеоролики:

|  |  |
| --- | --- |
| Формат | MP4, WebM, MOV, QT, FLV, AVI |
| Размер | не более 100 Мб |
| Длительность | от 5 до 60 c |
| Рекомендованное соотношение сторон | 16 : 9; 1 : 1; 9 : 16 |
| Минимальное разрешение | 360

*[Статья сокращена. Полная версия: docs/moderation/technical-restrictions.md]*


---

<!-- docs/moderation/age-alerts.md -->

# Предупреждения и возрастные ограничения в объявлениях

- [Предупреждения в текстово-графических объявлениях](../moderation/age-alerts.md#warnings)
- [Возрастные ограничения в текстово-графических объявлениях](../moderation/age-alerts.md#age)
- [Предупреждения и возрастные ограничения в графических объявлениях, медийных баннерах, видеорекламе](../moderation/age-alerts.md#image-ads-and-video)
- [Остались вопросы?](../moderation/age-alerts.md#questions)

## Предупреждения в текстово-графических объявлениях

В рекламу медицинской деятельности, медицинских изделий, лекарственных средств, заменителей женского молока и питания для младенцев, БАДов, конструктивно сходных с оружием изделий, финансовых услуг, долевого строительства и новостроек, сертификации, букмекерской деятельности, банкротства, взыскания долгов с физических лиц, дистанционной торговли необходимо добавлять предупреждения. Например:

- Есть противопоказания. Посоветуйтесь с врачом.
- Для детей с 11 месяцев. Грудное вскармливание предпочтительнее. Посоветуйтесь с врачом.
- Не является лекарством.
- Конструктивно сходные с оружием изделия.
- Проектная декларация на сайте [https://наш.дом.рф/](https://xn--80az8a.xn--d1aqf.xn--p1ai/). Застройщик ООО «Дом на Марсе».
- Финансовые услуги оказывает: ООО «Банк».
- Изучите все условия кредита (займа) на сайте в соответствующем разделе. Оцените свои финансовые возможности и риски.
- ООО «Сертификат», № RA.RU.12АБ34.
- Информация об организаторе азартных игр, правилах проведения, сроках, порядке определения выигрыша и максимально допустимом его значении, месте и порядке получения выигрышей на рекламируемом сайте.
- Банкротство влечет негативные последствия, в том числе ограничения на получение кредита и повторное банкротство в течение пяти лет. Предварительно обратитесь к своему кредитору и в МФЦ.
- Взаимодействие только по почте согласно п. 3 ч. 1 ст. 4 ФЗ от 03.07.2016 № 230-ФЗ.
- Продавец: Продавцов Продавец Михайлович ИНН 9876543210

В текстовые объявления, в том числе с [видео](../efficiency/video.md), предупреждения добавляются автоматически. В графические объявления в Единой перфоманс-кампании, медийные баннеры и видеорекламу их необходимо добавлять самостоятельно.

Чтобы в рекламу дистанционной продажи товаров или интернет-магазина сведения о продавце добавились автоматически, создайте [профиль в Яндекс Бизнесе](../efficiency/vcards.md#edit) и привяжите его в рекламной кампании.

Если рекламируемые вами товары и услуги не относятся ни к одной из перечисленных категорий, но к объявлениям добавилось предупреждение, пожалуйста, напишите нам через [форму обратной связи](../troubleshooting/shows.md), чтобы удалить его.

## Возрастные ограничения в текстово-графических объявлениях

Возрастные ограничения должны быть указаны во всех объявлениях, которые рекламируют информационную продукцию:

- игры, фильмы;
- концерты, спектакли, спортивные матчи и другие зрелищные мероприятия;
- печатные издания (газеты, журналы и книги);
- программы и передачи на ТВ и радио;
- базы данных и компьютерные программы.

Возрастная отметка 16+ добавляется на объявления автоматически. Для тематик, относящихся к взрослому контенту, по умолчанию будет добавлена отметка 18+.

Отметка «Для детей с 11 месяцев. Грудное вскармливание предпочтительнее. Посоветуйтесь с врачом» будет добавлена в рекламе товаров детского питания.

Если ваша продукция предлагается к использованию с более раннего возраста, вы можете изменить это ограничение самостоятельно на странице рекламной кампании. Пример:

Если рекламируемые вами товары и услуги не относятся ни к одной из перечисленных категорий, но к объявлениям добавилась отметка, напишите нам через [форму обратной связи](../troubleshooting/shows.md), чтобы удалить ее.

## Предупреждения и возрастные ограничения в графических объявлениях, медийных баннерах, видеорекламе

В графических объявлениях в Единой перфоманс-кампании, медийных баннерах, видеорекламе должна присутствовать вся информация, необходимая согласно требо

*[Статья сокращена. Полная версия: docs/moderation/age-alerts.md]*


---

<!-- docs/payments/payment-methods.md -->

# Способы оплаты

Выберите страну, чтобы ознакомиться с доступными способами оплаты.

Россия

Физические лица, включая самозанятых

Юридические лица, включая ИП

Банковский перевод

1. В меню нажмите кнопку **Пополнить**. В открывшемся окне введите сумму платежа, выберите **Другие способы оплаты** и нажмите кнопку **Пополнить счет**.

   Важно

   В соответствии с требованиями закона «О рекламе», необходимо предоставлять информацию о плательщике, включая его полное имя, отчество и фамилию, а также идентификационный номер налогоплательщика (ИНН). Эти сведения будут передаваться в Единый реестр интернет-рекламы (ЕРИР).
2. В следующем окне выберите способ оплаты **По счету** → **Выставить счет.**
3. Система сформирует счет и квитанцию для его оплаты. Квитанцию можно распечатать, загрузить в формате Word или получить по электронной почте. Реквизиты квитанции можно использовать для оплаты счета в любом отделении банка или в системе интернет-банкинга.

- При оплате сумма и реквизиты плательщика обязательно должны соответствовать указанным в счете. Если вы хотите оплатить счет на другую сумму, сформируйте в интерфейсе новую квитанцию.
- При оплате в отделении банка убедитесь, что ваш платеж правильно проведен и на оплаченной квитанции в отметке операциониста указан полный и точный номер вашего счета. Без этих данных невозможно установить, что оплата поступила от вас, и мы не сможем автоматически зачислить деньги на общий счет вашего аккаунта.
- Платеж зачисляется в течение 2–3 рабочих дней, в зависимости от банка, проводящего платеж.

Оплата картой

1. В меню нажмите кнопку **Пополнить**. В открывшемся окне введите сумму платежа, выберите **Банковской картой** и нажмите кнопку **Пополнить счет**.

   Важно

   В соответствии с требованиями закона «О рекламе», необходимо предоставлять информацию о плательщике, включая его полное имя, отчество и фамилию, а также идентификационный номер налогоплательщика (ИНН). Эти сведения будут передаваться в Единый реестр интернет-рекламы (ЕРИР).
2. В открывшемся окне выберите карту или добавьте новую, а затем подтвердите платеж. Для удобства сохраните данные новой банковской карты.

К оплате принимаются банковские карты Visa, EuroCard/MasterCard и МИР.

Максимальный размер платежа составляет 299 999 рублей.

Платеж происходит в режиме реального времени и зачисляется от 15 минут до часа.

Совет

Включите [автоплатеж](../payments/shared-account.md#autopayment) для общего счета, чтобы кампания не останавливалась из-за недостатка средств.

Система быстрых платежей

1. В меню нажмите кнопку **Пополнить**. В открывшемся окне введите сумму платежа, выберите **Банковской картой** и нажмите кнопку **Пополнить счет**.

   Важно

   В соответствии с требованиями закона «О рекламе», необходимо предоставлять информацию о плательщике, включая его полное имя, отчество и фамилию, а также идентификационный номер налогоплательщика (ИНН). Эти сведения будут передаваться в Единый реестр интернет-рекламы (ЕРИР).
2. Средства зачисляются так же быстро, как при оплате картой, при этом не нужно вводить реквизиты. QR-код появится после выбора СБП как способа оплаты:

- Если открыли QR-код на компьютере, отсканируйте его телефоном через приложение вашего банка или камерой.
- Если производите оплату со смартфона, выберите из списка банк, которым пользуетесь. Откроется приложение соответствующего банка с экраном оплаты счета.

Максимальный размер платежа составляет 299 999 рублей с НДС, минимальный — 300 рублей.

Платеж происходит в режиме реального времени и зачисляется от 15 минут до часа.

Оплата наличными с помощью кода платежа

Код платежа — это идентификатор, позволяющий физическим лицам быстро оплатить продвижение. Получить код платежа могут только резиденты РФ и только для оплаты счета из России.

Минимальная сумма оплаты составляет 300 рублей без учета НДС, максимальная — 12 000 рублей. Зачисление платежа занимает от 15 минут до часа.

Чтобы получить код платежа:

1. В меню нажмите кнопку **Пополнить**. В открывшемся о

*[Статья сокращена. Полная версия: docs/payments/payment-methods.md]*


---

<!-- docs/payments/promocode.md -->

# Промокод

- [Где получить промокод](../payments/promocode.md#how-to-get)
- [Условия использования промокода](../payments/promocode.md#conditions)
- [Как активировать промокод](../payments/promocode.md#activation)

Промокод позволяет клиентам из России, Казахстана, Беларуси и Узбекистана получить дополнительную сумму для оплаты продвижения в Директе.

Для использования промокода необходимо выставить и оплатить счет на размещение рекламно-информационных материалов в течение 30 календарных дней с момента активации промокода.

Полученный промокод не может быть передан третьим лицам на возмездной или безвозмездной основе.


## Где получить промокод

Вы можете получить промокод в рамках рекламной акции от Яндекса, Яндекс ОФД или от партнера Яндекса.

Наши партнеры в России: Альфа-Банк, Модульбанк, Открытие, Т-Банк, LPmotor, NetHouse и другие.

## Условия использования промокода

Промокод выдается на определенных условиях и на определенный срок. Проверьте условия акции в сопроводительных информационных материалах перед активацией промокода.

Промокод для новых рекламодателей

Промокод для действующих рекламодателей

Скидка по промокоду для запуска первой кампании предоставляется при выполнении следующих условий:

- Аккаунт рекламодателя ранее не использовался в Директе.
- Яндекс ранее в течение 365 дней не оказывал рекламодателю услуг по размещению рекламно-информационных материалов со ссылкой на информационный ресурс в интернете и/или контактной информацией о рекламодателе.
- Дополнительные условия, указанные в сопроводительных информационных материалах.

Промокод не может быть использован для продвижения:

- [мобильных приложений](../products-mobile-apps-ads/about.md);
- нескольких сайтов;
- кампаний без сайта;
- домена третьего уровня (например, `мойсайт.хостинг.рф`);
- страницы в социальных сетях.

Если после запуска продвижения на аккаунте рекламодатель изменит домен или настроит редирект на другой домен в любой из активных кампаний, то активированный промокод будет аннулирован.

Скидка по промокоду предоставляется при выполнении следующих условий:

- У рекламодателя есть аккаунт в Директе.
- Сумма бюджета кампании в месяце, в котором рекламодатель воспользовался промокодом, должна быть не меньше суммы, указанной в сопроводительных информационных материалах.
- Дополнительные условия, указанные в сопроводительных информационных материалах.

Заменить промокод или продлить срок его действия невозможно.

## Как активировать промокод

Один рекламодатель может активировать только один промокод.

Чтобы активировать промокод:

1. [Создайте кампанию](../quick-start/quick-start.md) и отправьте ее на проверку.

   Дождитесь результатов модерации. Промокод не может быть применен прежде, чем будут проверены ваши объявления.
2. На странице пополнения счета введите сумму бюджета кампании. Сумма (без учета НДС) должна быть не меньше суммы, указанной в условиях акции.
3. Введите промокод и выберите способ оплаты с подходящим плательщиком (физическое или юридическое лицо).

   Проверьте, что плательщик и способ оплаты соответствуют условиям акции.
4. Подтвердите свое согласие с условиями [оферты](https://yandex.ru/legal/oferta_direct/). Нажмите кнопку **Пополнить счет**.
5. Оплатите счет в течение 30 календарных дней с момента его выставления.

---

<!-- docs/technologies-and-services/vcg-auction.md -->

# Как работает аукцион в Директе

- [Отбор и ранжирование объявлений](../technologies-and-services/vcg-auction.md#adv-choose)
- [Определение списываемой цены](../technologies-and-services/vcg-auction.md#calculate-price)
  - [VCG-аукцион](../technologies-and-services/vcg-auction.md#calc-vcg)
  - [VCG-аукцион для расширенного формата](../technologies-and-services/vcg-auction.md#vcg-traf)
  - [GSP-аукцион](../technologies-and-services/vcg-auction.md#calc-gsp)

Директ — это система размещения поисковых и тематических контекстных объявлений. Вы платите за клики по объявлениям, которые показываются в блоках на поиске Яндекса и в сетях ([РСЯ](../general/yan.md) и внешние сети).

Стоимость кликов в Директе не фиксирована, а определяется в результате торгов между рекламодателями. Рекламодатели устанавливают ставки в валюте, а торги проходят во внутренних единицах Директа. Ставки конвертируются во внутренние единицы в режиме реального времени. Конвертация происходит по курсу Центрального банка РФ, установленному для соответствующей валюты на текущую дату.

Аукцион проходит в режиме реального времени, пока пользователь загружает страницу с результатами поиска или страницу с блоками РСЯ или внешних сетей. Аукцион включает несколько этапов.

## Отбор и ранжирование объявлений

Объявления отбираются отдельно для каждого блока для размещения объявлений на странице, которую открывает пользователь. Объявления ранжируются по комбинации ставки, коэффициента качества и прогноза CTR для конкретного показа. В блок попадает объявление с лучшим сочетанием показателей.

## Определение списываемой цены

Списываемая цена определяется по-разному для разных блоков:

- на поиске Яндекса и на поисковых площадках РСЯ списываемая цена определяется по правилам [VCG-аукциона](../technologies-and-services/vcg-auction.md#calc-vcg);
- на тематических площадках РСЯ и во внешних сетях списываемая цена определяется по правилам [GSP-аукциона](../technologies-and-services/vcg-auction.md#calc-gsp).

### VCG-аукцион

Правила VCG-аукциона используются для определения списываемой цены на поиске Яндекса, а также на поисковых площадках РСЯ. Далее описан расчет списываемой цены на примере блока [Премиум-показы (Спецразмещение)](../general/positions.md#sr).

В зависимости от конкуренции по конкретному поисковому запросу в блоке может показываться от 0 до 4 объявлений. Если в премиум-показах 4 места, то первое место приносит объем трафика 100 единиц, а второе, третье и четвертое — 85, 75 и 65 единиц соответственно. Объем трафика — это величина, прямо пропорциональная кликабельности места показа объявления. Он не постоянен и вычисляется для конкретного запроса. При расчете объема трафика учитываются дизайн объявления, количество объявлений в блоке и их дизайн, место показа объявления на поиске.

> Если пять рекламодателей конкурируют за 4 места в премиум-показах (без расширенных форматов), их ставки по ключевой фразе равны 10, 7, 5, 3 и 2 руб., а коэффициенты качества и прогнозы CTR объявлений совпадают, то в блок попадут четыре рекламодателя с наибольшими ставками. Количество кликов по объявлениям и средняя стоимость этих кликов будет зависеть от места рекламодателя в блоке:
>
> - Каждый из четырех победивших рекламодателей получает объем трафика 65 единиц. За этот трафик рекламодателям не нужно конкурировать. Цена этого минимального трафика определяется ставкой пятого конкурента, который не вошел в блок (2 рубля за клик).
> - Дополнительный объем трафика 10 единиц, который приносит третья позиция относительно четвертой, гарантированно получат три рекламодателя с наивысшими ставками. За эти клики с ними конкурирует четвертый рекламодатель. Ставка четвертого рекламодателя (3 рубля) обуславливает цену этого дополнительного объема трафика.
> - Увеличение объема трафика на 10 единиц дает подъем с третьей позиции на вторую — это трафик, который гарантированно получат два рекламодателя с наивысшими ставками. Конкуренцию за этот трафик им обеспечивает третий рекламодатель. Ставка трет

*[Статья сокращена. Полная версия: docs/technologies-and-services/vcg-auction.md]*


---

<!-- docs/technologies-and-services/antifraud.md -->

# Защита от недействительного трафика

- [Обновление антифрода для кампаний в РСЯ и Поиске](../technologies-and-services/antifraud.md#about)
- [Алгоритм работы системы антифрода](../technologies-and-services/antifraud.md#algoritm-raboty-sistemy-antifroda)
  - [До перехода на сайт](../technologies-and-services/antifraud.md#do-perehoda-na-sajt)
  - [После перехода на сайт](../technologies-and-services/antifraud.md#posle-perehoda-na-sajt)
- [Учет недействительного трафика в статистике](../technologies-and-services/antifraud.md#statistics)
- [Какие действия пользователей антифрод не фильтрует](../technologies-and-services/antifraud.md#conversions)

Недействительный трафик в рекламных системах — это клики и конверсии, не связанные с реальным интересом пользователей. Такой трафик вреден для рекламодателей, так как может привести к потере бюджета, искажению статистики и трате времени на обработку недействительных заявок.

Недействительный трафик делится на два типа:

- **Фродовый трафик** — преднамеренные мошеннические действия, направленные на обман рекламодателя, например:

  - клики, совершенные с помощью ботов или мошеннического программного обеспечения;
  - клики мотивированных пользователей, выполняющих задания за деньги.
- **Случайный трафик** — ненамеренные клики пользователей по рекламе, которые не имеют ценности для рекламодателя (например, повторные клики по одному баннеру).

Такой трафик удаляется из отчетов статистики в Директе, плата за него не взимается. Фродовые конверсии не учитываются при обучении стратегии.

## Обновление антифрода для кампаний в РСЯ и Поиске

Эффективное продвижение — это процесс, результат которого зависит от всех участников рынка:

- Площадки внедряют технологии для эффективного поиска потенциальных клиентов и борьбы с мошенничеством.
- Яндекс Директ постоянно совершенствует алгоритмы, чтобы точнее подбирать аудиторию и площадки для показа объявлений. А система антифрода помогает фильтровать фродовый трафик.

Ранее антифрод в Директе защищал бюджет рекламодателей. Алгоритм работал ретроспективно — анализировал поведение пользователя после перехода на сайт. Недействительные показы, клики и конверсии исключались из статистики Директа. Однако система не предотвращала попадание такого трафика на сайт.

Теперь антифрод не только защищает бюджет, но и снижает риски перехода недействительного трафика на сайт рекламодателя.

## Алгоритм работы системы антифрода

### До перехода на сайт

**Этап 1. До показа объявления**

С помощью агрегированных данных о поведении пользователей мы можем заранее распознавать недействительный трафик и блокировать его. Если система уверена, что перед ней бот или мошенник, объявления не показываются.

**Этап 2. При клике по объявлению**

Если взаимодействие с объявлением вызывает подозрение, система проверит пользователя с помощью капчи.

### После перехода на сайт

Если фродовый трафик все же попал на сайт, система определяет его автоматически благодаря многоуровневой фильтрации. Кроме того, если во время визита на сайте оставили заявку с некорректными данными, например несуществующим номером телефона, это тоже будет считаться недействительным трафиком.

Фродовые действия удаляются из отчетов Директа и не участвуют в обучении стратегий.

Все визиты на сайт, включая фродовые, записываются в CRM и системы аналитики. Поэтому в них вы можете увидеть фродовую активность, которая уже отфильтрована в отчетах Директа.

## Учет недействительного трафика в статистике

Расходы за недействительный трафик автоматически возвращаются на баланс общего счета, а отфильтрованные показы, клики и конверсии удаляются из всех отчетов статистики Директа.

Вы можете просмотреть количество кликов и конверсий, отсеянных системой антифрода, в [Мастере отчетов](../statistics/report-wizard.md), в отчетах **Общая статистика** и **Поисковые запросы** в строке **Недействительные клики и конверсии** за весь выбранный период. Эта цифра может меняться со временем в случае признания части кликов недействительн

*[Статья сокращена. Полная версия: docs/technologies-and-services/antifraud.md]*


---

<!-- docs/technologies-and-services/metrika-in-direct.md -->

# Яндекс Метрика

- [Цели и сегменты Метрики](../technologies-and-services/metrika-in-direct.md#data)
- [Что можно настроить с помощью Метрики](../technologies-and-services/metrika-in-direct.md#purposes)

[Яндекс Метрика](https://metrika.yandex.ru/) — инструмент веб-аналитики, с помощью которого можно собирать данные о визитах и посетителях вашего сайта. Для этого нужно [создать и установить счетчик](https://yandex.ru/support/metrica/quick-start.html#get-code) — код, который встраивается на страницы сайта. Данные счетчика можно использовать для настройки стратегий и аудитории в кампаниях Директа.

[Узнайте больше об отчетах по затратам на продвижение](https://yandex.ru/support/metrica/sources/direct-clicks.html)

## Цели и сегменты Метрики

В Директе можно использовать созданные в Метрике цели (поведение пользователей) и сегменты (пользователи с определенными характеристиками).

##### **Цели**

Цели позволяют отслеживать конкретные действия посетителей сайта, например:

- просмотр нескольких страниц товаров за один визит;
- посещение страницы со скидками;
- нажатие кнопки «Положить в корзину».

Чтобы создать цель, в настройках счетчика Метрики на вкладке **Цели** нажмите **Добавить цель**.

Подробнее о [целях](http://yandex.ru/support/metrica/reports/add-goals.html) в Справке Метрики.

##### **Сегменты**

Посетителей сайта с определенными характеристиками можно выделить в сегмент Метрики. Например, можно сгруппировать:

- посетителей, пришедших на сайт из социальных сетей;
- пользователей мобильных устройств;
- посетителей-женщин от 18 до 25 лет из Владивостока.

Чтобы создать сегмент Метрики,перейдите к любому отчету и настройте условия отбора визитов и людей. Например, так можно отобрать посетителей, которые пришли на сайт из социальных сетей.

После этого нажмите **Сегмент** → **Сохранить как** и укажите название сегмента.

Подробнее о [сегментах](https://yandex.ru/support/metrica/general/segmentation_report.html) в Справке Метрики.

## Что можно настроить с помощью Метрики

Данные Метрики, собираемые со страниц сайта, можно использовать для настройки ретаргетинга и автоматических стратегий.

##### **Ретаргетинг и подбор аудитории**

Вы можете показывать объявления тем, кто уже взаимодействовал с вашим сайтом. Например, можно рассказать о скидке на следующую покупку тем, кто уже заказывал товары на сайте. Или предложить посетителям, которые просматривали сайт с мобильных устройств, удобное приложение.

Для этого вы можете использовать цели и сегменты Метрики. На странице редактирования объявления нажмите **Ретаргетинг и подбор аудитории** → **Добавить**. Подробнее об [ретаргетинге и подборе аудитории](../impression-criteria/retargeting-lists.md).

##### **Автоматические стратегии**

Самые важные клики для бизнеса — те, которые приводят к полезному действию пользователя. Например, к добавлению товара в корзину или к оформлению заказа. В Метрике можно настроить цели, соответствующие полезным действиям, и по ним рассчитать бюджет кампании.

Для этого в Директе созданы автоматические стратегии [Максимум конверсий](../strategies/average-cpa.md#average-cpa) и [Максимум кликов](../strategies/average-cpc.md). Вам нужно только указать в настройках стратегии цель и значение для соответствующего показателя (например, цены конверсии). После этого система будет подбирать ставки и ключевые фразы, чтобы приблизить среднее значение показателя за неделю к заданному и принести как можно больше конверсий.

Примечание

---

<!-- docs/general/positions.md -->

# Места для продвижения в результатах поиска

- [Трафареты](../general/positions.md#templates)
- [В каком трафарете показывается объявление](../general/positions.md#conditions)
- [Примеры форматов объявлений в результатах поиска](../general/positions.md#examples)
- [Узнайте больше](../general/positions.md#uznajte-bolshe)

Пользователи ищут в интернете разные товары и услуги. В результатах поиска им показываются контекстные объявления. Такое продвижение точно попадает в интерес пользователя, прямо отвечая на его запрос подходящим объявлением.

Объявление показывается в результатах поиска Яндекса и на поисковых сайтах партнеров Рекламной сети — как на компьютерах, так и на планшетах и смартфонах.

На страницах результатов поиска Яндекса объявления могут быть показаны в следующих блоках:

##### **Премиум-показы (Спецразмещение)**

Блок расположен над результатами поиска. Также он может быть расположен на первых позициях в тематических блоках в результатах поиска и в Теме Поиска «Финансы».

Показы в этом блоке приносят наибольшее количество кликов.

##### **Остальные показы**

Объявления, не попавшие в блок Премиум-показы (Спецразмещение), могут показываться в середине или внизу страницы в момент поиска, а также когда пользователь вернулся к результатам выдачи.

Объявления также могут быть показаны в результатах поиска во вкладке **поиск с алисой** в блоке с ответами Алисы.

##### **Динамические места на поискеβ**

Дополнительные места показа рекламы, которые находятся в результатах органической поисковой выдачи. Они дают возможность получать дополнительные клики и конверсии за счет повышения видимости продвигаемой страницы. [Подробнее](../general/dynamic-places.md)

## Трафареты

Чтобы сделать объявления более привлекательными, Директ использует *трафареты* — разные варианты дизайна страницы с результатами поиска, которые отличаются расположением и форматом блоков. Каждый раз, когда человек хочет найти товар или услугу, алгоритм подбирает наиболее подходящий трафарет и формирует под него блоки.

От выбранного трафарета и от места вашего объявления в нем зависит [объем трафика](../troubleshooting/bidding.md). Объявления над результатами поиска приносят больше кликов, чем внизу страницы, а объявления в [расширенном формате](../general/positions.md#extended) — больше, чем обычные.

## В каком трафарете показывается объявление

Объявления отбираются отдельно для каждого блока. Они ранжируются на основе *ставки за клик*, *коэффициента качества*, *прогноза CTR* для каждого показа. В блок попадает объявление с лучшим сочетанием показателей. На поиске Яндекса и поисковых площадках РСЯ средняя цена, которую вы платите за клик по объявлению, определяется по правилам [VCG-аукциона](../technologies-and-services/vcg-auction.md#calc-vcg).

Чем больше [дополнительных элементов](../efficiency/improve-your-ads.md) вы добавили в объявление, тем больше трафаретов вам доступно. Например, для показа в расширенном формате объявление должно содержать [быстрые ссылки](../efficiency/quick-links.md) с описаниями.

В Директе постоянно проводятся эксперименты, и форматов для продвижения становится больше. Каждый новый формат проходит несколько этапов тестирования и оценивается по множеству метрик качества поиска и рекламного трафика. Чтобы увеличить потенциальный охват, используйте все возможные дополнительные элементы, выбирайте оптимальную для вашего бизнеса ставку или подходящую автоматическую стратегию, и система подберет наилучшее место и формат показа.

## Примеры форматов объявлений в результатах поиска

#### Обычный формат

Объявления показываются со всеми дополнениями (быстрые ссылки, контактная информация, отображаемая ссылка). Уточнения отображаются в объявлении только при показе на первой позиции.

#### Эксклюзивное размещение

Самый большой и заметный вариант показа объявления. Он появляется над результатами поиска и занимает единственное место для продвижения.

На компьютере

В мобильном

**Объявление в расширенном формате**

На компьютере

В 

*[Статья сокращена. Полная версия: docs/general/positions.md]*


---

<!-- docs/general/yan.md -->

# О Рекламной сети Яндекса и внешних сетях

- [Преимущества рекламы в сетях](../general/yan.md#yan-advantages)
- [Что нужно знать о показах в сетях](../general/yan.md#yan-whats-important)
- [Партнеры РСЯ](../general/yan.md#yan-partners)
- [Узнайте больше](../general/yan.md#uznajte-bolshe)

Рекламная сеть Яндекса (РСЯ) — это система размещения рекламы на сервисах Яндекса и площадках партнеров. РСЯ открывает рекламодателям Директа доступ к аудитории более чем 50 000 площадок: сайтов, мобильных приложений и приложений Connected TV. Партнеры Рекламной сети получают доход за размещение рекламы, а рекламодатели — приток трафика и клиентов.

Помимо Рекламной сети Яндекса, объявления Директа могут быть показаны на тематических площадках внешних партнерских сетей, например [Smaato](https://www.smaato.com/company/).

## Преимущества рекламы в сетях

#### Качественные и посещаемые ресурсы

Яндекс внимательно проверяет каждую площадку, на которой могут быть показаны объявления Директа. К участию не принимаются площадки с сомнительным контентом и созданные специально для заработка на размещении рекламы. Каждая площадка проходит многоступенчатую модерацию и подключается к мониторингу качества.

#### Новая аудитория и огромный охват

Среднесуточная аудитория площадок Рекламной сети — более 65 млн пользователей, из которых более 50% посетителей не пересекаются с аудиторией Яндекса.

#### Большой выбор форматов

На площадках Рекламной сети размещается как контекстная, так и медийная реклама. Предусмотрен отдельный набор форматов для показов на мобильных сайтах и в мобильных приложениях, а также видеореклама на площадках [видеосети](../general/yan.md#partner-video).

#### Точное нацеливание

Гибкие настройки условий показа помогают найти для каждого рекламодателя правильную аудиторию. Технологии машинного обучения подбирают для каждого посетителя интересные ему предложения.

#### Защита бюджетов

Автоматическая проверка качества трафика и видимости рекламы, защита от склика и накрутки показов — специалисты Яндекса постоянно отслеживают фрод и совершенствуют защиту рекламодателей. [Автоматическая корректировка ставок](../impressions/automatic-bid-adjustment-in-yan.md) позволяет сэкономить, снижая вашу ставку, если вероятность конверсии невелика.

## Что нужно знать о показах в сетях

Площадки подбираются на основе тематического или поведенческого таргетинга, то есть тематика объявления соответствует либо тематике страницы, которую просматривает посетитель сайта или пользователь приложения, либо его интересам и поведению в интернете.

Рекламодатели не могут самостоятельно выбрать площадки для показа, но могут исключить нежелательные площадки в параметрах кампании. Мы не рекомендуем исключать какие-либо площадки, это риск потерять целевую аудиторию. Автоматический контроль качества кликов и конверсий не позволит перерасходовать бюджет на некачественный трафик.

Выбор формата для показа на конкретном рекламном месте находится на стороне партнера, но рекламодатель может оценить внешний вид своих объявлений с помощью превью в интерфейсе.

Цена клика в сетях зависит от качества аудитории площадки, конкурентной ситуации, количества площадок нужной тематики в сети на данный момент. При работе с большинством стратегий Директа рекламодатель может регулировать расход бюджета в сетях, [ограничивая стоимость клика](../strategies/manual-strategy.md#yan-settings).

## Партнеры РСЯ

Место для размещения рекламы предоставляют сервисы Яндекса, например [Почта](https://mail.yandex.ru/), [Погода](https://yandex.ru/weather/), [Картинки](https://yandex.ru/_images/), [Видео](https://yandex.ru/portal/video), [Игры](https://yandex.ru/games/), [Браузер](https://browser.yandex.ru/), [Авто.ру](https://auto.ru/), [Спорт](https://yandex.ru/sport), [Музыка](https://music.yandex.ru/).

Среди партнеров РСЯ крупнейшие сайты:


И мобильные приложения:


###

Партнеры видеосети Яндекса:


Реклама может быть показана в блогах и каналах авторов ВКонтакте, RUTUBE, Telegram и YouTube.

*[Статья сокращена. Полная версия: docs/general/yan.md]*


---

<!-- docs/products-cpm-campaign/about.md -->

# Медийные баннеры

Медийная реклама — баннерная реклама с оплатой за показы, направленная на создание определенного образа бренда в глазах потребителей.

## Преимущества медийной рекламы в Яндекс Директе

##### **Нацеливание на нужную аудиторию**

Гибко и точно настраивайте показ баннеров по важным [пользовательским характеристикам](../products-cpm-campaign/display-ads-settings.md) — интересам в интернете, доходу, полу и возрасту. Показы можно нацеливать даже на тех, кто взаимодействовал с вашим сайтом или посещал определенные места.

Кроме того, баннеры могут показываться по ключевым фразам.

##### **Удобное создание баннера**

Соберите баннеры с нуля в [конструкторе креативов](../products-image-ads/builder.md), в том числе автоматически на основе материалов вашего сайта, или загрузите собственные креативы в формате HTML5, GIF, PNG, JPEG.

##### **Оплата только за реальные показы**

Яндекс использует строгие [критерии учета видимости](../technologies-and-services/iab-compliance.md#shows): показ баннера засчитывается только в случае, если не менее 50% площади баннера (для баннеров размером 242 500 или более пикселей — не менее 30% площади) непрерывно находится в видимой зоне экрана не менее одной секунды.

Яндекс применяет [многоступенчатые фильтры](../technologies-and-services/antifraud.md) для отсеивания недобросовестных и ошибочных показов и кликов.

##### **Кросс-сценарии коммуникации с аудиторией**

Вы можете собрать сегмент пользователей, [видевших медийный баннер](../products-cpm-campaign/retargeting-cpm-campaign.md), и продолжить взаимодействие с ними — например, обратиться к ним с помощью контекстной рекламы.

---

<!-- docs/reach-campaigns.md -->

# Охватные кампании

- [Медийная реклама](./branding.md) — продвижение, нацеленное на знакомство с брендом, привлечение внимания и рост целевых действий.
- [Реклама в телеграм-каналах](./efficiency/telegram-ads.md) — продвижение в публичных и закрытых телеграм-каналах партнеров Рекламной сети Яндекса.
- [Наружная рекламаβ](./dooh.md) — запуск рекламы на различных поверхностях на улицах города.

---

<!-- docs/glossary.md -->

# Глоссарий

При размещении объявлений в Директе вы будете встречаться со специальными терминами.

По алфавиту

По темам

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | [C](./glossary.md#C-en) | [O](./glossary.md#O-en) | [P](./glossary.md#P-en) | [R](./glossary.md#R-en) | [W](./glossary.md#W-en) |  |  |  |  |  |  |  |  |  |  |  |
|  | [A](./glossary.md#A-ru) | [Б](./glossary.md#B-ru) | [В](./glossary.md#V-ru) | [Г](./glossary.md#G-ru) | [Д](./glossary.md#D-ru) | [Е](./glossary.md#Е-ru) | [К](./glossary.md#K-ru) | [М](./glossary.md#M-ru) | [О](./glossary.md#O-ru) | [П](./glossary.md#P-ru) | [Р](./glossary.md#R-ru) | [С](./glossary.md#S-ru) | [Т](./glossary.md#T-ru) | [У](./glossary.md#U-ru) | [Ф](./glossary.md#F-ru) | [Ц](./glossary.md#TS-ru) |

#### CTR (кликабельность, от англ. Click-Through Rate)

Отношение числа кликов на объявление к числу его показов измеряется в процентах. Можно сказать, что этот показатель определяет эффективность работы объявления.

#### CPM (цена за тысячу показов, от англ. Cost per Mille)

Смотрите термин [Цена за тысячу показов](./glossary.md#cpm).

#### Performance-продвижение

Продвижение, направленное на достижение измеримого результата, такого как рост продаж, целевых действий на сайте, установок приложения.

#### ROI (коэффициент возврата инвестиций, от англ. Return on Investments)

Смотрите термин [Рентабельность инвестиций](./glossary.md#roi).

#### wCTR

См. [Взвешенный CTR](./glossary.md#wctr)

#### [Автотаргетинг](./impression-criteria/autotargeting.md)

Технология показа объявлений на поиске и в  сетях, не использующая ключевые фразы. Она анализирует информацию в объявлении и на странице перехода и определяет, соответствует ли объявление поисковому запросу, интересам пользователя или тематике площадки. Автотаргетинг позволяет получить дополнительный целевой трафик благодаря показам аудитории, которую сложно охватить с помощью ключевых фраз.

#### [Быстрые ссылки](./efficiency/quick-links.md)

Короткий путь к важной информации на вашем сайте. Они дают возможность пользователям сразу попасть на нужную страницу сайта.

#### Взвешенный CTR (wCTR)

Показатель кликабельности, скорректированный с учетом объемов трафика на позициях, где показываются объявления.

wCTR = КликиВзвешенные показы\frac{Клики}{Взвешенные\ показы}Взвешенные показыКлики

Взвешенные показы — это показы, скорректированные на объем трафика. То есть вес каждого показа определяется с учетом объема трафика позиции, на которой показывалось объявление. Чем больше объем трафика, тем выше вес показа.

Взвешенные показы = Трафик1100+Трафик2100+...+ТрафикN100\frac{Трафик\_1}{100} + \frac{Трафик\_2}{100} + ... + \frac{Трафик\_N}{100}100Трафик1+100Трафик2+...+100ТрафикN, где

Трафик100\frac{Трафик}{100}100Трафик — вес показа.

#### [Видео в объявлении](./efficiency/video.md)

Видеоролики, которые показываются в текстово-графических объявлениях вместо изображения. Загрузить или выбрать из сгенерированных нейросетью видео можно в Единой перфоманс-кампании, Мастере кампаний и Простом старте. Видео в объявлении показывается в [видеосети](./general/yan.md#partner-video) и других подходящих площадках Рекламной сети Яндекса.

#### Видеосеть Яндекса

Сервисы Яндекса и более 200 площадок [Рекламной сети](./general/yan.md#partner-video) — сайты телеканалов, онлайн-кинотеатры и другие ресурсы. Реклама показывается только в легальном контенте проверенных партнеров.

#### Вовлеченные сессии

Оценка вероятности целевых действий на сайте, на котором установлен счетчик Яндекс Метрики. Рассчитывается с помощью алгоритмов машинного обучения на основе данных Яндекс Метрики. [Показатели ВС](./statistics/report-wizard-engagement-rating.md) характеризуют заинтересованность посетителей сайта в ваших товарах и услугах.

#### Группа объявлений

Несколько вариантов объявлений, для которых заданы общие условия показа и настройки.

#### Динамическая 

*[Статья сокращена. Полная версия: docs/glossary.md]*


---

<!-- docs/quick-start/quick-start.md -->

# Начинающим

Яндекс Директ поможет привлечь потенциальных клиентов, которые заинтересованы в ваших товарах или услугах. Вы можете разместить объявления, даже если у вас нет сайта.

|  |  |  |
| --- | --- | --- |
| [Запустите свое первое объявление](../products-automatic/about.md) | [Помощь профессионалов](../quick-start/get-help.md) | [Гид по интерфейсу](../new-interface/guide.md) |
| [Вопросы по интерфейсу](../troubleshooting/interface.md) |
| [Вопросы по трафику и ставкам](../troubleshooting/bidding.md) |
| [Вопросы и ответы](../troubleshooting/advices.md) | [Решаем проблемы с доступом](../troubleshooting/access.md) |

Простой и быстрый способ самостоятельно разместить объявление — [Мастер кампаний](../campaign-master/about.md). На основе данных вашего сайта или мобильного приложения Мастер подскажет, как настроить кампанию, и предложит варианты оформления объявлений.

---

<!-- docs/quick-start/create-campaign.md -->

# Создайте аккаунт

- [Создайте логин](../quick-start/create-campaign.md#login)
- [Настройте аккаунт в Директе](../quick-start/create-campaign.md#account)

## Создайте логин

Для работы в Директе мы рекомендуем создать отдельный логин. Не используйте личные логины (например, для Яндекс Почты или Яндекс Диска): в дальнейшем перенести объявления с вашего логина на другой будет невозможно.

[Создать логин](https://passport.yandex.ru/passport?mode=register&origin=direct)

## Настройте аккаунт в Директе

**Выберите страну и валюту**

Выберите вашу страну. Для некоторых стран нужно еще выбрать валюту расчетов с Директом. Все расчеты будут производиться только в выбранной валюте.

Для разных стран и валют доступны разные [способы оплаты](../payments/payment-methods.md).

**Добавьте email и номер телефона**

Укажите актуальный адрес электронной почты и номер телефона. Нажмите **Подтвердить номер.**

Так вы сможете оперативно получать информацию об изменениях и советы по настройке.

Ознакомьтесь с условиями [Политики конфиденциальности](https://yandex.ru/legal/confidential/), [Договора об обработке данных при продвижении мобильных приложений](https://yandex.com/legal/direct_dpa_ch/) и [Оферты на оказание услуг Яндекс Директ](https://yandex.ru/legal/oferta_direct/?lang=ru).

Нажмите кнопку **Начать пользоваться сервисом**.

## Обновили мобильное приложение Директа

Настроить продвижение теперь проще и удобнее, даже если у вас нет опыта

[Скачать приложение](https://redirect.appmetrica.yandex.com/serve/1110145804347161038)

---

