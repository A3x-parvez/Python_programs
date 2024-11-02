import numpy as np
 
#creating 2d array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print("Dimention of array ",arr_2d.ndim)

#creatinf empty array
empty_array_2d = np.empty((3, 4))
print(empty_array_2d)

#array all eliment zero
arr1=np.zeros((2,3),dtype=int)
print(arr1)

#array all eliment one
arr2 = np.ones((3,5),dtype=int)
print(arr2)

#random number in array
arr3 = np.random.rand(5,5)
print(arr3)

# 3x3 identity matrix
identity_arr = np.eye(3,dtype=int) 
print(identity_arr)

#array with desire value
full_array_2d = np.full((2, 4), 7)
print(full_array_2d)


print(arr1.shape) # Returns a tuple indicating the array dimensions
print(arr1.dtype)  # Shows the data type of the elements in the array
print(arr2.size)  # Total number of elements in the array

