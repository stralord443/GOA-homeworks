// 1) 1. შეამოწმე რიცხვი 100-ზე მეტია თუ არა.

let num = prompt("enter a number")

if (num<100){
    console.log("your number is less than 100")
}else if(num=100){
    console.log("your number is 100")
}else{
    console.log("your number is bigger than 100")
}

// 2. მომხმარებლის სახელისთვის: თუ "kocho" → "Welcome back", სხვა შემთხვევაში "Hello"  

let name = prompt("enter your name")

if(name == "kocho"){
    console.log("Welcome back")
}else{
    console.log("hello")
}

// 3. თუ ასაკი < 13 → "child", თუ 13–17 → "teen", სხვა შემთხვევაში "adult".

let age = prompt("enter your age")

if (age < 13){
    console.log("child")
}else if(age < 18){
    console.log("teen")
}else{
    console.log("adult")
}

// 4. შეამოწმე რიცხვი 0-ის ტოლია თუ არა.

let number = prompt("enter a number")

if(number == 0){
    console.log('your number is 0')
}else{
    console.log("your number isn't 0")
}

// 5. თუ პაროლი 8 სიმბოლოზე მეტია → "strong", ნაკლებია → "weak".

let password = prompt("enter a password")

if(password.length > 8){
    console.log("your password is strong")
}else{
    console.log("your password is weak")
}