---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/calculation-status
---


# Получение статуса расчета ОСАГО

- [Формат запроса](../../thematic-section/insurance/calculation-status.md#request-format)
- [Успешный ответ](../../thematic-section/insurance/calculation-status.md#200-ok)
  - [CalculationStatus](../../thematic-section/insurance/calculation-status.md#calculationstatus)
  - [OfferStatus](../../thematic-section/insurance/calculation-status.md#offerstatus)

Метод для получения статуса расчета ОСАГО по идентификатору запроса (необязательный).

## Формат запроса

```
GET /osago/calculate/status
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `123e4567-e89b-12d3-a456-426614174000`. |

## Успешный ответ

**200 OK**

Успешный ответ

Формат ответа

```
{
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "DRAFT",
    "offers": [
        {
            "offer_id": "string",
            "offer_status": "CREATED"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `status` | Статусы процесса расчета ОСАГО. | [CalculationStatus](../../thematic-section/insurance/calculation-status.md#calculationstatus) |  |
| `offers` | Массив предложений. | `object[]` |  |

### CalculationStatus

Статусы процесса расчета полиса ОСАГО. Возможные значения:

- `DRAFT` — черновик (расчет не начат);
- `PARTNER_CALCULATION_IN_PROGRESS` — расчет выполняется партнером;
- `CALCULATION_READY` — расчет готов;
- `PAID` — полис оплачен по расчету (для страховой компании — единственный, для агрегатора — один из предложенных);
- `CLOSED` — закрыт, полис выпущен;
- `NO_CALCULATION_AVAILABLE` — отсутствуют доступные расчеты;
- `CALCULATION_ERROR` — ошибка расчета.

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
