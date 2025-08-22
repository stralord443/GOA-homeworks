# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია
# პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი

X=[1,4,7,16,21,7,6]

def my_func (func):
    return print(func[1:-1])

my_func(X)

# 2) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, გადაურეთ ორივეს for ციკლით და
# გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ

calc1=[4,6,7,2]
calc2=[7,66]

def sum_of_2 (num1,num2):
    sum1=0
    for calc1 in num1:
        sum1+=calc1

    sum2=0
    for calc2 in num2:
        sum2+=calc2

    return sum1*sum2

print(sum_of_2(calc1,calc2))

# 3) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ
# გაორმაგებული რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

lst=[8,3,74,9,1]

def duble (list):
    nlst=[]
    list_traccer=0
    while list_traccer < len(lst):
        current_object=lst[list_traccer]*2
        nlst.append(current_object)
        list_traccer+=1
    return nlst

print(duble(lst))

# 4) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით
# და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

lst=[4,6,18,3,7,26,1,79,56,9,43]

def even(list):
    nlist=[]
    for lst in list:
        if lst %2 ==0:
            nlist.append(lst)
    return nlist

print(even(lst))

# 5) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ 
# გადმოცემული სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

names=["nini","nana","luka","davit","aleqsandre","nika"]

def name_N (name):
    new_names=[]
    for name in names:
        if name[0] == "n" or name[0] == "N":
            new_names.append(name)

    return new_names

print(name_N(names))