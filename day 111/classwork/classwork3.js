// 4) შექმენი Promise, სადაც password = "12345".
// 1 წამში:
// თუ პაროლი ტოლია "admin123" → resolve "Welcome admin".
// თუ არა → reject "Wrong password".

let password = "12345";

const passwordPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (password === "admin123") {
            resolve("Welcome admin")
        } else {
            reject("Wrong password")
        }
    }, 1000)
})

passwordPromise
    .then((message) => {
        console.log(message)
    })
    .catch((error) => {
        console.log(error)
    })