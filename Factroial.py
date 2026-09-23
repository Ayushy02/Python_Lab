def Fact(num):
    if num==0:
        return 1
    
    return num*Fact(num-1)

num = int(input("enter the number: "))
a=Fact(num)
print(a)
