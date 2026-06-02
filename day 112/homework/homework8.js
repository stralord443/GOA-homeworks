// 10) შექმენი კლასი Phone, რომელსაც ექნება:
// - private field #password

// და setter, რომელიც შეცვლის პაროლს მხოლოდ მაშინ, თუ სიგრძე 4-ზე მეტია.

class Phone {
    #password = ""

    set password(value) {
        if (value.length > 4) {
            this.#password = value
        } else {
            console.log("Password is too short")
        }
    }

    get password() {
        return this.#password
    }
}

const phone = new Phone()

phone.password = "123"
phone.password = "12345"

console.log(phone.password)