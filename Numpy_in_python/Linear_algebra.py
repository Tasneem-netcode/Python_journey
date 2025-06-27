import numpy as np
a =np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

c= np.matmul(a , b)
print(c)

print(c.dtype)


# find determinat of a matrix:
d = np.identity(3)
print(d)
deter =np.linalg.det(d)
print(deter)

#min and max :
stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.min(stats , axis= 1))

print(np.max(stats))
print(np.min(stats , axis= 0))

print(np.sum(stats))
print(np.sum(stats, axis = 1 ))