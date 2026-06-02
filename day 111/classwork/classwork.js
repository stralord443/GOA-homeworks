// 1) შექმენი Promise, რომელიც 2 წამში დააბრუნებს ტექსტს "Login successful".
// თუ isLoggedIn = true არის → resolve.
// თუ false → reject "Login failed".
// გამოიყენე .then(), .catch() და .finally().

let isLoggedIn = true;

const loginPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (isLoggedIn) {
            resolve("Login successful")
        } else {
            reject("Login failed")
        }
    }, 2000)
})

loginPromise
    .then((message) => {
        console.log(message)
    })
    .catch((error) => {
        console.log(error)
    })
    .finally(() => {
        console.log("Request finished")
  })