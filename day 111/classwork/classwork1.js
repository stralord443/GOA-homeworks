// 2) შექმენი Promise, სადაც age = 18.
// setTimeout-ით 1 წამში:
// თუ ასაკი >= 18 → resolve "Access granted".
// სხვა შემთხვევაში → reject "Access denied".
// ბოლოში .finally()-ში გამოიტანე "Check finished".

let age = 18;

const agePromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (age >= 18) {
            resolve("Access granted")
        } else {
            reject("Access denied")
        }
    }, 1000)
})

agePromise
    .then((message) => {
        console.log(message)
    })
    .catch((error) => {
        console.log(error)
    })
    .finally(() => {
        console.log("Check finished")
    })