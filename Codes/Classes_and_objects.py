
# With ckasses we can define our own datatypes.
# class is like anoverall template.
# Object is an instance of a class.
# Now making a student datatype.

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# This student datatype is used in the next file named as 'Studentsdata'.

    def on_honor_roll(self):                        # Object function.
        if self.gpa >= 3.5:
            return True
        else:
            return False
