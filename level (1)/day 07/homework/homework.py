# 2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

# sequences არის ის თანმიმდევრობა რომლის მიხედივთაც ხდება კოდის შესრულება

# teration არის კოდის ციკლური გამეორება სანამ შესაბამის მნიშვნელობას არ მივიღებთ

# selection კოდის ორი ან მეტი არჩვანი რომელიც განისაზღვრება ჩვენს მიერ არჩეული პირობებით

# 3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

# ალგორითმი არის, იმ წესების, რეცეპტის ან რაიმე მოძრაობის სწორი თანმიმდევრობა,
# რაც არის საჭირო ჩვენთვის სასურველი მიზნის მისაღწევად

# 4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:

#print(True or False and False or True and False or False and False or False and True and False or True)
#print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)

# ორივე ვარიანტში True

# 5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

num=int(input())

if (num % 2) == 1:
    num >10 or 7
    print("True")

# 6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

str_example="7"
int_example=10
float_example=10.2
bool_example=True

str(int_example)
str(float_example)
str(bool_example)

int(str_example)
int(float_example)
int(bool_example)

float(str_example)
float(int_example)
float(bool_example)

bool(str_example)
bool(int_example)
bool(float_example)

# 7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ
# "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

leap_year=int(input())

if (leap_year %4) == 0:
    (leap_year %100) !=0 or (leap_year %400) == 0 
    print("This is leap year")