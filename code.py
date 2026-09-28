# <--------------- PART 1 ---------------->

# # output
# print("Hello Words")


# # Variables
# name = 'khan'
# age = 32
# cgpa = 3.44
# isStud = True


# # Inputs
# name = input("Enter Your Name: ")
# print("Salam! ", name)



# <--------------- PART 2 ---------------->

# Type Conversion & Type Casting

# # Type Casting is the conversion that the user change mennually the datatype like Exp.
# age = input('Enter Your Age: ')
# new_age = int(age) + 1
# print("Age: ",new_age)
# print(float(new_age))

# # Type Conversion is the conversion that the python do by defalt like.
# print(1 + 2.5) # the first value is 'int' and the 2nd value is 'float'. # Implicit
# print(1 + int(2.5)) # this is the type casting. # Explicit


# Sum program <= a , b => sum

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# sum = a + b

# print("Sum: ",sum)


# String operations

# name = "Tony stark"
# grade = 'A'

# print(name.upper()) # TONY STARK
# print(name) # Tony stark # this is called Immutible, (means don't change orignal str)


# find()
# print(name.find("ark")) # 0 index => position
# print(name.find("T")) # 0

# replace()
# print(name.replace("Tony stark", "Iron Man"))
# print(name.replace("stark", "Iron Man"))


# check for presence
# print("S" in name) # false
# print("T" in name) # True


# Operators 
# print(5 / 3) # 1.6666666666666667
# print(5 // 3) # 1
# print(5 * 3) # 15
# print(5 ** 3) # 125

# x = 2
# # x = x + 3
# x += 3
# print(x) # 5


# print((2 > 1) or (1 > 2)) # T or F => T
# print((2 > 1) and (1 > 2)) # T or F => F || T or T => T
# print(not (2 > 1)) # not T = F || not F = T



# Conditions

# age = 17

# # Indentation (profer sapcing before the next like its matter in the python)
# if age >= 18:
#   print("You are Adult")
#   print("You can drive / vote")
# elif age < 18:
#   print("You can't drive and vote")

# print("End of Code")




# # Grading

# marks = 60

# if marks >= 80:
#   print("Grade: A")
# elif marks < 80 and marks >= 60:
#   print("Grade: B")
# else:
#   print("Grade: C")


# # Range
# num = range(0, 5)
# print(num)

# # range(start, stop, step)


# # While Loop

# i = 5
# while i > 0:
#   print(i * "*")
#   i -= 1

# print("End of Code")


# For loop

# num = range(5) # 0 to 5
# for i in num:
#   print(i)


# for i in range(1, 6): # 1 to 5
#   print(i)

# even number

# for i in range(1, 11):
#   if i%2 == 0:
#     print(i)


# for i in range(2, 11, 2):
#   print(i)

# continue and breake key words

# for i in range(1, 51):
#   if(i == 21):
#     continue # it skip the value of 21 and print the remaining 
#     # break # it print the value upto 18 and will out from the loop and print the "End of loop".
#   if(i % 3 == 0):
#     print(i)

# print("End of code")


# part 4
# list

# marks = [98, 87, 89, 87, 87, 'A']

# print(marks, type(marks))

# # lengh of list
# print(len(marks))

# index
# print(marks[2])
# print(marks[-1]) # last index value when u don't now the last value index


# Sclicing a list

# print(marks[0:3])
# print(marks[-3:])

# for i in marks:
#   print(i)


# # append => add new value in the last of the list
# marks.append(50)
# print(marks)

# # insert => add new value on the specific location in the list
# marks.insert(1, 40)
# print(marks)

# print(98 in marks)

# clear the list
# marks.clear()
# print(marks)

# Tuple - immutable # its works like list but add some extra features

# marks = (98, 87, 89, 87, 87, 'A')

# print(marks.count(87))
# print(type(marks))


# set data type # its store the unique data.

# marks = {98, 97, 96, 95, 96, 95}

# print(len(marks))

# for i in marks:
#   print(i)


# Dictionary {key => value} like words meaning

# marks = {"math": 99, "phy": 98, "che":88}

# print(marks, type(marks))

# print(marks["phy"])

# marks["eng"] = 95

# print(marks["eng"])


# for key in marks:
#   print(key, marks[key])


# <--------- Part 4 --------------->

# Function

# def sum(a, b):
#   print(a + b)

# sum(123, 321)

# new_price +=  (price * 0.18)

# def calc_gst(price):
#   new_price = price + (price * 0.18)
#   print(new_price)

# calc_gst(100)
# calc_gst(1024)


# module function
# import math

# print(dir(math))

# from math import sqrt, log2

# print(log2(16))

import random

# print(random.random())
print(random.randint(1, 10))