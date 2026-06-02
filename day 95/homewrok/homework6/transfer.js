import { deposit, withdraw } from "./transactions.js"

export function transfer(type, amount) {
    if (type === "deposit") {
        deposit(amount)
    } else if (type === "withdraw") {
        return withdraw(amount)
    } else {
        return "Invalid transaction type"
    }
}