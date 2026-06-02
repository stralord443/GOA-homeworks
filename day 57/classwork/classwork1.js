// 3) სამი რიცხვიდან გამოიტანე ყველაზე დიდი.

let a = 10;
let b = 25;
let c = 7;

let max;

if (a >= b && a >= c) {
    max = a;
} else if (b >= a && b >= c) {
    max = b;
} else {
    max = c;
}

console.log("ყველაზე დიდი რიცხვია:"+ max);

// 4) სია: 5 + 7, 10 - 4, 3 * 3, 20 / 2 – ყველა console.log-ით.

console.log(5 + 7)
console.log(10 - 4)
console.log(3 * 3)
console.log(20 / 2)

// 5) შეადარე ორი რიცხვი: >, <, ===, !==.

console.log(10>12)
console.log(9<12)
console.log("5"!==5)
console.log("5"===5)
