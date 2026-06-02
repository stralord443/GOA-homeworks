// 3) შექმენი Promise, სადაც fileSize = 8.
// 2 წამში:
// თუ fileSize <= 10 → resolve "File uploaded".
// თუ არა → reject "File is too large".

const fileSize = 8

const uploadPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (fileSize <= 10) {
            resolve("File uploaded")
        } else {
        reject("File is too large")
        }
    }, 2000)
})

uploadPromise
    .then(result => console.log(result))
    .catch(error => console.log(error))