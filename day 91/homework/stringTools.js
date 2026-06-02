export function reverse(text) {
    let result = ""
    for (let i = text.length - 1; i >= 0; i--) {
        result += text[i]
    }
    return result
}

export default function countLetters(text) {
    let count = 0
    for (let i = 0; i < text.length; i++) {
        count++
    }
    return count
}