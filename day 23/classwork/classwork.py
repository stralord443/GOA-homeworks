# 1) მომხმარებელს შემოატანეთ ინფუთი სანამ პირველი და ბოლო ასო ინფუთის არ იქნება ხმოვანი

X=input("enter a input ")
J=0
while J<= 0:
    J=+1
    while X[0:1] == "a" or X[0:1] == "e" or X[0:1] == "i" or X[0:1] == "o" or X[0:1] == "u" and X[-1:] == "a" or X[-1:] == "e" or X[-1:] == "i" or X[-1:] == "o" or X[-1:] == "u":
        J=J-1
        X=input("enter a different input ")

print(X)