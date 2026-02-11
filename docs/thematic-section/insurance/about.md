---
source: https://yandex.ru/support/direct/ru/thematic-section/insurance/about
---


# Страхование — API для партнеров

- [Как настроить](../../thematic-section/insurance/about.md#setup)
- [Обзор ресурсов](../../thematic-section/insurance/about.md#list)
  - [Методы, предоставляющие справочники транспортных средств](../../thematic-section/insurance/about.md#metody,-predostavlyayushie-spravochniki-transportnyh-sredstv)
  - [Методы для интеграции с блоком ОСАГО](../../thematic-section/insurance/about.md#metody-dlya-integracii-s-blokom-osago)
- [Схема взаимодействия через API](../../thematic-section/insurance/about.md#scheme)

API позволяет интегрироваться с тематическим блоком, чтобы пользователи заполняли заявки на покупку полиса ОСАГО.

Благодаря интеграции пользователи смогут пройти меньше шагов от запроса до оформления полиса ОСАГО, а организации-партнеры могут увеличить возможный охват по релевантной аудитории.

Для интеграции необходимо реализовать публичный API эндпоинт.

## Как настроить

Для подключения в качестве партнера:

1. Свяжитесь со службой поддержки по адресу [finance-search@yandex-team.ru](mailto:finance-search@yandex-team.ru). В заголовке письма напишите: «Интеграция API в страховании <Название организации>».
2. Дождитесь, когда менеджер свяжется с вами по контактам, которые вы указали в письме.
3. Чтобы предоставить необходимую информацию, реализуйте публичный API эндпоинт. К нему Яндекс будет отправлять запросы. Вам нужно будет предоставлять офферы в ответ.
4. Пройдите проверку работоспособности интеграции.

## Обзор ресурсов

Конечная интеграция со страховой компанией / агрегатором страховых услуг осуществляется через REST API.

### Методы, предоставляющие справочники транспортных средств

Вызываются автоматически по планировщику для обновления справочников. Все ID справочников должны быть уникальными и не должны меняться в ходе обновления справочников на стороне партнера.

В случае изменения справочников на стороне партнера, необходимо предупредить команду Яндекса для оперативного обновления справочников.

Если партнер — агрегатор, нужно убедиться, что у вас единый справочник транспортных средств.

- [Получение списка брендов](../../thematic-section/insurance/dictionaries.md#brands).
- [Получение списка моделей](../../thematic-section/insurance/dictionaries.md#models).
- [Получение списка годов выпуска](../../thematic-section/insurance/dictionaries.md#years).
- [Получение списка мощностей двигателя](../../thematic-section/insurance/dictionaries.md#engine-powers).
- [Получение списка модификаций (необязательный)](../../thematic-section/insurance/dictionaries.md#modifications).
- [Получение иерархии автомобильных данных (необязательный)](../../thematic-section/insurance/dictionaries.md#vehicle-dictionaries).
- [Получение информации об автомобиле](../../thematic-section/insurance/dictionaries.md#vehicle-info)

### Методы для интеграции с блоком ОСАГО

- [Создание запроса на расчет ОСАГО](../../thematic-section/insurance/calc.md).
- [Получение расчета ОСАГО](../../thematic-section/insurance/calculation.md).
- [Получение статуса расчета ОСАГО (необязательный)](../../thematic-section/insurance/calculation-status.md).
- [Получение предложения ОСАГО (необязательный)](../../thematic-section/insurance/offer-status.md).
- [Подтверждение предложения ОСАГО](../../thematic-section/insurance/confirm-offer.md).
- [Запрос на получение pdf-файла с черновиком полиса](../../thematic-section/insurance/offer-draft.md).
- [Запрос на получение полиса](../../thematic-section/insurance/offer-policy.md).
- [Подтверждение продажи](../../thematic-section/insurance/confirmation-sale.md).

## Схема взаимодействия через API
