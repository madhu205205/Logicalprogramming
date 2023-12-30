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
# def fun(num):
#     print("the type of varible:", type(num))
#     converted_num = str(num)
#     print("the type of after converted:", type(converted_num))
#
#
# hh = fun(num=10)
# print(hh)

## print(sum(int(i)for i in list(input())))

##################
##odd number
#
# def odd_number(n):#10
#     if n % 3 == 0:
#         print("even number")
#     else:
#         print("odd number")
#
#
# data = odd_number(n=10)
# print(data)#odd number

############
##prime number
# print(sum([int(i) for i in list(input()) if i in '2357']))

# def prime_number(n):
#     if n > 2:
#         for i in range(2, int(n / 2) + 1):
#             if n % i == 0:
#                 print(n, "not prime number")
#                 break
#             else:
#                 print(n, "prime number")
#     else:
#         print(n, "not prime number")
#
#
# data = prime_number(15)
# print(data)

#####
##divisbale by 3,5
# print(sum([int(i) for i in list(input()) if i in '369']))


# def divisble(n):#50
#     for i in range(0, n):#50
#         if i % 15 == 0:
#             print(i, end='')
#
#
# data = divisble(n=50)
# print(data)
###########
###string charters reverse
#mothod 1
# s= "wellcome"
# print(s[::-1])

# #mothod 2

# s= "madhu"
# print("".join(reversed(s)))
##method 3
# s = input("enter name:")
# print(s[::-1])

#####
##palindrom
string = input("enter letter:")
if (string == string[::-1]):
    print("is palindro ")
else:
    print("is palindro invalid")
