const user = {
    name: "Giorgi",
    age: 25
}

function greet() {
    return `Hello, my name is ${user.name} and I am ${user.age} years old.`
}

export { user, greet }