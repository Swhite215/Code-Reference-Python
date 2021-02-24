import numpy as np

# Create Array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)

# Dimensions 0-D Arrays - Scalar - Each Element
scalar = np.array(42)
print(scalar)

# Dimensions 1-D Arrays - Uni-Dimensional - Most Common
arr3 = np.array([1,2,3])

# Dimensions 2-D Arrays - Matrix or 2nd Order Tensors
arr4 = np.array([[1,2,3], [4,5,6]])
print(arr4)

# Dimensions 3-D Arrays - 3rd Order Tensors
arr5 = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])
print(arr5)

# Check Dimensions
print(scalar.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)

# Indexing - 1-D Array
print(arr3[0])

# Indexing - 2-D Array
print(arr4[1][1])

# Indexing - 3-D Array
print(arr5[0][1][2])

# Array Slicing
print(arr3[:2])

arr6 = np.array([1,2,3,4,5,6,7])
print(arr[0::2])

print(arr4[1, :3])

# Data Type
print(arr3.dtype)

# Create with Data Type
arr7 = np.array([1,2,3,4], dtype='i')
print(arr7)
print(arr7.dtype)

# Create New Array with New DataType From Existing Array
arr8 = arr7.astype('S')
print(arr8)

# Copy Array
arr9 = arr7.copy()
arr9[0] = 42
print(arr7)
print(arr9)

# Array Shape
print(arr9.shape)
print(arr4.shape)
print(arr5.shape)

# Array Reshape - add/remove dimensions or change number of elements in each dimension
arr10 = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # 1-D with 12 elements
arr11 = arr10.reshape(4,3) # 2-D with 4 arrays each with 3 elements
print(arr11)

arr12 = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # 1-D with 12 elements
arr13 = arr12.reshape(2,3,2) # 3-D with 2 arrays each with 3 arrays of two elements
print(arr13)

# Array Flattening
arr14 = arr13.reshape(-1)
print(arr14)

# Array Iterating - Normal
for x in arr10:
    print(x)

for x in arr11:
    for y in x:
        print(y)

for x in arr13:
    for y in x:
        for z in y:
            print(z)

# Array Iterating - nditer() - Each Scalar Element
for x in np.nditer(arr11):
    print(x)

for x in np.nditer(arr13):
    print(x)

for x in np.nditer(arr11, flags=['buffered'], op_dtypes=['S']):
    print(x)

for x in np.nditer(arr11[:, ::2]):
    print(x)

# Joining Arrays - Concatenating
arr15 = np.array([1,2,3])
arr16 = np.array([4,5,6])
arr17 = np.concatenate((arr15, arr16))
print(arr17)

arr18 = np.array([[1,2], [3,4]])
arr19 = np.array([[5,6], [7,8]])
arr20 = np.concatenate((arr18, arr19), axis=0) # Keep Current Size of Array Chunks
arr21 = np.concatenate((arr18, arr19), axis=1) # Chunk Together Array Chunks
print(arr20)
print(arr21)

# Joining Arrays - Stacking
arr22 = np.stack((arr15, arr16), axis=0) # Stack on Top Keep Size
arr23 = np.stack((arr15, arr16), axis=1) # Stack Along Opposite Axis
print(arr22)
print(arr23)

arr24 = np.hstack((arr15, arr16)) # Stack Along Rows
print(arr24)

arr25 = np.vstack((arr15, arr16)) # Stack Along Columns
print(arr25)

# Splitting Arrays
arr26 = np.array_split(arr10, 5)
print(arr26) # Array Containing Five Arrays

arr27 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr28 = np.array_split(arr27, 3) # Array Containing 3 Arrays with 2 Arrays in Each
print(arr28)

# Searching Arrays
arr29 = np.array([1,2,3,4,4,5])
x = np.where(arr29 == 4) # Array of Indices Where Value is 4
print(x)

y = np.where(arr29 % 2 == 0) # Array of Indices Where Value is Even
print(y)

# Sorting Arrays
arr30 = np.array([1,9,34,45,65,23,45,7,6,23,45,8,9,677,45])
print(np.sort(arr30))

# Filter Arrays
arr31 = np.array([1,2,3,4])
booleanIndexList = [True, False, True, False]
arr32 = arr31[booleanIndexList]
print(arr32)

filter_arr = []
for element in arr30:
    if element > 10:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

arr33 = arr30[filter_arr]
print(arr33)

second_filter_arr = arr30 > 10;
arr34 = arr30[second_filter_arr]
print(arr34)