import re
text = (input("Enter the string: "))
word = (input("enter the word want to replace: "))


num = re.sub(rf"\d",word,text)
print(num)


