# Operators in Python
sum = 1 + 2
difference = 10 -1
product = 12 * 9
quotient = 100 / 5

# Assignment Operators
x = 10
x += 1
x -= 1
x *= 10
x /= 10
x **= 3

# Comparison Operators
print(9 == 0)
print(9 != 7)
print(9 > 1)
print(9 < 10)
print(9 >= 6)
print(9 <= 100)

# Logical Operators
print(x > 5 and x < 20)
print(x > 5 or x < 20)
print(not(x < 5 and x > 20))

# Identity Operators
myDict = dict(name="Spencer", age=27)
yourDict = dict(name="Spencer", age=27)

print(myDict is yourDict)
print(myDict is not yourDict)

# Membership Operators
s = ["apple", "banana"]
print("banana" in s)
print("orange" not in s)

# Bitwise Operators
bitOne = 1
bitTwo = 0
print(bitOne & bitTwo) # sets to 0 because both are not 1
print(bitOne | bitTwo) # sets to 1 because bitOne is 1
print(bitOne ^ bitTwo) # sets to 1
print(~bitOne)
print(bitOne<<10)
print(bitOne>>10)