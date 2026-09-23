def greatest_num(x,y):
    if x>y:
        return x
    return y


a = int(input("enter the first number: "))
b= int(input("enter the second number: "))
num = greatest_num(a,b)
print ("greatest number is",num)