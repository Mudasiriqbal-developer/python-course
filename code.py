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