# Lists in Python - Ordered and Changeable, Allows Duplicates
myList = ["apples", "banana", "cherry"]

print(myList)
print(len(myList))

# Access List Items
print(myList[0])
print(myList[:2])

if "cherry" in myList:
    print("Yes, cherry is in the fruits list!")

# Change List Items
myList[1] = "orange"
print(myList)

myList[:2] = ["blackberry", "raspberry"]
print(myList)

myList.insert(2, "strawberry")
print(myList)

# Add List Items
myList.append("apples")
myList.append("banana")

thatList = ["mango", "pineapple", "papaya"]
myList.extend(thatList)
print(myList)

myTuple = ("kiwi", "watermelon")
myList.extend(myTuple)
print(myList)

# Remove List Items
myList.append("banana")
print(myList)

myList.pop(4)
print(myList)

myList.pop()
print(myList)

# Loop through List
for x in myList:
    print(x)

for i in range(len(myList)):
    print(myList[i])

i = 0
while i < len(myList):
    print(myList[i])
    i = i + 1

# List Comprehension
[print(x) for x in myList]

newList = [x for x in myList if "a" in x]
print(newList)

# Sort Lists - Alphanumerically
myList.sort()
print(myList)

# Sort Lists - Descending
myList.sort(reverse = True)
print(myList)

# Customn Sort Function
def myFunc(n):
    return abs(n - 50)

thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myFunc)
print(thisList)

# Reverse
myList.reverse()
print(myList)

# Copy Lists
anotherList = myList.copy()
anotherList.append("pomegranate")

extraList = list(myList)
extraList.pop()

print(anotherList)
print(extraList)

# Join List
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

extraList.extend(list2)
print(extraList)

# Clear the List
myList.clear()
print(myList)