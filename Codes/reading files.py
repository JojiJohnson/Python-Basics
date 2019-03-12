# Reading files outside python file.

employee_file = open("employees.txt", "r")  # Different modes: r-read, w-write, a-append, 'r+' - read and write

print (employee_file.readable()) #checking if the file is readable.
#print (employee_file.readline())
#print (employee_file.readlines())
#print(employee_file.readlines()[1])         #different functions



for employee in employee_file.readlines():
    print(employee)

employee_file.close() # every opened files need to be closed.
