# 6) dictionary ფასებით:

products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

# დაბეჭდე ყველა პროდუქტი for loop-ით.
# მომხმარებლისგან შეიყვანე პროდუქტი, თუ არსებობს → დაბეჭდე ფასი.
# დაამატე ახალი პროდუქტი update()-ით.
# ბოლოს გამოიყენე clear() ჩასაშენებლად, მაგალითად, ცარიელი dictionary-ს დაბეჭდვა დასუფთავების შემდეგ.

for I in products:
    print(I)
X=input("chose one of the products: ")
if X == "apple":
    print("it's cost is 3$")
if X == "banana":
    print("it's cost is 2$")
if X == "milk":
    print("it's cost is 5$")

products.update({"orange":4})
print(products)
products.clear()
print(products)

# 7) კომენტარების გამოყენებით ახსენით clear() ფუნქცია.

# .clear() clears whole dictionary 