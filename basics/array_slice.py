import numpy as np

# Slicing 1-D arrays is similar to slicing normal Python lists

# For 2-D arrays, this is how it is done

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# From the second element slice elements from index 1 to index 4
print(arr[1, 1:4])


# From both elements, return index 2
print(arr[0:2, 2])

# From both elements slice index 1 to index 4(not included)
print(arr[0:2, 1:4])
