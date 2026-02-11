---
source: https://yandex.ru/support/direct/ru/feeds/examples
---


# Примеры фидов по категориям

Примеры заполнения фида для некоторых категорий товаров в формате YML и автомобилей в формате XML.

Автомобили

##### **Новый автомобиль**

```
<?xml version="1.0"?>
<data>
    <cars>
        <car>
            <mark_id>Hyundai</mark_id>
            <folder_id>Sonata</folder_id>
            <modification_id>2.0 AT (150 л.с.)</modification_id>
            <url>http://www.auto.ru/1</url>
            <images>http://picture.auto.ru/1.jpg</images>
            <body_type>Седан</body_type>
            <color>серый</color>
            <availability>в наличии</availability>
            <custom>растаможен</custom>
            <year>2022</year>
            <price>2575000</price>
            <currency>RUR</currency>
            <vin>XWBCA41ZXDK259205</vin>
            <owners_number>Не было владельцев</owners_number>
            <max_discount>90000</max_discount>
         </car>
     </cars>
</data>
```

##### **Подержанный автомобиль**

```
<?xml version="1.0"?>
<data>
    <cars>
        <car>
            <mark_id>Nissan</mark_id>
            <folder_id>Juke, I Рестайлинг</folder_id>
            <modification_id>1.6 CVT (117 л.с.)</modification_id>
            <url>http://www.auto.ru/2</url>
            <body_type>Внедорожник 5 дв.</body_type>
            <color>белый</color>
            <availability>в наличии</availability>
            <custom>растаможен</custom>
            <state>среднее</state>
            <owners_number>один владелец</owners_number>
            <run>60000</run>
            <year>2017</year>
            <price>550000</price>
            <max_discount>50000</max_discount>
            <currency>RUR</currency>
            <vin>XWBCA41ZXDK259107</vin>
            <images>
                <image>http://price.site.ru/files/image2.jpg</image>
                <image>http://price.site.ru/files/image3.jpg</image>
            </images>
         </car>
     </cars>
</data>
```

Бытовая техника и электроника

```
<offer id="18295" type="vendor.model" available="true">
  <name>Парогенератор Bosch TDS 4040</name>
  <categoryId>123</categoryId>
  <url>https://best-seller.ru/product-parogenerator-bosch-tds-4040</url>
  <picture>https://best-seller.ru/img/picture1.jpg</picture>
  <picture>https://best-seller.ru/img/picture2.jpg</picture>
  <picture>https://best-seller.ru/img/picture3.jpg</picture>
  <picture>https://best-seller.ru/img/picture4.jpg</picture>
  <picture>https://best-seller.ru/img/picture5.jpg</picture>
  <video>https://best-seller.ru/video/5463988.mp4</video>
  <price>11670</price>
  <oldprice>12000</oldprice>
  <currencyId>RUR</currencyId>
  <typePrefix>Парогенератор</typePrefix>
  <model>TDS 4040</model>
  <vendor>Bosch</vendor>
  <description>Мощность: 2400 Вт. Постоянная подача пара. Вертикальное отпаривание. Вес: 3.4 кг; Автоматическое отключение. Автоматическая регулировка пара. Расход при паровом ударе: 270 г/мин; Максимальное давление пара: 5.5 бар.</description>
  <sales_notes>Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="Цвет">белый</param>
  <param name="Материал">Пластик</param>
  <param name="Длина" unit="см">38.5</param>
  <param name="Ширина" unit="см">19.2</param>
  <param name="Высота" unit="см">26</param>
</offer>
```

Товары для красоты и здоровья

