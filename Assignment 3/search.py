import re
text = (input("Enter the string: "))

# find element in the string or text;
x = re.search(r"\d+",text) 
print(x.group())


word =(input("Enter the word you want to find: "))

m= re.search(rf"{word}",text)
if m:
    print(m.group(),"is present in text")
else:
    print(word,"word is not present in the text")
