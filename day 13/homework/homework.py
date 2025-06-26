# დავალება 1: წნევის ანალიზი
# მომხმარებელი შეიყვანს ორ მაჩვენებელს: სისტოლური და დიასტოლური წნევა.
# პროგრამამ უნდა განსაზღვროს წნევის კატეგორია:

# თუ სისტოლური > 140 ან დიასტოლური > 90 → "მაღალი წნევა"

# თუ სისტოლური < 90 ან დიასტოლური < 60 → "დაბალი წნევა"

# სხვა შემთხვევაში → "წნევა ნორმალურია"

sistol=int(input("enter a sistol: "))
distol=int(input("enter a distol: "))

if sistol > 140 or distol > 90:
    print("high preashure")
elif sistol < 90 or distol < 60:
    print("low preashure")
else:
    print("normal preashure")

# დავალება 2: წონის შეფასება ასაკის მიხედვით (უბრალოდ და ლოგიკურად)
# აღწერა:
# მომხმარებელი შეიყვანს საკუთარ ასაკს და წონას.
# პროგრამამ უნდა შეაფასოს წონა ასაკის მიხედვით მარტივი ლოგიკით:

# თუ ასაკი < 10:

# წონა < 20 → "წონა დაბალია"

# წონა 20-40 → "წონა ნორმალურია"

# წონა > 40 → "წონა მაღალია"

# თუ ასაკი 10-17:

# წონა < 40 → "წონა დაბალია"

# წონა 40-65 → "წონა ნორმალურია"

# წონა > 65 → "წონა მაღალია"

# თუ ასაკი 18 ან მეტი:

# წონა < 50 → "წონა დაბალია"

# წონა 50-90 → "წონა ნორმალურია"

# წონა > 90 → "წონა მაღალია"

age=int(input("enter your age: "))
weight=int(input("enter your weight: "))

if age < 10:
    if weight < 20:
        print("low weight ")
    elif weight <= 40:
        print ("normal weight ")
    else:
        print("high weight ")

if age >= 10 and age <= 17:
    if weight < 40:
        print("low weight ")
    elif weight <= 65:
        print ("normal weight ")
    else:
        print("high weight ")

if age >= 18:
    if weight < 50:
        print("low weight ")
    elif weight <= 90:
        print ("normal weight ")
    else:
        print("high weight ")

# დავალება 3: ასაკის შეჯერება დღის მონაკვეთთან
# შეიყვანოს მომხმარებელმა ასაკი და საათი (0-დან 23-მდე). პროგრამამ განსაზღვროს:

# თუ ასაკი < 18 და დრო ≥ 22 → "დროა დაძინების"

# თუ ასაკი ≥ 60 და დრო ≥ 21 → "დასვენება რეკომენდებულია"

# სხვა შემთხვევაში → "შეგიძლიათ გააგრძელოთ აქტივობა"

age=int(input("enter your age: "))
time=int(input("enter time: "))

if age <18 and time >= 22:
    print("it's time to stop ")
elif age >= 60 and tome >= 21:
    print("it's recomended to rest")
else:
    print("you can continue ")

# დავალება 4: ფიზიკური აქტივობის რეკომენდაცია
# მომხმარებელი შეიყვანს თავის ასაკს და გულის ცემას.
# პროგრამამ უნდა დაარიგოს ასეთი რჩევები:

# ასაკი < 30 და გულისცემა < 140 → "შეგიძლიათ მეტი ივარჯიშოთ"

# ასაკი ≥ 30 და გულისცემა > 170 → "დასვენება გჭირდებათ"

# სხვა შემთხვევაში → "Activity level is normal"

age=int(input("enter tour age: "))
heart_beat=int(input("enter your heart rate: "))

if age < 30 and heart_beat < 140:
    print("you can exercise more ")
elif age >= 30 and heart_beat > 170:
    print("you need to rest")
else:
    print("")

# დავალება 5: ასაკი და კვება
# მომხმარებელი შეიყვანს ასაკს. პროგრამა გასცემს კვების რეკომენდაციას:

# 0–12 → "ბევრი ვიტამინიანი საკვები"

# 13–25 → "ენერგიის მომცემი საკვები"

# 26–59 → "ბალანსირებული რაციონი"

# 60+ → "დაბალკალორიული და მსუბუქი საკვები"

age=int(input("enter your age: "))

if age >= 0 and age <= 12:
    print("you need food, rich with vitamines")
elif age <=25:
    print("you need high calory food")
elif age <= 59:
    print("you need low calory food")
else:
    print("you need low calory and easy to digest food")