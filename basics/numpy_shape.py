import numpy as np

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('Shape of array: ', arr.shape)

# Output:
#       Shape of array: (1,1,1,1,4)
#
# This means that the array has five dimensions
# Thee first dimension has one element the second has one ... and the fifth # has four elements.
