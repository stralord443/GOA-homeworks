#  1:
# სია: numbers = [10, 20, 30, 40, 50, 60, 70]
# აიღე ამ სიიდან პირველი 3 ელემენტი slicing-ის გამოყენებით.

numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[0:3])

#  2:
# სია: letters = ['a', 'b', 'c', 'd', 'e', 'f']
# დაპრინტე სიიდან ელემენტები 'c', 'd', 'e' slicing-ით.

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[2:5])

#  3:
# სია: words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# აიღე სიის ბოლო 2 ელემენტი slicing-ის მეშვეობით.

words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
print(words[len(words)-2:])

#  4:
# სია: colors = ['red', 'green', 'blue', 'yellow', 'purple']
# დაპრინტე სია შუიდან დაწყებული ბოლომდე (სადღაც 'blue'-დან ბოლომდე) slicing-ით.

colors = ['red', 'green', 'blue', 'yellow', 'purple']
print(colors[2:])

#  5:
# სტრინგი: text = "programming"
# დაპრინტე მხოლოდ პირველი 5 სიმბოლო slicing-ის მეშვეობით.

text = "programming"
print(text[:5])