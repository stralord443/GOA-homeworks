// I) სინქრონულია
// თუ ასინქრონული?

// 1.
console.log("Hello");
console.log("World");  
// სინქრონულია
 
// 2.
console.log("Start");
setTimeout(() => {
console.log("Timeout");
}, 1000);
console.log("End");
// არ არის სინქრონული 

// 3.
function sayHi() {
console.log("Hi");
}
sayHi();
console.log("Bye");
// სინქრონულია

// 4.
console.log("A");
console.log("B");
function greet() {
    console.log("Hello");
}
greet();
console.log("C");
// სინქრონულია
 
// 5.
for(let i = 0; i < 3; i++) {
console.log(i);
}
// სინქრონულია

// 6.
console.log("A");
setTimeout(() => {
console.log("B");
}, 0);
console.log("C");
// სინქრონულია
 
// 7.
function greet() {
    console.log("Hello");
}

console.log("A");
console.log("B");
greet();
console.log("C");
// არ არის სინქრონული
 
// 8.
alert("Hello");
console.log("Done");
// სინქრონულია
 
// 9.
console.log("1");
Promise.resolve().then(() => {
console.log("2");
});
console.log("3");
// არ არის სინქრონული

// 10.
const nums = [1, 2, 3];
nums.forEach(num => {
console.log(num);
});
// სინქრონულია