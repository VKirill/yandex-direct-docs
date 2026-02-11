---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/dictionaries
---


# Получение справочников транспортных средств

- [1. Получение списка брендов](../../thematic-section/insurance/dictionaries.md#brands)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#brands-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#brands-200-ok)
- [2. Получение списка моделей](../../thematic-section/insurance/dictionaries.md#models)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#models-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#models-200-ok)
- [3. Получение списка годов выпуска](../../thematic-section/insurance/dictionaries.md#years)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#years-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#years-200-ok)
- [4. Получение списка мощностей двигателя](../../thematic-section/insurance/dictionaries.md#engine-powers)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#engine-powers-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#engine-powers-200-ok)
- [5. Получение списка модификаций (необязательный)](../../thematic-section/insurance/dictionaries.md#modifications)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#modifications-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#modifications-200-ok)
- [6. Получение иерархии автомобильных данных (необязательный)](../../thematic-section/insurance/dictionaries.md#vehicle-dictionaries)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#vehicle-dictionaries-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#vehicle-dictionaries-200-ok)
- [7. Получение информации об автомобиле](../../thematic-section/insurance/dictionaries.md#vehicle-info)
  - [Формат запроса](../../thematic-section/insurance/dictionaries.md#vehicle-info-request-format)
  - [Успешный ответ](../../thematic-section/insurance/dictionaries.md#vehicle-info-200-ok)

1. [Получение списка брендов](../../thematic-section/insurance/dictionaries.md#brands).
2. [Получение списка моделей](../../thematic-section/insurance/dictionaries.md#models).
3. [Получение списка годов выпуска](../../thematic-section/insurance/dictionaries.md#years).
4. [Получение списка мощностей двигателя](../../thematic-section/insurance/dictionaries.md#engine-powers).
5. [Получение списка модификаций (необязательный)](../../thematic-section/insurance/dictionaries.md#modifications).
6. [Получение иерархии автомобильных данных (необязательный)](../../thematic-section/insurance/dictionaries.md#vehicle-dictionaries).
7. [Получение информации об автомобиле](../../thematic-section/insurance/dictionaries.md#vehicle-info).

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
| `modifications` | Массив модификаций. | [Modification[]](../../thematic-section/insurance/dictionaries.md#modification) |  |

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
| `brands` | Список брендов. | [VehicleBrand[]](../../thematic-section/insurance/dictionaries.md#vehiclebrand) |  |

#### VehicleBrand

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Уникальный идентификатор бренда. | `number` | Пример: `1`. |
| `models` | Список моделей бренда. | [VehicleModel[]](../../thematic-section/insurance/dictionaries.md#vehiclemodel) |  |
| `name` | Международное название бренда. | `string` | Пример: `Toyota`. |
| `name_ru` | Локализованное название бренда. | `string` | Пример: `Тойота`. |

#### VehicleModel

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Уникальный идентификатор модели. | `string` | Пример: `101`. |
| `name` | Международное название модели. | `string` | Пример: `Camry`. |
| `vehicle_types` | Категории транспортных средств. | `string[]` | Возможные значения: `A`, `B`, `C`, `D`, `E`. |
| `years` | Доступные года выпуска. | [ModelYear[]](../../thematic-section/insurance/dictionaries.md#modelyear) |  |
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
| `brand` | Бренд автомобиля. | [BrandInfo](../../thematic-section/insurance/dictionaries.md#brandinfo) |  |
| `car_documents` | Документы на автомобиль. | [CarDocument[]](../../thematic-section/insurance/dictionaries.md#cardocument) |  |
| `engine_power` | Мощность двигателя в л.с. | `number` | Пример: `150`. |
| `model` | Модель автомобиля. | [ModelInfo](../../thematic-section/insurance/dictionaries.md#modelinfo) |  |
| `year` | Год выпуска. | `integer` | Пример: `2020`. |
| `body_number` | Номер кузова. | `string` | Обязательно, если нет `vin` или c`hassis_number`. Пример: `ABC123456789`. |
| `car_number` | Номер автомобиля. | `string` | Обязательно, если есть СТС. Пример: `А123БВ777`. |
| `category` | Категория транспортного средства. | `string` | Возможные значения: `A`, `B`, `C`, `D`, `E`. Пример: `B`. |
| `chassis_number` | Номер шасси. | `string` | Обязательно, если нет `body_number` или `vin`. Пример: `CHS987654321`. |
| `modification` | Модификация автомобиля. | [ModificationInfo](../../thematic-section/insurance/dictionaries.md#modificationinfo) |  |
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
