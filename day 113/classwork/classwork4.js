// 5. URL: https://jsonplaceholder.typicode.com/comments
// დათვალე რამდენი კომენტარია სულ.

fetch("https://jsonplaceholder.typicode.com/comments")
.then(response => response.json())
.then(date => {
    console.log("სულ კომენტარების რაოდენობა:", date.length)
})