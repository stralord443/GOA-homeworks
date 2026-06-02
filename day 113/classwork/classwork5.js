// 6. URL: https://jsonplaceholder.typicode.com/photos
// გამოიტანე პირველი 20 ფოტო img თეგების გამოყენებით.

fetch("https://jsonplaceholder.typicode.com/photos")

.then((response)=>response.json())
.then((date)=>{
    for(let i = 0; i <=19; i++){
        console.log(i)
        console.log(date[i].thumbnailUrl)
    }
})
