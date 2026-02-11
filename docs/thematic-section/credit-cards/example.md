---
source: https://yandex.ru/support/direct/ru/thematic-section/credit-cards/example
---


# Примеры предложений

Положительное решение по кредитной карте

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

Одно положительное решение

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
				min: 13000,
				max: 21000
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
				min: 13000,
				max: 21000
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
	    	"proposal_link": {
				link: "https://my.bank.ru/propousals?id=1"
			}
        },
        {
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
				min: 13000,
				max: 21000
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

Заявка отклонена

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

[Справочник API](../../thematic-section/credit-cards/post-banking.md)
