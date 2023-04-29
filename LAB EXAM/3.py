import numpy as np
arr = np.random.randint(1,100,10)
mean_value = np.mean(arr)

greater_mean = arr[arr > mean_value]

print('Original array:', arr)
print('Mean value:', mean_value)
print('greater than mean:', greater_mean)
