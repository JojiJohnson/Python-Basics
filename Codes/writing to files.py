employee_file = open("employees.txt", "a")  # append

employee_file.write("\nJoji - Hello 4 added now")

employee_file.close()

# Here if mode is now given as 'w', the entire file will be overwritten.

employee_file = open("employee1.txt", "w") #this creates a new file.
