
def show_info(fun):
    def wrapper(num):
        print("before function calling")
        fun(num)
        print("after function calling")
        return fun
    return wrapper

show_info
def square(num):
    return num*num

print('square', square(5))
