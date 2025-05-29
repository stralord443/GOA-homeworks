# 2. ახსენით რა განსხვავებაა implicit და explicit datatype comversion-ში.


# implicit datatype conversion არის კომპიუტერის მიერ გარდაქმნილი დათა თაიპი, მაგალითად გამრავლებისას int + int მივიღებთ float-ს

# expelicit datatipe conversion არის ადამიანის მიერ გარდაქმნილი დათა თაიპი, მაგალითად int დათა თაიპის str ტიპად გარდაქმნა


# 3. წაიკითხეთ დამატებითი მასალა: https://www.geeksforgeeks.org/type-casting-in-python/

#done


# 4. შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)

X=int(input("enter a number "))

for I in range (X):
    print(I)

# 5. გაალეთეთ მეოთხე დავალება While loop-ის გამოყენებით.

P=int(input("enter a number "))
Z=1

while Z < P:
    print(Z)
    Z += 1