```
<offer id="1234145" type="vendor.model" available="true">
  <name>Мягкий тоник для лица L'Oreal Paris для сухой и чувствительной кожи</name>
  <categoryId>6</categoryId>
  <url>https://best-cosm.ru/product_page.asp?pid=12345</url>
  <picture>https://best-cosm.ru/img/picture1.jpg</picture>
  <picture>https://best-cosm.ru/img/picture2.jpg</picture>
  <picture>https://best-cosm.ru/img/picture3.jpg</picture>
  <picture>https://best-cosm.ru/img/picture4.jpg</picture>
  <picture>https://best-cosm.ru/img/picture5.jpg</picture>
  <video>https://best-cosm.ru/video/54533.mp4</video>
  <price>1000</price>
  <oldprice>1200</oldprice>
  <currencyId>RUR</currencyId>
  <typePrefix>Тоник для лица</typePrefix>
  <vendor>L'Oreal Paris</vendor>
  <model>Trio Active для сухой и чувствительной кожи</model>
  <description>Мягко тонизирует, нейтрализует токсины и удаляет остатки загрязнений. Создает ощущение свежести и комфорта. Увлажняет и предохраняет кожу от пересушивания, придает ей сияние.</description>
  <sales_notes>Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="Объем" unit="мл">200</param>
  <param name="Тип кожи">Для сухой и чувствительной</param>
  <param name="Линейка">Trio Active</param>
  <param name="Пол">Женский</param>
  <param name="Возраст">Взрослый</param>
</offer>
```

Мебель

```
<offer id="499871680344" type="vendor.model" available="true">
  <name>Диван Лофт Еллоу механизм еврокнижка</name>
  <categoryId>1</categoryId>
  <url>https://www.example.ru/myagkaya-mebel/loft-ellou/</url>
  <picture>https://www.example.ru/model-image/loft-ellou1.jpg</picture>
  <picture>https://www.example.ru/model-image/loft-ellou2.jpg</picture>
  <picture>https://www.example.ru/model-image/loft-ellou3.jpg</picture>
  <picture>https://www.example.ru/model-image/loft-ellou4.jpg</picture>
  <picture>https://www.example.ru/model-image/loft-ellou5.jpg</picture>
  <video>https://www.example.ru/video/loft-ellou-0005.mp4</video>
  <price>29400</price>
  <oldprice>35280</oldprice>
  <currencyId>RUR</currencyId>
  <vendor>Фабрика монолит</vendor>
  <model>Лофт Еллоу</model>
  <typePrefix>Диван</typePrefix>
  <description>Современный диван Лофт Еллоу. Прочный механизм трансформации «еврокнижка», удобные большие подушки. Большое спальное место. Наполнитель -ППУ+ремни. Подушки набивные: поролоновая крошка+синтешар.</description>
  <sales_notes>Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="Длина" unit="см">250</param>
  <param name="Ширина" unit="см">97</param>
  <param name="Высота" unit="см">95</param>
  <param name="Цвет">желтый</param>
  <param name="Материал">Рогожка</param>
</offer>
```

Медицинские товары

```
<offer id="345939" type="vendor.model" available="true">
  <name>NOW - комплекс витаминов B-50, 100 капс</name>
  <categoryId>3</categoryId>
  <url>https://example-apteka.ru/katalog-tovarov/vitaminy/vitaminy-gruppy-b/kompleks-vitaminov-b-50-now-100-tab</url>
  <picture>https://example-apteka.ru/3429951.jpg</picture>
  <picture>https://example-apteka.ru/3429952.jpg</picture>
  <picture>https://example-apteka.ru/3429953.jpg</picture>
  <picture>https://example-apteka.ru/3429954.jpg</picture>
  <picture>https://example-apteka.ru/3429955.jpg</picture>
  <video>https://example-apteka.ru/54533.mp4</video>
  <price>200</price>
  <oldprice>260</oldprice>
  <currencyId>RUR</currencyId>
  <vendor>Now Foods</vendor>
  <typePrefix>Комплекс витаминов B-50</typePrefix>
  <model>100 капсул</model>
  <description>Комплекс витаминов B-50 поможет обеспечить организм важнейшими витаминами группы B, которые отвечают за многие процессы в человеческом организме. Принимают участие в росте и укреплении волос, укрепляют нервную систему.</description>
  <sales_notes>Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="форма выпуска">капсулы</param>
  <param name="количество в упаковке">100 шт</param>
</offer>
```

Одежда и обувь

