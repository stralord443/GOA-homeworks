// 1) შექმენი ობიექტი, რომელსაც ექნება:
// name
// age
// city
// და Console-ში დაიპრინტე.

const object ={
    name: "goga",
    age: 18,
    city: "Tbilisi"
}

console.log(object.name)
console.log(object['age'])
console.log(object.city)

// 2) შექმენი ობიექტი car, რომელსაც ექნება:
// brand
// model
// year
// და Console-ში დაბეჭდე მხოლოდ brand და year.(გამოიტანეთ ორივე გზით)

const car = {
    brand: "BMW",
    model: "E59",
    year: 2003,
}

console.log(car.brand)
console.log(car["year"])

// 3) შექმენი ობიექტი user, რომელსაც ექნება:
// name
// დაამატეთ მეთოდი  sayHello() → რომელიც დაბეჭდავს "Hello"

const user = {
    name: "goga",
    sayHello: function() {
        console.log("hello "+ this.name)
    }
}
user.sayHello()

// 4) შექმენით კალკულატორი obj-თი (დაგჭირდებათ მეთოდები)
// უნდა ქონდეს მიმატების, გამოკლების, გაყოფის და გამრავლების მეთოდები

const calculator = {
  add(a, b) {
    return a + b;
  },
  subtract(a, b) {
    return a - b;
  },
  multiply(a, b) {
    return a * b;
  },
  divide(a, b) {
    if (b === 0) {
      return "NO Division by zero!";
    }
    return a / b;
  }
};

console.log(calculator.add(5, 3));       // 8
console.log(calculator.subtract(10, 4)); // 6
console.log(calculator.multiply(6, 7));  // 42
console.log(calculator.divide(20, 4));   // 5
console.log(calculator.divide(10, 0));   // NO Division by zero!

// 5) შექმენი ობიექტი რომელსაც ექნება მეთოდი, ობიექტს ექნება სახელი და ასაკი, ამ მეთოდმა უნდა გააკეთოს "ჩემი სახელია [სახელი] და ვარ [ასაკი]"

const person = {
  name: "goga",
  age: 25,
  introduce() {
    console.log(`ჩემი სახელია ${this.name} და ვარ ${this.age}`);
  }
};

person.introduce(); 