# python .\practice-ex5.py

# list

# roll_no = {101, 102, 105, 101, 108, 105, 108}

# for i in roll_no:
#   print(i)

# tople

employees = [
  (101, "Alice", 50000),
  (102, "Bob", 65000),
  (103, "Charlie", 70000)
]

search_id = int(input("Enter Employee ID: "))
found = False

for employee in employees:
  employee_id = employee[0]

  if(employee_id == search_id):
    print("Employee found!")
    print("Employee ID: ", employee[0])
    print("Employee Name: ", employee[1])
    print("Salery: ", employee[2])
    found = True
    break 
    
if found == False:
  print("Employee ID not found")
