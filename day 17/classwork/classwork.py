# 1)  შექმენით List, List-ში შეინახეთ 4 მანქანა და შემდეგ მე-1 და მე-2 ინდექსი შეცვალეთ, საბოლოოდ დაპრიტეთ მთლიანი List-ი

x=["BMW","Mercedes","Lexus","Tesla"]
x[1]="Ford"
x[2]="Audi"

print(x)


#2) რაში გვეხმარება ინდექსინგი? რა შეგივიძლია გავაკეთოთ ინდექსინგის მეშვეობით? შეგვიძლია თუ არა სტრინგების შეცვლა ინდექსინგით?


#indexing helps us for more detailed editing of a list

#with indexing we can make more detailed edits

#yes we can 


#3) txt = "hello world, python html" 
# --დაბეჭდეთ სტრინგის პირველი ასო,
# --დაბეჭდეთ სტრინგის ბოლო ასო ნეგატიური ინდექსის გამოყენებით,
# --ახსენი როგორ მუშაობს ინდექსები ანუ საიდან იწყება ასევე ნეგატიური ინდექსი საიდან იწყება 

txt = "hello world, python html" 

print(txt[0])

print(txt[len(txt)-1])

#index starts form 0 to infiniti and negative index starts from -1 to negative infiniti

