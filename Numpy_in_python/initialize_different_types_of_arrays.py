import numpy as np
#All zero matrix:
a =np.zeros((2,4) , dtype= "int16")
# a =np.zeros((2,4) )
print(a)
print(a.dtype)

b=np.ones((4,4), dtype = "int32")
print(b)

c= np.full((2,2), 33)
print(c)

# #Any other number (full_like)
d =np.full_like(a, 4)
print(d)

e = np.random.rand(1,4)
print(e)

f = np.random.randint(7, 10 , size =(3,3))
print(f)

#The identity matrix:
g = np.identity(4)
print(g)

#Example:
output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

# output[1: 4, 1:4] = z 
output[1: -1, 1:-1] = z 
print(output)


# Be careful while copying an arrays !!!
a =np.array([1,2,3])
b = a. copy()

b[0] =100

print(a)
# print(b)
