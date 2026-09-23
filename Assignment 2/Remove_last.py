def remove_last(list):
    list.pop()
list=[]
for i in range(0,5):
    n = int(input("enter the elements: "))
    list.append(n)
print(list)
remove_last(list)
print("after removing the last element",list)