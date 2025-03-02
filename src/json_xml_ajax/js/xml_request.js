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