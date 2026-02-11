---
source: https://yandex.ru/support/direct/ru/thematic-section/credits/example
---

Примеры предложений

# Примеры предложений

Положительное решение о выдаче кредита в размере 500 000 рублей

Формат тела запроса

```
{
    "phone_number": "9330445040",
    "amount": 500000.00,
    "term": 36,
    "product_type": "loan",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
{
    200
    {
        "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
        "status": "done",
        "name": "АО Супер-банк",
        "decision": "has_approve",
        "data": [
              {
                  "product_type": "loan",
                  "decision": "pre_approved",
                  "amount": {
                      "min": null,
                      "max": 1000000.0,
                  },
                  "term": {
                      "min": 36,
                      "max": 60,
                  },
                  "rate": {
                      "min": 24.3,
                      "max": 36.2,
                  },
                  "total_cost": {
                      "min": 25.1,
                      "max": 40.2,
                  },
                  "payment": {
                      "min": 13000,
                      "max": 21000
                  },
                  "special_conditions": null,
                  "required_documents": [
                      "Паспорт РФ",
                      "СНИЛС"
                  ],
                  "choosable_documents": [
                      "2-НДФЛ, Справка по форме банка",
                      "Подтверждение на Госуслугах, Справка по форме банка"
                  ],
                  "propousal_link":{
                  link: "https://my.bank.ru/propousals?id=1"
                  }
              }
          ]
      }
}
```

Положительное решение о выдаче кредитной карты на сумму 120 000

Формат тела запроса

```
{
    "phone_number": "9330445040",
    "product_type": "credit_card",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
200
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "status": "done",
    "name": "АО Супер-банк",
    "decision": "has_approve",
    "data": [
        {
            "product_type": "credit_card",
            "decision": "pre_approved",
            "amount": {
                "min": 120000.0,
                "max": 120000.0,
            },
            "rate": {
                "min": 24.3,
                "max": 36.2,
            },
            "total_cost": {
                "min": 25.1,
                "max": 40.2,
            },
            "grace_period": 120,
            "payment": {
                "cc_rate": 10
            }
            "special_conditions": null,
            "required_documents": {
                "min": 13000,
                "max": 21000
            },
            "special_conditions": null,
            "required_documents": [
                "Паспорт РФ",
                "СНИЛС"
            ],
            "choosable_documents": [
                "2-НДФЛ, Справка по форме банка",
                "Подтверждение на Госуслугах, Справка по форме банка"
            ],
            "propousal_link": {
                link: "https://my.bank.ru/propousals?id=1"
            }
        }
    ]
}
```

Несколько положительных решений

Формат тела запроса

```
{
    "phone_number": "9330445040",
    "amount": 500000.00,
    "term": 36,
    "product_type": "loan",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
200
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "name": "АО Супер-банк",
    "status": "done",
    "decision": "has_approve",
    "data": [
        {
            "product_type": "loan",
            "decision": "pre_approved",
            "amount": {
                "min": null,
                "max": 600000.0,
            },
            "term": {
                "min": 24,
                "max": 36,
            },
            "rate": {
                "min": 24.3,
                "max": 36.2,
            },
            "total_cost": {
                "min": 25.1,
                "max": 40.2,
            },
            "payment": {
                "min": 13000,
                "max": 21000
            },
            "special_conditions": null,
            "required_documents": [
                "Паспорт РФ",
                "СНИЛС"
            ],
            "choosable_documents": [
                "2-НДФЛ, Справка по форме банка",
                "Подтверждение на Госуслугах, Справка по форме банка"
            ],
            "propousal_link": {
                link: "https://my.bank.ru/propousals?id=1"
            }
        },
        }
            "product_type": "loan",
            "decision": "full_approved",
            "amount": {
                "min": 600000.01,
                "max": 1000000.0,
            },
            "term": {
                "min": 36,
                "max": 60,
            },
            "rate": {
                "min": 18.0,
                "max": 24.3,
            },
            "total_cost": {
                "min": 20.1,
                "max": 28.2,
            },
            "payment": {
                "min": 13000,
                "max": 21000
            },
            "special_conditions": "Необходим статус VIP-клиента",
            "required_documents": [
                "Паспорт РФ",
                "СНИЛС"
            ],
            "choosable_documents": [
                "2-НДФЛ, Справка по форме банка",
                "Подтверждение на Госуслугах, Справка по форме банка"
            ],
            "propousal_link": {
                link: "https://my.bank.ru/propousals?id=2"
            }
        }
    ]
}
```

Заявка на выдачу кредита отклонена

Формат тела запроса

```
{
    "phone_number": "9330445040",
    "amount": 500000.00,
    "term": 36,
    "product_type": "loan",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "status": "done",
    "name": "АО Супер-банк",
    "decision": "rejected",
    "data": null
}
```

Некорректный запрос

Формат тела запроса

```
{
    "phone_number": "93304450",
    "amount": "500000.00$",
    "term": 36,
    "product_type": "loan",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
400
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "message": "Поле phone_number должно содержать 10 цифр; поле amount должно быть числом",
    "properties": ["phone_number", "amount"]
}
```

Асинхронный запрос

Формат тела запроса

```
{
    "phone_number": "9330445040",
    "amount": 500000.00,
    "term": 36,
    "product_type": "loan",
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
200
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Через некоторое время:

Формат тела запроса

```
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
200
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "status": "done",
    "name": "АО Супер-банк",
    "decision": "rejected",
    "data": null
}
```

Информации по заявке не найдено

Формат тела запроса

```
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372"
}
```

Формат ответа

```
404
{
    "search_id": "e2b4948b-7d8a-4eec-875c-b1c11d7d8372",
    "message": "Заявок с таким search_id не найдено"
}
```

[Справочник API](ru/thematic-section/credits/post-banking)

[Стандартные коды ответов](ru/thematic-section/credits/responce-codes)

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

[Стандартные коды ответов](ru/thematic-section/credits/responce-codes)

Следующая

[Кредитные карты — API для партнеров](ru/thematic-section/credit-cards/about)
