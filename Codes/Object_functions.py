# putting functions inside class in order to acces by the objects.
# Writing a function in the class in file 'Classes_and_objects.py'.

from Classes_and_objects import Student

Student1 = Student ("Jos", "ECE", 3.2, True)
Student2 = Student ("Mike", "EEE", 6.99, False)

print (Student1.name)
print (Student2.gpa)                # accessing individual data


print (Student1.on_honor_roll())

print (Student2.on_honor_roll())

