---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/confirm-offer
---


# Подтверждение предложения ОСАГО

- [Формат запроса](../../thematic-section/insurance/confirm-offer.md#request-format)
  - [ReturnUrls](../../thematic-section/insurance/confirm-offer.md#returnurls)
- [Успешный ответ](../../thematic-section/insurance/confirm-offer.md#200-ok)
  - [PartnerInfo](../../thematic-section/insurance/confirm-offer.md#partnerinfo)
  - [OfferStatus](../../thematic-section/insurance/confirm-offer.md#offerstatus)
  - [UpsaleInfo](../../thematic-section/insurance/confirm-offer.md#upsaleinfo)
  - [UpsaleOption](../../thematic-section/insurance/confirm-offer.md#upsaleoption)
  - [RiskPayment](../../thematic-section/insurance/confirm-offer.md#riskpayment)

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
| `return_urls` | Ссылки для возврата после оплаты. | [ReturnUrls](../../thematic-section/insurance/confirm-offer.md#returnurls) |  |
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
| `partner` | Информация о партнере, который является страховщиком. | [PartnerInfo](../../thematic-section/insurance/confirm-offer.md#partnerinfo) |  |
| `status` | Текущий статус обработки предложения ОСАГО. | [OfferStatus](../../thematic-section/insurance/confirm-offer.md#offerstatus) |  |
| `draft_url` | Ссылка на черновик полиса в формате PDF. | `string` | Пример: `https://partner.ru/policy?id=112233`. |
| `is_ext_prolongation` | Является ли предложение пролонгацией от другой компании. | `boolean` | Пример: `false`. |
| `is_prolongation` | Является ли предложение пролонгацией. | `boolean` | Пример: `true`. |
| `is_reinsurance_pool` | Входит ли предложение в перестраховочный пул. | `boolean` | Возможные значения:   - `true` — входит; - `false`, `null` — не входит.   Если предложение входит в перестраховочный пул, то кросс-продажи обязательны, их отмена влечет отмену предложения. |
| `message` | Сообщение об ошибке / иные сообщения. | `string` | Пример: `Требуется указать действительный адрес проживания`. |
| `payment_url` | Ссылка на оплату. | `string` | Пример: `https://pay.it/policy?id=112233`. |
| `policy_number` | Номер полиса. | `string` | Пример: `0166171796`. |
| `policy_series` | Серия полиса. | `string` | Пример: `ХХХ`. |
| `price` | Цена. | `number` | Пример: `7072`. |
| `upsales` | Массив предложений кросс-продаж. | [UpsaleInfo](../../thematic-section/insurance/confirm-offer.md#upsaleinfo) |  |

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
| `options` | Массив опций кросс-продажи. | [UpsaleOption](../../thematic-section/insurance/confirm-offer.md#upsaleoption) | Пользователь может выбрать одну из опций. |
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
| `risk_payments` | Массив рисков и страховых сумм. | [RiskPayment](../../thematic-section/insurance/confirm-offer.md#riskpayment) |  |

### RiskPayment

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `pays` | Массив страховых сумм. | `string[]` | Пример: `[ "100% страховой суммы" ]`. |
| `risk` | Название риска. | `string` | Пример: `Смерть в результате несчастного случая`. |
