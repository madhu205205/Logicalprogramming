## even or odd

# def even_odd(i):#10
#     if i % 2 == 0:#10
#         return "even"
#     else:
#         return "odd"
#
#
# data = even_odd(10)# even
# print(data)#even
###########################
##sum of add fucnctions

# def sum_addfunctions(x, y, z):#10,20,30
#     return x+y+z#10,20,50
#
#
# add = sum_addfunctions(x=10, y=20, z=50)
# print(add)#80
##################
####hankerank exmple
# n = int(input())
#
# if n >= 1 and n <= 100:
#     if n % 2 != 0:
#         print("weird")
#     else:
#         if n >= 2 and n <= 5:
#             print("not weird")
#         elif n >= 6 and n <= 20:
#             print("weird")
#         else:
#             print("not weird")
#############
##leap year

def leap_year(year):
    # year = 20000
    if (year % 400 == 0) and (year % 100 != 0) or year % 4 == 0:
        print("leap year")
    else:
        print("not leap year")


year = int(input("enter year:"))
print(leap_year(year))
