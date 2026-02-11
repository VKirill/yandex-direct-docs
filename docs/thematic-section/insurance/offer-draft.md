---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/offer-draft
---


# Запрос на получение pdf-файла с черновиком полиса

- [Формат запроса](../../thematic-section/insurance/offer-draft.md#request-format)
- [Успешный ответ](../../thematic-section/insurance/offer-draft.md#200-ok)
  - [OsagoOfferDraftSuccessResponse](../../thematic-section/insurance/offer-draft.md#osagoofferdraftsuccessresponse)
  - [OsagoOfferDraftInProcessResponse](../../thematic-section/insurance/offer-draft.md#osagoofferdraftinprocessresponse)

Метод для получения pdf-файла с черновиком полиса по идентификатору запроса.

Можно перезапрашивать каждые 5 секунд не более 5 минут до получения статуса `success` и ссылки на черновик.

## Формат запроса

```
GET /osago/offer/draft
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
    "status": "success",
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
| `...rest` | Успешный ответ на запрос черновика. | oneOf [OsagoOfferDraftSuccessResponse](../../thematic-section/insurance/offer-draft.md#osagoofferdraftsuccessresponse) |  |
| `...rest` | Ответ на запрос черновика «В процессе формирования». | oneOf [OsagoOfferDraftInProcessResponse](../../thematic-section/insurance/offer-draft.md#osagoofferdraftinprocessresponse) |  |

- Если `format=base64`: base64-строка в формате MIME.
- Если `format=binary`: бинарный файл PDF.

### OsagoOfferDraftSuccessResponse

Успешный ответ на запрос черновика.

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор предложения. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `status` | Статус формирования черновика. | `string` | Возможные значения: `success`. |
| `file` | Файл черновика. | `object` |  |
| `url` | Ссылка на черновик в формате PDF. | `string` |  |

### OsagoOfferDraftInProcessResponse

Ответ на запрос черновика «В процессе формирования».

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `offer_id` | Идентификатор предложения. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `status` | Статус формирования черновика. | `string` | Возможные значения: `inProcess`. |
