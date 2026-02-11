---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/offer-policy
---


# Запрос на получение полиса

- [Формат запроса](../../thematic-section/insurance/offer-policy.md#request-format)
- [Успешный ответ](../../thematic-section/insurance/offer-policy.md#200-ok)
  - [OfferStatus](../../thematic-section/insurance/offer-policy.md#offerstatus)

Метод для получения pdf-файла с полисом по идентификатору запроса.

Можно перезапрашивать каждые 5 секунд не более 5 минут до получения статуса `success` и ссылки на полис.

## Формат запроса

```
GET /osago/offer/policy
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор предложения. | `string` | Пример: `offer_123456789`. |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `123e4567-e89b-12d3-a456-426614174000`. |

## Успешный ответ

**200 OK**

Формат ответа

```
{
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "offer_id": "string",
    "status": "CREATED",
    "policy_start_date": "2023-12-01T00:00:00Z",
    "url": "string",
    "file": {
        "type": "base64",
        "data": "data:application/pdf;base64,JVBERi0xLjUK..."
    }
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор предложения. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `status` | Текущий статус обработки предложения ОСАГО. | [OfferStatus](../../thematic-section/insurance/offer-policy.md#offerstatus) |  |
| `file` | Файл полиса. | `object` |  |
| `policy_start_date` | Дата начала действия полиса. | `string` | Формат: `date-time`. Пример: `2023-12-01T00:00:00Z`. |
| `url` | Ссылка на полис в формате PDF. | `string` |  |

- Если `format=base64`: base64-строка в формате MIME.
- Если `format=binary`: бинарный файл PDF.

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
