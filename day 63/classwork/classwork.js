// 1) შექმენი ობიექტი user, რომელსაც აქვს:
// name (სტრინგი)
// age (ნამბერი)
// isAdult (მეთოდი), რომელიც აბრუნებს ტექსტს:
// თუ age >= 18 → "You are an adult"
// თუ არა → "You are not an adult"

const user ={
    name:"goga",
    age:21,
    isadult: function(){
        if (this.age >= 18){
            console.log("You are an adult")
        } else{
            console.log("You are not an adult")
        }
    }
}

// 2) შექმენი ობიექტი car, რომელსაც აქვს:
// brand (სტრინგი)
// speed (ნამბერი)
// checkSpeed (მეთოდი), რომელიც აკონტროლებს:
// თუ speed > 120 → "Too fast!"
// თუ არა → "Speed is okay"

constcar = {
    brand:"BMW",
    speed:120,

    checkSpeed: function(){
        if (this.speed >120){
            console.log("Too fast!")
        } else{
            console.log("Speed is okay")
        }
    }
}

// 3) შექმენი ობიექტი student, რომელსაც აქვს:
// name (სტრინგი)
// score (ნამბერი)
// passOrFail (მეთოდი), რომელიც აბრუნებს:
// თუ score >= 50 → "Passed"
// თუ არა → "Failed"

const student = {
    name:"nika",
    score:82,

    passOrFail: function(){
        if(this.score >= 50){
            console.log("Pass")
        } else {
            console.log("Failed")
        }
    }
}

// 4) შექმენი ობიექტი calculator, რომელსაც აქვს:
// n (ნამბერი)
// sumToN მეთოდი, რომელიც while loop-ით ითვლის 1+2+...+n

let i = 1
let count = 0

const calculator = {
    n:4,

    sumTon: function(){
        while(i<= this.n){
            count+=i
            i++
        }
        console.log(count)
    }
}


// 5) შექმენი ობიექტი multiplier:
// number (ნამბერი)
// times (რამდენჯერ გავამრავლოთ)
// multiply მეთოდი, რომელიც while loop-ით აყვანს რიცხვს ნამრავლზე

let x = 1
let muly = 0

const multiplire ={
    number: 2,
    times:3,

    multiply: function(){
        muly = this.number
        while(x< this.times){
            this.number = this.number * muly
            x++
        }
    }
}

