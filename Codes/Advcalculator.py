num1 = int(input ("Enter the First number: "))
op = input ("Enter the operator: ")
num2 = int(input ("Enter the second number: "))

if op == "+":
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "*":
    print (num1 * num2)
elif op == "/":
    print (num1 / num2)
else:
    print ("Invalid Operator")
