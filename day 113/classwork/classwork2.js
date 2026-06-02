// 3. URL: https://jsonplaceholder.typicode.com/posts
// გამოიტანე ყველა პოსტის სათაური.

fetch ("https://jsonplaceholder.typicode.com/posts")

.then((response)=>response.json())
.then(date => {
    date.forEach(date => {
        console.log("სათაური:", date.title)
    })
})