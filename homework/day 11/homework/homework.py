# 1) შემოაყვანინეთ მომხმარებელს n რიცხვი და დაპრინტეთ ყველა რიცხვი ნოლიდან n+1-მდე

N=int(input("enter a number "))
I=1
while I<N:
    print(I)
    I+=1

# 2) მომხმარებელს სთხოვე შეიყვანოს თავისი ასაკი და მიუთითოს, აქვს თუ არა სტუდენტური ბარათი.
# შემდეგ:
# თუ ასაკი ნაკლებია 18-ზე ან სტუდენტური ბარათი აქვს → დაბეჭდე "დანაზოგი გაქვს!"
# თუ ასაკი 60 ან მეტია და არ აქვს ბარათი → დაბეჭდე "პენსიონერის ფასდაკლება გაქვს!"
# სხვა შემთხვევაში → "ფასდაკლება არ გეკუთვნის."

z=0
x=0


user_age=int(input("enter your age "))
user_card=input("do you have student card? ")

if user_age < 18 or user_card == "yes":
    print ("დანაზოგი გაქვს")
else:
    z=z+1

if user_age > 60 and user_card == "no":
    print ("პენსიონერის ფასდაკლება გაქვს ")
else:
    x=x+1

if z < 1 and x < 1:
    print ("ფასდაკლება არ გეკუთვნის")

y=0
# 3) მომხმარებელს სთხოვე შეიყვანოს ორი რიცხვი. შემდეგ:
# თუ ორივე რიცხვი დადებითია → დაბეჭდე "ორივე დადებითია"
# თუ მხოლოდ ერთი დადებითია → "მხოლოდ ერთი დადებითი რიცხვია"
# თუ არცერთი არ არის დადებითი → "არცერთი არ არის დადებითი"

num_1=int(input("enter number 1 "))
num_2=int(input("enter number 2 "))

if num_1 > -1 and num_2 > -1:
    print("ორივე დადებითია")
    y+=1

if (num_1 > -1 or num_2 > -1) and y < 1:
    print ("მხოლოდ ერთი დადებითი რიცხვია")
    y+=1

if (num_1 < 0 and num_2 < 0) and y < 2:
    print ("არცერთი არ არის დადებითი")

# 4) მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას (+, -, *, /)
# დაბეჭდე შედეგი შესაბამისი მოქმედებით.
# თუ ოპერაცია არასწორია (მაგ 0-ს გაყოფა ან ტექსტი ან უცხო სიმბოლო) → "არასწორი ოპერაცია!"

number1 = int(input("seiyvane ricxvi"))
number2 = int(input("seiyvane meore ricxvi"))
operacia = input("seiyvane sxva operaciebi rogoricaa: (+, -, , /)")

if operacia == "+":
    print(number1 + number2)
elif operacia == "-":
    print(number1 - number2)
elif operacia == "":
    print(number1 * number2)
elif operacia == "/":
    if number2  != 0:
        print(number1 / number2)
    else:
        print("araa swori")
else:
    print("araa zma swori")

# 5) შეამოწმეთ რესურსებში ჩაგდებული სურათი და მის მიხედვით დაწერეთ კომენტარებად ან პრეზენტაციაში მოქმედედების
#  თანმიმდევრობა და საბოლოო პასუხი, ასევე როგორც ნამდვილი პითონის კოდი (შექმენით a,b,c ცვლადები,
#  შექმენით result_0, result_1, result_2 ცვლადები და შეინახეთ თითოეულში შესაბამისი მნიშვნელობა და გამოპრინტეთ).

result_0=True
result_1=False
result_2=True

print (result_0)
print (result_1)
print (result_2)