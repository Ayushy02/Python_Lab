list=[]

for i in range(0,5):
    a = (input("enter the fruits: "))
    list.append(a)
print(list)

print("2nd element of the list is: ",list[1])

print("4th element of the list is:",list[3])

print("list after update")

list[4]='mango'
print(list)