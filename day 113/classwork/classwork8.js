// 9. URL: https://dummyjson.com/products
// გამოიტანე თითოეული პროდუქტის:
// - სურათი
// - სახელი
// - ფასი

fetch("https://dummyjson.com/products")
.then(response => response.json())
.then(data => {
    data.products.forEach(product => {
        console.log("სურათი:", product.thumbnail)
        console.log("სახელი:", product.title)
        console.log("ფასი:", product.price)
    })
})