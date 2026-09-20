list = []
n = int(input("enter the range of the list:"))

for i in range (0,n):
    a = int(input("enter the number :"))
    list.append(a)
print(list)

for i in range (0,n):
    a = list[i]
    b = (0-a)
    list[i] = list[b]
    list[b]= a
print("Reverse list is :",list)