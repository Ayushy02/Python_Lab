import re
text = (input("Enter the string: "))

#finding all the present in the text according to the conditon;
num = re.findall(r"\d+",text)
print(num)

#finding all the word in the text according to the condition; 
word = re.findall(r"[A-Z][a-z]+",text)
print(word)