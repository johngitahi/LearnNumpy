import numpy as np

# Creating a 0-D array
arr = np.array(30)
print(arr)

# Creating a 1-D array
arr2 = np.array([10, 20])
print(arr2)

# Creating a 2-D array
arr3 = np.array([[10, 20], [30, 40]])
print(arr3)

# Creating a 3-D array
arr4 = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
print(arr4)

# Check how many dimensions an array has with the ndim attribute
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
