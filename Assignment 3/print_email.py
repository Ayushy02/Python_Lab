import re
text = (input("Enter your email: "))
e = re.match(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}",text)
if e:
    print(e.group())
else:
    print("your email is not valid")