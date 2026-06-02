export function removeNumbers(text) {
    let result = ""

    for (let i = 0; i < text.length; i++) {
        if (text[i] >= '0' && text[i] <= '9') {
            continue
        } else {
            result += text[i]
        }
    }

    return result
}