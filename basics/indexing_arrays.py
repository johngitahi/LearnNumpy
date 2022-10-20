import numpy as np

arr = np.array([1, 2, 3, 4])

# Return 2
print(arr[1])


# Access 2-D arrays
arr2 = np.array([[1,2,3,4], [5,6,7,8]])

# Return 2
print('2nd element on 1st row is: ', arr2[0, 1])

# Access 3-D arrays
arr3 = np.array([[[10,20,30], [40,50,60]], [[11,21,31],[41,51,61]]])

# Return the third element of the second array of the first array: 60
print(arr3[0, 1, 2])

# Negative indexing
# Print the last element from the 2nd dimension of arr2
# Return 8
print(arr2[1, -1])
