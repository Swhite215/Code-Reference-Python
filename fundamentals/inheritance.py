# Inheritance in Python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        self.graduationyear = 2019

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

person1 = Person("Spencer", "White")
person1.print_name()

student1 = Student("Caitlin", "Fleming")
student1.welcome()