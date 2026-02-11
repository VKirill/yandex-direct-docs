---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/offer-draft
---

Запрос на получение pdf-файла с черновиком полиса

# Запрос на получение pdf-файла с черновиком полиса

- [Формат запроса](ru/thematic-section/insurance/offer-draft#request-format)
- [Успешный ответ](ru/thematic-section/insurance/offer-draft#200-ok)
  - [OsagoOfferDraftSuccessResponse](ru/thematic-section/insurance/offer-draft#osagoofferdraftsuccessresponse)
  - [OsagoOfferDraftInProcessResponse](ru/thematic-section/insurance/offer-draft#osagoofferdraftinprocessresponse)

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
| `...rest` | Успешный ответ на запрос черновика. | oneOf [OsagoOfferDraftSuccessResponse](ru/thematic-section/insurance/offer-draft#osagoofferdraftsuccessresponse) |  |
| `...rest` | Ответ на запрос черновика «В процессе формирования». | oneOf [OsagoOfferDraftInProcessResponse](ru/thematic-section/insurance/offer-draft#osagoofferdraftinprocessresponse) |  |

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

[Подтверждение предложения ОСАГО](ru/thematic-section/insurance/confirm-offer)

Следующая

[Запрос на получение полиса](ru/thematic-section/insurance/offer-policy)
