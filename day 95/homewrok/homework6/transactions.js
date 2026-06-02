import { user } from "./user.js"

export function deposit(amount) {
    user.balance += amount
}

export function withdraw(amount) {
    if (amount > user.balance) {
        return "Insufficient funds"
    }
    user.balance -= amount
}