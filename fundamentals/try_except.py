# Try Except in Python
def add(x, y):
    return x + y

try:
    add("Test", ("Test", "Tuple"))
except NameError:
    print("Variable x is not defined.")
except:
    print("An exception occurred.")
finally:
    print("The try except is finished.")

# Raise an Exception
a = -1
if a < 0:
    raise Exception("Sorry, no numbers below zero.")