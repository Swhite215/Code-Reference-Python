# Classes in Python
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def print_info(self): # self is a reference to the current instance of the class, and is used to access variables that belongs to the class
        print("This vehicle is a " + self.make + " " + self.model + " in the color " + self.color)

car1 = Car("Ford", "Explorer", "Silver")
car1.print_info()

# Modify Properties
car1.make = "Toyota"
car1.model = "Camry"
car1.color = "Black"
car1.print_info()
