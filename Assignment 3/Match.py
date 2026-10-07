import re
text = (input("enter the string: "))
word = (input("enter the starting word: "))
m = re.match(rf"{word}",text)

if m:
    print(m.group())
else:
    print("word not found")
