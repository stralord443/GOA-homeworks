// 6) შექმენი კლასი Person.
// შემდეგ შექმენი კლასი Student, რომელიც მემკვიდრეობით მიიღებს Person კლასს.

// Student კლასს დაამატე:
// - grade

// და მეთოდი showInfo().

class Person {
    constructor(name) {
        this.name = name
    }
}

class Student extends Person {
    constructor(name, grade) {
        super(name)
        this.grade = grade
    }

    showInfo() {
        return `${this.name} has a grade: ${this.grade}`
    }
}

const student1 = new Student("Nika", 10)

console.log(student1.showInfo())