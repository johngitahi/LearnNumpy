import numpy as np

# When the array is created, you can define the number of dimensions by using the ndmin argument

arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr)
print('Number of dimensions :',arr.ndim)


