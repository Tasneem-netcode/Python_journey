import numpy as np 
a = np.array([[1,2,3,4,5,6], [8,6,9,2,4,3]])
dim = np.ndim(a)# to check dimention 
print(dim)
print(a)

#get a specific element [r,c]
print(a[1,5])

#get a specific row:
print(a[1,:])

#get a specific column :
print ("This is column ",a[: , 5])


#get slicing 
print(a[1, 1: -1:2])#row
print(a[0: , 4]) # col

#to change values :
a[1,5] = 70 
print(a)

# 3d array example :
b = np .array([[[1,2, 2], [3,4,4], [12,11,5]], [[4,6, 8], [7,8, 9] , [34,89,76]] , [[8,9,65] , [34,67,65], [56,87,33]]])
print(b)
print(np.ndim(b))
print(b[ 2 ,1, 2])
print(b[ 2 , 1 , 1])


# lis = [1,2,3,4,5]
# s = lis[::-1 ]
# print(s)