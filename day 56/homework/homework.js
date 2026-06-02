// 1) კომენტარების სახით ახსენით რა არის ფუნქცია და რისთვის გამოიყენება.

// we use functions to make it easyer to white long codes

// 2) კომენტარების სახით ახსენით რა განსხვავებაა პითონის ფუნქციასა და ჯავასკრიპტის ფუნქციას შორის?

// there is no difference between them exept of sintax

// 3) შექმენით ჯავასკრიპტის ფუნქცია რომელიც გადაეცემა name, და შენი პროგრამა ესალმება ამ name-ს

function greet(name){
    console.log("Hello, " + name + "!")
}

greet('goga') //Hello, goga!

// 4) შექმენით ფუნქცია რომელიც გადაეცემა 4 რიცხვი და შენი პროგრამა დააბრუნებს ამ რიცხვების ჯამს

function sum(num1,num2,num3,num4){
    console.log(num1+num2+num3+num4)
}

sum(5,7,12,15) //39

// 5) ახსენი რა განსხვავებაა ჩვეულებრივ ფუნქციასა და arrow function-ს შორის.

// in normal functions we use this sintax


// function functions_name (elements_that_is_goind_to_be_used){
//     and what is going to be done tith them
// }

// and in arrow functions we use this sintax

// const functions_name= (creating_its_elements) => doing_operations_with_them ? after ? do_one_thing : after : do_different_thing;

// 6) შექმენი arrow function რომელსაც გადეცემა რიცხვი და გაიგებ ეს რიცხვი ლუწია თუ კენტი

const isEven = (num) => num % 2 === 0 ? "Even" : "Odd";

console.log(isEven(5)) //odd

// 7) შექმენი  arrow function სახელად countLetters, რომელსაც გადაეცემა სტრინგი და დააბრუნებს რამდენი ასოა სტრიქონში.

const CountLetters = (string) => console.log(string.length)

CountLetters('this is a test') //14