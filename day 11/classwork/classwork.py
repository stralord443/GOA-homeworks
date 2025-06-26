# 1)მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი 

num1=int(input("enter a number 1 "))
num2=int(input("enter a number 2 "))
num3=int(input("enter a number 3 "))

print(num1+num2+num3)

# 2)დაბეჭდეთ რიცხვები 10 - 1 მდე 

for I in range (10, 1, -1):
    print(I)


# 3)დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები

for I in range (1,101,2):
    print(I)

# 4)დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 1- 100

for I in range (1,101,3):
    print(I)

# 5)იპოვეთ 1 - 100 რიცხვის ჯამი 

c=1 
v=1
while c < 100:
    c+=1
    v=v+c

print(v)