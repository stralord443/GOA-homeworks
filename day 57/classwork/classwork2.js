// 6) ცვლადის გაზრდა: შექმენი num = 0 და num++ 3-ჯერ.

let num = 0;

num++;  // 1
num++;  // 2
num++;  // 3

console.log(num); // გამოიტანს 3

// 7) დაბეჭდე 1–დან 20-მდე ყველა რიცხვი.

for (let i = 1; i < 20; i++){
    console.log(i)
}

// 8) დაბეჭდე 1–30-მდე მხოლოდ ლუწები.

for (let ib = 1; i <= 30; ib++) {
    if (ib % 2 === 0) {
        console.log(ib);
    }
}

// 9) იპოვე ჯამი 1–50-მდე რიცხვების.

let r = 0;

for (let r = 1; i <= 50; r++) {
    sum += r;
}

console.log(sum);

// 10) while-ით დაბეჭდე 1–დან 5-მდე რიცხვები.

let ia = 1;

while (ia <= 5) {
    console.log(i);
    ia++;
}


// 11) შექმენი counter = 0 და ზრდე სანამ < 10 იქნება.

let counter = 0;

while (counter < 10) {
    console.log(counter);
    counter++;
}

// 12) while-ით დათვალე ჯამი 1–დან 20-მდე.

let i = 1;
let sum = 0;

while (i <= 20) {
    sum += i;
    i++;
}

console.log("ჯამი:" + sum);

// 13) მიანიჭე ცვლადს "apple" და switch-ით დაწერე:
// "apple" → "fruit"
// "carrot" → "vegetable"
// default → "unknown"

let item = "apple";
let category;

switch (item) {
    case "apple":
        category = "fruit";
        break;
    case "carrot":
        category = "vegetable";
        break;
    default:
        category = "unknown";
}

console.log(category); 