import numpy as np

"""1. Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it."""


arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Array:")
print(arr_2d)


print("\nndim:", arr_2d.ndim)


print("shape:", arr_2d.shape)


print("\nFirst row:", arr_2d[0, :])
print("First column:", arr_2d[:, 0])
print("Sub-matrix (top-left 2x2):\n", arr_2d[0:2, 0:2])




"""2. Create one dimensional array and perform ndim, shape, reshape operation on it."""

arr_1d = np.array([10, 20, 30, 40, 50, 60])

print("Array:", arr_1d)


print("\nndim:", arr_1d.ndim)


print("shape:", arr_1d.shape)


reshaped_arr = arr_1d.reshape(2, 3)
print("\nReshaped to 2x3:\n", reshaped_arr)
