list = []

for i in range (0,5):
    a = int(input("enter the number :"))
    list.append(a)
print(list)


for i in range (0,len(list)):
    for j in range (0,i):
        if list[i] == list[j]:
            if i!=j:
                list[j]=0
print("list after removing the duplicate element",list)