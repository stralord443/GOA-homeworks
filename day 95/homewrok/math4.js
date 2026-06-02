function sumArray(arr) {
    return arr.reduce((sum, num) => sum + num, 0)
}
function findMax(arr) {
    return Math.max(...arr)
}
export const arrayUtils = {
    sumArray,
    findMax
}