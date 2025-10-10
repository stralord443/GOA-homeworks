# 1) შექმენი dictionary, სადაც key = სტუდენტის სახელი, value = ქულა.
# შემდეგ loop-ით დაბეჭდე ყველა სტუდენტი და ქულა.

# dictionary (შეგიძლიათ გამოიყენოთ) :
scores = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}

for I in scores:
    P=f"{I} got {scores[I]}"
    print(P)

# 2) უკვე შექმნილ scores dictionary-ში დაამატე ახალი სტუდენტები update()-ით

scores.update({"nika":72})
print(scores)

# 3) ამ dictionary-ში:
countries = {
    "key": "Georgia",
    "fr": "France",
    "it": "Italy"
}

# შეცვალე key "kay" → "ge" pop()-ის გამოყენებით.

# დატოვე value უცვლელი.

print(countries)
countries.pop("key")
print(countries)
countries.update({"ge":"georgia"})
print(countries)

# 4) კომენტარების გამოყენებით ახსენი update() ფუნქცია.

# .update() changes value of creates it if theres no ket with chosen name

# 5) კომენტარების გამოყენებით ახსენით pop() ფუნქცია.

# .pop() eraces chosen key:value