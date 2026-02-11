---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/calculation
---


# Получение расчета ОСАГО

- [Формат запроса](../../thematic-section/insurance/calculation.md#request-format)
- [Успешный ответ](../../thematic-section/insurance/calculation.md#200-ok)
  - [PartnerInfo](../../thematic-section/insurance/calculation.md#partnerinfo)
  - [CalculationStatus](../../thematic-section/insurance/calculation.md#calculationstatus)
  - [DriverInfo](../../thematic-section/insurance/calculation.md#driverinfo)
  - [OsagoOffer](../../thematic-section/insurance/calculation.md#osagooffer)
  - [DriverCoefficients](../../thematic-section/insurance/calculation.md#drivercoefficients)
  - [OfferStatus](../../thematic-section/insurance/calculation.md#offerstatus)
  - [UpsaleInfo](../../thematic-section/insurance/calculation.md#upsaleinfo)
  - [UpsaleOption](../../thematic-section/insurance/calculation.md#upsaleoption)
  - [RiskPayment](../../thematic-section/insurance/calculation.md#riskpayment)

Метод для расчета стоимости полиса ОСАГО по идентификатору запроса.

Система рассчитывает стоимость полиса по доступным предложениям и отправляет ссылку на черновик/оплату.

Если рассчитать стоимость полиса не получилось, нужно вызвать метод [получения предложения](../../thematic-section/insurance/offer-status.md) для финального расчета.

Яндекс проверяет статус расчета не чаще одного раза в секунду, не дольше трех минут, пока он не примет одно из значений:

- `CALCULATION_READY` — расчет готов;
- `NO_CALCULATION_AVAILABLE` — доступных расчетов нет;
- `CALCULATION_ERROR` — ошибка расчета.

## Формат запроса

```
GET /osago/calculate
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `123e4567-e89b-12d3-a456-426614174000`. |

## Успешный ответ

**200 OK**

Формат ответа

```
{
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "DRAFT",
    "partner": {
        "code": 12,
        "name": "Банки.ру",
        "logo_url": "//partner.ru/ugc/logo_135x85.gif"
    },
    "offers": [
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
    ],
    "drivers": [
        {
            "series": "1234",
            "number": "123456",
            "coefficients": {
                "tb": 6896,
                "kt": 1.8,
                "kbm": 1.17,
                "kvs": 1,
                "ks": 1,
                "kp": 1,
                "km": 1.1,
                "kn": 1,
                "ko": 2.32,
                "kpr": 1
            }
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `partner` | Информация о партнере. | [PartnerInfo](../../thematic-section/insurance/calculation.md#partnerinfo) | Информация о страховщике или агрегаторе. |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `status` | Статус процесса расчета ОСАГО. | [CalculationStatus](../../thematic-section/insurance/calculation.md#calculationstatus) |  |
| `drivers` | Информация о водителях и их коэффициентах. | [DriverInfo](../../thematic-section/insurance/calculation.md#driverinfo) |  |
| `offers` | Массив предложений ОСАГО. | [OsagoOffer](../../thematic-section/insurance/calculation.md#osagooffer) |  |

### PartnerInfo

Информация о партнере.

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `code` | Код. | `integer` | Пример: `12`. |
| `logo_url` | Ссылка на логотип. | `string` | Пример: `//partner.ru/ugc/logo_135x85.gif`. |
| `name` | Наименование партнера. | `string` | Пример: `Банки.ру`. |

### CalculationStatus

Статусы процесса расчета полиса ОСАГО. Возможные значения:

- `DRAFT` — черновик (расчет не начат);
- `PARTNER_CALCULATION_IN_PROGRESS` — расчет выполняется партнером;
- `CALCULATION_READY` — расчет готов;
- `PAID` — полис оплачен по расчету (для страховой компании — единственный, для агрегатора — один из предложенных);
- `CLOSED` — закрыт, полис выпущен;
- `NO_CALCULATION_AVAILABLE` — отсутствуют доступные расчеты;
- `CALCULATION_ERROR` — ошибка расчета.

### DriverInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `coefficients` | Список коэффициентов. | [DriverCoefficients](../../thematic-section/insurance/calculation.md#drivercoefficients) |  |
| `number` | Номер водительского удостоверения. | `string` | Пример: `123456`. |
| `series` | Серия водительского удостоверения. | `string` | Пример: `1234`. |

### OsagoOffer

Предложение ОСАГО. Обязательность полей зависит от метода, в котором возвращается предложение.

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор. | `string` | Пример: `44234899`. |
| `partner` | Информация о партнере, который является страховщиком. | [PartnerInfo](../../thematic-section/insurance/calculation.md#partnerinfo) |  |
| `status` | Текущий статус обработки предложения ОСАГО. | [OfferStatus](../../thematic-section/insurance/calculation.md#offerstatus) |  |
| `draft_url` | Ссылка на черновик полиса в формате PDF. | `string` | Пример: `https://partner.ru/policy?id=112233`. |
| `is_ext_prolongation` | Является ли предложение пролонгацией от другой компании. | `boolean` | Пример: `false`. |
| `is_prolongation` | Является ли предложение пролонгацией. | `boolean` | Пример: `true`. |
| `is_reinsurance_pool` | Входит ли предложение в перестраховочный пул. | `boolean` | Возможные значения:   - `true` — входит; - `false`, `null` — не входит.   Если предложение входит в перестраховочный пул, то кросс-продажи обязательны, их отмена влечет отмену предложения. |
| `message` | Сообщение об ошибке / иные сообщения. | `string` | Пример: `Требуется указать действительный адрес проживания`. |
| `payment_url` | Ссылка на оплату. | `string` | Пример: `https://pay.it/policy?id=112233`. |
| `policy_number` | Номер полиса. | `string` | Пример: `0166171796`. |
| `policy_series` | Серия полиса. | `string` | Пример: `ХХХ`. |
| `price` | Цена. | `number` | Пример: `7072`. |
| `upsales` | Массив предложений кросс-продаж. | [UpsaleInfo[]](../../thematic-section/insurance/calculation.md#upsaleinfo) |  |

### DriverCoefficients

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `kbm` | Коэффициент бонус-малус. | `number` | Пример: `1.17`. |
| `km` | Коэффициент мощности двигателя. | `number` | Пример: `1.1`. |
| `kn` | Коэффициент нарушений. | `number` | Пример: `1`. |
| `ko` | Коэффициент ограничения числа водителей. | `number` | Пример: `2.32`. |
| `kp` | Коэффициент срока действия договора. | `number` | Пример: `1`. |
| `kpr` | Коэффициент категории транспортного средства. | `number` | Пример: `1`. |
| `ks` | Коэффициент сезонности. | `number` | Пример: `1`. |
| `kt` | Территориальный коэффициент. | `number` | Пример: `1.8`. |
| `kvs` | Коэффициент возраста и стажа. | `number` | Пример: `1`. |
| `tb` | Базовый тариф. | `number` | Пример: `6896`. |

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
| `options` | Массив опций кросс-продажи. | [UpsaleOption](../../thematic-section/insurance/calculation.md#upsaleoption) | Пользователь может выбрать одну из опций. |
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
| `risk_payments` | Массив рисков и страховых сумм. | [RiskPayment](../../thematic-section/insurance/calculation.md#riskpayment) |  |

### RiskPayment

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `pays` | Массив страховых сумм. | `string[]` | Пример: `[ "100% страховой суммы" ]`. |
| `risk` | Название риска. | `string` | Пример: `Смерть в результате несчастного случая`. |
