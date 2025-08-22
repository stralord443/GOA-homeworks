# 1)კომენტარების სახით ჩამოწერეთ  ყველა პილიუსი და მინუსი set -ების

# set allows us to find needed information very fast, and doesn't allow duplicants in it
# btu set saves information randomly, and we cant control the place where information is going to be 

# 2)შექენით სეტები და განიხილეთ ოპერატორები (union,intersection,difference,symmetric_difference,clear,add,remove) 
# ახსენით ასევე კომენტარებით და გააკეთეთ ორივე ხერხით როგორც ტექსტიტ ისე სიმბოლოთი.

A={1,2,3,4,5}
B={4,5,6,7,8}

print(A.union(B)) #creates a new set with all information
print(A |(B)) 
print(A.intersection(B)) #creates a new set with all identical information
print(A & (B))
print(A.difference(B)) #creates a new set with all different information from A
print(A - (B))
print(A.symmetric_difference(B)) #creates a new set with all different information  
print(A ^ (B))
print(A.clear()) #clears all information
print(A.add(7)) #adds an information 
print(A.remove(1)) #removes an information


# 3)შექმენი სეტი fruit1 და fruit2 შეინახეტ სხვადასხვა ხილები და გააკეთეთ ყველა მანიპულაცია რაც
# გახსენდებათ ოპერატორების დახმარებით, შემდეგ ახხსენით კომენტარებით.

fruit1 ={1,2,3,4,5}
fruit2 ={4,5,6,7,8}

print(fruit1.union(fruit2)) #creates a new set with all information
print(fruit1 |(fruit2)) 
print(fruit1.intersection(fruit2)) #creates a new set with all identical information
print(fruit1 & (fruit2))
print(fruit1.difference(fruit2)) #creates a new set with all different information from A
print(fruit1 - (fruit2))
print(fruit1.symmetric_difference(fruit2)) #creates a new set with all different information  
print(fruit1 ^ (fruit2))
print(fruit1.clear()) #clears all information
print(fruit1.add(7)) #adds an information 
print(fruit1.remove(1)) #removes an information
