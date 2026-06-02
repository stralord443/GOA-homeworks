// 5) შექმენი მშობელი კლასი Animal.
// დაამატე მეთოდი sound() რომელიც დააბრუნებს:
// "Animal sound"

// შემდეგ შექმენი შვილობილი კლასი Dog, რომელიც extends გამოიყენებს.

class Animal {
    sound() {
        return "Animal sound"
    }
}

class Dog extends Animal {

}

const dog1 = new Dog()

console.log(dog1.sound())