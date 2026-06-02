// 5) შექმენი Promise, სადაც temperature = 35.
// 2 წამში:
// თუ temperature > 30 → resolve "Hot weather".
// თუ არა → reject "Cold weather".

let temperature = 35;

const weatherPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (temperature > 30) {
            resolve("Hot weather")
        } else {
            reject("Cold weather")
        }
    }, 2000)
})

weatherPromise
    .then((message) => {
        console.log(message)
    })
    .catch((error) => {
        console.log(error)
    })