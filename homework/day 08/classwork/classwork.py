# 1. მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.

start=int(input("start "))
end=int(input("end "))
step=int(input("step "))

for I in range (start, end, step):
    print(I)

# 2. მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე,
# სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While Loop)

num_1=int(input("enter a number "))
i = 0
while i != num_1:
    print (i)
    i += 1

# 3. გააკეთეთ {2.} classwork For loop-ის გამოყენებით


num_2=int(input("enter a number "))
for i in range (1, num_2, 1 ):
    print (i)