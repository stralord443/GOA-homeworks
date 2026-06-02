// 2. URL: https://jsonplaceholder.typicode.com/users
// გამოიტანე თითოეული მომხმარებლის:
// - სახელი
// - ელფოსტა
// - ტელეფონის ნომერი

fetch("https://jsonplaceholder.typicode.com/users")

.then((response)=>response.json())
.then(date => {
    date.forEach(date => {
        console.log("სახელი:", date.name)
        console.log("ელფოსტა:", date.email)
        console.log("ტელეფონი:", date.phone)
    })
})