```
<offer id="12341" type="vendor.model" available="true">
  <name>Женская куртка Calvin Klein Aberash</name>
  <categoryId>6</categoryId>
  <url>http://best-clothes.ru/product_page12344</url>
  <picture>https://best-clothes.ru/img/picture1.jpg</picture>
  <picture>https://best-clothes.ru/img/picture2.jpg</picture>
  <picture>https://best-clothes.ru/img/picture3.jpg</picture>
  <picture>https://best-clothes.ru/img/picture4.jpg</picture>
  <picture>https://best-clothes.ru/img/picture5.jpg</picture>
  <video>https://best-clothes.ru/video/54533118.mp4</video>
  <price>7000</price>
  <oldprice>10000</oldprice>
  <currencyId>RUR</currencyId>
  <vendor>Calvin Klein</vendor>
  <typePrefix>куртка</typePrefix>
  <model>Aberash</model>
  <description>Женская куртка свободного кроя с капюшоном обеспечит тепло комфорт во время прогулок.</description>
  <sales_notes>Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="Размер" unit="RU">44</param>
  <param name="Цвет">Коричневый</param>
  <param name="Пол">Женский</param>
  <param name="Материал">Полиэстер 100%</param>
</offer>
```

Товары для спорта

```
<offer id="12341" type="vendor.model" available="true">
  <name>Сноуборд Burton Ripcord (14–15)</name>
  <categoryId>3</categoryId>
  <url>https://example-sport.ru/product_12344</url>
  <picture>https://example-sport.ru/img/device123451.jpg</picture>
  <picture>https://example-sport.ru/img/device123452.jpg</picture>
  <picture>https://example-sport.ru/img/device123453.jpg</picture>
  <picture>https://example-sport.ru/img/device123454.jpg</picture>
  <picture>https://example-sport.ru/img/device123455.jpg</picture>
  <video>https://example-sport.ru/54533.mp4</video>
  <price>16500</price>
  <oldprice>19800</oldprice>
  <currencyId>RUR</currencyId>
  <typePrefix>Сноуборд</typePrefix>
  <vendor>Burton</vendor>
  <model>Ripcord (14–15)</model>
  <description>Сноуборд Burton Ripcord — это универсальная и мягкая доска, ориентированная на новичков, желающих обучиться азам сноубординга, а так же для дальнейшего совершенствования в этом виде спорта.</description>
  <sales_notes>Необходима предоплата. Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <country_of_origin>США</country_of_origin>
  <param name="Размер" unit="см">154</param>
  <param name="Цвет">Крансый</param>
  <param name="Пол">Унисекс</param>
  <param name="Возраст">Взрослый</param>
</offer>
```

Ювелирные изделия

```
<offer id="12345" type="vendor.model" available="true">
  <name>Кольцо Сияние из белого золота с бриллиантами фактурное</name>
  <categoryId>2056</categoryId>
  <url>https://example-uvelir.ru/product_page.asp?pid=12344</url>
  <picture>https://example-uvelir.ru/img/picture1.jpg</picture>
  <picture>https://example-uvelir.ru/img/picture2.jpg</picture>
  <picture>https://example-uvelir.ru/img/picture3.jpg</picture>
  <picture>https://example-uvelir.ru/img/picture4.jpg</picture>
  <picture>https://example-uvelir.ru/img/picture5.jpg</picture>
  <video>https://example-uvelir.ru/54533.mp4</video>
  <price>7990</price>
  <oldprice>8990</oldprice>
  <currencyId>RUB</currencyId>
  <vendor>Сияние</vendor>
  <typePrefix>Кольцо</typePrefix>
  <model>из белого золота с брилиантами</model>
  <store>true</store>
  <pickup>true</pickup>
  <delivery>true</delivery>
  <description>Кольцо из белого золота с фактурным эффектом замерших волн. Оригинальная изящная форма в сочетании с практичностью.</description>
  <sales_notes>Упаковка в подарок. Скидка 10% на первую покупку. Бонусные баллы по карте постоянного покупателя.</sales_notes>
  <param name="Вес">0.85</param>
  <param name="Материал">золото</param>
  <param name="Проба золота">585</param>
  <param name="Тип золота">белое</param>
  <param name="Вставка">Бриллиант (природный) (23)</param>
</offer>
