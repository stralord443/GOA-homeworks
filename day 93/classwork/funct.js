export function findMin(arr) {
    if (arr.length === 0) return null

    let min = arr[0]
    for (let num of arr) {
        if (num < min) {
            min = num
        }
    }
    return min
}

export function findMax(arr) {
    if (arr.length === 0) return null
    
    let max = arr[0]
    for (let num of arr) {
        if (num > max) {
            max = num
        }
    }
    return max
}

