// II) კონსოლის შედეგის მიხედვით დაწერე შესაბამისი კოდი

// 1.
// კონსოლში უნდა გამოვიდეს:
// Hello
// World
// დაწერე მარტივი სინქრონული კოდი.

console.log("hello")
console.log("world")


// 2.
// კონსოლში უნდა გამოვიდეს:
// Start
// End
// Timeout
// გამოიყენე setTimeout.

setTimeout(()=>{
    console.log("Timeout")
},2000)
setTimeout(()=>{
    console.log("end")
},1000)
console.log("start")

// 3.
// კონსოლში უნდა გამოვიდეს:
// 1
// 2
// 3
// გამოიყენე for ციკლი.
for(let i = 1; i < 4;i++){
    console.log(i)
}

// 4.
// კონსოლში უნდა გამოვიდეს:
// Loading...
// Data received
// მეორე ტექსტი გამოვიდეს 2 წამის შემდეგ.
console.log("loading...")
setTimeout(()=>{
    console.log("data received")
},2000)

// 5.
// კონსოლში უნდა გამოვიდეს:
// A
// C
// B
// გამოიყენე setTimeout.

console.log("A")
setTimeout(()=>{
    console.log("b")
},1000)
console.log("C")