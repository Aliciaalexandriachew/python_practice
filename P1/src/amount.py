'''
Created on 20 Jul 2020

@author: Alicia

'''
import math

# amount = 3.5
# print("$", int(amount), " and ", int((amount - int(amount)) * 100), " cents", sep = "")

'''
Study Unit 2 Activity 2
'''
# print(int(3.0)) # result 3
# print(round(3.0)) # result 3
#  
# print(int(3.5)) # result 3
# print(round(3.5)) # result 4
 
'''
Study Unit 2 Activity 3
'''
# print(round(314.159265, -1)) # result 310.0

'''
Study Unit 2 Activity 4
'''
# a = (3 + 4) * 5
# print(a)
# 
# n = 2
# b = n * (n-1) / 2
# print(b)
# 
# r = 2
# c = 4 * math.pi * r**2
# print(c)
# 
# d = math.sqrt(r * (math.cos(a)**2) + r * (math.sin(b)**2))
# print(d)
# 
# x = 2
# y = 2
# e = ((y * 2) - (y * 1)) / ((x * 2) - (x *1))
# print(e)

'''
Study Unit 2 Activity 5
'''
# def main():
#     print("Program would calculate the cost per square inch of a circular pizza.")
#     print()
#     diameter = int(input("Enter the diameter of the pizza (in nearest inch): "))
#     price = float(input("Enter the price of the pizza: $"))
#     area = math.pi * (diameter/2)**2
# 
#     cost = price/area
#     
#     dollars = int(cost//1)
#     cents = cost % 1 * 100
#     centsR = round(cents)
#     
#     print()
#     print("The cost is", dollars, "dollars and", centsR ,"cents per square inch ")
# 
# 
# main()

'''
Study Unit 2 Activity 6
'''
#a
# for i in range(1, 11):
#     print(i * i)

#b
# for i in [1, 3, 5, 7, 9]:
#     print(i, ":", i**3)
#     print(i)

#c
# x = 2
# y = 10
# for j in range(0, y, x):
#     print(j, end="")
#     print(x + y)
#     print("done")
#     
#d
# ans = 0
# for i in range(1, 11):
#     ans = ans + i * i
#     print("i ", i)
#     print("ans ", ans)

# Num50cents = dollar/0.50
# 20centsValue = num20cents * 0.20

# print(‘’’She can’t
# Come ‘’’)
# print(‘I’m indeed surprised by Julie’s visit’)
# print(“Hurry! We’re ‘’’ late”)

# t = (1,2,3)
# print(t[-len(t) : -1])
# print(t[ : ])
# print(t[0: len(t)])

# aList = [1, 2, 3]
# print(aList[0] + aList[len(aList)])
# print(aList[0] = len(aList) )
# print(aList[ : ])
# print(2 * aList)

def main():
    print(1 + 2 * 0  - 1)
    print(5 // 2 -10 % 2 + 3)
    print( -5 % 3 + 2  * 1 / (-2))
    
main()








