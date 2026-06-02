// 8) BankAccount კლასში დაამატე setter:
// set balance(value)

// თუ value უარყოფითია, კონსოლში გამოიტანოს:
// "Invalid balance"

// 9) BankAccount კლასში დაამატე getter:
// get balance()

// getter-მა დააბრუნოს private field-ის მნიშვნელობა 

class BankAccount {
    #balance = 0

    set balance(value) {
        if (value < 0) {
            console.log("Invalid balance")
        } else {
            this.#balance = value
        }
    }

    get balance() {
        return this.#balance
    }
}

const account = new BankAccount()

account.balance = 10
console.log(account.balance)

account.balance = -1

