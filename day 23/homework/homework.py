# დავალება 1:
# შეიყვანე სიტყვა, სანამ მისი პირველი და ბოლო ასოები არ იქნებიან თანხმოვნები.
# რას ნიშნავს?
# შენ უნდა უთხრა რობოტს სიტყვები.
# მაგრამ რობოტი შეგეკითხება ბევრჯერ, სანამ არ ეტყვი ისეთ სიტყვას, რომლის პირველი ასოც და ბოლო ასოც არცერთი არ არის ხმოვანი (ანუ არ არის ა, ე, ი, ო, უ).


X=input("enter a input ")
J=0
while J<= 0:
    J=+1
    while X[0:1] == "a" or X[0:1] == "e" or X[0:1] == "i" or X[0:1] == "o" or X[0:1] == "u" and X[-1:] == "a" or X[-1:] == "e" or X[-1:] == "i" or X[-1:] == "o" or X[-1:] == "u":
        J=J-1
        X=input("enter a different input ")

print(X)

# დავალება 2:
# შეიყვანე 5 სიტყვა, მაგრამ შეინახე (დაახსოვრე) მხოლოდ ისინი, რომლებიც სწორია.
# რა არის „სწორი“ სიტყვა?
# ამაში უნდა გითხრან წინასწარ რა კრიტერიუმით აირჩიე სწორი, მაგრამ დავუშვათ, სიტყვა სწორია მაშინ, როცა მასში ორივე — პირველი და ბოლო ასოები — თანხმოვნებია.

# შენ უნდა უთხრა 5 სიტყვა. რობოტი კი შეინახავს მხოლოდ იმ სიტყვებს, რომლებიც სწორია.

# დავალება 3:
# რობოტმა უნდა დაითვალოს, რამდენჯერ სცადე სწორი სიტყვის შეყვანა.
# ანუ ყოველ ჯერზე, როცა სწორი სიტყვა უთხარი, უნდა დაიმახსოვროს და უთხრას ბოლოს რიცხვი.

k=[]
K=0

for I in range(0,5):
    word_1=input("input a word :")
    if word_1[0:1] == "a" or word_1[0:1] == "e" or word_1[0:1] == "i" or word_1[0:1] == "o" or word_1[0:1] == "u" and word_1[-1:] == "a" or word_1[-1:] == "e" or word_1[-1:] == "i" or word_1[-1:] == "o" or word_1[-1:] == "u":
        k.append(word_1)
        K+=1

print(k)
print(K)


# # დავალება 4:
# შეიყვანე 10 სიტყვა, მაგრამ დაბეჭდოს (გამოაჩინოს) მხოლოდ სწორი სიტყვები.
# ანუ ისევ იგივე ლოგიკა – 10 სიტყვა უთხარი, მაგრამ ეკრანზე უნდა გამოჩნდეს მხოლოდ სწორი სიტყვები
# (ისინი, რომელთაც პირველი და ბოლო ასო თანხმოვანია, ან რაც წესია მოცემულ ამოცანაში).


k=[]

for I in range(0,10):
    word_1=input("input a word :")
    if word_1[0:1] == "a" or word_1[0:1] == "e" or word_1[0:1] == "i" or word_1[0:1] == "o" or word_1[0:1] == "u" and word_1[-1:] == "a" or word_1[-1:] == "e" or word_1[-1:] == "i" or word_1[-1:] == "o" or word_1[-1:] == "u":
        k.append(word_1)

print(k)

# დავალება 5:
# შეიყვანე სიტყვა და რობოტმა უნდა დათვალოს რამდენი ხმოვანია და რამდენი თანხმოვანი აქვს მას.
# გაიმეორებს ამას მანამ, სანამ არ შეიყვან სწორ სიტყვას.

#  ანუ რობოტს ეუბნები სიტყვას → ის გეუბნება:

# "ამ სიტყვაში არის 3 ხმოვანი და 4 თანხმოვანი"

# და გთხოვს ახალს, სანამ სწორ სიტყვას არ ეტყვი. 
