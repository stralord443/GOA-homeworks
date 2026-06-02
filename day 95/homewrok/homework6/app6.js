import { user } from "./user.js"
import { transfer } from "./transfer.js"
import { getAccountInfo } from "./accountInfo.js"

// საწყისი მდგომარეობა
console.log(getAccountInfo())

// დეპოზიტი
transfer("deposit", 50);
console.log("After deposit: " + getAccountInfo())

// განაღდება
transfer("withdraw", 30);
console.log("After withdraw: " + getAccountInfo())

// შეცდომის ტესტი
const result = transfer("withdraw", 1000)
    console.log(result)

// საბოლოო მდგომარეობა
console.log("Final: " + getAccountInfo())