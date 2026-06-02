// 4. URL: https://jsonplaceholder.typicode.com/posts
// გამოიტანე მხოლოდ პირველი 10 პოსტი.

fetch("https://jsonplaceholder.typicode.com/posts")

.then((response)=>response.json())
.then((date)=>{
    for(let i = 1; i <=10; i++){
        console.log(i)
        console.log(date)
    }
})
