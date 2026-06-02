export function findIndex(arr, target) {
    let i = 0

    while (i < arr.length) {
        if (arr[i] === target) {
            return i
        } else {
            i++
        }
    }
    return "ვერ მოიძებნა"
}