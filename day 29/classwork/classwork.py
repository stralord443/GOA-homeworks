# 1) შექმენით ფუნქცა რომელიც იღებს წინადადებას და აბრუნებ რამდენი სიტყვაა მასში.

X=["agsga","agsahehadha","asgawashah"]

def ammount (words):
    p=0
    for I in words:
        p+=1
    return p

print(ammount(X))

# 2) შექმენით ფუნქცია რომელიც მიიღებს რიცხვების სიას და დაბრუნებს მხოლოდ ლუწების ჯამს.

lst=[4,6,18,3,7,26,1,79,56,9,43]

def even(list):
    nlist=[]
    for lst in list:
        if lst %2 ==0:
            nlist.append(lst)
    return nlist

print(even(lst))

# 3) შექმენით ფუნქცია რომელიც აბრუნებს სიაში უმაღლეს რიცხვს.

lst=[4,6,18,3,7,26,1,79,56,9,43]

def higth (list):
    higthest=0
    for lst in list:
        if lst >= higthest:
            higthest=lst

    return higthest

print(higth(lst))
