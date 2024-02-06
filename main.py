num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
smooth_operator = input("Enter an operator, tough guy: ")

if smooth_operator =="+":
  total = num1+num2
  print(f"{num1} + {num2} = {total}")

if smooth_operator =="-":
  total = num1-num2
  print(f"{num1} - {num2} = {total}")

if smooth_operator =="*":
  total = num1*num2
  print(f"{num1} * {num2} = {total}")

if smooth_operator == '/' and num2 == 0:
  print("NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO")
else:
  total = num1 * num2
  print(f"{num1} / {num2} = {total}")

if smooth_operator =="/":
  total = num1/num2
  print(f"{num1} / {num2} = {total}")

if smooth_operator not in ['+', '-', '*', '/']:
  print("wrong operator.")


