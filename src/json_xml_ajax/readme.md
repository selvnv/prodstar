#### Задание

Отправить POST запрос в формате XML на URI `/api/v1/xml/order` со следующими данными:

* order
    * атрибуты и их значения:
        * client = Jon Smith
    * вложенные теги
        * product
          * атрибуты и их значения:
              * name = product A
              * price = 20
        * product
            * атрибуты и их значения:
                * name = product B
                * price = 40
        * product
            * атрибуты и их значения:
                * name = product B
                * price = 40
        * discont
            * вложенный текст
                * 20%

#### Ответ

Запрос к серверу:

```js
(async () => {
    await fetch(
        "/api/v1/xml/order", {
            method: "POST",
            headers: {
                "Content-Type": "application/xml"
            },
            body: `<?xml version="1.0" encoding="UTF-8"?>
                <order client="Jon Smith">
                    <product name="product A" price="20"></product>
                    <product name = "product B" price="40"></product>
                    <product name="product B" price="40"></product>
                    <discount>20%</discount>
                </order>
            `
        }
    ).then(async data => {
        console.log(await data.text())
    })
})();
```
Ответ от сервера:

```xml
<order total="80" products="product B,product A" client="Jon Smith" />
```

<hr>

#### Задание

Отправить POST запрос в формате JSON на URI `/api/v1/json/order` со следующими данными:
* Объект c полями и значениями
    * client = Jon Smith
    * products = массив с объектами
        * поля и их значения:
            * name = product A
            * price = 20
        * поля и их значения:
            * name = product B
            * price = 40
        * поля и их значения:
            * name = product B
            * price = 40
    * voucher = объект с полями и значениями
        * discount = 20%

#### Ответ

Запрос к серверу
```js
(async () => {
    fetch (
        "/api/v1/json/order", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: `{
                "client": "Jon Smith",
                "products": [
                    {
                        "name": "product A",
                        "price": 20
                    },
                    {
                        "name": "product B",
                        "price": 40
                    },
                    {
                        "name": "product B",
                        "price": 40
                    }
                ],
                "voucher": {
                    "discount": "20%"
                }
            }`
        }
    ).then(async data => {
        console.log(await data.text())
    })
})();
```

Ответ сервера:
```json
{"client": "Jon Smith", "total": 80.0, "products": ["product B", "product A"]}
```