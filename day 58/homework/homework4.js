// 21. switch-ით შეამოწმე "sunny", "rainy", "cloudy" — და დაბეჭდე ამინდი.

let weather = prompt("enter a weather: sunny, rainy, cloudy")

switch (weather){
    case "sunny":
        console.log("the weather is sunny")
        break;
    case "rainy":
        console.log("the weather is rainy")
        break;
    case "cloudy":
        console.log("the weather is cloudy")
        break;
    default:
        console.log("unknown weather")
}

// 22. რიცხვი 1–4 → season: spring, summer, autumn, winter.

let season = prompt("eter a season as a number (1-4)")

switch(season){
    case 1:
        console.log("spring")
        break;
    case 2:
        console.log("summer")
        break;
    case 3:
        console.log("autum")
        break;
    case 4:
        console.log("winter")
        break;
    default:
        console.log("unknown season")
}


// 23. switch-ით შეამოწმე transport type: "car", "bus", "bike".

const transport = prompt("enter a transport")

switch (transport) {
  case "car":
    console.log("You chose a car.")
    break;
  case "bus":
    console.log("You chose a bus.")
    break;
  case "bike":
    console.log("You chose a bike.")
    break;
  default:
    console.log("Unknown transport type.")
}

const month = prompt("enter a month in number (1-12)")

switch (month) {
  case 12:
  case 1:
  case 2:
    console.log("winter")
    break;
  case 3:
  case 4:
  case 5:
    console.log("spring")
    break;
  case 6:
  case 7:
  case 8:
    console.log("summer")
    break;
  case 9:
  case 10:
  case 11:
    console.log("autumn")
    break;
  default:
    console.log("invalid month number")
}

// 25. switch-ით შეამოწმე score (A/B/C/D/F) და გამოიტანე შეფასება.

const score = prompt("enter a grade (A-F)")

switch (score) {
  case "A":
    console.log("Excellent")
    break;
  case "B":
    console.log("Good")
    break;
  case "C":
    console.log("Average")
    break;
  case "D":
    console.log("Poor")
    break;
  case "F":
    console.log("Fail")
    break;
  default:
    console.log("Invalid score")
}
