---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/responce-codes
---


# Стандартные коды ответов

**400 Bad Request**

Ошибка в запросе.

Формат ответа

```
{
    "request_id": "c3073b9d-edd0-49f2-a28d-b7ded8ff9a8b",
    "message": "string",
    "properties": [
        {
            "property": "string",
            "message": "string"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `message` | Сообщение об ошибке. | `string` |  |
| `properties` | Массив полей, содержащих ошибку. Объект подробностей об ошибке. | [ErrorDetail[]](../../thematic-section/insurance/responce-codes.md#errordetail) |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. |

### ErrorDetail

Объект подробностей об ошибке.

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `message` | Сообщение об ошибке. | `string` |  |
| `property` | Поле, содержащее ошибку. | `string` |  |

**403 Access Forbidden**

Ошибка доступа.

Формат ответа

```
{
    "request_id": "c3073b9d-edd0-49f2-a28d-b7ded8ff9a8b",
    "message": "string"
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `message` | Сообщение об ошибке. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. |

**404 Not Found**

По запросу ничего не найдено.

Формат ответа

```
{
    "request_id": "c3073b9d-edd0-49f2-a28d-b7ded8ff9a8b",
    "message": "string"
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `message` | Сообщение об ошибке. | `string` |  |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. |

**500 Internal Server Error**

Ошибка сервера.

Формат ответа

```
{
    "request_id": "c3073b9d-edd0-49f2-a28d-b7ded8ff9a8b",
    "message": "string"
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `message` | Сообщение об ошибке. | `string` |  |
