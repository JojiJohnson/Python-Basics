# Try except blocks are used when the user enters an unexpected input.

# number = int(input ("Enter a number: "))
# print (number)

# here an error occurs when the user enters something other than number

'''



try:
    number = int(input ("Enter a number: "))
    print (number)
except:
    print ("Invalid input!")

'''

# But this takes every errors happening inside the try block.

#eg:

try:
    value = 10/0                                    # division by zero will be an error
    number = int(input ("Enter a number: "))
    print (number)
except ZeroDivisionError:
    print ("Division by Zero")
except ValueError:
    print ("Invalid input")

# To print directly the error
'''
try:
    value = 10/0                                    # division by zero will be an error
    number = int(input ("Enter a number: "))
    print (number)
except ZeroDivisionError as err:   
    print (err)
except ValueError:
    print ("Invalid input")

'''