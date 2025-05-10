# 1) შემოატანინეთ მომხხმარებელს სტრინგი და გამოიტანეთ მისი პირველი ასო

name=input()

print(name[0])

# 2) შემოატანინეთ მომხმარებელს ორი სტრინგი და გამოიტანეთ მათ გაერთიანება

user_1=input()
user_2=input()

print(user_1+user_2)

#3) შემოატანინეთ მომხმარებელს სტრინგი და თუ მომხმარებლის შემოტანილი სტრინგი არის 'yes',
#  მაშინ შემოატანინეთ სახელი და გამოიტანეთ ის. ყველა ვარიანტში საბოლლოდ დაემშვიდობეთ მომხმარებლლს მესიჯი 'goodbye' - თი

user_input=input()

if user_input == "yes":
    user_name=input()
    print=user_name

print("goodbye")

# 4) შემოატანინეთ მომხმარებელს ასო თუ ეს ასო არის 'A' მაშინ გამოიტანეთ რიცხვი 100, თუ ის არის 'B' - 80,
# თუ 'C' - 60, თუ 'D' - 40, ხოლო თუ 'F' მაშინ სიტყვა 'Failed!'

user_letter=input()

if user_letter == "A":
    print(100)

if user_letter == "B":
    print(80)

if user_letter == "c":
    print(60)

if user_letter == "d":
    print(40)

if user_letter == "F":
    print("Failed")


# 5) მომხმარებელს შემოატანინეთ ორი სტრინგი და თუ ეს სტრინგები ერთმანეთს ემთხვევა გამოიტანეთ
# True ხოლო თუ არ ემთხვევა გამოიტანეთ False

user_word_1=input()
user_word_2=input()

if user_word_1 == user_word_2:
    print("True")

if user_word_1!= user_word_2:
    print("False")
