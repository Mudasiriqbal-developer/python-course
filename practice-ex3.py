# Calculator

a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter op: ")

if op == '+':
  print(a + b)
elif op == '-':
  print(a - b)
elif op == '*':
  print(a * b)
elif op == '**':
  print(a ** b)
elif op == '/':
  print(a / b)
else:
  print("Invalid Operator")