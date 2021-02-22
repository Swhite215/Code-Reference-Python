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