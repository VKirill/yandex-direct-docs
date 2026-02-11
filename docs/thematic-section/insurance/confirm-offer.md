---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/confirm-offer
---

Подтверждение предложения ОСАГО

# Подтверждение предложения ОСАГО

- [Формат запроса](ru/thematic-section/insurance/confirm-offer#request-format)
  - [ReturnUrls](ru/thematic-section/insurance/confirm-offer#returnurls)
- [Успешный ответ](ru/thematic-section/insurance/confirm-offer#200-ok)
  - [PartnerInfo](ru/thematic-section/insurance/confirm-offer#partnerinfo)
  - [OfferStatus](ru/thematic-section/insurance/confirm-offer#offerstatus)
  - [UpsaleInfo](ru/thematic-section/insurance/confirm-offer#upsaleinfo)
  - [UpsaleOption](ru/thematic-section/insurance/confirm-offer#upsaleoption)
  - [RiskPayment](ru/thematic-section/insurance/confirm-offer#riskpayment)

Метод для подтверждения предложения ОСАГО по идентификатору запроса (используется не всеми партнерами).

## Формат запроса

```
POST osago/offer
```

Пример запроса

```
{
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "offer_id": "string",
    "return_urls": {
        "success_url": "https://example.com/osago/success",
        "failure_url": "https://example.com/osago/failure"
    },
    "upsales": [
        {
            "upsale_id": "string",
            "option_id": "string"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор предложения. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `return_urls` | Ссылки для возврата после оплаты. | [ReturnUrls](ru/thematic-section/insurance/confirm-offer#returnurls) |  |
| `upsales` | Массив кросс-продаж, выбранных к предложению. | `object[]` |  |

### ReturnUrls

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `failure_url` | URL для редиректа при ошибке. | `string` | `URI`. Пример: `https://example.com/osago/failure`. |
| `success_url` | URL для редиректа при успехе. | `string` | `URI`. Пример: `https://example.com/osago/success`. |

## Успешный ответ

**200 OK**

Формат ответа

```
{
    "offer_id": "44234899",
    "partner": {
        "code": 12,
        "name": "Банки.ру",
        "logo_url": "//partner.ru/ugc/logo_135x85.gif"
    },
    "price": 7072,
    "status": "CREATED",
    "is_prolongation": true,
    "is_ext_prolongation": false,
    "is_reinsurance_pool": false,
    "draft_url": "https://partner.ru/policy?id=112233",
    "payment_url": "https://pay.it/policy?id=112233",
    "policy_series": "ХХХ",
    "policy_number": "0166171796",
    "message": "Требуется указать действительный адрес проживания",
    "upsales": [
        {
            "id": "112234",
            "is_required": true,
            "upsale_code": "AccidentPassengersPoolForEOsago150",
            "short_name": "Страхование пассажиров",
            "full_name": "Страхование пассажиров от несчастного случая при ДТП",
            "insured": "Все, кто находился в машине в момент ДТП, до 5 человек",
            "insurance_period": "1 год",
            "options": [
                {
                    "id": 1,
                    "is_default": false,
                    "compatibility_id": 1,
                    "name": "Страхование пассажиров",
                    "description": "Страхование пассажиров от несчастного случая при ДТП",
                    "insured": "Все, кто находился в машине в момент ДТП, до 5 человек",
                    "risk_payments": [
                        {
                            "risk": "Смерть в результате несчастного случая",
                            "pays": [
                                "100% страховой суммы"
                            ]
                        }
                    ],
                    "price": 1480
                }
            ]
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор. | `string` | Пример: `44234899`. |
| `partner` | Информация о партнере, который является страховщиком. | [PartnerInfo](ru/thematic-section/insurance/confirm-offer#partnerinfo) |  |
| `status` | Текущий статус обработки предложения ОСАГО. | [OfferStatus](ru/thematic-section/insurance/confirm-offer#offerstatus) |  |
| `draft_url` | Ссылка на черновик полиса в формате PDF. | `string` | Пример: `https://partner.ru/policy?id=112233`. |
| `is_ext_prolongation` | Является ли предложение пролонгацией от другой компании. | `boolean` | Пример: `false`. |
| `is_prolongation` | Является ли предложение пролонгацией. | `boolean` | Пример: `true`. |
| `is_reinsurance_pool` | Входит ли предложение в перестраховочный пул. | `boolean` | Возможные значения:   - `true` — входит; - `false`, `null` — не входит.   Если предложение входит в перестраховочный пул, то кросс-продажи обязательны, их отмена влечет отмену предложения. |
| `message` | Сообщение об ошибке / иные сообщения. | `string` | Пример: `Требуется указать действительный адрес проживания`. |
| `payment_url` | Ссылка на оплату. | `string` | Пример: `https://pay.it/policy?id=112233`. |
| `policy_number` | Номер полиса. | `string` | Пример: `0166171796`. |
| `policy_series` | Серия полиса. | `string` | Пример: `ХХХ`. |
| `price` | Цена. | `number` | Пример: `7072`. |
| `upsales` | Массив предложений кросс-продаж. | [UpsaleInfo](ru/thematic-section/insurance/confirm-offer#upsaleinfo) |  |

### PartnerInfo

Информация о партнере.

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `code` | Код. | `integer` | Пример: `12`. |
| `logo_url` | Ссылка на логотип. | `string` | Пример: `//partner.ru/ugc/logo_135x85.gif`. |
| `name` | Наименование партнера. | `string` | Пример: `Банки.ру`. |

### OfferStatus

Текущий статус обработки предложения ОСАГО. Группы статусов:

1. Создание и расчет:

- `CREATED` — предложение создано;
- `PRE_CALC_SENT` — отправлено на предварительный расчет;
- `PRE_CALC_IN_PROGRESS` — расчет выполняется;
- `PRE_CALC_READY` — предварительный расчет готов;
- `APPROVED` — предложение подтверждено;
- `REJECTED` — предложение отклонено.

2. Оплата:

- `PAYMENT_READY` — готово к оплате (ссылка получена);
- `PAYMENT_LINK_FAILED` — не удалось получить ссылку на оплату;
- `PAYMENT_COMPLETED` — оплачено;
- `PAYMENT_CANCELLED` — оплата отменена.

3. Финальные статусы:

- `CLOSED_PAID` — успешно завершено (оплата);
- `CLOSED_OTHER_OFFER` — клиент выбрал другое предложение;
- `CLOSED_TIMEOUT` — закрыто по таймауту;
- `OFFER_ERROR` — ошибка обработки.

### UpsaleInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `full_name` | Полное название кросс-продажи. | `string` | Пример: `Страхование пассажиров от несчастного случая при ДТП`. |
| `id` | Идентификатор кросс-продажи. | `string` | Пример: `112234`. |
| `insurance_period` | Период страхования. | `string` | Пример: `1 год`. |
| `insured` | Застрахованные объекты/лица. | `string` | Пример: `Все, кто находился в машине в момент ДТП, до 5 человек`. |
| `short_name` | Короткое название кросс-продажи. | `string` | Пример: `Страхование пассажиров`. |
| `is_required` | Является ли кросс-продажа обязательной для оформления полиса. | `boolean` | Пример: `true`. |
| `options` | Массив опций кросс-продажи. | [UpsaleOption](ru/thematic-section/insurance/confirm-offer#upsaleoption) | Пользователь может выбрать одну из опций. |
| `upsale_code` | Код кросс-продажи. | `string` | Пример: `AccidentPassengersPoolForEOsago150`. |

### UpsaleOption

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `compatibility_id` | Идентификатор совместимости опции кросс-продажи. | `integer` | Каждой опции кросс-продажи может быть выдан идентификатор совместимости. Если в конечном наборе выбранных кросс-продаж и их опций есть те, чьи `compatibility_id` различны, эти кросс-продажи несовместимы. Пример: `1`. |
| `description` | Описание опции кросс-продажи. | `string` | Пример: `Страхование пассажиров от несчастного случая при ДТП`. |
| `id` | Идентификатор опции кросс-продажи. | `integer` | Пример: `1`. |
| `insured` | Застрахованные объекты/лица. | `string` | Пример: `Все, кто находился в машине в момент ДТП, до 5 человек`. |
| `is_default` | Является ли опция включенной по умолчанию. | `boolean` | Если для кросс-продажи есть `is_required = true`, то данная опция обязательна и включена как `read only`. |
| `name` | Название опции. | `string` | Пример: `Страхование пассажиров`. |
| `price` | Страховая премия опции. | `number` | Пример: `1480`. |
| `risk_payments` | Массив рисков и страховых сумм. | [RiskPayment](ru/thematic-section/insurance/confirm-offer#riskpayment) |  |

### RiskPayment

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `pays` | Массив страховых сумм. | `string[]` | Пример: `[ "100% страховой суммы" ]`. |
| `risk` | Название риска. | `string` | Пример: `Смерть в результате несчастного случая`. |

[Стандартные коды ответов](ru/thematic-section/insurance/responce-codes)

#### Остались вопросы?

Внимание

Специалисты отдела клиентского сервиса могут вас проконсультировать только по кампаниям того логина, с которого вы обращаетесь. Логин можно увидеть, если открыть [ya.ru](http://ya.ru/) на соседней вкладке браузера. Специалист получит доступ к вашим данным только при обработке обращения.

Сканируйте QR-код или нажмите на него для перехода по ссылке.


При выборе Telegram, WhatsApp учитывайте, что Яндекс не контролирует, как сторонние мессенджеры хранят ваши данные и переписку на своей стороне, и не несет за это ответственность.

Написать в Viber

|  |  |
| --- | --- |
|  | Для обращений из Республики Беларусь |

[Написать в чат](https://yandex.ru/chat#/user/840c4ce4-ed25-4c66-a7c7-ba8c001e02d9?utm_source=pay)

Позвонить

Клиентам и представителям агентств можно связаться с нами круглосуточно по телефонам:

**Регионы России**: [8 800 700-47-45](tel:88007004745) (звонок из России бесплатный)

**Москва**: [+7 495 139-91-93](tel:+74951399193)

**Беларусь**: [+375 17 336-31-36](tel:+375173363136)

**Узбекистан**: [+998 71 205-58-05](tel:+998712055805)

**Казахстан**: [+7 727 344-31-31](tel:+77273443131)

Для доступа к кампаниям специалисту потребуется [PIN-код](ru/troubleshooting/pin-code)

Написать письмо

Клиентам

Агентствам

[Формы обратной связи](https://yandex.ru/partner-office/knowledge-base)


### Полезные ссылки

- [Перейти в кабинет](https://direct.yandex.ru/)
- [Мои кампании](https://direct.yandex.ru/registered/main.pl)
- [Вордстат](https://wordstat.yandex.ru/)
- [Способы оплаты](https://yandex.ru/support/direct/payments/payment-methods.html)
- [Контакты](https://yandex.ru/support/direct/contact-us.html)

### Правовые документы

- [Требования к рекламным материалам](https://yandex.ru/legal/direct_adv_rules/ru/)
- [Правила показа](https://yandex.ru/legal/direct_display_rules/ru/)
- [Оферта](https://yandex.ru/legal/oferta_direct/ru/)

### Онлайн-обучение

- [Курсы по Директу](https://yandex.ru/adv/edu/online/direct)
- [Вебинары](https://yandex.ru/adv/edu/events)
- [Полезные материалы](https://yandex.ru/adv/edu/materials/tag-direct)

### Узнайте больше

- [Новости Директа](https://yandex.ru/adv/news?tag=direkt)
- [Кейсы клиентов Яндекса](https://yandex.ru/adv/solutions/cases)
- [Тренды и аналитика](https://yandex.ru/adv/solutions/analytics)
- [Мероприятия Яндекс Рекламы](https://yandex.ru/adv/meropriyatiya)

Предыдущая

[Получение предложения ОСАГО](ru/thematic-section/insurance/offer-status)

Следующая

[Запрос на получение pdf-файла с черновиком полиса](ru/thematic-section/insurance/offer-draft)
