#1)1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np
null_vector = np.zeros(10)  # Create a null vector of size 10
null_vector[4] = 1  # Set the fifth value to 1 (remember, array indexing starts from 0)
print(null_vector)

#2)Create a vector with values ranging from 10 to 49.

import numpy as np
vector = np.arange(10, 50)
print(vector)

#3)Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
matrix = np.arange(9).reshape(3, 3)
print(matrix)

#4)Find indices of non-zero elements from [1,2,0,0,4,0]
import numpy as np
arr = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(arr)
print(indices)

#5)Create a 10x10 array with random values and find the minimum and maximum values.
import numpy as np
array = np.random.random((10, 10))
minimum_value = np.min(array)
maximum_value = np.max(array)
print("Minimum value:", minimum_value)
print("Maximum value:", maximum_value)

#6)Create a random vector of size 30 and find the mean value.
import numpy as np
vector = np.random.random(30)
mean_value = np.mean(vector)
print("Mean value:", mean_value)


