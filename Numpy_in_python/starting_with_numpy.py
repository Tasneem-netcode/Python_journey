import numpy as np

my_list = [1,2,3]
my_array = np.array([1,2,3])
my_array2 = np.array([1,3,6])

print(type(my_array))
print(type(my_list))

print(my_array * my_array2)


#use a tuple to create a numpy array :
arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))


import numpy as np

# 1d array
a = np.array([1, 2, 3])  
print(type(a))  # <class 'numpy.ndarray'>


#2 dimentional array :
b = np.array([[3.2, 5.9, 1.2 , 7.8], [3.7, 8.0 , 1.7 , 6.7]])
print(b)

# How to get the dimentions of array  in numpy :
print(a.ndim)
print(b.ndim)

# to get the shape of array :
print(a.shape)
print(b.shape)

#datatype of array:
print(a.dtype)
print(b.dtype)


# we can also assign datatypes into this :
a = np.array([1, 2, 64] , dtype='int16')  
print(a)
print(a.dtype)
print(a.itemsize)
print(b.itemsize)


# get total size :
# a.size * a.itemsize
# print(a.size ) * print(a.itemsize)
print(a.nbytes)