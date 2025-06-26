# 1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.

U=1
while U >=1 and U <= 10 :
    print(U)
    U=U+1
    
    
# 2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე

I=10
while I >=1 and I <= 10 :
    print(I)
    I=I-1

# 3)კომენტარებით ახსენი while loop.
# while loop is an operatino in which we choose what will come out if statement is true (it will loop itself)

# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას.
#  სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან

password=("python123")

user_password=input("enter password ")

while user_password != "python123":
    user_password=input("enter right password ")

# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი

n=int(input("enter your number "))
p=1
x=0
while p <= n:
    x += p
    p += 1
print(x)