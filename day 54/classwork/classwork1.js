// 2)დაწერე კოდი რომელიც იღებს ასო ქულას ("A", "B", "C", "D", "F")
// და დაბეჭდავს შეფასებას:

// "A" → "Excellent!"
// "B" → "Good"
// "C" → "Average"
// "D" → "Poor"
// "F" → "Fail"

// სხვა სიმბოლო → "Invalid grade"

let grade = prompt ('enter a grade')

switch (grade) {
    case "A":
        console.log("Excellent!")
        break;
    case "B":
        console.log("Good")
        break;
    case "C":
        console.log("Average")
        break;
    case "D":
        console.log("Poor")
        break;
    case "E":
        console.log("allmost fail")
        break;
    case "F":
        console.log("Fail")
        break;
    default:
        console.log("Invalid grade")
        break;
}