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

# def leap_year(year):
#     # year = 20000
#     if (year % 400 == 0) and (year % 100 != 0) or year % 4 == 0:
#         print("leap year")
#     else:
#         print("not leap year")
#
#
# year = int(input("enter year:"))
# print(leap_year(year))
###other method
# import calendar
# year = 2000
# print(calendar.isleap(year))

###########
##e - commers coding
# def ifcondtions(n):
#     # n = int(input())
#     if n >= 30 and n <= 100:
#         if n >= 30 and n <= 50:
#             print("d")
#
#         elif n >= 51 and n <= 60:
#             print("c")
#         elif n >= 61 and n <= 80:
#             print("b")
#         else:
#             print("a")
#     else:
#         print("both are condtion is false")
#
#
# mm = ifcondtions(n=100)
# print(mm)
#####
## haker rank cupes code
# def coups(n):
#     print(n + n // 6)##1 add
#
#
# mm = coups(n=6)
# print(mm)

#####
###digit given number
# def numbers(n):
#     while n != 0:
#         d = n % 10
#         print(d, end='')
#         n = n // 10
#
#
# obj = numbers(n=145)
# print(obj)
###
##digit number from the reverse
##reversed string

# for i in input()[::-1]:
#     print(i,end='')

###


#### interger to string function
def fun(num):
    print("the type of varible:", type(num))
    converted_num = str(num)
    print("the type of after converted:", type(converted_num))

hh = fun(num=10)
print(hh)


# print(sum(int(i)for i in list(input())))



# str = "madhusudhanr"
# print("".join(reversed(str)))
# print(str[::-1])