// 5) შექმენი Promise, სადაც coins = 250.
// 2 წამში:
// თუ coins >= 200 → resolve "You can buy the item".
// თუ არა → reject "Not enough coins".

const coins = 250

const coinsPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (coins >= 200) {
            resolve("You can buy the item")
        } else {
            reject("Not enough coins")
        }
    }, 2000)
})

coinsPromise
    .then(result => console.log(result))
    .catch(error => console.log(error))