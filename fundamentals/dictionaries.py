# Dictionaries in Python - Ordered and Changeable, Allows Duplicates
carDict = {
    "brand": "Ford",
    "model": "F-150",
    "year": 2021,
    "color": "red",
    "owned": True
}

print(carDict)
print(carDict["owned"])
print(len(carDict))

# Access Items
x = carDict["brand"]
y = carDict.get("year")
print(x)
print(y)

dictKeys = carDict.keys()
print(dictKeys)

dictValues = carDict.values()
print(dictValues)

dictItems = carDict.items()
print(dictItems)

if "color" in carDict:
    print("Color is one of the keys in my carDict")

# Change Items
carDict["year"] = 2022
carDict.update({"color": "blue"})
print(carDict)

# Add Items
carDict["location"] = "Garage"
carDict.update({"radio": "XM"})
print(carDict)

# Remove Items
carDict.pop("radio")
print(carDict)

del carDict["location"]
print(carDict)

# Loop Dictionaries - Keys
for x in carDict:
    print(x)

# Loop Dictionaries - Values
for x in carDict:
    print(carDict[x])

# Loop Dictionaries - Items
for key, value in carDict.items():
    print(key, value)

# Copy Dictionaries
newDict = carDict.copy()
anotherDict = dict(carDict)

# Nested Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myFamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myFamily)

# Clear Dictionary
carDict.clear()
print(carDict)