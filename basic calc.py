op = input("enter operator: ")
num1 = float(input("enter a num: "))
num2 = float(input("enter another num: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
  print("invalid operator")