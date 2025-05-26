# 1) შექმენით უსასრულო while loop

while True:
    print("you are right")

# 2) გამოიტანეთ მომხმარებლის შემოყვანილი სახელი 10-ჯერ იტერაციის მეშვეობით

user_name=input("enter your name ")
i=1

while i<=10:
    i=i+1
    print(user_name)

# 3) შექმენით while loop და კომენტარად მიაწერეთ რომელია თავი და რომელი სხეული

U=10

#    head
while U==10:

#     body
    print("A")

# 4) მომხმარებელს შემოაყვანინეთ რიცხვი, სანამ ეს რიცხვი არ იქნება 100-ზე მეტი მაქამდე თავიდან მოთხოვთ რიცხვის შემოტანა

user_num=int(input("enter your number "))

while user_num <100:
    user_num=int(input("enter new number "))

# 5) მომხმარებელს შემოატანინეთ სხვადასხვა სახელები 5-ჯერ იტერაციის მეშვეობით, შექმენით ამ სახელებისთვის ცვლადი
#  რომელშიც ყოველი სახელი დაემატება და ეს სახელები გამოიყოფა მძიმეებით, ანუ თქვენი ცვლადი 5 სახელის შეყვანის
#  შემდეგ უნდა გამოიყურებოდეს ასე: "{სახელი პირველი}, {სახელი მეორე}, ... {სახელი მეხუთე}" 

O=1
user_name_1=input("enter your name ")

while O<5:
    user_name_1=user_name_1+(", ")+ input("enter your name ")
    O=O+1

print(user_name_1)