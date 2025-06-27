import numpy as np
before =np.array([[1,2,3,4], [6,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)

#vertically stacking vectors : it stacks arrays on top of each other, row-wise.

v1 = np.array([1,2,3,4])
v2 = np.array([6,7,8,9])

v = np.vstack([v1 , v2 , v1 , v2 ])
print(v)

#horizontal stack vector: Horizontal Stack — it stacks arrays side by side, column-wise
h1 = np.array([1,2,3])
h2 = np.array([4,5,6])

result = np.hstack((h1 , h2))
print(result)