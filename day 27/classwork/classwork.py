# 1) მომხმარებელს შემოატანინეთ სიტყვა, თუ ამ სიტყვის სიგრძე არის 5-ზე მეტი, მაშინ გამოვიტანოთ ყველა ასო, პატარა შრიფტით, თუ არადა დიდით.

X=input("please enter a word: ")

if len(X)>5:
    X=X.lower()
    print(X)
else:
    X=X.upper()
    print(X)

# 2)შექმენით ფუნქცია რომელიც არგუმენტად იღებს სიტყვას/წინადადებას და ასოს, ის აბრუნებს პირველი სად შეხვდა ასო ამ სიტყვაში

def finder (subject):
    return subject.find("l")

print(finder(input("enter something: ")))


# 3) შექმენით ერთი ვოიდ ფუნქცია და ერთი ფუნქცია რომელიც აბრუნებს სტრინგს.

def void ():
    print("hello user")

def return_func ():
    return 1+2
