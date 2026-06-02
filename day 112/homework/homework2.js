// 3) შექმენი კლასი MathHelper, რომელსაც ექნება static მეთოდი sum(a, b).
// მეთოდმა უნდა დააბრუნოს ორი რიცხვის ჯამი.

// გამოიძახე კლასი ობიექტის შექმნის გარეშე.

class MathHelper {
    static sum(a, b) {
        return a + b
    }
}

console.log(MathHelper.sum(5, 7))