#Comparison operators <, >, <=, >=, != etc..

print("Comparing nos")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 401 , 7))

print("Comparing Strings")

def equal_str(str1, str2):
    if str1 == str2:
        return "Equal Strings"
    else:
        return "Unequal Strings"

print (equal_str("dog", "dog"))



