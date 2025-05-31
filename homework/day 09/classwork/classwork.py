# 1. მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.

start=int(input("enter a number "))
end=int(input("enter a number "))
step=int(input("enter a number "))

for I in range (start,end,step):
    print (I)

# 2. მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე, სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While Loop)
z=int(input("enter a number "))
x=1
while x < z:
    print(x)
    x+=1

# 2. გააკეთეთ {2.} classwork For loop-ის გამოყენებით

for I in range (1,z,1):
    print(I)