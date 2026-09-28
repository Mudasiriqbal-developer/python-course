# def calc_no(number):
#   if number % 2 == 0: 
#     print("Even Number: ", number)
#   else:
#     print("Odd Number: ", number)

# calc_no(9)

# def vowels(str):
#   count = 0

#   for character in str.lower():
#     if character in "aeiou":
#       count += 1
#   return count

# result = vowels("Toney Stark")
# result1 = vowels("Mudasir iqbal")
# print(result)
# print(result1)

# prime number 
# def prime_no(num):
#  if num <= 1:
#    print("Prime Number not found!")
#    return 

#  for i in range(2, num):
#    if(num % i == 0):
#     print("number is not found")
#     return 

#   print(num ": is prime")


# Everage of an list

def calc_averg(marks):
  if(len(marks) == 0):
    return

  average = sum(marks) / len(marks)
  return average

std_marks = [86, 90, 89, 87]

result = calc_averg(std_marks)

print(result)