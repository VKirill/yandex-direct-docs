---
source: https://yandex.ru/support/direct/ru/impression-criteria/universal-links
---

Трекинговые ссылки на базе Universal Links

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

Обязательные параметры описаны в разделе [Adjust](ru/products-mobile-apps-ads/tracking-systems#tracking-links). Для Universal Links от Adjust нужно добавить в параметры префикс `adjust_`или `adj_`, например: `adj_ya_click_id={logid}`. Для корректного учета конверсий при переходах на сайт добавьте в URL фолбека на сайт параметр `yclid={logid}`. При этом кодировать нужно все символы, кроме `{logid}`.

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

Обязательные параметры описаны в разделе [AppsFlyer](ru/products-mobile-apps-ads/tracking-systems#tracking-links).

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
```

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
