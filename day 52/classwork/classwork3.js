// 4) შექმენი 3 ცვლადი, ერთი იყოს რო მომხმარებელს უნდა შემოატანინო მათემატიკური
// სიმბოლო (+, -, *, /, %), დანარჩენი ორი ცვლადი უნდა იყოს რიცხვები. სიმბოლოს
// მიხედვით შეასრულე ამ ორ ცვლადში სადაც რიცხვები, არის შესრულდეს მოქმედება. (შედეგი გამოიტანეთ console.log-ით)

let operation = prompt('enter a matemathical operation')
let num1 = prompt('enter fist number')
let num2 = prompt('enter second number')

if (operation =="+"){
    let num3 = num1 + num2
}else if (operation == "-"){
    let num3 = num1 - num2
}if (operation == "*"){
    let num3 = num1 * num2
}if (operation == "/"){
    let num3 = num1 / num2
}if (operation == "%"){
    let num3 = num1 % num2
}

console.log(num3)

// 5) ახსენი რა განსხვავებაა ორტოლობასა და სამტოლობას შორის

// ორი ტოლობა ადარებს ინფორმაციას და სამი ტოლობა ადარებს დათა თაიპს