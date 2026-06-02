// 1) შექმენი Promise, სადაც serverStatus = 500.
// 2 წამში:
// თუ serverStatus === 200 → resolve "Server works correctly".
// თუ არა → reject "Server error".

const serverStatus = 500

const serverPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (serverStatus === 200) {
            resolve("Server works correctly")
        } else {
            reject("Server error")
        }
    }, 2000)
})

serverPromise
    .then(result => console.log(result))
    .catch(error => console.log(error))