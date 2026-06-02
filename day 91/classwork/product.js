const products = [
    { name: "Laptop", price: 1200 },
    { name: "Phone", price: 800 },
    { name: "Headphones", price: 150 },
    { name: "Keyboard", price: 100 }
];

export default products

export function getAllProducts(arr) {
    return arr;
}

export function filterByPrice(arr, minPrice) {
    return arr.filter(product => product.price >= minPrice);
}