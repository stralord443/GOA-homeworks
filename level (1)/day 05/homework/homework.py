# 1)შემოატანინეთ მომხმარებელს რიცხვი  და თუ 10 ზე მეტი იქნება  გამოიტანინოს ("you are right ")

user_number=int(input())

if user_number > 10:
    print("you are right ")

# 2)მომხმარებელს შემოატანინეთ ორი რიცხვი გააკეთეთ მათზე მათემატიკური ოპერაციები  ("+, -, *, /, %, <, >, <=, >=, ==, !=. **) 

user_input_1=int(input())
user_input_2=int(input())

user_input_1+user_input_2
user_input_1-user_input_2
user_input_1*user_input_2
user_input_1/user_input_2
user_input_1%user_input_2
user_input_1<user_input_2
user_input_1>user_input_2
user_input_1<=user_input_2
user_input_1>=user_input_2
user_input_1==user_input_2
user_input_1!=user_input_2
user_input_1**user_input_2

# 3)ახსენით დღეს ნასწავლი If კომენტარებით 

#if ფუნქცია საშვალებას გვაძლევს ჩვენს მიერ არჩეული ინფორმციის ნაწილის მიხედვით გავაკეთოთ ოპერაციები.
#მაგალითად: არჩეული რიცხვი S ცვლადის ფორმით თუ აღემატება 10-ს დავპრინტოს you are right 
