# 1) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას, ფუნქციამ ამ წინადადების თითოეული სიტყვა უნდა შეინახოს სიაში,
# როგორც ცალკე ელემენტი. საბოლოოდ გადააქციეთ სია ისევ წინადადებად, სადაც სიტყვებს შორის არის მძიმე და ერთი დაშორება(", ")

centence = "hello user im here to help you"

def words(item):
    list=[]
    X=""
    for letter in item:
        if letter != ' ':
            X += letter
        else:
            list.append(X)
            X=""

    new_centence = ""

    for word in list:
        new_centence += word + ", "
    return new_centence

print(words(centence))

# 2) შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)

def words_len(item):
    list=[]
    X=""
    for letter in item:
        if letter != ' ':
            X += letter
        else:
            list.append(X)
            X=""
    
    for word in list:
        word_len =len(word)
        print(f"in {word} is {word_len} letters")

print(words_len(centence))

# 3) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, სადაც ყოველი სიტყვის შორის ერთზე მეტი დაშორებაა(space).
# თქვენი დავალებაა ჩამოაშოროთ გადმოცემულ წინადადებას ზედმეტი space-ები(სიტყვებს შორის მხოლოდ ერთი უნდა იყოს). 
# საბოლოოდ დააბრუნეთ ეს წინადადება
 
centence=input("enter a centence: ")
centence+=" "

def space(item):
    list=[]
    X=""
    for word in item:
        if word != " ":
            X+=word
        else:
            list.append(X)
            X=""

    new_item=""

    for I in list:
        if len(I) > 0:
            new_item += I + " "
    return new_item

print(space(centence))

# 4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). საბოლოოდ კი აბრუნებს მას

centence = input("enter a centence: ")
centence+= " "

def underline(item):
    list=[]
    X=""
    for word in item:
        if word != " ":
            X+=word
        else:
            list.append(X)
            X=""
        
    new_item=""

    for I in list:
        new_item+= I + "-"
    return new_item

print(underline(centence))

# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება. თქვენი დავალებაა ამ წინადადების სიტყვები შეაბრუნოთ და
# დააბრუნოთ(სიტყვების სიმბოლოები არ უნდა იყოს შებრუნებული) 

centence ="hi there im goga"
centence += " "

def reverse(item):
    list=[]
    X=""
    for word in item:
        if word != " ":
            X+=word
        else:
            list.append(X)
            X=""

    new_list= ""
    new_item= list[::-1]

    for I in new_item:
        new_list+= I + " "
    return new_list

print(reverse(centence))