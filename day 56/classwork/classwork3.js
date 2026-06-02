// 4) შექმენი რეგულარ ფუნქცია რომელსაც გადაეცემა ასაკი და შენი ფუნქცია განსაზღვრავს მომხმარეელი სრულწლოვანია თუ არა

function adult(age){
    if (age >= 18){
        return "you are adult"
    }else{
        return "you are child"
    }
}

console.log(adult(17))
console.log(adult(18))
console.log(adult(19))