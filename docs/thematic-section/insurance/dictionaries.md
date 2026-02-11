---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/dictionaries
---

Получение справочников транспортных средств

# Получение справочников транспортных средств

- [1. Получение списка брендов](ru/thematic-section/insurance/dictionaries#brands)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#brands-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#brands-200-ok)
- [2. Получение списка моделей](ru/thematic-section/insurance/dictionaries#models)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#models-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#models-200-ok)
- [3. Получение списка годов выпуска](ru/thematic-section/insurance/dictionaries#years)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#years-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#years-200-ok)
- [4. Получение списка мощностей двигателя](ru/thematic-section/insurance/dictionaries#engine-powers)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#engine-powers-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#engine-powers-200-ok)
- [5. Получение списка модификаций (необязательный)](ru/thematic-section/insurance/dictionaries#modifications)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#modifications-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#modifications-200-ok)
- [6. Получение иерархии автомобильных данных (необязательный)](ru/thematic-section/insurance/dictionaries#vehicle-dictionaries)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#vehicle-dictionaries-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#vehicle-dictionaries-200-ok)
- [7. Получение информации об автомобиле](ru/thematic-section/insurance/dictionaries#vehicle-info)
  - [Формат запроса](ru/thematic-section/insurance/dictionaries#vehicle-info-request-format)
  - [Успешный ответ](ru/thematic-section/insurance/dictionaries#vehicle-info-200-ok)

1. [Получение списка брендов](ru/thematic-section/insurance/dictionaries#brands).
2. [Получение списка моделей](ru/thematic-section/insurance/dictionaries#models).
3. [Получение списка годов выпуска](ru/thematic-section/insurance/dictionaries#years).
4. [Получение списка мощностей двигателя](ru/thematic-section/insurance/dictionaries#engine-powers).
5. [Получение списка модификаций (необязательный)](ru/thematic-section/insurance/dictionaries#modifications).
6. [Получение иерархии автомобильных данных (необязательный)](ru/thematic-section/insurance/dictionaries#vehicle-dictionaries).
7. [Получение информации об автомобиле](ru/thematic-section/insurance/dictionaries#vehicle-info).

## 1. Получение списка брендов

### Формат запроса

```
GET /dictionaries/brands
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `category` | Категории транспортных средств. | `string` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |

### Успешный ответ

**200 OK**

Список брендов.

Формат ответа

```
{
    "brands": [
        {
            "brand_id": "string",
            "name": "string",
            "name_ru": "string"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brands` | Список брендов. | `object[]` |  |

## 2. Получение списка моделей

### Формат запроса

```
GET /dictionaries/models
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Идентификатор бренда. | `string` |  |
| `category` | Категории транспортных средств. | `string` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |

### Успешный ответ

**200 OK**

Список моделей.

Формат ответа

```
{
    "brand_id": "string",
    "models": [
        {
            "model_id": "string",
            "name": "string",
            "name_ru": "string",
            "vehicle_type": [
                "A"
            ]
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Идентификатор бренда. | `string` |  |
| `models` | Список моделей. | `object[]` |  |

## 3. Получение списка годов выпуска

### Формат запроса

```
GET /dictionaries/years
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `category` | Категории транспортных средств. | `string` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |
| `model_id` | Идентификатор модели. | `string` |  |

### Успешный ответ

**200 OK**

Список годов выпуска.

Формат ответа

```
{
    "brand_id": "string",
    "model_id": "string",
    "years": [
        0
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` |  |
| `years` | Года. | `number[]` |  |
| `brand_id` | Идентификатор бренда. | `string` |  |

## 4. Получение списка мощностей двигателя

### Формат запроса

```
GET /dictionaries/powers
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` | Пример: `123`. |
| `year` | Год выпуска. | `number <integer>` | Пример: `2020`. |

### Успешный ответ

**200 OK**

Список мощностей.

Формат ответа

```
{
    "model_id": "string",
    "year": 0,
    "powers": [
        0
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` |  |
| `powers` | Список мощностей. | `number[]` |  |
| `year` | Год выпуска. | `number` |  |

## 5. Получение списка модификаций (необязательный)

Транспортное средство может быть представлено комбинацией модели, года выпуска и мощности двигателя.

### Формат запроса

```
GET /dictionaries/modifications
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` | Пример: `123`. |
| `power` | Мощность двигателя. | `number` | Пример: `123`. |
| `year` | Год выпуска. | `number` | Пример: `2020`. |

### Успешный ответ

**200 OK**

Список модификаций.

Формат ответа

```
{
    "modifications": [
        {
            "id": 1,
            "name": "2.4 Luxe, Седан, Автоматическая, Бензин, дверей 4, мест 5"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `modifications` | Массив модификаций. | [Modification[]](ru/thematic-section/insurance/dictionaries#modification) |  |

#### Modification

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `id` | Идентификатор модификации. | `integer` | Пример: `1`. |
| `name` | Название модификации. | `string` | Пример: `2.4 Luxe, Седан, Автоматическая, Бензин, дверей 4, мест 5`. |

## 6. Получение иерархии автомобильных данных (необязательный)

Метод возвращает полную структуру:

- бренды;
- модели;
- годы выпуска;
- мощности двигателей.

Метод необязательный.

### Формат запроса

```
GET /dictionaries/sync-all
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `category` | Категории транспортных средств. | `string[]` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |

### Успешный ответ

**200 OK**

Успешный ответ.

Формат ответа

```
{
    "brands": [
        {
            "brand_id": "1",
            "name": "Toyota",
            "name_ru": "Тойота",
            "models": [
                {
                    "model_id": "101",
                    "name": "Camry",
                    "name_ru": "Камри",
                    "years": [
                        {
                            "year": 2023,
                            "engine_powers": [
                                150,
                                200
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brands` | Список брендов. | [VehicleBrand[]](ru/thematic-section/insurance/dictionaries#vehiclebrand) |  |

#### VehicleBrand

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Уникальный идентификатор бренда. | `number` | Пример: `1`. |
| `models` | Список моделей бренда. | [VehicleModel[]](ru/thematic-section/insurance/dictionaries#vehiclemodel) |  |
| `name` | Международное название бренда. | `string` | Пример: `Toyota`. |
| `name_ru` | Локализованное название бренда. | `string` | Пример: `Тойота`. |

#### VehicleModel

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Уникальный идентификатор модели. | `string` | Пример: `101`. |
| `name` | Международное название модели. | `string` | Пример: `Camry`. |
| `vehicle_types` | Категории транспортных средств. | `string[]` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |
| `years` | Доступные года выпуска. | [ModelYear[]](ru/thematic-section/insurance/dictionaries#modelyear) |  |
| `name_ru` | Локализованное название модели. | `string` | Пример: `Камри`. |

#### ModelYear

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `engine_powers` | Доступные мощности двигателя (мощность двигателя в лошадиных силах). | `number[]` | Пример: `150`. Минимальное значение: `0`. |
| `year` | Год выпуска модели. | `number` | Пример: `2023`. |

## 7. Получение информации об автомобиле

Метод для получения информации об автомобиле по VIN-коду или госномеру.

### Формат запроса

```
GET /auto/info
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `car_number` | Госномер автомобиля. | `string` | Пример: `A123AA123`. |
| `vin` | VIN-код автомобиля. | `string` | Пример: `WVWZZZ1JZDW123456`. |

### Успешный ответ

**200 OK**

Успешный ответ.

Формат ответа

```
{
    "car_number": "А123БВ777",
    "category": "B",
    "vin": "XTA210990Y2765439",
    "body_number": "ABC123456789",
    "chassis_number": "CHS987654321",
    "brand": {
        "brand_id": "1",
        "name": "Toyota",
        "name_ru": "Тойота"
    },
    "model": {
        "model_id": "101",
        "name": "Camry",
        "name_ru": "Камри"
    },
    "modification": {
        "modification_id": "5001",
        "name": "2.0 Turbo (249 л.с.)"
    },
    "year": 2020,
    "engine_power": 150,
    "car_documents": [
        {
            "series": "77AA",
            "number": "123456",
            "date": "2020-05-15",
            "document_type": "sts"
        }
    ]
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand` | Бренд автомобиля. | [BrandInfo](ru/thematic-section/insurance/dictionaries#brandinfo) |  |
| `car_documents` | Документы на автомобиль. | [CarDocument[]](ru/thematic-section/insurance/dictionaries#cardocument) |  |
| `engine_power` | Мощность двигателя в л.с. | `number` | Пример: `150`. |
| `model` | Модель автомобиля. | [ModelInfo](ru/thematic-section/insurance/dictionaries#modelinfo) |  |
| `year` | Год выпуска. | `integer` | Пример: `2020`. |
| `body_number` | Номер кузова. | `string` | Обязательно, если нет `vin` или c`hassis_number`. Пример: `ABC123456789`. |
| `car_number` | Номер автомобиля. | `string` | Обязательно, если есть СТС. Пример: `А123БВ777`. |
| `category` | Категория транспортного средства. | `string` | Возможные значения: `A`, `B`, `C`, `D`, `E`. Пример: `B`. |
| `chassis_number` | Номер шасси. | `string` | Обязательно, если нет `body_number` или `vin`. Пример: `CHS987654321`. |
| `modification` | Модификация автомобиля. | [ModificationInfo](ru/thematic-section/insurance/dictionaries#modificationinfo) |  |
| `vin` | VIN номер. | `string` | Обязательно, если нет `body_number` или `chassis_number`. Пример: `XTA210990Y2765439`. |

#### BrandInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Идентификатор бренда. | `string` | Пример: `1`. |
| `name` | Название бренда. | `string` | Пример: `Toyota`. |
| `name_ru` | Название бренда на русском. | `string` | Пример: `Тойота`. |

#### CarDocument

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `date` | Дата выдачи документа. | `string` | Формат: `date`. Пример: `2020-05-15`. |
| `document_type` | Тип документа. | `string` | Пример: `sts`. Возможные значения:   - `sts`; - `pts`; - `epts`. |
| `number` | Номер документа. | `string` | Пример: `123456`. |
| `series` | Серия документа. | `string` | Пример: `77AA`. |

#### ModelInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` | Пример: `101`. |
| `name` | Название модели. | `string` | Пример: `Camry`. |
| `name_ru` | Название модели на русском. | `string` | Пример: `Камри`. |

#### ModificationInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `modification_id` | Идентификатор модификации. | `string` | Пример: `5001`. |
| `name` | Название модификации. | `string` | Пример: `2.0 Turbo (249 л.с.)`. |

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

[API-интеграция](ru/thematic-section/insurance/about)

Следующая

[Создание запроса на расчет ОСАГО](ru/thematic-section/insurance/calc)
