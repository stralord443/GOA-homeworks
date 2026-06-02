// 16. while-ით დაბეჭდე 2–დან 20-მდე ლუწი რიცხვები.

let i = 1

while (i<20){
    if(i % 2 === 0){
        console.log(i)
    }
    i++
}

// 17. შექმენი counter = 5 და ამატე სანამ 20-ს არ მიაღწევს.

let counter = 5

while(counter < 20){
    if (counter = 20){
        console.log(counter)
    }
    counter++
}

// 18. while-ით დათვალე ჯამი მხოლოდ კენტ რიცხვებზე 1–30-მდე.

let num = 1
let sum = 0

while(num < 30){
    if(num % 2 === 1){
        sum=num+sum
    }
    num++
}
console.log(sum)

// 19. while ციკლით მოძებნე პირველი რიცხვი, რომელიც იყოფა 9-ზე.

let L = 1


while(L < 100){
    if(L % 9 === 0){
        console.log(L)
        break
    }
    L++
}

// 20. while-ით ჩათვალე რამდენჯერ მოდის 3-ის ჯერადი 1–დან 40-მდე.

let david = 1
let result = 0

while(david < 40){
    if(david % 3 === 0){
        result++
    }
    david++
}
console.log(result)