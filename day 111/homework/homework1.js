// 2) შექმენი Promise, სადაც isSubscribed = false.
// 1 წამში:
// თუ true → resolve "Premium access granted".
// თუ false → reject "You need subscription".

const isSubscribed = false

const subscriptionPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (isSubscribed) {
            resolve("Premium access granted")
        } else {
        reject("You need subscription")
        }
    }, 1000)
})

subscriptionPromise
    .then(result => console.log(result))
    .catch(error => console.log(error))