# 1) გააკეთეთ პატარა გულის ცემის სისტემა რომელიც ითვლის რა თქმა უნდა გულის ცემას  თუ 180 ზე 
# მეტია ამ შემთხვევაში მაღალია თუ 160-დან 170 მდე არის ამ შემთვევაში არის ნორმალური თუ 160-ზე ნაკლებია ამ შემთხვევაში დაბალია

heart_beat=int(input("enter your heart beat rate "))

if heart_beat > 180:
    print("მეტია")
elif heart_beat>160:
    print("ნორმაა")
else:
    print("ნაკლებია")

# შექმენი პროგრამა, რომელიც მომხმარებლის მიერ შეყვანილი ასაკის მიხედვით დაადგენს, რომელი ასაკობრივი ჯგუფის წევრია ადამიანი.
# თუ ასაკი უარყოფითია — გამოიტანე: "არასწორი ასაკი"
# თუ ასაკი ნაკლებია 13-ზე — გამოიტანე: "ბავშვი"
# თუ ასაკი არის 13-დან 19-ის ჩათვლით — გამოიტანე: "თინეიჯერი"
# თუ ასაკი არის 20-დან 59-ის ჩათვლით — გამოიტანე: "ზრდასრული"
# თუ ასაკი არის 60 ან მეტი — გამოიტანე: "პენსიონერი"

age=int(input("enter your age "))

if age <0:
    print ("error")
elif age <13:
    print("ბავშვი")
elif age <20:
    print("თინეიჯერი")
elif age <60:
    print("ზრდასრული")
else:
    print("პენსიონერი")