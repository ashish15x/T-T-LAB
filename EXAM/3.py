import numpy as np

# create 1D array of random values
arr = np.random.rand(10)

# calculate mean value
mean = np.mean(arr)

# filter out values less than or equal to the mean
filtered_arr = arr[arr > mean]

# output results
print("Original array:", arr)
print("Mean value:", mean)
print("Filtered array (values greater