// 3) შექმენი Promise, სადაც balance = 120.
// 2 წამში:
// თუ balance >= 100 → resolve "Payment completed".
// თუ არა → reject "Not enough money".
// გამოიყენე სამივე: .then(), .catch(), .finally().

let balance = 120;

const paymentPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (balance >= 100) {
            resolve("Payment completed")
        } else {
        reject("Not enough money")
        }
    }, 2000)
})

paymentPromise
    .then((message) => {
        console.log(message)
    })
    .catch((error) => {
        console.log(error)
    })
    .finally(() => {
        console.log("Process finished")
    })