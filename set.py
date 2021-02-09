# Sets in Python - Unordered, Unchangeable, and Does Not Allow Duplicates
thisSet = {1, 2, 3}
print(thisSet)
print(len(thisSet))

# Access Set Items
for x in thisSet:
    print(x)

print(2 in thisSet)

# Add Set Items
thisSet.add(4)
thisSet.add(5)
print(thisSet)

anotherSet = {6,7,8,9,10}
thisSet.update(anotherSet)
print(thisSet)

# Remove Set Items
thisSet.remove(10)
thisSet.discard(9)
print(thisSet)

# Join Sets
unionSet = anotherSet.union(thisSet)
print(unionSet)

intersectionSet = anotherSet.intersection({6,8,10, 11})
print(intersectionSet)

differenceSet = anotherSet.symmetric_difference({12, 11, 8, 6, 7, 9, 30})
print(differenceSet)

# Clear the Set
thisSet.clear()
print(thisSet)