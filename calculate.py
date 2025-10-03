try:
  num_1 = int(input("Enter first number:"))
  num_2 = int(input("Enter second number:"))

  print("Choose calculation to perform: \n",
  "1. add\n",
  "2. substract\n",
  "3. multiply\n",
  "4. divide\n")
  
  cal = input().strip().lower()

  if cal == "add":
    ans = num_1 + num_2
  elif cal == "substract":
    ans = num_1 - num_2
  elif cal == "multiply":
    ans = num_1 * num_2
  elif cal == "divide":
    if num_2 == 0:
      print("Error! can't be divided by zero:")
      ans = None
    else:
      ans = num_1 / num_2
  else:
    print("Invalid operation")
    ans = None
        
  if ans is not None:
    print("The answer is :", ans)
    ans = None

except ValueError:
  print("Invalid input! please enter valid number")
