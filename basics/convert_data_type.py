# the astype() method allows you to change the data type of an existing array by creating a copy of the array

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
