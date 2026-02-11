# Yandex Direct Documentation (RU)

Полная документация Яндекс.Директа на русском языке, конвертированная в Markdown.

## Содержание

**509 страниц** документации, организованных по разделам:

| Раздел | Описание | Файлов |
|--------|----------|--------|
| `strategies/` | Стратегии показов (автоматические и ручные) | 27 |
| `campaigns/` | Управление кампаниями, настройки | 19 |
| `efficiency/` | Повышение эффективности рекламы | 35 |
| `keywords/` | Ключевые фразы и операторы | 8 |
| `impression-criteria/` | Критерии показа, автотаргетинг, ретаргетинг | 6 |
| `impressions/` | Ставки, бюджеты, прогнозы | 6 |
| `feeds/` | Управление фидами | 10 |
| `moderation/` | Модерация и правила рекламы | 60+ |
| `payments/` | Оплата и взаиморасчёты | 13 |
| `statistics/` | Статистика и отчёты | 19 |
| `unified-performance-campaign/` | Единая перфоманс-кампания | 17 |
| `campaign-master/` | Мастер кампаний | 7 |
| `telegram-ads/` | Реклама в Telegram | 8 |
| `products-mobile-apps-ads/` | Продвижение мобильных приложений | 18 |
| `products-cpm-campaign*/` | CPM-кампании (охват, видео, баннеры) | 30+ |
| `technologies-and-services/` | Технологии (аукцион, антифрод, Крипта) | 12 |
| `troubleshooting/` | Решение проблем | 21 |
| `agencies/` | Для агентств | 4 |
| `alternative-interfaces/` | API, Директ Коммандер, XLS | 4 |
| И другие... | brand-lift, search-lift, visit-lift, DOOH, vendor | 30+ |

## Источник

Документация получена с [yandex.ru/support/direct/ru/](https://yandex.ru/support/direct/ru/) по sitemap.xml.

Каждый файл содержит YAML front matter с полем `source:` — ссылку на оригинальную страницу.

## Формат файлов

```markdown
---
source: https://yandex.ru/support/direct/ru/strategies/select-strategy
---

# Стратегии показов

Контент статьи в Markdown...
```

## Обновление

Для повторного скрапинга используйте скрипт `scripts/scrape.py`.

## Дата скрапинга

2026-02-11
