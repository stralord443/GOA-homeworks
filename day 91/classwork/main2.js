import products, { getAllProducts, filterByPrice } from "./products.js";

console.log("ყველა პროდუქტი:")
console.log(getAllProducts(products))

console.log("პროდუქტები ფასით 200-ზე მეტი:")
console.log(filterByPrice(products, 200))
