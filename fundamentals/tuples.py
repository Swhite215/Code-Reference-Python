# Tuples in Python - Ordered and Unchangeable, Allows Duplicates

myTuple = (1, 2, 3)
print(myTuple)
print(len(myTuple))

# Create Tuple with One Item
thatTuple = ("apple",)
print(thatTuple)

# Access Tuples
print(myTuple[0])

if 3 in myTuple:
    print("3 is in my tuple!")

# Change Tuple Values - Tuple -> List: list() -> Modification -> Tuple: tuple()
x = (1,2,3)
y = list(x)
y[0] = 10
x = tuple(y)
print(x)

# Unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Loop Tuples
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[i])

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# Join Tuples
tuple3 = fruits + myTuple
print(tuple3)

tuple4 = fruits * 10
print(tuple4)