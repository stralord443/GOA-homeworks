// 4) შექმენი Promise, სადაც weather = "rainy".
// 1 წამში:
// თუ weather === "sunny"→ resolve"Go outside". თუ არა → reject "Stay at home"`.

const weather = "rainy"

const weatherPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (weather === "sunny") {
            resolve("Go outside")
        } else {
            reject("Stay at home")
        }
    }, 1000)
})

weatherPromise
    .then(result => console.log(result))
    .catch(error => console.log(error))