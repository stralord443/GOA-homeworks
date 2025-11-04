// 1) ახსენი რას აკეთებს alert

// alert is used to show something to user

// 2) ახსენი რას აკეთებს prompt

// prompt is used to ask user for some info

// 3) ახსენი რა განსხვავებაა alert-სა და prompt-ს შორის

// alert gives info and promps asks for info

// 4) გამოიტანეთ alert-ით "hello world" მესიჯი

alert("hello world")

// 5) მომხმარებელს შემოატანინე 2 რიცხვი და მოახდინე ყველა მათემატიკური ოპერაცია

let num1 = prompt("enter a number")
let num2 = prompt("enter a second number")

console.log(num1+num2)
console.log(num1-num2)
console.log(num1/num2)
console.log(num1*num2)
console.log(num1%num2)
console.log(num1>num2)
console.log(num1<num2)
console.log(num1=num2)
console.log(num1==num2)
console.log(num1===num2)

// 6) მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ სრულწლოვანია თუ არა  (გამოიტანეთ alert-ით) 

let age = promt("enter your age")

if (age < 18){
    alert("არასრულწლოვანი ხარ")
}else {
    alert("სრულწლოვანი ხარ ")
}
// 7)  შექმენი 2 ცვლადი, სადაც მომხმარებელს შემოატანინებ რიცხვებს. შეამოწმე რომელი რიცხვია დადებითი
//  და რომელი უარყოფითი (გამოიტანეთ console.log()-ით) 

let number1 = prompt("enter a positive or negative number")
let number2 = prompt("enter a different number")

if (number1 > 0){
    console.log("first number is positiv")
}else if (number1 < 0){
    console.log("first number is negative")
}else{
    console.log("first number is a 0")
}
if (number2 > 0){
    console.log("second number is positiv")
}else if (number2 < 0){
    console.log("second number is negative")
}else{
    console.log("second number is a 0")
}

// 8) შექმენი 3 ცვლადი, ერთი იყოს რო მომხმარებელს უნდა შემოატანინო მათემატიკური სიმბოლო (+, -, *, /, %), 
// დანარჩენი ორი ცვლადი უნდა იყოს რიცხვები. სიმბოლოს მიხედვით შეასრულე ამ ორ ცვლადში სადაც რიცხვები, არის
// შესრულდეს მოქმედება. (შედეგი გამოიტანეთ console.log-ით)

let operation = prompt('enter a matemathical operation')
let numb1 = prompt('enter fist number')
let numb2 = prompt('enter second number')

if (operation =="+"){
    let num3 = numb1 + numb2
}else if (operation == "-"){
    let num3 = numb1 - numb2
}if (operation == "*"){
    let num3 = numb1 * numb2
}if (operation == "/"){
    let num3 = numb1 / numb2
}if (operation == "%"){
    let num3 = numb1 % numb2
}

console.log(num3)