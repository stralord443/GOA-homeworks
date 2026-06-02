import { findIndex } from './app1.js'

const numbers = [10, 20, 30, 40, 50]

const result1 = findIndex(numbers, 30)
console.log(result1)

const result2 = findIndex(numbers, 99)
console.log(result2)