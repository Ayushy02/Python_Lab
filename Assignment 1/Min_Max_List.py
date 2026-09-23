list = []

for i in range (0,7):
    a = int(input("enter the number :"))
    list.append(a)
print(list)

min = list[0]
max = list[0]

for n in list:
    if n < min:
        min = n
       
    if n > max:
        max = n
        
print("minimum no. of the list is :",min)

print("maximum no. of the list is :",max)