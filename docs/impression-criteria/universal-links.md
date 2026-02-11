---
source: https://yandex.ru/support/direct/ru/impression-criteria/universal-links
---


# Трекинговые ссылки на базе Universal Links

Используйте трекинговые ссылки в объявлениях, чтобы отслеживать конверсии после переходов в мобильное приложение. Возможность доступна в Единой перфоманс-кампании.

Трекинговые ссылки создаются на основе [Apple Universal Links](https://developer.apple.com/ios/universal-links/) или [Android App Links](https://developer.android.com/training/app-links). Если приложение не установлено, пользователь перейдет на сайт, если установлено — в приложение. При этом нельзя задавать переход в Google Play или App Store.

Директ поддерживает работу ссылок популярных трекинговых систем AppMetrica, Adjust и AppsFlyer. Перед созданием трекинговых ссылок проверьте с вашим мобильным разработчиком, что ваше приложение поддерживает их корректную работу.

AppMetrica

Adjust

AppsFlyer

В документации AppMetrica описано:

- поддержка [Universal Links](https://appmetrica.yandex.ru/docs/mobile-sdk-dg/concepts/ios-universal-links.html?lang=ru) и открытие приложения с помощью [deeplink](https://appmetrica.yandex.ru/docs/mobile-sdk-dg/concepts/android-operations.html#deeplink-tracking);
- настройка трекинговой ссылки [Smart Link](https://yandex.ru/dev/appmetrica/doc/mobile-tracking/concepts/add-tracker.html#add-tracker__step3).

Пример ссылки:

> https://0000000.redirect.appmetrica.yandex.com/cars/new/group/bmw/3er/21398591-21398651?appmetrica\_tracking\_id=00000000000000000&referrer=reattribution%3D1&click\_id={LOGID}&campaign\_id={campaign\_id}&path=%2F%20cars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651

В документации Adjust описано:

- как настроить [Universal Links](https://help.adjust.com/en/article/set-up-universal-links) ;
- как создать [трекинговую ссылку](https://help.adjust.com/en/article/create-a-universal-link).

Обязательные параметры описаны в разделе [Adjust](../products-mobile-apps-ads/tracking-systems.md#tracking-links). Для Universal Links от Adjust нужно добавить в параметры префикс `adjust_`или `adj_`, например: `adj_ya_click_id={logid}`. Для корректного учета конверсий при переходах на сайт добавьте в URL фолбека на сайт параметр `yclid={logid}`. При этом кодировать нужно все символы, кроме `{logid}`.

Пример ссылки:

```
https://sb00.adj.st/cars/new/group/bmw/3er/21398591-21398651?adjust_ya_click_id={logid}&adjust_t=abc_def&adjust_campaign={campaign_name}&adjust_deeplink=autoru%3A%2F%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651&adjust_redirect=
      https%3A%2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%3Fyclid%3D{logid}
```

Пример ссылки с добавлением параметров Adjust в обычный Universal Link:
`https://auto.ru/cars/new/group/bmw/3er/21398591-21398651?adjust_ya_click_id={logid}&adjust_t=abc_def&adjust_campaign={campaign_name}`

В документации AppsFlyer описано:

- как настроить [OneLink](https://dev.appsflyer.com/hc/docs/getting-started-1);
- как создать [трекинговую ссылку](https://support.appsflyer.com/hc/ru/articles/207033836-OneLink-3-4-%D0%9F%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BC%D0%B5%D1%8E%D1%89%D0%B8%D1%85%D1%81%D1%8F-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D0%B4%D0%B8%D0%BF%D0%BB%D0%B8%D0%BD%D0%BA%D0%BE%D0%B2).

Обязательные параметры описаны в разделе [AppsFlyer](../products-mobile-apps-ads/tracking-systems.md#tracking-links).

Пример ссылки:

> https://autoru.onelink.me/AbcD?pid=yandexdirect\_int&is\_retargeting=true&clickid={logid}&c={campaign\_name}&af\_dp=autoru%3A%2F%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%0A&af\_web\_dp=https%3A%2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%0A&af\_ios\_url=https%3A%2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%0A&af\_android\_url=https%3A%2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%0A

## Как использовать трекинговые ссылки в фиде

В фиде для товарных объявлений и объявлений для страниц каталога в Единой перфоманс-кампании добавьте трекинговую ссылку в элемент, содержащий ссылку на товар. Ссылка должна вести пользователя на конкретный товар — на сайте или в приложении. Для XML/YML фидов соблюдайте [дополнительные требования](https://yandex.ru/support/partnermarket/export/yml.html#requirements).

Пример использования трекинговой ссылке в фиде:

```
<offer id="21398651" available="true">
    <url>https://sb00.adj.st/cars/new/group/bmw/3er/21398591-21398651?adjust_ya_click_id={logid}
         &amp;adjust_t=abc_def&amp;adjust_campaign={campaign_name}&amp;adjust_deeplink=autoru%3A
         %2F%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651&amp;adjust_redirect= https%3A%
         2F%2Fauto.ru%2Fcars%2Fnew%2Fgroup%2Fbmw%2F3er%2F21398591-21398651%3Fyclid%3D{logid}
    </url>
...
</offer>
