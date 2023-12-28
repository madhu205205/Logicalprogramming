# even or odd
# def function_odd(n):
# i = int(input("enter the value:"))
# if i%2==0:
#     print("even")
# else:
#     print("odd")

def even_odd(i):

    if i % 2 == 0:
        return "even"
    else:
        return "odd"

data = even_odd(10)
print(data)