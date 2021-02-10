a = 10
b = 11

# Conditional
if a > 10:
    print("A greater than 10")
elif a == 10:
    print("A is equal to 10")
else:
    print("A is less than 10")

# Short Hand
if b >= 11: print("B is greater than or equal to 11")

# Short Hand
print("A") if a > b else print("B")

i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i = i + 1

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for char in fruits[1]:
    print(char)

for x in range(len(fruits)):
    print(fruits[x])

for x in range(2,6):
    print(x)

for x in range(0,100,10):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finished Looping...")