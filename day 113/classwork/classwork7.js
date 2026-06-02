// 8. URL: https://dummyjson.com/products
// კონსოლში დაბეჭდე ყველა პროდუქტის სახელი.

fetch("https://dummyjson.com/products")

.then((response)=>response.json())
.then(date => {
    date.forEach(date => {
        console.log("სახელი:", date.title)
    })
})