---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/calc
---


# Создание запроса на расчет ОСАГО

- [Формат запроса](../../thematic-section/insurance/calc.md#request-format)
  - [DriversInfo](../../thematic-section/insurance/calc.md#driversinfo)
  - [PersonInfo](../../thematic-section/insurance/calc.md#personinfo)
  - [VehicleInfo](../../thematic-section/insurance/calc.md#vehicleinfo)
  - [ReturnUrls](../../thematic-section/insurance/calc.md#returnurls)
  - [AddressInfo](../../thematic-section/insurance/calc.md#addressinfo)
  - [ContactInfo](../../thematic-section/insurance/calc.md#contactinfo)
  - [LicenseInfo](../../thematic-section/insurance/calc.md#licenseinfo)
  - [PassportInfo](../../thematic-section/insurance/calc.md#passportinfo)
  - [PreviousLicenseInfo](../../thematic-section/insurance/calc.md#previouslicenseinfo)
  - [BrandInfo](../../thematic-section/insurance/calc.md#brandinfo)
  - [CarDocument](../../thematic-section/insurance/calc.md#cardocument)
  - [ModelInfo](../../thematic-section/insurance/calc.md#modelinfo)
  - [ModificationInfo](../../thematic-section/insurance/calc.md#modificationinfo)
- [Успешный ответ](../../thematic-section/insurance/calc.md#200-ok)

Метод для инициализации запроса на расчет ОСАГО.

## Формат запроса

```
POST /osago/calculate
```

Пример запроса

```
{
    "product_type": "osago",
    "partner": "yandex",
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "is_cross_allowed": true,
    "purpose": "taxi",
    "policy_start_date": "2023-12-01T00:00:00Z",
    "vehicle": {
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
    },
    "drivers_info": {
        "is_unlimited_drivers": false,
        "drivers": [
            {
                "last_name": "Иванов",
                "middle_name": "Иванович",
                "first_name": "Иван",
                "birth_date": "1980-06-12",
                "license": {
                    "series": "77AA",
                    "number": "123456",
                    "date": "2015-06-10"
                },
                "foreign_license": {
                    "series": "77AA",
                    "number": "123456",
                    "date": "2015-06-10"
                },
                "previous_license": {
                    "last_name": "Иванов",
                    "middle_name": "Иванович",
                    "first_name": "Иван",
                    "license": {
                        "series": "77AA",
                        "number": "123456",
                        "date": "2015-06-10"
                    }
                },
                "passport": {
                    "series": "1234",
                    "number": "567890",
                    "issue_date": "2010-10-05",
                    "issuer": "ОУФМС России по г. Москве",
                    "subdivision": "770-001"
                },
                "addresses": [
                    {
                        "type": "registration",
                        "address": "Красноярский край, г. Красноярск, ул. Ленина, д. 1, кв. 1",
                        "country_code": "7",
                        "region_name": "Красноярский край",
                        "region_type": "г",
                        "district_name": "Сибирский",
                        "city_name": "Красноярск",
                        "city_type": "г",
                        "settlement_name": "Красноярск",
                        "settlement_type": "г",
                        "street_name": "Ленина",
                        "street_type": "ул",
                        "house": "1",
                        "building": "string",
                        "block": "string",
                        "apartment": "1",
                        "addresses_kladr_code": "7700000000000000001",
                        "region_kladr_code": "7700000000000",
                        "city_kladr_code": "7700000000000",
                        "settlement_kladr_code": "string",
                        "street_kladr_code": "7700000000000010000",
                        "fias_code": "f26b876b-6857-4951-b060-ec6559f04a9a",
                        "region_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                        "area_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                        "city_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                        "settlement_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                        "street_fias_code": "95dbf7fb-0dd4-4a04-8100-4f6c847564b5",
                        "house_fias_code": "00a77cd5-e431-46df-8832-f9f462c15205"
                    }
                ],
                "contact": {
                    "phone": "79161234567",
                    "email": "user@Пример.com"
                }
            }
        ]
    },
    "owner": {
        "last_name": "Иванов",
        "middle_name": "Иванович",
        "first_name": "Иван",
        "birth_date": "1980-06-12",
        "license": {
            "series": "77AA",
            "number": "123456",
            "date": "2015-06-10"
        },
        "foreign_license": {
            "series": "77AA",
            "number": "123456",
            "date": "2015-06-10"
        },
        "previous_license": {
            "last_name": "Иванов",
            "middle_name": "Иванович",
            "first_name": "Иван",
            "license": {
                "series": "77AA",
                "number": "123456",
                "date": "2015-06-10"
            }
        },
        "passport": {
            "series": "1234",
            "number": "567890",
            "issue_date": "2010-10-05",
            "issuer": "ОУФМС России по г. Москве",
            "subdivision": "770-001"
        },
        "addresses": [
            {
                "type": "registration",
                "address": "Красноярский край, г. Красноярск, ул. Ленина, д. 1, кв. 1",
                "country_code": "7",
                "region_name": "Красноярский край",
                "region_type": "г",
                "district_name": "Сибирский",
                "city_name": "Красноярск",
                "city_type": "г",
                "settlement_name": "Красноярск",
                "settlement_type": "г",
                "street_name": "Ленина",
                "street_type": "ул",
                "house": "1",
                "building": "string",
                "block": "string",
                "apartment": "1",
                "addresses_kladr_code": "7700000000000000001",
                "region_kladr_code": "7700000000000",
                "city_kladr_code": "7700000000000",
                "settlement_kladr_code": "string",
                "street_kladr_code": "7700000000000010000",
                "fias_code": "f26b876b-6857-4951-b060-ec6559f04a9a",
                "region_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "area_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "city_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "settlement_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "street_fias_code": "95dbf7fb-0dd4-4a04-8100-4f6c847564b5",
                "house_fias_code": "00a77cd5-e431-46df-8832-f9f462c15205"
            }
        ],
        "contact": {
            "phone": "79161234567",
            "email": "user@Пример.com"
        }
    },
    "insurer": {
        "last_name": "Иванов",
        "middle_name": "Иванович",
        "first_name": "Иван",
        "birth_date": "1980-06-12",
        "license": {
            "series": "77AA",
            "number": "123456",
            "date": "2015-06-10"
        },
        "foreign_license": {
            "series": "77AA",
            "number": "123456",
            "date": "2015-06-10"
        },
        "previous_license": {
            "last_name": "Иванов",
            "middle_name": "Иванович",
            "first_name": "Иван",
            "license": {
                "series": "77AA",
                "number": "123456",
                "date": "2015-06-10"
            }
        },
        "passport": {
            "series": "1234",
            "number": "567890",
            "issue_date": "2010-10-05",
            "issuer": "ОУФМС России по г. Москве",
            "subdivision": "770-001"
        },
        "addresses": [
            {
                "type": "registration",
                "address": "Красноярский край, г. Красноярск, ул. Ленина, д. 1, кв. 1",
                "country_code": "7",
                "region_name": "Красноярский край",
                "region_type": "г",
                "district_name": "Сибирский",
                "city_name": "Красноярск",
                "city_type": "г",
                "settlement_name": "Красноярск",
                "settlement_type": "г",
                "street_name": "Ленина",
                "street_type": "ул",
                "house": "1",
                "building": "string",
                "block": "string",
                "apartment": "1",
                "addresses_kladr_code": "7700000000000000001",
                "region_kladr_code": "7700000000000",
                "city_kladr_code": "7700000000000",
                "settlement_kladr_code": "string",
                "street_kladr_code": "7700000000000010000",
                "fias_code": "f26b876b-6857-4951-b060-ec6559f04a9a",
                "region_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "area_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "city_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "settlement_fias_code": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
                "street_fias_code": "95dbf7fb-0dd4-4a04-8100-4f6c847564b5",
                "house_fias_code": "00a77cd5-e431-46df-8832-f9f462c15205"
            }
        ],
        "contact": {
            "phone": "79161234567",
            "email": "user@Пример.com"
        }
    },
    "return_urls": {
        "success_url": "https://Пример.com/osago/success",
        "failure_url": "https://Пример.com/osago/failure"
    }
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `drivers_info` | Информация о водителях. | [DriversInfo](../../thematic-section/insurance/calc.md#driversinfo) |  |
| `insurer` | Информация о страхователе. | [PersonInfo](../../thematic-section/insurance/calc.md#personinfo) |  |
| `is_cross_allowed` | Разрешены ли кросс-продажи. | `boolean` | Пример: `true`. |
| `owner` | Информация о владельце. | [PersonInfo](../../thematic-section/insurance/calc.md#personinfo) |  |
| `partner` | Название партнера. | `string` | Пример: `yandex`. |
| `policy_start_date` | Дата начала действия полиса. | `string` | В формате `date-time`. Пример: `2023-12-01T00:00:00Z`. |
| `product_type` | Тип продукта. | `string` | Пример: `osago`. |
| `purpose` | Назначение полиса. | `string` | Значение по умолчанию: `personal`. Возможные значения:   - `taxi` — полис для такси; - `personal` — полис для личного использования. |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. |
| `vehicle` | Информация о транспортном средстве. | [VehicleInfo](../../thematic-section/insurance/calc.md#vehicleinfo) |  |
| `return_urls` | Ссылки для возврата после оплаты. | [ReturnUrls](../../thematic-section/insurance/calc.md#returnurls) |  |

### DriversInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `drivers` | Список водителей. | [PersonInfo](../../thematic-section/insurance/calc.md#personinfo) |  |
| `is_unlimited_drivers` | Является ли список водителей неограниченным. | `boolean` | Пример: `false`. |

### PersonInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `birth_date` | Дата рождения. | `string` | Формат: `date`. Пример: `1980-06-12`. |
| `first_name` | Имя. | `string` | Пример: `Иван`. |
| `last_name` | Фамилия. | `string` | Пример: `Иванов`. |
| `addresses` | Адреса. | [AddressInfo](../../thematic-section/insurance/calc.md#addressinfo) |  |
| `contact` | Контактные данные. | [ContactInfo](../../thematic-section/insurance/calc.md#contactinfo) |  |
| `foreign_license` | Иностранное водительское удостоверение. | [LicenseInfo](../../thematic-section/insurance/calc.md#licenseinfo) | Обязательно, если нет водительского удостоверения РФ. |
| `license` | Водительское удостоверение. | [LicenseInfo](../../thematic-section/insurance/calc.md#licenseinfo) | Необязательно, если указано иностранное водительское удостоверение `foreign_license`. |
| `middle_name` | Отчество. | `string` | Пример: `Иванович`. |
| `passport` | Паспортные данные. | [PassportInfo](../../thematic-section/insurance/calc.md#passportinfo) |  |
| `previous_license` | Предыдущее водительское удостоверение. | [PreviousLicenseInfo](../../thematic-section/insurance/calc.md#previouslicenseinfo) |  |

### VehicleInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand` | Бренд автомобиля. | [BrandInfo](../../thematic-section/insurance/calc.md#brandinfo) |  |
| `car_documents` | Документы на автомобиль. | [CarDocument[]](../../thematic-section/insurance/calc.md#cardocument) |  |
| `engine_power` | Мощность двигателя в л.с. | `number` | Пример: `150`. |
| `model` | Модель автомобиля. | [ModelInfo](../../thematic-section/insurance/calc.md#modelinfo) |  |
| `year` | Год выпуска. | `integer` | Пример: `2020`. |
| `body_number` | Номер кузова. | `string` | Обязательно, если нет `vin` или c`hassis_number`. Пример: `ABC123456789`. |
| `car_number` | Номер автомобиля. | `string` | Обязательно, если есть СТС. Пример: `А123БВ777`. |
| `category` | Категория транспортного средства. | `string` | Пример: `B`. Возможные значения: `A`, `B`, `C`, `D`, `E`. |
| `chassis_number` | Номер шасси. | `string` | Обязательно, если нет `body_number` или `vin`. Пример: `CHS987654321`. |
| `modification` | Модификация автомобиля. | [ModificationInfo](../../thematic-section/insurance/calc.md#modificationinfo) |  |
| `vin` | VIN номер. | `string` | Обязательно, если нет `body_number` или `chassis_number`. Пример: `XTA210990Y2765439`. |

### ReturnUrls

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `failure_url` | URL для редиректа при ошибке. | `string` | `URI`. Пример: `https://example.com/osago/failure`. |
| `success_url` | URL для редиректа при успехе. | `string` | `URI`. Пример: `https://example.com/osago/success`. |

### AddressInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `address` | Полный адрес. | `string` | Пример: `Красноярский край, г. Красноярск, ул. Ленина, д. 1, кв. 1`. |
| `addresses_kladr_code` | Код *КЛАДР* адреса. | `string` | Пример: `7700000000000000001`. |
| `city_type` | Тип города. | `string` | Пример: `г`. |
| `region_kladr_code` | Код *КЛАДР* региона. | `string` | Пример: `7700000000000`. |
| `region_name` | Название региона. | `string` | Пример: `Красноярский край`. |
| `region_type` | Тип региона. | `string` | Пример: `г`. |
| `type` | Тип адреса. | `string` | Возможные значения:   - `registration` — адрес регистрации; - `residence` — адрес проживания.   Пример: `registration`. |
| `apartment` | Номер квартиры. | `string` | Пример: `1`. |
| `area_fias_code` | Код *ФИАС* района. | `string` | Пример: `0c5b2444-70a0-4932-980c-b4dc0d3f02b5`. |
| `block` | Строение. | `string` |  |
| `building` | Корпус. | `string` |  |
| `city_fias_code` | Код *ФИАС* города. | `string` | Пример: `0c5b2444-70a0-4932-980c-b4dc0d3f02b5`. |
| `city_kladr_code` | Код *КЛАДР* города. | `string` | Пример: `7700000000000`. |
| `city_name` | Название города. | `string` | Пример: `Красноярск`. |
| `country_code` | Код страны. | `string` | Пример: `7`. |
| `district_name` | Название района. | `string` | Пример: `Сибирский`. |
| `fias_code` | Код *ФИАС* адреса. | `string` | Пример: `f26b876b-6857-4951-b060-ec6559f04a9a`. |
| `house` | Номер дома. | `string` | Пример: `1`. |
| `house_fias_code` | Код *ФИАС* дома. | `string` | Пример: `00a77cd5-e431-46df-8832-f9f462c15205`. |
| `region_fias_code` | Код *ФИАС* региона. | `string` | Пример: `0c5b2444-70a0-4932-980c-b4dc0d3f02b5`. |
| `settlement_fias_code` | Код *ФИАС* населенного пункта. | `string` | Пример: `0c5b2444-70a0-4932-980c-b4dc0d3f02b5`. |
| `settlement_kladr_code` | Код *КЛАДР* населенного пункта. | `string` |  |
| `settlement_name` | Название населенного пункта. | `string` | Пример: `Красноярск`. |
| `settlement_type` | Тип населенного пункта. | `string` | Пример: `г`. |
| `street_fias_code` | Код *ФИАС* улицы. | `string` | Пример: `95dbf7fb-0dd4-4a04-8100-4f6c847564b5`. |
| `street_kladr_code` | Код *КЛАДР* улицы. | `string` | Пример: `7700000000000010000`. |
| `street_name` | Название улицы. | `string` | Пример: `Ленина`. |
| `street_type` | Тип улицы. | `string` | Пример: `ул`. |

### ContactInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `email` | Email адрес. | `string` | Пример: `user@example.com`. |
| `phone` | Номер телефона. | `string` | Пример: `79161234567`. |

### LicenseInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `date` | Дата выдачи / дата начала стажа. | `string` | Формат: `date`. Пример: `2015-06-10`. |
| `number` | Номер водительского удостоверения. | `string` | Пример: `123456`. |
| `series` | Серия водительского удостоверения. | `string` | Пример: `77AA`. |

### PassportInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `issue_date` | Дата выдачи. | `string` | Формат: `date`. Пример: `2010-10-05`. |
| `number` | Номер паспорта. | `string` | Пример: `567890`. |
| `series` | Серия паспорта. | `string` | Пример: `1234`. |
| `issuer` | Кем выдан. | `string` | Пример: `ОУФМС России по г. Москве`. |
| `subdivision` | Код подразделения. | `string` | Пример: `770-001`. |

### PreviousLicenseInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `first_name` | Имя. | `string` | Пример: `Иван`. |
| `last_name` | Фамилия. | `string` | Пример: `Иванов`. |
| `license` | Предыдущее водительское удостоверение. | [LicenseInfo](../../thematic-section/insurance/calc.md#licenseinfo) |  |
| `middle_name` | Отчество. | `string` | Пример: `Иванович`. |

### BrandInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `brand_id` | Идентификатор бренда. | `string` | Пример: `1`. |
| `name` | Название бренда. | `string` | Пример: `Toyota`. |
| `name_ru` | Название бренда на русском. | `string` | Пример: `Тойота`. |

### CarDocument

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `date` | Дата выдачи документа. | `string` | Формат: `date`. Пример: `2020-05-15`. |
| `document_type` | Тип документа. | `string` | Пример: `sts`. Возможные значения:   - `sts`; - `pts`; - `epts`. |
| `number` | Номер документа. | `string` | Пример: `123456`. |
| `series` | Серия документа. | `string` | Пример: `77AA`. |

### ModelInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `model_id` | Идентификатор модели. | `string` | Пример: `101`. |
| `name` | Название модели. | `string` | Пример: `Camry`. |
| `name_ru` | Название модели на русском. | `string` | Пример: `Камри`. |

### ModificationInfo

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `modification_id` | Идентификатор модификации. | `string` | Пример: `5001`. |
| `name` | Название модификации. | `string` | Пример: `2.0 Turbo (249 л.с.)`. |

## Успешный ответ

**200 OK**

Формат ответа

```
{
    "request_id": "550e8400-e29b-41d4-a716-446655440000",
    "calculation_date": "2023-12-01T00:00:00Z"
}
```

|  |  |  |  |
| --- | --- | --- | --- |
| **Параметр** | **Описание** | **Тип** | **Комментарий** |
| `request_id` | Идентификатор запроса. | `string` | `UUID`. Пример: `550e8400-e29b-41d4-a716-446655440000`. |
| `calculation_date` | Дата расчета. | `string` | В формате `date-time`. Пример: `2023-12-01T00:00:00Z`. |
