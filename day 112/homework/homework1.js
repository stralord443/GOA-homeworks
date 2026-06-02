// 2) შექმენი კლასი Car, რომელსაც ექნება:
// - brand
// - model

// დაამატე მეთოდი info(), რომელიც დააბრუნებს ტექსტს:
// "This car is BMW M5"

class Car {
    constructor(brand, model) {
        this.brand = brand
        this.model = model
    }

    info() {
        return `This car is ${this.brand} ${this.model}`
    }
}

const car1 = new Car("BMW", "M5")

console.log(car1.info())