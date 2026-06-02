// 1) შექმენი მასივი, მაგალითად let fruits = ["apple", "banana"]; და გაუკეთე push() ფუნქცია, 
// რომ დაამატო ახალი ელემენტი "kiwi" მასივში. შემდეგ გამოიტანე კონსოლში განახლებული მასივი.

let fruits = ["apple", "banana"]

fruits.push("kiwi")

// 2) შექმენი ნებისმიერი 5 ელემენტიანი მასივი. length თვისებით გამოიტანე ეკრანზე რამდენი ელემენტია მასივში.
//  შემდეგ push()-ით დაამატე ორი ელემენტი და თავიდან გამოიტანე length.

let brands = ["mercedes","audi","toyota","bmw","tesla"]

brands.push("wolfcwagen","ford")

// 3) შექმენი მასივი რიცხვებით და pop() ფუნქციით წაშალე ბოლო ელემენტი.
//  კონსოლში გამოიტანე რა წაიშალა და როგორ გამოიყურება მასივი ბოლოს.

let numbers = [1,2,3,4,5]

console.log(numbers)

numbers.pop()

console.log(numbers)

// 4) შექმენი პროგრამა, სადაც გექნება მარტივი შეყვანილი ტექსტი (prompt-ის მაგივრად შეგიძლია უბრალოდ ცვლადად ჩაწერო). 
// დაამატე ტექსტი მასივში push-ით და დაბეჭდე რამდენი ელემენტი გაქვს (length).

let words = ["apple","banana"]

words.push(prompt("enter a word"))

console.log(words.length)

// 5) შექმენი ობიექტი counter. ობიექტს ქონდეს მეთოდი სადაც უკვე შექმნილ count-s (key-ს) დაემატება 1.
//  ეს უნდა გამეორდეს 50 ჯერ. დაგჭირდება for loop.

let counter ={
    num : 1,
    muli : function(){
        for(let i =1;i<=50;i++){
            console.log(i)
        }
    }
}

// 6) შექმენი ობიექტი sum რომელიც გამოიტანს 1 დან 20 მდე რიცხვების ჯამს

const sum = {
  result: 0,

  calculate() {
    for (let i = 1; i <= 20; i++) {
      this.result += i;
    }
  },
  show() {
    console.log(this.result);
  }
};

sum.calculate();
sum.show();
