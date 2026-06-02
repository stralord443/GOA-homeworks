// 1) შექმენი კლასი User, რომელსაც ექნება:
// - name
// - age

// შექმენი ობიექტი და გამოიტანე ორივე მნიშვნელობა კონსოლში.


class User {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}

const user1 = new User("Gio", 20)

console.log(user1.name)
console.log(user1.age)