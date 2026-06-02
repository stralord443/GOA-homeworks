function capitalize(str) {
    return str[0].toUpperCase() + str.slice(1)
}
function reverse(str) {
    return str.split("").reverse().join("")
}
export const stringUtils = {
    capitalize,
    reverse
}