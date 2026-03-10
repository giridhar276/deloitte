#
# you want to change the value of class variable : school_name
# this change should refelect across all existing and future instances of the class
# @classmethod operators on the class itself, not for individual instance.

# use @classmethod when you want to chaange or access class variables - variables that are shared by all instances



class School:
    school_name = "Green Valley High"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def change_school_name(cls, name):

        cls.school_name = name

student1 = School("John")
student2 = School("Jane")

print(student1.school_name)
print(student2.school_name)

School.change_school_name("Blue Ridge High")

print(student1.school_name)
print(student2.school_name)

