// 7. URL: https://jsonplaceholder.typicode.com/albums
// გამოიტანე ყველა ალბომის სათაური.

fetch("https://jsonplaceholder.typicode.com/albums")

.then((response)=>response.json())
.then(date => {
    date.forEach(date => {
        console.log("სათაური:", date.title)
    })
})