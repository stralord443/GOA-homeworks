// import { add } from './math.js'

// export function log(msg) {
//   console.log(msg)
// }

// export function logSum(a, b) {
//   log(add(a, b))
// }

// logger.js needs imformation from math.js and math.js needs information from logger.js
// this is circular dependency


// correct code

import { add } from './math.js'
import { log } from './utils.js'

export function logSum(a, b) {
    log(add(a, b))
}