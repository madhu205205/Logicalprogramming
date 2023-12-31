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
# string = input("enter letter:")
# if (string == string[::-1]):
#     print("is palindro ")
# else:
#     print("is palindro invalid")


# def str_pal(str):
#     if str == str[::-1]:
#         return True
#     else:
#         return False
#
#
# print(str_pal(str='madhu'))


#other method
# s = input()
# print("valid" if s==s[::-1] else "invalid")


############
#excption interview
# try:
#     a = 10
#     b = 33
#     print(a + b)
#    # raise Exception
# except Exception:
#     print("hello")
# else:
#     print("hiii")
# finally:
#     print("good morning")
###############
# t = (1, 2, 3, 4)
# tuple = t + (5,)
# print(tuple)
################
# s="   wellcome to python   "
# print(len(s))
# print(s)
####
# str = "madhusudhanr"
# print("".join(reversed(str)))
# print(str[::-1])
# x = ""
# for i in str:
#     x = i + x
# print(x)
###########

# str = "hello"
# str_rever = ""
# for i in str.split():
#     str_rever = str_rever + i[::-1] + ""
# print(str_rever)
#
# str_rever = ""
# for i in str.split():
#     str_rever = i + "" + str_rever
# print(str_rever)

#######
##substring
# str = "wellcome to python"
# str_rever = "wellcome to python"
# print(str in str_rever)
#
# str = "hellow madhu"
# sub_str = "hellow madhu"
# print(sub_str in str)
#
# splited_str = str.split()
# count = splited_str.count(sub_str)
# print(count)
# print("index of ",str.find(sub_str))

############
##sort method
# x=[10,30,20,1,3,2]
# x.sort()
# print(x)

#
#reverse
# x=[10,20,10,30,20,1,2,3]
# x.reverse()
# print(x)

##
# import copy
# x = [1,2,3,4,[10,20,30]]
# y = copy.copy(x)
# x[4][1]=100
# print(y) # [1, 2, 3, 4, [10, 100, 30]]
# Y = copy.deepcopy(x)
# # X[4][1] = 100
# print(y)


# from collections import Counter
# z = ['madhu', 'bali', 'redddy', 'madhu', 'redddy', 'bali']
# print(Counter(z))

# list = ['a', 'b', 'c', 'a', 'b', 'c']
#
#
# def func(list):
#     dict = {}
#     for i in list:
#         if i not in dict.keys():
#             dict[i] = list.count(i)
#     return dict



# print(func(list))




##############
# s=input("enter name:")
# print(s[::-1])

# s=input("enter name:")
# print("".join(reversed(s)))
##########
# num = 10
# print("the type of varible:", type(num))
# converted_num = str(num)
# print("the type of after converted:", type(converted_num))
# #########
# def decor(fun):
#     def inner(name):
#         if name == "madhu":
#             print("hell")
#         else:
#             print(fun)
#
#     return inner
#
#
# @decor
# def wish(name):
#     print("hello", name)
#
#
# wish("madhu")
###############
##factorial
# fact = 1
# n = 5
# while n > 1:
#     fact = fact * n
#     n = n - 1
#     print(fact)
#other method
# import math
# print(math.factorial(5))
#other method
# def fact(n):
#     num = 1
#     for i in range(1, n + 1):
#         num = num * i
#     return num
#
#
# print(fact(5))


############
##fabinosis
# a = 10
# b = 0
# c = 1
# for z in range(0, a):
#     if (z <= 1):
#         temp = z
#     else:
#         temp = b + c
#         b = c
#         c = temp
#         print(temp)


##
# def fabi(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#         # print(a, b)
#
#
# print(list(fabi(int(input("enter value:")))))


###
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def func_par(arr, pair):
#     count = 0
#     for i in arr:
#         for j in arr:
#             if i + j == pair:
#                 count = count + 1
#     return count
#
#
# print(func_par(x, 7))


##list compression
# xx = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4]
# print([x ** 2 if x % 2 == 0 else 0 for x in xx])
#
# print([x**2 for x in xx if x%2==0])


#intervie quations dict
# from collections import OrderedDict
#
# test_dict = {'madhu': 4, 'reddy': 2, 'bali': 5}
#
# res = OrderedDict(reversed(list(test_dict.items())))
#
# # printing result
# print("The reversed dict : " + str(res))
#
#output ('bali',5),('reddy',2)('madhu',4)

##how to find the get frequency of following string in python
# text = """Yesterday I went fishing. I don't fish that often"""
# data = text.split()
# dictt = {}
# for i in data:
#     if i in dictt.keys():
#         dictt[i] = dictt[i] + 1
#     else:
#         dictt[i] = 1
# print(dictt)

##write a read a string and covert all even number index value into upper case

# x "madhusudhan"
# out put
#MaDhUsUdHaN
#012345678910

# def myfunc(st):#madhusudh
#     newst = ''#MaDhUsUdH
#     for index, alpha in enumerate(st):
#         if index % 2 == 0:#MaDhUsUdH
#             newst = newst + alpha.upper()
#         else:
#             newst = newst + alpha.lower()
#     return newst
#
#
# print(myfunc("madhusudh"))
###################################
#even charter i upper case in index
# def convert_even_index_to_uppercase(input_string):
#     result = ""
#
#     for index, char in enumerate(input_string):
#         if index % 2 == 0:
#             result += char.upper()
#         else:
#             result += char
#
#     return result
#
#
# user_input = convert_even_index_to_uppercase(input("Enter a string:"))
# print("Result:", user_input)

###############
# hello = {'name':'madhu','emp':'reddy','salary':'55666'}
#
# for i in enumerate(hello):
#     print(i)
###############
##regx
# import re
# def fun(s1, s2):
#     print(re.sub("[aeiou]", s2, s1))
#
#
# dd = fun(s1="madhu", s2="bali")
# print(dd)
##




# def fun(n,s):
#     # s = ''
#     if n== 1:
#         print("hello",s)
#     else:
#         print("bye",s)
#
# mm = int(input(fun(n=1,s=1)))
# print(mm)
###############
# def fun(c):
#     s = ''
#     for i in s:
#         if i.isdigit():
#             c=c+1
#     print("true" if c==5 else "false")
#
#
# mm = fun(c=0)
# print(mm)

##prime number

# def func(num):
#     x = []
#     for j in range(1, num):  # 5
#         for i in range(2, j):  # 2,5
#             if j % i == 0:  # 5%2
#                 break
#         else:
#             x.append(j)
#     return x
#
#
# print(func(50))
############
##interview quation string chareter count
# s = "madhumadhu"
# d = {}
# for i in s:
#     if i in d.keys():
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)

# s1 = input()
# s2 = input()
#
# print("true" if s2 in s1+s1 else "false")

###########
# def string(s1, s2):
#     if s1 + s2 == 0:
#         print("true")
#     else:
#         print("false0")
#
#
# print(string(s1="reddy", s2="reddy"))
###########
##missing numbers


# def missing(s):
#     for i in range(97, 128):
#         if chr(i) not in s:
#             print(chr(i), end='')
#
#
# print(missing(s=input("madhu")))

def find_missing(lst):
    return [i for x, y in zip(lst, lst[1:])
            for i in range(x + 1, y) if y - x > 1]


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))
