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