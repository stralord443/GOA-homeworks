import { user } from "./user.js"

export function getAccountInfo() {
    return `Name: ${user.name}, Balance: ${user.balance}`
}