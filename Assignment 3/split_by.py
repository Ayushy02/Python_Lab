import re
text = (input("Enter the string: "))
word = (input("Enter the word want to split: "))

s = re.split(rf"{word}",text)
print(s)