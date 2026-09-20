list = []
sum=0

for i in range (0,10):
    a = int(input("enter the numbers..:"))
    list.append(a)
    sum+=a
print("sum of the list is :",sum)

average = sum/10
print("average of the list is :",average)