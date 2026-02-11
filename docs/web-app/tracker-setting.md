---
source: https://yandex.ru/support/direct/ru/web-app/tracker-setting
---

Настройка трекера

# Настройка трекера

- [Шаг 1. Настройка сбора данных в мобильном приложении](ru/web-app/tracker-setting#setup)
- [Шаг 2. Настройка пересылки событий](ru/web-app/tracker-setting#forwarding)
- [Шаг 3. Настройка ссылок на приложение](ru/web-app/tracker-setting#linking)
- [Настройка универсальных ссылок](ru/web-app/tracker-setting#url-settings)
- [Настройка трекинговых ссылок](ru/web-app/tracker-setting#treking-links)

Настройка трекера состоит из 3 шагов:

1. [Настройка сбора данных в мобильном приложении](ru/web-app/tracker-setting#setup).
2. [Настройка пересылки событий](ru/web-app/tracker-setting#forwarding).
3. [Настройка ссылок на приложение](ru/web-app/tracker-setting#linking).

## Шаг 1. Настройка сбора данных в мобильном приложении

Если вы уже использовали ретаргетинг по событиям из приложения в других рекламных сетях, то этот шаг можно пропустить.

##### **Чек-лист по настройке событий в трекере:**

- Проверьте, что в трекере собираются события, на которые вы хотите оптимизировать кампании или делать ретаргетинг.
- Если вы планируете запускать товарные объявления и объявления для страниц каталога, убедитесь, что у вас собираются следующие события: просмотр страницы товара, добавление и удаление из корзины, покупка товара. События включают id ваших продуктов.
- Для использования стратегии [Максимум конверсий](ru/strategies/average-cpa) с ограничением «Доля рекламных расходов» (ДРР) необходимо также фиксировать выручку.

Если вы не знаете, как проверить, настроены ли события корректно, обратитесь к разработчику приложения или в поддержку вашего трекера.

AppMetrica

AppsFlyer

Adjust

##### **Формат данных для текстово-графических объявлений**

Поддерживаются все виды разметки — обычные [События](https://appmetrica.yandex.ru/docs/data-collection/about-events.html), [ECommerce](https://appmetrica.yandex.ru/docs/data-collection/about-ecommerce.html), [In-App покупки](https://appmetrica.yandex.ru/docs/data-collection/about-revenue.html).

##### **Формат данных для товарных объявлений и объявлений для страниц каталога**

Требуется разметка [ECommerce-событий](https://appmetrica.yandex.ru/docs/data-collection/about-ecommerce.html). Она доступна для версий выше 3.16.1 на Android и 3.12.0 на iOS.

Для работы товарных объявлений и объявлений для страниц каталога достаточно следующих событий:

- `showProductDetailsEvent`;
- `addCartItemEvent`;
- `removeCartItemEvent`;
- `purchaseEvent`.

В каждом из событий в классе ECommerceProduct должен быть передан SKU (артикул товара). Остальные параметры нужны для наполнения отчета **Анализ покупок**.

Внимание

Убедитесь, что id товара в событиях совпадает с id товара в фиде — иначе для кампании потребуется сгенерировать новый фид либо перевыпустить приложение с другими id.

##### **Отслеживание открытий**

Чтобы AppMetrica смогла атрибутировать конверсию после перехода по универсальной или трекинговой ссылке, необходимо настроить [отслеживание открытий по deeplink](https://appmetrica.yandex.ru/docs/data-collection/deeplinks.html).

В SDK 4.0 и выше отслеживание [работает автоматически](https://appmetrica.yandex.ru/docs/data-collection/deeplinks.html).

##### **Требования для стратегии Максимум конверсий с ограничением ДРР**

Для использования конверсий в этой стратегии подойдут [ECommerce-события](https://appmetrica.yandex.ru/docs/data-collection/about-ecommerce.html) или разметка [In-App покупок](https://appmetrica.yandex.ru/docs/data-collection/about-revenue.html).

##### **Формат данных для текстово-графических объявлений**

Поддерживаются любые события формата [Rich In-App Events](https://support.appsflyer.com/hc/ru/articles/360019347957--WIP-Recommended-eCommerce-app-events#recommended-structures-for-predefined-events).

##### **Формат данных для товарных объявлений и объявлений для страниц каталога**

Требуются следующие события формата [Rich In-App Events](https://support.appsflyer.com/hc/ru/articles/360019347957--WIP-Recommended-eCommerce-app-events#recommended-structures-for-predefined-events):

- Просмотр товара — `af_content_view`;
- Добавление в корзину — `af_add_to_cart`;
- Удаление из корзины — `remove_from_cart`;
- Покупка — `af_purchase`.

Во всех событиях должен быть добавлен параметр `af_content_id`, в который передается id товара.

Подробнее см. в [документации трекера по имплементации кода событий](https://dev.appsflyer.com/hc/docs/in-app-events-sdk).

Внимание

Убедитесь, что id товара в событиях совпадает с id товара в фиде — иначе для кампании потребуется сгенерировать новый фид либо перевыпустить приложение с другими id.

##### **Требования для стратегии Максимум конверсий с ограничением ДРР**

Необходимо настроить сбор выручки в параметре `af_revenue` событий мобильного приложения. Инструкции для разработчиков:

- [Android](https://dev.appsflyer.com/hc/docs/in-app-events-android#logging-revenue)
- [iOS](https://dev.appsflyer.com/hc/docs/in-app-events-ios#logging-revenue)

##### **Формат данных для текстово-графических объявлений**

Поддерживаются любые [события Adjust](https://help.adjust.com/ru/classic/article/app-events-classic).

##### **Формат данных для товарных объявлений и объявлений для страниц каталога**

Поддерживаются события с [Partner Parameters](https://help.adjust.com/ru/article/receive-custom-event-data-with-partner-parameters) (доступно в Adjust SDK версий 4.0 и выше),в которых ожидается параметр `offer_id` , значением которого является либо id одного товара, либо список товаров в формате json.

Пример события с одним значением

```
AdjustEvent event = new AdjustEvent("VIEWED_CONTENT");
event.addPartnerParameter("offer_id", "10001");
Adjust.trackEvent(event);
```

Пример события со списком товаров

```
AdjustEvent event = new AdjustEvent("PURCHASED");
event.addPartnerParameter("offer_id", "[\"1234\",\"5678\"]");
Adjust.trackEvent(event);
```

Если id товара есть в параметрах событий, но его название отличается от offer\_id, то изменений в приложении не потребуется — вы сможете поменять его при настройке передачи событий в Директ с помощью [Parameter Mapping](https://help.adjust.com/en/integrated-partners/yandex#forward-custom-data).

Внимание

Убедитесь, что id товара в событиях совпадает с id товара в фиде — иначе для кампании потребуется сгенерировать новый фид либо перевыпустить приложение с другими id.

##### **Атрибуция с помощью отслеживания deeplink**

Чтобы Adjust смог атрибутировать конверсии после перехода в приложение, в нем необходимо поддержать отслеживание диплинков. Инструкции для разработчиков:

- [Android](https://help.adjust.com/en/article/deep-linking-android-sdk#reattribution-deep-links)
- [iOS](https://help.adjust.com/en/article/deep-linking-ios-sdk#reattribution-deep-links)

##### **Требования для стратегии Максимум конверсий с ограничением ДРР**

Необходимо настроить сбор выручки в событиях мобильного приложения. Инструкции для разработчиков:

- [Android](https://help.adjust.com/en/article/event-tracking-android-sdk#revenue-tracking)
- [iOS](https://help.adjust.com/en/article/event-tracking-ios-sdk#revenue-tracking)

## Шаг 2. Настройка пересылки событий

Настройте отправку событий мобильного приложения из трекера в Директ, чтобы использовать их в оптимизации стратегий или в качестве условия ретаргетинга.

AppMetrica

AppsFlyer

Adjust

##### **Для текстово-графических объявлений**

События пересылаются автоматически: дополнительные настройки в трекере не требуются. В кабинете Директа необходимо выбрать события, по которым будет фиксироваться статистика по целям мобильных приложений.

Доступна оптимизация и ретаргетинг по целям.

##### **Для товарных объявлений и объявлений для страниц каталога**

- В настройках приложения в поле **Привязка к счетчику Метрики** укажите счетчик Метрики.
- У логина должен быть доступ к счетчику.

Рекомендуем использовать счетчик сайта, на котором настроена [электронная коммерция](https://yandex.ru/support/metrica/ecommerce/about.html) — так алгоритмы машинного обучения будут учитывать товары, просмотренные в приложении, для посетителей сайта, и наоборот. Это позволяет повысить эффективность ретаргетинга.

##### **Общие правила настройки**

1. Откройте раздел **Integrated Partners** и выберите партнера **Yandex.Direct**.

2. Перейдите на вкладку **Integration**.

3. Включите опцию **Activate partner**.

4. В поле **Yandex App ID** укажите **App ID**, полученный при [добавлении мобильного приложения](ru/web-app/tracker-setting#add-aps) в Директ.

5. Включите опцию **In-app events postback** для передачи событий.

6. Выберите события и настройте соответствие **SDK Event Name > Partner Event Identifier**. Используйте идентификаторы EVENT\_1, EVENT\_2 или EVENT\_3, если ни один из предопределенных не подходит.

7. Выберите **Sending option: All media sources, including organic** и **Send revenue: Values & revenue** для передачи выручки и параметров событий.

##### **Требования для товарных объявлений и объявлений для страниц каталога**

1. В поле **Yandex Ecom Feed Counter ID** укажите счетчик Метрики в формате `12345`.

Рекомендуем использовать счетчик сайта, на котором настроена [электронная коммерция](https://yandex.ru/support/metrica/ecommerce/about.html) — так алгоритмы машинного обучения будут учитывать товары, просмотренные в приложении, для посетителей сайта, и наоборот. Это позволяет повысить эффективность ретаргетинга.

2. Выберите события:

- `af_content_view` > `VIEWED_CONTENT` (обязательно);
- `af_added_to_cart` > `ADDED_TO_CART` (обязательно);
- `remove_from_cart` > `REMOVED_FROM_CART` (желательно);
- `af_purchase` > `PURCHASED` (обязательно).

3. Выберите **Sending option: All media sources, including organic** и **Send revenue: Values & revenue** для передачи выручки и параметров событий.

##### **Требования для стратегии Максимум конверсий с ограничением ДРР**

Выберите опцию **Send revenue: Values & revenue** для передачи выручки.

**Общие правила настройки**

1. Зайдите в настройки приложения и откройте раздел **Partner Setup**.

2. Выберите **Add Partner** → **Yandex.Direct** → **(+)**.

3. В поле **Yandex App ID** укажите **App ID**, полученный при [добавлении мобильного приложения](ru/web-app/tracker-setting#add-aps) в Директ.

4. Включите опции **In-App Revenue Forwarding**, **Parameter Forwarding** и **Session Forwarding**.

5. Настройте передачу событий в разделе **Event Linking**, указав соответствующее название из списка. Все настройки указываются на iOS и Android отдельно.

##### **Требования для товарных объявлений и объявлений для страниц каталога**

1. В поле **Yandex Ecom Feed Counter** укажите счетчик Метрики в формате `12345`.

Рекомендуем использовать счетчик сайта, на котором настроена [электронная коммерция](https://yandex.ru/support/metrica/ecommerce/about.html) — так алгоритмы машинного обучения будут учитывать товары, просмотренные в приложении, для посетителей сайта, и наоборот. Это позволяет повысить эффективность ретаргетинга.

2. В разделе **Event Linking** настройте передачу событий:

- Просмотр товара — `Viewed content` (обязательно);
- Добавление в корзину — `Added to cart` (обязательно);
- Удаление из корзины — `Removed from cart` (желательно);
- Покупка — `Purchased` (обязательно).

3. Если в событиях параметр **ID товара** называется не `offer_id`, нажмите **Partner Parameter Mapping**. В поле **FROM APP** укажите, как параметр называется в SDK, а в поле **TO PARTNER** укажите `offer_id`.

## Шаг 3. Настройка ссылок на приложение

Используйте [универсальные ссылки](ru/web-app/tracker-setting#url-settings), которые приведут пользователей в приложение, если оно уже установлено, или на сайт, если приложения еще нет, — это позволяет повысить конверсионность кампаний.

Если у вас нет возможности настроить универсальные ссылки или они по каким-то причинам вам не подходят, то вы можете использовать [трекинговые ссылки](ru/web-app/tracker-setting#treking-links).

## Настройка универсальных ссылок

Использование универсальных ссылок позволяет работать с тем же фидом, который используется для сайта, в товарных объявлениях и объявлениях для страниц каталога в Единой перфоманс-кампании.

##### **Общие правила для ссылок**

Ссылка на приложение должна подходить для учета конверсий, то есть:

- вести в приложение, если оно установлено;
- вести на сайт, если приложение не установлено или клик совершен на компьютере;
- позволять трекеру атрибутировать конверсии к клику.

Как проверить, настроены ли универсальные ссылки

Универсальные ссылки имеют вид обычной ссылки (например, `avito.ru` ) и подключаются на сайте и в приложении без участия SDK трекера. Если приложение установлено, вставьте ссылку в Telegram или Notes и кликните по ней. Должно открыться приложение.

Если приложение не установлено, вы можете проверить, установлены ли универсальные ссылки по файлу на сайте, заменив `example.ru` на ваш домен:

- iOS: <https://www.example.ru/.well-known/apple-app-site-association>;
- Android: <https://www.example.ru/.well-known/assetlinks.json>.

Должна открыться страница с текстом или скачаться текстовый файл.

Как настроить универсальные ссылки

Инструкция для разных платформ:

- [iOS Universal Links](https://developer.apple.com/ios/universal-links);
- [Android App Links](https://developer.android.com/training/app-links#add-app-links).

Если у вас нет возможности настроить универсальные ссылки или они по каким-то причинам вам не подходят, то вы можете использовать [трекинговые ссылки](ru/web-app/tracker-setting#treking-links). В них есть домен трекера (например, `adj.st`, `onelink.me`, `redirect.appmetrica.com`), и они создаются в трекере.

##### **Трекинговые параметры в универсальных ссылках**

Чтобы после перехода по универсальной ссылке объявления происходила атрибуция конверсии к Директу, ссылка должна содержать набор обязательных трекинговых параметров. Для приложений с AppMetrica или Adjust они добавляются к ссылке так же и там же, где и UTM-метки для веб-трафика, в блоке **Параметры URL** в [настройках кампании, групп, объявлений](ru/statistics/url-tags-for-camping#how-add).

Если вы используете AppsFlyer, при настройке кампании подключите межсерверную отправку кликов.

AppMetrica

AppsFlyer

Adjust

Добавьте в кампании параметр `referrer=reattribution%3D1`.

В товарных объявлениях и объявлениях для страниц каталога в Единой перфоманс-кампании можно добавить параметр на уровне группы объявлений, не внося изменений в фид.

Дополнительные изменения в ссылке не требуются. Клики будут отправляться из Директа в AppsFlyer c помощью отслеживания server-to-server.

Межсерверная отправка кликов подключается при настройке кампании в Директе. Начните создавать кампанию, выберите цель для мобильного приложения. После этого на странице ниже появится блок, в котором активируется передача кликов в трекер мобильного приложения.

Добавьте в универсальную ссылку параметры:

- `adjust_ya_click_id={logid}`;
- `adjust_campaign={campaign_name}`;
- `adjust_t=abc_def`: впишите ID трекер-токена (уникальный [токен идентификации](https://help.adjust.com/ru/article/tracker-urls#adjust-tracker-token), который автоматически создается для каждого трекера Adjust). Вместо `abc` для Android, вместо `def` — для iOS. Оставьте подчеркивание посередине. Если приложение мультиплатформенное, то указывается единый ID трекера: `adjust_t=abc`. Допустимо использовать параметр `adjust_tracker` вместо `adjust_t`.

Пример ссылки:

`https://example.ru/cars/new/group/bmw/3er/21398591-21398651?adjust_ya_click_id={logid}&adjust_t=abc_def&adjust_campaign={campaign_name}`

Прежде чем использовать универсальные ссылки в кампании, важно их [протестировать](https://help.adjust.com/ru/article/test-your-universal-links). Это обеспечит их правильную настройку, доставку пользователю предназначенного ему контента и отслеживание этих ссылок Adjust.

См. также [FAQ по универсальным ссылкам в Adjust](https://help.adjust.com/ru/article/universal-links-faqs).

## Настройка трекинговых ссылок

Мы рекомендуем использовать [универсальные ссылки](ru/web-app/tracker-setting#url-settings), но если у вас нет возможности их настроить, вы можете реализовать маршрутизацию пользователей при помощи трекинговых ссылок, которые создаются в интерфейсе мобильного трекера.

При использовании трекинговых ссылок вам необходимо обновить фид в товарных объявлениях и объявлениях для страниц каталога в Единой перфоманс-кампании. Ссылки на товары в нем необходимо заменить на трекинговые.

По ссылке ожидаются следующие сценарии:

|  |  |
| --- | --- |
| **Сценарий** | **Ссылка** |
| Переход с мобильного. Приложение не установлено | 1. Нужный раздел или страница товара на мобильной версии сайта.  2. Страница приложения в магазине приложений. После установки приложения желательно, чтобы срабатывал `deferred deeplinking` (отложенный диплинкинг) для перевода на нужный раздел или товар в приложении. |
| Переход с мобильного. Приложение установлено | Нужный раздел или страница товара в приложении. |
| Переход на компьютере | Нужный раздел или страница товара на сайте. |

AppMetrica

AppsFlyer

Adjust

##### **Как настроить**

1. Настройте универсальные ссылки для iOS.

Добавьте:

- [Поддержку Universal Links](https://appmetrica.yandex.ru/docs/mobile-sdk-dg/ios/ios-universal-links.html) в приложении.
- Отслеживание открытий deeplink на [iOS](https://appmetrica.yandex.ru/docs/mobile-sdk-dg/ios/ios-operations.html#deeplink-tracking).

2. Настройте поддержку deeplink для Android.

Добавьте:

- [Поддержку deeplink](https://developer.android.com/training/app-links/deep-linking#adding-filters) в приложении.
- Отслеживание открытий deeplink для [Android](https://appmetrica.yandex.ru/docs/mobile-sdk-dg/android/about/android-operations.html#deeplink-tracking).

3. Создайте трекинговую ссылку SmartLink.

Настройка

Добавьте [ремаркетинговый трекер с SmartLink](https://yandex.ru/dev/appmetrica/doc/mobile-tracking/concepts/add-remarketing-tracker.html).

Пример настройки для ссылок, используемых в сценарии Web+App:

- В поле **Магазины приложений** укажите: Google Play, App Store, Fallback (для web).
- Для каждого Магазина приложения необходимо задать Целевую ссылку и Deeplink:
- В поле **Целевая ссылка** задайте ссылку на страницу приложения в магазине или шаблон вида `https://myshop.ru/{path}`, где `{path}` будет содержать путь до конкретной страницы мобильного сайта. Так пользователи, у которых не установлено приложение, попадут или в магазин приложений, или на мобильную версию сайта.
- В поле **Deeplink** задайте шаблон вида `myshop://{path}`, где `{path}` будет содержать путь до конкретной страницы в приложении. Так пользователи, у которых установлено приложение, попадут на нужную страницу в приложении.
- Используйте app-to-app ссылку — в ней поддержаны настройки для работы Universal links.
- В поле **Fallback** укажите шаблон вида `https://myshop.ru/{path}`, где `{path}` будет содержать путь до конкретной страницы десктопного сайта. Так пользователи, которые переходят по ссылке с десктопа, попадут на десктопную версию сайта.

При корректной настройке Universal links отобразится app-to-app ссылка — используйте именно ее.

UTM-метки и другие пользовательские параметры можно задать в настройках Smart Link по [инструкции](https://appmetrica.yandex.ru/docs/mobile-tracking/concepts/tracking-specification.html#passing-params).

Пример ссылки:
`https://0000000.redirect.appmetrica.yandex.com/cars/new/group/bmw/3er/21398591-21398651?appmetrica_tracking_id=00000000000000000&referrer=reattribution%3D1&click_id={LOGID}&campaign_id={campaign_id}&path=%2F%20cars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651`
Подробнее см. [Трекинговые ссылки на базе Universal Links](ru/impression-criteria/universal-links).

##### **Обновление ссылок в фиде**

Получившийся шаблон ссылки передайте разработчику для перегенерации ссылок на товары в фиде.

В фиде добавьте трекинговую ссылку в элемент, содержащий ссылку на товар. Ссылка должна вести пользователя на конкретный товар — на сайте или в приложении. Для XML/YML фидов соблюдайте [дополнительные требования](https://yandex.ru/support/partnermarket/export/yml.html#requirements).

##### **Как настроить**

1. Настройте ссылки:

- [iOS](https://dev.appsflyer.com/hc/docs/dl_ios_init_setup#procedures-for-ios-universal-links)
- [Android App Links](https://dev.appsflyer.com/hc/docs/dl_android_init_setup#procedures-for-android-app-links)
- Samsung OS — [схемы URI](https://dev.appsflyer.com/hc/docs/dl_android_init_setup#procedures-for-uri-scheme)

2. Добавьте [шаблон OneLink](https://support.appsflyer.com/hc/ru/articles/207032246).

Он является основой логики перенаправления в сценариях для всех ссылок OneLink, которые используются в кампаниях:

- **Приложение не установлено** — пользователь переходит в нужный магазин приложений или на мобильный веб-адрес.

  Настройка

  [Инструкция](https://support.appsflyer.com/hc/ru/articles/207032246#create-a-onelink-template-with-redirection-logic-for-new-app-users) — выполните пункты 1-8, 10. В зависимости от сценария, в пункте 6 задайте перенаправление в магазин приложений или на мобильную веб-страницу. Если необходимо, добавьте брендированный домен. Подробнее в [статье](https://support.appsflyer.com/hc/ru/articles/360002329137) AppsFlyer.
- **Приложение уже установлено** — пользователь открывает приложение через Android App Links, iOS Universal Links или схемы URI.

  Настройка

  [Инструкция](https://support.appsflyer.com/hc/ru/articles/207032246#add-redirection-logic-for-existing-app-users).

  - Для универсальных ссылок iOS укажите **Team ID**.
  - Для Android App Links укажите **отпечаток SHA256** и сохраните автоматически сгенерированный **код для фильтра намерений** — он необходим для завершения настройки Android App Links.

3. Настройте [ссылки OneLink](https://support.appsflyer.com/hc/ru/articles/208874366) — кликабельные ссылки, которые отображаются в объявлениях.

Настройка

- [Инструкция](https://support.appsflyer.com/hc/ru/articles/208874366#general-settings) — пункты 1, 2, 3 обязательны для нужного сценария:

**Медиа-источник** — укажите **yandexdirect\_int** (определяет параметр `pid=yandexdirect_int`).

**Кампания** — укажите **название рекламной кампании в Директе** (определяет параметр `c=<название кампании>`).

**Ретаргетинг** необходимо включить (определяет параметр `is_retargeting=true`).

- [Диплинкинг и отложенный диплинкинг](https://support.appsflyer.com/hc/ru/articles/208874366#deep-linking-and-deferred-deep-linking) на страницу товара в приложении.

Определите значения `deep_link_value` — названия для определенного контента в приложении, на который будут перенаправлены пользователи. Используйте динамические значения, чтобы генерировать множество различных диплинков, ведущих на разный контент внутри приложения, без необходимости каждый раз менять код приложения.

Подробнее в руководстве по Унифицированному диплинкингу (UDL) для для [Android](https://dev.appsflyer.com/hc/docs/dl_android_unified_deep_linking) и [iOS](https://dev.appsflyer.com/hc/docs/dl_ios_unified_deep_linking).

- [Перенаправление на сайт при клике с десктопа](https://support.appsflyer.com/hc/ru/articles/360014821438-OneLink-%D1%83%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B5%D0%BF%D0%BE%D0%BB%D0%B0%D0%B4%D0%BE%D0%BA-%D0%B8-%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B#how-can-i-redirect-desktop-users).

URL, нужный для перенаправления при клике на десктопе, можно добавить к ссылке в параметре `af_web_dp`.

- [Дополнительные параметры](https://support.appsflyer.com/hc/ru/articles/208874366#additional-parameters).

Добавьте обязательный для интеграции с Директом параметр `clickid` со значением `{logid}` (`clickid={logid}`). Список других параметров — на [странице руководства](https://support.appsflyer.com/hc/ru/articles/207447163).

- Проведите [тестирование ссылки](https://support.appsflyer.com/hc/ru/articles/208874366#testing). См. также раздел [Устранение неполадок и часто задаваемые вопросы](https://support.appsflyer.com/hc/ru/articles/360014821438-OneLink-%D1%83%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B5%D0%BF%D0%BE%D0%BB%D0%B0%D0%B4%D0%BE%D0%BA-%D0%B8-%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B#how-can-i-redirect-desktop-users).

##### **Обязательные параметры ссылок**

- `pid=yandexdirect_int`
- `clickid={logid}`
- `is_retargeting=true`

UTM-метки и другие [пользовательские параметры](https://support.appsflyer.com/hc/ru/articles/208874366#additional-parameters) можно задать в настройках шаблона ссылки OneLink.

Пример ссылки:

> https://app.appsflyer.com/ru.magnit.express.android?c={campaign\_name}&af\_siteid={source\_type}*{source}&af\_adset\_id={gbid}&af\_ad\_id={ad\_id}&af\_keywords={keyword}&keyword\_id={phrase\_id}&is\_retargeting=true&af\_click\_lookback=7d&af\_reengagement\_window=30d&af\_inactivity\_window=0d&google\_aid={google\_aid}&android\_id={android\_id}&af\_ad={ad\_id}&af\_sub1={region\_neme}&af\_sub2={match\_type}*&af\_sub3={position\_type}\_{position}&af\_sub4={keyword}&af\_ip={client\_ip}&af\_ua={user\_agent}&af\_lang={device\_lang}&af\_web\_dp=https%3A%2F%2Fdostavka.magnit.ru%2Fexpress%2Fpromotion&af\_xp=social&deep\_link\_value=magnit.dostavka%3A%2F%2Fexpress%2Fpromotion&af\_dp=magnit.dostavka%3A%2F%2Fexpress%2Fpromotion&deep\_link\_sub1=magnit.dostavka%3A%2F%2Fexpress%2Fpromotion&advertising\_id={google\_aid}&oaid={oaid}&pid=yandexdirect\_int&clickid={logid}&af\_c\_id=

##### **Опциональные параметры**

- `af_click_lookback` — окно атрибуции (от клика до перехода в приложение). Указывается в днях (например, 14d). Дефолтное значение (если не передавать параметр) — 7 дней.
- `af_reengagement_window` — окно вовлечения (от атрибуции до конверсии). Указывается в днях. Дефолтное значение — 30 дней.

##### **Обновление ссылок в фиде**

Получившийся шаблон ссылки передайте разработчику для перегенерации ссылок на товары в фиде.

В фиде добавьте трекинговую ссылку в элемент, содержащий ссылку на товар. Ссылка должна вести пользователя на конкретный товар — на сайте или в приложении. Для XML/YML фидов соблюдайте [дополнительные требования](https://yandex.ru/support/partnermarket/export/yml.html#requirements).

Подключение описано в [Справке AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115005248543-Customer-experience-and-deep-linking-overview).

См. также [Трекинговые ссылки на базе Universal Links](ru/impression-criteria/universal-links).

##### **Как настроить**

1. Настройте [ссылки](https://help.adjust.com/ru/article/set-up-universal-links#set-up-universal-links-for-deep-linking) для диплинкинга в приложениях.

2. Настройте [ссылки](https://help.adjust.com/ru/article/deep-linking-ios-sdk#reattribution-deep-links) для реатрибуции и отложенного диплинкинга.

Чтобы [отложенный диплинкинг](https://help.adjust.com/ru/article/deferred-deep-linking-on-reinstall) работал, необходимо:

- поддержать реатрибуцию посредством диплинка на [iOS](https://help.adjust.com/ru/article/deep-linking-ios-sdk#reattribution-deep-links) и [Android](https://help.adjust.com/ru/article/deep-linking-android-sdk#reattribution-deep-links);
- включать в трек-ссылку идентификатор устройства (`IDFA` для iOS и `GPS_ADID` для Android).

3. Настройте многоплатформенную универсальную трекинг-ссылку:

- На основании необработанной универсальной трекинг-ссылки и токена трекера создайте многоплатформенную ссылку.
- Уточните, являются ли путь и параметры запроса ваших приложений на iOS и Android одинаковыми. Используйте подходящий формат:

  - iOS и Android используют [одинаковые параметры пути и запроса](https://help.adjust.com/ru/article/create-a-universal-link#shared-path-and-parameters);
  - в приложениях iOS и Android используются [разные параметры пути и запроса](https://help.adjust.com/ru/article/create-a-universal-link#different-path-and-parameters).

  Для настройки универсальной ссылки лучше использовать [генератор диплинков](https://dash.adjust.com/deeplink-generator).

  Скриншоты генератора с пояснениями

  **PLATFORM (платформа)** — введите название платформы приложения так, как оно указано на панели управления Adjust. Доступные варианты: Android; iOS; Многоплатформенные приложения.

  **AD ENVIRONMENT (рекламная среда)** — существует несколько различных форматов диплинков, которые работают в разных рекламных средах. Для Директа выберите **Other** (Другое).

  **FORMAT (формат)** — в зависимости от вашей рекламной среды может поддерживаться несколько форматов диплинков. Здесь можно задать формат, который нужно использовать. Для Директа выберите **ulink** (универсальная ссылка).

  **APP (приложение)** — выберите приложение из раскрывающегося меню. Будут перечислены все приложения из выбранной платформы.

  **TRACKER (трекер)** — выберите трекер, который хотите использовать. Будут перечислены все трекеры уровня сети из приложения.

  **RAW UNIVERSAL LINK (необработанная универсальная ссылка)** — необработанная универсальная ссылка добавляется автоматически при выборе приложения с универсальными ссылками, включенным на панели управления.

  **ANDROID APP SCHEME (схема приложения Android)** — схема задается в настройках приложения и добавляется в это поле автоматически.

  **IOS UNIVERSAL LINK PATH (путь универсальной ссылки iOS)** — путь до места назначения в приложении на iOS, куда перенаправляются пользователи. Укажите путь до конкретного товара/раздела в приложении или шаблон. [Подробнее](https://help.adjust.com/ru/article/deeplink-generator#what-syntax-is-accepted) о шаблонах и синтаксисе путей.

  **ANDROID DEEPLINK PATH (путь диплинка Android)** — путь до места назначения в приложении на Android, куда перенаправляются пользователи. Укажите путь до конкретного товара/раздела в приложении или шаблон. [Подробнее](https://help.adjust.com/ru/article/deeplink-generator#what-syntax-is-accepted) о шаблонах и синтаксисе путей.

  **CAMPAIGN, ADGROUP, CREATIVE (кампания, группа, креатив)** — макросы для Директа будут предложены автоматически. Если вы не хотите получать какой-либо из параметров, не указывайте соответствующий макрос.

  **LABEL (метка)** — здесь можно указать параметры которые не подходят ни для каких других полей в Adjust.

  **FALLBACK URL (резервный URL)** — адрес конкретной целевой страницы, на которую вы отправляете пользователей, находящихся вне поддерживаемой платформы (т. е. клики из неподдерживаемой ОС). Важно: если трекер поддерживает iOS, Adjust может перенаправить macOS-трафик в магазин App Store. Для решения проблемы можно задать URL-адрес для macOS в поле REDIRECT MACOS.

  **REDIRECT URL/MACOS/iOS/Android (перенаправление URL/MACOS/iOS/Android)** — добавьте URL-адрес перенаправления, чтобы изменить заданное по умолчанию перенаправление Adjust в магазин приложений и вместо этого отправлять пользователей на определенный URL-адрес. Пользователей можно перенаправлять по платформе устройства (REDIRECT MACOS/iOS/Android) или отправлять всех в одно местоположение (REDIRECT URL).

  **DEVICE ID MACROS (макрос идентификатора устройства)** — макросы для Директа будут предложены автоматически. Если вы не хотите получать какой-либо из параметров, не указывайте соответствующий макрос.

  [Описание параметров в документации Adjust](https://help.adjust.com/ru/article/deeplink-generator)

  ##### **Примеры ссылок для разных сценариев**

  В зависимости от сценария будут срабатывать следующие ссылки, заданные через описанные выше поля:

  - Если пользователя без приложения необходимо вести в магазин приложений:

    - iOS, есть приложение — universal link;
    - iOS, нет приложения — автоматический переход в магазин приложений;
    - Android, есть приложение — deep link;
    - Android, нет приложения — автоматический переход в магазин приложений;
    - Десктоп — FALLBACK URL и REDIRECT MACOS.

    Пример ссылки:

    > https://nquw.adj.st/product/100586311342?adj\_t=aflb3js&adj\_fallback=https%3A%2F%2Fmarket.yandex.ru%2Fproduct--cold-steel-luzon-medium-20nql%2F388454980%3Fcpa%3D1%26sku%3D100586311342&adj\_redirect\_macos=https%3A%2F%2Fmarket.yandex.ru%2Fproduct--cold-steel-luzon-medium-20nql%2F388454980%3Fcpa%3D1%26sku%3D100586311342&adj\_gps\_adid=%7Bgoogle\_aid%7D&yclid=%7Blogid%7D
  - Если пользователя без приложения необходимо вести на страницу сайта:

    - iOS, есть приложение — universal link;
    - iOS, нет приложения — REDIRECT URL IOS;
    - Android, есть приложение — deep link;
    - Android, нет приложения — REDIRECT URL ANDROID;
    - Десктоп — REDIRECT URL.

    Пример ссылки:

    > https://nquw.adj.st/product/100586311342?adj\_t=aflb3js&adj\_redirect\_ios=https%3A%2F%2Fmarket.yandex.ru%2Fproduct--cold-steel-luzon-medium-20nql%2F388454980%3Fcpa%3D1%26sku%3D100586311342&adj\_redirect\_android=https%3A%2F%2Fmarket.yandex.ru%2Fproduct--cold-steel-luzon-medium-20nql%2F388454980%3Fcpa%3D1%26sku%3D100586311342&adj\_gps\_adid=%7Bgoogle\_aid%7D&yclid=%7Blogid%7D&adj\_redirect=https%3A%2F%2Fmarket.yandex.ru%2Fproduct--cold-steel-luzon-medium-20nql%2F388454980%3Fcpa%3D1%26sku%3D100586311342&adj\_gps\_adid=%7Bgoogle\_aid%7D&yclid=%7Blogid%7D

##### **Обязательные параметры**

Обязательные трекинговые параметры необходимо добавить в ссылку для того, чтобы события в приложениях могли быть атрибутированы к клику Директа:

- в трекинговой ссылке: `adj_ya_click_id={logid}` или `adjust_ya_click_id={logid}`;
- в fallback URL внутри трекинговой ссылки: `yclid={logid}`

UTM-метки указываются в fallback URL.

Пример ссылки:

> https://sb00.adj.st/cars/new/group/bmw/3er/21398591-21398651?adjust\_ya\_click\_id={logid}&adjust\_t=abc\_def&adjust\_campaign={campaign\_name}&adjust\_deeplink=autoru%3A%2F%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651&adjust\_redirect=https%3A%2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%3Fyclid%3D

См. также [Трекинговые ссылки на базе Universal Links](ru/impression-criteria/universal-links).

Настройка ссылок в фиде

Актуально только для товарных объявлений и объявлений для страниц каталога в Единой перфоманс-кампании.

В фиде добавьте трекинговую ссылку в элемент, содержащий ссылку на товар. Ссылка должна вести пользователя на конкретный товар — на сайте или в приложении. Для XML/YML фидов соблюдайте [дополнительные требования](https://yandex.ru/support/partnermarket/export/yml.html#requirements).

Пример использования трекинговой ссылки в фиде:

```
<offer id="21398651" available="true">
    <url>https://sb00.adj.st/cars/new/group/bmw/3er/21398591-21398651?adjust_ya_click_id={logid}
         &amp;adjust_t=abc_def&amp;adjust_campaign={campaign_name}&amp;adjust_deeplink=autoru%3A
         %2F%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651&amp;adjust_redirect= https%3A%
         2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%3Fyclid%3D{logid}
    </url>
...
</offer>
```

Важно

Проверьте наличие необходимых параметров в ссылках в фиде. При необходимости вы можете добавить их на уровне группы объявлений, не изменяя сам фид.

Настройка реатрибуции

Реатрибуция — вовлечение неактивного пользователя в приложение или повторная установка приложения в результате ретаргетинга. Если это происходит в течение окна реатрибуции, источнику ретаргетинга засчитывается реатрибуция.

Настройки реатрибуции стоит установить в трекере, если вы используете цель мобильного приложения в настройках стратегии — оптимизации конверсий или целевой доли рекламных расходов.

AppsFlyer

Adjust

[Руководство по атрибуции ретаргетинга](https://support.appsflyer.com/hc/ru/articles/207033786-%D0%A0%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D1%80%D0%B5%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%B0#%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D1%80%D0%B5%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%B0) в документации AppsFlyer.

1. В настройках трекера перейдите в раздел **Configuration** → **App settings**.

2. В блоке **Attribution** выберите **Re-engagement attribution**.

Настройки реатрибуции включаются отдельно для каждого приложения.

[Настройка реатрибуции](https://help.adjust.com/en/article/reattribution) в документации Adjust.

1. В настройках трекера зайдите на вкладку **Reattribution**.

2. Укажите показатели:

- **Inactivity period** — время с момента последнего входа в приложение до возможности атрибуции. По умолчанию 7 дней, для атрибуции последнего клика должно быть 0 дней.
- **Reattribution window** — время с момента клика до конверсии, в течение которого конверсия атрибутируется источнику. По умолчанию 7 дней. Например, если пользователь кликнул по объявлению Директа в понедельник, а купил в пятницу, то покупка будет атрибутирована Директу.

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

[Добавление приложения в библиотеку Директа](ru/web-app/add-aps)

Следующая

[Настройка кампаний по сценарию Web+App](ru/web-app/campaign-settings)
