# 1) შექმენი for loop- რომელიც გამოიტანს 1-100 ჩატვლით რიცხვებს და ასევე კენტია თუ ლუწი ეს რიცხვი.

for I in range (1, 101,1):
    if I % 2 == 1:
        print(I)
        print("odd")
    elif I % 2 == 0:
        print (I)
        print ("even")

# 2) მომხმარებელს შემოატანინეთ რიცხვი და და გამოიტანეთ ეს რიცხვი კენტია თუ ლუწი

num=int(input("enter a number "))

if num % 2 == 1:
        print("odd")
elif num % 2 == 0:
        print ("even")

# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ 'მეტია' თუ მეორე რიცხვი პირველზე მეტია თუ არადა დაბეჭდეთ  ''ნაკლებია"

number_1=int(input("enter a nnumber 1 "))
number_2=int(input("enter a nnumber 2 "))

if number_1 < number_2:
    print("ნაკლებია")
elif number_1 > number_2:
     print("მეტია")

# 4) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ უფრო მაღალი რიცხვი

num1=int(input("enter a nnumber 1 "))
num2=int(input("enter a nnumber 2 "))

if num1 < num2:
    print(num2)
elif num1 > num2:
     print(num1)