# Numpy has some extra data types which are referenced using one character
# Example: i for integer, u for unsigned integer, m for timedelta

# Check the data types of an array with the dtype property of the Numpy array object

import numpy as np

arr = np.array(['apple', 'banana', 'apricot'])


print(arr.dtype)

# Creating arrays with a defined data type

'''The array function takes an optional argument dtype that allows for the explicit definition of the data types of the array elements'''

arr2 = np.array([1,2,3,4], dtype='S')

print(arr2)

# For i, u, f, S and U we can define size as well.

# Create an array with data type 4 bytes integer

arr3 = np.array([1,2,4,5], dtype='i4')

print(arr3) 
