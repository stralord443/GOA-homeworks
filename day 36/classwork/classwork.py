# 1) კომენტარების სახით ახსენით რა არის Dictionary

# dictionary is user to save information in key:value pairs

# 2) შექმენი Dictionary, სადაც შენახული იქნება შენს შესახებ ინფორმაცია (სახელი, ასაკი, გვარი)

X={
    "name":"goga",
    "surname":"adamashvili",
    "age":18
}
print(X)

# 3) უკვე შექმნილი Dictionary-დან წამოიღეთ მხოლოდ key-ები და ასევე value

print(X.get("name"))
print(X.get("surname"))
print(X.get("age"))

print(X.keys())

# 4) უკვე შექმნილ Dictionary-ში დაამატეთ ელემენტი (თქვენი საყვარელი ფერი)

X.update({"color":"blue"})
print(X)

# 5) უკვე შექმნილ Dictionary-დან, შეცვალე key ისე, რომ value იგივე დარჩეს და დაბეჭდე Dictionary საბოლოო სახით (გააკეთეთ pop-ით)

X.update({"fav_color":"blue"})
X.pop("color")
print(X)